#!/usr/bin/env python3
"""dump chars in a rect: python3 dump_rect.py PAGE x0 y0 x1 y1"""
import sys
import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
page, x0, y0, x1, y1 = int(sys.argv[1]), *map(float, sys.argv[2:6])
doc = fitz.open(PDF)
pg = doc[page - 1]
chars = []
for blk in pg.get_text('rawdict')['blocks']:
    if blk.get('type') != 0:
        continue
    for line in blk['lines']:
        for span in line['spans']:
            for ch in span['chars']:
                bb = ch['bbox']
                if bb[2] >= x0 and bb[0] <= x1 and bb[3] >= y0 and bb[1] <= y1:
                    chars.append((bb[1], bb[0], ch['c'], span['font'], bb))
for c in sorted(chars):
    print('y %7.1f x %6.1f-%6.1f  %-14s %r' % (c[0], c[4][0], c[4][2], c[3], c[2]))
