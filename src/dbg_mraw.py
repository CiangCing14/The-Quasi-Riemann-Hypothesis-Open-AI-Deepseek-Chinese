import re
h = open('/home/a/Downloads/25/build/paper-zh-cn.html', encoding='utf-8').read()
blocks = re.findall(r'<div class="mraw">(.*?)</div>', h, re.S)
print('mraw blocks in html:', len(blocks))
idx = h.find('局部因子')
print('--- context around "局部因子" ---')
print(h[max(0, idx - 300):idx + 700].replace('\n', ' ')[:1000])
print()
print('--- first 10 mraw blocks ---')
for b in blocks[:10]:
    print('   ', b.replace('\n', ' ')[:150])
