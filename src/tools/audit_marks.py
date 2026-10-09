#!/usr/bin/env python3
"""Audit every page: what the PDF really prints vs what the Chinese LaTeX expresses.

PDF side (font-encoded, immune to the broken ToUnicode):
  CMEX10 'X' -> \\sum        'Y' -> \\prod        'Z' -> \\int
  CMEX10 'b'/'e' -> \\sqrt    '\\x0c' -> \\left| ... \\right|
  horizontal vector rule with text only below -> \\overline
Chinese side: the corresponding macros in out/page_NNN.zh.md.

Prints one row per page with any mark, plus totals and the list of pages whose
counts disagree (that is the work list).

usage: python3 tools/audit_marks.py [start] [end]
"""
import os
import re
import sys

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'

SUM_GLYPHS = {'X': 'sum', 'Y': 'prod', 'Z': 'int', 'b': 'sqrt', 'e': 'sqrt'}
BAR_CODES = {0x0c: 'bar', 0x0d: 'dbar'}
PAREN_CODES = {0x00: '(', 0x01: ')', 0x12: '(', 0x13: ')', 0x10: '(', 0x11: ')',
               0x1a: '(', 0x1b: ')'}
BRACK_CODES = {0x02: '[', 0x03: ']'}
BRACE_CODES = {0x08: '{', 0x09: '}'}


def pdf_counts(pg):
    c = {'sum': 0, 'prod': 0, 'int': 0, 'sqrt': 0, 'bar': 0, 'dbar': 0,
         '(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0, 'overline': 0}
    spans = []
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type') != 0:
            continue
        for line in blk['lines']:
            for span in line['spans']:
                for ch in span['chars']:
                    ch_ = ch['c']
                    bb = ch['bbox']
                    spans.append((bb, ch_, span['font']))
                    if 'CMEX' in span['font']:
                        if ch_ in SUM_GLYPHS:
                            c[SUM_GLYPHS[ch_]] += 1
                        elif len(ch_) == 1 and ord(ch_) in BAR_CODES:
                            c[BAR_CODES[ord(ch_)]] += 1
                        elif len(ch_) == 1 and ord(ch_) in PAREN_CODES:
                            c[PAREN_CODES[ord(ch_)]] += 1
                        elif len(ch_) == 1 and ord(ch_) in BRACK_CODES:
                            c[BRACK_CODES[ord(ch_)]] += 1
                        elif len(ch_) == 1 and ord(ch_) in BRACE_CODES:
                            c[BRACE_CODES[ord(ch_)]] += 1
    # rules that only have text underneath = overline
    for p in pg.get_drawings():
        r = p['rect']
        if r.height > 2.5 or r.width < 1.5:
            continue
        below = any(bb[2] > r.x0 + 0.5 and bb[0] < r.x1 - 0.5
                    and bb[1] >= r.y1 - 2.0 and bb[1] <= r.y1 + 14.0 for bb, _, _ in spans)
        above = any(bb[2] > r.x0 + 0.5 and bb[0] < r.x1 - 0.5
                    and bb[3] <= r.y0 + 2.0 and bb[3] >= r.y0 - 9.0 for bb, _, _ in spans)
        if below and not above:
            c['overline'] += 1
    return c


def zh_counts(path):
    t = open(path, encoding='utf-8').read()
    return {
        'sum': len(re.findall(r'\\sum\b', t)),
        'prod': len(re.findall(r'\\prod\b', t)),
        'int': len(re.findall(r'\\int\b', t)),
        'sqrt': len(re.findall(r'\\sqrt\b', t)),
        'overline': len(re.findall(r'\\overline\b', t)) + len(re.findall(r'\\bar\b', t)),
        'abs': len(re.findall(r'\\lvert|\\rvert|\\lVert|\\rVert|\\left\||\\right\||(?<!\\)\|', t)),
    }


def main():
    args = [int(a) for a in sys.argv[1:]]
    doc = fitz.open(PDF)
    lo = args[0] if args else 1
    hi = args[1] if len(args) > 1 else doc.page_count
    tot = {}
    rows = []
    print('page| pdf: sum prod int sqrt bar | zh: sum prod int sqrt over abs | verdict')
    for n in range(lo, hi + 1):
        p = pdf_counts(doc[n - 1])
        for k, v in p.items():
            tot[k] = tot.get(k, 0) + v
        pth = os.path.join(OUT, 'page_%03d.zh.md' % n)
        if not os.path.exists(pth):
            continue
        z = zh_counts(pth)
        bad = []
        if p['sum'] != z['sum']:
            bad.append('sum %d/%d' % (p['sum'], z['sum']))
        if p['prod'] != z['prod']:
            bad.append('prod %d/%d' % (p['prod'], z['prod']))
        if p['int'] != z['int']:
            bad.append('int %d/%d' % (p['int'], z['int']))
        if p['sqrt'] and not z['sqrt']:
            bad.append('sqrt %d/0' % p['sqrt'])
        if p['overline'] and not z['overline']:
            bad.append('overline %d/0' % p['overline'])
        if any(v for k, v in p.items() if k in '()[]{}'):
            if not re.search(r'\\left|\\right|\\big|\\Big', open(pth, encoding='utf-8').read()):
                bad.append('delims')
        if bad:
            rows.append((n, bad))
            print('%4d| %3d %4d %3d %4d %3d | %3d %4d %3d %4d %3d %3d | %s'
                  % (n, p['sum'], p['prod'], p['int'], p['sqrt'], p['bar'],
                     z['sum'], z['prod'], z['int'], z['sqrt'], z['overline'], z['abs'],
                     '; '.join(bad)))
    print()
    print('PDF TOTALS: %s' % {k: v for k, v in sorted(tot.items()) if v})
    print('pages with a count mismatch: %d' % len(rows))
    print('  ' + ' '.join(str(n) for n, _ in rows))


main()
