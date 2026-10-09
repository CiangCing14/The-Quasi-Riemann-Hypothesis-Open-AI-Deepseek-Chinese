#!/usr/bin/env python3
"""Build a junior-high-school-friendly explainer PDF of the paper."""
import os, re, json, subprocess, html as _html

ROOT = '/home/a/Downloads/25'
OUTDIR = os.path.join(ROOT, 'Junior High School')
os.makedirs(OUTDIR, exist_ok=True)
HTML_OUT = os.path.join(OUTDIR, 'paper-junior.html')
PDF_OUT = os.path.join(OUTDIR, 'paper-junior.pdf')

# ---------- formulas (MathJax -> SVG) ----------
MATHS = {
    'zeta':   r'\zeta(s) = 1 + \frac{1}{2^{s}} + \frac{1}{3^{s}} + \frac{1}{4^{s}} + \cdots',
    'euler':  r'\zeta(s) = \prod_{p\ \text{素数}} \left(1 - \frac{1}{p^{s}}\right)^{-1}',
    'pitx':   r'\pi(x) \ \text{大约等于}\  \frac{x}{\ln x}',
    'seven':  r'\Re(s) > \frac{7}{8}',
    'half':   r'\Re(s) = \frac{1}{2}',
    'gap':    r'\frac{7}{8} - \frac{1}{2} = \frac{3}{8}',
}


def render_maths():
    keys = sorted(MATHS)
    payload = [{'key': k, 'latex': MATHS[k], 'display': True} for k in keys]
    with open('/tmp/jr_in.json', 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False)
    r = subprocess.run(['node', os.path.join(ROOT, 'mjx', 'tex2svg.js'),
                        '/tmp/jr_in.json', '/tmp/jr_out.json'],
                       capture_output=True, text=True, cwd=os.path.join(ROOT, 'mjx'))
    print('mathjax:', (r.stderr or '').strip()[-80:])
    out = json.load(open('/tmp/jr_out.json', encoding='utf-8'))
    for k in keys:
        if not (out.get(k) or {}).get('svg'):
            print('  !! failed:', k, (out.get(k) or {}).get('error'))
    return {k: (out.get(k) or {}).get('svg', '') for k in keys}


