import re
p='/home/a/Downloads/25/out/page_149.zh.md'
t=open(p,encoding='utf-8').read()
def zh_counts(t):
    named = len(re.findall(r'\\lvert|\\rvert|\\lVert|\\rVert|\\left\||\\right\||\\mid(?![a-z])', t))
    plain = len(re.findall(r'(?<!\\left)(?<!\\right)(?<!\\lvert)(?<!\\rvert)(?<!\\lVert)(?<!\\rVert)(?<!\\)\|', t))
    return named, plain
print('named,plain', zh_counts(t))
print('all | occurrences:')
for m in re.finditer(r'.{0,6}\|.{0,6}', t):
    print(repr(m.group(0)))
