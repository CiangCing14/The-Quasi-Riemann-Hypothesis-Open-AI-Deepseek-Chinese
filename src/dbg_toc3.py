import importlib.util, glob
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
toc = bh.load_toc()
bh.TOC = sorted(toc, key=lambda t: -len(t[1]))
bh.TOC_NUMS = set(n for n, _ in toc)
print('nums:', sorted(bh.TOC_NUMS))
for s in ['7 泊松表示及其欧拉因子', '5.1 完备反射', '1 引言', '6.3 中的两个范数结合起来']:
    print(repr(s), '->', bh.is_head_line(s))
txt = open('/home/a/Downloads/25/out/page_050.zh.md', encoding='utf-8').read()
marked = bh.mark_headings(txt)
print('--- marked first 400 chars ---')
print(repr(marked[:400]))
print('--- blocks ---')
for b in bh.page_blocks(marked)[:4]:
    print('   ', repr(b[:60]))
