#!/usr/bin/env python3
"""Convert the translated LaTeX source into Markdown (and plain text), computing the
numbers LaTeX itself would have computed.

  * \\section/\\subsection -> ##/### with numbers + a generated TOC
  * equation (with inner split/gathered) -> $$ ... \\tag{n.m} $$
  * align -> one $$ block per row, each with its \\tag unless \\notag
  * theorem/proposition/lemma/corollary/definition share one counter per section,
    remark has its own; \\label binds to the most recent counter (like \\refstepcounter)
  * \\ref -> number, \\eqref -> （number）, \\cite -> [n] in \\bibitem order

usage: python3 tools/tex_md.py [--tex in.tex] [--md out.md] [--txt out.txt]
"""
import argparse
import json
import os
import re
import sys

SRC = '/home/a/Downloads/25/paper.tex'
sys.path.insert(0, '/home/a/Downloads/25')
ZH = '/home/a/Downloads/25/build/paper-zh-cn.tex'
MD = '/home/a/Downloads/25/paper-zh-cn.md'
TXT = '/home/a/Downloads/25/paper-zh-cn.txt'
TITLE_CACHE = '/home/a/Downloads/25/build/title_zh.txt'

THM = {'theorem': '定理', 'proposition': '命题', 'lemma': '引理', 'corollary': '推论',
       'definition': '定义', 'remark': '注', 'proof': '证明'}
MATH_ENVS = ['equation', 'align', 'align*', 'gather', 'multline', 'eqnarray']


class Num:
    """replays LaTeX's counters"""
    def __init__(self):
        self.sec = self.sub = self.eq = self.thm = self.rem = 0
        self.labels = {}
        self.last = None

    def section(self):
        self.sec += 1
        self.sub = self.eq = self.thm = self.rem = 0
        self.last = ('sec', str(self.sec))
        return str(self.sec)

    def subsection(self):
        self.sub += 1
        self.last = ('sub', '%d.%d' % (self.sec, self.sub))
        return '%d.%d' % (self.sec, self.sub)

    def equation(self):
        self.eq += 1
        self.last = ('eq', '%d.%d' % (self.sec, self.eq))
        return '%d.%d' % (self.sec, self.eq)

    def theorem(self, kind):
        if kind == 'remark':
            self.rem += 1
            n = '%d.%d' % (self.sec, self.rem)
        else:
            self.thm += 1
            n = '%d.%d' % (self.sec, self.thm)
        self.last = ('thm', n)
        return n

    def bind(self, name):
        if self.last and name not in self.labels:
            self.labels[name] = self.last[1]

    def resolve(self, name):
        return self.labels.get(name, '??')


def flat(s):
    return re.sub(r'\s+', ' ', s).strip()


def split_rows(blob):
    """split an align body on top-level \\\\"""
    body = re.sub(r'\\begin\{align\*?\}', '', blob)
    body = re.sub(r'\\end\{align\*?\}', '', body)
    rows, cur, depth, i = [], '', 0, 0
    while i < len(body):
        if body.startswith('\\begin{', i):
            depth += 1
        elif body.startswith('\\end{', i):
            depth -= 1
        if body.startswith('\\\\', i) and depth == 0:
            rows.append(cur)
            cur = ''
            i += 2
            continue
        cur += body[i]
        i += 1
    rows.append(cur)
    return [r for r in rows if r.strip()]


def grab_cmd(lines, i, cmd):
    """join lines until the braces of \\cmd{...} balance (titles may wrap)"""
    buf = lines[i]
    j = i
    while buf.count('{') > buf.count('}') and j + 1 < len(lines):
        j += 1
        buf += ' ' + lines[j].strip()
    return buf.strip(), j


