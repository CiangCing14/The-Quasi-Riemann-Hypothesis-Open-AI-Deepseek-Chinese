#!/usr/bin/env python3
"""Compare the source's \\section/\\subsection titles with the headings emitted in the md."""
import re
from collections import Counter

T = open('/home/a/Downloads/25/paper.tex', encoding='utf-8').read()
MD = open('/home/a/Downloads/25/paper-zh-cn.md', encoding='utf-8').read()


def cmd_arg(s, cmd):
    i = s.find(cmd)
    if i < 0:
        return None
    try:
        j = s.index('{', i)
    except ValueError:
        return None
    depth = 0
    for k in range(j, len(s)):
        if s[k] == '{':
            depth += 1
        elif s[k] == '}':
            depth -= 1
            if depth == 0:
                return s[j + 1:k]
    return None


src_sec = [cmd_arg(m.group(0), '\\section') for m in re.finditer(r'\\section\*?\{', T)]
src_sub = [cmd_arg(m.group(0), '\\subsection') for m in re.finditer(r'\\subsection\*?\{', T)]
print('source: %d sections, %d subsections' % (len(src_sec), len(src_sub)))

md_sec = [m.group(1) for m in re.finditer(r'^## (.*)$', MD, re.M)]
md_sub = [m.group(1) for m in re.finditer(r'^### (.*)$', MD, re.M)]
print('md    : %d h2, %d h3' % (len(md_sec), len(md_sub)))
print()
print('--- source section titles ---')
for i, s in enumerate(src_sec, 1):
    print('%3d. %s' % (i, (s or '?')[:70]))
print()
print('--- md h2 headings ---')
for s in md_sec:
    print('    %s' % s[:70])
print()
# subsections per section
print('--- subsections per source section ---')
cur = 0
cnt = {}
for m in re.finditer(r'\\section\*?\{|\\subsection\*?\{', T):
    if m.group(0).startswith('\\section'):
        cur += 1
        cnt[cur] = 0
    else:
        cnt[cur] = cnt.get(cur, 0) + 1
print(cnt)
print('--- quasi-Riemann wording in the body ---')
print('准黎曼 %d | 拟黎曼 %d' % (MD.count('准黎曼'), MD.count('拟黎曼')))