CONTENT = r"""
<div class="cover">
  <div class="kicker">一份写给初中生的读本</div>
  <h1>素数的秘密，<br>和一条 7/8 的线</h1>
  <div class="sub">读懂《准黎曼假设：无零点半平面 Re(s) &gt; 7/8》</div>
  <div class="meta">原文：英文论文，199 页，作者署名 OpenAI，2026 年 9 月 30 日<br>
  本读本：通俗解读，不用于学术引用</div>
</div>

<h2>一、数字世界里的“原子”：素数</h2>

<p>任何一个整数都能拆成更小的数相乘。比如 12 可以拆成 2×2×3，60 可以拆成 2×2×3×5。一直拆下去，最后剩下的那批数没法再拆了：2、3、5、7、11、13、17……它们只能被 1 和自己整除，叫做<b>素数</b>（也叫质数）。</p>

<p>两千多年前，古希腊的欧几里得就证明了一件事：<b>素数有无限多个，永远用不完。</b>这个证明只用了三行推理，是数学里最漂亮的证明之一。</p>

<p>素数为什么重要？因为它们是整数的“原子”。每个整数都能由素数唯一地拼出来（这叫算术基本定理）。所以，只要搞清楚素数是怎么分布的，很多关于整数的问题就拿到了钥匙。</p>

<div class="note">
<b>一句话记住：</b>素数是整数的原子，就像化学里的元素周期表。化学家想知道元素怎么排列，数学家想知道素数怎么分布。
</div>

<h2>二、素数越往后越稀少，但“什么时候出现”没人能完全预测</h2>

<p>把素数排出来：2、3、5、7、11、13、17、19、23、29…… 一开始很密，越往后越稀疏。数一数就会发现：</p>

<ul>
  <li>100 以内有 25 个素数（占了四分之一）；</li>
  <li>1000 以内有 168 个；</li>
  <li>100 万以内有 78498 个，占比不到 8%；</li>
  <li>100 亿以内，占比只剩 4% 左右。</li>
</ul>

<p>一个很自然的问法：从 1 数到 x，一共能碰到多少个素数？这个个数，数学家记作 <b>π(x)</b>。</p>

<p>18 世纪末，高斯和勒让德各自猜测：π(x) 大约等于 x 除以 x 的自然对数。这个猜想后来被称为<b>素数定理</b>，1896 年被阿达马和德拉瓦莱布桑分别独立证明。它是数学史上最漂亮的成果之一。</p>

<div class="eq">{{m:pitx}}</div>

<p>但“大约”是不够的。真正要命的是：估算的误差有多大？误差是慢慢摆动还是剧烈跳动？素数分布的<b>全部秘密</b>，就藏在这个误差里。</p>

<h2>三、黎曼的魔法望远镜</h2>

<p>1859 年，德国数学家伯恩哈德·黎曼做了一件几乎像魔术的事：他把“素数的问题”翻译成了“另一个问题”。</p>

<p>他定义了一个函数，叫 <b>ζ 函数</b>（读“泽塔”）。它是一串无穷相加：</p>

<div class="eq">{{m:zeta}}</div>

<p>这里的 s 可以取<b>复数</b>。复数听起来神秘，其实就是形如 a+bi 的数，a 叫“实部”，b 叫“虚部”。为什么数学家要用复数？因为多了一个维度之后，函数的行为反而变得更有规律、更对称。</p>

<p>接着是黎曼最惊人的发现：这个由<b>所有整数</b>相加得到的东西，还有一个只用<b>素数</b>就能写出来的样子：</p>

<div class="eq">{{m:euler}}</div>

<p>左边是全世界的整数在说话，右边只有素数在说话，而它们相等。这一下就把两件看起来毫不相干的事焊在了一起：<b>ζ 函数的性质，本质上就是素数的性质。</b></p>

<p>于是黎曼给出了全新的思路：想知道素数怎么分布？那就去看 ζ(s) 什么时候等于 0。那些让函数等于 0 的点，叫做<b>零点</b>。素数的秘密，被搬到了一张平面的地图上。</p>

<h2>四、黎曼猜想：一条竖线上的秘密</h2>

<p>问题变成了：ζ(s) = 0 的那些点，落在地图上的什么地方？</p>

<p>黎曼发现，有些零点很“平凡”（落在负半轴上，叫平凡零点），真正有意思的是剩下的那些<b>非平凡零点</b>。他猜测：<b>所有非平凡零点的实部都恰好等于 1/2</b>，也就是说它们全部站在同一条竖直的直线上。</p>

<div class="eq">{{m:half}}</div>

<p>这就是<b>黎曼猜想</b>。它至今没有被证明，是数学界公认最重要、最难的未解问题之一，也是克雷研究所悬赏一百万美元的七个“千禧年问题”之一。</p>

<p>它为什么这么重要？因为如果所有零点都规规矩矩站在这条线上，素数分布的误差就被牢牢锁住了 —— 相当于给素数的“随机摇摆”画出一条极窄的边界。零点越“不听话”，素数的分布就越难预测。</p>

<h2>五、一百多年来，人们从侧面逼近</h2>

<p>直接证明黎曼猜想太难了，于是数学家从旁边一点点包抄：</p>

<ul>
  <li><b>1896 年：</b>阿达马和德拉瓦莱布桑证明了 ζ 函数在最右边那条线 Re(s) = 1 上没有零点。光凭这一条，就能推出素数定理。</li>
  <li><b>之后：</b>人们又证明，在 1 的左边确实有一小条“<b>无零点</b>”的安全带。可惜这条带子会随着你往地图上方走（虚部变大）而越来越窄，最后贴着 1，没法一次性把一大片区域统一划成禁区。</li>
  <li><b>还有一类工具：</b>零点密度估计。它给的是“某条竖线右边零点不会太多”，请注意：是“不会太多”，不是“没有”。</li>
</ul>

<p>于是产生了一个比黎曼猜想弱一些、但同样很漂亮的问题：</p>

<div class="note">
<b>准黎曼假设：</b>能不能找到一个固定的数 σ₀（比 1 小），不管函数是哪一个、不管地图上多高，都能保证在 Re(s) &gt; σ₀ 这整片右半平面里<b>一个零点也没有</b>？
</div>

<p>请分清两者的差别：黎曼猜想要的是“零点<b>恰好</b>住在 Re = 1/2 这条线上”；准黎曼假设只要“零点<b>不许越过</b> Re = σ₀ 这条线”。一个要求精确地址，一个只要求不许越界。</p>

<h2>六、这篇论文证明了什么</h2>

<p>论文的答案是：σ₀ 可以取 <b>7/8</b>。</p>

<p>换句话说：在这篇论文研究的那一大类函数里（把 √−3 加到有理数上得到的数域上的 Hecke L-函数，以及所有的 Dirichlet L-函数，其中包含黎曼的 ζ 函数），<b>在 Re(s) &gt; 7/8 的范围内一个零点都没有</b>（s = 1 处的一个极点除外，那不是零点）。</p>

<div class="eq">{{m:seven}}</div>

<p>把它翻译成地图上的话：整条 7/8 直线右边的地带，一律是禁区。于是 ζ 函数的全部非平凡零点，实部都不会超过 7/8。</p>

<p>这就把准黎曼假设解决了 —— 不只是说“存在这样一个边界”，而是给出了一个具体数字。</p>

<h2>七、他们是怎么做到的：一面镜子，加一个哨兵</h2>

<p>论文有 199 页，绝大多数是技术。但思路可以用三句话讲清楚。</p>

<h3>（1）一个“哨兵”装置</h3>
<p>与其直接证明某处没有零点，不如反过来：假设“这里躲着一个零点”，然后用这个假设造出一个会发生冲突的装置。论文构造了一个“零点探测器”—— 如果零点真的越过了预定的线，探测器就会“饱和”并给出一个过大的数值，而这个数值与之前已经证明的估计相矛盾。<b>矛盾出现了，假设就不成立。</b></p>

<h3>（2）一面“镜子”：立方 theta 反射</h3>
<p>论文用到一个对称性极强的对象 —— <b>三次 theta 函数</b>。它像一面镜子：把一个位置上的值，和另一个位置上的值绑在一起。如果一边“太亮”（意味着有零点），镜子里对应的另一边也必须“太亮”；可是另一边的亮度早就被算清楚了，不可能那么亮。矛盾再次出现。</p>
<p>“三次”这个词来自一个特殊的数域（把 √−3 加进有理数得到的世界）。正是因为结构里有“三次”，才能动用三次剩余、高斯和这些几百年前就磨好的老工具。</p>

<h3>（3）分两步走：从 11/12 推到 7/8</h3>
<p>第一阶段先证明：Re(s) &gt; 11/12 之内没有零点。第二阶段再引入“素数补偿”“非对称尺度”和两个额外的矩估计，把边界从 11/12 一路推进到 7/8。</p>
<p>整个证明最费力的地方在于：所有这些比较里的“正余量”必须是<b>普适的</b> —— 不管你看的是哪一个具体函数，不管它的导子多大、位置多高，余量都不能变成 0。在无穷多个目标函数上把这件事做成统一的，就是这篇论文的主要工作量。</p>

<h2>八、这重要吗？也要说清楚“没有说”的部分</h2>

<h3>重要在哪里</h3>
<ul>
  <li>它回答了“固定的无零点半平面存在吗、能有多宽”这个问题，而且给出具体数字 7/8。</li>
  <li>无零点区域越宽，素数定理的误差就被压得越好。这类结果是解析数论里最有用的工具之一。</li>
  <li>它覆盖的不是一个函数，而是一大类 L-函数，对研究数域中的素数分布也有意义。</li>
</ul>

<h3>没有说的是什么</h3>
<ul>
  <li><b>黎曼猜想仍然没有被证明。</b>从 7/8 到 1/2 之间还有 3/8 的宽度，那里仍然可能藏着零点。</li>
</ul>

<div class="eq">{{m:gap}}</div>

<ul>
  <li>而且，即使把 7/8 一路推到 1/2 也不够：黎曼猜想要的是“零点<b>恰好</b>在 1/2 线上”，而不是“不超过 1/2”。</li>
  <li>论文也没有证明广义黎曼猜想（GRH）之类的更强命题。</li>
</ul>

<div class="warn">
<b>一个必须说清楚的提醒：</b>这是一篇 2026 年 9 月底公开的<b>预印本</b>（作者署名 OpenAI），<b>还没有经过同行评审</b>。数学史上，越是重大的结论，越要等专业数学家把每一步（199 页的每一步）逐条检查完。所以准确的说法是：<b>这篇论文声称解决了准黎曼假设</b>，而不是“准黎曼假设已经被证实”。读任何重大数学新闻时，都请保留这个习惯。
</div>

<h2>九、小词典</h2>

<table class="gloss">
  <tr><td>素数</td><td>只能被 1 和自己整除的整数，如 2、3、5、7。</td></tr>
  <tr><td>π(x)</td><td>从 1 到 x 之间素数的个数。</td></tr>
  <tr><td>复数 / 实部</td><td>形如 a+bi 的数；Re(s) 表示它的实部 a。</td></tr>
  <tr><td>ζ 函数</td><td>黎曼定义的那个函数，它的零点决定了素数的分布。</td></tr>
  <tr><td>零点</td><td>让函数值等于 0 的那些点。</td></tr>
  <tr><td>临界线</td><td>Re(s) = 1/2 这条竖线。黎曼猜想认为所有非平凡零点都在它上面。</td></tr>
  <tr><td>半平面</td><td>地图上某条竖线右边（或左边）的一大片区域。</td></tr>
  <tr><td>无零点区域</td><td>可以保证没有零点的那片区域。</td></tr>
  <tr><td>L-函数</td><td>ζ 函数的一大类“亲戚”，各自对应不同的数论对象。</td></tr>
  <tr><td>Dirichlet 特征</td><td>给整数按“除以某个数的余数”分组的标签，用于研究等差数列中的素数。</td></tr>
  <tr><td>Hecke L-函数</td><td>在更一般的数域（例如加了 √−3 的世界）上定义的 L-函数。</td></tr>
  <tr><td>高斯和</td><td>一串“转圈”的数相加（形如 e<sup>2πik/n</sup>），专门用来描述对称性。</td></tr>
  <tr><td>theta 函数</td><td>对称性极强的函数，像镜子，反射前后形状相似。</td></tr>
  <tr><td>模形式</td><td>拥有一大堆对称性的函数；theta 函数是最简单的例子之一。</td></tr>
  <tr><td>矩估计</td><td>研究“平均行为”的工具 —— 像统计全班平均分，而不是盯住每个同学。</td></tr>
  <tr><td>大筛法</td><td>数论里估计“一大堆和加起来有多大”的经典工具。</td></tr>
  <tr><td>幂节省</td><td>比“刚刚够用”多出来的安全余量，通常是 x 的某个小次幂。</td></tr>
  <tr><td>预印本</td><td>先公开、还没经过同行评审的论文。</td></tr>
</table>

<h2>十、如果你还想自己玩一玩</h2>

<ul>
  <li><b>动手数一数：</b>用计算器或几行 Python，数出 100、1000、10000 以内各有多少个素数，再和 x/ln x 比一比，看看差多少。</li>
  <li><b>看一眼零点：</b>网上有 ζ 函数非平凡零点的数值表。它们的实部真的都是 0.5 吗？这就是“数值证据”—— 它很有说服力，但它不是证明。</li>
  <li><b>想继续读：</b>《素数之恋》（John Derbyshire）是最好的入门书；再进一步可以看 Ribenboim 的《素数的世界》，专业一点是 Davenport 的《Multiplicative Number Theory》。</li>
</ul>

<div class="note">
<b>关于这份读本：</b>它是对上述论文的通俗解读，不是论文本身，也不用于学术引用。文中的结论与数字取自论文的摘要、定理 1.1 和证明概述；“两阶段、11/12 到 7/8、立方 theta 反射、特征矩、零点探测器”等说法来自论文自己的路标。原文英文 199 页，中文全译与更详细的注记见同目录下的其他文件。
</div>
"""

