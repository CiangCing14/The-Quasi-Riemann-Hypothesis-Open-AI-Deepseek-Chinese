#!/usr/bin/env python3
"""Locate the tokens the subagents flagged as uncertain, so they can be cropped."""
import re
import subprocess

ROOT = '/home/a/Downloads/25'


def toks(page):
    xml = '/tmp/loc_%d.xml' % page
    subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page),
                    ROOT + '/paper.pdf', xml], check=True)
    raw = open(xml, encoding='utf-8').read()
    return [(float(a), float(b), float(c), float(d), t)
            for a, b, c, d, t in re.findall(
                r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', raw)]


# page -> list of (label, regex on the token text)
WANT = {
    7:   [('a-in-Fp', r'^F$|^p$'), ('sup', r'≪|δ')],
    22:  [('sqrt3v', r'√|3v|^2$'), ('hatphi', r'ϕ|^b$')],
    25:  [('prod', r'^Y$|±|Γ'), ('substack', r'sf|\(nb,E\)')],
    32:  [('evalbar', r'z=|−δ|∂'), ('local', r'ϵ|τ')],
    40:  [('u-lambda-k', r'uλ|λ|fact|Fact'), ('lambda-k', r'λ')],
    41:  [('u-lambda', r'uλ|λ')],
    77:  [('LS', r'^L$|^S$'), ('al-y', r'al|ly'), ('CI', r'CI|^I$')],
    123: [('indicator', r'1|p\|n|nb'), ('N-star', r'^N$|^∗$')],
    132: [('k-new', r'^k$|new|^d$'), ('hats', r'^b$')],
    129: [('radicals', r'√|qdk|qd')],
}


def main():
    for pg, wants in WANT.items():
        ws = toks(pg)
        for label, rx in wants:
            r = re.compile(rx)
            hits = [w for w in ws if r.search(w[4])]
            if not hits:
                print('p%-4d %-12s : (no token match)' % (pg, label))
                continue
            for x0, y0, x1, y1, t in hits[:6]:
                print('p%-4d %-12s : x %6.1f-%6.1f  y %6.1f-%6.1f  %r' % (pg, label, x0, x1, y0, y1, t))
        print()


main()
