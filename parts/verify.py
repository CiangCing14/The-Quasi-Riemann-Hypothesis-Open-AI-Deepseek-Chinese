#!/usr/bin/env python3
"""Structural verification: per-paragraph token multiset + global token counts (compact)."""
import re, os, json, collections, sys

SRC = "/home/a/Downloads/26/paper.tex"
PARTS = "/home/a/Downloads/26/parts"
PLAN = "/home/a/Downloads/26/parts_plan.json"

src = open(SRC, encoding="utf-8").read().split("\n")
plan = json.load(open(PLAN))

TOKEN_RE = re.compile(
    r'(\\label\{[^}]*\})|(\\begin\{[^}]*\})|(\\end\{[^}]*\})'
    r'|(\\cite(?:\[[^\]]*\])?\{[^}]*\})|(\\bibitem\{[^}]*\})'
    r'|(\\ref\{[^}]*\})|(\\eqref\{[^}]*\})|(\$\$?[^$]*\$\$?)|(\\\[|\\\])')
TEXT_RE = re.compile(r'\\text\{[^{}]*\}')
CITE_OPT_RE = re.compile(r'\\cite\[[^\]]*\]\{')

def norm(s):
    s = TEXT_RE.sub(r'\\text{@@}', s)
    s = CITE_OPT_RE.sub(r'\\cite{', s)
    return re.sub(r'\s+', ' ', s).strip()

def toks(text):
    return collections.Counter(norm(m.group(0)) for m in TOKEN_RE.finditer(text))

def paras(text):
    return [b for b in re.split(r'\n[ \t]*\n', text) if b.strip()]

only = sys.argv[1:] if len(sys.argv) > 1 else None
out, bad = [], []
for idx, (a, b) in enumerate(plan):
    if idx == 30:
        continue
    if only and f"{idx:02d}" not in only:
        continue
    path = os.path.join(PARTS, f"part_{idx:02d}.tex")
    if not os.path.exists(path):
        out.append(f"part_{idx:02d}: MISSING"); bad.append(idx); continue
    sseg = "\n".join(src[a-1:b])
    zseg = open(path, encoding="utf-8").read()
    cs, cz = toks(sseg), toks(zseg)
    SEXTRA, ZEXTRA = cs - cz, cz - cs      # direction: what source has that zh lacks
    diff = dict(SEXTRA) | dict(ZEXTRA)
    PS, PZ = paras(sseg), paras(zseg)
    msgs = []
    if len(PS) != len(PZ):
        msgs.append(f"PARAS {len(PS)}!={len(PZ)}")
    if diff:
        for tag, d in (("ZH-MISSING", SEXTRA), ("ZH-EXTRA", ZEXTRA)):
            if d:
                keys = sorted(d)[:8]
                msgs.append(tag + " " + "; ".join(f"{k[:40]}x{d[k]}" for k in keys))
    pmis = []
    if len(PS) == len(PZ):
        for j, (x, y) in enumerate(zip(PS, PZ)):
            if toks(x) != toks(y):
                pmis.append((j, toks(x) - toks(y), toks(y) - toks(x)))
        for j, se, ze in pmis[:6]:
            keys = [("ZH-MISSING " + k[:30]) for k in sorted(se)[:4]] + \
                   [("ZH-EXTRA " + k[:30]) for k in sorted(ze)[:4]]
            msgs.append(f"para#{j} [" + "; ".join(keys) + "]")
    if msgs:
        bad.append(idx)
        out.append(f"part_{idx:02d} L{a}-{b}: " + " | ".join(msgs))
    else:
        out.append(f"part_{idx:02d} L{a}-{b}: OK")
out.append(f"\nbad parts: {bad if bad else 'none'}")
open("/home/a/Downloads/26/parts/verify_report.txt", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out))
