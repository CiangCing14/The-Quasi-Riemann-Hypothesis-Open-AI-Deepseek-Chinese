import re, subprocess

P = '/home/a/Downloads/25/paper-zh-cn.pdf'
txt = subprocess.run(['pdftotext', P, '-'], capture_output=True, text=True).stdout
pages = txt.split('\f')
hit = [i + 1 for i, p in enumerate(pages) if '相异的冻结商计算一次' in p]
print('PDF pages containing the passage:', hit)
if hit:
    p = pages[hit[0] - 1]
    print('--- text layer of that page ---')
    print(re.sub(r'\n{2,}', '\n', p)[:1200])
    print('--- plain-text formula leftovers on that page ---')
    for tox in ['πinit', 'πcount,init', 'rmax', 'zmax', 'mmax', 'sslot', 'Dmax', 'τinit', 'Bcrude,init',
                'Ainit', 'Tinit', 'Binit', 'Minit', 'Finit', 'qd′', 'CZ Dmax', 'Z −Tinit']:
        if tox in p:
            print('   LEFTOVER:', tox)
print()
# document-wide: how many pages still show such plain-text math tokens
leftover = 0
for i, p in enumerate(pages):
    if re.search(r'(rmax|zmax|mmax|sslot|Dmax|τinit|πinit|Bcrude|Ainit|Tinit)\b', p):
        leftover += 1
print('pages still containing plain-text sub/superscript tokens:', leftover)
print('pdf size:', len(open(P, 'rb').read()))
