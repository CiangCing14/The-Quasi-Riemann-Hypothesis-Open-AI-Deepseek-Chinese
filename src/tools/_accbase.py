import fitz, sys
doc=fitz.open('/home/a/Downloads/25/paper.pdf')
for n in [int(a) for a in sys.argv[1:]]:
    pg=doc[n-1]
    chars=[]
    for blk in pg.get_text('rawdict')['blocks']:
        if blk.get('type')!=0: continue
        for line in blk['lines']:
            for span in line['spans']:
                for ch in span['chars']:
                    chars.append((span['font'],ch['c'],ch['bbox']))
    print('==== PAGE',n)
    for f,c,b in chars:
        if f.startswith('CMEX') and c in ('b','e'):
            cx=(b[0]+b[2])/2
            # candidate bases: chars near cx, font not CMEX, y overlapping or just below
            cands=[(cc,bb,ff) for ff,cc,bb in chars if not (ff.startswith('CMEX') or ff.startswith('CMSY'))
                   and bb[0]-3 < cx < bb[2]+3 and bb[1] > b[1]-6]
            cands.sort(key=lambda t:t[1][1])
            print('  acc %s %r x%.1f y%.1f  bases=%s'%(f,c,b[0],b[1],
                  [(cc,ff,'x%.1f'%bb[0]) for cc,bb,ff in cands[:3]]))
