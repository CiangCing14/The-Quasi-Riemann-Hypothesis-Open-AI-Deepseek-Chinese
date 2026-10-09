import glob, re
src = 0
for f in sorted(glob.glob('/home/a/Downloads/25/pages/page_*.txt')):
    src += len(open(f, encoding='utf-8').read())
cjk = other = 0
for f in sorted(glob.glob('/home/a/Downloads/25/out/page_*.zh.md')):
    t = open(f, encoding='utf-8').read()
    cjk += len(re.findall(r'[\u4e00-\u9fff]', t))
    other += len(re.sub(r'[\u4e00-\u9fff]', '', t))
in_tok = src / 4.0
out_tok = cjk * 1.0 + other / 3.5
print('source chars          %d' % src)
print('input tokens  (est)   %d' % in_tok)
print('output CJK chars      %d' % cjk)
print('output tokens (est)   %d' % out_tok)
for lab, (pi, po) in {'off-peak': (0.15, 0.60), 'peak': (0.30, 1.20)}.items():
    usd = in_tok / 1e6 * pi + out_tok / 1e6 * po
    print('%-9s cost  $%.4f   ~CNY %.2f' % (lab, usd, usd * 7.1))
