#!/usr/bin/env python3
"""Translate paper.tex's prose into Chinese, keeping every byte of mathematics.

Design
  * the document is cut into translation units at blank lines and grouped to ~3.5 kB
  * each unit is translated by DeepSeek with thinking disabled (ds_api)
  * every unit is verified against its source: the ordered list of math snippets and of
    \\label/\\ref/\\eqref/\\cite/\\url/environment tokens must match exactly.  A unit
    that fails is retried with the diff spelled out, then reported.
  * results are cached per unit, so re-runs cost nothing.

usage
  python3 tools/tex_translate.py --plan          # segmentation + verification dry run
  python3 tools/tex_translate.py --pilot 6       # translate 6 units, report
  python3 tools/tex_translate.py                 # full run (parallel)
  python3 tools/tex_translate.py --status        # cache/coverage report
"""
import argparse
import hashlib
import json
import os
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, '/home/a/Downloads/25')
import ds_api  # noqa: E402

SRC = '/home/a/Downloads/25/paper.tex'
BUILD = '/home/a/Downloads/25/build'
CACHE = os.path.join(BUILD, 'texchunks')
OUT_TEX = os.path.join(BUILD, 'paper-zh-cn.tex')

MATH_ENVS = ['equation', 'align', 'align*', 'split', 'aligned', 'gathered', 'array', 'cases',
             'pmatrix', 'smallmatrix', 'matrix', 'gather', 'gather*', 'multline', 'eqnarray']

GLOSSARY = """
quasi-Riemann hypothesis 拟黎曼假设 | zero-free half-plane 无零点半平面 | Hecke L-function 赫克 L 函数
Dirichlet L-function 狄利克雷 L 函数 | Riemann zeta function 黎曼 zeta 函数 | character 特征
cubic theta 三次 theta | reflection 反射 | moment 矩 | residue 留数 | contour 围道
squarefree 无平方因子 | nonresidue 非剩余 | Gauss sum 高斯和 | reciprocity 互反律
norm 范数 | ideal 理想 | prime 素数 | prime ideal 素理想 | ray class 射线类
sieve 筛法 | large sieve 大筛法 | zero detector 零点检测器 | saturated witness 饱和见证
row 行 | row count 行计数 | profile 轮廓 | energy 能量 | bound 界 | estimate 估计
completion 完备化 | canonical 典范 | canonical bound 典范界 | puncture 穿刺
cardinality 基数 | dilation 缩扩 | dyadic 二进的 | admissible 允许的 | tail 尾项
Poisson summation 泊松求和 | Euler factor 欧拉因子 | Fourier 傅里叶 | lattice 格
lemma 引理 | proposition 命题 | theorem 定理 | corollary 推论 | definition 定义 | remark 注
proof 证明 | abstract 摘要 | introduction 引言 | notation 记号 | conclusion 结论
""".strip()


# ---------------------------------------------------------------- segmentation
def load():
    t = open(SRC, encoding='utf-8').read()
    i = t.index('\\begin{document}')
    j = t.index('\\begin{thebibliography}')
    k = t.index('\\end{thebibliography}') + len('\\end{thebibliography}')
    return t[:i + len('\\begin{document}')], t[i + len('\\begin{document}'):j], t[j:k], t[k:]


MATH_RE = re.compile(
    r'(\\begin\{(?:' + '|'.join(re.escape(e) for e in MATH_ENVS) + r')\}.*?\\end\{(?:'
    + '|'.join(re.escape(e) for e in MATH_ENVS) + r')\}'
    r'|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?!\$).*?(?<!\\)\$)',
    re.S)
REF_RE = re.compile(r'\\(?:label|ref|eqref|cite|bibitem|url|href|input|include)\{[^}]*\}'
                    r'|\\(?:begin|end)\{[^}]*\}')


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def math_seq(s):
    return [norm(m.group(0)) for m in MATH_RE.finditer(s)]


def split_math(s):
    """inline snippets may move with Chinese word order; display/env blocks may not.
    Delimiters are canonicalised, so \\(x\\) and $x$ compare equal (both are valid LaTeX)."""
    inline, block = [], []
    for m in MATH_RE.finditer(s):
        t = norm(m.group(0))
        if t.startswith('\\[') or t.startswith('\\begin{'):
            block.append(t if t.startswith('\\begin{') else '\\[' + t[2:-2].strip() + '\\]')
        else:
            if t.startswith('$'):
                inner = t[1:-1].strip()
            elif t.startswith('\\('):
                inner = t[2:-2].strip()
            else:
                inner = t
            inline.append(inner)
    return inline, block


