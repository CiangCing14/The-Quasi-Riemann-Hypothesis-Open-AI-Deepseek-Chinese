import re, subprocess
P = '/home/a/Downloads/25/Junior High School/paper-junior.pdf'
for p in range(1, 10):
    t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), P, '-'], capture_output=True, text=True).stdout
    t = re.sub(r'\s+', ' ', t).strip()
    print('--- page %d (%d chars) ---' % (p, len(t)))
    print(t[:230])
h = open('/home/a/Downloads/25/Junior High School/paper-junior.html', encoding='utf-8').read()
print()
print('svg formulas in html:', len(re.findall(r'<svg', h)), '| unresolved placeholders:', h.count('{{m:'))
print('sections:', len(re.findall(r'<h2', h)), '| glossary rows:', h.count('<tr>'))
