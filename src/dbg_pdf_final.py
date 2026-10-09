import re
import subprocess

P = '/home/a/Downloads/25/paper-zh-cn.pdf'
txt = subprocess.run(['pdftotext', P, '-'], capture_output=True, text=True).stdout
pages = txt.split('\f')
print('PDF pages:', len(pages))

# 1) plain-text sub/superscript identifiers left anywhere
pat = re.compile(r'[a-zA-Z]\s?(max|init|crude|slot)\b')
bad = [i + 1 for i, p in enumerate(pages) if len(pat.findall(p)) >= 2]
print('pages still showing plain-text identifiers:', len(bad), bad)

# 2) fragments that were plain text before the repair and must now be vector math
FRAGS = ['πcount,init', 'πinit', 'Dmax', 'rmax', 'sslot', 'Bcrude', 'Ainit', 'Tinit',
         'si = r', 'κi = M', 'qd′', 'nb3 = 1', 'Z −Tinit', 'qdk']
left = {}
for i, p in enumerate(pages):
    for f in FRAGS:
        if f in p:
            left.setdefault(f, []).append(i + 1)
print('plain-text fragments still present:', {k: v[:3] for k, v in left.items()} or 'none')

# 3) the repaired passages still carry their Chinese prose
for probe, expect in [('这里把相异的冻结商计算一次', 'page 150 passage'),
                      ('设', None)]:
    hits = [i + 1 for i, p in enumerate(pages) if probe in p]
    if expect:
        print('%s -> PDF page(s) %s' % (expect, hits))
        if hits:
            seg = pages[hits[0] - 1]
            k = seg.find(probe)
            print('   context:', re.sub(r'\s+', ' ', seg[k:k + 150]))

# 4) equation tags are drawn inside the SVG (not text-extractable) - count what is visible
print('equation numbers still in the text layer:', len(re.findall(r'\(\d{1,2}\.\d{1,3}\)', txt)))
