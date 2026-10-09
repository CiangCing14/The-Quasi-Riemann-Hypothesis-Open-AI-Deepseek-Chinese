#!/usr/bin/env python3
"""Replay the numbering and print, for every equation, the line number and the number
LaTeX would give it - so that anchors known from the compiled PDF can be verified.

usage: python3 tools/eq_lines.py [pattern ...]
"""
import re
import sys

T = open('/home/a/Downloads/25/paper.tex', encoding='utf-8').read()
lines = T.split('\n')
sec = sub = eq = 0
recs = []
i = 0
while i < len(lines):
    ln = lines[i]
    if re.match(r'\s*\\section\{', ln):
        sec += 1
        sub = 0
        eq = 0
    elif re.match(r'\s*\\subsection\{', ln):
        sub += 1
    m = re.match(r'\s*\\begin\{(equation|align|gather|multline)\}', ln)
    if m:
        env = m.group(1)
        body = [ln]
        j = i + 1
        while j < len(lines) and ('\\end{%s}' % env) not in lines[j]:
            body.append(lines[j])
            j += 1
        if j < len(lines):
            body.append(lines[j])
        blob = '\n'.join(body)
        if env == 'align':
            rows = blob.split('\\\\')
            for r in rows:
                if '\\notag' in r or '\\nonumber' in r:
                    continue
                eq += 1
                recs.append((i + 1, '%d.%d' % (sec, eq), r.strip()[:70], blob))
        else:
            eq += 1
            recs.append((i + 1, '%d.%d' % (sec, eq), blob.strip()[:70], blob))
        i = j
    i += 1

pats = sys.argv[1:]
if not pats:
    for line, num, txt, _ in recs:
        print('%5d  (%s)  %s' % (line, num, txt))
else:
    for pat in pats:
        print('=== %s ===' % pat)
        rx = re.compile(pat, re.S)
        for line, num, txt, full in recs:
            if rx.search(full):
                print('   line %5d -> (%s)  %s' % (line, num, txt))
