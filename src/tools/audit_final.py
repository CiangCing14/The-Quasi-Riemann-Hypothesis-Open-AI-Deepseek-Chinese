#!/usr/bin/env python3
"""DEFINITIVE audit: every mark the text layer loses, PDF vs Chinese LaTeX.

Glyph decoding (verified against rendered pixels):
  CMEX10 'X'->\\sum  'Y'->\\prod  'Z'->\\int
  CMEX10 'b'/'e' -> accent (circumflex \\hat) when nothing sits to its right at its
        own height, else the RADICAL sign \\sqrt whose vinculum is the rule attached
        to its top-right corner
  CMEX10 \\x0c -> |   \\x0d -> \\|  (these come in stacked pieces: 4 pieces = 1 tall
        delimiter, so pieces are clustered by x before counting)
  CMEX10 \\x00/\\x01, \\x12/\\x13, \\x10/\\x11, \\x1a/\\x1b -> ( ) in four size classes
  CMEX10 \\x02/\\x03 -> [ ]   \\x08/\\x09 -> { }   CMSY10 '|' '\\u2225' -> | \\|
  horizontal vector rule with text only below -> \\overline

usage:
  python3 tools/audit_final.py                 # per-page table + totals
  python3 tools/audit_final.py --worklists 135 149 ...
  python3 tools/audit_final.py --page 149      # full detail for one page
"""
import json
import os
import re
import sys

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'
WL = '/home/a/Downloads/25/tools/worklists'

BIGOP = {'X': 'sum', 'Y': 'prod', 'Z': 'int'}
RADCH = {'b', 'e'}
BARCODE = {0x0c: 'bar', 0x0d: 'dbar'}
PAREN = {0x00: '(', 0x01: ')', 0x12: '(', 0x13: ')', 0x10: '(', 0x11: ')',
         0x1a: '(', 0x1b: ')'}
BRACK = {0x02: '[', 0x03: ']'}
BRACE = {0x08: '{', 0x09: '}'}


def page_items(pg):
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

    def under(r, pad=14.0):
        return [(bb, t) for bb, t in spans if bb[2] > r.x0 + 0.5 and bb[0] < r.x1 - 0.5
                and bb[1] >= r.y1 - 2.5 and bb[1] <= r.y1 + pad]

    def above(r):
        return [(bb, t) for bb, t in spans if bb[2] > r.x0 + 0.5 and bb[0] < r.x1 - 0.5
                and bb[3] <= r.y0 + 2.0 and bb[3] >= r.y0 - 9.0]

    def line_of(bb):
        y0 = bb[1]
        same = sorted([(b, t) for b, t in spans if abs(b[1] - y0) < 3.5 or (b[1] < bb[3] and b[3] > bb[1])],
                      key=lambda x: x[0][0])
        return ' '.join(t.strip() for _, t in same if t.strip())

    items = {'radical': [], 'accent': [], 'overline': [], 'bar': [], 'dbar': [],
             'paren': [], 'brack': [], 'brace': [], 'sum': [], 'prod': [], 'int': []}
    for c in chars:
        f, ch, bb = c['font'], c['c'], c['bb']
        if f.startswith('CMEX'):
            if ch in BIGOP:
                items[BIGOP[ch]].append({'bb': bb, 'line': line_of(bb)})
                continue
            if ch in RADCH:
                vin = [r for r in rules if abs(r.y0 - bb[1]) < 4.0
                       and bb[2] - 4.0 < r.x0 < bb[2] + 12.0]
                if vin:
                    r = min(vin, key=lambda r: abs(r.y0 - bb[1]))
                    items['radical'].append({'bb': bb, 'rule': tuple(r),
                                             'content': ' '.join(t.strip() for _, t in under(r) if t.strip()),
                                             'line': line_of(bb)})
                else:
                    items['accent'].append({'bb': bb, 'line': line_of(bb)})
                continue
            if len(ch) == 1 and ord(ch) in BARCODE:
                items[BARCODE[ord(ch)]].append({'bb': bb})
                continue
            if len(ch) == 1 and ord(ch) in PAREN:
                items['paren'].append({'bb': bb, 'ch': PAREN[ord(ch)]})
                continue
            if len(ch) == 1 and ord(ch) in BRACK:
                items['brack'].append({'bb': bb, 'ch': BRACK[ord(ch)]})
                continue
            if len(ch) == 1 and ord(ch) in BRACE:
                items['brace'].append({'bb': bb, 'ch': BRACE[ord(ch)]})
                continue
        if f.startswith('CMSY') and ch in ('|', '\u2225'):
            items['bar'].append({'bb': bb})
    for r in rules:
        if any(abs(r.y0 - g['bb'][1]) < 4.0 and g['bb'][2] - 4.0 < r.x0 < g['bb'][2] + 12.0
               for g in ([c for c in chars if c['font'].startswith('CMEX') and c['c'] in RADCH])):
            continue
        u, a = under(r), above(r)
        if u and not a:
            items['overline'].append({'rule': tuple(r),
                                      'content': ' '.join(t.strip() for _, t in u if t.strip()),
                                      'line': line_of(r)})
    return items, spans


