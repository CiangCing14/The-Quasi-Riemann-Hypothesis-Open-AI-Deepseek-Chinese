#!/usr/bin/env python3
"""Normalise beta-star to a SUBSCRIPT.

Geometry (page 82: star box y156.5-164.0 vs beta y153.3-162.9; page 8: star on a
lower line) shows the paper writes beta with a *subscript* star, exactly as the
already-correct pages do (\\beta_*).  16 pages carry it wrongly as \\beta^*.
"""
import glob
import re

ROOT = '/home/a/Downloads/25/out'
changed = 0
total = 0
for p in sorted(glob.glob(ROOT + '/page_*.zh.md')):
    t = open(p, encoding='utf-8').read()
    new, n = re.subn(r'\\beta\^\s*\{?\s*\\?\*?\s*\}?', r'\\beta_{*}', t)
    if n and new != t:
        open(p, 'w', encoding='utf-8').write(new)
        changed += 1
        total += n
        print('  %s  %d occurrence(s)' % (p.split('/')[-1], n))
print('normalised %d occurrence(s) on %d page(s)' % (total, changed))