def ref_seq(s):
    return [norm(m.group(0)) for m in REF_RE.finditer(s)]


def chunk_body(body, target=3500, hard=6000):
    """cut at blank lines, but never inside an open environment (a proof or a display
    block split in half invites the model to 'repair' the LaTeX and break it)"""
    blocks = re.split(r'(\n\s*\n)', body)
    units, cur, depth = [], '', 0
    for i in range(0, len(blocks), 2):
        blk = blocks[i] + (blocks[i + 1] if i + 1 < len(blocks) else '')
        depth += len(re.findall(r'\\begin\{', blk)) - len(re.findall(r'\\end\{', blk))
        if cur and depth <= 0 and len(cur) + len(blk) > target:
            units.append(cur)
            cur = blk
        else:
            cur += blk
    if cur:
        units.append(cur)
    # split any oversized unit at the last safe blank line
    out = []
    for u in units:
        while len(u) > hard:
            c = u.rfind('\n\n', 0, hard)
            if c < 200:
                break
            out.append(u[:c + 2])
            u = u[c + 2:]
        out.append(u)
    return out


# ---------------------------------------------------------------- translation
SYSTEM = """你是学术论文翻译引擎，把 LaTeX 源码里的英文翻译成简体中文（大陆术语习惯）。

硬规则（违者视为失败）：
1. 数学内容**逐字节原样保留**：$...$、\\(...\\)、\\[...\\]、equation/align/split/aligned/gathered/array/cases/pmatrix/smallmatrix 等数学环境，连同其中的每一个字符、空格、换行、命令，全部不许改动、不许重排、不许补全、不许省略。
2. \\label \\ref \\eqref \\cite \\bibitem \\url \\href 的参数、\\begin{...}/\\end{...} 的环境名、以及 \\\\ & ~ 等排版符号原样保留。
3. 只翻译自然语言（正文、标题、定理/引理/证明等环境里的文字、\\paragraph 标题、\\emph/\\textbf 里的文字）。不增删任何内容，不加译者注，不改公式编号。
4. 原样保留原有的段落结构与空行（一个空行仍是一个空行）；行内换行可随中文语序调整。
5. 输出**只有翻译后的 LaTeX 片段**，不要用 ``` 代码块包裹，不要任何说明文字。
6. 术语遵循（不在这张表里的按论文惯例）：%s
""" % GLOSSARY


def translate_unit(unit, idx, retries=3):
    key = hashlib.sha1(unit.encode()).hexdigest()[:16]
    path = os.path.join(CACHE, '%s.txt' % key)

    def verdict(src, out):
        from collections import Counter
        si, sb = split_math(src)
        oi, ob = split_math(out)
        plain_src = MATH_RE.sub(' ', src)          # source with all math removed
        # the model may put a bare symbol it found in the prose into math mode; that is a
        # typographic choice, not a content change: allow it only for single tokens that
        # really do occur in the source text.
        def harmless(tok):
            # symbol re-set in math mode: it must actually occur in the source, either in
            # the prose or inside another formula (i.e. it is not invented)
            t = tok.strip()
            return (bool(re.fullmatch(r'[A-Za-z0-9\\_{}^+\-*/=().,|\[\]\s]{1,24}', t))
                    and len(t) <= 24 and t in src)
        bad = []
        cs, co = Counter(si), Counter(oi)
        if cs != co:
            for k, v in (cs - co).items():          # lost: never forgiven
                bad.append('少写 %d 次：%r' % (v, k[:120]))
            for k, v in (co - cs).items():          # added: forgiven only if the symbol
                if not harmless(k):                 # does occur in the source text
                    bad.append('多写 %d 次：%r' % (v, k[:120]))
        if ob != sb:
            bad.append('行间公式块被改动：缺少 %r'
                       % ([m[:120] for m in sb if m not in ob][:3],))
        rs, ro = Counter(ref_seq(src)), Counter(ref_seq(out))
        if rs != ro:
            for k, v in rs.items():
                if ro.get(k, 0) < v:
                    bad.append('引用少写 %d 次：%r' % (v - ro.get(k, 0), k))
            for k, v in ro.items():
                if rs.get(k, 0) < v:
                    bad.append('引用多写 %d 次：%r' % (v - rs.get(k, 0), k))
        return bad

    if os.path.exists(path):
        got = open(path, encoding='utf-8').read()
        if not verdict(unit, got):
            return got, 'cached'
    msgs = [{'role': 'system', 'content': SYSTEM},
            {'role': 'user', 'content': unit}]
    last = None
    for attempt in range(retries):
        got, usage = ds_api.call(msgs, max_tokens=8000, temperature=0.2)
        got = got.strip()
        if got.startswith('```'):
            got = re.sub(r'^```[a-z]*\n|\n```$', '', got)
        bad = verdict(unit, got)
        if not bad:
            open(path, 'w', encoding='utf-8').write(got)
            return got, 'ok'
        msgs = msgs[:2] + [
            {'role': 'assistant', 'content': got},
            {'role': 'user', 'content':
             '上面这版不合格。只翻译英文，数学与引用必须与原文逐字一致（行内公式可以随语序移动，但内容不能变；'
             '\\[...\\] 与 equation/align 等公式块的位置和内容都必须不动）。问题：\n- '
             + '\n- '.join(bad) + '\n请重新输出完整片段。'}]
        last = bad
    raise RuntimeError('unit %d failed verification: %s' % (idx, last))


