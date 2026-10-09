#!/usr/bin/env python3
"""Semantic resolver helper: find where a symbol is defined / used in the paper.

usage:  python3 tools/sym_grep.py "sslot" "Aker,1" ...

Searches the English page extracts (pages/*.txt) and the Chinese translations
(out/*.zh.md) for a symbol, tolerating the spaces and broken subscripts that
pdftotext inserts ("s slot", "r max", "Dmax").  Prints, per hit:

    file:line  ...context...            <- the raw evidence

so a formula can be settled from the paper's own usage instead of guesswork.
"""
import glob
import os
import re
import sys

ROOT = '/home/a/Downloads/25'
WINDOW = 170


def flex(pat):
    """'sslot' -> regex matching s\s*slot ; keeps punctuation literal."""
    chars = [re.escape(c) if c.isalnum() else re.escape(c) for c in pat]
    return r'\s?'.join(chars)


def show(files, rx, label):
    hits = 0
    for f in sorted(files):
        try:
            lines = open(f, encoding='utf-8').read().split('\n')
        except Exception:
            continue
        for i, ln in enumerate(lines, 1):
            for m in rx.finditer(ln):
                a = max(0, m.start() - WINDOW // 2)
                b = min(len(ln), m.end() + WINDOW)
                print('   %s %-22s L%-4d ...%s...' % (label, os.path.basename(f), i,
                                                      ln[a:b].strip()))
                hits += 1
                if hits > 40:
                    return hits
    return hits


def main():
    pats = sys.argv[1:]
    if not pats:
        print(__doc__)
        return 2
    files_en = glob.glob(os.path.join(ROOT, 'pages', 'page_*.txt'))
    files_zh = glob.glob(os.path.join(ROOT, 'out', 'page_*.zh.md'))
    for p in pats:
        print('=' * 78)
        print('SYMBOL: %r' % p)
        rx = re.compile(flex(p), re.I)
        n1 = show(files_en, rx, 'EN')
        n2 = show(files_zh, rx, 'ZH')
        print('   (%d english hits, %d chinese hits)' % (n1, n2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