def scan(text, seed_labels=None):
    """walk the document once; when emit is given, append markdown lines"""
    nb = Num()
    if seed_labels:
        nb.labels.update(seed_labels)
    lines = text.split('\n')
    out = []
    toc = []
    bib = []
    i = 0
    in_bib = False
    para = []

    def flush_para():
        if para:
            joined = ' '.join(x.strip() for x in para)
            joined = re.sub(r'\s{2,}', ' ', joined).strip()
            if joined:
                out.append(joined)
                out.append('')
            del para[:]

    def bind_blob(b):
        for lab in re.findall(r'\\label\{([^}]*)\}', b):
            nb.bind(lab)

    def fix(s, inline=True):
        s = re.sub(r'\\eqref\{([^}]*)\}', lambda m: '（%s）' % nb.resolve(m.group(1)), s)
        s = re.sub(r'\\ref\{([^}]*)\}', lambda m: nb.resolve(m.group(1)), s)
        s = re.sub(r'\\cite(\[[^\]]*\])?\{([^}]*)\}',
                   lambda m: cite_txt(m.group(1), m.group(2)), s)
        s = re.sub(r'\\subref\{([^}]*)\}', lambda m: nb.resolve(m.group(1)), s)
        s = re.sub(r'\\emph\{([^{}]*)\}', r'*\1*', s)
        s = re.sub(r'\\textit\{([^{}]*)\}', r'*\1*', s)
        s = re.sub(r'\\textbf\{([^{}]*)\}', r'**\1**', s)
        s = re.sub(r'\\texttt\{([^{}]*)\}', r'`\1`', s)
        s = re.sub(r'\\textsc\{([^{}]*)\}', r'\1', s)
        s = re.sub(r'\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}', r'\1', s)
        s = re.sub(r'\\url\{([^{}]*)\}', r'\1', s)
        s = re.sub(r'\\label\{[^}]*\}', '', s)
        s = re.sub(r'\\(?:noindent|medskip|smallskip|bigskip|newpage|clearpage|par|newblock|'
                   r'quad|qquad)\b', ' ', s)
        s = re.sub(r'\\[,;!:]\s?', '', s)
        s = s.replace('~', ' ').replace('\\&', '&').replace('\\%', '%')
        s = s.replace('\\_', '_').replace('\\#', '#').replace('\\S', '§')
        s = re.sub(r'\\[a-zA-Z]+\{\}', '', s)
        return re.sub(r'[ \t]{2,}', ' ', s).strip()

    def cite_txt(opt, keys):
        nums = []
        for k in [x.strip() for x in keys.split(',')]:
            nums.append(str(cite_map.get(k, '?')))
        t = '[%s]' % ', '.join(nums)
        if opt:
            t += '（%s）' % opt.strip('[]')
        return t

    cite_map = {}
    ii = 0
    while True:
        m = re.search(r'\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}', text[ii:])
        if not m:
            break
        ii += m.end()
        cite_map[m.group(1)] = len(cite_map) + 1

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        for lab in re.findall(r'\\label\{([^}]*)\}', ln):
            nb.bind(lab)
        if in_bib:
            if s.startswith('\\end{thebibliography}'):
                in_bib = False
                i += 1
                continue
            m = re.match(r'\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}', s)
            if m:
                flush_para()
                key = m.group(1)
                body = [s[m.end():]]
                i += 1
                while i < len(lines) and not re.match(r'\s*\\bibitem|\\end\{thebibliography\}',
                                                      lines[i]):
                    body.append(lines[i].strip())
                    i += 1
                txt = ' '.join(x for x in body if x)
                out.append('[%d] %s' % (cite_map.get(key, 0), flat(fix(txt))))
                out.append('')
                continue
            i += 1
            continue
        if s.startswith('\\begin{thebibliography}'):
            flush_para()
            out += ['', '## 参考文献', '']
            in_bib = True
            i += 1
            continue
        if not s:
            flush_para()
            i += 1
            continue
        # ---- structure (titles may wrap over several lines)
        if re.match(r'\\(?:sub)?section\*?\{', s) or re.match(r'\\paragraph\{', s):
            full, j = grab_cmd(lines, i, '')
            mm = re.match(r'\\(sub)?section(\*)?\{(.*)\}$', full, re.S)
            mp = re.match(r'\\paragraph\{(.*)\}$', full, re.S)
            flush_para()
            if mm:
                is_sub, star, title = mm.group(1), mm.group(2), fix(mm.group(3))
                if is_sub:
                    lvl, base = 3, '###'
                    num = None if star else nb.subsection()
                else:
                    lvl, base = 2, '##'
                    num = None if star else nb.section()
                head = '%s %s' % (base, title) if star else '%s %s %s' % (base, num, title)
                out += [head, '']
                toc.append((lvl, title if star else '%s %s' % (num, title)))
            elif mp:
                out += ['#### %s' % fix(mp.group(1)), '']
            i = j + 1
            continue
        if re.match(r'\\begin\{abstract\}', s):
            flush_para()
            out += ['## 摘要', '']
            i += 1
            continue
        if re.match(r'\\end\{abstract\}', s):
            flush_para()
            i += 1
            continue
        # ---- display math
        if s.startswith('\\['):
            flush_para()
            body = []
            while i < len(lines):
                body.append(lines[i])
                if '\\]' in lines[i]:
                    break
                i += 1
            blob = re.sub(r'^\s*\\\[', '', '\n'.join(body))
            blob = re.sub(r'\\\]\s*$', '', blob)
            out += math_block(blob)
            i += 1
            continue
        m = re.match(r'\\begin\{(equation|align|align\*|gather|multline)\}', s)
        if m:
            flush_para()
            env = m.group(1)
            body = []
            depth = 0
            while i < len(lines):
                body.append(lines[i])
                depth += len(re.findall(r'\\begin\{%s\}' % re.escape(env), lines[i]))
                depth -= len(re.findall(r'\\end\{%s\}' % re.escape(env), lines[i]))
                if depth <= 0:
                    break
                i += 1
            blob = re.sub(r'\\begin\{%s\}' % re.escape(env), '', '\n'.join(body))
            blob = re.sub(r'\\end\{%s\}' % re.escape(env), '', blob)
            bind_blob(blob)
            tag = None
            mt = re.search(r'\\tag\{([^}]*)\}', blob)
            if mt:
                tag = mt.group(1)
                blob = blob.replace(mt.group(0), '')
            if env == 'align':
                for r in split_rows('\\begin{align}' + blob + '\\end{align}'):
                    num = None
                    if '\\notag' not in r and '\\nonumber' not in r:
                        num = tag or nb.equation()
                    else:
                        nb.equation()
                    r = re.sub(r'\\notag|\\nonumber', '', r).replace('&', ' & ')
                    r = re.sub(r'\s*&\s*&\s*', ' &= ', r)
                    out += math_block(r, num)
            elif env == 'align*':
                out += ['$$', '\\begin{aligned}' + blob.rstrip() + '\\end{aligned}', '$$', '']
            else:
                num = tag or nb.equation()
                out += math_block(blob, num)
            i += 1
            continue
        # ---- theorem-like
        m = re.match(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark)\}'
                     r'(\[[^\]]*\])?', s)
        if m:
            flush_para()
            kind, opt = m.group(1), m.group(2)
            num = nb.theorem(kind)
            body = []
            while i < len(lines):
                body.append(lines[i])
                if '\\end{%s}' % kind in lines[i]:
                    break
                i += 1
            blob = re.sub(r'\\begin\{%s\}(\[[^\]]*\])?' % kind, '', '\n'.join(body))
            blob = re.sub(r'\\end\{%s\}' % kind, '', blob)
            bind_blob(blob)
            head = '**%s %s**' % (THM[kind], num)
            if opt:
                head += '（%s）' % flat(fix(opt.strip('[]')))
            txt = flat(fix(re.sub(r'\\label\{[^}]*\}', '', blob)))
            out += [head + ' ' + txt, '']
            i += 1
            continue
        m = re.match(r'\\begin\{proof\}(\S*)', s)
        if m:
            flush_para()
            opt = m.group(1)
            if opt.startswith('['):
                j = i
                buf = ''
                while ']' not in buf:
                    buf += ' ' + lines[j]
                    j += 1
                opt = buf[buf.index('['):buf.index(']') + 1]
            body = []
            while i < len(lines):
                body.append(lines[i])
                if '\\end{proof}' in lines[i]:
                    break
                i += 1
            blob = re.sub(r'\\begin\{proof\}(\[[^\]]*\])?', '', '\n'.join(body))
            blob = re.sub(r'\\end\{proof\}', '', blob)
            bind_blob(blob)
            head = '**证明'
            if opt and opt.startswith('['):
                head += '（%s）' % flat(fix(opt.strip('[]')))
            head += '。**'
            out += [head + ' ' + flat(fix(blob)) + ' □', '']
            i += 1
            continue
        # ---- lists
        if re.match(r'\\begin\{(enumerate|itemize)\}', s):
            flush_para()
            i += 1
            continue
        if re.match(r'\\end\{(enumerate|itemize)\}', s):
            flush_para()
            i += 1
            continue
        if s.startswith('\\item'):
            flush_para()
            out.append('- ' + flat(fix(s[5:])))
            i += 1
            continue
        if re.match(r'\\begin\{center\}', s) or re.match(r'\\end\{center\}', s):
            i += 1
            continue
        m = re.match(r'\\begin\{tabularx\}', s)
        if m:
            flush_para()
            body = []
            while i < len(lines):
                body.append(lines[i])
                if '\\end{tabularx}' in lines[i]:
                    break
                i += 1
            blob = '\n'.join(body)
            blob = re.sub(r'\\begin\{tabularx\}[^\n]*\n', '', blob)
            blob = re.sub(r'\\end\{tabularx\}', '', blob)
            for row in blob.split('\\\\'):
                cells = [c.strip() for c in row.split('&')]
                if len(cells) >= 2 and cells[0]:
                    out.append('- %s：%s' % (flat(fix(cells[0])),
                                             flat(fix(' '.join(cells[1:])))))
                elif ''.join(cells).strip():
                    out.append(flat(fix(' '.join(cells))))
            out.append('')
            i += 1
            continue
        if re.match(r'\\maketitle|\\tableofcontents|\\clearpage|\\newpage|\\noindent|\\medskip|'
                    r'\\smallskip|\\bigskip|\\vspace|\\hspace', s):
            i += 1
            continue
        para.append(ln)
        i += 1
    flush_para()
    return out, toc, nb, cite_map