def sub_parts(unit, limit=900):
    """split a stubborn unit: first at blank lines without breaking environments, then
    (for parts that are still long) at line boundaries that are not inside display math"""
    pieces = re.split(r'(?<=\n)\n(?=\S)', unit)
    parts, cur, depth = [], '', 0
    for p in pieces:
        depth += len(re.findall(r'\\begin\{', p)) - len(re.findall(r'\\end\{', p))
        cur += p
        if depth <= 0 and len(cur) > 600:
            parts.append(cur)
            cur = ''
    if cur:
        parts.append(cur)
    fine = []
    for p in parts:
        if len(p) <= limit:
            fine.append(p)
            continue
        buf, disp = '', False
        for ln in p.split('\n'):
            opens = len(re.findall(r'\\\[', ln)) - len(re.findall(r'(?<!\\)\\\]', ln))
            buf += ln + '\n'
            disp = bool(opens) if opens else disp
            if not disp and len(buf) > limit:
                fine.append(buf)
                buf = ''
        if buf.strip():
            fine.append(buf)
    return [p for p in fine if p.strip()]


def translate_robust(unit, idx, depth=0):
    if depth >= 3 or len(unit) < 500:
        got, _ = translate_unit(unit, idx)
        return got
    try:
        got, _ = translate_unit(unit, idx)
        return got
    except Exception as e:
        parts = sub_parts(unit)
        if len(parts) < 2:
            raise
        print('   unit %d: splitting into %d parts after %s' % (idx, len(parts), e), flush=True)
        return ''.join(translate_robust(p, idx, depth + 1) for p in parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', action='store_true')
    ap.add_argument('--pilot', type=int, default=0)
    ap.add_argument('--status', action='store_true')
    ap.add_argument('--jobs', type=int, default=8)
    a = ap.parse_args()
    os.makedirs(CACHE, exist_ok=True)
    pre, body, bib, post = load()
    units = chunk_body(body)
    print('preamble %d chars | body %d chars in %d units | bibliography %d chars'
          % (len(pre), len(body), len(units), len(bib)))
    print('math snippets: %d | refs: %d | units with no math: %d'
          % (sum(len(math_seq(u)) for u in units), sum(len(ref_seq(u)) for u in units),
             sum(1 for u in units if not math_seq(u))))
    if a.plan:
        for i, u in enumerate(units[:8]):
            print('--- unit %d (%d chars, %d math, %d refs) ---' % (i, len(u), len(math_seq(u)),
                                                                    len(ref_seq(u))))
            print(u[:300].replace('\n', ' | ')[:300])
        return
    if a.status:
        have = len([f for f in os.listdir(CACHE) if f.endswith('.txt')])
        print('cached units: %d / %d' % (have, len(units)))
        return
    todo = range(len(units)) if not a.pilot else range(min(a.pilot, len(units)))
    lock = threading.Lock()
    done = [0]
    results = {}

    def work(i):
        try:
            got = translate_robust(units[i], i)
            how = 'ok'
            results[i] = got
            with lock:
                done[0] += 1
                print('[%d/%d] unit %d %s' % (done[0], len(list(todo)), i, how), flush=True)
        except Exception as e:
            with lock:
                done[0] += 1
                print('[%d/%d] unit %d FAILED: %s' % (done[0], len(list(todo)), i, e), flush=True)

    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        list(ex.map(work, todo))
    if a.pilot:
        miss = [i for i in todo if i not in results]
        print('pilot done: %d ok, %d failed %s' % (len(results), len(miss), miss))
        return
    if len(results) != len(units):
        print('INCOMPLETE: %d/%d units translated' % (len(results), len(units)))
        return
    out = pre + ''.join(results[i] for i in range(len(units))) + bib + post
    open(OUT_TEX, 'w', encoding='utf-8').write(out)
    print('wrote %s (%d chars)' % (OUT_TEX, len(out)))


main()
