import re, subprocess
h = open('/home/a/Downloads/25/build/paper-zh-cn.html', encoding='utf-8').read()
print('toc rows in html      :', len(re.findall(r'class="toc lvl', h)))
print('  lvl1 / lvl2         :', len(re.findall(r'class="toc lvl1"', h)), '/', len(re.findall(r'class="toc lvl2"', h)))
print('dot-run leaders in html:', len(re.findall(r'(?:\.\s){5,}', h)))
i = h.find('lvl1')
print('--- html lines around TOC (each div on its own line?) ---')
seg = h[i - 120:i + 700]
for ln in seg.split('\n')[:10]:
    print('   ', ln[:150])
print('--- a TOC chapter heading wrongly promoted? ---')
print('   h1 containing "从公共信号" :', '从公共信号' in re.sub(r'<div class="toc[^>]*>.*?</div>', '', h) and 'yes' or 'no')
txt = subprocess.run(['pdftotext', '/home/a/Downloads/25/paper-zh-cn.pdf', '-'], capture_output=True, text=True).stdout
print('dot-run leaders in PDF :', len(re.findall(r'(?:\.\s?){5,}', txt)))
pg = subprocess.run(['pdftotext', '-f', '2', '-l', '2', '/home/a/Downloads/25/paper-zh-cn.pdf', '-'], capture_output=True, text=True).stdout
print('--- PDF page 2 (TOC) ---')
print('\n'.join(pg.split('\n')[:30]))
info = subprocess.run(['pdfinfo', '/home/a/Downloads/25/paper-zh-cn.pdf'], capture_output=True, text=True).stdout
print([l for l in info.split('\n') if l.startswith(('Pages', 'Page size'))])