def math_block(body, tag=None):
    b = body.strip()
    b = re.sub(r'\\begin\{split\}', r'\\begin{aligned}', b)
    b = re.sub(r'\\end\{split\}', r'\\end{aligned}', b)
    if tag:
        b += '\n\\tag{%s}' % tag
    return ['$$', b, '$$', '']


def title_md():
    import ds_api
    if os.path.exists(TITLE_CACHE):
        d = json.load(open(TITLE_CACHE, encoding='utf-8'))
    else:
        got, _ = ds_api.call([{'role': 'system', 'content':
                               '把 JSON 里每个值翻译成简体中文，只输出同样结构的 JSON，不要解释。'},
                              {'role': 'user', 'content':
                               '{"title": "The Quasi-Riemann Hypothesis", '
                               '"subtitle": "A Zero-Free Half-Plane"}'}],
                             max_tokens=300, temperature=0.2)
        got = re.sub(r'^```[a-z]*\n|\n```$', '', got.strip())
        try:
            d = json.loads(got[got.index('{'):got.rindex('}') + 1])
        except Exception:
            d = {'title': '拟黎曼假设', 'subtitle': '无零半平面'}
        json.dump(d, open(TITLE_CACHE, 'w', encoding='utf-8'), ensure_ascii=False)
    lines = ['# %s' % d.get('title', '拟黎曼假设'), '',
             '**%s** $\\Re s>7/8$' % d.get('subtitle', '无零半平面'), '',
             '**OpenAI** ｜ 2026 年 9 月 30 日', '']
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tex', default=ZH)
    ap.add_argument('--md', default=MD)
    ap.add_argument('--txt', default=TXT)
    ap.add_argument('--notitle', action='store_true')
    a = ap.parse_args()
    text = open(a.tex, encoding='utf-8').read()
    body = text[text.index('\\begin{document}') + len('\\begin{document}'):]
    labels = scan(body)[2].labels              # pass 1: collect the label map
    out, toc, nb, cites = scan(body, seed_labels=labels)
    # drop the leading empty runs
    while out and not out[0].strip():
        out.pop(0)
    head = [] if a.notitle else title_md() + ['---', '']
    toc_md = ['## 目录', '']
    for lvl, t in toc:
        toc_md.append(('    ' * (lvl - 2)) + '- ' + t)
    toc_md.append('')
    toc_md.append('---')
    md = '\n'.join(head + toc_md + [''] + out)
    md = re.sub(r'\n{3,}', '\n\n', md)
    open(a.md, 'w', encoding='utf-8').write(md)
    # plain text: drop markdown markers, keep math source
    txt = []
    for ln in md.split('\n'):
        s = re.sub(r'^#{1,6}\s*', '', ln)
        s = re.sub(r'^-\s+', '  - ', s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'\1', s)
        s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\1', s)
        s = re.sub(r'`([^`]+)`', r'\1', s)
        if s.strip() == '---':
            s = ''
        txt.append(s)
    txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(txt))
    open(a.txt, 'w', encoding='utf-8').write(txt)
    print('md  %s  (%d chars, %d lines)' % (a.md, len(md), md.count('\n')))
    print('txt %s  (%d chars)' % (a.txt, len(txt)))
    print('sections %d | subsections in toc %d | labels %d | bibitems %d'
          % (nb.sec, len(toc), len(nb.labels), len(cites)))
    print('display blocks: %d | inline math: %d'
          % (md.count('\n$$\n'), len(re.findall(r'(?<!\$)\$(?!\$)', md)) // 2))
    unresolved = sorted(set(re.findall(r'(?<![\\\w])[?]{2}(?![?\w])', md)))
    print('unresolved refs: %d' % md.count('??'))


main()
