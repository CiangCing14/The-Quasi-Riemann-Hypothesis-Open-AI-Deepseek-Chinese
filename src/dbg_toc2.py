import importlib.util, glob, re, collections
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
rows = []
for f in sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md')):
    txt = open(f, encoding='utf-8').read().replace('**', '')
    if '目录' in txt:
        continue
    for b in bh.page_blocks(txt):
        m = re.match(r'^(\d+(?:\.\d+)*)[ \u3000]+(\S.*)', b, re.S)
        if not m:
            continue
        rest = m.group(2)
        first = rest.split('\n')[0]
        cut = re.split(r'[。，；：]', first)[0]
        rows.append((m.group(1), cut[:34], len(cut), 'OWNLINE' if '\n' in rest else 'MERGED'))
print('number-prefixed blocks:', len(rows))
for r in rows[:70]:
    print('  %-7s %-36s len=%-3d %s' % r)
