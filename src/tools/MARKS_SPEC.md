# MARKS_SPEC — 补齐 PDF 文本层丢失的记号（上划线 / 帽子 / 竖线 / 大定界符）

## 背景（已由字形与像素双重验证，勿怀疑）
论文 PDF 的数学排版里有三类记号**不进文本层**，逐页翻译时静默丢失：

1. **上划线 `\overline{...}`** —— 在 PDF 里是**矢量线段**（不是字形），文本层完全没有痕迹。
2. **帽子 `\hat{...}`** —— 抽取时变成字母 **`b`**（坏 ToUnicode）。所以原文里那个孤零零的 `b` 不是变量，是帽子。
3. **竖线 `|`／双竖线 `\|`（绝对值、范数、求值）** —— 普通尺寸是 CMSY10 的 `|`/`∥`（文本层可见），大号是 CMEX10 控制符（文本层不可见）。
另外大号圆括号/方括号/花括号在文本层也是控制符（`\u0010`–`\u0013` 等）。

## 每个工作项怎么做
对 `tools/worklists/page_NNN.txt` 里的每一项，在 `out/page_NNN.zh.md` 的**同一个公式**里补上它：

- `OVERLINE  covers: 'X Y'` → 在译文的 LaTeX 里找到覆盖的那些符号，整体包起来：`\overline{...}`。
  例：`covers: 'Q 2'` → 把 `Q_2` 写成 `\overline{Q_2}`；`covers: 'F b (a 0) j'` → `\overline{F^{\text{...}}_b(a_0)^j}` 之类的**实际**内容（以译文里该公式的真实写法为准）。
- `ACCENT` → 该位置的符号应带 `\hat{...}`。译文若写成裸符号或错下标（例如把帽子当成了下标 b），改正为 `\hat{...}`。
- `BAR` → 该位置应有 `|`；成对的用 `\left| ... \right|`。译文若写成了圆括号，改成竖线。
- `PAREN / BRACK / BRACE` → 译文对应位置应有 `\left( \right)` / `\left[ \right]` / `\left\{ \right\}`。
- 大运算符 `SUM / PROD / INT` 仅作位置参考，**不要**改动（全篇计数已无缺口）。

## 硬规则
1. **只动数学**：`$...$` 与 `$$...$$` 内部。中文正文、标点、语序**一字不许改**（`check_page.py` 会逐字校验）。
2. 只允许**插入**缺失记号或改正该记号本身；不许重写公式、不许换符号体系、不许"顺手优化"。
3. 定不了位就不要改，写进报告的 `unresolved` 并说明原因。**绝不臆造**。
4. 改前备份：`cp out/page_NNN.zh.md out/page_NNN.zh.md.premarks`
5. 参考材料（只读，别改）：`pages/page_NNN.txt`（英文页文本，注意 `b`/`X`/`Y`/`Z` 是帽子/Σ/∏/∫ 的坏抽取）、`tools/worklists/page_NNN.txt`（几何与覆盖内容）、`tools/bbox_dump.py`（字形坐标）。

## 验收（必须跑，并把输出粘进报告）
```
cd /home/a/Downloads/25
python3 tools/check_page.py N            # 必须 PASS：中文序列与快照逐字一致
python3 tools/audit_final.py 2>/dev/null | grep -E "^ *N \|"   # 该行 overline/hat/abs 的 pdf 与 zh 两列必须相等
```
两项都过才算完成。若某项实在无法定位，允许该页仍有差额，但必须在报告的 unresolved 里点名。