def cluster_bars(lst):
    """collapse stacked pieces (same x, consecutive y) into one delimiter"""
    out = []
    for it in sorted(lst, key=lambda i: (round(i['bb'][0], 1), i['bb'][1])):
        for o in out:
            if abs(o['bb'][0] - it['bb'][0]) < 2.0 and it['bb'][1] - o['yv'][1] < 3.5:
                o['yv'] = (o['yv'][0], it['bb'][3])
                o['n'] = o.get('n', 1) + 1
                break
        else:
            out.append({'bb': it['bb'], 'yv': (it['bb'][1], it['bb'][3]), 'n': 1})
    return out


def zh_counts(path):
    t = open(path, encoding='utf-8').read()
    named = len(re.findall(r'\\lvert|\\rvert|\\lVert|\\rVert|\\left\||\\right\||\\mid(?![a-z])', t))
    plain = len(re.findall(r'(?<!\\left)(?<!\\right)(?<!\\lvert)(?<!\\rvert)(?<!\\lVert)(?<!\\rVert)(?<!\\)\|', t))
    return {'sum': len(re.findall(r'\\sum', t)), 'prod': len(re.findall(r'\\prod', t)),
            'int': len(re.findall(r'\\int', t)), 'sqrt': len(re.findall(r'\\sqrt', t)),
            'overline': len(re.findall(r'\\overline|\\bar(?!\w)', t)),
            'hat': len(re.findall(r'\\hat|\\widehat', t)),
            'abs': named + plain}


def counts_of(items):
    return {'sum': len(items['sum']), 'prod': len(items['prod']), 'int': len(items['int']),
            'sqrt': len(items['radical']), 'overline': len(items['overline']),
            'hat': len(items['accent']),
            'abs': len(cluster_bars(items['bar'])) + len(cluster_bars(items['dbar']))}


def main():
    doc = fitz.open(PDF)
    args = sys.argv[1:]
    if '--page' in args:
        n = int(args[args.index('--page') + 1])
        items, spans = page_items(doc[n - 1])
        print(json.dumps({k: v for k, v in items.items() if v}, indent=1, ensure_ascii=False))
        print('counts:', counts_of(items))
        return
    if '--worklists' in args:
        os.makedirs(WL, exist_ok=True)
        pages = [int(a) for a in args if a.isdigit()]
        for n in pages:
            items, _ = page_items(doc[n - 1])
            lines = ['PAGE %d' % n, 'counts pdf: %s' % counts_of(items), '']
            for k in ('radical', 'overline', 'accent', 'sum', 'prod', 'int', 'paren', 'brack', 'brace', 'bar', 'dbar'):
                for it in items[k]:
                    bb = it.get('bb') or it.get('rule')
                    lines.append('%-9s y %6.1f x %6.1f-%6.1f %s%s'
                                 % (k.upper(), bb[1], bb[0], bb[2],
                                    ('covers: %r' % it['content']) if it.get('content') else '',
                                    ('ch=%s' % it['ch']) if it.get('ch') else ''))
                    if it.get('line'):
                        lines.append('          line: %s' % it['line'][:170])
            open('%s/page_%03d.txt' % (WL, n), 'w', encoding='utf-8').write('\n'.join(lines))
        print('worklists written to %s for %s' % (WL, pages))
        return
    tot_p, tot_z = {}, {}
    gaps = []
    print('page | pdf: sqrt over hat abs sum prod int | zh: sqrt over hat abs sum prod int | gaps')
    for n in range(1, doc.page_count + 1):
        items, _ = page_items(doc[n - 1])
        p = counts_of(items)
        for k, v in p.items():
            tot_p[k] = tot_p.get(k, 0) + v
        pth = '%s/page_%03d.zh.md' % (OUT, n)
        if not os.path.exists(pth):
            continue
        z = zh_counts(pth)
        for k, v in z.items():
            tot_z[k] = tot_z.get(k, 0) + v
        g = [k for k in ('sqrt', 'overline', 'hat', 'abs') if p[k] != z[k]]
        if g:
            gaps.append(n)
            print('%4d | %4d %4d %3d %3d %4d %3d %3d | %4d %4d %3d %3d %4d %3d %3d | %s'
                  % (n, p['sqrt'], p['overline'], p['hat'], p['abs'], p['sum'], p['prod'], p['int'],
                     z['sqrt'], z['overline'], z['hat'], z['abs'], z['sum'], z['prod'], z['int'],
                     ' '.join('%s %d/%d' % (k, p[k], z[k]) for k in g)))
    print()
    print('PDF totals: %s' % {k: v for k, v in sorted(tot_p.items()) if v})
    print('ZH  totals: %s' % {k: v for k, v in sorted(tot_z.items()) if v})
    print('pages with a gap: %d  -> %s' % (len(gaps), gaps))


main()
