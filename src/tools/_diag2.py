import sys, re, importlib.util, fitz
src=open('/home/a/Downloads/25/tools/audit_final.py').read().replace('\nmain()\n','\n')
ns={}; exec(compile(src,'audit_final.py','exec'),ns)
doc=fitz.open('/home/a/Downloads/25/paper.pdf')

def raw_glyphs(pg):
    """return list of (font,char,bbox) for CMEX/CMSY chars"""
    out=[]
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type')!=0: continue
        for line in blk['lines']:
            for span in line['spans']:
                for ch in span['chars']:
                    f=span['font']
                    if f.startswith('CMEX') or f.startswith('CMSY'):
                        out.append((f,ch['c'],ch['bbox']))
    return out

for n in [int(a) for a in sys.argv[1:]]:
    pg=doc[n-1]
    print('===== PAGE',n)
    for f,c,b in raw_glyphs(pg):
        o=ord(c) if len(c)==1 else -1
        tag=''
        if f.startswith('CMEX') and c in ('X','Y','Z'): tag='BIGOP'
        if f.startswith('CMEX') and c in ('b','e'): tag='RADCH/ACC'
        if f.startswith('CMEX') and o in (0x0c,0x0d): tag='BARCODE'
        if f.startswith('CMEX') and o in (0,1,0x12,0x13,0x10,0x11,0x1a,0x1b): tag='PAREN'
        if f.startswith('CMEX') and o in (2,3): tag='BRACK'
        if f.startswith('CMEX') and o in (8,9): tag='BRACE'
        if f.startswith('CMSY') and c in ('|','\u2225'): tag='CMSY-BAR'
        if tag:
            print('  %-8s %s U+%04X x%.1f-%.1f y%.1f-%.1f'%(tag,f,o if o>=0 else 0,b[0],b[2],b[1],b[3]))
    items,_=ns['page_items'](pg)
    print('  clustered bar:',len(ns['cluster_bars'](items['bar'])),'dbar:',len(ns['cluster_bars'](items['dbar'])))
    for it in ns['cluster_bars'](items['bar']):
        print('    bar x%.1f y%.1f-%.1f n=%d'%(it['bb'][0],it['yv'][0],it['yv'][1],it['n']))
    for it in ns['cluster_bars'](items['dbar']):
        print('    dbar x%.1f y%.1f-%.1f n=%d'%(it['bb'][0],it['yv'][0],it['yv'][1],it['n']))
