import re
h = open('/home/a/Downloads/25/build/paper-zh-cn.html', encoding='utf-8').read()
wide = [(m.start(), float(m.group(1))) for m in re.finditer(r'width="([0-9.]+)ex"', h)]
wide.sort(key=lambda t: -t[1])
inline_wide = 0
for pos, w in wide[:12]:
    before = h[max(0, pos - 400):pos]
    ctx = 'DISPLAY' if 'class="eq"' in before[-300:] else 'inline '
    if ctx == 'inline ' and w > 60:
        inline_wide += 1
    print('%.1fex  %s  ...%s' % (w, ctx, re.sub(r'\s+', ' ', before[-70:])[-70:]))
print()
print('inline formulas wider than 60ex:', sum(1 for p, w in wide if w > 60 and 'class="eq"' not in h[max(0, p - 300):p]))
print('max inline width (ex):', max([w for p, w in wide if 'class="eq"' not in h[max(0, p - 300):p]] or [0]))
