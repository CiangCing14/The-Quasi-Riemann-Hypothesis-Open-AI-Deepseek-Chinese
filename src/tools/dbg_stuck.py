#!/usr/bin/env python3
"""Inspect the smallest failing sub-part of a stuck unit: source snippet inventory vs output."""
import importlib.util
import re
import sys

spec = importlib.util.spec_from_file_location('tt', '/home/a/Downloads/25/tools/tex_translate.py')
tt = importlib.util.module_from_spec(spec)
_argv = sys.argv[:]
sys.argv = ['tt', '--status']
spec.loader.exec_module(tt)

idx = int(_argv[1]) if len(_argv) > 1 else 41
pre, body, bib, post = tt.load()
units = tt.chunk_body(body)
u = units[idx]
parts = tt.sub_parts(u)
print('unit %d: %d chars, %d parts' % (idx, len(u), len(parts)))
part = min(parts, key=len)
print('=== source part (%d chars) ===' % len(part))
print(part[:700])
print('=== source inline snippets ===')
print(tt.split_math(part)[0])
got, _ = tt.ds_api.call([{'role': 'system', 'content': tt.SYSTEM},
                         {'role': 'user', 'content': part}], max_tokens=4000, temperature=0.2)
got = got.strip()
print('=== model output ===')
print(got[:700])
print('=== output inline snippets ===')
print(tt.split_math(got)[0])
