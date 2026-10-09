#!/usr/bin/env python3
"""Inventory the glyphs a page prints that the text extraction cannot name.

Anything whose character is a control code (\x00-\x1f) or a replacement char is a
glyph with a broken ToUnicode map: TeX big delimiters \left( \right| \right) ,
bars, braces, radicals, and overline/rule glyphs all land here.  Their size and
position identify what they are.

usage: python3 tools/glyph_probe.py PAGE [Y0 Y1]
"""
import sys
from collections import Counter

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'


def main():
    page_no = int(sys.argv[1])
    y0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    y1 = float(sys.argv[3]) if len(sys.argv) > 3 else 10000.0
    doc = fitz.open(PDF)
    pg = doc[page_no - 1]

    print('=== page %d  band %.0f-%.0f ===' % (page_no, y0, y1))
    print('vector drawings on page: %d' % len(pg.get_drawings()))

    spans = []
    d = pg.get_text('rawdict')
    for blk in d.get('blocks', []):
        if blk.get('type') != 0:
            continue
        for line in blk.get('lines', []):
            for span in line.get('spans', []):
                x0, sy0, x1, sy1 = span['bbox']
                if sy1 < y0 or sy0 > y1:
                    continue
                for ch in span.get('chars', []):
                    spans.append((ch['c'], ch['bbox'], span['font'], round(span['size'], 2)))

    base = Counter(round(s[3]) for s in spans).most_common(1)
    print('dominant text size: %s' % (base[0][0] if base else '?'))

    print('--- control / unnamed glyphs (candidate bars, braces, rules, radicals) ---')
    n = 0
    for c, bb, font, size in sorted(spans, key=lambda s: (round(s[1][1], 1), s[1][0])):
        uname = c.encode('unicode_escape').decode()
        if len(c) == 1 and ord(c) < 32 or c in ('\ufffd', ''):
            h = bb[3] - bb[1]
            w = bb[2] - bb[0]
            shape = 'TALL' if h > size * 1.3 else ('wide' if w > size * 0.9 else 'small')
            print('   %-8s x %6.1f-%6.1f y %6.1f-%6.1f  w %.1f h %.1f  size %.1f %-10s %s'
                  % (uname, bb[0], bb[2], bb[1], bb[3], w, h, size, font, shape))
            n += 1
    print('   total unnamed glyphs in band: %d' % n)

    print('--- named bar-ish glyphs (| U+007C, \u2223, \u2016, \u00af, \u0304, \u2212) ---')
    for c, bb, font, size in sorted(spans, key=lambda s: (round(s[1][1], 1), s[1][0])):
        if c in ('|', '\u2223', '\u2225', '\u2016', '\u00af', '\u0304', '\u0305', '\u2212', '\u23b8'):
            print('   %-4r x %6.1f-%6.1f y %6.1f-%6.1f size %.1f %s'
                  % (c, bb[0], bb[2], bb[1], bb[3], size, font))


main()
