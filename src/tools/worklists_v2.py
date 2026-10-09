#!/usr/bin/env python3
"""V2 work list = letter alphabets (\\mathcal / \\mathfrak / \\mathbb) + big-operator limits.

Writes tools/worklists_v2/page_NNN.txt for every page that needs either job, so one
worker owns a page and the two jobs cannot race on the same file.

usage: python3 tools/worklists_v2.py
"""
import os
import re
import subprocess

import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
OUT = '/home/a/Downloads/25/out'
SRC = '/home/a/Downloads/25/tools/worklists_alpha'
DST = '/home/a/Downloads/25/tools/worklists_v2'


def main():
    os.makedirs(DST, exist_ok=True)
    doc = fitz.open(PDF)
    pages = sorted(int(f[5:8]) for f in os.listdir(SRC) if f.startswith('page_'))
    # add pages whose multi-line limits need checking
    for n in range(1, doc.page_count + 1):
        r = subprocess.run(['python3', '/home/a/Downloads/25/tools/limit_check.py', str(n)],
                           capture_output=True, text=True).stdout
        if r.count('below[1]') or r.count('above[1]'):
            if n not in pages:
                pages.append(n)
    pages = sorted(set(pages))
    for n in pages:
        parts = []
        ap = '%s/page_%03d.txt' % (SRC, n)
        if os.path.exists(ap):
            parts.append(open(ap, encoding='utf-8').read())
        lim = subprocess.run(['python3', '/home/a/Downloads/25/tools/limit_check.py', str(n)],
                             capture_output=True, text=True).stdout.strip()
        if lim:
            parts.append('\n---- BIG-OPERATOR LIMITS (compare with the Chinese subscripts) ----\n' + lim)
        try:
            zh = open('%s/page_%03d.zh.md' % (OUT, n), encoding='utf-8').read()
        except OSError:
            continue
        subs = len(re.findall(r'\\substack', zh))
        nl = len(re.findall(r'\\\\', zh))
        parts.append('\n---- Chinese file today: \\substack x%d, line breaks \\\\ x%d ----' % (subs, nl))
        open('%s/page_%03d.txt' % (DST, n), 'w', encoding='utf-8').write('\n'.join(parts))
    print('worklists_v2 for %d pages' % len(pages))
    print(pages)
    open('/tmp/v2pages.txt', 'w').write(' '.join(map(str, pages)))


main()
