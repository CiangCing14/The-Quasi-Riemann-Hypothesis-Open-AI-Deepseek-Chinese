#!/usr/bin/env python3
"""render a crop: python3 crop.py PAGE x0 y0 x1 y1 OUT [zoom]"""
import sys
import fitz

PDF = '/home/a/Downloads/25/paper.pdf'
page, x0, y0, x1, y1 = int(sys.argv[1]), *map(float, sys.argv[2:6])
out = sys.argv[6]
zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 4.0
doc = fitz.open(PDF)
pg = doc[page - 1]
clip = fitz.Rect(x0, y0, x1, y1)
pix = pg.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
pix.save(out)
print(out, pix.width, 'x', pix.height)
