#!/usr/bin/env python3
"""Assemble the Chinese paper and run global structural/completeness checks."""
import re, os, json, collections, sys

BASE = "/home/a/Downloads/26"
SRC = f"{BASE}/paper.tex"
PARTS = f"{BASE}/parts"
OUT = f"{BASE}/paper-zh-cn.tex"

if os.path.exists(OUT):
    sys.exit(f"REFUSING TO OVERWRITE existing {OUT}")

order = ["part_P0.tex"] + [f"part_{i:02d}.tex" for i in range(30)] + ["part_30.tex"]
chunks = []
for name in order:
    p = os.path.join(PARTS, name)
    if not os.path.exists(p):
        sys.exit(f"missing {p}")
    t = open(p, encoding="utf-8").read().rstrip("\n")
    chunks.append(t)
text = "\n\n".join(chunks) + "\n"
open(OUT, "w", encoding="utf-8").write(text)
print(f"wrote {OUT}: {len(text)} chars, {text.count(chr(10))+1} lines")

# ---------- global checks ----------
src = open(SRC, encoding="utf-8").read()

def body(t):
    i = t.index("\\begin{document}")
    return t[i:]

def seq(t, pat):
    return re.findall(pat, t)

checks = [
    ("label order", r'\\label\{[^}]*\}'),
    ("cite order", r'\\cite(?:\[[^\]]*\])?\{[^}]*\}'),
    ("ref/eqref order", r'\\e?ref\{[^}]*\}'),
]
B_s, B_z = body(src), body(text)
for name, pat in checks:
    a, b = seq(B_s, pat), seq(B_z, pat)
    print(f"{name}: src={len(a)} zh={len(b)} {'IDENTICAL' if a==b else 'DIFFER'}")

# begin/end sequence (including environment names)
a = re.findall(r'\\(begin|end)\{([^}]*)\}', B_s)
b = re.findall(r'\\(begin|end)\{([^}]*)\}', B_z)
print(f"env tokens: src={len(a)} zh={len(b)} {'IDENTICAL' if a==b else 'DIFFER'}")
if a != b:
    for i,(x,y) in enumerate(zip(a,b)):
        if x!=y:
            print("   first diff at", i, x, y); break

# math segment counts
def mathcounts(t):
    inline = len(re.findall(r'(?<!\$)\$(?!\$)[^$]*\$(?!\$)', t))
    disp = len(re.findall(r'\\\[', t))
    envs = len(re.findall(r'\\begin\{(?:equation|align|gather|multline|array|split|aligned|gathered|cases|pmatrix|smallmatrix|eqnarray)\*?\}', t))
    return inline, disp, envs
ms, mz = mathcounts(B_s), mathcounts(B_z)
print("math counts (inline, \\[, math-envs): src=", ms, " zh=", mz)

# source words vs translation size
print("src chars:", len(src), " zh chars:", len(text))

# leftover English prose scan (outside math)
def strip_math(t):
    t = re.sub(r'\\begin\{(?:equation|align|gather|multline|array|split|aligned|gathered|cases|pmatrix|smallmatrix|eqnarray)\*?\}.*?\\end\{(?:equation|align|gather|multline|array|split|aligned|gathered|cases|pmatrix|smallmatrix|eqnarray)\*?\}', ' ', t, flags=re.S)
    t = re.sub(r'\\\[.*?\\\]', ' ', t, flags=re.S)
    t = re.sub(r'\$[^$]*\$', ' ', t)
    return t
S = strip_math(B_z)
bad = []
for i, ln in enumerate(S.split("\n"), 1):
    if re.search(r'\b[A-Za-z]{2,}\b(?:\s+[A-Za-z][A-Za-z\-\']*){3,}', ln):
        bad.append(ln.strip()[:110])
print(f"lines with >=4 consecutive ASCII words: {len(bad)}")
for x in bad[:12]:
    print("   ", x)
