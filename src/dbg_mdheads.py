import re
lines = open('/home/a/Downloads/25/paper-zh-cn.md', encoding='utf-8').read().split('\n')
heads = [(i + 1, l) for i, l in enumerate(lines) if re.match(r'^#{1,4} ', l)]
print('headings:', len(heads))
for n, l in heads:
    print('  %5d  %s' % (n, l[:80]))
