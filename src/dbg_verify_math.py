import re, subprocess
H = '/home/a/Downloads/25/build/paper-zh-cn.html'
P = '/home/a/Downloads/25/paper-zh-cn.pdf'
h = open(H, encoding='utf-8').read()
print('html size          : %.1f MB' % (len(h) / 1e6))
print('inline <svg>       :', len(re.findall(r'<svg', h)))
print('mraw fallbacks     :', len(re.findall(r'class="mraw"', h)))
print('raw latex text left:', len(re.findall(r'\\\\(?:frac|begin|sum|int|left|mathbb|mathcal)', h)))
print('eq blocks          :', len(re.findall(r'class="eq"', h)))
print('eq numbers         :', len(re.findall(r'class="eqno"', h)))
print()
i = h.find('局部因子')
print('--- around the formula the user flagged ---')
print(re.sub(r'\s+', ' ', h[i - 60:i + 620])[:620])
print()
info = subprocess.run(['pdfinfo', P], capture_output=True, text=True).stdout
print([l for l in info.split('\n') if l.startswith(('Pages', 'Page size', 'File size'))])
txt = subprocess.run(['pdftotext', P, '-'], capture_output=True, text=True).stdout
print('latex source strings in pdf text:', len(re.findall(r'\\\\(?:frac|begin|sum|left|pmatrix)', txt)))
img = subprocess.run(['pdfimages', '-list', P], capture_output=True, text=True).stdout
print('embedded raster images:', max(0, len(img.strip().split(chr(10))) - 2))
print('blank-ish page check:', end=' ')
empt = []
for p in range(1, 199):
    o = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), P, '-'], capture_output=True, text=True).stdout
    if len(o.strip()) < 25:
        empt.append(p)
print(empt if empt else 'none')
