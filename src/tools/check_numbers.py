#!/usr/bin/env python3
"""Validate the computed equation/theorem numbering against the numbers that appear
in the previous (PDF-derived) translation, which carried LaTeX's own numbers.

usage: python3 tools/check_numbers.py
"""
import re
from collections import defaultdict

OLD = '/home/a/Downloads/25/out'            # per-page Chinese translation (PDF-derived)
import glob


def old_max_per_section():
    mx = defaultdict(int)
    for f in glob.glob(OLD + '/page_*.zh.md'):
        t = open(f, encoding='utf-8').read()
        for m in re.finditer(r'\\tag\{(\d+)\.(\d+)\}', t):
            s, e = int(m.group(1)), int(m.group(2))
            mx[s] = max(mx[s], e)
        for m in re.finditer(r'\((\d+)\.(\d+)\)', t):
            s, e = int(m.group(1)), int(m.group(2))
            if e < 400:
                mx[s] = max(mx[s], e)
    return mx


def new_max_per_section():
    """replay the numbering over the tex and report the last equation number per section"""
    import importlib.util
    spec = importlib.util.spec_from_file_location('tm', '/home/a/Downloads/25/tools/tex_md.py')
    tm = importlib.util.module_from_spec(spec)
    import sys
    sys.argv = ['tm', '--dry']
    spec.loader.exec_module(tm)
    text = open('/home/a/Downloads/25/paper.tex', encoding='utf-8').read()
    nb = tm.build_numbers(text)
    # count equations per section by walking again
    mx = defaultdict(int)
    sec = 0
    eq = 0
    for m in re.finditer(r'\\section\{|\\begin\{(equation|align|gather|multline)\}', text):
        if m.group(0) == '\\section{':
            sec += 1
            eq = 0
        else:
            eq += 1
            mx[sec] = eq
    return mx


old = old_max_per_section()
new = new_max_per_section()
print('sec | old-translation max | computed max | match')
bad = 0
for s in sorted(set(list(old) + list(new))):
    o, n = old.get(s, 0), new.get(s, 0)
    ok = 'OK' if o == n else ('(old <= new)' if o <= n else 'MISMATCH')
    if o != n:
        bad += 1
    print('%3d | %6d | %6d | %s' % (s, o, n, ok))
print('sections differing: %d' % bad)
