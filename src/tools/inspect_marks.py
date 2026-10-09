#!/usr/bin/env python3
"""Show, for each accent / overline / bar item on selected pages, the glyphs
lying on the same text line (sorted by x) with their x-extents, so we can see
which base symbol an accent sits on and which symbols an overline spans."""
import sys
import fitz

PDF = '/home/a/Downloads/25/paper.pdf'

BIGOP = {'X': 'sum', 'Y': 'prod', 'Z': 'int'}
RADCH = {'b', 'e'}


def items_of(pg):
    chars, spans = [], []
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type') != 0:
            continue
        for line in blk['lines']:
            for span in line['spans']:
                txt = ''.join(c['c'] for c in span['chars'])
                if txt.strip():
                    spans.append((span['bbox'], txt))
                for ch in span['chars']:
                    chars.append({'c': ch['c'], 'bb': ch['bbox'], 'font': span['font']})
    rules = [p['rect'] for p in pg.get_drawings()
             if p['rect'].height <= 2.5 and p['rect'].width >= 1.5]
    return chars, spans, rules


def line_chars(chars, yref, band=6.0):
    sel = [c for c in chars if abs(c['bb'][1] - yref) < band]
    return sorted(sel, key=lambda c: c['bb'][0])


def main():
    page = int(sys.argv[1])
    doc = fitz.open(PDF)
    pg = doc[page - 1]
    chars, spans, rules = items_of(pg)

    print('=== page', page, '===')
    # accents
    print('--- accents (CMEX10 b/e without attached rule) ---')
    for c in chars:
        f, ch, bb = c['font'], c['c'], c['bb']
        if f.startswith('CMEX') and ch in RADCH:
            vin = [r for r in rules if abs(r.y0 - bb[1]) < 4.0 and bb[2] - 4.0 < r.x0 < bb[2] + 12.0]
            if vin:
                continue
            lc = line_chars(chars, bb[1])
            s = ''.join(x['c'] for x in lc)
            print('ACCENT bb=(%.1f,%.1f,%.1f,%.1f)' % (bb[0], bb[1], bb[2], bb[3]))
            for x in lc:
                mark = ' <== under accent' if x['bb'][0] - 3 <= bb[0] <= x['bb'][2] + 1 else ''
                print('     x %6.1f-%6.1f  %r%s' % (x['bb'][0], x['bb'][2], x['c'], mark))
    # rules / overlines
    print('--- horizontal rules (overline candidates) ---')
    for r in rules:
        rad = any(abs(r.y0 - c['bb'][1]) < 4.0 and c['bb'][2] - 4.0 < r.x0 < c['bb'][2] + 12.0
                  for c in chars if c['font'].startswith('CMEX') and c['c'] in RADCH)
        tag = 'RADICAL' if rad else 'RULE'
        lc = [c for c in chars if c['bb'][1] >= r.y1 - 2.0 and c['bb'][1] <= r.y1 + 15.0
              and c['bb'][2] > r.x0 + 0.5 and c['bb'][0] < r.x1 - 0.5]
        lc.sort(key=lambda c: c['bb'][0])
        print('%s y=%.1f x=%.1f-%.1f (w=%.1f) covers=%r' % (tag, r.y0, r.x0, r.x1, r.x1 - r.x0,
              ''.join(c['c'] for c in lc)))
    # bars
    print('--- bars (CMSY | / U+2225) ---')
    for c in chars:
        f, ch, bb = c['font'], c['c'], c['bb']
        if f.startswith('CMSY') and ch in ('|', '\u2225'):
            lc = line_chars(chars, bb[1])
            print('BAR y=%.1f x=%.1f-%.1f  line=%r' % (bb[1], bb[0], bb[2],
                  ''.join(x['c'] for x in lc)[:120]))


main()
