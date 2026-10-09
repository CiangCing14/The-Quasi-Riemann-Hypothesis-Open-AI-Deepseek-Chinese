import re, glob, os
fs = sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md'))[-16:]
for f in fs:
    t = open(f, encoding='utf-8').read()
    refs = re.findall(r'\[\d+\]', t)
    blocks = [b for b in re.split(r'\n\s*\n', t) if b.strip()]
    print('%-16s len=%-6d [n]=%-3d blocks=%-3d lines=%d' % (os.path.basename(f), len(t), len(refs), len(blocks), len(t.split('\n'))))
print('--- page_196 raw (first 900 chars) ---')
print(open('/home/a/Downloads/25/out/page_196.zh.md', encoding='utf-8').read()[:900])
print('--- page_198 raw (first 700 chars) ---')
print(open('/home/a/Downloads/25/out/page_198.zh.md', encoding='utf-8').read()[:700])
