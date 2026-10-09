#!/usr/bin/env python3
"""Full per-font character census, to catch broken glyphs that were mapped to an
ordinary ASCII letter (the radicals and accents do this - e.g. the circumflex
comes out as 'b').

usage: python3 tools/font_census.py [font-substring ...]
"""
import sys
from collections import Counter, defaultdict

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
doc = fitz.open(PDF)
want = sys.argv[1:] or ['CMEX', 'CMSY', 'CMMI', 'CMR', 'CMSS', 'MSAM', 'MSBM', 'EUSM', 'EUFM', 'RSFS']

per = defaultdict(Counter)
sample = {}
for n in range(doc.page_count):
    pg = doc[n]
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type') != 0:
            continue
        for line in blk['lines']:
            for span in line['spans']:
                f = span['font']
                if not any(w in f for w in want):
                    continue
                for ch in span['chars']:
                    c = ch['c']
                    key = c if c else '<empty>'
                    per[f][key] += 1
                    sample.setdefault((f, key), (n + 1, tuple(round(v, 1) for v in ch['bbox']),
                                                 round(span['size'], 2)))

for f in sorted(per):
    tot = sum(per[f].values())
    print('=== %s  (%d chars) ===' % (f, tot))
    for c, cnt in per[f].most_common():
        pg, bb, sz = sample[(f, c)]
        if c.isalpha() and c.isascii() and cnt > 3:
            print('   %-8r %6d   page %3d bbox %-34s size %s' % (c, cnt, pg, bb, sz))
        elif not (c.isalpha() and c.isascii()):
            print('   %-8r %6d   page %3d bbox %-34s size %s' % (c, cnt, pg, bb, sz))
