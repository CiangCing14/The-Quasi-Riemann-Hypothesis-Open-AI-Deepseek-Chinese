#!/usr/bin/env python3
"""Work lists for calligraphic letters (CMSY10 \\mathcal{A}..\\mathcal{Z}).

The extraction hands these over as plain letters, so a translation can drop the
font and lose a distinction the paper actually uses (plain B vs \\mathcal{B} are
different objects here).  Per page: every calligraphic glyph with its position and
the formula line it sits in.

usage: python3 tools/cal_worklists.py            # report + gap list
       python3 tools/cal_worklists.py --write    # write tools/worklists_cal/page_NNN.txt
"""
import os
import re
import sys
from collections import Counter

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'
WDIR = '/home/a/Downloads/25/tools/worklists_cal'


def main():
    doc = fitz.open(PDF)
    write = '--write' in sys.argv
    if write:
        os.makedirs(WDIR, exist_ok=True)
    gaps = []
    for n in range(1, doc.page_count + 1):
        spans = []
        glyphs = []
        for blk in doc[n - 1].get_text('rawdict')['blocks']:
            if blk.get('type') != 0:
                continue
            for line in blk['lines']:
                for span in line['spans']:
                    txt = ''.join(c['c'] for c in span['chars'])
                    if txt.strip():
                        spans.append((span['bbox'], txt))
                    if span['font'].startswith('CMSY'):
                        for ch in span['chars']:
                            if ch['c'].isascii() and ch['c'].isalpha():
                                glyphs.append((ch['c'], ch['bbox']))
        pth = '%s/page_%03d.zh.md' % (OUT, n)
        if not os.path.exists(pth) or not glyphs:
            continue
        t = open(pth, encoding='utf-8').read()
        zm = len(re.findall(r'\\mathcal\{', t)) + len(re.findall(r'\\mathscr\{', t)) \
            + len(re.findall(r'\\mathfrak\{', t))
        if len(glyphs) <= zm:
            continue
        gaps.append(n)
        if not write:
            continue
        lines = ['PAGE %d   calligraphic glyphs in the PDF: %d   \\mathcal in the Chinese: %d'
                 % (n, len(glyphs), zm), '']
        for ch, bb in sorted(glyphs, key=lambda g: (g[1][1], g[1][0])):
            same = sorted([(b, s) for b, s in spans if abs(b[1] - bb[1]) < 3.5],
                          key=lambda x: x[0][0])
            line = ' '.join(s.strip() for _, s in same if s.strip())
            lines.append('CAL %s  y %6.1f x %6.1f-%6.1f' % (ch, bb[1], bb[0], bb[2]))
            lines.append('      line: %s' % line[:170])
        open('%s/page_%03d.txt' % (WDIR, n), 'w', encoding='utf-8').write('\n'.join(lines))
    print('pages with fewer \\mathcal than calligraphic glyphs: %d' % len(gaps))
    print(gaps)


main()
