import importlib.util
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
bh.EN_TOC = bh.load_en_toc()
tot = 0
for n in (1, 2, 3, 4, 127):
    txt = open('/home/a/Downloads/25/out/page_%03d.zh.md' % n, encoding='utf-8').read()
    is_toc = bh.is_toc_page(txt)
    marked = bh.toc_mark(txt) if is_toc else txt
    rows = [l.strip() for l in marked.split('\n') if l.strip().startswith('@@TOC@@')]
    tot += len(rows)
    print('page %-4d toc_page=%-5s rows=%d' % (n, is_toc, len(rows)))
    for r in rows[:3]:
        print('     ', bh.toc_row(r))
print('total rows:', tot)
