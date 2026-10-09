#!/usr/bin/env python3
import re, sys
for p in sys.argv[1:]:
    path = '/home/a/Downloads/25/out/page_%03d.zh.md' % int(p)
    t = open(path, encoding='utf-8').read()
    lines = t.split('\n')
    print('===== page_%03d =====' % int(p))
    for i, ln in enumerate(lines, 1):
        for pat, tag in [(r'\\hat\b', 'HAT'), (r'\\widehat', 'WIDEHAT'), (r'\\tilde', 'TILDE'),
                         (r'\\overline', 'OVERLINE'), (r'\\bar(?![a-zA-Z])', 'BAR-acc'),
                         (r'\\lvert|\\rvert|\\left\||\\right\||\\mid(?![a-z])', 'BARDELIM')]:
            for m in re.finditer(pat, ln):
                print('  L%d %s @%d  ctx=%r' % (i, tag, m.start(), ln[max(0, m.start()-25):m.start()+25]))
        # plain bars
        for m in re.finditer(r'(?<![\\|])\|(?![|])', ln):
            # exclude those preceded by \left \right etc which matched above
            seg = ln[max(0, m.start()-6):m.start()]
            if re.search(r'\\left$|\\right$|\\lvert$|\\rvert$|\\lVert$|\\rVert$|\\mid$', seg):
                continue
            print('  L%d PLAINBAR @%d  ctx=%r' % (i, m.start(), ln[max(0, m.start()-25):m.start()+25]))
