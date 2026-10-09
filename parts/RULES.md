# 任务：把英文 LaTeX 数学论文逐行翻译为简体中文（保持 LaTeX 结构 100% 不变）

你现在负责该论文的一个**行区间**。把该区间的英文内容翻译成地道的学术简体中文，写入指定输出文件。
这是严肃的数学论文（数论 / 解析数论 / Hecke L 函数），译文必须准确、术语统一、可编译。

## 0. 流程（必须按顺序）
1. 先 `read_file` 本文件（就是 RULES.md），记住规则与术语表。
2. `read_file` 源文件，参数 `offset=<区间起始行>`、`limit=<区间行数>`（行号是 1 开始计数的；若一次读不完可再读一次）。
3. 逐行翻译。
4. 用 `write_file` 把**完整**译文写入你的输出路径（UTF-8，无 BOM，纯 LaTeX，不要 Markdown、不要代码围栏、不要任何解释文字）。
5. 自查：`\begin{...}` 与 `\end{...}` 的**数量与顺序**必须与源区间完全一致；`\label{}`、`\ref{}`、`\eqref{}`、`\cite{}` 的数量与参数必须与源区间完全一致。

## 1. 绝对原样保留（逐字符不许改）
- 所有 LaTeX 命令名与环境名：`\documentclass \usepackage \begin/\end{...} \section* \subsection* \paragraph \label \ref \eqref \cite \href \url \frac \sum \int \prod \binom \operatorname \DeclareMathOperator \newtheorem \emph \texorpdfstring \bigl \Big \left \right ...` 等等。
- 所有数学内容原样：`$...$`、`\(...\)`、`\[ ... \]`、以及 `equation / align / gather / multline / array / split / aligned / gathered / cases / pmatrix / smallmatrix / eqnarray` 等环境内部的**全部**内容（除下一节允许的 `\text{}` 外，一个字符都不要动）。
- `\label{...}` 的键名；`\ref{}`/`\eqref{}`/`\cite{}` 的参数；`\url{}`/`\href{}{}` 中的 URL；`\bibitem{...}` 的键名；文件名；包选项。
- `\texorpdfstring{A}{B}`：翻译 A（这是排版用文本），**B 原样保留**（这是 PDF 书签用的 ASCII）。
- `%` 注释行：原样保留，不要翻译、不要删除。
- 数学环境内部只有 `\text{...}` 和 `\mbox{...}` 的内容是自然语言，**要翻译成中文**（例：`\text{for some primitive finite-order Hecke character }\eta` → `\text{对某个本原有限阶 Hecke 特征 }\eta`）。`\mathrm{...}`、`\operatorname{...}`、`\mathbf{...}` 里的记号不动。
- 数式中的标点（逗号、句号、`\quad`、`\qquad`、`\\`、`&`）不动。数式之间的连接词（如 `and`、`where`、`with`）在 `\text{}` 内时按中文译出。

## 2. 必须翻译成简体中文
- 所有英文自然语言：正文段落、`\section`/`\subsection`/`\paragraph` 的标题文字、`abstract` 内容。
- `theorem` / `proposition` / `lemma` / `corollary` / `definition` / `remark` / `proof` 环境的正文（环境名本身不动，正文要译）。
- `\emph{...}` 命令名保留，括号内的英文文本要译。
- `\textbf{...}`、`\textit{...}` 同理。
- 交叉引用前的引导词要译：`Theorem~\ref{x}` → `定理~\ref{x}`；`Section~\ref{x}` → `节~\ref{x}`；`Part~\ref{x}` → `部分~\ref{x}`；`Proposition` → `命题`；`Lemma` → `引理`；`Corollary` → `推论`；`Definition` → `定义`；`Remark` → `注记`；`Equation~\eqref{x}` → `方程~\eqref{x}`；`Appendix` → `附录`；`Chapter` → `章`；`Table` → `表`；`page` → `页`。`~` 与 `\ref`/`\eqref` 的参数必须原样保留。
- 英文引号 ``xxx'' 在译文中改为中文引号 “xxx”（数学模式或代码里出现的引号不动）。
- 英文破折号 `--`（人名之间等）保留原样。

## 3. 段落与换行
- **不得合并或拆分段落**：源文中由空行分隔的段落块，译文中仍用空行分隔成同样多的段落块（同段落内的硬换行可以重排）。
- 段落内可自由折行（建议每行 40–60 个汉字，便于阅读）；不要为了对齐而插入额外空行。
- **不得增删内容**：不解释、不补充、不省略、不改写数学论断、不合并两个句子。忠实逐句对应。
- **行内数学符号必须原样保留为数学模式**：正文里出现的 `$1$`、`$u$`、`$C$`、`$k$`、`$a$`、`$A$`、`$\zeta$`、`$M^2$`、`$1\pmod3$` 等，译文中仍是 `$...$`，既不要省略、也不要写成普通文字、也不要拆成「$1$ 模 $3$」这样的形式。
- **不要给译文添加原文没有的数学符号**（例如把 English 的 one 写成 `$1$`、把 a unit 写成 `$u$`）；原文写文字就用中文字词。
- 区间可能从段落中间开始或结束：照原文片段翻译，**不要补全**缺失的另一半，也不要输出区间外的内容。
- 译文中的专用名词、人名保持拉丁原文拼写（见下）。

