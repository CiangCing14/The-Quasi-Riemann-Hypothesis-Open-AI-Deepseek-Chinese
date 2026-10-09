#!/usr/bin/env python3
"""paper-zh-cn.md -> HTML (MathJax SVG inlined, offline) -> printed by headless Chrome.

  * display math becomes <div class="eq"> with the equation number right-aligned
  * inline math becomes an inline SVG sized in ex
  * the TOC is rebuilt with dotted leaders from the ## / ### headings
  * CSS is the one the earlier PDF used (A4, Noto Serif CJK SC)
"""
import hashlib
import html
import json
import os
import re
import subprocess
import sys

ROOT = '/home/a/Downloads/25'
MD = os.path.join(ROOT, 'paper-zh-cn.md')
HTML = os.path.join(ROOT, 'build/paper-zh-cn.html')
CACHE = os.path.join(ROOT, 'build/paper-zh-cn-svg.json')

DISPLAY_RE = re.compile(r'^\$\$\n(.*?)\n\$\$$', re.S | re.M)
INLINE_RE = re.compile(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$|\\\((.+?)\\\)')

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
html { font-family: 'Noto Serif CJK SC','Noto Serif',serif; }
body { font-size: 10.5pt; line-height: 1.75; text-align: justify; color:#111; margin:0; }
h1,h2,h3,h4 { font-weight: 700; line-height: 1.35; page-break-after: avoid; }
h1 { font-size: 1.7em; margin: 0 0 8pt; }
h2 { font-size: 1.28em; margin: 20pt 0 9pt; padding-bottom: 3pt; border-bottom: 1px solid #bbb; }
h3 { font-size: 1.12em; margin: 14pt 0 6pt; }
h4 { font-size: 1.0em; margin: 11pt 0 5pt; color:#333; }
p { margin: 0 0 7pt; text-indent: 0; }
ul { margin: 4pt 0 8pt 0; padding-left: 18pt; }
li { margin: 0 0 3pt; }
.eq { text-align:center; margin: 9pt 0; position: relative; page-break-inside: avoid; }
.eq svg { max-width: 100%%; }
.eqno { position: absolute; right: 0; top: 50%%; transform: translateY(-50%%); font-size: 0.9em; color:#333; }
.mtxt svg { vertical-align: middle; }
svg text { font-family: 'Noto Serif CJK SC','DejaVu Serif',serif; }
.toc { display:flex; align-items:baseline; margin:0 0 3pt; page-break-inside: avoid; }
.toc .t { }
.toc .lead { flex:1 1 auto; border-bottom:1px dotted #999; margin:0 4pt; position:relative; top:-0.3em; min-width:1.5em; }
.toc .pg { color:#333; }
.toc .l3 { padding-left: 1.6em; font-size: 0.97em; }
.cover { text-align:center; margin-top: 70mm; page-break-after: always; }
.cover h1 { font-size: 2.0em; margin-bottom: 10mm; }
.cover .meta { font-size: 1.05em; color:#444; line-height: 2.0; }
.cover .note { margin-top: 60mm; font-size: 0.85em; color:#666; text-align:left; line-height: 1.7; }
hr { border:0; border-top:1px solid #ccc; margin: 14pt 0; }
.pb { page-break-before: always; }
"""


def render_math(items):
    """items: {key: (latex, display)} -> {key: svg|None}"""
    cache = {}
    if os.path.exists(CACHE):
        cache = json.load(open(CACHE, encoding='utf-8'))
    todo = []
    for k, (latex, disp) in items.items():
        h = hashlib.sha1((('D' if disp else 'I') + latex).encode()).hexdigest()[:16]
        if h in cache:
            continue
        todo.append({'key': h, 'latex': latex, 'display': disp})
    if todo:
        json.dump(todo, open('/tmp/mjx_in.json', 'w'), ensure_ascii=False)
        r = subprocess.run(['node', os.path.join(ROOT, 'mjx/tex2svg.js'),
                            '/tmp/mjx_in.json', '/tmp/mjx_out.json'],
                           cwd=ROOT, capture_output=True, text=True)
        sys.stderr.write(r.stderr[-800:] + '\n')
        got = json.load(open('/tmp/mjx_out.json'))
        for k, v in got.items():
            cache[k] = v.get('svg') or ('ERROR:' + (v.get('error') or '?'))
        json.dump(cache, open(CACHE, 'w'))
    out, err = {}, []
    for k, (latex, disp) in items.items():
        h = hashlib.sha1((('D' if disp else 'I') + latex).encode()).hexdigest()[:16]
        v = cache.get(h)
        if not v or v.startswith('ERROR:'):
            err.append((latex[:70], (v or 'missing')[:80]))
            out[k] = None
        else:
            out[k] = v
    return out, err


def main():
    md = open(MD, encoding='utf-8').read()
    # ---- cover
    m = re.match(r'# (.*?)\n\n(.*?)\n', md)
    title, meta = (m.group(1).strip(), m.group(2).strip()) if m else ('准黎曼假设', '')
    md = md[m.end():] if m else md
    # ---- drop the source TOC (we rebuild it)
    md = re.sub(r'^## 目录\n(?:(?!^## ).)*', '', md, flags=re.S | re.M)
    md = re.sub(r'^---\n', '', md, flags=re.M)

    # ---- pull math out
    store = {}
    eqno = {}

    def disp_sub(m):
        body = m.group(1).strip()
        tag = re.search(r'\\tag\{([^}]*)\}', body)
        k = '@@D%d@@' % len(store)
        if tag:
            eqno[k] = tag.group(1)
            body = body.replace(tag.group(0), '').strip()
        store[k] = (body, True)
        return '\n\n' + k + '\n\n'

    md = DISPLAY_RE.sub(disp_sub, md)

    def inl_sub(m):
        body = (m.group(1) or m.group(2) or '').strip()
        if not body:
            return m.group(0)
        k = '@@I%d@@' % len(store)
        store[k] = (body, False)
        return k

    md = INLINE_RE.sub(inl_sub, md)

    # ---- headings (for the TOC) and markdown -> html
    toc = []
    for h in re.finditer(r'^(#{2,3}) (.*)$', md, re.M):
        toc.append((len(h.group(1)), h.group(2).strip()))
    try:
        import markdown
        body_html = markdown.markdown(md, extensions=['extra', 'sane_lists', 'nl2br'])
    except ImportError:
        body_html = ''.join('<p>%s</p>' % html.escape(x) for x in md.split('\n\n'))
    body_html = re.sub(r'<p>(@@[DI]\d+@@)</p>', r'\1', body_html)

    svgs, err = render_math(store)
    for k, svg in svgs.items():
        if svg is None:
            body_html = body_html.replace(k, '<span class="mraw">[未渲染]</span>')
            continue
        if store[k][1]:
            num = eqno.get(k)
            en = '<span class="eqno">(%s)</span>' % num if num else ''
            body_html = body_html.replace(k, '<div class="eq">%s%s</div>' % (svg, en))
        else:
            body_html = body_html.replace(k, '<span class="mtxt">%s</span>' % svg)

    toc_html = ['<h2>目录</h2>']
    for lvl, t in toc:
        cls = 'toc l3' if lvl == 3 else 'toc'
        toc_html.append('<div class="%s"><span class="t">%s</span><span class="lead"></span></div>'
                        % (cls, html.escape(t)))
    doc = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<title>%s</title><style>%s</style></head><body>
<div class="cover"><h1>%s</h1><div class="meta">%s</div></div>
%s
<div class="pb"></div>
%s
</body></html>""" % (html.escape(title), CSS, html.escape(title),
                    re.sub(r'\*\*(.+?)\*\*', r'\1', meta), '\n'.join(toc_html), body_html)
    open(HTML, 'w', encoding='utf-8').write(doc)
    print('html %s (%d chars) | math %d (failed %d) | toc %d'
          % (HTML, len(doc), len(store), len(err), len(toc)))
    for e in err[:10]:
        print('   SVG FAIL %r -> %s' % e)


main()
