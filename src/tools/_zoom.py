import fitz, sys
doc=fitz.open('/home/a/Downloads/25/paper.pdf')
n=int(sys.argv[1]); y0,y1,x0,x1=[float(a) for a in sys.argv[2:6]]; z=float(sys.argv[6]) if len(sys.argv)>6 else 12
pg=doc[n-1]
clip=fitz.Rect(x0,y0,x1,y1)
pix=pg.get_pixmap(matrix=fitz.Matrix(z,z), clip=clip)
out='/tmp/zoom_%d_%d.png'%(n,int(y0)); pix.save(out)
print(out,pix.width,pix.height)
