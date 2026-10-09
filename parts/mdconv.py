#!/usr/bin/env python3
"""LaTeX(中文) -> 便于 pandoc 转换的中间 LaTeX，带编号解析（读 .aux）。"""
import re, os, sys

BASE = "/home/a/Downloads/26"
SRC  = f"{BASE}/paper-zh-cn.tex"
AUX  = f"{BASE}/paper-zh-cn.aux"
OUT  = "/tmp/paper-md-src.tex"

tex = open(SRC, encoding="utf-8").read()

# ---------- 1. 读 .aux ----------
labels, bibcite = {}, {}
if os.path.exists(AUX):
    aux = open(AUX, encoding="utf-8").read()
    for m in re.finditer(r'\\newlabel\{([^}]*)\}\{\{([^}]*)\}', aux):
        labels[m.group(1)] = m.group(2).strip()
    for m in re.finditer(r'\\bibcite\{([^}]*)\}\{([^}]*)\}', aux):
        bibcite[m.group(1)] = m.group(2)
print(f"aux: labels={len(labels)} bibcite={len(bibcite)}")

# ---------- 2. 元数据 ----------
preamble, body = tex.split("\\begin{document}", 1)
body = body.replace("\\end{document}", "")
title = re.search(r'\\title\{(.*?)\}\n', preamble, re.S).group(1)
title = re.sub(r'\\\\\[[^\]]*\]', ' ', title)
title = re.sub(r'\\large\s*', '', title)
title = re.sub(r'\\texorpdfstring\{(.*?)\}\{.*?\}', r'\1', title, flags=re.S)
title = " ".join(title.split())
author = re.search(r'\\author\{(.*?)\}', preamble, re.S).group(1)
date = re.search(r'\\date\{(.*?)\}', preamble, re.S).group(1)
head = f"# {title}\n\n{author} · {date}\n"

# ---------- 3. 统计编号回退用计数器 ----------
missing_ref, missing_cite = [], []

# 4. 定理类环境 -> 加粗小标题
ENVNAME = {"theorem": "定理", "proposition": "命题", "lemma": "引理",
           "corollary": "推论", "definition": "定义", "remark": "注记"}
sec_ctr = [0]
thm_ctr = [0]
eqr_ctr = [0]
lines = body.split("\n")
out_lines = []
thm_re = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark)\}(?:\[([^\]]*)\])?\s*(\\label\{([^}]*)\})?')

def esc(s):
    return s

i = 0
buf = body
# 逐行处理章节计数（用于无 label 回退）
processed = []
for ln in lines:
    m = re.match(r'\\section\*?\{(.*)\}', ln)
    if m:
        sec_ctr[0] += 1
        thm_ctr[0] = 0
        eqr_ctr[0] = 0
    processed.append(ln)
body = "\n".join(processed)

def thm_repl(m):
    env, title, _, key = m.group(1), m.group(2), m.group(3), m.group(4)
    thm_ctr[0] += 1
    num = labels.get(key) if key else None
    if not num:
        num = f"{sec_ctr[0]}.{thm_ctr[0]}"
    name = ENVNAME[env]
    head = f"**{name} {num}**"
    if title:
        head += f"（{title}）"
    return head + " "

body = thm_re.sub(thm_repl, body)
body = re.sub(r'\\end\{(?:theorem|proposition|lemma|corollary|definition|remark)\}', '', body)

# proof 环境
body = body.replace("\\begin{proof}", "**证明.** ")
body = re.sub(r'\\end\{proof\}', '\n\n∎\n', body)

# abstract
body = body.replace("\\begin{abstract}", "## 摘要\n")
body = body.replace("\\end{abstract}", "")

# ---------- 5. 参考文献 ----------
bib_start = body.find("\\begin{thebibliography}")
if bib_start >= 0:
    head_part, bib = body[:bib_start], body[bib_start:]
    bib = re.sub(r'\\begin\{thebibliography\}\{[^}]*\}', '## 参考文献\n', bib)
    depth = 0
    outb = []
    pos = 0
    for m in re.finditer(r'\\bibitem\{([^}]*)\}', bib):
        num = bibcite.get(m.group(1), '?')
        outb.append(bib[pos:m.start()] + f"\n\n[{num}] ")
        pos = m.end()
    outb.append(bib[pos:])
    bib = "".join(outb).replace("\\end{thebibliography}", "")
    body = head_part + bib

# ---------- 6. 引用与交叉引用 ----------
def cite_repl(m):
    opts = m.group(1) or ""
    keys = [k.strip() for k in m.group(2).split(",")]
    nums = []
    for k in keys:
        if k in bibcite: nums.append(bibcite[k])
        else:
            missing_cite.append(k); nums.append(k)
    pre = ""
    for o in re.findall(r'\[([^\]]*)\]', opts):
        pre += o + " "
    return f"{pre}[{', '.join(nums)}]".strip()

body = re.sub(r'\\cite((?:\[[^\]]*\])*)\{([^}]*)\}', cite_repl, body)

def ref_repl(m):
    kind, star, key = m.group(1), m.group(2), m.group(3)
    num = labels.get(key)
    if num is None:
        missing_ref.append(key); num = f"⟦{key}⟧"
    return f"({num})" if kind == "eqref" else num
body = re.sub(r'\\(eqref|ref)(\*?)\{([^}]*)\}', ref_repl, body)

# hyperref / texorpdfstring / label
body = re.sub(r'\\hyperref\[[^\]]*\]\{([^}]*)\}', r'\1', body)
body = re.sub(r'\\texorpdfstring\{(.*?)\}\{[^{}]*\}', r'\1', body, flags=re.S)
body = re.sub(r'\\label\{[^}]*\}', '', body)

# ---------- 7. 公式编号 \tag ----------
def tag_eq(m):
    inner = m.group(1)
    lm = re.search(r'\\label\{([^}]*)\}', inner)
    inner = re.sub(r'\\label\{[^}]*\}', '', inner)
    if lm and lm.group(1) in labels and '\\tag' not in inner:
        inner = inner.rstrip() + f"\\tag{{{labels[lm.group(1)]}}}"
    return "\\begin{equation}" + inner + "\\end{equation}"
body = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', tag_eq, body, flags=re.S)

# ---------- 8. 清理排版命令 ----------
for cmd in [r'\\maketitle', r'\\tableofcontents', r'\\clearpage', r'\\medskip', r'\\smallskip',
            r'\\bigskip', r'\\noindent', r'\\allowdisplaybreaks(\[\d\])?', r'\\qed\b',
            r'\\setcounter\{[^}]*\}\{[^}]*\}', r'\\addtocontents\{[^}]*\}\{[^}]*\}']:
    body = re.sub(cmd, '', body)
body = body.replace('~', ' ')
body = re.sub(r'\\begin\{center\}', '', body).replace('\\end{center}', '')
body = re.sub(r'\\end\{document\}', '', body)

# 处理逐行：[opt] 形式的定理标题可能残留
open(OUT, "w", encoding="utf-8").write(head + "\n" + body)
print("wrote", OUT, len(head + body), "chars")
print("未解析 \\ref:", len(missing_ref), sorted(set(missing_ref))[:10])
print("未解析 \\cite:", len(missing_cite), sorted(set(missing_cite))[:10])
print("残留 \\begin/\\end 计数:", body.count("\\begin{"), body.count("\\end{"))
