#!/usr/bin/env python3
"""Audit: does each page carry the same number of hat-accent glyphs as \\hat macros?

The paper writes the log-norm accent as a circumflex glyph that pdftotext extracts
as the character 'b'.  Geometrically it is a small token (height <= ~7.6) whose
x-range sits exactly over a full-size letter and whose y0 is ~7pt below the
letter's y0 (that is how the accent glyph's box is reported).  Counting those
tokens gives an independent check that every accent in the source is rendered by
a \\hat in the translation.

usage: python3 tools/hat_audit.py 129 132 ...
"""
import re
import subprocess
import sys

ROOT = '/home/a/Downloads/25'
ACCENT_CHARS = set('b^ˆ˘~')


def tokens(page):
    xml = '/tmp/hat_%d.xml' % page
    subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page),
                    ROOT + '/paper.pdf', xml], check=True)
    raw = open(xml, encoding='utf-8').read()
    out = []
    for a, b, c, d, t in re.findall(
            r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', raw):
        out.append((float(a), float(b), float(c), float(d),
                    t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')))
    return out


def accents(page):
    ws = tokens(page)
    big = [w for w in ws if (w[3] - w[1]) >= 9.2]
    found = []
    for a, b, c, d, t in ws:
        h = d - b
        if h > 8.0 or t.strip() not in ACCENT_CHARS:
            continue
        for A, B, C, D, T in big:
            ov = min(c, C) - max(a, A)
            if ov > 0.5 * (c - a) and 4.0 <= (b - B) <= 9.5:
                found.append((t, T, round(a, 1), round(b, 1), round(B, 1)))
                break
    return found


for pg in [int(x) for x in sys.argv[1:]]:
    f = accents(pg)
    zh = open('%s/out/page_%03d.zh.md' % (ROOT, pg), encoding='utf-8').read()
    nhat = len(re.findall(r'\\hat', zh))
    status = 'OK' if abs(len(f) - nhat) <= 1 else 'MISMATCH'
    print('page_%03d  accent-glyphs=%2d  \\hat-macros=%2d  %s' % (pg, len(f), nhat, status))
    if status == 'MISMATCH':
        for t, T, x, y, Y in f:
            print('        glyph %r over %r at x=%.1f (accent y=%.1f, letter y=%.1f)' % (t, T, x, y, Y))