## 4. 统一术语表（务必遵守；源文中的英文一律按此译）
- quasi-Riemann hypothesis → 拟黎曼假设
- zero-free half-plane / region → 无零点半平面 / 无零点区域
- half-plane → 半平面；strip → 带形域；critical line → 临界线
- Hecke $L$-function → Hecke $L$ 函数；Dirichlet $L$-function → Dirichlet $L$ 函数；Riemann zeta function → 黎曼 zeta 函数
- finite-order Hecke character → 有限阶 Hecke 特征；primitive / imprimitive character → 本原 / 非本原特征
- conductor → 导子；ray class group → 射线类群；ray class → 射线类
- integral ideal → 整理想；prime ideal → 素理想；ring of integers → 整数环；norm → 范数
- ramified → 分歧的；Euler product → Euler 乘积；Euler factor → Euler 因子；functional equation → 函数方程
- meromorphic continuation → 亚纯延拓；holomorphic → 全纯
- zero / pole / residue → 零点 / 极点 / 留数；principal pole → 主极点；principal residue → 主留数；principal character → 主特征
- nontrivial zeros → 非平凡零点；exceptional zero → 例外零点；zero-density estimate → 零点密度估计
- large sieve → 大筛法；sextic large sieve → 六次大筛法；quadratic large sieve → 二次大筛法；additive large sieve → 加性大筛法；planar large sieve → 平面大筛法
- moment → 矩；first/second/fourth moment → 一阶/二阶/四阶矩；inverse moment → 逆矩；mollified moment → 磨光矩；mean square → 均方
- Poisson summation → Poisson 求和；Mellin integral / transform → Mellin 积分 / 变换
- contour → 围道；contour move → 移动围道；contour tail → 围道尾部
- theta series → theta 级数；cubic theta → 三次 theta；Gauss sum → Gauss 和
- metaplectic → metaplectic（保留原文）；cusp expansion → 尖点展开；Fourier coefficient → Fourier 系数
- squarefree → 无平方因子；sixth-power-free → 无六次幂因子；reduced fraction → 既约分数
- residue character → 剩余特征；character → 特征；inducing character → 诱导特征；induction / induced → 诱导
- smooth norm profile → 光滑范数剖面；norm range → 范数区间；scale → 尺度；height → 高度
- exponent margin → 指数余量；power saving → 幂次节省；seminorm → 半范数
- witness → 见证；saturated witness → 饱和见证；zero detector → 零点探测器；buffered rectangle → 带缓冲的矩形
- row → 行；row count → 行计数；base sum → 基础和；probe → 探针
- compensation / compensated → 补偿 / 补偿的；mark / marked → 标记 / 带标记的；mask → 掩码；envelope → 包络
- Dirichlet polynomial → Dirichlet 多项式；Möbius function → Möbius 函数（理想 Möbius 函数）
- arithmetic progression → 等差数列；least quadratic nonresidue → 最小二次非剩余
- Legendre symbol → Legendre 符号；square root → 平方根；deterministic algorithm → 确定性算法
- principal normalizer → 主正规化因子；normalization → 正规化；affine power → 仿射幂
- finite propagation → 有限传播；correlation → 相关性；Gram bound → Gram 界
- reflected energy → 反射能量；unmarked / marked → 无标记 / 有标记；completed sum / completion → 完备化和 / 完备化
- index → 指标；primary generator convention → 主生成元约定；Eisenstein integer / lattice → Eisenstein 整数 / 格
- idelic definition → 伊代尔定义；complex place → 复位；nonvanishing → 非零
- asymptotic → 渐近；GRH-conditional → 以 GRH 为条件的；positive proportion → 正比例
- bin → 分箱；frequency → 频率；order of choices → 选择次序；endpoint inequality → 端点不等式
- 人名与专名保持拉丁原文：Hecke, Dirichlet, Riemann, Euler, Gauss, Legendre, Poisson, Mellin, Fourier, Tonelli--Shanks, Kubota, Patterson, Dunn, Radziwi\l\l, Goldmakher, Louvel, Blomer, Heath-Brown, Huxley, Baier, Bansal, David, de Faveri, Stucky, Vinogradov, Tao, Bhargava, Ivanyos, Mittal, Saxena, Galbraith, Milne, Thorner, Zaman, Chebotarev, Elliott--Halberstam, Clay, OpenAI, M\"obius

## 5. 输出格式硬性要求
- 只写译文文件本身：`write_file(path, content)`，`content` 就是该区间的完整 LaTeX 译文。
- 不使用 Markdown、不添加 ``` 围栏、不添加任何"以下是翻译"之类的话、不添加 LaTeX 注释。
- 区间内的 `\begin{document}`、`\tableofcontents`、`\clearpage`、`\section{...}` 等结构行必须出现在译文中（命令不变，标题文字译成中文）。
- 完成后你的最终回复只需一行：`OK <输出路径> <行数>`。
