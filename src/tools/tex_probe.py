#!/usr/bin/env python3
"""Quick census of the LaTeX source constructs that matter for the translator."""
import re

T = open('/home/a/Downloads/25/paper.tex', encoding='utf-8').read()
print('chars: %d lines: %d' % (len(T), T.count('\n')))
print('\ndelimiters:')
for name, pat in [('$$', r'\$\$'), ('$', r'(?<!\$)\$(?!\$)'), (r'\\[', r'\\\['), (r'\\(', r'\\\('),
                  (r'\\]', r'\\\]'), (r'\\)', r'\\\)')]:
    print('   %-6s %5d' % (name, len(re.findall(pat, T))))
print('\nconstructs:')
for c in ['texorpdfstring', 'footnote', 'href', 'url{', 'item', 'emph{', 'textbf', 'paragraph{',
          'noindent', 'notag', 'nonumber', 'tag{', 'cite{', 'label{', 'ref{', 'eqref{',
          'verbatim', 'includegraphics', 'caption', 'substack', 'text{', 'mathrm{', 'mathbb{',
          'operatorname', 'left', 'right', 'hfill', 'qquad', 'quad', 'newline', 'medskip',
          'smallskip', 'bigskip', 'vspace', 'hspace', 'protect', 'frac{', 'binom']:
    print('   %-16s %5d' % (c, T.count(c)))
print('\nmath environments (numbered vs unnumbered):')
for env in ['equation', 'align', 'gather', 'multline', 'split', 'aligned', 'gathered',
            'array', 'cases', 'pmatrix', 'smallmatrix', 'matrix']:
    n = len(re.findall(r'\\begin\{%s\}' % env, T))
    s = len(re.findall(r'\\begin\{%s\*\}' % env, T))
    print('   %-12s %4d   starred %d' % (env, n, s))
print('\ntheorem-like environments:')
for env in ['theorem', 'lemma', 'proposition', 'corollary', 'definition', 'remark', 'proof']:
    print('   %-12s %4d' % (env, len(re.findall(r'\\begin\{%s\}' % env, T))))
print('\nsections:')
for lvl in ['section', 'subsection', 'subsubsection', 'paragraph']:
    print('   %-14s %4d (starred %d)' % (lvl, len(re.findall(r'\\%s\{' % lvl, T)),
                                         len(re.findall(r'\\%s\*\{' % lvl, T))))
