#!/usr/bin/env python3
"""Normalise the table-of-contents lines inside the translated markdown pages.

Each entry becomes its own line, entries are separated by blank lines (so any
markdown renderer breaks the line), dot leaders are removed, the page number
stays at the end, and sub-entries keep a real leading indent (2 spaces per level).

Only real TOC lines qualify: the title must contain Chinese characters, which
keeps numeric tables / maths fragments out.
"""
import re, glob, os

ROOT = '/home/a/Downloads/25'
OUTD = os.path.join(ROOT, 'out')

E_DOTS = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(.+?)'
                    r'[ \u3000]*((?:[.．·][ \u3000]*){3,})[ \u3000]*(\d{1,3})?[ \u3000]*$')
E_PLAIN = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(\S.*?)'
                     r'[ \u3000]+(\d{1,3})[ \u3000]*$')
DOTS_ONLY = re.compile(r'^[ \u3000]*[.．·][.．·\u3000 ]*$')
BARE_NUM = re.compile(r'^[ \u3000]*(\d{1,3})[ \u3000]*$')
EN_TOC_LINE = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(.+?)[ \u3000]*'
                         r'((?:\.\s*){3,})[ \u3000]*(\d{1,3})\s*$')


def cjk(s):
    return len(re.findall(r'[\u4e00-\u9fff]', s))


def match_entry(ln):
    """-> (num, title, page) or None, for a real TOC entry line."""
    m = E_DOTS.match(ln)
    if m:
        title, page = m.group(3).strip().rstrip(' .．·'), m.group(5)
        if cjk(title) < 2:
            return None
        return m.group(2), title, page
    m = E_PLAIN.match(ln)
    if m:
        title, page = m.group(3).strip(), m.group(4)
        if cjk(title) < 2 or re.search(r'[。，；：]', title):
            return None
        return m.group(2), title, page
    return None


def load_en_toc():
    m = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'pages', 'page_*.txt')))[:4]:
        for ln in open(f, encoding='utf-8').read().split('\n'):
            mm = EN_TOC_LINE.match(ln)
            if mm:
                m.setdefault(mm.group(2), mm.group(5))
    return m


EN_TOC = {}


def normalise(text):
    lines = text.split('\n')
    hits = sum(1 for ln in lines if match_entry(ln))
    if '目录' not in text and hits < 4:
        return 0, text
    out, i, n = [], 0, 0
    while i < len(lines):
        ent = match_entry(lines[i])
        if ent:
            num, title, page = ent
            if not page:                       # page number wrapped onto the following line
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and BARE_NUM.match(lines[j]):
                    page, i = BARE_NUM.match(lines[j]).group(1), j
            if not page:
                page = EN_TOC.get(num, '')
            lvl = 1 if '.' not in num else min(num.count('.') + 1, 3)
            out += ['', ' ' * (2 * (lvl - 1)) + ('%s %s %s' % (num, title, page)).strip()]
            n += 1
            i += 1
            continue
        if DOTS_ONLY.match(lines[i]):
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return n, re.sub(r'\n{3,}', '\n\n', '\n'.join(out))


EN_TOC = load_en_toc()
total = 0
for p in sorted(glob.glob(os.path.join(OUTD, 'page_*.zh.md'))):
    src = open(p, encoding='utf-8').read()
    n, new = normalise(src)
    if n and new != src:
        if not os.path.exists(p + '.bak'):
            open(p + '.bak', 'w', encoding='utf-8').write(src)
        open(p, 'w', encoding='utf-8').write(new)
        print('%-28s %d entries' % (os.path.basename(p), n))
        total += n
print('total entries normalised:', total)

# drop backups for pages that ended up identical (from an earlier run)
removed = 0
for b in glob.glob(os.path.join(OUTD, 'page_*.zh.md.bak')):
    if open(b, encoding='utf-8').read() == open(b[:-4], encoding='utf-8').read():
        os.remove(b)
        removed += 1
print('stale backups removed:', removed)
