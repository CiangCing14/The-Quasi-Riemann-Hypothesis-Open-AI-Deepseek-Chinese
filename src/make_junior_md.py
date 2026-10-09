#!/usr/bin/env python3
"""Turn the junior-high explainer HTML (in build_junior.py) into correct Markdown."""
import os, re, sys, importlib.util
from html.parser import HTMLParser

ROOT = '/home/a/Downloads/25'
OUT_MD = os.path.join(ROOT, 'Junior High School', 'paper-junior.md')

spec = importlib.util.spec_from_file_location('bj', os.path.join(ROOT, 'build_junior.py'))
bj = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bj)
MATHS, CONTENT = bj.MATHS, bj.CONTENT


class Node:
    def __init__(self, tag=None, attrs=None, text=''):
        self.tag, self.attrs, self.text = tag, dict(attrs or []), text
        self.children = []

    def cls(self):
        return self.attrs.get('class', '')


class P(HTMLParser):
    VOID = {'br', 'hr', 'img'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('root')
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        self.stack[-1].children.append(n)
        if tag not in self.VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if data.strip():
            self.stack[-1].children.append(Node(None, None, data))


def inline(node):
    out = []
    for ch in node.children:
        if ch.tag is None:
            out.append(re.sub(r'\s+', ' ', ch.text))
        elif ch.tag == 'b':
            out.append('**%s**' % inline(ch).strip())
        elif ch.tag == 'br':
            out.append(' ')
        elif ch.tag == 'sup':
            out.append('<sup>%s</sup>' % inline(ch).strip())
        else:
            out.append(inline(ch))
    return re.sub(r'[ \t]{2,}', ' ', ''.join(out)).strip()


def table_md(node):
    rows = []
    for tr in node.children:
        if tr.tag != 'tr':
            continue
        cells = [inline(td) for td in tr.children if td.tag == 'td']
        if cells:
            rows.append(cells)
    if not rows:
        return ''
    out = ['| 术语 | 解释 |', '| --- | --- |']
    out += ['| %s | %s |' % (r[0], r[1]) for r in rows]
    return '\n'.join(out)


def lines_of(node):
    """Yield the node's content split into lines at <br>."""
    lines, cur = [], []
    for ch in node.children:
        if ch.tag is None:
            cur.append(re.sub(r'\s+', ' ', ch.text))
        elif ch.tag == 'br':
            lines.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(inline(ch))
    lines.append(''.join(cur).strip())
    return [x for x in lines if x]


def emit(node, out):
    for ch in node.children:
        cls = ch.cls()
        if ch.tag == 'div' and 'cover' in cls:
            title = sub = kicker = ''
            meta = []
            for k in ch.children:
                if k.tag == 'h1':
                    t = ''.join(lines_of(k))
                    t = re.sub(r'([\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])', r'\1', t)
                    title = re.sub(r'([，。、：；])\s+', r'\1', t)
                elif k.tag == 'div' and 'sub' in k.cls():
                    sub = inline(k)
                elif k.tag == 'div' and 'kicker' in k.cls():
                    kicker = inline(k)
                elif k.tag == 'div' and 'meta' in k.cls():
                    meta = lines_of(k)
            out.append('# %s' % title)
            if kicker:
                out.append('*%s*' % kicker)
            if sub:
                out.append('**%s**' % sub)
            for m in meta:
                out.append(m)
        elif ch.tag == 'h2':
            out.append('## %s' % inline(ch))
        elif ch.tag == 'h3':
            out.append('### %s' % inline(ch))
        elif ch.tag == 'p':
            out.append(inline(ch))
        elif ch.tag == 'ul':
            items = [inline(li) for li in ch.children if li.tag == 'li']
            out.append('\n'.join('- %s' % i for i in items))
        elif ch.tag == 'div' and ('note' in cls or 'warn' in cls):
            body = re.sub(r'\s+', ' ', inline(ch)).strip()
            out.append('> %s' % body)
        elif ch.tag == 'div' and 'eq' in cls:
            key = re.search(r'\{\{m:(\w+)\}\}', ''.join(
                c.text for c in ch.children if c.tag is None)).group(1)
            out.append('$$\n%s\n$$' % MATHS[key].strip())
        elif ch.tag == 'table':
            md = table_md(ch)
            if md:
                out.append(md)
        elif ch.tag in ('div',):
            emit(ch, out)


parser = P()
parser.feed(CONTENT)
pieces = []
emit(parser.root, pieces)
doc = '\n\n'.join(p for p in pieces if p.strip()) + '\n'
open(OUT_MD, 'w', encoding='utf-8').write(doc)

# ---- checks ----
d = open(OUT_MD, encoding='utf-8').read()
lines = d.split('\n')
print('written:', OUT_MD)
print('bytes/words:', len(d.encode()), '/', len(re.sub(r'\s', '', d)))
print('h1/h2/h3:', len([l for l in lines if l.startswith('# ')]),
      len([l for l in lines if l.startswith('## ')]),
      len([l for l in lines if l.startswith('### ')]))
print('list items:', len([l for l in lines if l.startswith('- ')]),
      '| blockquotes:', len([l for l in lines if l.startswith('> ')]))
print('$$ fences:', len([l for l in lines if l.strip() == '$$']),
      '| table rows:', len([l for l in lines if l.startswith('| ')]))
print('4-space indent lines:', len([l for l in lines if l.startswith('    ')]))
odd = [i + 1 for i, l in enumerate(lines) if len(re.findall(r'(?<!\$)\$(?!\$)', l)) % 2]
print('unbalanced inline $:', len(odd))
print('unresolved placeholders:', d.count('{{m:'))
try:
    import markdown
    hh = markdown.markdown(d, extensions=['tables'])
    print('rendered html chars:', len(hh), '| <pre> blocks:', hh.count('<pre>'),
          '| <table>:', hh.count('<table>'), '| <blockquote>:', hh.count('<blockquote>'))
except Exception as e:
    print('markdown lib not used:', e)
print('--- head ---')
print('\n'.join(lines[:14]))
