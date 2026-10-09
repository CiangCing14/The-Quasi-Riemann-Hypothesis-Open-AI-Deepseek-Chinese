import importlib.util, re, glob
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
bh.EN_TOC = bh.load_en_toc()
rows = []
for f in sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md')):
    marked = bh.toc_mark(open(f, encoding='utf-8').read())
    rows += [l.strip() for l in marked.split('\n') if l.strip().startswith('@@TOC@@')]
print('total toc rows:', len(rows))
for r in rows[:6]:
    print('   ', bh.toc_row(r)[:150])
miss = [r for r in rows if not r.split('@@')[5].strip()]
print('rows without a page number:', len(miss))
for r in miss[:6]:
    print('   ', bh.toc_row(r)[:150])
print('--- pages with leftover dot runs ---')
for f in sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md')):
    for ln in open(f, encoding='utf-8').read().split('\n'):
        if re.search(r'(?:[.．·]\s?){4,}', ln):
            print('  %s | %s' % (f[-12:], ln.strip()[:110]))
