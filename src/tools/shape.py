#!/usr/bin/env python3
"""Pixel-shape classification of accents and big delimiters (the marks the text
layer cannot name).

Accents: a circumflex (\\hat) is a wedge - narrow at the top, wide at the bottom.
A macron (\\bar) is a flat bar - constant width, tiny height.  A tilde is wavy.
Delimiters: '|' is one thin column, '‖' two, '(' has its middle pushed left,
')' its middle pushed right, '{' / '}' have a spike / bulge and are wide.

usage: python3 tools/shape.py page X0 Y0 X1 Y1 [...]
"""
import sys

import fitz
import numpy as np

PDF = '/home/a/Downloads/25/paper.pdf'


def mask(pg, rect, dpi=900):
    clip = fitz.Rect(*rect)
    pix = pg.get_pixmap(clip=clip, dpi=dpi, colorspace=fitz.csGRAY)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
    return a < 128


def trim(m):
    rs = np.where(m.any(axis=1))[0]
    cs = np.where(m.any(axis=0))[0]
    if len(rs) == 0 or len(cs) == 0:
        return None
    return m[rs.min():rs.max() + 1, cs.min():cs.max() + 1]


def row_extents(m):
    out = []
    for r in m:
        xs = np.where(r)[0]
        out.append((int(xs.min()), int(xs.max())) if len(xs) else None)
    return out


def classify_accent(m):
    """Return (label, diagnostics)."""
    h, w = m.shape
    if h < 2 or w < 2:
        return 'TINY', {}
    ext = [e for e in row_extents(m) if e]
    widths = np.array([e[1] - e[0] + 1 for e in ext], float)
    hw = h / w
    # flat bar?
    flat = widths.std() / max(widths.mean(), 1e-6)
    # wedge? compare top third to bottom third
    t = max(1, h // 3)
    topw = widths[:t].mean()
    botw = widths[-t:].mean()
    diag = {'h': h, 'w': w, 'h/w': round(hw, 2), 'flatness(std/mean)': round(float(flat), 3),
            'top_w': round(float(topw), 1), 'bot_w': round(float(botw), 1)}
    if hw <= 0.30 and flat < 0.25:
        return 'MACRON', diag
    if topw < botw * 0.72 and hw >= 0.30:
        return 'CIRCUMFLEX', diag
    if botw < topw * 0.72 and hw >= 0.30:
        return 'WEDGE-DOWN?', diag
    return 'AMBIGUOUS', diag


def classify_delim(m):
    h, w = m.shape
    ext = [e for e in row_extents(m) if e]
    widths = np.array([e[1] - e[0] + 1 for e in ext], float)
    centers = np.array([(e[0] + e[1]) / 2.0 for e in ext], float)
    runs = []
    for r in m:
        xs = np.where(r)[0]
        if len(xs) == 0:
            runs.append(0)
            continue
        runs.append(1 + int((np.diff(xs) > 1).sum()))
    n_runs = max(runs)
    hw = h / max(w, 1)
    diag = {'h': h, 'w': w, 'h/w': round(hw, 2), 'max_runs_per_row': n_runs,
            'center_span': round(float(centers.max() - centers.min()), 1)}
    if w <= 4 or hw >= 4:
        if n_runs >= 2:
            return 'DBAR', diag
        return 'BAR', diag
    span = centers.max() - centers.min()
    if span <= 1.5:
        return 'BAR', diag
    mid = centers[len(centers) // 3: 2 * len(centers) // 3].mean()
    if mid < centers.mean() - span * 0.15:
        return 'CURVE_OPEN', diag
    if mid > centers.mean() + span * 0.15:
        return 'CURVE_CLOSE', diag
    return 'AMBIGUOUS', diag


def main():
    doc = fitz.open(PDF)
    args = sys.argv[1:]
    page = int(args[0])
    pg = doc[page - 1]
    rects = [tuple(float(v) for v in args[1 + 4 * i:5 + 4 * i]) for i in range((len(args) - 1) // 4)]
    for r in rects:
        m = trim(mask(pg, r))
        if m is None:
            print('%-22s EMPTY' % (r,))
            continue
        la, da = classify_accent(m)
        ld, dd = classify_delim(m)
        print('rect %-30s  accent=%-12s %s   delim=%-12s %s'
              % (tuple(round(v, 1) for v in r), la, da, ld, dd))


main()
