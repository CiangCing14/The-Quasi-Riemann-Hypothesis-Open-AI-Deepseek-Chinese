import importlib.util, re, glob
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
bh.EN_TOC = bh.load_en_toc()
bad = []
for f in sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md')):
    marked = bh.toc_mark(open(f, encoding='utf-8').read())
    for ln in marked.split('\n'):
        if ln.strip().startswith('@@TOC@@'):
            continue
        if re.search(r'(?:[.．·]\s?){4,}', ln):
            bad.append((f[-12:], ln.strip()[:120]))
print('lines still carrying dot-run leaders after toc_mark:', len(bad))
for f, l in bad[:25]:
    print('  %s | %s' % (f, l))
