import re
d = open('/home/a/Downloads/25/paper-zh-cn.md', encoding='utf-8').read()
lines = d.split('\n')
print('bytes:', len(d.encode()), 'lines:', len(lines))
print('headings:', len([l for l in lines if re.match(r'^#{1,4} ', l)]))
toc = [l for l in lines if re.match(r'^[ ]*- ', l)]
print('toc items:', len(toc), '| nested:', len([l for l in toc if l.startswith('  ')]))
print('reference lines:', len([l for l in lines if re.match(r'^\[\d+\] ', l)]))
print('$$ fences:', len([l for l in lines if l.strip() == '$$']))

# classic markdown hazards
code_blocks = [i + 1 for i, l in enumerate(lines) if l.startswith('    ') and not l.startswith('    - ')]
print('4-space indented lines (would become code blocks):', len(code_blocks), code_blocks[:6])
tabs = [i + 1 for i, l in enumerate(lines) if '\t' in l]
print('lines containing tabs:', len(tabs), tabs[:5])
odd = [i + 1 for i, l in enumerate(lines) if len(re.findall(r'(?<!\$)\$(?!\$)', l)) % 2]
print('lines with unbalanced inline $:', len(odd), odd[:5])
print('trailing horizontal-rule/space issues:', len([l for l in lines if l != l.rstrip()]))
print('file ends with newline:', d.endswith('\n'))

try:
    import markdown  # noqa
    have = 'python-markdown'
except Exception:
    try:
        import mistune  # noqa
        have = 'mistune'
    except Exception:
        have = None
print('markdown lib available:', have)
if have == 'python-markdown':
    import markdown
    html = markdown.markdown(d, extensions=['fenced_code', 'toc'])
    print('rendered html chars:', len(html))
    print('pre/code blocks in render:', html.count('<pre>'))
if have == 'mistune':
    import mistune
    html = mistune.html(d)
    print('rendered html chars:', len(html))
    print('pre/code blocks in render:', html.count('<pre>'))

print('--- last 8 lines ---')
print('\n'.join(l[:100] for l in lines[-8:]))
