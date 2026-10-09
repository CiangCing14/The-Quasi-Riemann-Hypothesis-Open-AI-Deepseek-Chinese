import sys, re, importlib.util
spec=importlib.util.spec_from_file_location('af','/home/a/Downloads/25/tools/audit_final.py')
src=open('/home/a/Downloads/25/tools/audit_final.py').read().replace('\nmain()\n','\n')
ns={}; exec(compile(src,'audit_final.py','exec'),ns)
import fitz
doc=fitz.open('/home/a/Downloads/25/paper.pdf')
def zh_counts(path):
    t=open(path,encoding='utf-8').read()
    named=len(re.findall(r'\\lvert|\\rvert|\\lVert|\\rVert|\\left\||\\right\||\\mid(?![a-z])',t))
    plain=len(re.findall(r'(?<!\\left)(?<!\\right)(?<!\\lvert)(?<!\\rvert)(?<!\\lVert)(?<!\\rVert)(?<!\\\\)\|',t))
    return dict(sqrt=len(re.findall(r'\\sqrt',t)),overline=len(re.findall(r'\\overline|\\bar(?!\w)',t)),
        hat=len(re.findall(r'\\hat|\\widehat',t)),abs=named+plain)
for n in [int(a) for a in sys.argv[1:]]:
    items,_=ns['page_items'](doc[n-1])
    p=ns['counts_of'](items)
    z=zh_counts('/home/a/Downloads/25/out/page_%03d.zh.md'%n)
    print('PAGE',n)
    print('  pdf',p)
    print('  zh ',z)
    print('  GAP', {k:(p[k],z[k]) for k in ('sqrt','overline','hat','abs') if p[k]!=z[k]})
    for k in ('overline','accent'):
        for it in items[k]:
            bb=it.get('bb') or it.get('rule')
            print('   %-8s y%6.1f x%6.1f-%6.1f covers:%r'%(k,bb[1],bb[0],bb[2],it.get('content')))