CSS = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
html { font-family: 'Noto Serif CJK SC','Noto Serif',serif; }
body { font-size: 12.5pt; line-height: 1.95; color:#1a1a1a; margin:0; }
p { margin: 0 0 9pt; text-align: justify; }
h1 { font-size: 1.9em; line-height: 1.35; margin: 0 0 8pt; }
h2 { font-size: 1.32em; margin: 20pt 0 9pt; padding-bottom: 3pt; border-bottom: 1.5pt solid #d8462f; color:#8f2a17; page-break-after: avoid; }
h3 { font-size: 1.08em; margin: 13pt 0 6pt; color:#333; page-break-after: avoid; }
ul { margin: 0 0 9pt; padding-left: 1.4em; }
li { margin-bottom: 4pt; }
b { color:#111; }
.eq { text-align:center; margin: 11pt 0; page-break-inside: avoid; }
.eq svg { max-width: 92%; height: auto; vertical-align: middle; }
svg text { font-family: 'Noto Serif CJK SC', serif; }
.note { background:#fdf6e9; border-left: 4pt solid #d8a53a; padding: 9pt 11pt; margin: 12pt 0; page-break-inside: avoid; }
.warn { background:#fdecea; border-left: 4pt solid #c0392b; padding: 9pt 11pt; margin: 12pt 0; page-break-inside: avoid; }
.cover { text-align:center; padding-top: 48mm; page-break-after: always; }
.cover .kicker { font-size: 1em; letter-spacing: .25em; color:#c0392b; margin-bottom: 12mm; }
.cover h1 { font-size: 2.5em; margin-bottom: 7mm; line-height: 1.3; }
.cover .sub { font-size: 1.15em; color:#444; margin-bottom: 22mm; }
.cover .meta { font-size: .92em; color:#666; line-height: 1.9; }
table.gloss { width:100%; border-collapse: collapse; font-size: .95em; }
table.gloss td { border-bottom: 1pt solid #eee; padding: 5pt 6pt; vertical-align: top; }
table.gloss td:first-child { white-space: nowrap; color:#8f2a17; font-weight: 700; width: 5.5em; }
.newpage { page-break-before: always; }
"""


def main():
    svg = render_maths()
    doc = CONTENT
    for k, s in svg.items():
        doc = doc.replace('{{m:%s}}' % k, s)
    if '{{m:' in doc:
        print('WARNING unresolved placeholders')
    out = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
           '<title>素数的秘密，和一条 7/8 的线</title><style>%s</style></head><body>%s</body></html>'
           % (CSS, doc))
    open(HTML_OUT, 'w', encoding='utf-8').write(out)
    text = re.sub(r'<[^>]+>', '', re.sub(r'<svg[\s\S]*?</svg>', ' [公式] ', doc))
    print('html  :', HTML_OUT, '| %.0f KB | 正文约 %d 字' % (len(out) / 1024, len(re.sub(r'\s', '', text))))


if __name__ == '__main__':
    main()
