#!/usr/bin/env python3
"""Census of glyph codes whose ToUnicode is broken.

Every glyph the text layer cannot name keeps a stable *code* inside the font
(cmex10 for big delimiters / radicals, cmsy10 for bars and accents).  The code
is the same wherever it appears, so each code needs to be identified once and
can then be used to classify every occurrence document-wide.

Prints, per (font, code): occurrence count and the first few sample boxes.

usage: python3 tools/code_census.py
"""
from collections import defaultdict

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
doc = fitz.open(PDF)

seen = defaultdict(list)
for n in range(doc.page_count):
    pg = doc[n]
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type') != 0:
            continue
        for line in blk['lines']:
            for span in line['spans']:
                for ch in span['chars']:
                    c = ch['c']
                    if len(c) == 1 and ord(c) < 32 or c == '\ufffd' or c == '':
                        key = (span['font'], ord(c) if c else -1, round(span['size'], 1))
                        if len(seen[key]) < 6:
                            seen[key].append((n + 1, tuple(round(v, 1) for v in ch['bbox'])))
                        else:
                            seen[key].append(None)

print('%-12s %-5s %-5s %-6s %s' % ('font', 'code', 'uni', 'count', 'samples (page, x0,y0,x1,y1)'))
for (font, code, size), samples in sorted(seen.items(), key=lambda kv: (kv[0][0], kv[0][1])):
    n = len([s for s in samples if s]) + len([s for s in samples if s is None])
    cnt = len(samples) if None in samples else len(samples)
    real = [s for s in samples if s]
    print('%-12s %-5d %-5s %-6s %s' % (font, code, 'U+%04X' % code, cnt if None in samples else cnt,
                                       ' '.join('%d:%s' % (p, b) for p, b in real[:4])))
