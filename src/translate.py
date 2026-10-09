import os, sys, glob, json, time
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, '/home/a/Downloads/25')
from ds_api import call

ROOT = '/home/a/Downloads/25'
OUT = os.path.join(ROOT, 'out')
os.makedirs(OUT, exist_ok=True)

SYS = """你是数学论文的专业译者。把用户给出的英文学术论文段落翻译成简体中文。

规则：
1. 只输出译文，不要任何解释、前言、结语或"以下是译文"之类的话。
2. 保持原文段落结构：段落之间用空行分隔，不要合并或拆分段落。
3. 公式一律用 LaTeX 表示：行间公式（独占一行的公式）用 $$...$$ 包起来，行内公式用 $...$。
   源文本是 PDF 提取的，公式可能被拆行、错位，请依据数学含义还原成正确的 LaTeX。
   如果实在无法确定某个式子，就原样保留其中的符号文本，不要编造数学内容。
4. 术语用通行中文译法，首次出现时可在括号内保留英文原词。人名、定理名、文献编号 [n] 保留原样。
5. 不要输出页码、页眉页脚、页码数字。参考文献列表中已发表的英文标题保留原文，不要翻译。
6. 标题、小节标题保留原编号，例如 "4.3 Smooth norm profiles" 译为 "4.3 光滑范数剖面"。
7. 不要使用 Markdown 标记（不要 #、*、- 等符号），标题单独成行即可。"""


def job(n):
    src = os.path.join(ROOT, 'pages', 'page_%03d.txt' % n)
    dst = os.path.join(OUT, 'page_%03d.zh.md' % n)
    if os.path.exists(dst) and os.path.getsize(dst) > 0:
        return n, 'skip', 0
    text = open(src, encoding='utf-8').read().strip()
    if len(text) < 5:
        open(dst, 'w', encoding='utf-8').write('')
        return n, 'empty', 0
    t0 = time.time()
    for attempt in range(3):
        try:
            r, u = call([{'role': 'system', 'content': SYS},
                         {'role': 'user', 'content': text}], max_tokens=32000)
            if not r or not r.strip():
                raise RuntimeError('empty completion')
            open(dst, 'w', encoding='utf-8').write(r.strip() + '\n')
            return n, 'ok', round(time.time() - t0, 1)
        except Exception as e:
            print('page %d attempt %d failed: %s' % (n, attempt + 1, e), flush=True)
            time.sleep(3)
    return n, 'FAIL', round(time.time() - t0, 1)


pages = sorted(int(os.path.basename(p)[5:8])
               for p in glob.glob(os.path.join(ROOT, 'pages', 'page_*.txt')))
print('pages to process:', len(pages), flush=True)
done = fail = 0
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = {ex.submit(job, n): n for n in pages}
    for f in as_completed(futs):
        n, st, el = f.result()
        done += 1
        if st == 'FAIL':
            fail += 1
        print('[%d/%d] page %d %s %ss' % (done, len(pages), n, st, el), flush=True)
print('FINISHED ok/skip=%d fail=%d' % (done - fail, fail), flush=True)
