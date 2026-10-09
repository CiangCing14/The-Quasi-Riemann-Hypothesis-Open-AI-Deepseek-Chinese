#!/usr/bin/env python3
"""Per-page work list of the marks the text layer loses, with the exact content
each mark covers.

  RADICAL : CMEX10 'b' / 'e' glyph + its vinculum rule; radicand = spans under the rule
  OVERLINE: a short horizontal rule with text only below it
  BAR     : CMEX10 \\x0c / \\x0d (| and ||) and CMSY10 '|' / '∥'
  BIGOP   : CMEX10 'X' Σ, 'Y' ∏, 'Z' ∫  (extracted as letters - check the Chinese!)
  DELIM   : CMEX10 paren/bracket/brace code pairs

usage: python3 tools/page_worklist.py PAGE [PAGE ...]
       python3 tools/page_worklist.py 130-140
"""
import re
import sys

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'

RAD = {'b', 'e'}
BIGOP = {'X': r'\sum', 'Y': r'\prod', 'Z': r'\int'}
BARS = {0x0c: r'|', 0x0d: r'\|'}
DELIM = {0x00: '(', 0x01: ')', 0x12: '(', 0x13: ')', 0x10: '(', 0x11: ')',
         0x1a: '(', 0x1b: ')', 0x02: '[', 0x03: ']', 0x08: r'\{', 0x09: r'\}'}


def collect(pg):
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
                    chars.append({'c': ch['c'], 'bb': ch['bbox'], 'font': span['font'],
                                  'size': span['size']})
    rules = [p['rect'] for p in pg.get_drawings()
             if p['rect'].height <= 2.5 and p['rect'].width >= 1.5]
    return chars, spans, rules


def under(rule, spans, pad=14.0):
    return [(bb, t) for bb, t in spans
            if bb[2] > rule.x0 + 0.5 and bb[0] < rule.x1 - 0.5
            and bb[1] >= rule.y1 - 2.5 and bb[1] <= rule.y1 + pad]


def above(rule, spans):
    return [(bb, t) for bb, t in spans
            if bb[2] > rule.x0 + 0.5 and bb[0] < rule.x1 - 0.5
            and bb[3] <= rule.y0 + 2.0 and bb[3] >= rule.y0 - 9.0]


def line_of(bb, spans):
    """every span sharing the formula line, in reading order"""
    same = sorted([(b, t) for b, t in spans if b[1] < bb[3] + 6 and b[3] > bb[1] - 6],
                  key=lambda x: x[0][0])
    return ' '.join(t.strip() for _, t in same if t.strip())


def main():
    doc = fitz.open(PDF)
    pages = []
    for a in sys.argv[1:]:
        if '-' in a:
            lo, hi = a.split('-')
            pages += list(range(int(lo), int(hi) + 1))
        else:
            pages.append(int(a))
    for n in pages:
        pg = doc[n - 1]
        chars, spans, rules = collect(pg)
        print('=' * 78)
        print('PAGE %d' % n)
        # --- radicals
        rads = [c for c in chars if c['font'].startswith('CMEX') and c['c'] in RAD]
        for g in rads:
            vin = [r for r in rules if abs(r.y0 - g['bb'][1]) < 3.5 and r.x0 > g['bb'][2] - 3.0
                   and r.x0 < g['bb'][2] + 12.0]
            if vin:
                r = min(vin, key=lambda r: abs(r.y0 - g['bb'][1]))
                content = ' '.join(t.strip() for _, t in under(r, spans) if t.strip())
                print('  RADICAL  glyph y %.1f  vinculum x %.1f-%.1f  covers: %r'
                      % (g['bb'][1], r.x0, r.x1, content[:70]))
                print('           line: %s' % line_of(g['bb'], spans)[:150])
            else:
                print('  RADICAL? glyph y %.1f x %.1f (no vinculum found)  line: %s'
                      % (g['bb'][1], g['bb'][0], line_of(g['bb'], spans)[:110]))
        # --- overlines (excluding vinculums)
        for r in rules:
            if any(abs(r.y0 - g['bb'][1]) < 3.5 and r.x0 > g['bb'][2] - 3.0
                   and r.x0 < g['bb'][2] + 12.0 for g in rads):
                continue
            u, a = under(r, spans), above(r, spans)
            if u and not a:
                content = ' '.join(t.strip() for _, t in u if t.strip())
                print('  OVERLINE rule x %.1f-%.1f y %.1f  covers: %r'
                      % (r.x0, r.x1, r.y0, content[:70]))
                print('           line: %s' % line_of(r, spans)[:150])
        # --- big operators
        for c in chars:
            if c['font'].startswith('CMEX') and c['c'] in BIGOP:
                print('  BIGOP %-6s y %.1f x %.1f  line: %s'
                      % (BIGOP[c['c']], c['bb'][1], c['bb'][0], line_of(c['bb'], spans)[:110]))
        # --- bars and delimiters
        bars = [c for c in chars if (c['font'].startswith('CMEX') and len(c['c']) == 1
                                     and ord(c['c']) in BARS)
                or (c['font'].startswith('CMSY') and c['c'] in ('|', '∥'))]
        delims = [c for c in chars if c['font'].startswith('CMEX') and len(c['c']) == 1
                  and ord(c['c']) in DELIM]
        print('  BARS %d at y: %s' % (len(bars), ' '.join('%.0f' % b['bb'][1] for b in bars[:14])))
        print('  DELIMS %d at y: %s' % (len(delims),
                                        ' '.join('%.0f%s' % (d['bb'][1], DELIM[ord(d['c'])])
                                                 for d in delims[:14])))
        # --- zh side
        try:
            t = open('%s/page_%03d.zh.md' % (OUT, n), encoding='utf-8').read()
        except OSError:
            continue
        zc = {'sum': len(re.findall(r'\\sum', t)), 'prod': len(re.findall(r'\\prod', t)),
              'int': len(re.findall(r'\\int', t)), 'sqrt': len(re.findall(r'\\sqrt', t)),
              'overline': len(re.findall(r'\\overline|\\bar', t)),
              'abs': len(re.findall(r'\\lvert|\\rvert|\\lVert|\\rVert|\\left\||\\right\||(?<!\\)\|', t))}
        pc = {'sum': sum(1 for c in chars if c['font'].startswith('CMEX') and c['c'] == 'X'),
              'prod': sum(1 for c in chars if c['font'].startswith('CMEX') and c['c'] == 'Y'),
              'int': sum(1 for c in chars if c['font'].startswith('CMEX') and c['c'] == 'Z'),
              'sqrt': len(rads), 'overline': sum(1 for r in rules if under(r, spans) and not above(r, spans)
                                                 and not any(abs(r.y0 - g['bb'][1]) < 3.5
                                                             and r.x0 > g['bb'][2] - 3.0
                                                             and r.x0 < g['bb'][2] + 12.0 for g in rads)),
              'abs': len(bars)}
        print('  SUMMARY %s' % '  '.join('%s pdf=%d zh=%d%s' % (k, pc[k], zc[k],
                                                                '  <== GAP' if pc[k] != zc[k] else '')
                                         for k in ('sqrt', 'overline', 'sum', 'prod', 'int', 'abs')))


main()
