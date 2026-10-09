#!/usr/bin/env python3
"""Classify every horizontal rule in the PDF: fraction bar / radical vinculum / overline.

TeX draws all three as short horizontal lines, so counting "lines" alone over-reports.
The neighbours disambiguate:
  text above AND below the rule            -> FRACTION bar   (\\frac, \\dfrac)
  only text below, a CMEX hook at its left -> RADICAL vinculum (\\sqrt / \\sqrt[3])
  only text below, nothing to the left     -> OVERLINE (\\overline / \\bar)
Prints the overline/radical items with the text they cover, so they can be diffed
against the LaTeX in out/page_NNN.zh.md.

usage: python3 tools/marks_inventory.py [start] [end] [--detail]
"""
import os
import re
import sys

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'


def page_data(pg):
    spans, bars, tall = [], [], []
    d = pg.get_text('rawdict')
    for blk in d.get('blocks', []):
        if blk.get('type') != 0:
            continue
        for line in blk.get('lines', []):
            for span in line.get('spans', []):
                txt = ''.join(ch['c'] for ch in span.get('chars', []))
                if txt.strip():
                    spans.append((span['bbox'], txt))
                for ch in span.get('chars', []):
                    c, bb = ch['c'], ch['bbox']
                    if c in ('|', '\u2223', '\u2225', '\u2016'):
                        bars.append((bb, c))
                    elif len(c) == 1 and ord(c) < 32:
                        tall.append(bb)
    rules = []
    for p in pg.get_drawings():
        r = p['rect']
        if r.height <= 2.5 and r.width >= 1.5:
            rules.append(r)
    return spans, bars, tall, rules


def classify(rule, spans, tall):
    above, below = [], []
    for bb, txt in spans:
        if bb[2] > rule.x0 + 0.5 and bb[0] < rule.x1 - 0.5:
            if bb[3] <= rule.y0 + 2.0 and bb[3] >= rule.y0 - 9.0:
                above.append(txt.strip())
            if bb[1] >= rule.y1 - 2.0 and bb[1] <= rule.y1 + 14.0:
                below.append(txt.strip())
    hook = any(bb[2] <= rule.x0 + 3.5 and bb[0] >= rule.x0 - 8.0 and bb[3] > rule.y0
               and bb[1] < rule.y1 for bb in tall)
    a = ' '.join(t for t in above if t)
    b = ' '.join(t for t in below if t)
    if a and b:
        return 'FRACTION', a, b
    if hook:
        return 'RADICAL', a, b
    if b:
        return 'OVERLINE', a, b
    return 'OTHER', a, b


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    detail = '--detail' in sys.argv
    lo = int(args[0]) if args else 1
    doc = fitz.open(PDF)
    hi = int(args[1]) if len(args) > 1 else doc.page_count
    counts = {'FRACTION': 0, 'RADICAL': 0, 'OVERLINE': 0, 'OTHER': 0}
    over_pages, bar_pages = [], []
    for n in range(lo, hi + 1):
        spans, bars, tall, rules = page_data(doc[n - 1])
        items = [classify(r, spans, tall) for r in rules]
        c = {k: sum(1 for it in items if it[0] == k) for k in counts}
        for k in counts:
            counts[k] += c[k]
        zt = ''
        pth = os.path.join(OUT, 'page_%03d.zh.md' % n)
        if os.path.exists(pth):
            t = open(pth, encoding='utf-8').read()
            nb = len(re.findall(r'\\overline\b', t)) + len(re.findall(r'\\bar\b', t))
            nabs = len(re.findall(r'\\lvert|\\rvert|\\lVert|\\rVert|\\mid(?![a-z])|\\left\||\\right\|', t))
            nbar = len(re.findall(r'(?<!\\)\|', t))
            zt = 'zh: overline=%d abs=%d bar=%d' % (nb, nabs, nbar)
            if c['OVERLINE'] and nb == 0 and c['RADICAL'] == 0:
                over_pages.append((n, c['OVERLINE'], zt))
        if c['OVERLINE'] or c['RADICAL'] or bars:
            print('page %3d | frac %2d rad %2d OVER %2d other %2d bars %2d | %s'
                  % (n, c['FRACTION'], c['RADICAL'], c['OVERLINE'], c['OTHER'], len(bars), zt))
            # self-check: square roots are what RADICAL should be
            if detail:
                for kind, a, b in items:
                    if kind in ('OVERLINE', 'RADICAL'):
                        print('        %-9s over %r   (above=%r)' % (kind, b[:48], a[:24]))
    print()
    print('TOTAL rules by class: %s' % counts)
    print()
    print('pages whose only rules are overlines while the LaTeX has none (%d):' % len(over_pages))
    for n, k, zt in over_pages:
        print('   page %d  (%d overline rules)  %s' % (n, k, zt))


main()
