import importlib.util, glob, re
spec = importlib.util.spec_from_file_location('bh', '/home/a/Downloads/25/build_html.py')
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)
toc = bh.load_toc()
bh.TOC_NUMS = set(n for n, _ in toc)
PAT = re.compile(r'^(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(.{1,34})$')
cand = []
for f in sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md')):
    txt = open(f, encoding='utf-8').read().replace('**', '')
    if '目录' in txt:
        continue
    for ln in txt.split('\n'):
        s = ln.strip()
        m = PAT.match(s)
        if not m:
            continue
        if re.search(r'[。，；：！？]', s) or s.endswith('的'):
            continue
        cjk = len(re.findall(r'[\u4e00-\u9fff]', m.group(2)))
        cand.append((m.group(1), m.group(2), cjk, m.group(1) in bh.TOC_NUMS))
print('candidates:', len(cand))
for num, title, cjk, intoc in cand:
    print('  %-7s cjk=%-2d toc=%-5s %s' % (num, cjk, intoc, title[:40]))
