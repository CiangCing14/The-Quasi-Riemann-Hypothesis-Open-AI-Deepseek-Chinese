#!/usr/bin/env python3
"""Whole-document audit: the translated .tex must carry exactly the same mathematics,
references and environments as paper.tex (only the prose may differ)."""
import importlib.util
import re
import sys
from collections import Counter

spec = importlib.util.spec_from_file_location('tt', '/home/a/Downloads/25/tools/tex_translate.py')
tt = importlib.util.module_from_spec(spec)
sys.argv = ['tt', '--status']
spec.loader.exec_module(tt)

src = open('/home/a/Downloads/25/paper.tex', encoding='utf-8').read()
zh = open('/home/a/Downloads/25/build/paper-zh-cn.tex', encoding='utf-8').read()


def inv(t):
    pre, body, bib, post = (t[:t.index('\\begin{document}')],
                            t[t.index('\\begin{document}'):t.index('\\begin{thebibliography}')],
                            t[t.index('\\begin{thebibliography}'):t.index('\\end{thebibliography}')],
                            t[t.index('\\end{thebibliography}'):])
    si, sb = tt.split_math(body)
    return dict(inline=Counter(si), block=sb, refs=Counter(tt.ref_seq(body)),
                chars=len(body), pre=len(pre), bib=len(bib), post=len(post))


a, b = inv(src), inv(zh)
print('body chars      src %d -> zh %d' % (a['chars'], b['chars']))
print('preamble chars  src %d -> zh %d (preamble is copied verbatim)' % (a['pre'], b['pre']))
print('bibliography    src %d -> zh %d (kept in English)' % (a['bib'], b['bib']))
print('inline math     src %d -> zh %d  identical=%s'
      % (sum(a['inline'].values()), sum(b['inline'].values()), a['inline'] == b['inline']))
print('display blocks  src %d -> zh %d  identical=%s'
      % (len(a['block']), len(b['block']), a['block'] == b['block']))
print('refs/labels     src %d -> zh %d  identical=%s'
      % (sum(a['refs'].values()), sum(b['refs'].values()), a['refs'] == b['refs']))
if a['inline'] != b['inline']:
    for k, v in (a['inline'] - b['inline']).items():
        print('   LOST %d x %r' % (v, k[:80]))
    for k, v in (b['inline'] - a['inline']).items():
        print('   ADDED %d x %r' % (v, k[:80]))
if a['block'] != b['block']:
    for m in a['block']:
        if m not in b['block']:
            print('   LOST block %r' % m[:100])
if a['refs'] != b['refs']:
    for k, v in (a['refs'] - b['refs']).items():
        print('   LOST ref %d x %r' % (v, k))
    for k, v in (b['refs'] - a['refs']).items():
        print('   ADDED ref %d x %r' % (v, k))
# how much English prose is left outside math?
zh_prose = tt.MATH_RE.sub(' ', zh[zh.index('\\begin{document}'):])
en = re.findall(r'[A-Za-z]{4,}', zh_prose)
print('english words left outside math: %d (proper nouns / terms): %s' % (len(en), en[:12]))
