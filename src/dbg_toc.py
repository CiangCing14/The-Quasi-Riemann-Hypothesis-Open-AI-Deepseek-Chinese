import importlib.util, glob, os, re
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
bh.TOC = sorted(bh.load_toc(), key=lambda t: -len(t[1]))
print('TOC size', len(bh.TOC))
for n in (15, 16, 50, 120):
    txt = open('/home/a/Downloads/25/out/page_%03d.zh.md' % n, encoding='utf-8').read()
    print('--- page', n)
    for b in bh.page_blocks(txt)[:5]:
        t, rest = bh.split_title(b)
        print('   ', 'TITLE' if t else 'para ', repr(b[:55]), '->', repr(t))
