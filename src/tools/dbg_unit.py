#!/usr/bin/env python3
"""Show exactly where a translated unit's math/ref sequence drifts from the source."""
import difflib
import importlib.util
import sys

spec = importlib.util.spec_from_file_location('tt', '/home/a/Downloads/25/tools/tex_translate.py')
tt = importlib.util.module_from_spec(spec)
_argv = sys.argv[:]
sys.argv = ['tt', '--status']
spec.loader.exec_module(tt)

idx = int(_argv[1]) if len(_argv) > 1 else 0
pre, body, bib, post = tt.load()
units = tt.chunk_body(body)
u = units[idx]
got, usage = tt.ds_api.call([{'role': 'system', 'content': tt.SYSTEM},
                             {'role': 'user', 'content': u}], max_tokens=8000, temperature=0.2)
got = got.strip()
sm, om = tt.math_seq(u), tt.math_seq(got)
sr, orr = tt.ref_seq(u), tt.ref_seq(got)
print('math: src %d out %d | refs: src %d out %d' % (len(sm), len(om), len(sr), len(orr)))
print('--- math differences ---')
n = 0
for line in difflib.unified_diff(sm, om, lineterm='', n=0):
    if line.startswith(('---', '+++', '@@')):
        continue
    print('   ' + line[:200])
    n += 1
    if n > 24:
        print('   ...')
        break
print('--- ref differences ---')
for line in difflib.unified_diff(sr, orr, lineterm='', n=0):
    if line.startswith(('---', '+++', '@@')):
        continue
    print('   ' + line[:200])
