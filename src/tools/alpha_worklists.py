#!/usr/bin/env python3
"""Work lists for the three lost letter alphabets.

  CMSY10 ASCII letters -> \\mathcal{X}
  EUFM10 letters       -> \\mathfrak{X}   (Euler Fraktur)
  MSBM10 letters       -> \\mathbb{X}     (AMS blackboard bold)
The extraction hands all of them over as plain letters, so a translation silently
loses the font - and the paper does use plain and calligraphic letters as different
objects.

Per page and per alphabet: the glyph count, the letters involved, each glyph's
position and formula line, and how many of the matching macro the Chinese uses.

usage: python3 tools/alpha_worklists.py            # summary + gap list
       python3 tools/alpha_worklists.py --write    # write tools/worklists_alpha/
"""
import os
import re
import sys
from collections import Counter

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'
WDIR = '/home/a/Downloads/25/tools/worklists_alpha'
FONTS = {'CMSY': ('\\mathcal', r'\\mathcal\{'), 'EUFM': ('\\mathfrak', r'\\mathfrak\{'),
         'MSBM': ('\\mathbb', r'\\mathbb\{')}


def main():
    doc = fitz.open(PDF)
    write = '--write' in sys.argv
    if write:
        os.makedirs(WDIR, exist_ok=True)
    gap_pages = []
    for n in range(1, doc.page_count + 1):
        spans, per = [], {k: [] for k in FONTS}
        for blk in doc[n - 1].get_text('rawdict')['blocks']:
            if blk.get('type') != 0:
                continue
            for line in blk['lines']:
                for span in line['spans']:
                    txt = ''.join(c['c'] for c in span['chars'])
                    if txt.strip():
                        spans.append((span['bbox'], txt))
                    for key in FONTS:
                        if span['font'].startswith(key):
                            for ch in span['chars']:
                                if ch['c'].isascii() and ch['c'].isalpha():
                                    per[key].append((ch['c'], ch['bbox']))
        pth = '%s/page_%03d.zh.md' % (OUT, n)
        if not os.path.exists(pth):
            continue
        t = open(pth, encoding='utf-8').read()
        cur = {k: len(re.findall(FONTS[k][1], t)) for k in FONTS}
        gaps = {k: len(per[k]) - cur[k] for k in FONTS}
        if not any(v > 0 for v in gaps.values()):
            continue
        gap_pages.append(n)
        if not write:
            continue
        lines = ['PAGE %d   (pdf glyphs vs Chinese macros)' % n]
        for k in ('CMSY', 'EUFM', 'MSBM'):
            if not per[k]:
                continue
            lines.append('%s -> %s : pdf %d glyph(s) %s | zh %d'
                         % (k, FONTS[k][0], len(per[k]),
                            ' '.join('%s%d' % (a, b) for a, b in Counter(c for c, _ in per[k]).most_common()),
                            cur[k]))
            for ch, bb in sorted(per[k], key=lambda g: (g[1][1], g[1][0])):
                same = sorted([(b, s) for b, s in spans if abs(b[1] - bb[1]) < 3.5],
                              key=lambda x: x[0][0])
                line = ' '.join(s.strip() for _, s in same if s.strip())
                lines.append('   %s %s  y %6.1f x %6.1f   line: %s'
                             % (FONTS[k][0], ch, bb[1], bb[0], line[:150]))
        open('%s/page_%03d.txt' % (WDIR, n), 'w', encoding='utf-8').write('\n'.join(lines))
    print('pages needing an alphabet fix: %d' % len(gap_pages))
    print(gap_pages)


main()
