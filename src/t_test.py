import sys, time
sys.path.insert(0, '/home/a/Downloads/25')
from ds_api import call

page = open('/home/a/Downloads/25/pages/page_015.txt', encoding='utf-8').read()

SYS = """你是数学论文的专业译者。把用户给出的英文学术论文段落翻译成简体中文。

规则：
1. 只输出译文，不要任何解释、前言、结语或"以下是译文"之类的话。
2. 保持原文段落结构：段落之间用空行分隔，不要合并或拆分段落。
3. 公式一律用 LaTeX 表示：行间公式（独占一行的公式）用 $$...$$ 包起来，行内公式用 $...$。
   源文本是 PDF 提取的，公式可能被拆行、错位，请依据数学含义还原成正确的 LaTeX。
   如果实在无法确定某个式子，就原样保留其中的符号文本，不要编造数学内容。
4. 术语用通行中文译法，首次出现时可在括号内保留英文原词。人名、定理名、文献编号 [n] 保留原样。
5. 不要输出页码、页眉页脚、参考文献条目里的英文标题（参考文献列表整体保留原样，只需把中文期刊名等按需处理，拿不准就保留原文）。
6. 标题、小节标题保留原编号，例如 "4.3 Smooth norm profiles" 译为 "4.3 光滑范数剖面"。
"""

r, u = call([{'role': 'system', 'content': SYS},
             {'role': 'user', 'content': page}], max_tokens=16000)
print('--- USAGE ---')
print({k: v for k, v in u.items() if 'token' in k})
print('--- OUT (chars %d) ---' % len(r))
print(r)
open('/home/a/Downloads/25/pages/test_015.zh.md', 'w', encoding='utf-8').write(r)
