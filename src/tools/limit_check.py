#!/usr/bin/env python3
"""Check the limits (sub/superscripts) of every big operator.

A translator working from the broken text layer can move a limit line to the wrong
sum or invent one, so this prints, per big operator, the lines actually printed
under/over it (grouped by y), for comparison with the Chinese \\substack content.

usage: python3 tools/limit_check.py PAGE [Y0 Y1]
       python3 tools/limit_check.py --all          # per-page summary + gap list
"""
import sys
from collections import Counter

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
BIGOP = {'X': '\\sum', 'Y': '\\prod', 'Z': '\\int'}


def ops_of(pg, y0=0, y1=9999, x0=0, x1=9999):
    spans, ops = [], []
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type') != 0:
            continue
        for line in blk['lines']:
            for span in line['spans']:
                t = ''.join(c['c'] for c in span['chars'])
                if t.strip():
                    spans.append((span['bbox'], t, span['font']))
                if span['font'].startswith('CMEX'):
                    for ch in span['chars']:
                        if ch['c'] in BIGOP and span['size'] > 10:
                            ops.append((BIGOP[ch['c']], ch['bbox']))
    out = []
    for name, bb in ops:
        if not (y0 <= bb[1] <= y1 and x0 <= bb[0] <= x1):
            continue
        below, above = {}, {}
        for sbb, t, f in spans:
            cx = (sbb[0] + sbb[2]) / 2
            if not (bb[0] - 30 < cx < bb[2] + 30):
                continue
            if bb[3] <= sbb[1] <= bb[3] + 30 and f != 'CMEX10':
                below.setdefault(round(sbb[1] / 3.0), []).append((sbb[0], t))
            if bb[1] - 30 <= sbb[3] <= bb[1] and f != 'CMEX10':
                above.setdefault(round(sbb[3] / 3.0), []).append((sbb[0], t))
        fmt = lambda d: [' '.join(t.strip() for _, t in sorted(v) if t.strip())
                         for _, v in sorted(d.items())]
        out.append((name, bb, fmt(below), fmt(above)))
    return out


def main():
    doc = fitz.open(PDF)
    if '--all' in sys.argv:
        rows = []
        for n in range(1, doc.page_count + 1):
            ops = ops_of(doc[n - 1])
            multi = [(nm, len(b), len(a)) for nm, bb, b, a in ops if len(b) > 1 or len(a) > 1]
            if multi:
                rows.append((n, len(ops), len(multi)))
                print('page %3d: %d operators, %d with multi-line limits  %s'
                      % (n, len(ops), len(multi), ' '.join('%s(L%d)' % (nm, b) for nm, b, a in multi[:8])))
        print()
        print('pages with multi-line limits: %d' % len(rows))
        print([r[0] for r in rows])
        return
    page = int(sys.argv[1])
    y0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    y1 = float(sys.argv[3]) if len(sys.argv) > 3 else 9999
    for name, bb, below, above in ops_of(doc[page - 1], y0, y1):
        print('%s at y %.1f x %.1f' % (name, bb[1], bb[0]))
        for i, l in enumerate(below):
            print('    below[%d]: %s' % (i, l))
        for i, l in enumerate(above):
            print('    above[%d]: %s' % (i, l))


main()
