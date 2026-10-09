import re
h = open('/home/a/Downloads/25/build/paper-zh-cn.html', encoding='utf-8').read()
hs = re.findall(r'<h([123])>([^<]*)', h)
print('total headings:', len(hs))
bad = [t for lvl, t in hs if len(re.findall(r'[\u4e00-\u9fff]', t)) < 2]
print('non-Chinese headings (should be ~0):', bad)
for lvl, t in hs:
    print(' h%s %s' % (lvl, t))
