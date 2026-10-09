#!/usr/bin/env python3
"""Audit calligraphic letters.

CMSY10 holds \\mathcal{A}..\\mathcal{Z} at the ASCII letter positions, and the text
extraction hands them over as plain letters - so a translation can silently lose the
calligraphic font. This compares, per page, how many CMSY10 letters the PDF prints
with how many \\mathcal{...} the Chinese file uses.

usage: python3 tools/audit_mathcal.py [start] [end]
"""
import os
import re
import sys
from collections import Counter

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'
# CMSY10 positions that are genuinely symbols, not calligraphic letters
KEEP = set('A')


def main():
    doc = fitz.open(PDF)
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else doc.page_count
    tot_p = tot_z = 0
    rows = []
    for n in range(lo, hi + 1):
        letters = Counter()
        for blk in doc[n - 1].get_text('rawdict')['blocks']:
            if blk.get('type') != 0:
                continue
            for line in blk['lines']:
                for span in line['spans']:
                    if not span['font'].startswith('CMSY'):
                        continue
                    for ch in span['chars']:
                        if ch['c'].isascii() and ch['c'].isalpha():
                            letters[ch['c']] += 1
        p = sum(letters.values())
        tot_p += p
        pth = '%s/page_%03d.zh.md' % (OUT, n)
        if not os.path.exists(pth):
            continue
        t = open(pth, encoding='utf-8').read()
        zm = len(re.findall(r'\\mathcal\{', t)) + len(re.findall(r'\\mathscr\{', t)) \
            + len(re.findall(r'\\mathfrak\{', t))
        tot_z += zm
        if p != zm:
            rows.append(n)
            print('%4d | pdf calligraphic %3d %-28s | zh \\mathcal/\\mathfrak %3d | %s'
                  % (n, p, ' '.join('%s%d' % (k, v) for k, v in letters.most_common(9)), zm,
                     '<== GAP' if p > zm else '(zh has more)'))
    print()
    print('PDF calligraphic total: %d | ZH \\mathcal+\\mathfrak total: %d' % (tot_p, tot_z))
    print('pages differing: %d -> %s' % (len(rows), rows))


main()
