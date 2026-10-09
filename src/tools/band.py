#!/usr/bin/env python3
"""Dump characters in a horizontal band for a page.

usage: band.py PAGE Y0 Y1 [X0 X1]
Prints each char with its x0-x1, y0-y1, font, and codepoint.
"""
import sys
import fitz

PDF = '/home/a/Downloads/25/paper.pdf'


def main():
    pg = int(sys.argv[1])
    y0, y1 = float(sys.argv[2]), float(sys.argv[3])
    x0 = float(sys.argv[4]) if len(sys.argv) > 4 else -1e9
    x1 = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
    doc = fitz.open(PDF)
    chars = []
    for blk in doc[pg - 1].get_text('rawdict')['blocks']:
        if blk.get('type') != 0:
            continue
        for line in blk['lines']:
            for span in line['spans']:
                for ch in span['chars']:
                    bb = ch['bbox']
                    if bb[1] >= y0 and bb[3] <= y1 and bb[2] > x0 and bb[0] < x1:
                        chars.append((bb[0], ch['c'], bb, span['font']))
    chars.sort()
    for cx, c, bb, font in chars:
        cp = ord(c)
        print('x %7.2f-%7.2f y %7.2f-%7.2f %-16s %r U+%04X' % (bb[0], bb[2], bb[1], bb[3], font, c, cp))


main()
