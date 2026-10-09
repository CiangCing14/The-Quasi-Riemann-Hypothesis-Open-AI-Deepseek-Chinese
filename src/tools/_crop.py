import fitz, sys
doc=fitz.open('/home/a/Downloads/25/paper.pdf')
n=int(sys.argv[1]); y0=float(sys.argv[2]); y1=float(sys.argv[3]); x0=float(sys.argv[4]); x1=float(sys.argv[5])
pg=doc[n-1]
# render crop
clip=fitz.Rect(x0,y0,x1,y1)
pix=pg.get_pixmap(matrix=fitz.Matrix(4,4), clip=clip)
out='/tmp/crop_%d_%d.png'%(n,int(y0))
pix.save(out)
print('saved',out,pix.width,pix.height)
# dump chars in region
for blk in pg.get_text('rawdict')['blocks']:
    if blk.get('type')!=0: continue
    for line in blk['lines']:
        for span in line['spans']:
            for ch in span['chars']:
                b=ch['bbox']
                if b[1]>y0-3 and b[3]<y1+3 and b[2]>x0-3 and b[0]<x1+3:
                    print('  %r x%.1f-%.1f y%.1f-%.1f %s'%(ch['c'],b[0],b[2],b[1],b[3],span['font']))
# drawings in region
for p in pg.get_drawings():
    r=p['rect']
    if r.y0>y0-3 and r.y1<y1+3 and r.x1>x0-3 and r.x0<x1+3:
        print('  DRAW x%.1f-%.1f y%.1f-%.1f w%.1f h%.1f'%(r.x0,r.x1,r.y0,r.y1,r.width,r.height))
