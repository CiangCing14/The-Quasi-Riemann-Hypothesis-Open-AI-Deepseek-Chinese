import re, xml.etree.ElementTree as ET
h = open('/home/a/Downloads/25/build/paper-zh-cn.html', encoding='utf-8').read()

def svg_spans(s):
    """depth-aware <svg>...</svg> spans (MathJax nests <svg> for stretchy pieces)"""
    out = []
    for m in re.finditer(r'<svg\b|</svg>', s):
        pass
    stack = []
    for m in re.finditer(r'<svg\b[^>]*?(/?)>|</svg>', s):
        tok = m.group(0)
        if tok.startswith('</'):
            if stack:
                start = stack.pop()
                if not stack:
                    out.append((start, m.end()))
        elif not tok.endswith('/>'):
            stack.append(m.start())
    return out

spans = svg_spans(h)
print('top-level svg elements:', len(spans))
bad = unresolved = 0
samples = []
for a, b in spans:
    s = h[a:b]
    try:
        root = ET.fromstring(s)
    except Exception as e:
        bad += 1
        if len(samples) < 3:
            samples.append('XML: ' + str(e)[:90])
        continue
    ids = {el.get('id') for el in root.iter() if el.get('id')}
    for el in root.iter():
        for k, v in el.attrib.items():
            if k.endswith('href') and v.startswith('#') and v[1:] not in ids:
                unresolved += 1
                if len(samples) < 5:
                    samples.append('dangling ' + v[:40])
print('malformed svg      :', bad)
print('dangling glyph refs:', unresolved)
print('samples            :', samples)
# widest formula check
w = [float(x) for x in re.findall(r'width="([0-9.]+)ex"', h)]
print('svg widths(ex): max %.1f  p95 %.1f  count %d' % (max(w), sorted(w)[int(len(w) * 0.95)], len(w)))
