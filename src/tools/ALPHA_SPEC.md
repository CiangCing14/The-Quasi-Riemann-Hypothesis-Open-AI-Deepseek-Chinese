# ALPHA_SPEC — 补回被文本层抹掉的字母字体（花体 / Fraktur / 黑板体）

## 背景（已由字体表验证）
论文 PDF 里三种数学字母在抽取时都退化成了普通字母，逐页翻译时字体信息丢失：

| PDF 字体 | 实际含义 | 应写成 |
|---|---|---|
| CMSY10 的 ASCII 大写字母 | 花体 `\mathcal{A}`…`\mathcal{Z}` | `\mathcal{X}` |
| EUFM10 的字母（大小写都有） | Fraktur `\mathfrak{a}`,`\mathfrak{p}`,`\mathfrak{R}`… | `\mathfrak{X}` |
| MSBM10 的字母 | 黑板体 `\mathbb{R}`,`\mathbb{Z}`,`\mathbb{C}`… | `\mathbb{X}` |

这不是纯装饰：论文里 $B$（普通）与 $\mathcal{B}$（花体）、$\mathfrak{p}$（素理想）与 $p$（有理素数）**是不同的对象**，字体丢了就把它们混成一个符号。

## 怎么做
对 `tools/worklists_alpha/page_NNN.txt` 里列出的**每一个字形**，在 `out/page_NNN.zh.md` 的**同一个表达式**里把那个字母包成对应的宏：

- 工作清单给出：字体类别、字母、坐标、以及它所在那一行的原始字形文本（定位线索）。
- 用「该行还有哪些符号」来找到译文里对应的那个公式，再把相应的字母改成 `\mathcal{X}` / `\mathfrak{X}` / `\mathbb{X}`。
- 计数必须对得上：该页 PDF 有 n 个某类字形，译文该页就要有 n 个对应的宏（允许译文已有一部分）。

**验收命令会给出两边的计数**，改到相等为止。

## 第二批附加任务：核对大运算符的下标内容（防"下标串位"）
源文里 Σ/∏/∫ 的下标常是多行 `\substack`。逐页翻译时会出现**整行被挪到另一个运算符上**或**凭空多出一行**的错误（实例：page_149 的 (17.82)，译文把第一个 Σ 的第二行 `q_f/Z^{V_c^{\text{init}}}\in I_f` 挪到了第二个 Σ 上，而第二个 Σ 本应是 `\substack{k\in\mathcal{O}\\ 0<q_k\le Z^{M_{\text{init}}}}`）。

`tools/worklists_v2/page_NNN.txt` 每个文件的 `---- BIG-OPERATOR LIMITS ----` 段列出了**每个大运算符真实印出的下标行**（按 y 分行，below[n] 是下标第 n 行，above[n] 是上标）。做法：
1. 按 x 坐标把每个 `\sum at y .. x ..` 对应到译文里同一个运算符（用该页公式顺序与上下文）。
2. 逐行核对：译文该运算符的 `_{...}` 内容必须与 below 各行**一一对应**（行数、顺序、内容），多出的行删掉，缺的行补回，被挪走的行移回正确的运算符。
3. 若译文用了 `\substack` 而源文只有一行，或反之，按源文改。

## 硬规则
1. 只动 `$...$` / `$$...$$` 内部，而且只改**字母的字体**；中文正文、标点、公式结构一字不动。
2. 不确定是哪个出现位置时，看该行上下文与编号（公式编号、周围的符号组合）来定位；实在定不了就跳过并写进 unresolved。
3. 大写 `\mathcal{X}` 与小写 `\mathfrak{x}` 按工作清单里给的字母原样使用。
4. 不要改动别的记号（上划线/竖线等由另一批任务负责）。
5. 改前备份：`cp out/page_NNN.zh.md out/page_NNN.zh.md.prealph`

## 验收
```
cd /home/a/Downloads/25
python3 tools/check_page.py N                    # 必须 PASS
python3 tools/alpha_worklists.py 2>/dev/null | grep -c .   # 不应再包含 N
python3 -c "
import re;t=open('out/page_NNN.zh.md',encoding='utf-8').read()
print({k:len(re.findall(p,t)) for k,p in [('cal',r'\\\\mathcal\{'),('frak',r'\\\\mathfrak\{'),('bb',r'\\\\mathbb\{')]})"
```
最后一条打印的三个数，应当与 `tools/worklists_alpha/page_NNN.txt` 首行区域声明的 pdf 字形数**不小于**（即不再少于）。
