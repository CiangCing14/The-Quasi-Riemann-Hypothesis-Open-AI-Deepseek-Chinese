#!/usr/bin/env python3
"""Assemble the translated pages into one correct Markdown document.

- section titles become markdown headings (level = numbering depth)
- the table of contents becomes a nested markdown list (page numbers kept)
- bibliography entries are separate paragraphs
- display maths ($$...$$) is lifted onto its own paragraph, inline maths kept
- dot leaders / stray page numbers are dropped
"""
import re, glob, os

ROOT = '/home/a/Downloads/25'
OUTD = os.path.join(ROOT, 'out')
DST = os.path.join(ROOT, 'paper-zh-cn.md')

HEAD_LINE = re.compile(r'^(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(\S.{0,32})$')
DOTS_ONLY = re.compile(r'^[ \u3000]*[.．·][.．·\u3000 ]*$')
BARE_NUM = re.compile(r'^\s*(\d{1,3})\s*$')
REF_LINE = re.compile(r'^\s*\[\d+\]\s')
E_DOTS = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(.+?)'
                    r'[ \u3000]*((?:[.．·][ \u3000]*){3,})[ \u3000]*(\d{1,3})?[ \u3000]*$')
E_PLAIN = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(\S.*?)'
                     r'[ \u3000]+(\d{1,3})[ \u3000]*$')
DISPLAY = re.compile(r'\$\$(.+?)\$\$|\\\[(.+?)\\\]', re.S)


def cjk(s):
    return len(re.findall(r'[\u4e00-\u9fff]', s))


def toc_entry(ln):
    m = E_DOTS.match(ln)
    if m:
        t = m.group(3).strip().rstrip(' .．·')
        return (m.group(2), t, m.group(5)) if cjk(t) >= 2 else None
    m = E_PLAIN.match(ln)
    if m:
        t = m.group(3).strip()
        return (m.group(2), t, m.group(4)) if cjk(t) >= 2 and not re.search(r'[。，；：]', t) else None
    return None


def is_toc_page(text):
    return ('目录' in text) or sum(1 for ln in text.split('\n') if toc_entry(ln)) >= 4


def is_bib_page(text):
    return sum(1 for ln in text.split('\n') if REF_LINE.match(ln)) >= 3


def head_level(ln):
    m = HEAD_LINE.match(ln.strip())
    if not m:
        return None
    num, title = m.group(1), m.group(2)
    if re.search(r'[。，；：！？]', title) or title.endswith('的'):
        return None
    if cjk(title) < 2 or re.search(r'[$\\{}^_=<>|]', title):
        return None
    return min((1 if '.' not in num else num.count('.') + 1), 4)


def clean_lines(text):
    out = []
    for ln in text.split('\n'):
        s = ln.strip()
        if s and DOTS_ONLY.match(s):
            continue
        if BARE_NUM.match(s):
            continue
        # leading whitespace from the PDF layout must go: 4+ spaces would become a code block
        out.append(re.sub(r'^#{1,6}\s*', '', ln).replace('**', '').strip())
    return out


INLINE_HEAD = re.compile(r'^(\d+(?:\.\d+)*)[ \u3000]+(\S[^\s]{0,23})((?:[ \u3000]+\S.*)?)$')
CONT = set('中的所给是在与对为此其该这若令设由从当把即而也则便故因如把按于第')
TOC_TITLES = []


def load_toc_titles():
    out = []
    for p in sorted(glob.glob(os.path.join(OUTD, 'page_*.zh.md')))[:6]:
        t = open(p, encoding='utf-8').read()
        if not is_toc_page(t):
            continue
        for ln in t.split('\n'):
            e = toc_entry(ln)
            if e:
                out.append(e)
    return sorted(out, key=lambda e: -len(e[1]))


def match_toc_title(block):
    for num, title, _ in TOC_TITLES:
        full = num + ' ' + title
        if block.startswith(full):
            rest = block[len(full):]
            if rest[:1] in (' ', '\u3000') or (rest[:1] and '\u4e00' <= rest[:1] <= '\u9fff'):
                return num, title, rest.strip()
    return None


def split_inline_head(block):
    """Split '6.2 平衡低估计 对于平衡估计，…' into a heading plus the rest."""
    m = INLINE_HEAD.match(block)
    if not m:
        return None, block
    num, title, rest = m.group(1), m.group(2), (m.group(3) or '').strip()
    if not rest or cjk(title) < 2 or re.search(r'[。，；：！？]', title):
        return None, block
    if title[0] in CONT or re.search(r'[$\\{}^_=<>|]', title):
        return None, block
    # keep appending tokens while they still read like part of the title
    while rest:
        tok, _, tail = rest.partition(' ')
        if not tok or len(title) + len(tok) > 30 or re.search(r'[。，；：！？]$', tok):
            break
        if cjk(tok) == 0 and re.search(r'[。，；：！？]', tail[:1]):
            break
        title += ' ' + tok
        rest = tail.strip()
        if len(tail.strip()) < 6:
            break
    return num, rest


