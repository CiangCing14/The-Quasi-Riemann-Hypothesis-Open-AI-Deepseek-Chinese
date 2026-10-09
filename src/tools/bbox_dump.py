#!/usr/bin/env python3
"""Geometry dumper: recover sub/superscript structure of a PDF page.

usage:  python3 tools/bbox_dump.py <page> [y0 y1]

Prints, for the given PDF page, every text token with its x/y box so that
sub- and superscripts can be identified unambiguously, plus a compact
"visual line" view where tokens of the same baseline are joined and
smaller/offset tokens are marked  ^up  /  vdn  (with their x offset).
This is the authoritative source of truth for rebuilding LaTeX.
"""
import re
import subprocess
import sys

ROOT = '/home/a/Downloads/25'


def load(page):
    xml = '/tmp/bbox_%d.xml' % page
    subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page),
                    ROOT + '/paper.pdf', xml], check=True)
    raw = open(xml, encoding='utf-8').read()
    out = []
    for a, b, c, d, t in re.findall(
            r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', raw):
        t = (t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
             .replace('&#39;', "'").replace('&quot;', '"'))
        out.append((float(a), float(b), float(c), float(d), t))
    return out


def main():
    page = int(sys.argv[1])
    lo = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    hi = float(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
    ws = [w for w in load(page) if lo <= w[1] <= hi]
    ws.sort(key=lambda w: (round(w[1]), w[0]))

    # baseline clusters: words sharing (approximately) the same y0
    lines = []
    for x0, y0, x1, y1, t in ws:
        for ln in lines:
            if abs(ln['y0'] - y0) < 1.6:
                ln['ws'].append((x0, y0, x1, y1, t))
                break
        else:
            lines.append({'y0': y0, 'ws': [(x0, y0, x1, y1, t)]})
    lines.sort(key=lambda l: l['y0'])

    for ln in lines:
        ln['ws'].sort()
        base = max((w[3] - w[1]) for w in ln['ws'])
        ref_hi = min(w[1] for w in ln['ws'] if (w[3] - w[1]) >= base - 0.8)
        ref_lo = max(w[3] for w in ln['ws'] if (w[3] - w[1]) >= base - 0.8)
        parts = []
        for x0, y0, x1, y1, t in ln['ws']:
            small = (y1 - y0) < base - 0.7
            mark = ''
            if small:
                if y1 <= ref_hi + 0.9:
                    mark = '^'          # raised: superscript
                elif y0 >= ref_lo - 0.9:
                    mark = 'v'          # lowered: subscript
                else:
                    mark = '~'          # odd height (rule, brace, sqrt, ...)
            parts.append('%s%s' % (mark, t))
        print('y=%7.1f (base %.1f) | %s' % (ln['y0'], base, ' '.join(parts)))

    print()
    print('=== raw tokens (x0, y0, x1, y1, token) — use for fractions / big ops ===')
    for x0, y0, x1, y1, t in ws:
        print('   x %6.1f-%6.1f   y %6.1f-%6.1f   %s' % (x0, x1, y0, y1, t))


if __name__ == '__main__':
    main()
