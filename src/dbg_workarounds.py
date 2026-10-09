import glob
import os
import re

ROOT = '/home/a/Downloads/25/out'
targets = [7, 8, 22, 25, 31, 32, 40, 42, 56, 58, 77, 82, 123, 129, 130, 132, 133, 136,
           140, 154, 175, 187, 191, 193]

print('=== workaround artefacts to review ===')
for n in targets:
    p = os.path.join(ROOT, 'page_%03d.zh.md' % n)
    t = open(p, encoding='utf-8').read()
    flags = []
    if '&nbsp;' in t:
        flags.append('&nbsp; x%d' % t.count('&nbsp;'))
    # display blocks and how many \tag they carry
    for m in re.finditer(r'\$\$(.+?)\$\$', t, flags=re.S):
        body = m.group(1)
        ntag = len(re.findall(r'\\tag\{', body))
        if ntag > 1:
            flags.append('DISPLAY WITH %d TAGS: %s' % (ntag, ' '.join(body.split())[:70]))
        if '\\begin{aligned}' in body and ntag >= 1:
            flags.append('aligned-with-tag: %s' % ' '.join(body.split())[:60])
    if flags:
        print('page_%03d: %s' % (n, ' | '.join(flags)))

print()
print('=== state of the six timed-out pages ===')
for n in [140, 154, 175, 187, 191, 193]:
    new = os.path.join(ROOT, 'page_%03d.zh.md' % n)
    old = os.path.join(ROOT, 'page_%03d.zh.md.premath' % n)
    a = open(old, encoding='utf-8').read() if os.path.exists(old) else ''
    b = open(new, encoding='utf-8').read()
    print('page_%03d  premath=%s  was=%dB now=%dB  display=%d  inline=%d'
          % (n, 'yes' if a else 'NO', len(a.encode()), len(b.encode()),
             len(re.findall(r'\$\$', b)) // 2, len(re.findall(r'(?<!\$)\$(?!\$)', b)) // 2))
