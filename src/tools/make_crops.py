#!/usr/bin/env python3
"""Crop the uncertain formulas to PNG so they can be read directly."""
import subprocess

ROOT = '/home/a/Downloads/25'
DPI = 600
S = DPI / 72.0

CROPS = [
    ('p7_Fp',      7, 330, 512, 100, 36),
    ('p22_sqrt',  22, 190,  95, 115, 62),
    ('p22_hatphi', 22, 300,  62, 205, 40),
    ('p25_prod',  25, 285, 438, 145, 52),
    ('p25_sub',   25, 150, 348, 150, 52),
    ('p32_bar',   32, 140, 595, 285, 38),
    ('p40_ulam',  40, 140, 200, 130, 32),
    ('p41_ulam',  41, 135, 142, 115, 34),
    ('p77_LS',    77, 120, 298, 155, 34),
    ('p129_rad', 129, 100, 555, 370, 70),
]


def main():
    for name, page, x, y, w, h in CROPS:
        out = '/tmp/crop_' + name
        subprocess.run(['pdftoppm', '-png', '-r', str(DPI), '-f', str(page), '-l', str(page),
                        '-x', str(int(x * S)), '-y', str(int(y * S)),
                        '-W', str(int(w * S)), '-H', str(int(h * S)),
                        ROOT + '/paper.pdf', out], check=True)
        print('%s.png  (page %d, x %d-%d pt, y %d-%d pt)' % (out, page, x, x + w, y, y + h))


main()