def lift_display(block):
    """Put every $$...$$ onto its own paragraph inside a block of text."""
    parts = []
    pos = 0
    for m in DISPLAY.finditer(block):
        seg = m.group(1) if m.group(1) is not None else m.group(2)
        before = block[pos:m.start()].strip()
        if before:
            parts.append(before)
        parts.append('$$\n%s\n$$' % seg.strip())
        pos = m.end()
    tail = block[pos:].strip()
    if tail:
        parts.append(tail)
    return parts


def convert(text):
    toc_page = is_toc_page(text)
    bib_page = is_bib_page(text)
    lines = clean_lines(text)
    blocks = [b.strip() for b in re.split(r'\n\s*\n', '\n'.join(lines)) if b.strip()]
    pieces = []
    for b in blocks:
        one = [l.strip() for l in b.split('\n') if l.strip()]
        if not one:
            continue
        if toc_page and all(toc_entry(l) for l in one):
            for l in one:
                num, title, page = toc_entry(l)
                lvl = 1 if '.' not in num else min(num.count('.') + 1, 3)
                pieces.append('%s- %s %s%s' % ('  ' * (lvl - 1), num, title, (' ' + page) if page else ''))
            continue
        if bib_page and len(one) == 1 and REF_LINE.match(one[0]):
            pieces.append(one[0])
            continue
        first = one[0]
        # 1) the first line is a complete section title
        lvl = head_level(first)
        if not lvl:
            t = match_toc_title(first)
            if t and not t[2]:
                lvl = min((1 if '.' not in t[0] else t[0].count('.') + 1), 4)
                first = '%s %s' % (t[0], t[1])
        if lvl:
            pieces.append('%s %s' % ('#' * (lvl + 1), re.sub(r'\s+', ' ', first)))
            if one[1:]:
                pieces.extend(lift_display('\n'.join(one[1:])))
            continue
        if first in ('摘要', '目录', '參考文獻', '参考文献', '符号说明', '记号'):
            pieces.append('## %s' % first)
            if one[1:]:
                pieces.extend(lift_display('\n'.join(one[1:])))
            continue
        # 2) title glued to the following sentence on one line
        t = match_toc_title(b)
        if t:
            num, title, rest = t
            lvl = min((1 if '.' not in num else num.count('.') + 1), 4)
            pieces.append('%s %s %s' % ('#' * (lvl + 1), num, re.sub(r'\s+', ' ', title)))
            one = ([rest] if rest else []) + one[1:]
            pieces.extend(lift_display('\n'.join(one)))
            continue
        num, rest = split_inline_head(b)
        if num:
            lvl = min((1 if '.' not in num else num.count('.') + 1), 4)
            head = b.strip()[:len(b.strip()) - len(rest)].strip()
            pieces.append('%s %s' % ('#' * (lvl + 1), re.sub(r'\s+', ' ', head)))
            one = ([rest] if rest else []) + one[1:]
            pieces.extend(lift_display('\n'.join(one)))
            continue
        pieces.extend(lift_display('\n'.join(one)))
    return '\n\n'.join(p for p in pieces if p.strip())


TOC_TITLES = load_toc_titles()
print('toc titles loaded:', len(TOC_TITLES))
pages = sorted(glob.glob(os.path.join(OUTD, 'page_*.zh.md')))
parts = []
for p in pages:
    t = open(p, encoding='utf-8').read().strip()
    if not t:
        continue
    c = convert(t)
    if c.strip():
        parts.append(c)

doc = '\n\n'.join(parts)
# keep consecutive TOC list items tight (one block, no blank lines between them)
doc = re.sub(r'(^[ \u3000]*- .*)\n\n(?=[ \u3000]*- )', r'\1\n', doc, flags=re.M)
doc = re.sub(r'\n{3,}', '\n\n', doc).strip() + '\n'
open(DST, 'w', encoding='utf-8').write(doc)

# ---- self checks ----
d = open(DST, encoding='utf-8').read()
lines = d.split('\n')
heads = [l for l in lines if re.match(r'^#{1,4} ', l)]
toc_items = [l for l in lines if re.match(r'^\s*- ', l)]
disp = len(re.findall(r'^\$\$$', d, re.M))
refs = [l for l in lines if REF_LINE.match(l)]
dollar_odd = [i + 1 for i, l in enumerate(lines)
              if len(re.findall(r'(?<!\$)\$(?!\$)', l)) % 2]
print('written          :', DST)
print('bytes / lines    : %d / %d' % (len(d.encode()), len(lines)))
print('headings         :', len(heads), '| toc list items:', len(toc_items))
print('display $$ fences:', disp, '| reference paras:', len(refs))
print('dot-leader runs  :', len(re.findall(r'(?:\.\s){5,}', d)))
print('lone page numbers:', len([l for l in lines if BARE_NUM.match(l)]))
print('lines with odd $ :', len(dollar_odd), dollar_odd[:5])
print('--- first 18 lines ---')
print('\n'.join(lines[:18]))
