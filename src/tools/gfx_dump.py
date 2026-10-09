#!/usr/bin/env python3
"""Dump everything the PDF actually prints in a y-band of a page: every glyph
(with its box) and every vector drawing (lines / thin rects = overlines & bars).

usage: python3 tools/gfx_dump.py PAGE Y0 Y1 [--chars]
"""
import sys

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'


def main():
    page_no = int(sys.argv[1])
    y0, y1 = float(sys.argv[2]), float(sys.argv[3])
    chars = '--chars' in sys.argv[4:]
    doc = fitz.open(PDF)
    pg = doc[page_no - 1]
    print('=== page %d  band y %.1f-%.1f  (page rect %s) ===' % (page_no, y0, y1, pg.rect))

    print('--- text spans ---')
    d = pg.get_text('rawdict')
    for blk in d.get('blocks', []):
        if blk.get('type') != 0:
            continue
        for line in blk.get('lines', []):
            for span in line.get('spans', []):
                x0, sy0, x1, sy1 = span['bbox']
                if sy1 < y0 or sy0 > y1:
                    continue
                txt = ''.join(ch['c'] for ch in span.get('chars', []))
                print('  span y %6.1f-%6.1f x %6.1f-%6.1f size %4.2f %r'
                      % (sy0, sy1, x0, x1, span['size'], txt))
                if chars:
                    for ch in span.get('chars', []):
                        cx0, cy0, cx1, cy1 = ch['bbox']
                        print('        %-4r x %6.1f-%6.1f y %6.1f-%6.1f'
                              % (ch['c'], cx0, cx1, cy0, cy1))

    print('--- vector drawings (bar / rule candidates) ---')
    for p in pg.get_drawings():
        r = p['rect']
        if r.y1 < y0 or r.y0 > y1:
            continue
        w, h = r.width, r.height
        kind = []
        if h <= 2.0 and w >= 2.0:
            kind.append('HORIZ-RULE')
        if w <= 2.0 and h >= 2.0:
            kind.append('VERT-BAR')
        items = p.get('items', [])
        desc = ','.join(sorted({it[0] for it in items}))
        print('  draw [%s] rect x %6.1f-%6.1f y %6.1f-%6.1f  w %.2f h %.2f  fill=%s stroke=%s'
              % (desc, r.x0, r.x1, r.y0, r.y1, w, h,
                 tuple(round(c, 2) for c in (p.get('fill') or ())),
                 tuple(round(c, 2) for c in (p.get('color') or ()))))
        for it in items:
            if it[0] == 'l':
                print('        line %s -> %s' % (tuple(round(v, 1) for v in it[1]),
                                                 tuple(round(v, 1) for v in it[2])))
            elif it[0] == 're':
                rr = it[1]
                print('        rect %s' % (tuple(round(v, 1) for v in rr),))


main()
