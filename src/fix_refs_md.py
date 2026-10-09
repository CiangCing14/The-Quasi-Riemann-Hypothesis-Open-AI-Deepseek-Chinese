#!/usr/bin/env python3
"""Put every bibliography entry on its own markdown block.

Reference lines ("[12] Author, Title, ...") are separated by a blank line so that
each entry renders as its own line; wrapped continuation lines stay with their
entry.  Only bibliography pages (>= 3 reference lines starting a line) are touched.
"""
import re, glob, os

ROOT = '/home/a/Downloads/25'
OUTD = os.path.join(ROOT, 'out')
REF_LINE = re.compile(r'^\s*\[\d+\]\s')


def is_bib(lines):
    return sum(1 for ln in lines if REF_LINE.match(ln)) >= 3


def normalise(text):
    lines = text.split('\n')
    if not is_bib(lines):
        return 0, text
    out, n = [], 0
    for i, ln in enumerate(lines):
        if REF_LINE.match(ln) and i > 0:
            if out and out[-1].strip() != '':
                out.append('')
                n += 1
        out.append(ln)
    return n, re.sub(r'\n{3,}', '\n\n', '\n'.join(out))


total = 0
for p in sorted(glob.glob(os.path.join(OUTD, 'page_*.zh.md'))):
    src = open(p, encoding='utf-8').read()
    n, new = normalise(src)
    if n and new != src:
        if not os.path.exists(p + '.bak2'):
            open(p + '.bak2', 'w', encoding='utf-8').write(src)
        open(p, 'w', encoding='utf-8').write(new)
        print('%-28s %d reference entries separated' % (os.path.basename(p), n))
        total += n
print('total reference entries separated:', total)
