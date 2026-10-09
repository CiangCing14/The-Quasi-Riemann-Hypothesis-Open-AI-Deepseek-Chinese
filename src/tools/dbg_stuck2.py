#!/usr/bin/env python3
"""Locate the exact spot that makes a stuck unit fail: show source vs output around the diff."""
import importlib.util
import sys
from collections import Counter

spec = importlib.util.spec_from_file_location('tt', '/home/a/Downloads/25/tools/tex_translate.py')
tt = importlib.util.module_from_spec(spec)
_argv = sys.argv[:]
sys.argv = ['tt', '--status']
spec.loader.exec_module(tt)

for idx in [int(x) for x in _argv[1:]] or [11, 41]:
    pre, body, bib, post = tt.load()
    units = tt.chunk_body(body)
    u = units[idx]
    for part in tt.sub_parts(u):
        got, _ = tt.ds_api.call([{'role': 'system', 'content': tt.SYSTEM},
                                 {'role': 'user', 'content': part}], max_tokens=6000,
                                temperature=0.2)
        got = got.strip()
        si, sb = tt.split_math(part)
        oi, ob = tt.split_math(got)
        cs, co = Counter(si), Counter(oi)
        if cs == co and sb == ob:
            continue
        print('=== unit %d, failing part (%d chars) ===' % (idx, len(part)))
        for k, v in cs.items():
            if co.get(k, 0) != v:
                print('   src has %d x %r, out has %d' % (v, k, co.get(k, 0)))
        for k, v in co.items():
            if cs.get(k, 0) != v:
                print('   out has %d x %r, src has %d' % (v, k, cs.get(k, 0)))
        print('--- source ---')
        print(part[:900])
        print('--- output ---')
        print(got[:900])
        break
