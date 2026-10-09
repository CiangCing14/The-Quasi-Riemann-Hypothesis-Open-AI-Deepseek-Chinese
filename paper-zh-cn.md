### 引言

令 \(F=\mathbb Q(\sqrt{-3})\)，设 \(\mathcal O\) 为其整数环，并记 \(N\mathfrak a=|\mathcal O/\mathfrak a|\) 为非零整理想的范数。模一个非零整理想 \(\mathfrak f\) 的有限阶 Hecke 特征 \(\eta\) 是模 \(\mathfrak f\) 的射线类群的一个特征，并零延拓到与 \(\mathfrak f\) 不互素的理想上。这与通常的有限阶伊代尔定义一致：复位不贡献任何非平凡有限阶连续特征 。对 \(\Re s>1\)，置 \[L_F(s,\eta)=\sum_{\mathfrak a\ne0}
       \frac{\eta(\mathfrak a)}{(N\mathfrak a)^s}
 =\prod_{\mathfrak p}
       \left(1-\eta(\mathfrak p)(N\mathfrak p)^{-s}\right)^{-1}.\] 同一记号也用以表示其亚纯延拓。对模 \(q\) 的 Dirichlet 特征 \(\chi\)（在非单位上零延拓），我们同样写 \[L(s,\chi)=\sum_{n\ge1}\frac{\chi(n)}{n^s}
 \qquad(\Re s>1)\] 然后将其亚纯延拓；模 \(1\) 的特征给出黎曼 zeta 函数 \(\zeta(s)\)。此处的问题是一致排除：寻找一个常数 \(\sigma_0<1\)，它与特征、其导子及高度无关，使得这些函数在 \(\Re s>\sigma_0\) 内无零点。

仅对 \(\zeta\) 而言，存在固定的 \(\sigma_0<1\) 使得 \(\zeta(s)\ne0\) 于 \(\Re s>\sigma_0\)，这称为拟黎曼假设 。它要求一个在每个高度都成立的间隙，而不仅仅是在 \(\Re s=1\) 上的非零。关于所有 Dirichlet 特征的相应一致表述出现在  中。

这些函数与素数分布之间的联系有着悠久的历史。Dirichlet 在 1837 年关于每个既约等差数列中素数无穷多的证明引入了分离剩余类的特征 \(L\) 级数 。Riemann 1859 年的论文将 \(\zeta\) 的零点与素数分布联系起来，并提出了临界线猜想 。Hadamard 和 de la Vallée Poussin 于 1896 年独立证明了 \(\zeta\) 在 \(\Re s=1\) 上无零点，从而得到素数定理 。Hecke 随后发展了特征 zeta 函数及其在数域上的解析理论 。

Hecke \(L\) 函数的经典无零点区域随着导子或高度的增大而逼近直线 \(\Re s=1\)，并可能允许一个单实例外零点；关于阿贝尔扩张的一个精确形式由  给出。这类区域不能给出固定半平面内的一致排除。零点密度估计处理的是另一个问题：它们给出位于给定竖直线右侧的零点数目的上界。例如，Guth 和 Maynard 的大值估计改进了 \(\zeta\) 的零点密度界 ，但这些零点密度界并不排除每一个零点。

<span id="thm:main" label="thm:main">\[thm:main\]</span> \(F=\mathbb Q(\sqrt{-3})\) 上的每个有限阶 Hecke \(L\) 函数在 \(\Re s>7/8\) 内无零点。对每个 Dirichlet \(L\) 函数（包括 \(\zeta(s)\)）同样成立。允许主特征在 \(s=1\) 处有极点。

特别地，定理 [\[thm:main\]](#thm:main) 肯定地解决了拟黎曼假设：\(\zeta\) 的非平凡零点（即其在 \(0<\Re s<1\) 中的零点）实部的上确界至多为 \(7/8\)。边界 \(\Re s=7/8\) 不包含在内，而 \((7/8,1)\) 中的任何例外实零点均被排除。该定理并未建立黎曼假设或其推广形式，后者将非平凡零点置于 \(\Re s=1/2\) 上。黎曼假设仍然未决 。

Kubota 的 metaplectic 理论与 Patterson 的三次 theta 级数提供了自守框架 。我们使用 Dunn 和 Radziwiłł 记录的无条件显式尖点展开 ；他们以 GRH 为条件的素数渐近不作为输入。相应的一阶矩渐近在一份独立手稿中被无条件证明 ；该结果在此亦未被使用。命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 推导出此处所用的反射，同时保留特征的零于非单位上的限制。

特征大筛法论证建立在 Goldmakher 和 Louvel 的二次 Hecke 族估计 、Blomer、Goldmakher 和 Louvel 的高阶范数递推 ，以及 Heath-Brown 的三次估计  之上。我们在引理 [\[lem:sextic-large-sieve\]](#lem:sextic-large-sieve) 中证明此处所需的确切六次特殊化，利用配对的剩余特征在主生成元约定下实现该递推。Gao 和 Zhao 也记录了 Eisenstein 整数形式 。递推矩论证与 Heath-Brown 二次方法的框架相关 。我们还使用通常的 Hecke 函数方程  以及固定射线类中的素数计数 。

第一阶段使用的平面加性大筛法是经典的；可与 Huxley 的多变量与数域不等式  以及  中的 Poisson 证明相比较。我们给出一个直接的 Eisenstein 格证明，以记录既约分数展开所需的正规化。David、de Faveri、Dunn 和 Stucky 结合 Patterson 系数、三次大筛法和磨光矩，证明一个三次 Hecke 族的正比例部分在 \(s=1/2\) 处非零 。下面的零点探测器使用经典的截断逆机制；可与  相比较，而关于高阶特征的密度应用见 。

证明分为两个阶段，每个阶段都比较一个完备化三次 theta 和的两个表示，但在延拓论证中使用不同的正规化和。部分 [](#part:eleven-twelfths) 在定理 [\[thm:eleven-twelfths\]](#thm:eleven-twelfths) 中证明相应的 \(11/12\) 断言，已对两个族得到固定的无零点半平面。部分 [](#part:seven-eighths) 从该结论出发，引入素数补偿、非对称尺度以及两个额外的矩估计。此处发展的贡献是构造这些相容的反射比较与 Poisson 比较（包括主留数），其正指数余量的选取独立于目标特征。

#### 证明概览

###### 一个共同的延拓原理。

解析论证从 \(F\) 上的本原有限阶 Hecke 特征族开始。令 \(\beta_*\) 为 \(1/2\) 与它们在 \(1/2\le\Re s\le1\) 中零点实部的上确界；极点不包含在内。非本原特征在 \(\Re s>0\) 中具有相同的可能零点，因为有限多个被略去的 Euler 因子在该处非零。若 \(\beta_*\) 超过所提议的边界 \(\sigma_0\)，则任务是把每个目标倒数延拓跨过 \(\beta_*\) 左侧一个共同的正距离。

节 [2](#sec:analytic-reduction) 给出精确的判别准则。对每个目标 \(\eta\) 及大的实尺度 \(Z\)，它在删去有限多个 Euler 因子并乘以一个有界远离零的全纯因子之后，将一个正规化特征和与一个包含 \(1/L_F(s,\eta)\) 的 Mellin 积分相比较。对和的直接界以及其与该积分之差的幂次节省界蕴含所需的延拓。两部分在 Mellin 积分中使用 \(Z\) 的不同仿射幂，应用同一原理： \[C_{\mathrm I}(s)=s-\frac23,\qquad
 C_{\mathrm{II}}(s)=s-\frac{11}{16}.\] 因此共同的解析原理并不使两个正规化和相同。只有正的幂次余量必须独立于 \(\eta\)；固定特征的常数与下阈值可以依赖于它。

###### 完备化和。

节 [2](#sec:arithmetic) 建立 \(\mathcal O\) 上的六次剩余特征，始终保留其在非单位上的零值。节 [4](#sec:probe) 中的基础和把这些特征与一个固定目标 \(\eta\) 对光滑化的三次 theta Fourier 系数取平均。在 theta 展开中固定的重标度之后，完备化指标为 \(cn^3\)，其中 \(c,n\in\mathcal O\) 模 \(3\) 同余于 \(1\) 且 \(c\) 无平方因子。变量 \(c\) 与 \(n\) 可以共享素因子。此处完备化意味着保留完整的立方因子 \(n^3\)，而不是把指标限制到其无平方因子部分。目标特征与一个有限射线类相位作用在整个乘积 \(cn^3\) 上，而不是分别作用在其两个因子上。

所得完备化基础和有两个精确表示。命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 中的反射变换其 theta 系数，同时在所得公式中保留特征的零点。Poisson 求和变换平均变量。其非零频率形如 \(ua^6\)，其中 \(u,a\in\mathcal O\) 且 \(u\) 无六次幂因子：即 \(u\) 的每个素赋值至多为五。节 [5.2](#sec:local-euler) 随后通过 Hecke \(L\) 函数的商与一个受控的 Euler 乘积来表示每个此类行的贡献。当 \(u=1\) 时，该商包含目标函数的倒数。

###### 平衡的第一阶段。

在部分 [](#part:eleven-twelfths) 中，两个平均尺度均为 \(Z^{1/2}\)。在反射一侧，基础和分离为一个完备化 theta 行与一个加性多项式。二次大筛法给出反射行的均方的界。展开加性多项式产生 \(\mathbb C/\mathcal O\) 中的既约分数；它们的间距与系数质量给出所需的平面大筛法界。Cauchy–Schwarz 不等式把命题 [\[prop:balanced-low\]](#prop:balanced-low) 中的两个范数结合起来。这一直接估计不使用后来的逆矩递推。

在 Poisson 一侧，中间行按其范数以及对于每个行所确定的有限 Hecke 扭转族在有界高度矩形中零点的位置进行分组。节 [6](#sec:detector) 为这些族分配无零点矩形。当某个行实部有一个高于探测器固定下界的被选取的零点时，它产生两个大的 Dirichlet 多项式：一个带理想 Möbius 系数，表示一个截断的倒数，另一个不带这些系数。它们有一个共同的行特征和一个共同的扭转高度。部分 [](#part:eleven-twelfths) 在其行计数中仅使用逆多项式。在行的素赋值至少为二的部分被固定之后，六次大筛法应用于其无平方因子部分；命题 [\[prop:sextic-row-count\]](#prop:sextic-row-count) 给出所得的计数。位于下界的行以及其余的小范数区间与大范数区间直接估计。

主行单独处理。其留数连同局部 Euler 恒等式给出目标 Mellin 积分的一个非零标量倍数。在正规化之后，直接估计与剩余行估计以 \(C_{\mathrm I}(s)=s-2/3\) 验证共同的延拓判别准则。这证明了定理 [\[thm:eleven-twelfths\]](#thm:eleven-twelfths)。即使对于关于 \(\zeta\) 的推论，也需要整个族，因为 Poisson 行引入了目标的有限阶 Hecke 扭转。

###### 精细化的第二阶段。

部分 [](#part:seven-eighths) 保留完备化支集与共有的算术恒等式，但修改基础和。选定的素因子提供局部补偿，以消去一个不需要的 Euler 贡献，且两个平均尺度不再相等。在新的留数计算与标量正规化之后，相应的 Mellin 信号使用 \(C_{\mathrm{II}}(s)=s-11/16\)。正规化和的低估计再次直接由反射能量与一个加性均方估计得出；节 [4](#sec:compensated-low) 对修改后的和证明它。

高估计使用零点探测器提供的两个多项式。对于 \((0,\infty)\) 上光滑紧支的 \(W\)、尺度 \(D>0\) 及有限阶 Hecke 特征 \(\psi\)，它们的基本形式为 \[D^{-1/2}\sum_{\mathfrak a\ne0}\mu(\mathfrak a)\psi(\mathfrak a)
       W(N\mathfrak a/D),\qquad
 D^{-1/2}\sum_{\mathfrak a\ne0}\psi(\mathfrak a)W(N\mathfrak a/D),\] 其中 \(\mu\) 是理想 Möbius 函数。在探测器下界之上的指定中间范数区间中，每个保留下来的行都有一个大的逆多项式和一个大的普通多项式，二者有一个共同的行特征和扭转高度。对其矩的界限制了此类行的数目。节 [8](#sec:refined-row-counts) 结合这两个界，在较大的中间范数区间中使用整数幂与选定的素因子。小范数区间与大范数区间以及下界类仍为直接估计。

这两个矩界需要分别归纳。节 [6](#sec:inverse) 证明一个逆多项式乘以互不相交素数集上的和的二阶矩估计（引理 [\[lem:marked\]](#lem:marked)）。其递推步骤使用两个有限 Poisson 变换以缩短行区间，反射能量提供终端界。节 [7](#sec:plain) 证明两个普通多项式之积的均方估计，同样带有允许的素因子（引理 [\[lem:plain\]](#lem:plain)）。通常的 Hecke 反射在每一阶段缩短长度区间；递推步骤使用两个有限 Poisson 变换。

普通估计根据是否存在素因子而保留不同的行族。当存在它们时，它排除其本原诱导特征属于由目标与辅助射线特征生成的固定有限群的行；当不存在它们时，它仅排除主诱导特征。该有限族中的变换行在归纳中单独处理。直接的体积界处理非中心化乘积。对于具有相同两个剖面且尺度乘积相等的两个乘积之差，共同的主项相互抵消。此抵消仅用于该中心化表达式，而不用于有限诱导特征族中的每一个行。

节 [9](#sec:conclusion) 把所得的行计数与补偿展开、其局部误差、围道尾部以及主留数结合起来。在正规化之后，它们的界在 \(7/8\) 处验证延拓判别准则中的第二个比较。

###### 向 Dirichlet \(L\) 函数的转移。

最终的转移在两个边界处相同。将 Dirichlet 特征 \(\chi\) 与理想范数复合，得到 \(F\) 上的一个 Hecke 特征。除去有限多个 Euler 因子之外，二次因子分解把其 \(L\) 函数写为附属于 \(\chi\) 与 \(\chi\chi_{-3}\) 的 Dirichlet \(L\) 函数之积，其中 \(\chi_{-3}\) 是 \(F/\mathbb Q\) 的二次特征。被略去的因子在 \(\Re s>0\) 中非零，主极点单独处理。因此每个 Hecke 半平面都转移到所有 Dirichlet 特征，从而完成两个阶段。

#### 素域上的最小非剩余与平方根

固定的 Dirichlet 无零点半平面还使以下经典推论成为无条件的。

<span id="cor:nonresidues-square-roots" label="cor:nonresidues-square-roots">\[cor:nonresidues-square-roots\]</span> 存在绝对常数 \(A,C>0\)，使得对每个奇素数 \(p\)，最小的正二次非剩余 \(n(p)\) 满足 \[n(p)\le C(\log p)^A.\] 特别地，\(n(p)\ll_\delta p^\delta\) 对每个 \(\delta>0\) 成立，从而证明 Vinogradov 的最小二次非剩余猜想 。给定一个奇素数 \(p\) 以及二进制表示下的 \(a\in\mathbb F_p\)，存在一个运行时间为 \(\log p\) 的多项式的确定性算法，返回 \(a\) 的一个平方根或报告不存在平方根。

由定理 [\[thm:main\]](#thm:main) 与函数方程，每个本原 Dirichlet \(L\) 函数的非平凡零点位于 \(1/8\le\Re s\le7/8\)。因此它们位于严格更大的带形域 \(1/16<\Re s<15/16\) 中。这以 \(\epsilon=7/16\) 提供了 Bhargava、Ivanyos、Mittal 和 Saxena 的弱 GRH 假设 。他们对最小二次非剩余的界给出所断言的不等式，例如取 \(A=32\)；此处无需优化。对每个 \(\delta>0\) 的断言随之成立，因为 \(\log p\) 的每个固定幂都是 \(O_\delta(p^\delta)\)。

对于算法，先处理 \(a=0\)，并用 Euler 判别法检验非零的 \(a\)。若 \(a\) 是平方数，则扫描 \(2,3,\ldots\) 直到找到二次非剩余，用每个候选的 Legendre 符号检验之。刚刚证明的界使这成为多项式时间的确定性搜索；其停止规则不需要知道 \(C\)。将所得的二次非剩余用于 Tonelli–Shanks 算法 。所有剩余步骤都是确定性的，且是 \(\log p\) 的多项式。将 \(p-1=2^e u\) 写成 \(u\) 为奇数，只需移除因子二，而不需要分解 \(u\)。

### 从一个共同信号到无零点半平面

证明的两部分使用相同的解析原理。一个特征和被直接估计，同时也与一个包含目标 \(L\) 函数倒数的 Mellin 积分相比较。两个比较中的幂次节省随后把该倒数延拓跨过最右的可能零点。我们证明此原理对于可变边界成立，从而可以在 \(11/12\) 与 \(7/8\) 处应用它，而无需重复论证。

全文设 \(F=\mathbb Q(\sqrt{-3})\)。只需考虑本原目标特征。事实上，由本原特征 \(\eta\) 诱导的特征，其 \(L\) 函数与 \(L_F(s,\eta)\) 相差有限多个因子 \(1-\eta(\mathfrak p)N\mathfrak p^{-s}\)，它们在 \(\Re s>0\) 时均非零。定义 \[\beta_* = \sup\left(\{1/2\}\cup
 \left\{\Re\rho:\begin{array}{l}
  1/2\le\Re\rho\le1,\quad L_F(\rho,\eta)=0\\
  \text{对某个本原有限阶 Hecke 特征 }\eta
 \end{array}\right\}\right).
 \label{old-eq:1.1b}\] 极点不包含在内。Euler 乘积的绝对收敛排除了 \(\Re s>1\) 中的零点，故 \(1/2\le\beta_*\le1\)。

对素理想的有限集 \(\mathcal S\)，上标 \(\mathcal S\) 表示相应的 Euler 因子已被删去： \[L_F^{\mathcal S}(s,\eta)
 =L_F(s,\eta)\prod_{\mathfrak p\in\mathcal S}
       (1-\eta(\mathfrak p)N\mathfrak p^{-s}).\] 局部值在分歧素理想处为零。所显示的每个因子在 \(\Re s>0\) 时非零，故删去有限多个因子既不会在该处产生也不会移除零点。

<span id="lem:continuation-criterion" label="lem:continuation-criterion">\[lem:continuation-criterion\]</span> 固定 \(\sigma_0\in(1/2,1)\)，并假设 \(\Delta_0=\beta_*-\sigma_0>0\)。令 \(C(s)=s+c\)，其中 \(c\in\mathbb R\) 固定。假设数 \(\omega,\sigma\) 满足 \[0<\omega<\Delta_0,\qquad \sigma>0\] 可以独立于目标特征选取。对每个本原有限阶 Hecke 特征 \(\eta\)，假设存在有限集 \(\mathcal S\)、\(\Re s>\sigma_0\) 上的全纯函数 \(H_\eta\)，以及对所有充分大的实数 \(Z\) 定义的函数 \(J_\eta(Z)\)，使得 \[\sup_{\Re s>\sigma_0}|H_\eta(s)-1|\le\frac12.
 \label{eq:signal-euler-contract}\] 对 \(Z>0\)，定义 \[f_\eta(Z)=\frac1{2\pi i}\int_{\Re s=2}
 Z^{C(s)}e^{(s-5/6)^2}
 \frac{H_\eta(s)}{L_F^{\mathcal S}(s,\eta)}\,ds.
 \label{eq:common-residue}\] 假设当 \(Z\to\infty\) 时， \[\begin{aligned}
 |J_\eta(Z)|&\ll_\eta Z^{C(\sigma_0)+\omega},
       \label{eq:low-probe-contract}\\
 |J_\eta(Z)-f_\eta(Z)|&\ll_\eta Z^{C(\beta_*)-\sigma}.
       \label{eq:high-probe-contract}\end{aligned}\] 隐含常数、下阈值、被排除的集合以及函数 \(H_\eta\) 可以依赖于 \(\eta\)。那么这些假设与 \(\beta_*>\sigma_0\) 矛盾。

令 \[\epsilon_*:=\min\{\Delta_0-\omega,\sigma\}>0.\] 因为 \(C\) 的斜率为一，三角不等式给出 \[|f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-\epsilon_*}
 \qquad (Z\ge Z_{0,\eta}).
 \label{eq:uniform-saving}\] 此外 \(\epsilon_*\le\Delta_0-\omega<\Delta_0\)，故 \(\beta_*-\epsilon_*>\sigma_0\)。

我们还需要 \(Z\downarrow0\) 时的控制。由方程 [\[eq:signal-euler-contract\]](#eq:signal-euler-contract)，\(H_\eta\) 在 \(\Re s>\sigma_0\) 上有界。倒数 Euler 乘积在 \(\Re s\ge2\) 上绝对且一致有界。在每个固定带形域 \(2\le\Re s\le B\) 上，方程 [\[eq:common-residue\]](#eq:common-residue) 中的 Gauss 函数为 \(O_B(e^{-(\Im s)^2})\)。因此矩形上的 Cauchy 定理把围道移动到任意固定的 \(B>2\)，其中水平积分趋于零。从而 \[|f_\eta(Z)|\ll_{\eta,B}Z^{B+c}\qquad(0<Z\le1).\] 由于 \(B\) 任意，该信号在零处具有任意快的幂衰减。

此界与方程 [\[eq:uniform-saving\]](#eq:uniform-saving) 表明 \[F_\eta(s):=\int_0^\infty f_\eta(Z)Z^{-C(s)}\,\frac{dZ}{Z}\] 在 \(\Re s>\beta_*-\epsilon_*\) 上局部一致收敛。在每个紧子集上，选取 \(B\) 大于零附近积分所出现的所有实部，并在无穷远处使用方程 [\[eq:uniform-saving\]](#eq:uniform-saving)。因此 \(F_\eta\) 在该半平面上全纯。

我们在不移动围道跨过零点的前提下辨认此 Mellin 变换。令 \[A_\eta(s)=e^{(s-5/6)^2}
             \frac{H_\eta(s)}{L_F^{\mathcal S}(s,\eta)}
 \qquad(\Re s>1).\] 函数 \(A_\eta(2+it)\) 关于 \(t\) 连续且可积。写 \(Z=e^u\)，则方程 [\[eq:common-residue\]](#eq:common-residue) 变为 \[e^{-(2+c)u}f_\eta(e^u)
   =\frac1{2\pi}\int_{\mathbb R}e^{itu}A_\eta(2+it)\,dt.\] 由两个端点估计，左端关于 \(u\) 可积。因此通常的 Fourier 反演给出 \(F_\eta(2+it)=A_\eta(2+it)\) 对每个实 \(t\) 成立。两端在 \(\Re s>1\) 上全纯，故由恒等定理有 \[F_\eta(s)=e^{(s-5/6)^2}
             \frac{H_\eta(s)}{L_F^{\mathcal S}(s,\eta)}
 \qquad(\Re s>1).\]

方程 [\[eq:signal-euler-contract\]](#eq:signal-euler-contract) 蕴含在 \(\Re s>\sigma_0\) 上 \(|H_\eta(s)|\ge1/2\)。因此 \[e^{-(s-5/6)^2}\frac{F_\eta(s)}{H_\eta(s)}
 \qquad(\Re s>\beta_*-\epsilon_*)\] 是 \(1/L_F^{\mathcal S}(s,\eta)\) 的一个全纯延拓。数 \(\epsilon_*\) 的选取独立于 \(\eta\)。由 \(\beta_*\) 的定义，某个目标的零点 \(\rho\) 满足 \(\Re\rho>\beta_*-\epsilon_*\)。其倒数在 \(\rho\) 处有极点，而被删去的因子在该处非零。这与延拓矛盾。

命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion) 中的高估计是相对于 \(C(\beta_*)\) 而非相对于 \(C(\sigma_0)\) 度量的。当某个行贡献达到低尺度但仍相对于假设的最右零点有幂次节省时，这一区别是重要的。部分 [](#part:eleven-twelfths) 使用 \[\sigma_0=\frac{11}{12},\qquad C(s)=s-\frac23,
 \qquad C(\sigma_0)=\frac14,\] 而部分 [](#part:seven-eighths) 使用 \[\sigma_0=\frac78,\qquad C(s)=s-\frac{11}{16},
 \qquad C(\sigma_0)=\frac3{16}.\] 只有正的幂次余量必须对目标一致。在两个应用中，固定特征的常数、被排除的集合以及充分大的下阈值都可以依赖于它。

# 拟黎曼假设

### 第一个无零点半平面

我们首先利用基本的完备化三次 theta 和证明一个固定的无零点半平面。这分离出排除零点的机制，先于为更精细边界所需的额外估计被引入。

<span id="thm:eleven-twelfths" label="thm:eleven-twelfths">\[thm:eleven-twelfths\]</span> \(F=\mathbb Q(\sqrt{-3})\) 上的每个有限阶 Hecke \(L\) 函数在 \(\Re s>11/12\) 内无零点。对每个 Dirichlet \(L\) 函数（包括 \(\zeta(s)\)）同样成立。允许主特征在 \(s=1\) 处有极点。

对 Hecke 断言，假设反证法有 \[\Delta_1:=\beta_*-\frac{11}{12}>0.
 \label{eq:first-stage-gap}\] 证明将构造一个具有两个精确表示的特征和。三次 theta 反射在一个初等加性大筛法估计之后给出该和的界。Poisson 求和把同一个和表示为一个主 Mellin 信号与一族剩余特征行。一个零点探测器与六次大筛法控制这些行。这些估计以边界 \(11/12\) 验证命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion)。

方程 [\[old-eq:1.1b\]](#old-eq:1.1b) 中的固定族是必要的，即使所需推论涉及 \(\zeta\)：Poisson 表示引入了目标的有限阶 Hecke 扭转。证明整个族范围的断言还提供了在部分 [](#part:seven-eighths) 开头所使用的精确输入。

### 算术与解析预备

两部分使用相同的算术约定与解析估计。本节固定剩余符号，即使对于主幂也保留其零值，并证明用于变换特征和的 Gauss 恒等式与互反恒等式。随后它建立一个光滑范数剖面的演算，以及在一个已知无零点圆盘上 Hecke \(L\) 函数的一致界。这些是平衡论证的共同预备。

#### 算术记号与系数类

令 \(F=\mathbb Q(\sqrt{-3})\)，令 \(\omega=e^{2\pi i/3}\)，并置 \[\mathcal O=\mathbb Z[\omega],\qquad
 \lambda=\sqrt{-3}=\omega-\omega^2=1+2\omega.\] 对元素 \(a\) 记 \(q_a=|a|^2=N_{F/\mathbb Q}(a)\)，对 \(a\ne0\) 记 \(\alpha(a)=a/|a|\)。同一记号 \(q_{\mathfrak a}\) 表示一个非零理想的范数。环 \(\mathcal O\) 关于此范数是欧几里得的：\(\mathbb C\) 中的点到三角格 \(\mathcal O\) 的距离至多为 \(1/\sqrt3<1\)，这给出欧几里得除法。特别地每个理想都是主的。六个单位是 \(\{\pm1,\pm\omega,\pm\omega^2\}\)，它们的像是 \(\mathcal O/3\mathcal O\) 的六个单位。因此每个与 \(3\) 互素的理想都有唯一的同余于 \(1\pmod3\) 的生成元；我们称此生成元为主生成元。主生成元的乘积是主的。

在下面的特征多项式估计中，行是特征多项式的外层指标，而列是求和于其内的一个理想指标或理想指标元组。标记是区分族中各部分的辅助指标。一个标记是被平均还是局部冻结是相对于当前和而言的；冻结它并不使它成为固定算术数据的一部分。

对任何给定调用中的算术数据，从一开始就固定一个素理想的有限集 \(S\)，它包含 \(6\) 之上的素数，以及该数据中每个有限阶特征表示的定模之素支集，和用于表示它们的固定有限射线群的素支集。对一个特征表示，其定模支集恰好由它被零延拓的素数组成，包括非本原表示中的任何冗余素数。一个固定特征包括其整个零延拓表示以及通过它被表示的有限射线群，所有这些都独立于 \(Z\)、当前行和被平均的标记而固定。固定数据可以依赖于事先固定的目标。特别地，每个这样的特征在 \(S\) 之外的每个素数处模为一。我们还写 \(\mathcal S=S\)。我们称 \(S\) 之外的素数为好素数，并称一个理想为好理想，若其所有素因子都位于 \(S\) 之外。除非指定了不同的支集，理想和排除 \(S\) 并使用主生成元。我们用 “sf” 表示无平方因子，用 \(\mu\) 表示理想 Möbius 函数。相比之下，元素行可以带有任意的素数幂和单位因子。

对 \(z\in F\)，定义 \[e(z)=\exp\bigl(2\pi i\operatorname{Tr}_{F/\mathbb Q}(z/\lambda)\bigr).\] 它到 \(\mathbb C\) 的延拓为 \(e(z)=\exp(4\pi i\operatorname{Im}z/\sqrt3)\)。测度 \(d\mu(z)=(2/\sqrt3)\,dx\,dy\) 使 \(\mathcal O\) 关于配对 \((z,y)\mapsto e(zy)\) 自对偶。事实上，将 \(y=u+v\omega\) 写为实 \(u,v\)，条件 \(e(y)=e(\omega y)=1\) 说明 \(v,u-v\in\mathbb Z\)，因此 \(y\in\mathcal O\)；且 \(\mathcal O\) 关于 \(d\mu\) 的余体积为一。圆盘中的格点计数， 随后除以六个单位，给出无限制的 理想计数 \[\#\{\mathfrak a:q_{\mathfrak a}\le H\}
 =\frac{\pi H}{3\sqrt3}+O(\sqrt H+1)\qquad(H\ge0).\] 例如，其误差可由用 \(O(\sqrt H+1)\) 个固定基本平行四边形覆盖圆盘边界得到。

若 \(p\notin S\) 为素数，则其剩余域阶为 \(P=q_p\equiv1\pmod6\)： 六个单位根在该域中仍互不相同。定义六次 符号 \(\chi_p(a)=(a/p)_6\) 为满足下式的唯一六次单位根 \[\chi_p(a)\equiv a^{(P-1)/6}\pmod p\quad(p\nmid a),
 \qquad \chi_p(a)=0\quad(p\mid a).\] 对 \(S\) 之外的某一主元 \(c=\prod p^{v_p(c)}\)，定义 \(\chi_c(a)=\prod_{p\mid c}\chi_p(a)^{v_p(c)}\)，并对每个 \(a\) 置 \(\chi_1(a)=1\)。对每个整数 \(j\)，包括 \(j=0\) 与负 \(j\)，记号 \(\chi_c(a)^j\) 在 \((a,c)=1\) 时表示其通常的幂，否则表示零。 因此被六整除的指数对应函数 \(1_{(a,c)=1}\)，而非常数函数一。平方 \(\chi_c^2\) 是 三次符号。对无平方因子的 \(c\)，置 \[\gamma_j(c)=q_c^{-1/2}\sum_{v\bmod c}\chi_c(v)^j e(v/c),
 \qquad \gamma_j(1)=1.\]

<span id="lem:fixed-numerator-ray" label="lem:fixed-numerator-ray">\[lem:fixed-numerator-ray\]</span> 固定 \(0\ne a\in\mathcal O\)。在素理想 \(\mathfrak p\nmid6a\) 处，令 \((a/\mathfrak p)_6\) 为与 \(a^{(q_{\mathfrak p}-1)/6}\pmod{\mathfrak p}\) 同余的唯一六次单位根；在 \(S\) 之外的素处它即为 \(\chi_p(a)\)。扩张 \(F(a^{1/6})/F\) 是有限阿贝尔的，且在 \(6a\) 的素因子之外非分歧，并且 \[\frac{\operatorname{Frob}_{\mathfrak p}(a^{1/6})}{a^{1/6}}
       =(a/\mathfrak p)_6,\] 其中 \(\operatorname{Frob}_{\mathfrak p}\) 是算术 Frobenius。因此该符号到与 \(6a\) 互素的理想上的乘法延拓是一个 有限阶射线特征，其导子的支集在 \(6a\) 的素因子上。并未断言其在那些素处的导子指数有界。 这一等同仅在与 \(6a\) 互素的理想上成立；当好的理想 \(A\) 与 \(a\) 相交时， 它并不抹去 \(\chi_A(a)\) 的指定零点。

特别地，为每个 \(\mathfrak p\in S\) 选取一个生成元 \(\pi_{\mathfrak p}\)。在 \(S\) 之外的主元理想上，特征 \[A\longmapsto\chi_A\left(u\prod_{\mathfrak p\in S}
                       \pi_{\mathfrak p}^{v_{\mathfrak p}}\right),
 \qquad u\in\mathcal O^\times,\quad v_{\mathfrak p}\ge0,\] 属于同一个有限射线特征族，具有公共模 支集在 \(S\) 上；该族由 \(u\) 与剩余 \(v_{\mathfrak p}\pmod6\) 决定。

令 \(\xi^6=a\)。由于 \(F\) 含所有六次单位根，\(X^6-a\) 的所有根 都落在 \(F(\xi)\) 中，且 \(\sigma\mapsto\sigma(\xi)/\xi\) 将其 Galois 群嵌入 \(\mu_6\)。 因此该扩张是阿贝尔的。\(6a\) 之外的素处非分歧； 例如这可由 \(X^6-a\) 的判别式推出，该判别式的支集 在 \(6a\) 上。在这样的素处，算术 Frobenius 在 剩余域上由 \(x\mapsto x^{q_{\mathfrak p}}\) 刻画。因此它在 \(\xi\) 上的商约化为 \(a^{(q_{\mathfrak p}-1)/6}\)。约化在 \(6\) 之外的 \(\mu_6\) 上单射，从而证明了所显示的等式。 Artin 映射的乘法性给出关于理想的断言。Artin 互反律使该 映射分解过一个射线群，其模的支集在整除 \(6a\) 的素因子上；这些正是  中的幂剩余与射线群断言。

对于最后的论断，\(S\) 之外的理想 \(A\) 与每个 \(\pi_{\mathfrak p}\) 以及与每个单位都互素。因此其符号在那里没有零点， 且每个 \(\chi_A(\pi_{\mathfrak p})\in\mu_6\) 的幂仅 依赖于 \(v_{\mathfrak p}\pmod6\)。在此约化之后至多有 \(6^{|S|+1}\) 个可能的所显示分子。对每个应用 第一个断言，并取其射线模的公共倍数。 它们的素支集全部包含于 \(S\)，因为 \(S\) 含有 \(6\) 之上的素理想。

本引理中"固定"一词至关重要：含变动 好素处的分子并不因此进入一个独立于 \(Z\) 而固定的射线群。 其特征及其自然零点支集仍是变动数据。

在基 \(Z>1\) 处，实对数长度为 \(n\) 的朴素多项式为 \[S_\psi(n;W)=Z^{-n/2}\sum_l\psi(l)W(q_l/Z^n),
 \label{old-eq:1.1}\] 而对数长度为 \(r\) 的中心正规化逆多项式为 \[M_\psi(r;W)=Z^{-r/2}\sum_n\mu(n)\psi(n)W(q_n/Z^r).
 \label{old-eq:1.1a}\] 两个定义中都保留了 \(\psi\) 中的每个掩码。在基 \(U\) 处，当 \(\psi(n)=\nu(n)\chi_n(u)\) 时，我们也将后一多项式记为 \(M_u(U^r;W)\)，或在 \(D=U^r\) 时记为 \(M_u(D;W)\)。

环形检验函数是一个光滑函数，其支集位于 \((0,\infty)\) 的一个固定紧 子区间内。环形剖面或耦合剖面的族仅 与固定的对数支集以及对所引用的每个对数导数的一致界一起使用。 精确的分离范数 由引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 给出。在两个朴素因子的乘积中， 两个因子具有相同的行特征，包括相同的固定有限射线 扭转。在绝对值内对整体因子取共轭允许 相反取向；仅对其系数的一部分取共轭则不允许。

我们采用如下一致性约定。对数长度取值于固定的 有界集合，且每个估计允许任意指定的正幂次损失。 范数尺度的指数仅依赖于那些实参数范围、 严格余量以及指定的损失。 记 \(\mathcal A\) 为此固定的算术数据：固定有限特征的完备零延拓 表示、其定义模与用于表示它们的固定有限射线群、 被排除的集合，以及任何固定的 算术正规化。它的选取独立于 \(Z\)、当前各行 以及被平均的标记，尽管它可以依赖于先前固定的 目标。有限半范数阶、多项式高度阶、 隐含常数与下阈值可以依赖于 \(\mathcal A\)。它们 在所声明的变动的模与外标记各自的所述范围内是一致 的，即使某个外标记在某次行求和期间被固定。

对非零理想 \(\mathfrak a\)，令 \(d_{\mathcal O}(\mathfrak a)=\#\{\mathfrak d:\mathfrak d\mid\mathfrak a\}\)， 其中计数包含所有整理想因子，包括与 \(S\) 相交者；并对 \(0\ne f\in\mathcal O\) 置 \(d_{\mathcal O}(f)=d_{\mathcal O}((f))\)。 非负重数 \(w(f)\) 称为除子有界的，仅当 \[w(f)\le C\,d_{\mathcal O}(f)^C\] 对某个固定的 \(C\ge1\) 成立，该 \(C\) 独立于 \(Z\)、当前各行与被平均的 标记。常数 \(C\) 可以依赖于 \(\mathcal A\)。 该约定不放松任何要求 \(w\) 仅依赖于 \(f\) 的独立条件。对每个 \(\delta>0\)，它蕴含 \(w(f)\ll_{C,\delta}q_f^\delta\) 一致成立。事实上，对范数充分大的素理想 \(\mathfrak p\)， 由 \(e\ge1\) 时 \(e+1\le2^e\) 可知，对每个整数 \(e\ge0\) 有 \((e+1)^C\le q_{\mathfrak p}^{\delta e}\)。 对其余有限多个素理想中的每一个， \(\sup_{e\ge0}(e+1)^Cq_{\mathfrak p}^{-\delta e}<\infty\)；在 \(f\) 的素因子分解上 乘这些界即证得该断言。

#### Gauss 和与有限互反相位

我们首先计算素 Gauss 和。这也固定了 所有后续公式中三次符号的取向。

<span id="lem:prime-gauss-identities" label="lem:prime-gauss-identities">\[lem:prime-gauss-identities\]</span> 设 \(p\) 为 \(S\) 之外某素理想的主生成元，并置 \(H=\chi_p\)、\(P=q_p\)。则 \[\gamma_2(p)^3=-\alpha(p),\qquad
 \gamma_1(p)\gamma_2(p)
   =\overline{H(4)}\gamma_3(p)\gamma_2(p)^3.\] 对 \(j\not\equiv0\pmod6\)，有 \(|\gamma_j(p)|=1\)。

令 \(k=\mathcal O/(p)\)，令 \(\psi(x)=e(x/p)\) 为其非平凡加性 特征。对 \(k^\times\) 的乘法特征 \(A\)，按零 延拓，置 \[\tau(A)=\sum_{x\in k}A(x)\psi(x),\qquad
 J(A,B)=\sum_{x\in k}A(x)B(1-x).\] 若 \(A\) 非主，则变量替换 \(x=ty\) 给出 \[|\tau(A)|^2
 =\sum_{t\in k^\times}A(t)\sum_{y\in k^\times}\psi((t-1)y)=P.\] 内和在 \(t=1\) 时为 \(P-1\)，否则为 \(-1\)，且 \(\sum_{t\in k^\times}A(t)=0\)。取共轭还给出 \(\tau(A)\tau(\overline A)=A(-1)P\)。当 \(AB\) 非主时，按 \(x+y\) 对乘积 \(\tau(A)\tau(B)\) 分组给出 \[\tau(A)\tau(B)=J(A,B)\tau(AB).\] \(x+y=0\) 的组为零，因为 \(AB\) 非主；对非零 的和，除以 \(x+y\) 给出所显示的 Jacobi 因子。特别地 若 \(A,B,AB\) 均非主，则 \(|J(A,B)|=\sqrt P\)。

\(4x(1-x)=y\) 的解数为 \(1+H^3(1-y)\)。将 \(H(y)\) 乘此恒等式求和，并利用 \(\sum_yH(y)=0\)，给出 \(J(H,H^3)=H(4)J(H,H)\)。记 \(\tau_j=\tau(H^j)\)。 Gauss–Jacobi 恒等式与 \(\tau_2\tau_4=P\) 现在给出 \[\frac{\tau_1\tau_3}{\tau_4}
   =H(4)\frac{\tau_1^2}{\tau_2},\qquad
 \tau_1\tau_2=\overline{H(4)}\frac{\tau_3\tau_2^3}{P}.\] 这里 \(H^2(-1)=1\)，因为 \(-1\) 是三次方。

尚需固定三次 Jacobi 和，包括其单位。置 \(m=(P-1)/3\)。\(H^2\) 的定义在 \(k\) 中给出 \[J(H^2,H^2)\equiv\sum_{x\in k}x^m(1-x)^m=0\pmod p.\] 事实上该多项式的次数为 \(2m<P-1\)，且每个次数小于 \(P-1\) 的单项式在 \(k\) 上的和 为零（在 \(k\) 中；常数情形为 \(k\) 中的 \(P=0\)）。Jacobi 和属于 \(\mathcal O\)，其绝对 值为 \(\sqrt P\)。

对 \(x\ne0,1\)，选取 \(j_x\in\{0,1,2\}\) 使得 \(H^2(x(1-x))=\omega^{j_x}\)。在这些 \(x\) 上 \(x\) 与 \(1-x\) 的乘积 均为 \(-1\)，故 \(\prod_{x\ne0,1}x(1-x)=1\)。因此 \(\sum_{x\ne0,1}j_x\equiv0\pmod3\)。由于 \[\omega^j\equiv1+j(\omega-1)\pmod{(\omega-1)^2},
 \qquad ((\omega-1)^2)=(3),\] 我们得到 \(J(H^2,H^2)\equiv P-2\equiv-1\pmod3\)。被 \(p\) 整除 与范数相等蕴含 \(J(H^2,H^2)=up\)，其中 \(u\) 为单位。由于 \(p\) 是主元且六个单位的模 \(3\) 剩余互不相同，该同余式 迫使 \(u=-1\)。最后， \(\tau_2^3=J(H^2,H^2)\tau_2\tau_4=-pP\)。将两个 Gauss 恒等式 除以 \(\sqrt P\) 的适当幂即证得本引理。

剩余的相位是二次的。其下文的计算即使对 非无平方因子或非主元的奇元素也有效。

<span id="lem:quadratic-four-term" label="lem:quadratic-four-term">\[lem:quadratic-four-term\]</span> 对非零奇 \(c\in\mathcal O\)，定义 \[\Gamma(c)=|c|^{-1}\sum_{x\bmod c}e(x^2/c).\] 则 \[\label{eq:quadratic-four-term}
 \Gamma(c)=\frac12\sum_{y\bmod2\mathcal O}e(-cy^2/4).\] 对 \(c=a+b\omega\)，右端为 \((1+i^{-b}+i^a+i^{b-a})/2\)。特别地 \(\Gamma\) 仅依赖于 \(c\bmod4\mathcal O\)，且对每个奇 \(v\) 有 \(\Gamma(cv^2)=\Gamma(c)\)。 模 \(4\) 的单位有平方子群 \(\{1,\omega,\omega^2\}\) 与 平方类代表元 \(1,-1,\lambda,-\lambda\)。函数 \(\Gamma\) 在这些单位上从不取零，且 \(\mathfrak r(a,b)=\Gamma(ab)/(\Gamma(a)\Gamma(b))\) 满足 \[\label{eq:reciprocity-four-class}
 \begin{gathered}
 \begin{array}{c|rrrr}
  c&1&-1&\lambda&-\lambda\\ \hline
  \Gamma(c)&1&1&i&-i
 \end{array}\\
 \mathfrak r((-1)^e\lambda^f,(-1)^g\lambda^h)
       =(-1)^{eh+fg+fh},\qquad e,f,g,h\in\{0,1\}.
 \end{gathered}\] 因此 \(|\Gamma(c)|=1\)，且 \(\mathfrak r\) 是 平方类群上的对称 \(\{\pm1\}\)-值双特征。

使用核为 \(e(-zy)\)、测度为 \(d\mu\) 的 Fourier 变换。 对 \(\varepsilon>0\)，在 \(\mathcal O\) 上对 \(f_\varepsilon(z)=e(z^2/c)e^{-\pi\varepsilon|z|^2}\) 应用 Poisson 求和。直接 Gauss 积分给出，其中 \(r_\varepsilon=1+3q_c\varepsilon^2/16\)， \[\widehat f_\varepsilon(y)
 =\frac{|c|}{2\sqrt{r_\varepsilon}}
    e^{-\pi\varepsilon q_c|y|^2/(4r_\varepsilon)}
    e\bigl(-cy^2/(4r_\varepsilon)\bigr).\] 为验证正规化，将 \(z\) 旋转 \(c\) 的辐角的一半。所得的 实二元 Gauss 的二次矩阵为 \[\begin{pmatrix}
 \varepsilon&-4i/(\sqrt3|c|)\\
 -4i/(\sqrt3|c|)&\varepsilon
 \end{pmatrix},
 \qquad \det=\frac{16r_\varepsilon}{3q_c}.\] 其特征值为具有正实部的共轭对。行列式的正平方 根、\(d\mu\) 中的因子 \(2/\sqrt3\) 以及配方 给出上述公式。

置 \(I_\varepsilon=\int_{\mathbb C}e^{-\pi\varepsilon|z|^2}d\mu(z)
=2/(\sqrt3\varepsilon)\)。对固定理想 \((b)\)、固定类 \(v\bmod b\) 以及 \(a>0\)，在 \(b\mathcal O\) 上的 Gauss Poisson 求和给出 \[\frac1{I_\varepsilon}\sum_{z\in v+b\mathcal O}
             e^{-\pi a\varepsilon|z|^2}
 \longrightarrow\frac1{a q_b}\qquad(\varepsilon\downarrow0).\] 零对偶向量给出极限，每个非零对偶向量都 指数级小。相位 \(e(z^2/c)\) 模 \(c\) 周期。 因此 Poisson 恒等式正规化后的左端趋于 \(\Gamma(c)/|c|\)。

在右端可将 \(r_\varepsilon\) 替换为 \(1\)。对固定 \(c\)， 来自相位的总误差至多为 \[C_c\varepsilon^2\sum_{y\in\mathcal O}|y|^2
                         e^{-C_c^{-1}\varepsilon|y|^2}=O_c(1),\] 因为该和为 \(O_c(\varepsilon^{-2})\)。振幅误差为 \(O_c(\varepsilon)\)，阻尼误差由同样的格点估计亦然。 三者均为 \(o(I_\varepsilon)\)。相位 \(e(-cy^2/4)\) 模 \(2\mathcal O\) 周期。在前述 Gauss 均值中取 \(b=2\)、\(a=q_c/4\)； 其四个类的每个正规化均值均为 \(1/q_c\)。正规化后的右 端因此趋于 \((2|c|)^{-1}\sum_{y\bmod2}e(-cy^2/4)\)，这证明了 方程 [\[eq:quadratic-four-term\]](#eq:quadratic-four-term)。

模 \(2\) 的代表元 \(0,1,\omega,\omega^2\) 给出所断言的 四项表达式。乘以奇 \(v\) 置换这些类， 故同一公式给出 \(\Gamma(cv^2)=\Gamma(c)\)。模 \(4\) 的单位 群的阶为 \(12\)。模 \(4\) 的提升的平方仅依赖于其 模 \(2\) 的类，且其三种可能的平方为 \(1,\omega,\omega^2\)。 论断中的四个代表元模该子群互不相同； 又 \(\lambda^2=-3\equiv1\pmod4\)。将四项表达式在 它们上求值给出该表。将 \(\Gamma(ab)/(\Gamma(a)\Gamma(b))\) 在两个 生成元 \(-1,\lambda\) 上求值给出所显示的指数，证明了最后的 论断。

<span id="lem:fixed-gauss-phase" label="lem:fixed-gauss-phase">\[lem:fixed-gauss-phase\]</span> 对 \(S\) 之外互素的主元 \(a,b\)， \[\chi_b(a)=\mathcal R(a,b)\chi_a(b),\qquad
 \mathcal R(a,b)=\mathfrak r(a,b).\] 在 \(S\) 之外的所有主元对上，包括非互素对，按 方程 [\[eq:reciprocity-four-class\]](#eq:reciprocity-four-class) 的双特征 \(\mathfrak r\) 定义 \(\mathcal R\)。在 \(S\) 之外的每个主元指标上定义 \[G(c)=\overline{\chi_c(4)}\Gamma(c).\] 其模为一，且分解过一个支集在 \(2,3\) 上的固定射线群。 对所有这样的 \(v,w\)， \[\label{eq:G-quadratic-refinement}
 G(vw)=G(v)G(w)\mathcal R(v,w),\qquad G(1)=1.\] 此外 \(G(v^2)=\chi_v(4)\)，且在好素处 \[\label{eq:fixed-gauss-phases}
 G(p^3)=\gamma_3(p),\qquad
 \mathcal R(p,p)=\gamma_3(p)^2=\chi_p(-1).\] 在 \(S\) 之外的每个主元 \(n\) 上，有 \(\chi_n(-1)=\mathcal R(n,n)\)。对角线 \(t\mapsto\mathcal R(t,t)\) 是 固定射线群的特征。在方程 [\[eq:reciprocity-four-class\]](#eq:reciprocity-four-class) 的平方类记号中，它是 \(\mathfrak r(-1,n)\)，其中 \(-1\) 表示其模 \(4\) 的剩余平方类，而非 单位理想 \((-1)\) 的理想射线类。 对无平方因子的 \(c\)，完备 Gauss 恒等式为 \[\label{eq:signal}
 \gamma_2(c)^3=\mu(c)\alpha(c),\qquad
 \gamma_1(c)\gamma_2(c)=\mu(c)\alpha(c)G(c),\qquad
 G(c)=\overline{\chi_c(4)}\gamma_3(c),\quad |G(c)|=1.\] \(G\) 在非无平方因子指标上的所有出现均指刚定义的有限射线 函数，而非非无平方因子的 Gauss 和。

在好素处，在剩余域中计数平方根给出 \[\sum_{x\bmod p}e(x^2/p)
 =\sum_{y\bmod p}(1+\chi_p(y)^3)e(y/p)
 =\sum_{y\bmod p}\chi_p(y)^3e(y/p).\] 不含特征的加性和为零。因此 \(\Gamma(p)=\gamma_3(p)\)，且对单位 \(u\) 将 \(x^2/p\) 替换为 \(ux^2/p\) 使该和乘以 \(\chi_p(u)^3\)。对无平方因子的 \(c\)，将剩余表示为 \(\sum_{p\mid c}(c/p)x_p\) 在两个和中给出 \[\Gamma(c)=\prod_{p\mid c}\chi_p(c/p)^3\Gamma(p),\qquad
 \gamma_3(c)=\prod_{p\mid c}\chi_p(c/p)^3\gamma_3(p).\] 平方中的交叉项在加性特征下为整。 因此对无平方因子的 \(c\) 有 \(\Gamma(c)=\gamma_3(c)\)。特别地，对互不相同的 好素处 \(p,q\)， \[\frac{\Gamma(pq)}{\Gamma(p)\Gamma(q)}
 =\chi_p(q)^3\chi_q(p)^3.\]

我们使用如下精确形式的三次互反律：对互素的主元 \(a,b\)，有 \((a/b)_3=(b/a)_3\)；见 。因此 商 \(\chi_b(a)/\chi_a(b)\) 是一个符号。在 \(p,q\) 处其三次方为 \(\chi_q(p)^3\chi_p(q)^3\)，故此符号等于 \(\mathfrak r(p,q)\)。 两个变元的乘法性与双特征性质将该 等式推广到每个互素主元对。用 \(\mathfrak r\) 在 非互素对上的定义不涉及零符号的除法。

元素 \(-2\) 是主元，且 \(-1\) 是三次方。因此三次互反律 给出 \[\chi_c(4)=(2/c)_3=(-2/c)_3=(c/(-2))_3.\] 这是 \(c\bmod2\) 的特征。连同 \(\Gamma\) 对 \(c\bmod4\) 的依赖，这证明了 \(G\) 是固定射线群上的函数（例如模 \(12\) 的射线群在此已足够）。事实上，若两个主元 生成元表示模 \(12\) 的同一射线类，则其商与一个模 \(12\) 同余于一的元素相差一个单位；模 \(3\) 约化 迫使该单位为 \(1\)。因此这些生成元有相同的 模 \(4\) 剩余。其乘法性 加细即为 \(\mathfrak r\) 的定义。由于 \(\Gamma(v^2)=1\)，且 \(\chi_v(4)\) 的阶整除三， \(G(v^2)=\overline{\chi_v(4)}^{\,2}=\chi_v(4)\)。该表还给出 \[\Gamma(p)^2=(-1)^{(q_p-1)/2}=\chi_p(-1).\] 对最后的等式，使用 \(\chi_p(-1)=(-1)^{(q_p-1)/6}\) 以及这些奇偶性的相等。 现 \(\Gamma(p^3)=\Gamma(p)\)，且 \(\overline{\chi_p(4)}^{\,3}=1\)，证明了 \(G(p^3)=\gamma_3(p)\)。最后 \(\mathcal R(p,p)=1/\Gamma(p)^2=\Gamma(p)^2\)，因为该平方是一个符号。

对对称的符号值双特征，其对角线是乘法的： \[\mathcal R(vw,vw)
 =\mathcal R(v,v)\mathcal R(v,w)^2\mathcal R(w,w)
 =\mathcal R(v,v)\mathcal R(w,w).\] 素恒等式因此给出：对 \(S\) 之外的每个主元 \(n\)，有 \(\mathcal R(n,n)=\chi_n(-1)\)。在平方类 \((-1)^e\lambda^f\) 上， 该表给此对角线与 \(\mathfrak r(-1,n)\) 都赋予值 \((-1)^f\)。 这里对 \(-1\) 的使用是在剩余平方类群中；理想 \((-1)\) 是理想射线类群中的单位元，在此并未被代入。

对 \(S\) 之外互素的无平方因子主元 \(a,b\)，中国剩余定理给出 \[\gamma_j(ab)=\chi_a(b)^j\chi_b(a)^j\gamma_j(a)\gamma_j(b).\] 将剩余表示为 \(bx+ay\)，其中 \(x\bmod a\)、 \(y\bmod b\)，即得此式。对 \(j=2\) 的因子取三次方得一。 \(j=1\) 与 \(j=2\) 的因子之积为 \((\chi_a(b)\chi_b(a))^3=\mathcal R(a,b)\)。来自 引理 [\[lem:prime-gauss-identities\]](#lem:prime-gauss-identities) 的素恒等式，随后由 方程 [\[eq:G-quadratic-refinement\]](#eq:G-quadratic-refinement)，因此按素因子个数 归纳证明了方程 [\[eq:signal\]](#eq:signal)。

对于后面的元素行，固定来自 引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 的生成元 \(\pi_{\mathfrak p}\)。每个 \(0\ne m\in\mathcal O\) 有 唯一表达式 \[m=u m_S m_{\mathrm{good}},\qquad
 m_S=\prod_{\mathfrak p\in S}\pi_{\mathfrak p}^{v_{\mathfrak p}(m)},\] 其中 \(u\) 是单位，\(m_{\mathrm{good}}\) 是 \((m)\) 在 \(S\) 之外部分的 主元生成元。在 \(S\) 之外的每个主元 \(A\) 上，乘法性 与六次互反律给出保零恒等式 \[\label{eq:row-fixed-ray-reduction}
 \chi_A(m)=\chi_A(u m_S)\mathcal R(A,m_{\mathrm{good}})
       \prod_{p\mid m_{\mathrm{good}}}\chi_p(A)^{v_p(m)}.\] 对 \((A,m_{\mathrm{good}})=1\)，这是刚才证明的互反公式； 若它们相交，则两端为零，且 \(\mathcal R\) 按其 单独定义的双特征求值。一旦好的部分的固定射线类与 \(S\)-赋值模六固定，右端的头两个因子 就取值于 \(A\) 的一个固定有限特征族。关于 好素处的乘积保留变动的特征因子及其全部零点。

固定有限阿贝尔射线群上的每个函数都有有限 Fourier 展开（用其特征）。例如，若 \(\phi:T\to\mathbb C\)，则 \[\phi(v)=\sum_{\theta\in\widehat T}a_\theta\theta(v),\qquad
 a_\theta=\frac1{|T|}\sum_{u\in T}\phi(u)\overline{\theta(u)}.\] Parseval 与 Cauchy–Schwarz 将 \(\sum_\theta|a_\theta|\) 界为 \(|T|^{1/2}\max_T|\phi|\)。在 \(T\times T\) 上应用同一论断将 \(\mathcal R(a,b)\) 分离为特征的乘积的有限和。 这些展开在非互素主元对处仍然有效，因为 那里的 \(\mathcal R\) 是固定射线双特征，而非符号商。 例如，对好素处 \(p\) 与 \(S\) 之外的每个主元 \(n\)， \[\chi_n(p)\overline{\chi_p(n)}
       =\mathcal R(p,n)1_{(n,p)=1}.\] 在互素对上这是六次互反律，在其余对上两端 均为零。因此变动局部特征的抵消可能留下 互素指示函数与固定射线相位两者；二者皆不可舍去。

#### 光滑范数剖面

以下约定使特征多项式估计中的光滑依赖性 成为定量的。它们区分固定检验函数的导数与谱高度的幂。 当 Fourier 尾部仅在高度范围选定之后 才被移除时，这一区分是必要的。

对 \((0,\infty)^d\) 上对数支集位于固定紧集 \(\Omega\subset\mathbb R^d\) 中的剖面 \(w\)，置 \[w_{\log}(\boldsymbol u)=w(e^{u_1},\ldots,e^{u_d}),\qquad
 p_j(w)=\sum_{|\alpha|\le j}\sup_{\boldsymbol u\in\mathbb R^d}
                  |\partial^\alpha w_{\log}(\boldsymbol u)|.\] 我们始终约定 \(w_{\log}\) 光滑且支集在 \(\Omega\) 中。 定义 \[\widehat w(\boldsymbol t)=\int_{\mathbb R^d}w_{\log}(\boldsymbol u)
                    e^{-i\boldsymbol t\cdot\boldsymbol u}\,d\boldsymbol u,
 \qquad
 \|w\|_{J,\mathrm{sep}}
 =\int_{\mathbb R^d}|\widehat w(\boldsymbol t)|
                    (1+|\boldsymbol t|)^J\,d\boldsymbol t.\] 对固定的有限元组 \(\boldsymbol w=(w_1,\ldots,w_r)\)（其维数可以 各不相同但均固定），我们使用 \(p_j(\boldsymbol w)=1+\sum_{i=1}^r p_j(w_i)\)。

<span id="lem:smooth-calculus" label="lem:smooth-calculus">\[lem:smooth-calculus\]</span> 对整数 \(J\ge0\)， \[\|w\|_{J,\mathrm{sep}}\ll_{J,d,\Omega}p_{J+d+2}(w).\] 对数 Fourier 反演分离任何固定的范数单项式。更 精确地，若 \(x_j=c_j\prod_{\ell=1}^r y_\ell^{a_{j\ell}}\)，其中 \(c_j,y_\ell>0\)、 实指数 \(a_{j\ell}\) 固定，则 \[w(x_1,\ldots,x_d)=\frac1{(2\pi)^d}\int_{\mathbb R^d}
 \widehat w(\boldsymbol t)\prod_j c_j^{it_j}
       \prod_\ell y_\ell^{i\sum_j a_{j\ell}t_j}\,d\boldsymbol t.\] 若此公式中的系数测度对一族 行是公共的，则只要该分离界的高度增长至多为 \((1+|\boldsymbol t|)^J\)，Minkowski 不等式就利用 \(\|w\|_{J,\mathrm{sep}}\) 将任何分离的行 \(\ell^2\) 界 通过积分传递。

对单位盒 \(I\subset\mathbb R^d\) 与 \(I+[-1,1]^d\) 上的光滑标量函数 \(F\)， \[\label{eq:parameter-sobolev}
 \sup_I|F|^2\ll_d
 \sum_{\alpha\in\{0,1\}^d}
 \int_{I+[-1,1]^d}|\partial^\alpha F|^2.\] 因此，在相应的导数界之下，多项式范围内尺度的逐行 选择代价为 \(\log Z\) 的幂，而绝对值至多 \(T_1\) 的范数扭转高度的 逐行选择代价为 \(1+T_1\) 的固定幂。

对 \(T_1\ge1\) 与整数 \(J,N\ge0\)， \[\label{eq:late-fourier-tail}
 \int_{|\boldsymbol t|>T_1}|\widehat w(\boldsymbol t)|
             (1+|\boldsymbol t|)^J\,d\boldsymbol t
 \le T_1^{-N}\|w\|_{J+N,\mathrm{sep}}.\] 在 Mellin 约定 \(\mathcal MW(s)=\int_0^\infty W(y)y^s\,dy/y\) 下，纯扭转满足 \[\mathcal M[W(y)y^{i\omega}](s)=\mathcal MW(s+i\omega).\] 设 \(D_y=y\partial_y\)，设 \(I\subset\mathbb R\) 为紧集，并设 \(N\ge0\) 为整数。假设下述积分有限，且在 \(N\) 次对数分部积分中的边界项 消失。则对 \(\sigma\in I\) 与 \(T\in\mathbb R\) 一致地， \[\label{eq:pointwise-mellin-tail}
 |\mathcal MW(\sigma+iT)|
 \ll_{I,N}(1+|T|)^{-N}
     \sum_{j=0}^N\int_0^\infty y^\sigma|D_y^jW(y)|\,\frac{dy}{y}.\] 对每个这样的 \(I\)，这些假设对环状 \(W\) 成立。当 \(W\) 在零点处光滑、 在无穷远处为 Schwartz 函数且 \(I\) 是 \((0,\infty)\) 的紧子集时，它们 同样成立。特别地，虚坐标固定的水平围道衔接由此逐点界估计，而 不只是由方程 [\[eq:late-fourier-tail\]](#eq:late-fourier-tail) 中的积分尾部估计。

下面的联合版本也将有用。对使右端有限的可测函数 \(a(v),b(w)\)，以及整数 \(J,N\ge0\)， \[\label{eq:joint-gaussian-slice}
 \begin{split}
 &\int_{\mathbb R^2}e^{-(T+v)^2}|a(v)b(w)|
       (1+|T|+|v|+|w|)^J\,dv\,dw\\
 &\quad\ll_{J,N}(1+|T|)^{-N}
       \sup_v(1+|v|)^{J+N}|a(v)|
       \int_{\mathbb R}(1+|w|)^J|b(w)|\,dw.
 \end{split}\] 因此，两个高度之和中的一个 Gaussian 与另外两个高度中快速下降的 Mellin 变换之乘积，在固定高度切片上具有快速的逐点衰减。对积分 尾部，线性映射 \((t_1,t_2,t_3)\mapsto(t_1+t_2,t_2,t_3)\) 可逆，故该 乘积的所有固定加权 \(L^1\) 矩也控制原始高度中盒子的补集。再附加 有限多个分离频率以及这三个变元的固定线性平移，通过块三角变量 替换得到相同的结论。

在 Mellin 变量中平移纯扭转后，被 \(Z^B(1+|\boldsymbol t|)^J\) 界定 的、被舍弃的分离被积函数的绝对尾部至多为 \(Z^BT_1^{-N}\|w\|_{J+N,\mathrm{sep}}\)。这里 \(B\) 与 \(J\) 必须在选定 \(N\) 之前固定。一致光滑的分离剖面的进一步导数改变的是这最后一个 半范数，而不是先前固定的高度阶。在与 \(T_1\) 可比的高度处、实长度 有界的衔接上，阶为 \(N+\lceil J\rceil\) 的 方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 给出 \(Z^BT_1^{-N}\) 乘以外部 测试函数的相应有限加权导数范数，只要其他因子在那里具有所述的界。 当那些外部范数一致时，这是 \(O(Z^BT_1^{-N})\)。

对满足 \(2m>J+d\) 的整数 \(m\)，分部积分给出 \[(1+|\boldsymbol t|^2)^m\widehat w(\boldsymbol t)
 =\int_{\mathbb R^d}(1-\Delta)^m w_{\log}(\boldsymbol u)
                       e^{-i\boldsymbol t\cdot\boldsymbol u}\,d\boldsymbol u.\] 其绝对值被 \(\Omega\) 的体积乘以 \(C_{m,d}p_{2m}(w)\) 界定。加权积分 有限，因为 \(2m>J+d\)；可选取 \(2m\le J+d+2\)。Fourier 反演给出单项式 公式。对 \(\ell^2\) 中的行向量 \(B(\boldsymbol t)\)，那里所用的精确 不等式为 \[\left\|\frac1{(2\pi)^d}\int\widehat w(\boldsymbol t)
                 B(\boldsymbol t)\,d\boldsymbol t\right\|_{\ell^2}
 \le\frac1{(2\pi)^d}\int|\widehat w(\boldsymbol t)|
                 \|B(\boldsymbol t)\|_{\ell^2}\,d\boldsymbol t.\]

在一维情形，微积分基本定理、将基点在对扩大后的区间上取平均， 以及 Cauchy–Schwarz 给出 \(\sup_I|F|^2\ll\int_{I+[-1,1]}(|F|^2+|F'|^2)\)。在每个坐标上依次 应用它，即证明方程 [\[eq:parameter-sobolev\]](#eq:parameter-sobolev)。由于所有项非负， 它可以在导数积分之前按行求和。长度 \(O(\log Z)\) 的对数尺度区间 需要 \(O(\log Z)\) 个单位区间；高度区间 \([-T_1,T_1]\) 需要 \(O(1+T_1)\) 个区间。关于对数尺度的导数插入 \(yW'(y)\)，连同中心 正规化的常数导数一起插入。正规化扭转 \(y^{it}\) 的导数插入 \(\log y\) 的幂。这些仍是有界半范数的环状剖面。例如，若固定参数的 平方行界为 \(O((1+|t|)^H)\) 且有 \(d_t\) 个高度参数，则覆盖与积分 至多花费 \((1+T_1)^{H+d_t}\) 的固定倍数。

在 \(|\boldsymbol t|>T_1\) 上有 \((1+|\boldsymbol t|)^{-N}\le T_1^{-N}\)，这证明了 方程 [\[eq:late-fourier-tail\]](#eq:late-fourier-tail)。Mellin 平移由其定义立即得出。 为证明方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail)，置 \(F_\sigma(u)=e^{\sigma u}W(e^u)\)。对 \(|T|\ge1\)，分部积分给出 \[\mathcal MW(\sigma+iT)=(-iT)^{-N}
              \int_{\mathbb R}F_\sigma^{(N)}(u)e^{iTu}\,du,
 \qquad
 F_\sigma^{(N)}(u)=e^{\sigma u}\sum_{j=0}^N
       \binom Nj\sigma^{N-j}D_y^jW(e^u).\] 取绝对值即给出紧实带形域上的界。对 \(|T|<1\)，在增大常数后绝对值 积分给出该界。所述两类 \(W\) 具有所需的端点衰减：第一类中紧支集即 足够，而第二类中 \(-\infty\) 处的 \(e^{\sigma u}\) 与 \(+\infty\) 处的 Schwartz 衰减即足够。

对 方程 [\[eq:joint-gaussian-slice\]](#eq:joint-gaussian-slice)，利用 \[1+|T|\le(1+|T+v|)(1+|v|),\qquad
 1+|T|+|v|+|w|\le2(1+|T+v|)(1+|v|)(1+|w|).\] 将 \((1+|T|)^N\) 移至左端，逐点界定加权的 \(a(v)\)，并将剩余的多项式 权重对 \(T+v\) 中的 Gaussian 积分。剩余的 \(w\) 积分即为所展示者。 这证明了联合界以及所断言的衔接估计。对积分断言，映射 \((t_1,t_2,t_3)\mapsto(t_1+t_2,t_2,t_3)\) 及其逆都有固定的算子范数。 因此原始变量中的固定多项式权重被变换后变量中的固定多项式权重 界定。在盒子的补集上，插入该权重的额外逆幂，并分别对 Gaussian 与 两个 Mellin 因子积分。附加的块三角映射具有相同的性质，因为它的 所有系数及其逆的系数都是固定的。

依赖于公共乘积（如 \(y_1y_2\)）的核在单项式公式中对两个变量给出 相同的范数幂；这保持等乘积尺度的差。非光滑算术掩码没有这种导数 界，因此必须在本引理应用之前予以处理。

<span id="lem:gaussian-annular" label="lem:gaussian-annular">\[lem:gaussian-annular\]</span> 置 \[W_{\mathrm G}(y)=\frac1{2\sqrt\pi}
                         \exp\bigl(-\tfrac14(\log y)^2\bigr).\] 该函数不是环状的。选取固定的 \(\chi\in C_c^\infty(\mathbb R)\) 使得 \(\sum_{k\in\mathbb Z}\chi(u-k)=1\)，并定义 \[W_{{\mathrm G},k}(y)=W_{\mathrm G}(y)\chi(\log y-k),\qquad
 w_k(x)=W_{\mathrm G}(e^k x)\chi(\log x).\] 剖面 \(w_k\) 有一个固定的紧对数支集，且对每个固定的 \(A\ge0\) 与整数 \(j\ge0\)， \[\label{eq:gaussian-annular-sum}
 \sum_{k\in\mathbb Z}e^{A|k|}p_j(w_k)<\infty.\] 因此，在 \(y=e^k x\) 之后，可在每个环带上应用 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus)，且所得的加权分离范数可和。对固定的 \(\kappa>0\)、\(A,B,C_0\ge0\) 与 \(M>0\)，还有 \[Z^B\sum_{|k|>\kappa\log Z-C_0}e^{A|k|}p_j(w_k)\ll Z^{-M}
       \qquad(Z\to\infty).\] 直接地，\(\mathcal MW_{\mathrm G}(s)=e^{s^2}\)，且 方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 中的加权对数导数在每个紧实 带形域上一致有限。

这样的分拆由将 \([-1/2,1/2]\) 上为正的非负紧支光滑函数的整数平移 正规化得到。设 \(\operatorname{supp}\chi\subset[-C,C]\)。 \(W_{\mathrm G}(e^k x)\) 的每个对数导数是 \(k+\log x\) 的多项式乘以 同一 Gaussian。故乘积法则给出 \[p_j(w_k)\le C_j(1+|k|)^j
             \exp\bigl(-\tfrac14((|k|-C)_+)^2\bigr).\] 对每个固定的 \(A\)，乘以 \(e^{A|k|}\) 后它可和。第一断言随之成立，而 分离范数由引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 得到。在剖面的对数 Fourier 变换中，对一个环带作缩放只插入单位相位 \(e^{-ikt}\)，故它 不改变这些范数；周围的多项式的任何实正规化保持显式。在所指示的 尾部上，乘以 \(Z^Be^{A|k|}\) 后的最后界的对数至多为 \(-c\kappa^2(\log Z)^2+O(\log Z)\)，其中 \(c>0\) 固定；对 Gaussian 尾部求和即证明对每个 \(M\) 的所述估计。最后，置 \(u=\log y\) 并在其 Gaussian 积分中配方得到 \(\mathcal MW_{\mathrm G}(s)=e^{s^2}\)。 同一 Gaussian 在 \(L^1(\mathbb R)\) 中界定每个 \(e^{\sigma u}(d/du)^jW_{\mathrm G}(e^u)\)，对 \(\sigma\) 在紧区间上 一致。

我们记录伴随这一分离的两类核的显式有限阶连续性陈述。它们不对 算术变换作任何断言；该变换必须提供所述的核及其可用的实直线。

<span id="lem:kernel-seminorms" label="lem:kernel-seminorms">\[lem:kernel-seminorms\]</span> 对 \(\mathbb R^d\) 上的 Schwartz 函数 \(f\)，置 \[s_j(f)=\sum_{|\alpha|,|\beta|\le j}
             \|x^\alpha\partial^\beta f(x)\|_{L^1(\mathbb R^d)}.\] 对每个 \(A\ge0\) 与多重指标 \(\beta\)，通常的 Fourier 变换满足 \[\sup_\xi(1+|\xi|)^A|\partial^\beta\widehat f(\xi)|
 \ll_{A,\beta,d}s_{\lceil A\rceil+|\beta|}(f).\] 对任何固定的非退化线性 Fourier 配对，相同的结论在常数作固定改变后 成立。对写为 \(\widehat f(\xi)=F(|\xi|^2)\) 的径向变换，任何预先 给定的界 \[\sup_{r\ge0}(1+r)^A|(r\partial_r)^jF(r)|\] 因此被 \(f\) 的有限多个 Schwartz 半范数控制。

对 Mellin 断言，设 \(m(s)\) 在固定的闭竖直带形域上全纯，并假设在 那里一致地 \(|m(\sigma+it)|\le C(1+|t|)^h\)，其中 \(h\ge0\) 固定。 在该带形域中一条可用的直线 \(\Re s=\sigma\) 上定义 \[K_W(x)=\frac1{2\pi i}\int_{(\sigma)}\mathcal MW(-s)m(s)x^{-s}\,ds,\] 其中 \(W\) 具有使该积分绝对收敛所需的有限加权对数导数，且对数 分部积分中的边界项消失。对每个整数 \(j\ge0\)， \[|(x\partial_x)^jK_W(x)|
 \ll x^{-\sigma}\int_{\mathbb R}
       |\mathcal MW(-\sigma-it)|(1+|t|)^{h+j}\,dt.\] 右端的积分被有限多个 \(y^{-\sigma}|(y\partial_y)^kW(y)|\,dy/y\) 的 积分界定，对 \(\sigma\) 在固定带形域中一致。对 \(W(y)y^{i\omega}\)， 同一位界至多额外花费因子 \((1+|\omega|)^{h+j}\)。乘以固定的环状 截断后，这些结论也界定 \(y\mapsto K_W(Ry)\) 的每个固定对数半范数， 带有因子 \(R^{-\sigma}\)。

对 \(\widehat f\) 求导插入 \(x^\beta\)，而在 \(\xi\) 中乘以单项式在对 \(x^\beta f\) 作 Fourier 变换之前对其求导。Fourier 变换的 \(L^1\) 界、 乘积法则，以及将 \((1+|\xi|)^A\) 用次数至多为 \(\lceil A\rceil\) 的 单项式的有限和来界定，给出第一断言。对径向函数，\(r\partial_r\) 对应于 \((\xi\cdot\partial_\xi)/2\)。展开其 \(j\) 次幂给出 Fourier 导数的有限多个多项式倍数，故第一断言给出径向的那个。固定的线性 坐标变换只改变其常数。

对 Mellin 断言，在绝对收敛积分下求导插入 \((-s)^j\)。在固定带形域 上它被常数乘以 \((1+|t|)^j\) 界定。写 \(y=e^u\)，并将 \(e^{-\sigma u}W(e^u)\) 的 Fourier 变换分部积分超过 \(h+j+1\) 次。 乘积法则将所得的 \(L^1\) 导数用所述的加权对数导数界定，因为 \(\sigma\) 取值于固定集合。对纯扭转，Mellin 被积函数是 \(\mathcal MW(-\sigma-it+i\omega)\)。作替换 \(v=t-\omega\) 并利用 \((1+|v+\omega|)^{h+j}\le(1+|v|)^{h+j}(1+|\omega|)^{h+j}\)。 最后，固定环状截断的乘积法则与 \(Ry\) 的链式法则给出最后断言。

#### Hecke 函数的增长与对数控制

圆盘估计仅在该圆盘中的零点被排除之后才会应用。下面的初等增长界 为复分析论证提供输入，并明确哪些常数关于导子是一致的。当 \(\psi\) 是 Hecke 特征时，\(L(s,\psi)\) 简记 \(L_F(s,\psi)\)。本小节中 \(\Gamma(s)\) 表示 Euler gamma 函数；有限二次函数 \(\Gamma(c)\) 被 限制在上面的算术恒等式中。

<span id="lem:hecke-strip-growth" label="lem:hecke-strip-growth">\[lem:hecke-strip-growth\]</span> 设 \(\psi\) 是 \(F\) 的本原非主有限阶 Hecke 特征，其导子范数为 \(Q\)。 则 \[\label{eq:hecke-growth}
 |L(\sigma+it,\psi)|\ll Q^{3/5}(3+|t|)^2,
 \qquad-1/10\le\sigma\le11/10.\] 对主特征，带 \(Q=1\) 的同一界对 \((s-1)\zeta_F(s)/(s+1)\) 成立，在 \(s=1\) 处使用可去值。

有限阶特征具有平凡无穷类型，因为 \(\mathbb C^\times\) 连通。此情形 下的本原 Hecke 函数方程为 \[\Lambda(s,\psi)=(3Q)^{s/2}(2\pi)^{-s}\Gamma(s)L(s,\psi),\qquad
 \Lambda(s,\psi)=\varepsilon(\psi)\Lambda(1-s,\overline\psi),
 \quad |\varepsilon(\psi)|=1.\] 这是  中所述平凡无穷类型的本原特征的函数 方程；非主 \(L(s,\psi)\) 为整函数。绝对 Euler 收敛将 \(L(11/10+it,\psi)\) 关于 \(Q,t\) 一致地界定。在 \(\Re s=-1/10\) 上 应用函数方程与 Stirling 公式给出 \[|L(-1/10+it,\psi)|\ll Q^{3/5}(3+|t|)^{6/5}.\] 对有界 \(t\) 的估计由 gamma 商在该直线上的连续性得到，故那里的 常数也是一致的。

为完整起见，使用带形域原理所需的增长假设可直接由格 theta 积分 得到。设 \(\mathfrak f=(f)\) 为导子，并定义周期剩余特征 \(\phi(a)=\psi((a))\)（当 \((a,\mathfrak f)=1\) 时），否则取值为零。 对主导子 \((1)\)，置 \(\phi(a)=1\) 对所有 \(a\) 成立，包括 \(a=0\)。 由于理想类群平凡，导子为一的没有非主特征。模 \(\mathfrak f\) 的 周期性由射线特征性质得到；\(\phi\) 在六个单位上平凡，因为对单位 \(u\) 有 \((u)=(1)\)。因此，对 \(\Re s>1\)， \[6\pi^{-s}\Gamma(s)L(s,\psi)
 =\int_0^\infty\bigl(\Theta_\phi(v)-\phi(0)\bigr)v^{s-1}\,dv,
 \qquad
 \Theta_\phi(v)=\sum_{a\in\mathcal O}\phi(a)e^{-\pi vq_a}.\] 因子六计算每个理想的生成元个数。若 \(\widehat\phi(h)=Q^{-1}\sum_{a\bmod f}\phi(a)e(-ha/f)\)， 有限 Fourier 反演与 Gaussian Poisson 求和给出 \[\Theta_\phi(v)=\frac{2}{\sqrt3v}
 \sum_{h\bmod f}\widehat\phi(h)
 \sum_{b\in\mathcal O}
    \exp\left(-\frac{4\pi|b-h/f|^2}{3v}\right).\] 改变生成元 \(f\) 只是对有限和重作指标。对每个固定的导子，非零对偶 向量有正的最小长度。令 \(A_\phi=2\widehat\phi(0)/\sqrt3\)，这证明了 \[\Theta_\phi(v)=A_\phi v^{-1}+O_\phi(v^{-1}e^{-c_\phi/v})\quad(0<v\le1),
 \qquad
 \Theta_\phi(v)=\phi(0)+O_\phi(e^{-c_\phi v})\quad(v\ge1)\] 其中 \(c_\phi>0\)。将 Mellin 积分在 1 处拆分因而给出 \[\begin{split}
 6\pi^{-s}\Gamma(s)L(s,\psi)
 ={}&\frac{A_\phi}{s-1}-\frac{\phi(0)}s
 +\int_0^1\bigl(\Theta_\phi(v)-A_\phi/v\bigr)v^{s-1}\,dv\\
 &+\int_1^\infty\bigl(\Theta_\phi(v)-\phi(0)\bigr)v^{s-1}\,dv.
 \end{split}\] 两个积分都是整函数，且在每个有界实带形域上关于高度有界，常数可 依赖于固定的导子。因此 \(1/\Gamma(s)\) 的 Stirling 公式对 \(L(s,\psi)\) 在该带形域上给出至多指数级的高度增长。在主情形，乘以 \((s-1)/(s+1)\) 后相同的结论成立。带形域原理只用到对每个固定导子的 这种定性增长。

为了明确看出固定导子的增长常数不进入一致带形域界，置 \[H_Q(s)=Q^{-3/5}\frac{L(s,\psi)}{(s+2)^2}.\] 它在闭带形域上全纯，并由已证明的界在两条竖直边界直线上被一个 绝对常数 \(C\) 界定。对 \(\delta>0\)，对 \(H_Q(s)\exp(\delta(s-1/2)^2)\) 在高度为 \(T\) 的矩形上应用最大值 原理。在竖直边上，指数的模至多为 \(e^{9\delta/25}\)，因为 \(|\Re s-1/2|\le3/5\)。在水平边上其模至多为 \(e^{\delta(9/25-T^2)}\)，当 \(T\to\infty\) 时它比定性的固定 \(Q\) 指数增长更快地趋于零。先对此固定的 \(Q,\delta\) 令 \(T\to\infty\)， 然后令 \(\delta\downarrow0\)。结果是 \(|H_Q(s)|\le C\) 在整个带形域 上成立，且对每个 \(Q\) 有相同的常数。乘以 \(Q^{3/5}|s+2|^2\) 即 证明方程 [\[eq:hecke-growth\]](#eq:hecke-growth)。

对主函数，因子 \((s-1)/(s+1)\) 消去其在带形域中唯一的极点，并在 边界上有界。其函数方程给出带 \(Q=1\) 的相同边界界。该方程也可由 前面的 Poisson 公式取 \(\phi=1\) 得到：写 \(v=2t/\sqrt3\) 后，theta 关系为 \(\Theta_\phi(2t/\sqrt3)=t^{-1}\Theta_\phi(2/(\sqrt3t))\)， 其拆分的 Mellin 积分在 \(s\mapsto1-s\) 下不变。对 \((s-1)\zeta_F(s)/((s+1)(s+2)^2)\) 应用相同的阻尼矩形论证。

<span id="lem:logarithmic-control" label="lem:logarithmic-control">\[lem:logarithmic-control\]</span> 设 \(\psi\) 是导子范数为 \(Q\) 的本原非主有限阶 Hecke 特征，并置 \(\mathcal L(s)=L(s,\psi)\)。对主特征置 \(Q=1\) 与 \(\mathcal L(s)=(s-1)\zeta_F(s)/(s+1)\)，在 1 处取其可去值。固定 \(a\in[1/2,1]\) 与 \(0<e<10^{-3}\)。假设 \(\mathcal L\) 在以 \(2+it\) 为心、半径为 \(2-a-2e\) 的开圆盘中没有零点。则在半径为 \(2-a-6e\) 的闭同心圆盘上一致地， \[\label{eq:disk-control}
 |\mathcal L(s)|+|\mathcal L(s)^{-1}|
 \ll_{e,\epsilon}\{2Q(3+|t|)^2\}^{\epsilon}.\] 在半径为 \(2-a-8e\) 的圆盘上还有 \[|\mathcal L'(s)/\mathcal L(s)|\ll_e\log\{2Q(3+|t|)^2\}.\] 特别地，对每个固定的 \(b\ge\beta_*\) 与 \(v>0\)，这些界在 \(\Re s\ge b+v\) 上成立，常数依赖于 \(v,\epsilon\)（并以 \(s\) 的高度 代替 \(t\)）。在主情形，倒数界传递到 \(1/\zeta_F\)；上界与对数导数界 是对正规化函数 \(\mathcal L\) 而言的。

写 \(R_j=2-a-je\) 与 \(\mathcal C=2Q(3+|t|)^2\)。这里所用的所有圆盘 都落在 \(\Re s>1/2\) 中，主正规化因子在那里全纯。在无零点圆盘上， 选取全纯对数 \(g=\log\mathcal L\)，其在中心附近的值是 Euler 对数， 并在主情形连同正规化因子的对数一起选取。值 \(g(2+it)\) 一致有界。 引理 [\[lem:hecke-strip-growth\]](#lem:hecke-strip-growth) 与 \(11/10\) 右方的 Euler 收敛 给出 \[\Re g(s)=\log|\mathcal L(s)|\ll\log\mathcal C
       \qquad(|s-(2+it)|\le R_3).\] 可能的高度与 \(t\) 相差至多 \(3/2\)，这已包含在 \(\mathcal C\) 中。 在半径 \(R_3,R_4\)（其差为 \(e\)）上的 Borel–Carathéodory 现在 给出在半径 \(R_4\) 的圆盘上 \(|g|\ll_e\log\mathcal C\)。

在固定半径 \(r_0=49/100\) 的圆盘上，\(\Re s\ge151/100>1\)。绝对收敛 的 Euler 对数在那里一致有界。对主函数，\((s-1)/(s+1)\) 的对数在该 圆盘上也有界，使用其在 \(\Re s>1\) 中的分支。由于 \(r_0<R_6<R_4\)，对 \(g\) 应用 Hadamard 三圆定理给出 \[\max_{|s-(2+it)|\le R_6}|g(s)|
 \ll_e(\log\mathcal C)^\theta,
 \qquad
 \theta=\frac{\log(R_6/r_0)}{\log(R_4/r_0)}<1.\] 对固定的 \(e\)，在紧区间 \(1/2\le a\le1\) 上的连续性使 \(\theta\) 一致地小于一。对每个 \(\epsilon>0\)， \(\exp(C_e(\log\mathcal C)^\theta)\ll_{e,\epsilon}\mathcal C^\epsilon\)。 将其应用于 \(e^g\) 与 \(e^{-g}\) 二者即证明 方程 [\[eq:disk-control\]](#eq:disk-control)。在半径 \(R_6\) 与 \(R_8\) 之间的 Cauchy 估计给出对 \(g'=\mathcal L'/\mathcal L\) 的所述界。

对全局断言，先设 \(\beta_*\le b\le1\)。选取 \(0<e<\min(10^{-3},v/8)\) 并置 \(a=b\)。半径 \(R_2\) 的圆盘包含在 \(\Re s>b+2e>\beta_*\) 中，故由 \(\beta_*\) 的定义与超过一的绝对 Euler 收敛它是无零点的。半径 \(R_8\) 的圆盘覆盖其中心高度处的点 \(b+v\le\Re s\le2\)；Euler 收敛覆盖 \(\Re s\ge2\)。前面的常数关于 \(b\) 一致。若 \(b>1\)，则 \(\Re s\ge1+v\) 上的 Euler 收敛足够。最后 \[\frac1{\zeta_F(s)}=\frac{s-1}{s+1}\mathcal L(s)^{-1},
 \qquad \left|\frac{s-1}{s+1}\right|\le1\quad(\Re s\ge0),\] 这证明了主倒数断言。

<span id="lem:deleted-euler-factors" label="lem:deleted-euler-factors">\[lem:deleted-euler-factors\]</span> 设 \(R\) 是无平方因子理想，且对 \(p\mid R\) 有 \(|a_p|\le1\)。置 \(D_R(s)=\prod_{p\mid R}(1-a_pq_p^{-s})\)。对固定的 \(\sigma_0>0\) 与 每个 \(\epsilon>0\)， \[|D_R(s)|+|D_R(s)^{-1}|\ll_{\sigma_0,\epsilon}q_R^\epsilon
       \qquad(\Re s\ge\sigma_0).\] 在有界实带形域上，关于高度一致地有， \[|D_R(s)|\ll_\epsilon q_R^{(-\Re s)_++\epsilon},
 \qquad
 \left|\frac{D_R'(s)}{D_R(s)}\right|
 \ll_{\sigma_0}\log(2q_R)\quad(\Re s\ge\sigma_0).\] 特别地，有界 \(B\) 的支集 \(q_R\le Z^B\) 在固定的正实半平面上以 \(Z\) 的任意预先给定的正幂为代价。对非本原函数 \(L(s,\psi^*)D_R(s)\)，在应用对数控制时必须同时包含本原导子与删除 根 \(R\)。

每个因子在 \(\Re s>0\) 上非零。对 \(\Re s\ge\sigma_0\)，其绝对值与其 逆的绝对值都至多为 \((1-q_p^{-\sigma_0})^{-1}\)。对充分大的 \(q_p\) （依赖于 \(\sigma_0,\epsilon\)）， \(-\log(1-q_p^{-\sigma_0})\le\epsilon\log q_p\)。有限多个较小的素数 贡献一个固定常数。这证明了第一个估计。对任何实 \(\sigma\)， \[\prod_{p\mid R}(1+q_p^{-\sigma})
 \le q_R^{(-\sigma)_+}2^{\#\{p:p\mid R\}}
 \ll_\epsilon q_R^{(-\sigma)_++\epsilon}.\] 最后的不等式通过分离出满足 \(q_p<2^{1/\epsilon}\) 的有限多个素数 得到。最后，对数求导给出 \[\left|\frac{D_R'}{D_R}(s)\right|
 \le\sum_{p\mid R}\frac{\log q_p}{q_p^{\sigma_0}-1}
 \ll_{\sigma_0}\log(2q_R).\] 若 \(q_R\le Z^B\)，选取第一个估计中的指数小于 \(Z\) 的期望指数除以 \(B\) 的有界值；\(B=0\) 的情形立即成立。这证明了对被删除因子的所述 解释。

### 完备化的三次反射与无标记行能量

本节首先变换 Gauss 系数的完备化和，同时在其特征中保留每一个零 延拓。然后它将该恒等式与二次大筛法结合，以界定其在任意非零元素 行上的均方。在行长度与完备化长度相等时，结果是平衡论证所需的界 \(Z^{1+\epsilon}\)。

theta 函数及其在三个固定尖点处的 Fourier 系数是来自 Dunn 与 Radziwi<span>ł</span><span>ł</span>  的无条件输入。 原始的系数与尖点计算见 Patterson ；这里的 正式输入仍为  中的公式。下面的有限变换推导带掩码的公式， 包括其局部因子与相位。后面的均方论证只在固定其有限尖点扇区之后 才使用该相位。

#### 完备化反射

写 \[\check e(z)=\exp\bigl(2\pi i(z+\bar z)\bigr),
 \qquad e(z)=\check e(z/\lambda)\qquad(z\in\mathbb C).\] 在 \(F\) 上，\(\check e\) 中的指数为 \(2\pi i\operatorname{Tr}_{F/\mathbb Q}z\)。对每个整数指数，剩余 特征的幂在非单位处理解为零。特别地，\(\chi_p(x)^0=1_{p\nmid x}\)。

<span id="prop:completed-reflection" label="prop:completed-reflection">\[prop:completed-reflection\]</span> 固定一族导子支集在 \(S\) 上的有限射线特征 \(\mathcal X\)。选取一个 固定的整模 \(\mathfrak E\)，其素支集恰为 \(S\)，且被该族中的每个导子 整除。在主元素上，将 \(\mathcal X\) 的每个成员在 \(\mathfrak E\)-单位 之外作零延拓。选取单个 \(L\in\mathcal O\setminus\{0\}\)，其素支集为 \(S\)，满足 \((18)\mid(L)\) 与 \(\mathfrak E\mid(L)\)，且大到足以使对 每个 \(\Psi_0\in\mathcal X\)，\(\mathcal O\) 上的函数 \[\phi(x)=
 \begin{cases}
 \chi_x(\lambda)^2\Psi_0(x),&x\equiv1\pmod3,\ (x,\mathfrak E)=1,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad
 \widehat\phi(h)=q_L^{-1}\sum_{x\bmod L}\phi(x)e(-hx/L)\] 为 \(L\)-周期的。零分支的取值不涉及任一特征的计算。由三次补充 定律与射线周期性，这样的 \(L\) 之选择存在，如以下所验证。 \(\mathfrak E\) 与 \(L\) 二者对整个族都是固定的，在任何运动的素数被 选取之前。固定一个成员 \(\Psi_0\in\mathcal X\) 并置 \(\mathfrak L=(L)\)。设 \(\mathcal P\) 是任意不整除 \(L\) 的互异主素数 的有限集，对每个 \(p\in\mathcal P\) 选取 \(j_p\in\{0,1,\ldots,5\}\)，并在主元素上置 \[\Psi(n)=\Psi_0(n)\prod_{p\in\mathcal P}\chi_p(n)^{j_p}.\] 下面的乘积中，两个变量之间不施加互素条件： \[\begin{split}
 D(s,\Psi)&=\sum_{\substack{n\equiv1\ (3)\\(n,\mathfrak E)=1}}^{\rm sf}
       \gamma_2(n)\bar\alpha(n)\Psi(n)q_n^{-s},\\
 L_0(s,\Psi)&=\sum_{\substack{b\equiv1\ (3)\\(b,\mathfrak E)=1}}
       \bar\alpha(b)^3\Psi(b)^3q_b^{-3s+1/2},
       \qquad T(s,\Psi)=L_0(s,\Psi)D(s,\Psi).
 \end{split}\] 两个级数及其乘积对 \(\Re s>1\) 绝对收敛。

设 \(X>0\)。 设 \(V\in C^\infty(0,\infty)\)，并且对每个 \(C>0\) 及每个整数 \(j\ge0\)，当 \(x\to0\) 时 \((x\partial_x)^jV(x)\) 为 \(O_{C,j}(x^C)\)，当 \(x\to\infty\) 时为 \(O_{C,j}(x^{-C})\)。 定义 \[\widehat V(t)=\int_0^\infty V(x)x^t\,\frac{dx}{x}.\] 待变换的磨光表达式是完备化和 \[\begin{split}
 &\frac1{2\pi i}\int_{(a)}\widehat V(s-1/2)X^{s-1/2}T(s,\Psi)\,ds\\
 &\quad=\sum_{\substack{n\ {\rm sf},\ b\\n,b\equiv1\ (3)\\(nb,\mathfrak E)=1}}
 \frac{\gamma_2(n)\overline{\alpha(nb^3)}\Psi(nb^3)}
      {\sqrt{q_n}\,q_b}
 V\!\left(\frac{q_nq_b^3}{X}\right),\qquad a>1.
 \end{split}\] 此等式由绝对收敛与 Mellin 反演推得。 特征作用在整个指标 \(nb^3\) 上，其取零的值保留； \(n\) 与 \(b\) 可以有公共素因子。

反射检验函数定义为 \[K=\frac{(2\pi)^4}{27},\qquad
 R(t)=\prod_{\pm}\frac{\Gamma(1+t\pm1/6)}{\Gamma(1-t\pm1/6)},\] \[V^\sharp(x)=\frac1{2\pi i}\int_{(\sigma)}
       \widehat V(-t)R(t)(Kx)^{-t}\,dt\qquad(\sigma\ge0).\] 定义 \(V^\sharp\) 的积分绝对收敛，且与 \(\sigma\ge0\) 无关。

乘积 \(T\) 具有整函数延拓。 在每个固定竖直 带形域上它具有多项式增长，其中常数允许依赖于 \(L,\Psi_0,\mathcal P,(j_p)\) 及该带形域。 存在一组固定的三重 尖点系数函数，从 \(\lambda^{-4}\mathcal O\setminus\{0\}\) 到 \(\mathbb C\)，由证明中的 theta 展开构造。 同一 三重函数用于算术数据、尺度与检验剖面的所有选择。 对上述每个固定的算术选择，存在一族有限的项， 按 (1) 中的方式编号，独立于 \(X\)、\(V\) 及围道参数 \(a>1\)。 在每一项中，\(d\) 取自 这组三重函数，而 \(\vartheta\) 是 \(\mathcal O\) 的一个加性特征， 模一个仅依赖于 \(L\) 的固定模；它们按扇区的依赖关系 恰如 (3) 所述，其余数据具有性质 (1)–(3)。 对这些项及每个 \(a>1\)，恒等式为 \[\label{eq:reflection}
 \begin{aligned}
 &\frac1{2\pi i}\int_{(a)}\widehat V(s-1/2)X^{s-1/2}T(s,\Psi)\,ds\\
 &\quad=\sum_{\text{terms}}\zeta
 \sum_{0\ne\mu\in\lambda^{-4}\mathcal O}
 \frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}
 \prod_{p\ {\rm active}}B_p(\lambda^4\mu)
 V^\sharp\!\left(\frac{q_\mu X}{q_c^2}\right).
 \end{aligned}\] 每个内和绝对收敛。 这些项具有以下 精确性质。

1.  一项由 \(h_0\bmod L\) 及活跃素数的子集确定。 每个 \(j_p\ne0\) 的 \(p\) 都是活跃的，而 \(j_p=0\) 的素数可以是 活跃的或非活跃的。 记 \(r=\prod_{p\ {\rm active}}p\)。 则 \(c=c_Fr\)，其中 \(c_F\) 是 \(\lambda^2h_0/L\) 的既约分母，附以一个正规化单位。 于是 \(c_F\) 遍历一个 固定的有限集，且其素因子整除 \(L\)。 共有 \(O_{\mathfrak L}(2^{|\mathcal P|})\) 项，或在把下一式中 每个 Ramanujan 因子拆成它的两个被加项之后为 \(O_{\mathfrak L}(4^{|\mathcal P|})\) 项。

2.  局部列因子为 \[B_p(x)=\begin{cases}
     \chi_p(x)^{-j_p-2},&j_p\ne0,4,\\
     q_p^{-1/2}(-1+q_p1_{p\mid x}),&j_p=4,\\
     q_p^{-1/2}\chi_p(x)^{-2},&j_p=0\text{ and }p\text{ is active}.
     \end{cases}\] 函数 \(d\) 是三个固定尖点系数函数之一。 把 \(u\) 记作 Eisenstein 单位，它们的支撑与大小满足 \[\operatorname{supp}d\subset
     \{u\lambda^k n b^3:k\ge-4,\ n,b\equiv1\pmod3,\ n\ {\rm sf}\},
     \qquad |d(\mu)|\le27\,3^{k/6}|b|.
     \label{old-eq:4.3}\] 该界是针对被支撑指标所展示的表示而言的。 它允许 \(n\) 与 \(b\) 有公共素数，并且除 \(\lambda\) 处所展示的限制外，对 \(L\) 的素数不施加任何排除。 特征 \(\vartheta\) 是 \(\mathcal O\) 的一个商 模一个仅依赖于 \(L\) 的固定模的加性特征。

3.  标量 \(\zeta\) 与 \(\mu\) 无关，且满足 \(|\zeta|\le1/81\)。 其关于移动素数的依赖可以精确给出。 对 \(m\not\equiv0\pmod6\)，置 \[\tau_{p,m}^{\pm}=q_p^{-1/2}\sum_{y\bmod p}\chi_p(y)^m e(\pm y/p),
     \qquad |\tau_{p,m}^{\pm}|=1.\] 对每个活跃的 \(p\)，由 \[\sigma_p=\lambda^2c/p,\qquad
     \epsilon_p=-\big((\lambda^3c/p)\sigma_p\big)^{-1},\] 定义模 \(p\) 的单位，并置 \[\omega_{p,j}=\begin{cases}
     \tau_{p,j}^{-}\tau_{p,j+2}^{+}\chi_p(\epsilon_p)^{-j-2},&j\ne0,4,\\
     \tau_{p,4}^{-},&j=4,\\
     -\tau_{p,2}^{+}\chi_p(\epsilon_p)^{-2},&j=0.
     \end{cases}\] \(\tau\) 的下标按模六读取。 令 \(M=\lambda^{12}L^4\)，存在一个绝对值为一的数 \(\kappa_F\)， 仅依赖于 \(h_0\) 及 \(r\) 模 \(M^2\) 的类，使得 \[\label{eq:reflection-row-phase}
     \zeta=-\frac i{81}\bar\alpha(c)^2\widehat\phi(h_0)\bar\kappa_F
     \prod_{p\ {\rm inactive}}(1-q_p^{-1})
     \prod_{p\ {\rm active}}\chi_p(\sigma_p)^{-2}\omega_{p,j_p}.\] 在 \(h_0\) 与 \(r\bmod M^2\) 的有限多个类中的每一个类里，\(d\) 与 \(\vartheta\) 都是固定的。 因此在该扇区内它们是公共列 因子。 除所展示的尺度 \(q_c^2\) 外， \(B_p\) 之外的所有其他移动素数依赖都包含在标量 \(\zeta\) 中，而 \(\zeta\) 可以依赖于整个活跃集。
    
    分支约定对具有相同 \(L\) 与 \(\Psi_0\) 的所有局部素数集 同时成立。 特别地，若把一个好素数 \(p\) 以指数零加入 局部集并宣布其为非活跃的，则所得 分支具有相同的 \(c_F,c,d,\vartheta,\kappa_F\)，在每个 其他活跃素数处的数据相同，并与 \(p\) 缺席的分支具有相同的核。 其标量乘以 \(1-q_p^{-1}\)。 这种相容性包括每个 \(h_0\)，而不只是模 \(L\) 的单位类。

*变换后检验函数的界。* 对 \(A\ge0\) 及整数 \(B\ge0\)，置 \[\mathfrak M_{A,B}(V)=
 \sup_{-A\le\eta\le1/4}\int_{\mathbb R}
       (1+|u|)^B|\widehat V(\eta+iu)|\,du.\] 对每个整数 \(j\ge0\)， \[\label{eq:reflection-kernel}
 |(x\partial_x)^jV^\sharp(x)|
 \ll_{A,j}\min\{x^{1/4},(1+x)^{-A}\}
       \mathfrak M_{A,\lceil4A\rceil+j+2}(V).\] 若 \(\chi\in C_c^\infty(0,\infty)\) 固定，\(Y>0\)，且 \(J\ge0\) 为 整数，则 \[\label{eq:reflection-annular-fourier}
 \int_{\mathbb R}(1+|u|)^J
 \left|\int_0^\infty\chi(y)V^\sharp(Yy)y^{-iu}\frac{dy}{y}\right|du
 \ll_{A,J,\chi}\min\{Y^{1/4},(1+Y)^{-A}\}
       \mathfrak M_{A,\lceil4A\rceil+J+4}(V).\] 这些都是有限光滑半范数。 更精确地， \[\label{eq:reflection-test-seminorm}
 \mathfrak M_{A,B}(V)\ll_{A,B}
 \int_0^\infty(1+x^{-A}+x^{1/4})
       \bigl(|V(x)|+|(x\partial_x)^{B+2}V(x)|\bigr)\frac{dx}{x}.\] 把 \(V(x)\) 换成 \(x^{iu_0}V(x)\) 至多使 \(\mathfrak M_{A,B}\) 乘以 \((1+|u_0|)^B\)。

我们首先通过有限多个平移后的 theta 值来表达特征掩码。 随后变换它们的有理尖点，并计算所得的自守因子与局部 Fourier 因子；最后的 Mellin 比较给出反射恒等式 及其变换后检验函数的界。

*固定的 theta 输入。* 设 \(\Gamma=\mathrm{SL}_2(\mathcal O)\)， \(\Gamma_1(3)=\{g\in\Gamma:g\equiv I\pmod3\}\)，且 \(\Gamma_2=\langle\mathrm{SL}_2(\mathbb Z),\Gamma_1(3)\rangle\)。  中无条件成立的公式给出 \(\mathbb H^3=\mathbb C\times\mathbb R_{>0}\) 上的光滑三次 theta 函数 \(\theta\)，满足 \[\theta(gw)=\kappa(g)\theta(w)\quad(g\in\Gamma_2),\qquad
 \kappa\!\begin{pmatrix}a&b\\c&\delta'\end{pmatrix}
   =\left(\frac ca\right)_3\quad
   \left(\begin{pmatrix}a&b\\c&\delta'\end{pmatrix}\in\Gamma_1(3),\ c\ne0\right).\] 这里 \(\kappa\) 在 \(\mathrm{SL}_2(\mathbb Z)\) 上为一，且在 \(\Gamma_1(3)\) 中 左下元素为零的元素上为一。 下标 \(3\) 表示通常的三次剩余符号；对好素数 \(p\notin S\)， 有 \((x/p)_3=\chi_p(x)^2\)。 这些自守与系数公式不假设任何关于 \(L\) 函数零点的 条件。

置 \[\mathsf L(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix},\qquad
 (t_0,t_1,t_2)=(0,\omega^2,\omega),\qquad
 \Theta_b(w)=\theta(\mathsf L(t_b)w).\] 若 \(v\in\mathbb Z+3\mathcal O\)，则 \(\mathsf L(v)\) 是 \(\mathrm{SL}_2(\mathbb Z)\) 的一个元素与 \(\Gamma_1(3)\) 中一个自守因子为一的下平移之积。 对 上平移有类似断言成立。 因此 \[\theta(\mathsf L(\lambda)w)=\Theta_1(w),\qquad
 \theta(\mathsf L(-\lambda)w)=\Theta_2(w),\] 因为 \(\lambda-\omega^2=2+3\omega\) 且 \(-\lambda-\omega=-1-3\omega\)。 若 \(u_0=s+t\omega\)，其中 \(0\le s,t<3\)，且 \(E=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\)， 则 \[\begin{pmatrix}u_0&-1\\1&0\end{pmatrix}=E\mathsf L(-u_0),
 \qquad -u_0-t_t\in\mathbb Z+3\mathcal O,\] 从而 \(\theta\bigl(\bigl(\begin{smallmatrix}u_0&-1\\1&0\end{smallmatrix}\bigr)w\bigr)
=\Theta_t(w)\)。 这些是下文所需的仅有的尖点代表元。

对其中任一个，由 \[\label{eq:reflection-cusp-expansion}
 \bar\theta(H(z,v))=C_H(v)+
 \sum_{\mu\ne0}d_H(\mu)vK_{1/3}(4\pi|\mu|v)\check e(\mu z).\] 定义 \(d_H\)。 这里 \(C_H(v)\) 与 \(z\) 无关。 三个函数 \(\Theta_0,\Theta_1,\Theta_2\) 分别是   中的 \(F_1,F_{19},F_{10}\)。 其附录 A 的第 \(1,19,10\) 行 用其方程 (5.7)、(5.13) 与 (5.14) 中的 \(\tau,\tau_1,\tau_2\) 表达它们的系数。 在其记号中，共轭 展开使用 \(\overline{d_j(-\mu)}\)，如它们的方程 (5.16)。 那些公式给出 方程 [\[old-eq:4.3\]](#old-eq:4.3) 中的支撑包含。 为完整起见，\(\tau\) 在 \(\mu=u\lambda^k n b^3\) 处可能的两个大小为 \[3^{k/6+8/3}|b|\quad\hbox{and}\quad3^{k/6+3}|b|,\] 而 \(\tau_1,\tau_2\) 的大小为 \(9|b|\) 且 \(k=-4\)。 这里 Gauss 和仅使用三次符号，包括在 \(S\) 中的素数处。 为明确其定义域，对每个主无平方因子 \(n\)，如   中那样定义 \[\label{eq:reflection-cubic-source-gauss}
 \widetilde g_3(n)=q_n^{-1/2}\sum_{v\bmod n}
       \left(\frac vn\right)_3\check e(v/n),
 \qquad \widetilde g_3(1)=1.\] 通常的三次符号在除 \(\lambda\) 外的每个素数处有定义， 在非单位上取值为零，并在分母中按乘性延拓。 每个主 \(n\) 都与 \(\lambda\) 互素。 在 \(n\) 的每个素因子处 三次特征非平凡，且 \(\check e(v/n)=e(\lambda v/n)\) 是本原的， 因为 \(\lambda\) 在那里是单位。 因此有限域 Gauss 恒等式与 中国剩余定理给出 \(|\widetilde g_3(n)|=1\)，对每个 这样的无平方因子 \(n\) 成立。 这包括范数为 \(4\) 的主素数 \(-2\)； 不使用以该数为分母的六次特征。 又，只要 \((t,n)=1\)， 变量替换 \(y=tv\) 给出 \[q_n^{-1/2}\sum_{v\bmod n}\left(\frac vn\right)_3\check e(tv/n)
       =\left(\frac tn\right)_3^{-1}\widetilde g_3(n).\] 这涵盖了其他源系数族中的扭曲 \(t=\lambda^2,\omega\lambda^2,\omega^2\lambda^2\)。 于是所有三个尖点族中出现的未正规化 Gauss 和 其大小均为 \(|n|\)。 从而 上面展示的每个系数大小至多为 \(27\,3^{k/6}|b|\)，包括 \(k=-4\)。 这些公式只要求 \(n\) 无平方因子且 \(n,b\) 为主；它们不要求 \((n,b)=1\)。 \(nb^3\) 的素赋值还表明它由这样的 \(n,b\) 的表示（当存在时）是唯一的。 特别地，当 这些变量有公共素数或含有被排除在素数求和之外的素数时，同样的界 仍然成立。

在无穷远处，条件 \(x=\lambda^3\mu\equiv1\pmod3\) 恰好分离出 \(\mu=\lambda^{-3}nb^3\)，其中 \(n,b\) 为主且 \(n\) 无平方因子。 无穷远处的支撑有 \(\lambda^3\mu\in\mathcal O\)；  方程 (5.7) 中其他每个分歧 指数都使 \(x\) 被 \(\lambda\) 整除，而剩余 一对中的负号给出 \(x\equiv-1\pmod3\)。 在被分离出的指标处，\(\bar\theta\) 中的系数为 \[\label{eq:reflection-infinity-coefficient}
 d_I(\lambda^{-3}nb^3)=3^{5/2}|b|\widetilde g_3(n).\] 这是未加掩码的源公式，对每个主无平方因子 \(n\) 与每个主 \(b\) 成立，它们之间没有互素条件。 仅当 \((n,S)=1\) 时，它才可以用整体六次记号表达：在 \(\gamma_2(n)\) 中作替换 \(y=\lambda v\) 给出 \[\label{eq:reflection-cubic-sextic-conversion}
 \widetilde g_3(n)=\left(\frac\lambda n\right)_3^{-1}\gamma_2(n)
       =\chi_n(\lambda)^{-2}\gamma_2(n)\qquad((n,S)=1).\]   中的三次补充律使 \((\lambda/x)_3\) 在所有主 \(x\) 上模 \(9\) 周期。 在与 \(S\) 互素的 主元素上它等于 \(\chi_x(\lambda)^2\)。 \(\mathcal X\) 中的特征在与 \(\mathfrak E\) 互素的主元素上模其导子周期，而 零条件 \((x,\mathfrak E)\ne1\) 模 \(\mathfrak E\) 周期。 因此一个具有素支撑 \(S\) 的充分可整除的 \(L\) 对 固定有限族的每个成员都适用。 这在选择移动局部素数 之前验证了它的选取。

*带零延拓的有限 Fourier 反演。* 对 \(j\in\{0,\ldots,5\}\) 定义 \[C_{p,j}(h)=q_p^{-1}\sum_{x\bmod p}\chi_p(x)^j e(-hx/p).\] 由 \(e\) 给出的特征配对在 \(\mathcal O/(p)\) 上非退化。 在 Gauss 和中作变量替换，并利用 非平凡乘性特征的正交性，给出 \[\label{eq:reflection-local-fourier}
 C_{p,j}(h)=\begin{cases}
 q_p^{-1/2}\tau_{p,j}^{-}\chi_p(h)^{-j},&j\ne0,\ h\ne0,\\
 0,&j\ne0,\ h=0,\\
 -q_p^{-1},&j=0,\ h\ne0,\\
 1-q_p^{-1},&j=0,\ h=0.
 \end{cases}\] 这里及下文 \(h=0\) 表示 \(h\equiv0\pmod p\)。 \(\chi_p\) 的每个非平凡幂 在素数 \(p\) 处都是本原的，因此通常的有限域 Gauss 和恒等式给出 \(|\tau_{p,m}^{\pm}|=1\)。

\(\mathcal O/(L)\) 上及每个 \(\mathcal O/(p)\) 上的 Fourier 反演现在给出 \[\phi(x)\prod_p\chi_p(x)^{j_p}
  =\sum_h C(h)e\!\left(x\left(h_0/L+\sum_p h_p/p\right)\right),
 \qquad C(h)=\widehat\phi(h_0)\prod_pC_{p,j_p}(h_p).\] 这用到了每个加性频率，包括非单位 \(h_0\) 与零局部 频率。 我们不引用  中的扭曲公式，其单位 Fourier 支撑假设 对这些掩码未必成立。 以其无穷远系数 \(x=\lambda^3\mu\in\mathcal O\) 上带有该自守因子的 theta 函数是有限和 \[\label{eq:reflection-translated-theta}
 \mathcal F(z,v)=\sum_hC(h)\bar\theta(z+z_h,v),\qquad
 z_h=\lambda^2\left(h_0/L+\sum_p h_p/p\right).\] 对孤立的无穷远指标 \(x=nb^3\)，\(\phi\) 的分段定义 首先丢弃每个满足 \((nb,\mathfrak E)\ne1\) 的项。 这是 在整个完备化指标上的掩码：\((nb^3,\mathfrak E)=1\) 当且仅当 \(n\) 与 \(b\) 都是 \(\mathfrak E\)-单位。 仅在这个剩余的域上，我们才使用 完全乘性，包括 \(\chi_b(\lambda)^6=1\)，写出 \[\phi(nb^3)\prod_p\chi_p(nb^3)^{j_p}
 =\chi_n(\lambda)^2\Psi(n)\Psi(b)^3
 \qquad((nb,\mathfrak E)=1).\] 当 \(n,b\) 有公共移动素数时它仍然成立，因为相应的 局部幂保持其零值，包括 \(j_p=0\) 的情形。 对于 被丢弃的项，完备化系数直接定义为零； 那里不计算 \(\chi_n(\lambda)\) 的任何值。 在保留域上 结合方程 [\[eq:reflection-infinity-coefficient\]](#eq:reflection-infinity-coefficient) 与 [\[eq:reflection-cubic-sextic-conversion\]](#eq:reflection-cubic-sextic-conversion)，现在 把直接的 Mellin 级数与乘积 \(T\) 等同起来。 对偶系数 函数 \(d_H\) 保持方程 [\[old-eq:4.3\]](#old-eq:4.3) 中的完整源支撑； 不在它们上面放置 \(S\)-掩码。

固定 \(h_0\)，并恰在 \(h_p\ne0\) 时称 \(p\) 为活跃的。 方程 [\[eq:reflection-local-fourier\]](#eq:reflection-local-fourier) 迫使所有 \(j_p\ne0\) 的 素数都是活跃的。 对每个 \(h_0\bmod L\) 选取一次 代表元及既约表达式 \(\lambda^2h_0/L=a_F/c_F\)。 把分子与分母乘以 一个单位，当 \(\lambda\mid c_F\) 时把分子正规化为 \(1\pmod3\)， 否则把分母正规化为 \(1\pmod3\)。 由于每个活跃 素数都是主的，该单位仅依赖于 \(h_0\)。 对 \(r=\prod_{p\ {\rm active}}p\)，方程 [\[eq:reflection-translated-theta\]](#eq:reflection-translated-theta) 随后给出 \[\label{eq:reflection-cusp-fraction}
 z_h=\frac ac,\qquad c=c_Fr,\qquad
 a=a_Fr+\lambda^2c_F\sum_{p\mid r}(r/p)h_p.\] 在整除 \(c_F\) 的素数处，分子同余于 \(a_Fr\) 且 是单位。 在 \(p\mid r\) 处，它同余于 \(\lambda^2c_F(r/p)h_p\)，同样是单位。 因此这个分数是 既约的，即使 \(h_0\) 模 \(L\) 是非单位。 允许空乘积 \(r=1\)。 把任一提升换成另一个会使 \(z_h\) 改变 \(\lambda^2\mathcal O=3\mathcal O\) 中的一个元素，即 \(\theta\) 的一个周期。

*尖点矩阵及其自守因子的选取。* 接下来的构造对刚得到的每个既约尖点分数确定 自守因子与反射加性相位。 置 \(M=\lambda^{12}L^4\)。 对每个活跃的 \(p\)，中国剩余 定理容许把所选的非零类 \(h_p\bmod p\) 提升为满足 \(h_p\equiv0\pmod{M^2}\)。 把 \(r\) 限制到模 \(M^2\) 的一个类。 方程 [\[eq:reflection-cusp-fraction\]](#eq:reflection-cusp-fraction) 表明 \(a\) 此时模 \(Mc_F\) 固定； 事实上其移动项被 \(M^2c_F\) 整除，而 \(a_Fr\) 模 \(M^2\) 固定， 且由于 \(c_F\) 在相差一个单位的意义下整除 \(L\)，\(M^2\) 被 \(Mc_F\) 整除。 它还表明，当 \(\lambda\mid c\) 时 \(a\equiv1\pmod3\)，否则 \(c\equiv1\pmod3\)。

由以下相容的局部同余选取 \(\delta'\)： \[\begin{array}{ll}
 \delta'\equiv a^{-1}\pmod{Mc_F}
       &\text{在整除 }c_F\text{ 的每个素数处},\\
 \delta'\equiv0\pmod M
       &\text{在整除 }M\text{ 但不整除 }c_F\text{ 的每个素数处},\\
 \delta'\equiv a^{-1}\pmod p& (p\mid r).
 \end{array}\] 第一行指 \(Mc_F\) 的所示素幂部分。 所有逆都存在，因为 \(a/c\) 既约。 置 \(b=(a\delta'-1)/c\) 及 \(g=\bigl(\begin{smallmatrix}a&b\\c&\delta'\end{smallmatrix}\bigr)\)。 则 \(g\in\Gamma\)，且用 \(c\) 除 \(a\delta'-1\) 给出 \[b\equiv0\pmod M\text{ 在 }c_F\text{ 的素数处},\qquad
 b\equiv-c^{-1}\pmod M\text{ 在 }M\text{ 的其他素数处}.\] 于是 \(a,b,c,\delta'\) 在整除 \(L\) 的每个素数的所需幂处 有固定剩余，与类 \(h_p\) 无关。 每当在剩余符号计算中出现零元素时， 可以先把 \(z_h\) 平移 \(\lambda^2M^2\mathcal O\)，然后 给 \(\delta'\) 加上组合同余模的一个倍数。 这些改变保持所有展示的同余，并避开使 某个元素为零的有限多个取值。 它们不改变平移后的 theta 函数。

有三种情形，由 \(v_\lambda(c)\) 区分。 若 \(3\mid c\)，置 \(H=I\)。 则 \(G=g\in\Gamma_1(3)\)，而对主 \(a\) 与 \(r\) 的主素数应用三次 互反律给出 \[\label{eq:reflection-cusp-case-zero}
 \kappa(G)=\left(\frac{c_F}{a}\right)_3
             \left(\frac ar\right)_3.\] 若 \(v_\lambda(c)=1\)，取唯一的 \(u_0\in\{\lambda,-\lambda\}\) 使 \(u_0\equiv c\pmod3\)，并置 \(H=\mathsf L(u_0)\)；由于 \(\mathcal O/(\lambda)\simeq\mathbb F_3\)，这就是两种可能。 上面的同余表明 \(G=gH^{-1}\in\Gamma_1(3)\)。 记 \(A=a-u_0b\)。 \(A\) 与 \(a\) 都是主的，且它们互素： \((a,b)=1\) 且 \((a,u_0)=1\)。 行列式方程给出 \[a(c-u_0\delta')=cA-u_0,
 \qquad bc\equiv-1\pmod a.\] 由此，对 \(a,A\) 应用三次互反律，得到 \[\begin{split}
 \kappa(G)
 &=\left(\frac{-u_0}{A}\right)_3
          \left(\frac aA\right)_3^{-1}\\
 &=\left(\frac{-u_0}{A}\right)_3
          \left(\frac{c/u_0}{a}\right)_3
  =\left(\frac{-u_0}{A}\right)_3
          \left(\frac{c_F/u_0}{a}\right)_3
          \left(\frac ar\right)_3.
 \end{split}\] 对第二个等式，把 \(A\) 模 \(a\) 约化并使用 \((A/a)_3=(-u_0b/a)_3=(u_0/a)_3(c/a)_3^{-1}\)；\(-1\) 的三次符号 为一。 最后设 \((\lambda,c)=1\)。 选取 \(u_0=s+t\omega\equiv a\pmod3\) 且 \(0\le s,t<3\)，并置 \(H=\bigl(\begin{smallmatrix}u_0&-1\\1&0\end{smallmatrix}\bigr)\)。 这里 \(c\equiv1\)、\(\delta'\equiv0\) 且 \(b\equiv-1\pmod3\)，所以 \[G=gH^{-1}=\begin{pmatrix}-b&a+bu_0\\-\delta'&c+\delta'u_0\end{pmatrix}
       \in\Gamma_1(3).\] \(-b\) 与 \(c\) 都是主的。 此外 \(-bc=1-a\delta'\equiv1\pmod9\)。 把 \(\delta'=u\lambda^k\delta_0\) 分解，其中 \(\delta_0\) 为主。 补充律给出 \((u\lambda^k/(1-a\delta'))_3=1\)；三次 互反律给出 \((\delta_0/(1-a\delta'))_3=1\)，因为互反后 分子为 \(1\pmod{\delta_0}\)。 于是 \[\left(\frac{\delta'}{-bc}\right)_3=1,
 \qquad
 \kappa(G)=\left(\frac{\delta'}{-b}\right)_3
          =\left(\frac{\delta'}c\right)_3^{-1}
          =\left(\frac ac\right)_3
          =\left(\frac a{c_F}\right)_3\left(\frac ar\right)_3.\] 最后一个逆使用了 \(a\delta'\equiv1\pmod c\)。

在三种情形中我们都证明了 \[\label{eq:reflection-multiplier}
 \kappa(G)=\kappa_F\prod_{p\mid r}\chi_p(a)^2,
 \qquad |\kappa_F|=1.\] 当活跃的 \(h_p\) 在固定扇区内变动时，因子 \(\kappa_F\) 保持不变。 若 \(3\mid c\)，它为 \((c_F/a)_3\)：单位与 \(\lambda\)-幂因子由 \(a\bmod9\) 确定，而互反律 由 \(a\) 在 \(c_F\) 的素数处的剩余确定其余的固定素数因子。 在中间情形中它为 \((-u_0/A)_3((c_F/u_0)/a)_3\)，由 \(A=a-u_0b\) 与 \(a\) 的固定 剩余以同样的方式确定。 在最后一种情形中它为 \((a/c_F)_3\)， 直接由固定的分母 \(c_F\) 与 \(a\bmod c_F\) 确定。 因此 \(a,b,c,\delta'\) 所展示的同余 仅用 \(h_0\) 与 \(r\bmod M^2\) 就确定了 \(\kappa_F\)。 它们也确定了三个函数 \(\Theta_b\) 中被选中的那一个。

*反射加性相位。* 记 \(x=\lambda^4\mu\) 及 \(D_F=\lambda^3c_F\)。 在每个 \(p\mid r\) 处， 方程 [\[eq:reflection-cusp-fraction\]](#eq:reflection-cusp-fraction) 给出 \(a\equiv\sigma_ph_p\pmod p\)。 因此 \(\delta'\equiv\sigma_p^{-1}h_p^{-1}\pmod p\)。 对 \(D_Fr\) 的互素因子作加性中国剩余给出精确恒等式 \[\label{eq:reflection-additive-phase}
 \begin{split}
 \check e(-\delta'\mu/c)
 &=e(-\delta'x/(D_Fr))\\
 &=\vartheta(x)\prod_{p\mid r}e(\epsilon_ph_p^{-1}x/p),
 \qquad
 \vartheta(x)=e(-\delta'_F r^{-1}x/D_F).
 \end{split}\] 这里 \(\delta'_F\) 是 \(\delta'\) 模 \(D_F\) 的类，而 \(\vartheta\) 的公式中的 \(r^{-1}\) 模 \(D_F\) 取值。 例如，\(p\) 处的局部分子为 \(-\delta'(D_Fr/p)^{-1}=\epsilon_ph_p^{-1}\)；这验证了符号 与 \(\lambda\) 的幂次。 所选的同余固定了 \(\delta'_F\)， 因为 \(D_F\) 整除相应的局部模，而扇区固定了 \(r^{-1}\bmod D_F\)。 因此有限多个 \(D_F\) 的一个公倍数 是所有特征 \(\vartheta\) 的固定模。

对式 [\[eq:reflection-multiplier\]](#eq:reflection-multiplier) 取共轭贡献 \(\bar\kappa_F\prod_{p\mid r}\chi_p(\sigma_p)^{-2}\chi_p(h_p)^{-2}\)。 对 \(j\ne0\)，乘以 式 [\[eq:reflection-local-fourier\]](#eq:reflection-local-fourier) 使局部和变为 \[q_p^{-1/2}\tau_{p,j}^{-}
 \sum_{h\ne0}\chi_p(h)^{-j-2}e(\epsilon_ph^{-1}x/p).\] 置 \(y=h^{-1}\) 后，该和是次数为 \(j+2\) 的 Gauss 和。 若 \(j\ne4\)，其值为 \(q_p^{1/2}\tau_{p,j+2}^{+}\chi_p(\epsilon_px)^{-j-2}\)，在 \(p\mid x\) 处也如此，因为那时两边都为零。 若 \(j=4\)，它是 Ramanujan 和 \[\sum_{y\ne0}e(\epsilon_pxy/p)=-1+q_p1_{p\mid x}.\] 对活跃的 \(j=0\)，同样的替换给出 \[-q_p^{-1}\sum_{h\ne0}\chi_p(h)^{-2}e(\epsilon_ph^{-1}x/p)
 =-q_p^{-1/2}\tau_{p,2}^{+}\chi_p(\epsilon_px)^{-2}.\] 这些恰好是 \(\omega_{p,j}B_p(x)\)；非活跃的零指数 贡献 \(1-q_p^{-1}\)。 这证明了每个局部因子，包括 其零延拓。 \(h_0\) 与活跃子集的选择至多给出 \(q_L2^{\#\{p:j_p=0\}}\) 项。 拆分 \(j_p=4\) 的因子 至多把它乘以 \(2^{\#\{p:j_p=4\}}\)，从而证明了所述的 计数。

在这些局部和之前构造的分母与固定扇区数据 仅通过 \(h_0\) 与活跃根基 \(r\) 依赖于局部素数集；其余活跃频率依赖恰为刚求和 的局部依赖。 我们对每个 \(h_0\) 使用相同的代表元 与正规化分数，并在这些数据重现时使用相同的固定扇区选择： 尖点函数、固定加性特征与 \(\kappa_F\)。 一个缺席素数 与非活跃的零指数素数具有相同的活跃根基； 因此它们其余活跃的 \(\sigma_p,\epsilon_p\) 也相同。 非活跃系数 \(1-q_p^{-1}\) 是唯一的改变。 这证明了陈述中的同时分支相容性。

节 [3.2](#par:reflection-marks) 中的带标记反射将用到下列关于活跃素数对的依赖关系。由于 \[\epsilon_p=-\lambda^{-5}(c/p)^{-2}\pmod p,\] 存在一个绝对值为 1 的标量 \(\xi_{p,j}\)，它依赖于 \(p,j\)，但不依赖于任何其他活跃素数，使得 \[\label{eq:reflection-cross-prime-phase}
 \chi_p(\sigma_p)^{-2}\omega_{p,j}
       =\xi_{p,j}\chi_p(c/p)^{2j+2}.\] 对 \(j=4\)，这用到了 \(2j+2\equiv-2\pmod6\)；对其他指数，代入 \(\epsilon_p\) 的表达式即得。 于是另一个活跃素数对 \(p\) 处相位的贡献，其指数模六恰为 \(2j+2\)。特别地，活跃指数 \(j=1\) 具有列耦合 \(\chi_p(x)^{-3}=\chi_p(x)^3\)。

*Mellin 正规化与延拓。* 令 \[J(s)=\int_0^\infty
       \left.\partial_{\bar z}\mathcal F(z,v)\right|_{z=0}
       v^{2s-1}\,dv.\]  中用到的 Bessel 恒等式为 \[\int_0^\infty K_{1/3}(y)y^{w-1}\,dy
  =2^{w-2}\Gamma((w-1/3)/2)\Gamma((w+1/3)/2)
       \qquad(\Re w>1/3).\] 在 \(\Re s>1\) 上系数和绝对收敛，因此我们可以逐项求导并逐项积分它们的展开式。 由于 \(\partial_{\bar z}\check e(\mu z)=2\pi i\bar\mu\check e(\mu z)\)， 取 \(w=2s+1\) 的恒等式给出 \[J(s)=\frac i4(2\pi)^{-2s}\Gamma(s+1/3)\Gamma(s+2/3)
       \sum_{0\ne\mu\in\lambda^{-3}\mathcal O}d_I(\mu)\phi(\lambda^3\mu)
          \prod_p\chi_p(\lambda^3\mu)^{j_p}
          \bar\alpha(\mu)q_\mu^{-s}.\] 首先如上所述用整指标掩码把范围限制到 \((nb,\mathfrak E)=1\)， 再代入方程 [\[eq:reflection-infinity-coefficient\]](#eq:reflection-infinity-coefficient) 与 [\[eq:reflection-cubic-sextic-conversion\]](#eq:reflection-cubic-sextic-conversion)。利用 \(q_{\lambda^{-3}}=27^{-1}\) 与 \(\bar\alpha(\lambda^{-3})=-i\) 得到 \[\label{eq:reflection-direct-mellin}
 J(s)=\frac{3^{5/2}}4\left(\frac{27}{(2\pi)^2}\right)^s
       \Gamma(s+1/3)\Gamma(s+2/3)T(s,\Psi).\]

对于一个平移项 \(z_h=a/c\)，使用上面构造的矩阵 \(g=GH\)。由 ，\(g^{-1}\) 在双曲空间上的坐标作用给出 \[g^{-1}(z+a/c,v)=
 \left(-\frac{\delta'}c-\frac{\bar z}{c^2(v^2+|z|^2)},
               \frac{v}{q_c(v^2+|z|^2)}\right).\] 在 \(z=0\) 处，其第一个坐标关于 \(\bar z\) 的导数为 \(-(cv)^{-2}\)；其共轭坐标 与竖直坐标关于 \(\bar z\) 的导数均为零。 因此链式法则与 \(\bar\theta(gw)=\bar\kappa(G)\bar\theta(Hw)\) 给出 \[\left.\partial_{\bar z}\bar\theta(z+a/c,v)\right|_{z=0}
 =-\frac{\bar\kappa(G)}{c^2v^2}
   \left.\partial_z\bar\theta(H(z,1/(q_cv)))\right|_{z=-\delta'/c}.\] 特别地，该导数从方程 [\[eq:reflection-cusp-expansion\]](#eq:reflection-cusp-expansion) 中的每个尖点展开里消去了 \(C_H(v)\)。 代入该展开式，再在积分中作 \(v\mapsto1/(q_cv)\)， 对 \(\Re s<0\) 给出贡献 \[\label{eq:reflection-reflected-mellin}
 \begin{split}
 -\frac i4(2\pi)^{2s-2}\bar\alpha(c)^2q_c^{1-2s}\bar\kappa(G)
 \prod_{\pm}\Gamma(3/2-s\pm1/6)\\
 {}
 \times\sum_{\mu\ne0}d_H(\mu)\alpha(\mu)
       \check e(-\delta'\mu/c)q_\mu^{-(1-s)}.
 \end{split}\] 为直接验证该标量，在应用 Bessel 积分之前， 因子为 \(-2\pi i c^{-2}q_c^{2-2s}\)，剩余的积分为 \(\int_0^\infty u^{2-2s}K_{1/3}(4\pi|\mu|u)\,du\)。 取 \(w=3-2s\) 的 Bessel 恒等式，连同 \(c^{-2}=\bar\alpha(c)^2/q_c\)，恰好给出所显示的式子。

我们在此对延拓与围道运算一并给出论证。 方程 [\[old-eq:4.3\]](#old-eq:4.3) 中的系数界蕴含 当 \(\Re(1-s)>1\) 时反射级数绝对收敛：各自的优函数为 \[\sum_n^{\rm sf}q_n^{-(1-\Re s)},\qquad
 \sum_b q_b^{1/2-3(1-\Re s)},\qquad
 \sum_{k\ge-4}3^{k(1/6-(1-\Re s))}.\] 每个都在该区域内收敛。固定支集对 \(|\mu|\) 有正的下界。 \(K_{1/3}\) 及其所有导数的指数衰减、 系数界以及直接展开式蕴含，每个平移导数的每一对数导数在 \(v\to\infty\) 时指数衰减。刚才得到的 链式法则公式同样蕴含在 \(v\to0\) 时的指数衰减，其中常数取决于 固定的平移项。现在对 \(\log v\) 反复分部积分表明，\(J\) 是整函数，且在每个固定带形域上其衰减快于 \(|\Im s|\) 的任意幂。

方程 [\[eq:reflection-direct-mellin\]](#eq:reflection-direct-mellin) 右端含倒数 gamma 函数，把 \(T\) 延拓为整函数。其 直接级数在 \(1\) 右侧的任何直线上有界。 方程 [\[eq:reflection-reflected-mellin\]](#eq:reflection-reflected-mellin) 与 Stirling 公式 给出 \(0\) 左侧任何直线上的多项式界；两个 gamma 乘积的指数 部分相消。在这样的直线之间的带形域上， \(J\) 的快速界与倒数 gamma 因子首先给出 \(|T(\sigma+it)|\ll (1+|t|)^C e^{\pi|t|}\)，其中 \(C\) 为某个常数。 用 \(B+s\) 的足够高次幂去除 \(T\)，其中 \(B\) 的选取使得 \(B+s\) 在该带形域上无零点，再乘以 \(e^{\varepsilon s^2}\)。 对每个 \(\varepsilon>0\)，一个不断扩大的矩形的两条水平边趋于零。最大模原理，随后令 \(\varepsilon\to0\)，把两条竖直边上的多项式界转移到该带形域上。这就证明了所述的多项式带形增长。

把方程 [\[eq:reflection\]](#eq:reflection) 左端的积分从 \(\Re s=a\) 移到 \(\Re s=1/2-\sigma<0\)，其中 \(\sigma>1/2\)。 整函数延拓、多项式带形界与快速的 Mellin 衰减 保证了这一移动：将方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 应用于 \(V\) 的 加权对数导数，使水平连接部分趋于零。代入 方程 [\[eq:reflection-reflected-mellin\]](#eq:reflection-reflected-mellin) 除以 方程 [\[eq:reflection-direct-mellin\]](#eq:reflection-direct-mellin) 的结果，并令 \(t=1/2-s\)， 给出 gamma 商 \(R(t)\) 与因子 \[-\frac i{81}\bar\alpha(c)^2q_\mu^{-1/2}
       \left(\frac{Kq_\mu X}{q_c^2}\right)^{-t}.\] 确实 \((2\pi)^{4s-2}27^{-s}3^{-5/2}
=3^{-4}K^{-t}\)，且 \(q_c^{1-2s}q_\mu^{s-1}
=q_\mu^{-1/2}(q_\mu/q_c^2)^{-t}\)。 反射系数级数在这条直线上 绝对收敛，因此可以与积分交换。利用方程 [\[eq:reflection-additive-phase\]](#eq:reflection-additive-phase) 与已算出的 Gauss 和对其有限的局部因子求和，即证明方程 [\[eq:reflection\]](#eq:reflection) 与 方程 [\[eq:reflection-row-phase\]](#eq:reflection-row-phase)。由于 \(|\phi|\le1\)，我们有 \(|\widehat\phi(h_0)|\le1\)；该标量中其余每个因子的 绝对值至多为 1。这就证明了 \(|\zeta|\le1/81\)。

*变换后测试函数的统一估计。* \(R(t)\) 分子的第一个负极点为 \(-5/6\)。 分母中倒数 gamma 函数是整函数。因此定义 \(V^\sharp\) 的 被积函数在 \(\Re t>-5/6\) 上全纯。 在 \(-1/4\le\sigma\le A\) 上，Stirling 公式给出 \[|R(\sigma+iu)|\ll_A(1+|u|)^{4\sigma}.\] 该估计对有界的 \(u\) 也一致，因为此闭带形域 没有分子极点。方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 使 \(\widehat V\) 在每个竖直带形域上逐点快速衰减。因此矩形 围道移动在 \(-1/4\le\Re t\le A\) 内有效， 包括在任意两条非负直线之间。作用 \((x\partial_x)^j\) 贡献 \((-t)^j\)。三条直线 \(-1/4,0,A\) 把所得积分分别界以 \[x^{1/4}\mathfrak M_{A,\lceil4A\rceil+j+2}(V),\quad
 \mathfrak M_{A,\lceil4A\rceil+j+2}(V),\quad
 x^{-A}\mathfrak M_{A,\lceil4A\rceil+j+2}(V).\] 的常数倍。把它们结合起来即证明方程 [\[eq:reflection-kernel\]](#eq:reflection-kernel)。 快速的大 \(x\) 界，在 \(A\) 任意大时，还使得当 \(V^\sharp\) 表示在零线上时，方程 [\[eq:reflection\]](#eq:reflection) 中的每个 对偶和绝对收敛。因此核围道的移动不需要对一个条件收敛的 Dirichlet 级数作逐项移动。

对于方程 [\[eq:reflection-annular-fourier\]](#eq:reflection-annular-fourier)，令 \(f_Y(v)=\chi(e^v)V^\sharp(Ye^v)\)。它的支集位于一个固定的紧 区间上。对其 Fourier 变换分部积分 \(J+2\) 次 并对 \(|u|\le1\) 使用平凡界，给出 \[\int_{\mathbb R}(1+|u|)^J|\widehat f_Y(u)|\,du
 \ll_J\sum_{j=0}^{J+2}\|f_Y^{(j)}\|_{L^1(\mathbb R)}.\] Leibniz 法则与方程 [\[eq:reflection-kernel\]](#eq:reflection-kernel) 把每个 范数界以方程 [\[eq:reflection-annular-fourier\]](#eq:reflection-annular-fourier) 的右端， 因为 \(e^v\) 始终位于 \((0,\infty)\) 的一个固定紧子区间内。 最后，对 \(|u|\ge1\)，分部积分 \(B+2\) 次给出 \[|\widehat V(\eta+iu)|
 \le |\eta+iu|^{-B-2}
       \int_0^\infty|(x\partial_x)^{B+2}V(x)|x^\eta\frac{dx}{x}.\] 对 \(|u|\le1\) 使用相应的未求导积分。 在 \(-A\le\eta\le1/4\) 上， \(x^\eta\le1+x^{-A}+x^{1/4}\)，这证明了 方程 [\[eq:reflection-test-seminorm\]](#eq:reflection-test-seminorm)。恒等式 \(\widehat{x^{iu_0}V}(\eta+iu)=\widehat V(\eta+i(u+u_0))\) 与 \(1+|u|\le(1+|u+u_0|)(1+|u_0|)\) 给出所述的范数扭转 界。特别地，Gaussian 测试函数 \(V(x)=(2\sqrt\pi)^{-1}\exp(- (\log x)^2/4)\)，其 Mellin 变换为 \(e^{t^2}\)，直接满足本命题的假设。

#### 元素行与固定扇区

为了把反射应用于特征 \(A\mapsto\chi_A(m)\)，我们把固定的补充相位与该行 的好素因子分离开来。这种分离在每个共享的好素数处保留了零点。

<span id="lem:reflection-row-sectors" label="lem:reflection-row-sectors">\[lem:reflection-row-sectors\]</span> 设 \(\Psi_{\rm base}\) 取遍一个固定的有限族，其元素为导子支集在 \(S\) 上的有限射线 特征，并在与 \(S\) 互素的主元素之外按零延拓。使用引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 中 对 \(\mathfrak l\in S\) 的固定生成元 \(\pi_{\mathfrak l}\)。 对 \(0\ne m\in\mathcal O\)，唯一地写为 \[m=u m_Sm_{\rm good},\qquad
 m_S=\prod_{\mathfrak l\in S}\pi_{\mathfrak l}^{v_{\mathfrak l}(m)},\qquad
 m_{\rm good}=\prod_{p\notin S}p^{v_p(m)},\] 其中好素数生成元是主的，\(u\) 是单位。对每个 与 \(S\) 互素的主元素 \(A\) 有 \[\label{eq:reflection-row-reduction}
 \chi_A(m)=\chi_A(u m_S)\mathcal R(A,m_{\rm good})
       \prod_{p\mid m_{\rm good}}\chi_p(A)^{v_p(m)}.\] 右端的所有幂都保留其零值，包括当 \(v_p(m)\equiv0\pmod6\) 时。固定 \(u\)、赋值 \(v_{\mathfrak l}(m)\) 模六， 以及 \(m_{\rm good}\) 在 \(\mathcal R\) 分解所通过的固定射线群中的类。 在这样的扇区中，定义 \[\label{eq:reflection-sector-character}
 \Psi_0^{[m]}(A)=
 \begin{cases}
 \Psi_{\rm base}(A)\chi_A(u m_S)\mathcal R(A,m_{\rm good}),
       &A\equiv1\pmod3,\ (A,S)=1,\\
 0,&\text{otherwise}.
 \end{cases}\] 非零分支属于一个固定的有限族，其元素为导子支集在 \(S\) 上的有限射线 特征。因此命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 中的单个 \(\mathfrak E,L\) 对这些扇区全部适用。局部素数集包含每个 \(p\mid m_{\rm good}\)， 其指数为 \(v_p(m)\) 模六，即使该指数为零时也是如此。 没有可移动的好素数被吸收进 \(L\)。

若 \((A,m_{\rm good})=1\)，乘性性与引理 [\[lem:fixed-gauss-phase\]](#lem:fixed-gauss-phase) 中的对称互反 因子给出方程 [\[eq:reflection-row-reduction\]](#eq:reflection-row-reduction)。若共享一个好素数， 则两端都为零：左端是 \(\chi_A(m)\) 的零延拓， 而右端的局部因子即使对六整除的指数也为零。 这就证明了该恒等式在所陈述的整个定义域上成立。

在此定义域上 \(\chi_A(u m_S)\) 仅依赖于 \(u\) 以及 \(S\)-赋值 模六，因为每个分子因子都是模 \(A\) 的单位。对 有限多个代表元 \(d=u\prod_{\mathfrak l\in S}\pi_{\mathfrak l}^{e_{\mathfrak l}}\)， \(0\le e_{\mathfrak l}<6\) 中的每一个，引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 都把 \(A\mapsto\chi_A(d)\) 等同于一个有限射线特征，其导子的支集 位于 \(6d\) 上方的素数处，且全部落在 \(S\) 中。一旦好射线类固定， \(A\mapsto\mathcal R(A,m_{\rm good})\) 便是支集在 \(2,3\) 上方素数处的 某个固定有限族特征之一。它们与基础特征的 有限族之积给出所述的固定族。取其导子与 \(S\)-掩码的 公倍数，即得公共的 \(\mathfrak E\)，进而得到 \(L\)。完备化系数中 额外的好的局部剩余符号因子被放入 \(\mathcal P\)，并在共享 素数处以相同的零约定合并；它们不改变此固定模。 该论证要求 \(m\ne0\)，并且对行 \(m=0\) 不作任何局部素数断言。

#### 公共剖面与格尾部

反射级数有一个依赖于其行的尺度。我们把这种 依赖保留在一个联合光滑剖面中，直到 Fourier 反演之后； 这给出整个行范数的一个系数测度。

<span id="lem:reflection-common-profile" label="lem:reflection-common-profile">\[lem:reflection-common-profile\]</span> 设 \(V\) 满足命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 的假设。 固定一个整数 \(d\ge1\)、一个紧集 \(\Omega\subset\mathbb R^d\)，以及 实指数 \(a_1,\ldots,a_d\)。设 \(W\) 是一个对数支集 在 \(\Omega\) 中的光滑剖面，对给定块中的所有行公共，并设 \(Y>0\) 在该块内 固定。令 \[h(\boldsymbol y)=\prod_{i=1}^d y_i^{a_i},\qquad
 F_Y(\boldsymbol y)=W(\boldsymbol y)V^\sharp(Yh(\boldsymbol y)),\qquad
 \mathfrak m_A(Y)=\min\{Y^{1/4},(1+Y)^{-A}\}.\] 对 \(A\ge0\) 与整数 \(j,J\ge0\)， \[\begin{aligned}
 p_j(F_Y)&\ll_{A,j,d,\Omega,\boldsymbol a}
 \mathfrak m_A(Y)p_j(W)
 \mathfrak M_{A,\lceil4A\rceil+j+2}(V),
 \label{eq:reflection-common-profile}\\
 \|F_Y\|_{J,\mathrm{sep}}&\ll_{A,J,d,\Omega,\boldsymbol a}
 \mathfrak m_A(Y)p_{J+d+2}(W)
 \mathfrak M_{A,\lceil4A\rceil+J+d+4}(V).
 \label{eq:reflection-common-measure}\end{aligned}\] 这里 \(p_j\) 是单个剖面的齐次半范数，而非一个多元组的 非齐次半范数。常数与 \(Y\) 无关，也与该块内 实际的范数标号无关。

在 \(W\) 的支集上，单项式 \(h\) 被仅依赖于 \(\Omega\) 与指数的 正常数从上、下界住。作用在 \(V^\sharp(Yh(\boldsymbol y))\) 上的每个 算子 \(y_i\partial_{y_i}\) 等于 \(a_i\) 乘以 \(V^\sharp\) 在 \(Yh(\boldsymbol y)\) 处的 Euler 导数。它不产生 \(Y\) 的额外幂次。Leibniz 法则与 方程 [\[eq:reflection-kernel\]](#eq:reflection-kernel) 证明 方程 [\[eq:reflection-common-profile\]](#eq:reflection-common-profile)。取 \(j=J+d+2\) 应用引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 给出 方程 [\[eq:reflection-common-measure\]](#eq:reflection-common-measure)。

以下是范数方面的推论，包括其运算次序。设 \(\mathcal I\) 为原来的行集，并假设一个行向量 \(\mathcal U\) 关于整个剖面 \(F_Y\) 是线性的。该剖面包含其行与列范数变量的 完整固定对数盒的截断。 假设同时进行的对数 Fourier 反演用对每行公共的一个密度 来表示该向量。在相关的算术 系数独立性被验证之后，写 \(F_Y=\mathfrak m_A(Y)\widetilde F_Y\)。Minkowski 给出 \[\label{eq:reflection-common-minkowski}
 \|\mathcal U\|_{\ell^2(\mathcal I)}
 \le \frac{\mathfrak m_A(Y)}{(2\pi)^d}
       \int_{\mathbb R^d}|\widehat{\widetilde F_Y}(\boldsymbol t)|
       \|B(\boldsymbol t)\|_{\ell^2(\mathcal I)}\,d\boldsymbol t.\] 这里 \(B(\boldsymbol t)\) 是分离后的行向量，其范数幂的 绝对值都为 1。此不等式背后的恒等式是 \(\ell^2(\mathcal I)\) 中的一个 Bochner 积分；只要分离后的范数具有所述的 多项式高度增长，上面的有限分离范数就确保其绝对可积性。对各行 分别选取的密度的统一界不会给出这一恒等式。 只有在该不等式右端的非负范数内部，行集才可在随后 被扩大，此时对新增的行使用 \(B\) 的同一分离公式。 对新增的行，不断言核的自变量与 \(Y\) 之间的任何比较。 把此不等式平方给出因子 \(\mathfrak m_A(Y)^2\)。若只使用小自变量界，则同一论证 容许更弱的标量 \(\min\{1,Y^{1/4}\}\)，其平方为 \(\min\{1,Y^{1/2}\}\)。正规化后的剖面具有有界的多元组半范数； 它们并不被断言为小量，因为该多元组半范数包含一个常数 1。已经展开的二次表达式中出现一次的核，反而只贡献 其标量一次，而不自动贡献其平方。

命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 中的 Gaussian 测试函数在那里 以及在引理 [\[lem:reflection-common-profile\]](#lem:reflection-common-profile) 中都直接可用：只有后一引理中的 联合因子 \(W\) 需要紧对数支集。若改为 对 Gaussian 本身应用紧支集演算， 引理 [\[lem:gaussian-annular\]](#lem:gaussian-annular) 提供所需的绝对可和 环形分解。

<span id="lem:lattice-kernel-tail" label="lem:lattice-kernel-tail">\[lem:lattice-kernel-tail\]</span> 设 \(\Lambda\) 为 \(\mathcal O\) 或 \(\lambda^{-4}\mathcal O\)。假设 \(K:(0,\infty)\to\mathbb C\) 对 \(x\ge1\) 满足 \(|K(x)|\le C_Ax^{-A}\)， 其中 \(A>1\)。则对 \(a>0\) 与 \(U\ge1\)， \[\label{eq:lattice-kernel-tail}
 \sum_{\substack{0\ne\mu\in\Lambda\\a q_\mu>U}}|K(aq_\mu)|
 \ll_A C_A(1+a^{-1})U^{1-A}.\] 对 \(K=V^\sharp\) 可取 \(C_A\ll_A\mathfrak M_{A,\lceil4A\rceil+2}(V)\)。

层 \(2^jU<a q_\mu\le2^{j+1}U\) 含有 \(O(1+2^jU/a)\) 个任一固定格的点。其贡献至多为 \(C_A(1+2^jU/a)(2^jU)^{-A}\)。对两个几何级数求和得到 \(O_A(C_A(U^{-A}+a^{-1}U^{1-A}))\)，由于 \(U\ge1\) 即蕴含所显示的式子。 最后的断言由方程 [\[eq:reflection-kernel\]](#eq:reflection-kernel) 得到。

#### 完备化指标的二次范数

下一个估计界住反射在一个无平方因子因子与一个立方之积上 所留下的二次特征。我们从引入的筛法开始。对于在 某个包含 \(6\) 上方素数的固定集合之外的 无平方因子主理想，二次核 \(\chi_a(b)^3\) 满足 \[\label{eq:quadratic-large-sieve}
 \sum_{\substack{a\ {\rm sf}\\q_a\le U}}
 \left|\sum_{\substack{b\ {\rm sf}\\q_b\le V}}
             c_b\chi_a(b)^3\right|^2
 \ll_\epsilon (UV)^\epsilon(U+V)\sum_b|c_b|^2.\] 这是 Goldmakher–Louvel 的二次大筛法 。为验证其族假设， 设 \(\vartheta_a((x))\) 表示在 \((x)\) 的主生成元处取值所得的二次剩余符号。把 \(x\) 调整到其主 生成元贡献 \(\varepsilon_\lambda(x)^{e(a)}\)，其中 \(\varepsilon_\lambda\) 是 模 \(\lambda\) 的非平凡特征，且 \(e(a)=(q_a-1)/2\bmod2\)。\(\omega\) 的幂不贡献任何东西， 因为它们是平方。因此 CRT 给出精确的本原导子 \(a\lambda^{e(a)}\) 与平凡的无穷型。我们使用本原的 诱导特征：所显示的 公式首先指定它在 \(\lambda\)-单位上的限制，而当 \(e(a)=0\) 时在 \(\lambda\) 处的因子不出现。这不改变 方程 [\[eq:quadratic-large-sieve\]](#eq:quadratic-large-sieve) 中任何指标上的取值。 在一个固定的模 \(4\) 主平方 类中，两个 指标具有相同的 \(e(a)\)；对这样的互素指标，本原 乘积的导子恰为它们之积。互反因子是 方程 [\[eq:reciprocity-four-class\]](#eq:reciprocity-four-class) 的固定双特征 \(\mathcal R\)。 这些正是所引定理的 族条件。有限射线划分与 转置对偶给出所显示取向下的方程 [\[eq:quadratic-large-sieve\]](#eq:quadratic-large-sieve)。

对行集的一个固定限制使正的外层和减小。 对系数支集的一个固定限制通过把 被省略的系数置零来实现。这两个观察都不容许一个任意 同时依赖于行与列的掩码。下一个归约 解决了由完备化指标的平方因子所产生的 碰撞掩码。

<span id="lem:completed-quadratic-reduction" label="lem:completed-quadratic-reduction">\[lem:completed-quadratic-reduction\]</span> 设 \(K,N,B\ge1\)。设 \(\mathcal I\) 为任意一族满足 \(q_k\ll K\) 的 无平方因子主好理想 \(k\)。设 \(n\) 取遍满足 \(q_n\asymp N\) 的无平方因子主理想， 并设 \(b\) 取遍满足 \(q_b\asymp B\) 的主理想。理想 \(n,b\) 可以包含 \(S\) 中除 \(\lambda\) 以外的素数。设 \(\beta(n,b)\) 为任意的、不依赖于 \(k\) 的复系数。 允许对 \(\mathcal I\) 的固定限制以及对 \((n,b)\)-支集的固定限制。

唯一地写 \(b=gt^2\)，其中 \(g\) 无平方因子，并令 \(c=(n,g)\)，\(n=cm\)，\(g=ch\)。于是 \(c,m,h\) 两两互素且 无平方因子。固定一组二进区间 \[q_c\asymp C,\qquad q_g\asymp G,\qquad q_t\asymp T,
 \qquad B\asymp GT^2,\] 其中所有比较常数都固定。设 \(\mathcal Q_{C,G,T}(\beta)\) 为在 \(k\in\mathcal I\) 上对（限制到该组区间的 \((n,b)\)-和的）绝对值平方求和， 其被加项为 \(\beta(n,b)\chi_k(nb)^3\)。对一个无平方因子的好理想 \(r\) 与固定的 \(t\)， 设 \(\mathcal D_r(t)\) 为三元组 \((c',m,h)\) 的集合，使得 \[c=rc',\qquad n=rc'm,\qquad b=rc'ht^2\] 属于原来的支集且属于这些区间，并满足所述的 \(c,m,h\) 的无平方因子性与两两互素性。则 \[\label{eq:completed-quadratic-reduction}
 \begin{split}
 \mathcal Q_{C,G,T}(\beta)
 \ll_\epsilon{}&(KNB)^\epsilon T
 \sum_{q_t\asymp T}\ 
 \sum_{\substack{r\ {\rm sf},\ (r,S)=1\\q_r\ll\min(K,C)}}
 \left(\frac K{q_r}+\frac{NG}{C^2}\right)\frac C{q_r}
 \sum_{(c',m,h)\in\mathcal D_r(t)}
       |\beta(rc'm,rc'ht^2)|^2.
 \end{split}\] 空商区间贡献为零；所有有界区间，包括 单位理想，都由固定的比较常数纳入。允许固定的射线 扇区与有界的行标量。特别地，若 \(|\beta(n,b)|\le1\)，则 \[\label{eq:completed-quadratic-norm}
 \sum_{k\in\mathcal I}
 \left|\sum_{n,b}\beta(n,b)\chi_k(nb)^3\right|^2
 \ll_\epsilon (KNB)^\epsilon(K+NB)NB.\] 常数可以依赖于固定支集的比较以及 \(S\)，但 对系数以及允许的支集限制是一致的。

分解式 \(b=gt^2\) 允许 \(g\) 与 \(t\) 共享素因子。由于 \(nb=c^2mht^2\)，零约定给出精确恒等式 \[\label{eq:completed-quadratic-zero-mask}
 \chi_k(nb)^3=\chi_k(mh)^3\,1_{(k,ct)=1}.\] 确实，一个平方在所显示的二次特征下具有六次幂； 它在单位上为 1，在碰撞处为零。因此该恒等式当 \(n\) 或 \(g\) 与 \(t\) 共享一个素因子时也成立。

对所选的区间有 \(O(T)\) 个可能的 \(t\)。Hilbert 空间 Cauchy 给出 \[\left\|\sum_{q_t\asymp T}F_t\right\|_2^2
 \ll T\sum_{q_t\asymp T}\|F_t\|_2^2.\] 在正的和中固定 \(t\)。条件 \((k,t)=1\) 现在是一个固定的行 限制。对剩下的条件使用完整恒等式 \[1_{(k,c)=1}=\sum_{r\mid(k,c)}\mu(r).\] 对每个 \(k\)，可能的 \(r\) 的个数至多为 \(d_{\mathcal O}(k)\)。 逐行 Cauchy 随后对 \(k\) 求和，代价为 \((KNB)^\epsilon\)， 并给出对固定的无平方因子好 \(r\) 的正和。写 \(k=rk'\) 与 \(c=rc'\)。无平方因子性给出固定的行限制 \((k',r)=1\) 与系数限制 \((c',r)=1\)；满足 \((r,t)>1\) 的项为零，否则 \((k',t)=1\) 是另一个固定的行限制。 在单个 \(r\)-被加项中不再有剩余的 \((k',c')\) 条件： 完整的碰撞掩码已被展开。一旦 \(r\) 固定，\(k\) 的固定射线扇区就成为 \(k'\) 的固定扇区。

因子 \(\chi_r(mh)^3\) 是一个有界的列因子。把 \(m,h\) 的支集在 \(S\) 上的无平方因子部分与其好部分分开： \(m=m_Sm_{\rm g}\) 与 \(h=h_Sh_{\rm g}\)。\(m_S,h_S\) 只有有限多种 选择。它们的符号是有界的行因子，而 \(j=m_{\rm g}h_{\rm g}\) 是无平方因子的好的，范数为 \(O(NG/C^2)\)。 对固定的 \(r,t,m_S,h_S\)，按 \(j\) 把剩余的列分组。若 \(C_j\) 为所得的系数，则二次大筛法给出 \[\sum_{k'}\left|\sum_j C_j\chi_{k'}(j)^3\right|^2
 \ll_\epsilon (KNB)^\epsilon
       \left(\frac K{q_r}+\frac{NG}{C^2}\right)\sum_j|C_j|^2.\] 外层的和可以保留其全部固定限制。在一个非空区间上， 最后所显示式中的两个商长度都被一个固定正常数从下界住； 把它们替换为各自与 1 的最大值只改变 比较常数。

对每个 \(j\)，分解为 \(m_{\rm g},h_{\rm g}\) 的方式数是 除数有界的。在其区间中有 \(O(C/q_r)\) 个可能的 \(c'\)。因此对这两种 选择作 Cauchy 给出 \[\sum_j|C_j|^2
 \ll_\epsilon (KNB)^\epsilon\frac C{q_r}
 \sum_{(c',m,h)\in\mathcal D_r(t)}
          |\beta(rc'm,rc'ht^2)|^2.\] 来自 \(\chi_r\) 的有界列因子仅在这个正和中被丢弃。 固定的坏部分符号是单位模的行因子， 并在应用筛法之前已从外层的模中移除。 这里的理想 \(m,h\) 是原来的理想， 由它们固定的 \(S\)-部分重构得到；\(c'\) 的 \(S\)-部分未受影响。 把各式结合即证明方程 [\[eq:completed-quadratic-reduction\]](#eq:completed-quadratic-reduction)。

现在假设 \(|\beta|\le1\)。理想计数给出 \[\#\mathcal D_r(t)\ll
       \frac C{q_r}\frac NC\frac GC.\] 对 \(q_r\asymp r_0\)，它与前一个因子 \(C/q_r\) 之积为 \(O(NG/r_0^2)\)。在此区间中有 \(O(r_0)\) 个可能的 \(r\) 与 \(O(T)\) 个 可能的 \(t\)。由于 \(B\asymp GT^2\)，它们对方程 [\[eq:completed-quadratic-reduction\]](#eq:completed-quadratic-reduction) 的贡献 至多为 \[(KNB)^\epsilon\frac{NB}{r_0}
       \left(\frac K{r_0}+\frac{NG}{C^2}\right)
 \ll (KNB)^\epsilon NB(K+NB).\] 这里 \(r_0,C,T\) 在一个非空区间上被从下界住，且 \(G\ll B\)。 \(C,G,T,r_0\) 的二进选择个数对范数区间是 对数的。在 \(C,G,T\) 块上作 Hilbert 空间三角不等式，随后对 \(\epsilon\) 重新标度，即证明方程 [\[eq:completed-quadratic-norm\]](#eq:completed-quadratic-norm)。

#### 无标记反射能量

对固定的有限射线特征 \(\nu\)——它在与 \(S\) 互素的主元素之外零延拓——以及 \(m\ne0\)，定义中心完备化和 \[\label{eq:unmarked-central-completion}
 \mathcal C_V(X;m,\nu)=
 \sum_{\substack{c\ {\rm sf},\ n\\c,n\equiv1\ (3)\\(cn,S)=1}}
 \frac{\gamma_2(c)\overline{\alpha(cn^3)}\nu(cn^3)\chi_{cn^3}(m)}
      {\sqrt{q_c}\,q_n}
 V\!\left(\frac{q_cq_n^3}{X}\right).\] 此处 \(c,n\) 可以共享素因子。当 \(V\) 满足命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 的假设时， 定义级数对每个 \(X>0\) 都绝对收敛。完备乘性（保留零点）给出 \(\chi_{cn^3}(m)=\chi_c(m)\chi_n(m)^3\)。于是对每个 \(a>1\)， \[\label{eq:unmarked-central-mellin}
 \mathcal C_V(X;m,\nu)=\frac1{2\pi i}\int_{(a)}
 \widehat V(s-1/2)X^{s-1/2}T(s,\nu\chi_\bullet(m))\,ds.\] 事实上，绝对收敛性允许在该线上逐项进行 Mellin 反演。

我们对这个完备化和在非零元素行上的均方进行估计。在完备范数尺度与行范数尺度相等时，目标是 \[\sum_{0<q_m\le C_mZ}|\mathcal C_V(Z;m,\nu)|^2
 \ll Z^{1+\epsilon}\mathfrak M_{A,J}(V)^2\] 对每个固定的 \(C_m\ge1\) 与 \(\epsilon>0\)，取适当有限阶 \(A,J\)。 下面的引理 [\[lem:unmarked-completed-moment\]](#lem:unmarked-completed-moment) 给出更一般的估计，它追踪行中重复的素因子。

二次筛法的原因对无平方因子行已经可见。取 \(m=R\) 为主元素、无平方因子且良好（good）， 满足 \(q_R\asymp Z\)，并令 \(X=Z\)。固定一个行扇区、一个尖点扇区、一个对偶单位 \(u\)， 以及对偶支撑中的一个整数 \(k\ge-4\)。此情形下没有冻结的良好局部素因子。 \(R\) 的每个素因子都以指数一进入反射，因此对 \(\mu=u\lambda^k n b^3\)，其列因子给出 \[\chi_R(\lambda^4\mu)^3
 =\chi_R(u\lambda^{k+4})^3\chi_R(nb)^3.\] 此恒等式保留所有零点，且 \(n,b\) 可以共享素因子。第一个因子只依赖于 \(R\)； 尖点系数与加性特征在整个扇区中相同。它们的系数界留下列正规化因子 \(q_n^{-1/2}q_b^{-1}\)， 至多相差一个依赖于固定 \(k\) 的常数。因此，行与两个列指标之间唯一的算术相互作用 是引理 [\[lem:completed-quadratic-reduction\]](#lem:completed-quadratic-reduction) 的核。

在对偶二进区间 \(q_n\asymp U\)、\(q_b\asymp B\) 上，反射核的变量与 \(UB^3/Z\) 相当。 它的快速衰减允许对任意固定 \(\tau>0\) 丢弃满足 \(UB^3>Z^{1+\tau}\) 的整块； 当分歧指数与其他参数变化时，下面的尾部论证使这一限制一致成立。 在保留的块上，引理 [\[lem:reflection-common-profile\]](#lem:reflection-common-profile) 用一个公共系数测度分离核， 同时保留实际的行环带。把反射和的这个二进片段记作 \(\mathcal U_{U,B,k}(R)\)。 对保留的块，二次范数与列正规化的平方给出 \[\sum_R|\mathcal U_{U,B,k}(R)|^2
 \ll_{V,k,\tau,\epsilon}Z^\epsilon
       \frac{(Z+UB)UB}{UB^2}
 =Z^\epsilon\frac{Z+UB}{B}
 \ll_{V,k,\tau,\epsilon}Z^{1+\tau+\epsilon}.\] 此处 \(B\ge1\) 与 \(UB^3\le Z^{1+\tau}\) 给出最后一个不等式。这解释了平衡能量尺度。 一般论证还须对分歧指数求和、在不等尺度下保留核的节省，并处理行中重复的素因子。 我们冻结行中指数至少为二的素数幂，并把同样的二次范数应用于其无平方因子剩余因子。 下面的定义记录由此产生的局部项；完备化行的引理随后对它们求和。

<span id="def:unmarked-reflected-block" label="def:unmarked-reflected-block">\[def:unmarked-reflected-block\]</span> 固定 \(Z\ge2\)、\(X=Z^N\)、命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 中的某个固定特征 \(\Psi_0\) 及其公共模 \(L\)，并令 \(M_{\rm ref}=\lambda^{12}L^4\)。对 \(R\) 上的当前范数，冻结有限个 良好素因子集合 \(\mathcal F\)，其指数为 \(j_p\in\{0,\ldots,5\}\)。令 \(R\) 取遍无平方因子的 主元素良好理想，它们与 \(\mathcal F\) 的每个素因子互素，落在模 \(M_{\rm ref}^2\) 的一个 固定同余类中，并可带有任何进一步的固定行限制。这些限制独立于对偶变量。 在与 \(S\) 互素的主元素上令 \[\Psi_R(A)=\Psi_0(A)\prod_{p\in\mathcal F}\chi_p(A)^{j_p}
                         \prod_{p\mid R}\chi_p(A).\] 每个局部幂都保留其零点。在对 \(\Psi_R\) 的反射中，固定 \(h_0\)、\(\mathcal F\) 中每个 \(j_p=0\) 素因子处的活跃或非活跃选择，以及每个 \(j_p=4\) Ramanujan 因子的两个被加项之一。 \(R\) 的所有素因子都是活跃的且指数为一。令 \(F_{\rm act}\) 为 \(\mathcal F\) 中活跃素因子的乘积。

对 \(j_p=4\) 处选定的每个整除性被加项，使用精确划分 \[1_{p\mid n_0b_0^3}=1_{p\mid n_0}+1_{p\nmid n_0}1_{p\mid b_0}.\] 选择一项。令 \(N_F\) 为分配给无平方因子理想 \(n_0\) 的素因子之积，令 \(B_F\) 为分配给 \(b_0\)（而非 \(n_0\)）的素因子之积。记 \(n_0=N_Fn\)、\(b_0=B_Fb\)。在第一种分配中只抽取 \(n_0\) 中的出现，即使 \(b_0\) 也含该素因子；在第二种中恰从 \(b_0\) 抽取一次出现。 所有其余的源限制都保留在 \(n,b\) 上。令 \(F_{\rm sm}\) 为小的 \(j_p=4\) 被加项与活跃的 \(j_p=0\) 素因子之积，并令 \[A_0=\log_Zq_{F_{\rm act}},\qquad S_0=\log_Zq_{F_{\rm sm}},\qquad
 N_0=\log_Zq_{N_F},\qquad B_0=\log_Zq_{B_F}.\] 空积的对数范数为零。

固定一个单位 \(u\)、一个整数 \(k\ge-4\)，以及对偶区间 \[\mu=u\lambda^kN_Fn(B_Fb)^3,\qquad
 q_n\asymp Z^v,\quad q_b\asymp Z^{\ell_b},\quad
 q_{\lambda^k}=Z^{e_\lambda},\] 其中 \(v,\ell_b\ge0\)。无平方因子的 \(n\) 与主元素 \(b\) 保留方程 [\[old-eq:4.3\]](#old-eq:4.3) 的 完整源支撑，包括 \(S\) 的允许素因子与共享素因子。令 \(H\ge0\)，并在一个固定紧对数盒上 选取公共光滑剖面 \(W_1(y_R,y_n,y_b)\)，其中 \[y_R=q_R/Z^H,\qquad y_n=q_n/Z^v,\qquad y_b=q_b/Z^{\ell_b}.\] 为这三个区间选取固定的光滑环带截断 \(\chi_{\rm row},\chi_n,\chi_b\)，并令 \[W_0(\boldsymbol y)=\chi_{\rm row}(y_R)\chi_n(y_n)\chi_b(y_b)W_1(\boldsymbol y).\] 支撑集与所引用的半范数在块上一致固定。把方程 [\[eq:reflection\]](#eq:reflection) 右端限制到该对偶 表示并乘以 \(W_0(y_R,y_n,y_b)\) 后的指定项记作 \(\mathcal U_{v,\ell_b,e_\lambda}(R)\)。 原始行集 \(\mathcal I_H\) 由满足 \(\chi_{\rm row}(q_R/Z^H)\ne0\) 的允许 \(R\) 组成。 上述每一个固定选择都单独作此定义。

此定义中的冻结素因子在每次使用时可以变化；它们不被加入固定的算术模 \(L\)。 该定义只在取 \(R\) 上的当前范数之前固定它们。

<span id="lem:unmarked-reflected-block" label="lem:unmarked-reflected-block">\[lem:unmarked-reflected-block\]</span> 对无标记反射块，令 \[T_0=2H+2A_0-N-N_0-3B_0,\qquad
 \nu_0=\frac v2+\ell_b+\frac{e_\lambda}{3}+\frac{S_0+B_0}{2}.\] 令所有这些对数长度在固定有界集上变化。令 \[Y=\frac{q_{\lambda^kN_FB_F^3}X Z^vZ^{3\ell_b}}
          {q_{c_FF_{\rm act}}^2Z^{2H}},\qquad
 W(\boldsymbol y)=y_n^{-1/2}y_b^{-1}W_0(\boldsymbol y),\qquad
 F_Y(\boldsymbol y)=W(\boldsymbol y)V^\sharp(Yy_ny_b^3y_R^{-2}).\] 存在函数 \(\rho(R)\) 与 \(\beta(n,b)\)，其绝对值至多为一，使得 \(\beta\) 独立于 \(R\)，且 \[\label{eq:unmarked-structural-block}
 \mathcal U_{v,\ell_b,e_\lambda}(R)
 =\frac13 Z^{-\nu_0}\rho(R)
       \sum_{n,b}\beta(n,b)\chi_R(nb)^3F_Y(y_R,y_n,y_b).\] 该和保留定义中所有固定的对偶限制。此处唯一同时依赖于 \(R\) 与对偶变量的算术因子 是所示零延拓的二次符号。此外， \[\label{eq:unmarked-actual-annuli}
 \frac{q_\mu X}{q_c^2}=Yy_ny_b^3y_R^{-2},\qquad
 c=c_FF_{\rm act}R.\] 这是原始支撑上的精确恒等式，包括 \(N_F\) 与 \(b\) 共享素因子的情形。

对每个 \(\epsilon>0\) 与每个固定的 \(A\ge0\)， \[\label{eq:unmarked-reflected-energy}
 \begin{split}
 \sum_{R\in\mathcal I_H}|\mathcal U_{v,\ell_b,e_\lambda}(R)|^2
 &\ll_{\epsilon,A} Z^{E_0+\epsilon}p_5(W)^2
       \mathfrak M_{A,\lceil4A\rceil+7}(V)^2,\\
 E_0={}&\max(H,v+\ell_b)-S_0-B_0-\ell_b-\frac{2e_\lambda}{3}
       -\frac12(T_0-v-3\ell_b-e_\lambda)_+.
 \end{split}\] 常数可以依赖于固定的核阶 \(A\)、固定的算术数据、有界的对数长度范围以及固定的支撑盒， 但不依赖于变动的冻结局部集 \(\mathcal F\)。\(W_0\) 中的范数扭曲具有由其有限半范数 提供的多项式代价。

对固定的 \(h_0\) 与 \(R\) 模 \(M_{\rm ref}^2\) 的固定同余类，\(F_{\rm act}R\) 的类也是固定的。 因此命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 为整个行集给出一个公共的 \(d\) 和一个公共的 加性特征 \(\vartheta\)。记 \(x_F=u\lambda^{k+4}N_FB_F^3\)，从而 \(\lambda^4\mu=x_Fnb^3\)。 剩余局部因子恰为 \[\prod_{p\mid R}B_p(\lambda^4\mu)
 =\chi_R(x_F)^3\chi_R(nb^3)^3
 =\chi_R(x_F)^3\chi_R(nb)^3.\] 两个等式都包含零点；没有除以任何单位符号。特别地，与 \(x_F\) 的任何碰撞都是只依赖于 \(R\) 的限制。每个剩余的局部因子都是固定的，且只依赖于对偶指标。反射的标量 \(\zeta_R\) 依赖于 \(R\) 但不依赖于 \(\mu\)。

在指定的对偶支撑上定义 \[\delta(n,b)=
 \frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}
      {27\,3^{k/6}|B_Fb|}.\] 系数界给出 \(|\delta(n,b)|\le1\)。其分母非零，且当分子为零时定义仍然有效。 利用 \(q_\mu=3^kq_{N_Fn}q_{B_Fb}^3\) 得到精确分解 \[\frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}
 =27\delta(n,b)q_{\lambda^k}^{-1/3}
                  q_{N_Fn}^{-1/2}q_{B_Fb}^{-1}.\] 小的 Ramanujan 因子或活跃的零掩码因子贡献 \(q_p^{-1/2}\)。整除性因子贡献 \(q_p^{1/2}\)； 对分配给 \(N_F\) 的素因子，它抵消无平方因子分母中的 \(q_p^{-1/2}\)，而对分配给 \(B_F\) 的 素因子，它在抽取后留下 \(q_p^{-1/2}\)。当分配给 \(N_F\) 的素因子也整除 \(b\) 时，它在 \(b\) 中的全部出现都保留在 \(q_b^{-1}\) 与 \(\delta(n,b)\) 中。这些事实恰好给出公共幂 \(Z^{-\nu_0}y_n^{-1/2}y_b^{-1}\)。

把 \(\delta\)、小 Ramanujan 项的符号、有界固定局部特征以及固定对偶指示函数吸收进 \(\beta(n,b)\)。该函数被一界住且独立于 \(R\)。令 \(\rho(R)=81\zeta_R\chi_R(x_F)^3\)； 由于 \(|\zeta_R|\le1/81\)，它被一界住。因子 \(27/81=1/3\) 随即证明 方程 [\[eq:unmarked-structural-block\]](#eq:unmarked-structural-block)。范数的乘性证明 方程 [\[eq:unmarked-actual-annuli\]](#eq:unmarked-actual-annuli)。它不使用 \(N_F\) 与 \(b\) 之间的任何互素性。

由对数范数的定义， \[Y=q_{c_F}^{-2}Z^{v+3\ell_b+e_\lambda-T_0}.\] 可能的 \(c_F\) 的有限集只依赖于 \(L\)。因此 \(\mathfrak m_A(Y)\ll_L Z^{-(T_0-v-3\ell_b-e_\lambda)_+/4}\)。 把引理 [\[lem:reflection-common-profile\]](#lem:reflection-common-profile)（三维）与 方程 [\[eq:reflection-common-minkowski\]](#eq:reflection-common-minkowski) 应用于该结构恒等式。 该单一密度对所有 \(R\) 是公共的，因为 \(W\) 以行范数与两个对偶范数作为坐标。 在每个 Fourier 模处，范数幂的绝对值为一，可吸收进有界的行标量与公共对偶系数。 直到此时才把正的行范数从 \(\mathcal I_H\) 扩大到满足 \(q_R\ll Z^H\) 的无平方因子良好 \(R\)， 并保留任何固定限制。对新增的行不使用核估计。

方程 [\[eq:completed-quadratic-norm\]](#eq:completed-quadratic-norm)（取 \(K=Z^H\)、\(N_{\rm col}=Z^v\)、 \(B_{\rm col}=Z^{\ell_b}\)）把分离后的平方范数界为 \[Z^{\epsilon+\max(H,v+\ell_b)+v+\ell_b}.\] 结构恒等式中的公共系数平方具有指数 \(-v-2\ell_b-2e_\lambda/3-S_0-B_0\)。 抽取出的剖面标量的平方贡献 \(-(T_0-v-3\ell_b-e_\lambda)_+/2\)。把这些指数与 三维分离范数结合，即证明方程 [\[eq:unmarked-reflected-energy\]](#eq:unmarked-reflected-energy)。

为便于后面的求和，称一个对偶块是保留的，当 \[v+3\ell_b+e_\lambda\le T_0+\tau_{\rm ref},
 \qquad \tau_{\rm ref}>0.\] 在固定支撑盒上，方程 [\[eq:unmarked-actual-annuli\]](#eq:unmarked-actual-annuli) 把核变量置于 \([C_{\rm ker}^{-1},C_{\rm ker}]\) 乘以 \(Z^{v+3\ell_b+e_\lambda-T_0}\) 之中， 其中 \(C_{\rm ker}\) 固定。若 \(\log Z\ge2\log C_{\rm ker}/\tau_{\rm ref}\)， 则每个未保留的整块在其支撑上各处的实际变量都大于 \(Z^{\tau_{\rm ref}/2}\)。 当其余对数长度位于有界范围时，这些块可在 Fourier 反演之前以任意幂次节省被移除。 以下是该一致性断言所需的细节。

在完整源支撑上， \[\frac{|d(\mu)|}{\sqrt{q_\mu}}
 \le27q_{\lambda^k}^{-1/3}q_{n_0}^{-1/2}q_{b_0}^{-1}
 \le27q_\lambda^{4/3}.\] 在丢弃其指示函数之后，每个局部因子都被 \(q_p^{1/2}\) 界住，且关于 \(\mu\) 一致。 当活跃对数范数有界时，这些界的乘积具有固定的多项式大小。对固定的行令 \(a=X/q_c^2\)。 其因子 \(1+a^{-1}\) 在所述行与导子范围上也具有固定的多项式界。有限局部选择与有界行计数 具有进一步固定的多项式代价；把这些范数尺度指数之和记作 \(B_{\rm tail}\)。 固定的剖面半范数及其多项式高度代价仍是该指数之外的可乘因子。 它在核阶之前选定，且不计入被丢弃的对偶指标。 剩余的对偶和是引理 [\[lem:lattice-kernel-tail\]](#lem:lattice-kernel-tail) 中无限制的格点和，其中 \(U=Z^{\tau_{\rm ref}/2}\)。对任意 \(D>0\)，选取 \[A>1+\frac{2(B_{\rm tail}+D)}{\tau_{\rm ref}}\] 使被丢弃的贡献为 \(O(Z^{-D})\) 乘以 \(V\) 的一个有限半范数与固定剖面界。 该断言或对绝对总和成立，或在把 \(B_{\rm tail}\) 增大以计入有界行计数后对行范数成立。 二进截断具有有界重叠，因此该格点估计控制它们的整个和。特别地， 没有对被丢弃的对偶长度作任何假设。

我们最后对一个元素行求和这些反射块。下面的范数观察记录了支配该求和的实际支撑。 假设一个元素行有理想分解 \((m)=m_{\rm pow}m_{\rm sup}R\)，各因子为整理想， 且固定支撑常数给出 \[q_m\le C_mZ^M,\qquad q_{m_{\rm pow}}\ge Z^O/C_O,
 \qquad q_R\ge Z^H/C_H.\] 由于 \(q_{m_{\rm sup}}\ge1\)，乘性给出 \[\label{eq:actual-residual-row-dyad}
 H\le M-O+\frac{\log C_{\rm res}}{\log Z},
 \qquad C_{\rm res}=C_HC_mC_O.\] 该不等式不要求 \(m_{\rm sup}\) 的范数有界，且它不必取等号。我们将在三个因子位于 不相交素支撑上、且单位剩余理想落在有界 \(H=0\) 二进区间的情形下使用它。

<span id="lem:unmarked-completed-moment" label="lem:unmarked-completed-moment">\[lem:unmarked-completed-moment\]</span> 令 \(\nu\) 取遍一个固定的有限族乘性有限射线特征，其导子支撑于 \(S\) 上， 且都在与 \(S\) 互素的主元素之外零延拓。固定 \(M\ge0\) 与 \(N\in\mathbb R\) 的有界范围、 一个常数 \(C_m\ge1\)，以及固定的二进支撑比较。对非零元素 \(m\)，令 \[m_{\rm pow}=\prod_{v_{\mathfrak p}(m)\ge2}
                 \mathfrak p^{v_{\mathfrak p}(m)}\] 为其极大幂理想因子。对其二进区间使用非负中心 \(O\)，单位区间取中心零。

对每个 \(\epsilon>0\)，存在有限的 \(A\ge0\) 与整数 \(J\ge0\)，使得对每个满足 命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 的检验函数 \(V\)、每个实际的 \(O\)-二进区间 以及所有充分大的 \(Z\)， \[\label{eq:unmarked-completed-moment}
 \sum_{\substack{0<q_m\le C_mZ^M\\q_{m_{\rm pow}}\asymp Z^O}}
       |\mathcal C_V(Z^N;m,\nu)|^2
 \ll Z^{O/2+\max\{M-O,\,2M-O-N\}+\epsilon}
       \mathfrak M_{A,J}(V)^2.\] 有限阶、常数与下阈值可以依赖于固定的算术数据、参数范围、\(C_m\)、二进支撑比较 以及 \(\epsilon\)。它们对元素行与固定族中的 \(\nu\) 一致。该估计直接包含 Gaussian 检验函数；对 \(V\) 不作环带支撑假设。用 \(x^{it_0}V(x)\) 替换 \(V(x)\) 至多带来 关于 \(1+|t_0|\) 的固定多项式代价。

固定一个特征 \(\nu\)。取 \(\Psi_{\rm base}=\nu\)，引理 [\[lem:reflection-row-sectors\]](#lem:reflection-row-sectors) 为 \(\nu(A)\chi_A(m)\) 的反射提供固定的有限族字面特征。在任何良好行素因子变化之前 选定它们的公共 \(\mathfrak E,L\)。把行划分为该引理中的有限多个单位、\(S\)-赋值剩余与 良好射线扇区。这样保留了每个良好局部素因子，包括其行赋值被六整除的那些。

对指定的 \(O\)-二进区间中的行，把其赋值为一的素因子拆分为支撑于 \(S\) 上的 \(m_{\rm sup}\) 与无平方因子的良好积 \(R\)。于是 \((m)=m_{\rm pow}m_{\rm sup}R\)， 位于不相交的素支撑上。冻结单位、实际理想 \(m_{\rm pow},m_{\rm sup}\)，然后把 \(R\) 划分为实际光滑环带 \(q_R\asymp Z^H\)，其中 \(H\ge0\) 且单位落在有界的零二进区间。 在每个反射向量中保留此截断。方程 [\[eq:actual-residual-row-dyad\]](#eq:actual-residual-row-dyad) 给出 \[\label{eq:unmarked-row-width}
 H\le M-O+O_{\rm fixed}(1/\log Z).\] 固定的行限制，包括与冻结因子的互素性，都独立于对偶变量。

经过行扇区转换后，取定义 [\[def:unmarked-reflected-block\]](#def:unmarked-reflected-block) 中的 \(\mathcal F\) 为 \(m_{\rm pow}\) 的良好素因子，其赋值模六约简。\(R\) 的素因子指数为一。固定 \(h_0\)、 \(R\) 模 \(M_{\rm ref}^2\) 的一个同余类，以及冻结素因子处的局部活跃与 Ramanujan 选择。 每个活跃的冻结良好素因子都以至少二的指数整除 \(m_{\rm pow}\)。因此 \[\label{eq:unmarked-powerful-radical}
 q_{F_{\rm act}}^2\le q_{m_{\rm pow}},\qquad
 2A_0\le O+O_{\rm fixed}(1/\log Z).\] 这使用了实际幂二进区间的上界比较。\(m_{\rm pow}\) 可能的 \(S\)-素因子只增大其范数。

把 \(X=Z^N\) 处的方程 [\[eq:reflection\]](#eq:reflection) 应用于方程 [\[eq:unmarked-central-mellin\]](#eq:unmarked-central-mellin) 中的 Mellin 表示。其对偶和绝对收敛。在剩余无平方因子范数与立方范数中插入固定的 光滑二进划分，并固定对偶指标的单位与分歧指数。这些操作给出 定义 [\[def:unmarked-reflected-block\]](#def:unmarked-reflected-block) 的块，且 \(W\) 的半范数一致有界。 无需对原始检验函数 \(V\) 作划分：此处的紧剖面是对偶截断与行截断乘以正规化的逆根之积， 而 \(V^\sharp\) 仍是核。

固定一个小的 \(\tau_{\rm ref}>0\)。行长 \(H,O\)、活跃长度 \(A_0\) 与 \(N\) 位于固定有界 范围内。\(S_0,N_0,B_0\) 亦然，因为它们的素因子积整除 \(F_{\rm act}\)。因此， 引理 [\[lem:unmarked-reflected-block\]](#lem:unmarked-reflected-block) 之后的尾部论证以任意指定的幂次节省移除 所有未保留的整对偶块，并带 \(V\) 的一个有限半范数。其多项式代价包含下面的行计数 与局部计数，但不含被丢弃的对偶指标。先选定它的核阶，再增大命题中的 \(A,J\)， 使 \(\mathfrak M_{A,J}(V)\) 支配此尾部半范数与块半范数。这是可能的，因为增大 \(A\) 拓宽定义 \(\mathfrak M_{A,J}\) 的上确界，而增大 \(J\) 增大其权重。

记 \(e=e_\lambda\)。源限制 \(k\ge-4\) 给出 \(e\ge-4\log 3/\log Z\)。对保留的块， \[v+3\ell_b+e\le T_0+\tau_{\rm ref}.\] 由于 \(v,\ell_b\ge0\) 且 \(T_0\) 有界，这也界住了每个保留的对偶长度。对偶环带与 \(k\) 的保留选择只有对数多个。选取非负的 \(\epsilon_Z=O_{\rm fixed}(1/\log Z)\)， 大到足以覆盖方程 [\[eq:unmarked-row-width\]](#eq:unmarked-row-width) 与 [\[eq:unmarked-powerful-radical\]](#eq:unmarked-powerful-radical) 中的支撑偏移，并确保 \(e\ge-\epsilon_Z\)。

方程 [\[eq:unmarked-reflected-energy\]](#eq:unmarked-reflected-energy) 中的指数满足 \[E_0\le\max\{H,T_0-S_0-B_0\}+\frac53\epsilon_Z+\tau_{\rm ref}.\] 为看出这一点，使用 \(\max(H,v+\ell_b)-\ell_b=\max(H-\ell_b,v)\) 并丢弃非正的核项。 第一支至多为 \(H+2\epsilon_Z/3\)，因为 \(\ell_b,S_0,B_0\ge0\)。在第二支中， 保留性给出 \(v\le T_0-3\ell_b-e+\tau_{\rm ref}\)，故它至多为 \(T_0-S_0-B_0+5\epsilon_Z/3+\tau_{\rm ref}\)。此外， \[\begin{split}
 T_0-S_0-B_0
 &=2H+2A_0-N-N_0-S_0-4B_0\\
 &\le 2M-O-N+O(\epsilon_Z),
 \end{split}\] 由方程 [\[eq:unmarked-row-width\]](#eq:unmarked-row-width) 与 [\[eq:unmarked-powerful-radical\]](#eq:unmarked-powerful-radical)。 因此每个保留的块（其冻结行部分固定）的指数至多为 \[\max\{M-O,2M-O-N\}+\tau_{\rm ref}+O(\epsilon_Z).\]

还需计算冻结部分与有限展开。每个幂理想都唯一地写成 \(x^2y^3\)，其中 \(y\) 无平方因子： 在一个素因子处，\(y\) 的指数是幂指数的奇偶性，而奇正指数至少为三。因此理想计数与 \(\sum_yq_y^{-3/2}<\infty\) 给出 \[\#\{m_{\rm pow}:q_{m_{\rm pow}}\ll Z^O\}\ll Z^{O/2}.\] 无平方因子的 \(m_{\rm sup}\) 是 \(S\) 的固定根式的一个因子，只有有限多个选择。 \(m_{\rm pow}\) 的良好素因子处的局部分支具有被因子数界住的重数，其 Ramanujan 分配亦然。逐行的因子 Cauchy 再对局部选择求和，代价为 \(Z\) 的任意小幂。 \(h_0\)、固定射线扇区与单位的选择都有限，而实际的行环带与保留的对偶环带只花费 \(\log Z\) 的幂。这恰好一次地计入幂贡献 \(O/2\)。

在给定的 \(\epsilon\) 余量内选取 \(\tau_{\rm ref}\) 与局部小幂损失。然后增大固定数据 阈值 \(Z\)，使 \(O(\epsilon_Z)\) 项落在该余量内。块界、前面的计数以及已选定的尾部节省 证明方程 [\[eq:unmarked-completed-moment\]](#eq:unmarked-completed-moment)。扭曲断言由 命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 中 \(\mathfrak M_{A,J}\) 的范数扭曲界推出。

为明确等长度处所用的检验函数，令 \[V_{\rm G}(y)=\frac1{2\sqrt\pi}
           \exp\!\left(-\frac{(\log y)^2}{4}\right).\] 它直接满足命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 的假设，有 \(\widehat V_{\rm G}(t)=e^{t^2}\)，且对每个有限 \(A,J\) 都有有限的 \(\mathfrak M_{A,J}\)。 因此前面的引理无需额外的环带延拓即可应用于它。在 \(X=Z\) 处其精确的 Mellin 形式为 \[\mathcal C_{V_{\rm G}}(Z;m,\nu)=\frac1{2\pi i}\int_{(4)}
       Z^t e^{t^2}T(t+1/2,\nu\chi_\bullet(m))\,dt.\] 在定义和中，系数仍由 \(q_c^{-1/2}q_n^{-1}\) 正规化；尺度出现在 \(V_{\rm G}(q_cq_n^3/Z)\) 中。

最后取 \(M=N=1\)。实际 \(O\)-二进区间中的指数为 \(1-O/2+\epsilon\)。非负 \(O\)-二进区间 只有对数多个，且其单位二进区间已含在内。对它们求和（带一个更小的预备损失）， 给出对每个可容许 \(V\) 的等长度结论： \[\label{eq:unmarked-balanced-completed-moment}
 \sum_{0<q_m\le C_mZ}|\mathcal C_V(Z;m,\nu)|^2
 \ll Z^{1+\epsilon}\mathfrak M_{A,J}(V)^2.\]

### 基础探针及其平衡低估计

现在我们把上一节的完备化和放入一个平均 \(I_\eta(X,Y,Z)\) 中。它的原始表示分解为 一个加性多项式与一个完备化 theta 行。在平衡尺度 \(X=Y=Z^{1/2}\) 处，它们的均方 估计给出直接界 \(I_\eta\ll_\eta Z^{1/4+\epsilon}\)。我们先对独立的正尺度 \(X,Y,Z\) 定义该平均；本节只有最后的命题才将它们特殊化。下一节对同一平均应用 Poisson 求和， 并在其主行中识别目标 \(L\) 函数的倒数。

#### 两个因子的定义与分离

选取一个有限射线群 \(T\)（独立于目标特征），使函数 \(\mathcal R\)、\(G\) 以及 引理 [\[lem:fixed-gauss-phase\]](#lem:fixed-gauss-phase) 中支撑于 \(2,3\) 上的固定主相位与补充相位都能 通过它分解。下面依赖于目标的固定分子特征不必通过 \(T\) 分解。对有限阶 Hecke 特征 \(\eta\)，记 \[\Theta=\langle\eta,\widehat T\rangle.\] 对有限族 \(\{\eta\theta:\theta\in\widehat T\}\) 使用一个排除集 \(S\)。它包含 \(6\) 上的 素因子、\(\eta\) 与 \(\widehat T\) 中特征的固定零延拓表示的定义模的素支撑，以及范数 至多一个固定 \(P_0\) 的每个素因子。这些完整表示属于固定的算术数据。它们在选定 \(X,Y,Z\) 与变动的行参数、素参数之前就固定。扩大 \(S\) 不会改变 \(T\)。

有限变换应排除与 \(S\) 相交的频率（包括零），并应留下逐素因子分解的系数。 下面的特征与相位修正安排这两个性质。

令 \(b_*\) 生成 \(S\) 中素因子的无平方因子积。选取模 \(b_*\) 的剩余特征 \(\xi\)， 使其在每个素因子上的限制都是非主的，且其阶整除六。这样的选择存在： 在奇剩余特征的素因子处可以使用二次特征，而 \(2\) 上素因子处的剩余域阶为四且有一个 三阶特征。中国剩余定理使 \(\xi\) 模 \(b_*\) 本原。以下所有剩余特征都在非单位上零延拓。令 \[\begin{gathered}
 g_\psi(c,k)=\sum_{d\bmod c}\psi(d)e(kd/c),\qquad
 \tau=q_{b_*}^{-1/2}g_\xi(b_*,1),\qquad
 \Xi(a)=\xi(a)\chi_a(b_*),\\
 \Psi_{m,s,\eta}(a)=
       \eta(a)\Xi(a)^{-1}\mathcal R(a,s)\chi_a(m)
       \qquad ((a,S)=1).
 \end{gathered}\] 每个素因子处的有限特征正交性给出 \(|\tau|=1\)。 由引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray)，固定分子符号 \(a\mapsto\chi_a(b_*)\) 是一个 有限射线特征，其导子支撑于 \(S\) 上。因此 \(\Xi\) 是该目标的一个固定有限特征， 尽管它不必通过 \(T\) 分解。

\(S\) 中素点处的本原特征 \(\xi\) 将迫使 Poisson 频率与 \(S\) 互素。相伴随的 正规化消去了由辅助模 \(b_*\) 引入的单位因子。对完备化指标 \(A=cn^3\)，因子 \(\mathcal R(A,s)\) 消去 \(A\) 与 \(s\) 之间的跨素互反相位，而 \(\overline{G(A)}\) 消去 \(A\) 内剩余的配对相位。我们在 节 [5.2](#sec:local-euler) 中逐系数验证这些消去。

定义在谱参数 \(t+1/2\) 处的修正行为 \[T_{m,s,\eta}(t)=
 \sum_{\substack{c\ {\rm sf}\\n}}
 \gamma_2(c)\overline{\alpha(cn^3)}\Psi_{m,s,\eta}(cn^3)
 \overline{G(cn^3)}q_c^{-1/2-t}q_n^{-1-3t}.\] 此处及以下理想变量均避开 \(S\)。特别地，\(\Xi(a)^{-1}\) 中的每个因子都在一个 单位上取值。值 \(G(cn^3)\) 是方程 [\[eq:G-quadratic-refinement\]](#eq:G-quadratic-refinement) 中的有限 射线延拓，当 \(cn^3\) 非无平方因子时亦然。

固定非负且非零的函数 \(W_0,W_1\in C_c^\infty(0,\infty)\)，并令 \(\Phi(t)=e^{t^2}\)。定义 \[\label{eq:general-probe}
\begin{aligned}
 I_\eta(X,Y,Z)={}&\frac1Y\sum_s
 \frac{W_1(q_s/Y)\chi_s(b_*)}
      {\tau\xi(s)\sqrt{q_{b_*}q_sX}}\\
 &\quad\cdot\sum_{m\in\mathcal O}
       \xi(m)q_s^{-1/2}g_{\chi_s}(s,-m)
       W_0\!\left(\frac{q_m}{q_{b_*}q_sX}\right)
       \frac1{2\pi i}\int_{(4)}
             Z^t\Phi(t)T_{m,s,\eta}(t)\,dt.
\end{aligned}\] 此定义中的掩码去除了 \(S\) 处的非单位。方程 [\[eq:general-probe\]](#eq:general-probe) 中所有 求和都在所示的直线上绝对收敛；由于权重是环形的，\(m\) 与 \(s\) 的求和是有限的。

修正项的固定有限 Fourier 展开为 \[\overline{G(A)}=\sum_{\theta\in\widehat T}a_\theta\theta(A),
 \qquad
 a_\theta=\frac1{|T|}\sum_{v\in T}
                 \overline{G(v)}\,\overline{\theta(v)}.\] Parseval 与 Cauchy–Schwarz 给出 \(\sum_\theta|a_\theta|\le |T|^{1/2}\)。对射线类 \(\sigma\in T\)，选取代表元 \(s_\sigma\) 并令 \[\begin{aligned}
 \nu_\sigma(a)&=\eta(a)\Xi(a)^{-1}\mathcal R(a,s_\sigma)
       \quad ((a,S)=1),\\
 B_{m,\sigma}(Z)&=\sum_{\theta\in\widehat T}a_\theta
 \frac1{2\pi i}\int_{(4)}Z^t\Phi(t)
       T(t+1/2,\nu_\sigma\theta\chi_\bullet(m))\,dt.
 \end{aligned}\] 将 \(\nu_\sigma\) 在离开与 \(S\) 互素的主元素处按零延拓，且不在那里计算 \(\Xi(a)^{-1}\)。这里的函数 \(T\) 是方程 [\[eq:reflection\]](#eq:reflection) 中的完备化乘积， 带有其原有的零掩码。由于对 \(s\in\sigma\) 有 \(\mathcal R(A,s)=\mathcal R(A,s_\sigma)\)，修正行所示的 Mellin 积分在该类上 处处等于 \(B_{m,\sigma}(Z)\)。

对 \(m\ne0\)，中心 Mellin 恒等式 [\[eq:unmarked-central-mellin\]](#eq:unmarked-central-mellin) 给出直接的特别化 \[B_{m,\sigma}(Z)=\sum_{\theta\in\widehat T}a_\theta
       \mathcal C_{V_{\rm G}}(Z;m,\nu_\sigma\theta).\] 特征 \(\nu_\sigma\theta\) 构成一个固定的有限族，其导子与定义模的支撑都包含在 \(S\) 中。它们不必通过 \(T\) 分解。它们原有的零延拓即为完备化行矩中的那些， 因此该估计直接适用于这一行求和族。行 Hilbert 空间中的三角不等式只需付出 固定因子 \(\sum_\theta|a_\theta|\) 的代价。该估计所用的行扇区转换保留了在共享 好素点处的零点，包括行赋值被六整除的情形。

记 \(Q=q_{b_*}XY\)。选取 \((0,\infty)\) 上光滑且具紧支集的函数 \(\Omega\)，它在 \(W_1(q_s/Y)W_0(q_m/(q_{b_*}q_sX))\) 的支撑上可能出现的每个 \(q_m/Q\) 值处都等于 一。对 \(v\in\mathbb R\)，令 \[A_{m,\sigma,v}(Y)=\frac1Y\sum_{s\in\sigma}
 \frac{W_1(q_s/Y)\chi_s(b_*)}{\tau\xi(s)}
 (q_s/Y)^{-1/2+iv}q_s^{-1/2}g_{\chi_s}(s,-m).\] 我们对 \(W_0\) 的 Mellin 约定为 \(\widehat W_0(iv)=\int_0^\infty W_0(r)r^{iv}\,dr/r\)。由于 \(q_m/(q_{b_*}q_sX)=(q_m/Q)/(q_s/Y)\)，Mellin 反演给出精确恒等式 \[\label{eq:low-separated}
 I_\eta(X,Y,Z)=\frac{Q^{-1/2}}{2\pi}
 \sum_{\sigma\in T}\int_{\mathbb R}\widehat W_0(iv)
 \sum_{m\ne0}\Omega(q_m/Q)\xi(m)(q_m/Q)^{-iv}
                 A_{m,\sigma,v}(Y)B_{m,\sigma}(Z)\,dv.\] 被略去的 \(m=0\) 项由 \(W_0\) 的环形支撑而消失。因子 \((q_m/Q)^{-iv}\) 的绝对值为 一。在 \(A\) 中，算术系数是固定的，且其有界性与 \(m,v\) 无关；对 \(v\) 的全部依赖 都出现在环形变量的范数幂中。

Gauss 型 \(V_{\rm G}\) 的 Mellin 变换为 \(e^{t^2}\)，并直接满足反射假设。因此 引理 [\[lem:unmarked-completed-moment\]](#lem:unmarked-completed-moment) 无需对该检验函数作环形分解即可适用。

#### 平衡低估计

对于平衡估计，完备化行矩已经给出了 \(B_{m,\sigma}(Z)\) 的均方界。尚需给出加性 因子 \(A_{m,\sigma,v}(Y)\) 的界。它的 Gauss 展开给出 \(\mathbb C/\mathcal O\) 中 互不相同的既约分数；它们之间的分离度与系数质量给出了所需的均方。平面加性 大筛法是经典的；可比较 Huxley 的多变量与数域不等式  以及  中的 Poisson 证明。我们给出格点证明 以记录此处所用的正规化。

<span id="lem:planar-additive-sieve" label="lem:planar-additive-sieve">\[lem:planar-additive-sieve\]</span> 令 \(0<\delta\le1\)，\(Q\ge1\)，并令 \(z_1,\ldots,z_J\) 为 \(\mathbb C/\mathcal O\) 中满足 \[\inf_{n\in\mathcal O}|z_j-z_k-n|\ge\delta
 \qquad(j\ne k).\] 的有限点集。则对任意复数 \(a_1,\ldots,a_J\)， \[\sum_{\substack{m\in\mathcal O\\q_m\le Q}}
 \left|\sum_{j=1}^J a_j e(mz_j)\right|^2
 \ll (Q+\delta^{-2})\sum_{j=1}^J|a_j|^2.\] 隐含常数对上面固定的格、加性特征与自对偶测度是绝对的。行球中允许 \(Q\) 的固定 倍数，只需改变该常数。

当 \(J=0\) 时断言显然成立。由自对偶性，特征 \(e(mz_j)\) 在 \(\mathbb C/\mathcal O\) 上有良好定义。对其余情形在 \(\mathbb C\) 中选取代表元。 我们使用 Fourier 变换 \[\widehat F(y)=\int_{\mathbb C}F(x)e(-xy)\,d\mu(x),\qquad
 \check\phi(x)=\int_{\mathbb C}\phi(y)e(xy)\,d\mu(y).\] 选取非负的 \(\phi\in C_c^\infty(\mathbb C)\)，其积分为一，支撑在原点周围一个 足够小的圆盘内。由于 \(|e(xy)-1|\le (4\pi/\sqrt3)|x||y|\)，可选取其支撑使得 \[|\check\phi(x)-1|\le\frac12\qquad(|x|\le1).\] 于是 \(F(x)=4|\check\phi(x)|^2\) 是非负 Schwartz 函数，且 \(F(x)\ge1\) 在单位圆盘 上成立。若 \(\widetilde\phi(y)=\overline{\phi(-y)}\)，则 Fourier 反演与乘积 公式（卷积就 \(d\mu\) 取）给出 \[\widehat F=4\phi*\widetilde\phi.\] 特别地，\(\widehat F\) 有界，且支撑在某个固定半径 \(L\) 的圆盘内。这正是我们所需 的带限优函数。

令 \(R=\sqrt Q\)。\(F\) 的正性首先给出 \[\sum_{q_m\le Q}\left|\sum_j a_je(mz_j)\right|^2
 \le \sum_{m\in\mathcal O}F(m/R)
                    \left|\sum_j a_je(mz_j)\right|^2.\] 右端所有求和都绝对收敛。对任意 \(z\in\mathbb C\)，映射 \(x\mapsto F(x/R)e(xz)\) 在 \(y\) 处的 Fourier 变换为 \(R^2\widehat F(R(y-z))\)。因子 \(R^2\) 是实二维伸缩的 Jacobian；由于 \(d\mu\) 在 \(\mathcal O\) 上的余体积为一，不出现格体积因子。 因此 Poisson 求和将右端展开为 \[R^2\sum_{j,k}a_j\overline{a_k}
       \sum_{n\in\mathcal O}
       \widehat F\bigl(R(n-z_j+z_k)\bigr).\]

对每个固定的 \(j\)，内层求和中的项只有在提升 \(z_k+n\) 位于 \(z_j\) 的距离 \(L/R\) 之内时才可能非零。所有提升的集合 \(\{z_k+n:1\le k\le J,\ n\in\mathcal O\}\) 在 \(\mathbb C\) 中是 \(\delta\)-分离的。由假设，不同的类具有该性质，而同一类的两个不同提升之差为 一个非零 Eisenstein 整数，其绝对值至少为一，从而至少为 \(\delta\)。在以半径 \(L/R\) 的圆盘内、以提升为中心、半径 \(\delta/3\) 的圆盘互不相交，且位于半径 \(L/R+\delta/3\) 的同心圆盘内。比较它们的 Euclid 面积可将这些提升的数目界为 \[\left(1+\frac{3L}{R\delta}\right)^2
 \ll 1+(R\delta)^{-2}.\] 将 \(j\) 与 \(k\) 互换后同样的界成立。在 Poisson 展开中取绝对值，使用 \(\widehat F\) 的固定界，再使用 \(2|a_ja_k|\le |a_j|^2+|a_k|^2\)，我们得到 \[\sum_{q_m\le Q}\left|\sum_j a_je(mz_j)\right|^2
 \ll R^2\bigl(1+(R\delta)^{-2}\bigr)\sum_j|a_j|^2.\] 由于 \(R^2=Q\)，这就是所断言的估计。将 \(Q\) 换为固定倍数即证明最后的陈述。

我们将该估计应用于 Gauss 和中的完整剩余类。特征按零延拓在这里很重要：它使 这些分数相对于所展示的模是既约的，而不仅仅相对于某个诱导导子。

<span id="lem:balanced-additive-norm" label="lem:balanced-additive-norm">\[lem:balanced-additive-norm\]</span> 固定探针的算术数据、环形权重 \(W_1\)、射线类 \(\sigma\in T\) 以及行球常数 \(C>0\)。对 \(Y,Q\ge1\) 及每个实 \(v\)，多项式 \(A_{m,\sigma,v}(Y)\) 满足 \[\sum_{\substack{m\in\mathcal O\\q_m\le CQ}}
       |A_{m,\sigma,v}(Y)|^2
 \ll_{\mathcal A,W_1,C}\frac{Q+Y^2}{Y}.\] 该界对 \(v\) 一致。特别地，当 \(Q=q_{b_*}Y^2\) 时， \[\sum_{q_m\le CQ}|A_{m,\sigma,v}(Y)|^2
 \ll_{\mathcal A,W_1,C}\frac QY.\]

对 \(S\) 之外的主元素 \(s\)，令 \(r_s=q_s/Y\) 且 \[c_\sigma(s)=1_{s\in\sigma}\frac{\chi_s(b_*)}{\tau\xi(s)}.\] 逆只在与 \(S\) 互素的这些元素上取值。这里 \(|\tau|=1\)、\(|\xi(s)|=1\)、 \(|\chi_s(b_*)|=1\)，因为 \(b_*\) 的支撑在 \(S\) 上。因此 \(|c_\sigma(s)|\le1\)。\(A\) 的定义与 Gauss 展开给出精确恒等式 \[A_{m,\sigma,v}(Y)
 =Y^{-3/2}\sum_s c_\sigma(s)W_1(r_s)r_s^{-1+iv}
       \sum_{d\bmod s}\chi_s(d)e(-md/s).\] 该求和取遍 \(S\) 之外的主理想。对每个这样的 \(s\)，特征 \(\chi_s(d)\) 恰在 \((d,s)>1\) 时为零，否则其绝对值为一。这也包括非无平方因子的 \(s\)：被六整除的 局部指数是该素点处单位的指示函数，而非常值函数一。对 \(s=1\)，包含单个剩余类， 且 \(\chi_1=1\)。

我们验证：对作出贡献的配对，分数 \(d/s\) 模 \(\mathcal O\) 互不相同。设 \((d,s)=(d',s')=1\) 且 \(d/s-d'/s'\in\mathcal O\)。则 \(ss'\) 整除 \(ds'-d's\)。 将此整除性模 \(s\) 约化，并使用 \(d\) 模 \(s\) 的逆，得到 \(s\mid s'\)。对称论证给出 \(s'\mid s\)。\(S\) 之外理想的主生成元是唯一的，故 \(s=s'\)；原同余式随即给出 \(d=d'\pmod s\)。同一结论也包含单位模的情形。改变剩余代表元只会将其分数平移 \(\mathcal O\) 的一个元素。

固定 \(0<r_-<r_+\)，使 \(\operatorname{supp}W_1\subset[r_-,r_+]\)。对两个不同的 作出贡献的分数及每个 \(n\in\mathcal O\)，Eisenstein 整数 \(ds'-d's-nss'\) 非零。 因此 \[\left|\frac d s-\frac{d'}{s'}-n\right|
 =\frac{|ds'-d's-nss'|}{|ss'|}
 \ge\frac1{|ss'|}\ge\frac1{r_+Y}.\] 最后的不等式用到 \(q_s,q_{s'}\le r_+Y\)。因此这些分数在 \(\mathbb C/\mathcal O\) 中是 \(\delta_Y\)-分离的，其中 \(\delta_Y=\min(1,r_+^{-1})/Y\le1\)。

将展开后的多项式写作 \(\sum_{s,d}a_{s,d}e(-md/s)\)（只保留单位剩余类），其系数 的平方质量为恰好 \[\begin{split}
 \sum_{s,d}|a_{s,d}|^2
 &=Y^{-3}\sum_s |c_\sigma(s)W_1(r_s)|^2r_s^{-2}
       \varphi_{\mathcal O}(s),\\
 \varphi_{\mathcal O}(s)
 &:=\#(\mathcal O/s\mathcal O)^\times,\qquad
 \varphi_{\mathcal O}(1):=1.
 \end{split}\] 该表达式中不依赖于 \(v\)。由于 \(\varphi_{\mathcal O}(s)\le q_s\le r_+Y\)、在支撑上 \(r_s\ge r_-\)，且满足 \(q_s\le r_+Y\) 的理想有 \(O(Y)\) 个，该质量为 \(O(Y^{-1})\)。将 引理 [\[lem:planar-additive-sieve\]](#lem:planar-additive-sieve) 应用于以 \(\delta_Y\) 分离的点 \(-d/s\)， 即证明了第一个界。最后 \(q_{b_*}\ge1\)，故 \(Q=q_{b_*}Y^2\) 蕴含 \(Q+Y^2\le2Q\)，从而证明第二个。

加性范数现在恰好具有与无标记完备化行范数配对所需的尺度。下面的命题对原探针 完成该配对。

<span id="prop:balanced-low" label="prop:balanced-low">\[prop:balanced-low\]</span> 固定用于定义 \(I_\eta\) 的算术数据与光滑权重。对每个 \(\epsilon>0\)，当 \(Z\to\infty\) 时， \[\bigl|I_\eta(Z^{1/2},Z^{1/2},Z)\bigr|
 \ll_{\mathcal A,\epsilon} Z^{1/4+\epsilon}.\] 该指数与目标特征无关；隐含常数与下阈值可能依赖于它固定的算术数据。

令 \(X=Y=Z^{1/2}\) 且 \(Q=q_{b_*}XY=q_{b_*}Z\)。方程 [\[eq:low-separated\]](#eq:low-separated) 中 的函数 \(\Omega\) 有界，且其支撑在 \((0,\infty)\) 的一个固定紧子区间内。因此该 恒等式中的所有行都落在 \(0<q_m\le C_\Omega Q\) 中，其中 \(C_\Omega\) 为固定常数。

引理 [\[lem:unmarked-completed-moment\]](#lem:unmarked-completed-moment) 的特别化 \(M=N=1\)，继之以定义 \(B_{m,\sigma}\) 的有限射线分解，对每个 \(\epsilon_1>0\) 给出 \[\sum_{0<q_m\le C_\Omega Q}|B_{m,\sigma}(Z)|^2
 \ll_{\mathcal A,\epsilon_1} Z^{1+\epsilon_1}.\] 事实上，\(q_{b_*}\) 固定，故行球是 \(M=1\) 球的固定倍数。完备化尺度为 \(Z\)，在该 引理中即为 \(N=1\)。该引理直接适用于定义 \(B\) 的完备化积分中的 Gauss 型剖面； 由行 Hilbert 空间中的三角不等式，对射线特征的固定有限 Fourier 求和只需付出 固定因子的代价。特别地，此应用保留了原有的行零掩码。

对方程 [\[eq:low-separated\]](#eq:low-separated) 中的行求和应用 Cauchy–Schwarz。因子 \((q_m/Q)^{-iv}\) 的绝对值为一，\(|\xi(m)|\le1\)（带上其零延拓），且 \(\Omega\) 有界。引理 [\[lem:balanced-additive-norm\]](#lem:balanced-additive-norm) 对 \(v\) 一致，而 \(B\) 与 \(v\) 无关。 由于 \(W_0\) 光滑且为环形， \(\int_{\mathbb R}|\widehat W_0(iv)|\,dv<\infty\)。因此对 \(\sigma\in T\) 的有限 求和给出 \[\begin{split}
 |I_\eta(X,Y,Z)|
 &\ll_{\mathcal A,\epsilon_1}
 Q^{-1/2}\left(\frac QY\right)^{1/2}Z^{1/2+\epsilon_1/2}\\
 &=Z^{1/4+\epsilon_1/2}.
 \end{split}\] 取 \(\epsilon_1=2\epsilon\) 即证明命题。

### Poisson 表示及其 Euler 因子

直接估计现在已具备。为将探针与命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion) 中的 Mellin 信号作比较，我们回到相互独立的正常数尺度 \(X,Y,Z\)，并在元素变量 \(m\) 上应用 Poisson 求和。所得的行以频率的无六次幂因子部分为指标。我们将把每行 分解为 Hecke \(L\) 函数与一个全纯 Euler 乘积；行 \(u=1\) 将包含目标函数的倒数。

#### 精确的 Poisson 级数

修正项 \(\overline{G(A)}\) 与 \(m\) 无关，而完备化行中变化的特征恰为 \(\chi_A(m)\)（包括其零点）。于是 Poisson 求和使用完整模 \(sb_*A\)，即使 \(s\) 与 \(A\) 共享素点。展开 \(s\)-Gauss 和，并先对一个模 \(b_*A\) 的剩余类的提升求和。 这些提升施加 \(H\equiv b_*Ad\pmod s\)，并给出系数 \[\label{eq:local-F}
 F(s,A,H)=\sum_{\substack{d\bmod s\\H\equiv b_*Ad\pmod s}}
 \chi_s(d)g_{\xi\chi_A}\!\left(b_*A,\frac{H-b_*Ad}{s}\right).\] 事实上，\(\xi(m)\chi_A(m)q_s^{-1/2}g_{\chi_s}(s,-m)\) 模 \(sb_*A\) 的有限 Fourier 变换为 \(q_s^{1/2}F(s,A,H)\)。行尺度 \(q_{b_*}q_sX\) 的 Poisson 前因子为 \(X/q_A\)。在方程 [\[eq:general-probe\]](#eq:general-probe) 中外层平方根正规化之后（把其单独的 \(Y^{-1}\) 留在外面），它们的乘积为 \(X^{1/2}/(q_{b_*}^{1/2}q_A)\)。这也验证了 变换中所有 \(q_s\) 的因子。

在 \(b_*\) 的素点处，除非 \((H,S)=1\)，本原 Gauss 和为零。因此它也去除了 \(H=0\)。每个剩余元素都有唯一的表达式 \(H=ua^6\)，其中 \(u\) 是无六次幂因子的 元素（包括其单位因子），\(a\) 是某理想的主生成元。记 \(\sum_u^{(6)}\) 为对满足 \((u,S)=1\) 的这种非零 \(u\) 的求和。

令 \(\widetilde W_0(|y|^2)\) 为 \(W_0(|y|^2)\) 相对于节 [2](#sec:arithmetic) 中 固定的自对偶测度与特征的平面 Fourier 变换。Poisson 之后的径向 Fourier 变量 为 \(Xq_H/q_A\)。令 \[M(z)=\int_0^\infty\widetilde W_0(r)r^{z-1}\,dr,
 \qquad
 \widehat W_1(w)=\int_0^\infty W_1(r)r^{w-1}\,dr.\] 零点处的光滑性与 Schwartz 衰减表明 \(M\) 对 \(\Re z>0\) 全纯。在每个紧的正实带 形域上，它在 \(\Im z\) 方向具有任意阶多项式衰减：\(e^{(\Re z)v}\widetilde
W_0(e^v)\) 的每个导数对 \(v\) 都可积，且在该带形域上一致，故可反复分部积分。 同样的论证给出 \(\widehat W_1\) 在每个固定实带形域上的任意阶多项式衰减。

我们将需要严格正性 \[\label{eq:radial-mellin-positive}
 M(1/6)>0.\] 这里给出一个不需要 Fourier 变换自身非负的证明。对 \(0<\sigma<1\)， \[|y|^{2\sigma-2}=\frac1{\Gamma(1-\sigma)}
             \int_0^\infty t^{-\sigma}e^{-t|y|^2}\,dt.\] 左端与 \(\widetilde W_0(|y|^2)\) 的配对绝对可积。Fubini 与 Fourier 对偶将其 表示为 \[\frac1{\Gamma(1-\sigma)}\int_0^\infty t^{-\sigma}
 \int_{\mathbb C}W_0(|x|^2)
       \frac{2\pi}{\sqrt3\,t}
       \exp\!\left(-\frac{4\pi^2|x|^2}{3t}\right)
                  d\mu(x)\,dt>0.\] 由于 \(W_0\) 非负且非零，内层积分对每个 \(t>0\) 严格为正。绝对可积性或者由 Fourier 侧所示的表示式得到，或者由此侧 \(W_0\) 的环形支撑得到。极坐标积分将原 配对等同于 \((2\pi/\sqrt3)M(\sigma)\)，从而证明方程  [\[eq:radial-mellin-positive\]](#eq:radial-mellin-positive)。

在两个权重 Mellin 反演之后，令 \(x=t+1-z\)。对满足 \((u,S)=1\) 的非零无六次幂 因子 \(u\)，定义 \[\label{eq:local-full-series}
 \mathcal F_{\eta,u}(x,w,z)=
 \sum_{\substack{c\ {\rm sf}\\n,s,a}}
 K_\eta(c,n,s,a;u)\,
 q_c^{-1/2-x}q_n^{-1-3x}q_s^{-w}q_a^{-6z},\] 其中 \(A=cn^3\)，且保留全部正规化的系数为 \[\label{eq:local-full-coefficient}
 K_\eta(c,n,s,a;u)=
 \frac{F(s,A,ua^6)\chi_s(b_*)}
 {\sqrt{q_{b_*}}\tau\xi(s)\overline{\xi(u)}}
 \gamma_2(c)\overline{\alpha(A)G(A)}
 \eta(A)\Xi(A)^{-1}\mathcal R(A,s).\] 为方便起见，定义公共 Mellin 权重 \[\mathcal W(X,Y,Z;x,w,z)=
 X^{1/2-z}Z^{x+z-1}Y^{w-1}
 \Phi(x+z-1)M(z)\widehat W_1(w).\] 例如，直线 \(\Re x=3\)、\(\Re w=3\)、\(\Re z=2\) 对应原来的直线 \(\Re t=4\)，并 处于绝对收敛区域。完整的高阶恒等式为 \[\label{eq:probe-poisson-identity}
 \begin{split}
 I_\eta(X,Y,Z)=\frac1{(2\pi i)^3}
 \int_{(3)}\int_{(3)}\int_{(2)}
 &\mathcal W(X,Y,Z;x,w,z)\\
 &\cdot\sum_u^{(6)}q_u^{-z}\overline{\xi(u)}
             \mathcal F_{\eta,u}(x,w,z)\,dz\,dw\,dx.
 \end{split}\] 可以通过初等界 \(|F(s,A,H)|\le q_sq_{b_*A}\) 以及环形权重来论证这些直线上的 所有交换。特别地，方程 [\[eq:low-separated\]](#eq:low-separated) 与 [\[eq:probe-poisson-identity\]](#eq:probe-poisson-identity) 是同一探针的恒等式，而不是分别选取检验 表达式的估计。

#### 标量 Euler 恒等式

接下来我们计算方程 [\[eq:local-full-coefficient\]](#eq:local-full-coefficient) 中的系数。我们的目标是 证明该高阶级数是目标 \(\eta\) 的标量 Euler 乘积。该计算还单独记录了完备化指标 \(A\) 在给定素点处取正赋值的项。我们保留每个射线相位，直到它被消去或被指派给 某个局部因子。

固定满足 \((u,S)=1\) 的非零无六次幂因子行 \(u\) 以及素点 \(p\notin S\)。令 \[\label{eq:local-parameters}
 \begin{gathered}
 Q=q_p,\qquad j=v_p(u)\in\{0,\ldots,5\},\qquad
 \rho=\chi_p(u/p^j),\qquad \omega_p=\chi_p(-1),\\
 a_p=\overline{\alpha(p)}^3\eta(p)^3,\qquad
 b_p=\overline{\alpha(p)}^2\eta(p)^2\overline{\chi_p(4)},
 \qquad b_p^3=a_p^2,\\
 V=Q^{-6z},\qquad R=a_p^2Q^{4-6x-6z},\qquad
 W_{\rm loc}=\rho Q^{-w}.
 \end{gathered}\] 值 \(\rho,a_p,b_p\) 的绝对值为一，且 \(\omega_p\in\{1,-1\}\)。对 \(p\) 不施加任何 射线类限制。

###### 有限标量及其单位因子。

记 \(G_r=g_{\chi_p^r}(p,1)\)，其中 \(G_0=-1\)，并对 \(1\le r\le5\) 令 \(\gamma_r=Q^{-1/2}G_r\)。对 \(t\ge1\) 与 \(j'\ge0\)，对一个模 \(p\) 的剩余类的提升 求和给出 \[g_{\chi_p^r}(p^t,p^{j'})=
 \begin{cases}
 Q^{t-1}G_r1_{j'=t-1},&6\nmid r,\\
 Q^t1_{j'\ge t}-Q^{t-1}1_{j'\ge t-1},&6\mid r.
 \end{cases}\] 第二行是主特征（按零延拓）的 Ramanujan 和。正交性还给出 \(G_1G_{-1}=\omega_pQ\)。

令 \(e_0=v_p(c)\in\{0,1\}\)、\(l=v_p(n)\)、\(t=e_0+3l\)、\(k=v_p(s)\)、 \(m=v_p(a)\)，故 \(v_p(H)=j'=j+6m\)。方程 [\[eq:local-F\]](#eq:local-F) 在 \(p\) 处的部分 （在恢复其单位因子之前）为 \[\label{eq:local-scalar-definition}
 C_p(t,k,j')=
 \sum_{\substack{d\bmod p^k\\p^{j'}\equiv p^td\pmod{p^k}}}
 \chi_p^k(d)
 g_{\chi_p^t}\!\left(p^t,\frac{p^{j'}-p^td}{p^k}\right).\] 在模一时，此公式中的两个因子都表示一。其完整计算为 \[\label{eq:local-scalar-values}
 C_p(t,k,j')=
 \begin{cases}
 1,&t=k=0,\\
 1_{j'=0},&t=0,\ k>0,\\
 g_{\chi_p^t}(p^t,p^{j'}),&t>0,\ k=0,\\
 \omega_p^{-1}G_1g_{\chi_p^{t-1}}(p^t,p^{j'-1}),
                      &t>0,\ k=1,\ j'\ge1,\\
 0,&\text{otherwise}.
 \end{cases}\] 对 \(t=0\) 与 \(k>0\)，同余式固定 \(d=p^{j'}\) 模 \(p^k\)，其零延拓特征恰在 \(j'=0\) 时非零。对第四行，同余式首先迫使 \(j'\ge1\)。展开内层 Gauss 和，对 \(d\bmod p\) 的求和为 \[\sum_{d\bmod p}\chi_p(d)e(-vd/p)
       =\omega_p^{-1}G_1\chi_p(v)^{-1}
       \qquad(p\nmid v),\] 这使 Gauss 特征从 \(\chi_p^t\) 变为 \(\chi_p^{t-1}\)。若 \(t>0\) 且 \(k\ge2\)， 允许的提升 \(d=d_0+p^{k-1}v\) 不改变 \(\chi_p^k(d)\)，但其 Gauss 相位为 \(e(-yv/p)\)，其中 Gauss 变量 \(y\) 是单位。它们的和为零。这证明了方程  [\[eq:local-scalar-values\]](#eq:local-scalar-values)，包括 Gauss 特征为主特征且按零延拓的情形。

对原始单位，记 \(h_p=H/p^{j'}\)、\(s_p=s/p^k\)，以及 \(A_p^\circ=A/p^t\)。中国剩余定理与代换 \(d=h_p(b_*A_p^\circ)^{-1}d'\) 给出额外的单位因子 \[\label{eq:local-unit-factor}
 U_p=\chi_p^{k-t}(h_p)\chi_p^t(s_p)
       \chi_p^{t-k}(A_p^\circ)\chi_p^{t-k}(b_*).\] 更明确地说，外层的剩余特征给出 \(\chi_p^k(h_p)\chi_p^{-k}(b_*A_p^\circ)\)，而中国 剩余因子以及 Gauss 论证的重新缩放给出 \(\chi_p^t(b_*A_p^\circ)\chi_p^{-t}(h_p/s_p)\)。它们的乘积为 方程 [\[eq:local-unit-factor\]](#eq:local-unit-factor)。由于 \(h_p=(u/p^j)(a/p^m)^6\)，故有 \(\chi_p(h_p)=\rho\)。

在 \(b_*\) 的素因子处，有 \((H-b_*Ad)/s\equiv H/s\pmod {b_*}\)。完备 Gauss 和中的 局部因子为 \(\sqrt{q_{b_*}}\tau\xi(A)\overline{\xi(H/s)}\)。 此处 \(\overline{\xi(H/s)}=\overline{\xi(u)}\xi(s)\)，因为 \(\xi(a)^6=1\)。这消去了方程 [\[eq:local-full-coefficient\]](#eq:local-full-coefficient) 中每个出现的 \(\xi\) 因子。方程 [\[eq:local-unit-factor\]](#eq:local-unit-factor) 中最后几个因子的乘积消去了 \(\chi_s(b_*)\chi_A(b_*)^{-1}\)。此相消是逐系数的。 对 \(S\) 的任一固定扩大，同样的计算使用同一个射线群 \(T\)。

###### 剩余配对相位的相消。

令 \(t_p=v_p(A)\)、\(k_p=v_p(s)\)，在每个不同的素数对上，互反律给出 \[\mathcal R(A,s)\prod_p
       \chi_p^{t_p}(s_p)\chi_p^{-k_p}(A_p^\circ)
       =\prod_p\mathcal R(p,p)^{t_pk_p}.\] 事实上，对 \(p\ne r\)，两种定向具有相反的符号指数，其商为 \(\mathcal R(p,r)\)；这消去了双特征 \(\mathcal R(A,s)\) 中对应的配对。只剩其对角部分。

方程 [\[eq:signal\]](#eq:signal) 给出 \(\gamma_2(c)=\mu(c)\alpha(c)G(c)/\gamma_1(c)\)。中国剩余公式 \[\gamma_1(c)=\prod_{p\mid c}\gamma_1(p)
             \prod_{p<r,\ p,r\mid c}\chi_p(r)\chi_r(p)\] 消去了剩余配对乘积的无平方因子部分。若 \(e_p=v_p(c)\) 与 \(l_p=v_p(n)\)， 它在配对 \(p<r\) 处的指数为 \(t_pt_r-e_pe_r=3(e_pl_r+e_rl_p+3l_pl_r)\)。\(\chi_p(r)\chi_r(p)\) 的立方为 \(\mathcal R(p,r)\)，其平方为一。因此，此除法之后剩余的配对乘积为 \[\prod_{p<r}\mathcal R(p,r)^{e_pl_r+e_rl_p+l_pl_r}
 =\mathcal R(c,n)G(n^3)
   \prod_p\overline{G(p^3)}^{\,l_p}
            \mathcal R(p,p)^{-e_pl_p-l_p(l_p-1)/2}.\] 该等式通过对 \(n^3\) 的素因子展开二次精细化 方程 [\[eq:G-quadratic-refinement\]](#eq:G-quadratic-refinement) 而得。同一精细化给出 \(G(c)\mathcal R(c,n)G(n^3)=G(cn^3)\)，它被插入的 \(\overline{G(cn^3)}\) 消去。最后，方程 [\[eq:fixed-gauss-phases\]](#eq:fixed-gauss-phases) 给出 \(G(p^3)=\gamma_3(p)\) 与 \(\mathcal R(p,p)=\omega_p\)。 这些恒等式解释了所有的配对相位，对 \(p\) 的射线类无任何限制。

因此，方程 [\[eq:local-full-coefficient\]](#eq:local-full-coefficient) 中的系数已分离为素因子。 在绝对收敛下，它在 \(p\) 处的因子是级数 \[\label{eq:local-P}
\begin{aligned}
 P_p={}&\sum_{\substack{e_0=0,1\\l,k,m\ge0}}
 (-1)^{e_0}\gamma_1^{-e_0}\eta(p)^{e_0}
 (a_p\overline{\gamma_3})^l\rho^{k-t}
 \omega_p^{tk-e_0l-l(l-1)/2}C_p(t,k,j+6m)\\
 &\hspace{33mm}\cdot
 Q^{-(x+1/2)e_0-(1+3x)l-wk-6zm},\qquad t=e_0+3l.
\end{aligned}\] 令 \(P_p^*\) 为限制到 \(t>0\)（等价地，完备化指标 \(A\) 的正赋值）的同一和。

<span id="lem:local-euler" label="lem:local-euler">\[lem:local-euler\]</span> 对每个满足 \((u,S)=1\) 的非零无六次幂因子 \(u\) 以及每个 素数 \(p\notin S\)，刚刚定义的因子为 \[\label{old-eq:5.13a}
\begin{aligned}
 P_p^*&=\frac1{1-R}\left\{
 \frac{R(1-Q^{-1})-\eta(p)(Q-1)
 Q^{-x-w}V^{1_{j\le1}}}{1-V}+J_j\right\},\\
 P_p&=\frac1{1-V}+1_{j=0}\frac{W_{\rm loc}}{1-W_{\rm loc}}+P_p^*,
\end{aligned}\] 其中 \(J_j\) 的六个值为 \[\begin{array}{c|l}
 j&J_j\\\hline
 0&-\eta(p)\rho^{-1}Q^{-x}+W_{\rm loc}R\\
 1&\eta(p)Q^{-x-w}\\
 2&a_p\rho^{-3}Q^{3/2-3x}\\
 3&-\eta(p)b_p\rho^{-2}Q^{2-3x-w}
       +b_p^2\rho^{-4}Q^{2-4x}\\
 4&-\eta(p)a_p\rho^{-3}Q^{5/2-4x-w}\\
 5&-a_p^2Q^{3-6x}.
\end{array}\] 令 \(W=\chi_p(u)Q^{-w}\) 与 \(D=\eta(p)\overline{\chi_p(u)}Q^{-x}\)，并在 \(p\mid u\) 处采用原始的零延拓，定义 \[\label{eq:local-H-definition}
 H_p=P_p\frac{(1-V)(1-W)}{1-D},\qquad
 \mathcal H_{\eta,u}=\prod_{p\notin S}H_p.\] 则方程 [\[eq:local-full-series\]](#eq:local-full-series) 中的级数具有标量分解 \[\label{eq:probe-high}
 \mathcal F_{\eta,u}(x,w,z)=
 \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
 {L^S(x,\eta\overline{\chi_\bullet(u)})}
 \mathcal H_{\eta,u}(x,w,z).\] 记 \(x_r=\Re x\)、\(w_r=\Re w\)、\(z_r=\Re z\)。对每个 固定的 \(\epsilon_0>0\)，修正乘积在下述每个区域中每一点的 邻域上正规收敛，因而在那里定义一个全纯函数： \[\begin{aligned}
 x_r\ge51/100,\quad z_r\ge17/50,\quad w_r\ge-1/100,\quad
 x_r+w_r\ge1+\epsilon_0;\label{eq:local-region-one}\\
 x_r\ge7/8,\quad z_r\ge33/200,\quad w_r\ge19/20.
 \label{eq:local-region-two}\end{aligned}\] 关于虚部与单位相位一致地，\(\mathcal H_{\eta,u}\ll_\epsilon q_u^\epsilon\)， 其中常数在第一区域还依赖于 \(\epsilon_0\)。对第二区域中的 \(u=1\)， \(\mathcal H_{\eta,1}=1+O(P_0^{-c_H})\)，例如 \(c_H=4/5\)。 方程 [\[eq:probe-high\]](#eq:probe-high) 始于绝对收敛，并提供穿过这些区域的亚纯延拓。

第一区域将包含非主行的带缓冲围道，包括反射分子线。 第二区域包含主留数点 \(w=1\)、\(z=1/6\) 以及用于到达它的围道。

有四个 \(t>0\) 的族： \((e_0,l)=(0,2r+2),(1,2r),(0,2r+1),(1,2r+1)\)，其中 \(r\ge0\)。 在每个族中，将 \(r\) 增加一、并将第一个允许的 \(m\) 增加一，会使 方程 [\[eq:local-P\]](#eq:local-P) 的被加项乘以 \(R\)。事实上相位比为 \(a_p^2\)： 由于 \(\gamma_3^2=\omega_p\)、\(\omega_p^2=1\)、\(\rho^6=1\)，剩余的比为 1。 进一步增大 \(m\) 会使被加项乘以 \(V\)。

为清晰起见，下表列出除以 \(R^r\) 之后的每个非零被加项。 在其第一行中 \(j\) 任意；其余条件均如表所示。 每个被省略的情形都由方程 [\[eq:local-scalar-values\]](#eq:local-scalar-values) 为零。 \[\label{eq:local-family-table}
\begin{array}{c|c|l|l}
 (e_0,l)&k&\text{condition on }(j,m)&R^{-r}\text{ times summand}\\\hline
 (0,2r+2)&0&m\ge r+1&R(1-Q^{-1})V^{m-r-1}\\
 (0,2r+2)&0&j=5,\ m=r&-a_p^2Q^{3-6x}\\
 (0,2r+2)&1&j=0,\ m=r+1&W_{\rm loc}R\\
 (1,2r)&0&j=0,\ m=r&-\eta(p)\rho^{-1}Q^{-x}\\
 (1,2r)&1&j=1,\ m=r&\eta(p)Q^{-x-w}\\
 (1,2r)&1&m\ge r+1_{j\le1}&-\eta(p)(Q-1)Q^{-x-w}V^{m-r}\\
 (0,2r+1)&0&j=2,\ m=r&a_p\rho^{-3}Q^{3/2-3x}\\
 (0,2r+1)&1&j=3,\ m=r&-\eta(p)b_p\rho^{-2}Q^{2-3x-w}\\
 (1,2r+1)&0&j=3,\ m=r&b_p^2\rho^{-4}Q^{2-4x}\\
 (1,2r+1)&1&j=4,\ m=r&-\eta(p)a_p\rho^{-3}Q^{5/2-4x-w}.
\end{array}\] 这里对其各项作直接验证。在第一个族中 \(t=6r+6\)。 对 \(k=0\)，当 \(m\ge r+1\) 时主 Gauss 提升为 \(Q^t(1-Q^{-1})\)； 其在 \((j,m)=(5,r)\) 处的额外边界值为 \(-Q^{t-1}\)。对 \(k=1\)， 乘积 \(\omega_p^{-1}G_1G_{-1}=Q\) 只允许 \((j,m)=(0,r+1)\)。 这些给出前三行。在第二个族中 \(t=6r+1\)。 对 \(k=0\)，非主等式 \(j'=t-1\) 给出第四行。 对 \(k=1\)，主 Gauss 提升在 \(j'=t\) 处有其负边界，给出第五行， 而其在 \(j'>t\) 处的值 \(Q^{t-1}(Q-1)\) 给出第六行。 后一条件恰好是 \(m\ge r+1_{j\le1}\)。

对于两个奇族 \(t=6r+3\) 与 \(t=6r+4\)。其 \(k=0\) 行要求 \(j'=t-1\)， 其 \(k=1\) 行要求 \(j'=t\)。相位化简为 \[\gamma_1\gamma_2
       =-\alpha(p)\overline{\chi_p(4)}\gamma_3,
 \qquad
 \frac{\gamma_4}{\gamma_1}
       =-\frac{\overline{\alpha(p)}}{G(p)}.\] 第一式是 \(p\) 处的方程 [\[eq:signal\]](#eq:signal)；第二式由第一式与 \(\gamma_2\gamma_4=1\) 推出。代入给出最后四行，包括两个 \(j=3\) 项。 因此该表覆盖了所有五个分歧赋值以及 \(j=0\)。

对 \(r\ge0\) 求和给出 \((1-R)^{-1}\)，两个无界的 \(m\) 范围给出 \((1-V)^{-1}\)。这些和正是方程 [\[old-eq:5.13a\]](#old-eq:5.13a) 中 \(P_p^*\) 的公式。 若 \(t=0\)，则 \(e_0=l=0\)。\(k=0\) 的项给出 \((1-V)^{-1}\)， 而 \(k>0\) 的项要求 \(j=m=0\) 并给出 \(W_{\rm loc}/(1-W_{\rm loc})\)。 这同时证明了 \(P_p\) 的公式。

尚需验证这些解析断言，尤其是在 \(w_r\) 为负处。 令 \(\mathcal E_p=P_p^*+D\)。\(t=0\) 的贡献为 \((1-V)^{-1}+W/(1-W)\)， 因此精确化简给出 \[\label{eq:local-H-defect}
 H_p-1=
 \frac{D(V+W-VW)-VW+(1-V)(1-W)\mathcal E_p}{1-D}.\] 此表达式没有 \(1-W\) 分母。在 \(p\mid u\) 处，\(D=W=0\)， 它化简为 \((1-V)\mathcal E_p\)。在两个所述区域中 \(|R|<1\)、\(|V|<1\)、 \(|D|<1\)，一致地远离一，因此这些是全纯的局部表达式。

对 \(p\nmid u\) 且 \(\vartheta=(-w_r)_+\)，\(j=0\) 行给出 \[|\mathcal E_p|\ll
 Q^{4-6x_r-6z_r+\vartheta}+Q^{1-x_r-w_r-6z_r}.\] 在第一区域中 \(4-6x_r-6z_r\le-11/10\) 且 \(\vartheta\le1/100\)。 因此方程 [\[eq:local-H-defect\]](#eq:local-H-defect) 中额外的因子 \(1-W\) 使此贡献 至多为 \(Q^{-27/25}\)。项 \(DW\) 至多为 \(Q^{-1-\epsilon_0}\)； 该方程中其他项更小。对 \(p\mid u\)，严格的第二族项的指数为 \(1-x_r-w_r\le-\epsilon_0\)。表中其他最接近的指数为 \[3/2-3x_r\le-3/100,\qquad
 2-3x_r-w_r\le-1/50-\epsilon_0,\] 其余所有指数均不大于 \(-3/100\)。 因此，令 \(\epsilon_H=\min(\epsilon_0,1/50)\)， \[H_p-1=O(Q^{-1-\epsilon_H})\quad(p\nmid u),\qquad
 H_p-1=O(Q^{-\epsilon_H})\quad(p\mid u).\] 在第二区域中，同样的比较给出更强的界 \[H_p-1=O(Q^{-363/200})\quad(p\nmid u),\qquad
 H_p-1=O(Q^{-33/40})\quad(p\mid u).\] 此处最接近的好素数项为 \(Q^{1-x_r-w_r-6z_r}\)， 最接近的分歧项为 \(Q^{1-x_r-w_r}\)。

对不整除 \(u\) 的素数的和正规收敛，而对 \(u\) 的素数取有限乘积 由除子乘积界为 \(O_\epsilon(q_u^\epsilon)\)。这些估计对所有虚部与 单位相位一致。当 \(u=1\) 时，超出 \(P_0\) 的好素数尾部由理想计数为 \(O(P_0^{-163/200})\)，这蕴含了所断言的乘积估计 \(O(P_0^{-4/5})\)。 最后，在每个素数处提取 \((1-V)^{-1}(1-W)^{-1}(1-D)\) 便给出 方程 [\[eq:probe-high\]](#eq:probe-high)。剩余乘积的正规收敛证明了其所断言的延拓。

对 \(u=1\)，方程 [\[eq:probe-high\]](#eq:probe-high) 包含 \(1/L^S(x,\eta)\)， 其分子含有两个主因子 \(\zeta_F^S(6z)\) 与 \(\zeta_F^S(w)\)。 它们的留数将产生目标 Mellin 信号。对于中间行范数， 下一节为与每一行相关联的有限特征族指定一个无零点矩形， 并从选定的零点产生同时多项式见证。主行与有界行以及外部范数区间 在节 [8](#sec:shared-analytic-estimates) 中处理。

### 带饱和见证的零点探测器

高展开包含一个对无六次幂因子的行 \(u\) 的求和。 我们把每个非主行与其所确定的有限特征表示族的一个带缓冲的 无零点矩形相关联。只要所得到的分箱位于固定下界之上， 一个零点便产生一个逆多项式与一个普通多项式，且二者具有同时下界。 这些见证随后可用不同的均值估计来计数。此处的解析输入为 引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control)、引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 的光滑演算、方程 [\[eq:hecke-growth\]](#eq:hecke-growth) 中的全局增长估计， 以及引理 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors) 的删去 Euler 因子界。

在本节中，始终假设 \(\beta_*>51/100\)，其中 \(\beta_*\) 是方程 [\[old-eq:1.1b\]](#old-eq:1.1b) 中的全局上确界。 此设定不选出延拓判据中两个边界中的任何一个。

#### 带缓冲的矩形与逐点界

如节 [2](#sec:arithmetic) 那样，独立于 \(Z\) 固定算术数据 \(\mathcal A\)。特别地，有限群 \[\Theta=\langle\eta,\widehat T\rangle\] 包含目标以及在高行族中使用的固定射线扭曲，且 \(\Theta\) 中 每个元素的每个导子素数都属于 \(S\)。对无六次幂因子的元素 \(u\)， 定义有限表示集合 \[\mathcal X_u=
 \bigl\{\psi_{u,\nu,\varsigma}(n)=\nu(n)\chi_n(u)^\varsigma:
       \nu\in\Theta,\ \varsigma\in\{-1,1\}\bigr\}.\] 在非单位处，\(\chi_n(u)^{-1}\) 的值，如同符号的每个其他幂一样， 为零。\(\Theta\) 的群性质表明 \(\mathcal X_u\) 在共轭下封闭。 它包含分子特征 \(\chi_\bullet(u)\)、分母特征 \(\eta\overline{\chi_\bullet(u)}\)，以及通过将六次符号的 任一方向定向乘以 \(\Theta\) 中某个元素而得到的每个零延拓表示。

令 \(\psi^*\) 为诱导表示 \(\psi\in\mathcal X_u\) 的本原特征， 令 \(Q_\psi\) 为其导子范数。互反律与固定的导子素数给出 \[Q_\psi\ll_{\mathcal A}q_u,\qquad
 L_{\rm orig}(s,\psi)
   =L(s,\psi^*)\prod_{p\in E_u}(1-\psi^*(p)q_p^{-s}),
 \qquad
 E_u\subset S\cup\{p:p\mid u\}.\] 删去乘积的根基具有范数 \(O_S(q_u)\)。 这些恒等式保留了原始的零延拓；特别地，它们不会把依赖于行的掩码 替换为独立选取的掩码。

<span id="par:physical-row-ramification" label="par:physical-row-ramification">\[par:physical-row-ramification\]</span> 若在素数 \(p\notin S\) 处 \(v_p(u)=j\in\{1,\ldots,5\}\)， 则 \(\chi_\bullet(u)\) 在 \(p\) 处单位上的局部特征阶为 \(6/\gcd(6,j)>1\)。\(\Theta\) 中的特征在该处是非分歧的， 因此无法消去此局部特征。因此，\(\mathcal X_u\) 中的一个表示 只有在 \(u\) 的支集位于 \(S\) 上时才能诱导主特征。 这样的无六次幂因子的行只有有限多个，包括单位因子。 对当前探测器将其移除；每个应用都必须单独估计这些有界的物理行。

固定 \(0<d_{\min}<d_{\max}<\infty\)，记 \(U=Z^d\)，其中 \(d_{\min}\le d\le d_{\max}\)。当前二元组中的行满足 \(q_u\asymp U\)， 比较常数固定。令 \[0<\tau\le d_{\min}/100,\qquad T_1=Z^\tau>2,\qquad
 0<e<10^{-3},\qquad I=\lceil1/e\rceil+2.\] \(\tau\) 的取值将在已知固定高度阶数之后选定。目前它独立于 \(Z\) 固定。 特别地 \(T_1\le U^{1/100}\)。

<span id="lem:buffered-bins" label="lem:buffered-bins">\[lem:buffered-bins\]</span> 对每个保留的行 \(u\)，存在一个指标 \(i\in\{1,\ldots,I-1\}\) 与一个格点 \[a\in(51/100+e\mathbb Z_{\ge0})\cap[51/100,1]\] 具有下述性质。对 \(j=1,\ldots,I\)，令 \[M_j(u)=\max\left(\{51/100\}\cup
 \left\{\Re\rho:
 \begin{array}{l}
  \psi\in\mathcal X_u,\quad L(\rho,\psi^*)=0,\\
  \Re\rho\ge51/100,\quad |\Im\rho|\le3jT_1
 \end{array}\right\}\right).\] 则 \[a\le M_i(u)<a+e,\qquad M_{i+1}(u)<a+2e.\] 若 \(a>51/100\)，则某个 \(\psi\in\mathcal X_u\) 有一个零点 \(\rho=\sigma+i\gamma\)，满足 \[a\le\sigma<a+e,\qquad |\gamma|\le3iT_1.\] 对每个 \(\epsilon_1>0\)、每个 \(\psi\in\mathcal X_u\) 以及 充分大的 \(Z\)，关于保留的行一致地， \[|L_{\rm orig}(s,\psi)|+|L_{\rm orig}(s,\psi)^{-1}|
 \ll_{\mathcal A,e,\epsilon_1} U^{\epsilon_1}
 \quad
 \left(\Re s\ge a+6e,\ |\Im s|\le(3i+2)T_1\right).\] 在同一高度范围内的反射线上， \[|L_{\rm orig}(1-a-6e+it,\psi)|
 \ll_{\mathcal A,e,\epsilon_1}
 U^{a-1/2+12e+\epsilon_1}(3+T_1)^C,\] 其中 \(C\) 只依赖于固定的实带形域与域。 可能的配对 \((i,a)\) 有 \(O_e(1)\) 个，独立于该行及其导子。

每个最大值都存在：集合有限，每个非主本原 \(L\) 函数的零点 在紧矩形中离散，且绝对 Euler 收敛排除了实部大于一的零点。 序列 \(M_j(u)\) 单调不减且位于 \([51/100,1]\) 中。若其 \(I-1\) 个增量中的每一个都超过 \(e\)，则 \[M_I(u)-M_1(u)>(I-1)e>1,\] 这是不可能的。选取一个满足 \(M_{i+1}(u)-M_i(u)\le e\) 的指标， 并将 \(M_i(u)\) 在所给格点上向下取整。这给出两个不等式。 当 \(a>51/100\) 时，最大值 \(M_i(u)\) 由某个实际零点达到， 给出 \(\rho\)。此推理允许零点位于直线一上。

对 \(|t|\le(3i+2)T_1\)，以 \(2+it\) 为中心、半径为 \(2-a-2e\) 的闭圆盘具有至少 \(a+2e\) 的实部。其半径小于 \(3/2<T_1\)， 因此其中每一点的虚部绝对值小于 \(3(i+1)T_1\)。 因此界 \(M_{i+1}(u)<a+2e\) 排除了此圆盘中每个本原函数的每个零点。 引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control) 控制半径为 \(2-a-6e\) 的同心圆盘。 以中心 \(2+i\Im s\) 应用它，并在更右处使用绝对 Euler 收敛。 由于 \(Q_\psi\ll_{\mathcal A}U\) 且 \((3+|t|)^2\ll_e U^{1/50}\)， 该引理中任意小的幂可取为使其余贡献为 \(U^{\epsilon_1/2}\)。 该引理之后关于多项式大小删去 Euler 乘积的估计提供另一个 \(U^{\epsilon_1/2}\)。

对于最后的断言，引理 [\[lem:hecke-strip-growth\]](#lem:hecke-strip-growth) 的证明中 回顾的本原函数方程  将 \(1-a-6e+it\) 处的值与 \(a+6e-it\) 处的共轭本原函数相关联。 共轭表示属于 \(\mathcal X_u\)。导子与 gamma 商至多贡献 \[Q_\psi^{a-1/2+6e}(3+|t|)^C.\] 由前面的圆盘界，反射本原值具有任意小的 \(U\)-幂。 最后，\(1-a-6e\ge-6e\)，因此在减少初步损失之后， 删去乘积的上界为 \(U^{6e+\epsilon_1}\)。这证明了反射估计。 \(i\) 与 \(a\) 的取值范围给出 \(O_e(1)\) 个配对。

我们称 \((i,a)\) 为该行的分箱，并令 \[\delta=2a-1,\qquad 1/50\le\delta\le1.\] 诱导 \(\mathcal X_u\) 中某个表示的每个本原特征都是有限阶 Hecke 特征。 \(\beta_*\) 的定义连同 \(\beta_*>51/100\) 因此给出 \(M_i(u)\le\beta_*\)。特别地，该分箱满足精确不等式 \[a\le\beta_*,\qquad \delta\le2\beta_*-1.\] 分箱 \(a=51/100\) 将由平凡行计数来界定。对 \(a>51/100\)， 引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 中的零点产生大的多项式， 可对其应用矩。

<span id="lem:detector-dyads" label="lem:detector-dyads">\[lem:detector-dyads\]</span> 固定 \(r,m\) 的有界非负区间，并令 \[M_r=M_\psi(r;W_M),\qquad S_m=S_\psi(m;W_S)\] 表示方程 [\[old-eq:1.1a\]](#old-eq:1.1a) 与 [\[old-eq:1.1\]](#old-eq:1.1) 中的多项式， 现在取基 \(U\)。设 \(\psi\in\mathcal X_u\)，非扭曲剖面在固定圆环上 有有界光滑半范数，且任何纯范数扭曲的高度至多为 \((3i+1)T_1\)。 进入同一 \(L\) 论证的所有额外 Mellin 频率要求其总绝对值至多为 \(T_1/2\)。

对每个 \(\epsilon>0\)，存在 \(e_0>0\)（只依赖于 \(\epsilon\) 与有界长度区间）以及一个有限高度阶 \(A_{\mathcal A}\) （关于变动的行与剖面一致），使得当 \[0<e<e_0,\qquad (1+T_1)^{A_{\mathcal A}}\le U^{\epsilon/10},\] 下述估计对充分大的 \(Z\) 成立： \[|M_r|^2\ll_{\mathcal A,\epsilon}U^{\delta r+\epsilon},
 \label{old-eq:6.2}\] \[|S_m|^2\ll_{\mathcal A,\epsilon}
       U^{\delta\min(m,1-m)+\epsilon}.
 \label{old-eq:6.3}\] 外部尾部阶可在正数 \(\tau\) 之后选取。它不改变 \(A_{\mathcal A}\)。

我们详细说明高度限制，因为完整的无限围道移动不能由该分箱 来证明其合理性。对固定的圆环 \(W\)、有界实数 \(\sigma\) 以及纯扭曲 \(y^{i\omega}\)，在直线 \(c+\sigma>1\) 上的 Mellin 反演给出 \[\begin{split}
 &U^{-r/2}\sum_n\mu(n)\psi(n)
       W(q_n/U^r)(q_n/U^r)^{-\sigma+i\omega}\\
 &\quad=\frac1{2\pi i}\int_{(c)}
  \mathcal MW(s)\,
  U^{r(s+\sigma-i\omega-1/2)}
  L_{\rm orig}(s+\sigma-i\omega,\psi)^{-1}\,ds.
 \end{split}\] 此处 \(\mathcal MW\) 是引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中定义的 Mellin 变换。该扭曲出现在 \(L\) 论证中，而不出现在估计其尾部的 变换中。只将附加频率至多为 \(T_1\) 的指定份额的那部分移动到 \(\Re(s+\sigma)=a+6e\)。水平连接段与移动的部分保持在 引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 的无零点矩形中。 其界给出中心部分的 \(U^{(a-1/2+6e)r+\epsilon_1}\)。

把剩余的尾部留在绝对线上，我们可以取之为 \(\Re(s+\sigma)=2\)。在那里倒数 Euler 乘积绝对有界。 在反向连接段上，倒数仍位于带缓冲的矩形内。 由于实连接区间与长度区间有界，连接段上剩余的算术与尺度因子为 \(O(U^B(1+|\Im s|)^J)\)，其中固定 \(B,J\) 在外部尾部阶之前选取。 方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 中的逐点 Mellin 界， 以导数阶 \(N+\lceil J\rceil+1\) 应用于该紧实区间， 将每个水平连接段界为 \(O(U^B T_1^{-N})\)。 单独的竖直尾部由方程 [\[eq:late-fourier-tail\]](#eq:late-fourier-tail) 具有相同的界。 两个估计都适用于非扭曲剖面，关于所述族一致。 由于 \(T_1=Z^\tau\)、\(\tau>0\)，且所有长度都位于固定的有界区间内， 充分大的固定 \(N\) 使这些误差小于所断言的界。 在规定的 \(\epsilon\) 下取 \(e\) 与 \(\epsilon_1\) 足够小， 便证明了方程 [\[old-eq:6.2\]](#old-eq:6.2)。

对普通多项式，同样的计算使用 \(L_{\rm orig}\) 而非其倒数。 移动至 \(\Re(s+\sigma)=a+6e\) 给出 \[|S_m|\ll U^{(a-1/2+6e)m+\epsilon_1}
          +O(U^B T_1^{-N}).\] 或者将其中心部分移动至 \(\Re(s+\sigma)=1-a-6e\)。 该函数为整函数，因为该行是非主的。引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 的反射估计给出 \[|S_m|\ll
 U^{a-1/2+12e+\epsilon_1}
 U^{(1/2-a-6e)m}(3+T_1)^C
 +O(U^B T_1^{-N}).\] 此处的连接段只需要全局上带形域界以及删去乘积的负带形域界， 因为不存在倒数。它们给出如上固定的 \(B,J\)，因此逐点 Mellin 估计 界定连接段，积分 Fourier 估计界定绝对线尾部。 取更好的中心界，选取 \(N\) 也去支配当 \(m>1\) 时可能为负的指数， 并使用所示的高度假设，便证明了方程 [\[old-eq:6.3\]](#old-eq:6.3)。 小于 \(U\) 的本原导子会减小反射导子因子。 原始的删去 Euler 因子已经包含在引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 中。

在任何单个 \(L\)-自变量中，分离变量只有有限多个。给每个变量分配 \(T_1/2\) 这一单项配额中的一个固定份额；不要在相继的移位处重新分配该配额。行估计中所用的剖面窗口与有限高度阶都在 \(N\) 之前固定。引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 在增大 \(N\) 时只对未扭变的分离剖面求导，这便证明了最后的断言。

#### 同时的饱和见证

在一个选定的零点处，下面的截断逆构造产生一个乘积，其平方大小至少为 \(U^{\delta(r+m)-\epsilon}\)。 逐点估计将同一乘积界为 \(U^{\delta(r+\min(m,1-m))+\epsilon}\)。由于 \(\delta\ge1/50\)， 这两个界迫使 \(m\le1/2+O(\epsilon)\)。于是每个因子都在指定的损失范围内达到其自身的逐点指数； 这就是下一命题中所断言的饱和性。

<span id="prop:detector-witness" label="prop:detector-witness">\[prop:detector-witness\]</span> 设 \(u\) 有一个分箱 \((i,a)\)，其中 \(a>51/100\)，并假设引理 [\[lem:detector-dyads\]](#lem:detector-dyads) 的损失与高度假设。 对每个 \(t\in[1,3/2]\)，以及每个指定的 \(\epsilon>0\)， 在缩减其初步损失之后，存在 \(\psi\in\mathcal X_u\)、如引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 那样的一个零点 \(\rho=\sigma+i\gamma\)、 二进长度 \(D=U^r\)、\(N=U^m\)，以及公共行特征 \(\psi\) 的两个多项式 \(M_r,S_m\)，使得 \[\label{eq:detector-note}
 r\le t+O(1/\log U),\qquad
 r+m\ge t-O(1/\log U),\qquad
 |M_rS_m|^2\gg_{\mathcal A,\epsilon}
 U^{\delta(r+m)-\epsilon}.\] 它们的长度与各自的值也满足 \[\label{eq:saturated-witness}
 \begin{gathered}
 t-\tfrac12-O(\epsilon)\le r\le t+O(1/\log U),
 \qquad 0\le m\le\tfrac12+O(\epsilon),\\
 |M_r|^2\gg_{\mathcal A,\epsilon}U^{\delta r-\epsilon},
 \qquad
 |S_m|^2\gg_{\mathcal A,\epsilon}U^{\delta m-\epsilon}.
 \end{gathered}\] 在所述参数范围内，\(O(\epsilon)\) 项中的常数是绝对的。两个多项式具有相同的扭变高度 \(\gamma-\nu\)，其中 \(|\nu|\le cT_1\)，\(c>0\) 固定且取自累积频率配额之内。 它们的未扭变剖面构成一个一致光滑的环形族。 对每一行，两个见证都使用一个表示 \(\psi_{u,\vartheta,\varsigma}\)，由一个固定的有限集合 \((\vartheta,\varsigma)\)，取自固定有限集合 \(\Theta\times\{-1,1\}\) 中的标号选取。表示本身随 \(u\) 变化。 二进对同样可以逐行地从 \(O((\log U)^2)\) 种可能性中分别选取。

截断逆与 Gamma 积分构造是经典零点探测器的一种形式；比较  与 。此处所需的带缓冲的行相关矩形与 同时下界将在下面建立。选取由该分箱给出的零点 \(\rho\)，并令 \[D_*=U^t,\qquad Y_*=U^{20}.\] 设 \(V_{\le}\) 为一个固定的光滑函数，在 \([0,1]\) 上等于一、在 \([2,\infty)\) 上等于零。定义 \[C_\psi(s)=\sum_l\mu(l)\psi(l)V_{\le}(q_l/D_*)q_l^{-s},
 \qquad
 J=\frac1{2\pi i}\int_{(2)}
       Y_*^z\Gamma(z)L_{\rm orig}(\rho+z,\psi)
       C_\psi(\rho+z)\,dz.\] 行特征是非主特征，故 \(L_{\rm orig}\) 为整函数。 将直线移至 \(\Re z=-1/4\) 只穿过 \(\Gamma(z)\) 在零处的极点，且其留数为零，因为 \(L_{\rm orig}(\rho,\psi)=0\)。方程 [\[eq:hecke-growth\]](#eq:hecke-growth) 中的全局带形界， 连同被删除的 Euler 因子，将新直线界为 \[U^{-5}U^2D_*^{\,1-\sigma+1/4+o(1)}T_1^2.\] 事实上 \(\Re(\rho-1/4)\ge26/100>0\)，故被删除的乘积具有 任意小的 \(U\)-幂；刻意取弱的 \(U^2\) 包含了本原导子界。有限 多项式利用理想计数由所示 \(D_*\) 的幂界出。最后，所加高度中的固定多项式 对 \(\Gamma(-1/4+iv)\) 可积，因为 \((1+|\gamma+v|)^2\le(1+|\gamma|)^2(1+|v|)^2\)。 对 \(1\le t\le3/2\) 一致地有 \[-3+t(5/4-\sigma)
 \le-3+\frac32\left(\frac54-\frac{51}{100}\right)
 =-\frac{189}{100}.\] 于是 \(J=o(1)\)。这一 Gamma 积分只使用全局上 界，不消耗任何倒数高度配额。

在原始直线上，绝对收敛性与指数的 Mellin 公式 给出 \[J=\sum_{l,k}\mu(l)\psi(lk)V_{\le}(q_l/D_*)
       (q_lq_k)^{-\rho}e^{-q_lq_k/Y_*}.\] 对 \(1<q_n\le D_*\)，\(\psi(n)q_n^{-\rho}\) 的系数 为 \(\sum_{l\mid n}\mu(l)=0\)。对 \(n=1\) 它为一。 当 \(q_n>D_*\) 时，\(V_{\le}(2q_n/D_*)=0\)。 因此插入 \(1-V_{\le}(2q_lq_k/D_*)\) 恰好 移除单位贡献 \(e^{-1/Y_*}=1+o(1)\)。 所得尾部具有绝对值 \(1+o(1)\)。 用这样一个固定的光滑终端截断函数乘它——该函数对 \(q_lq_k\le U^{21}\) 等于一、对 \(q_lq_k\ge2U^{21}\) 等于零——将其改变 \(o(1)\)；这由 \(Y_*=U^{20}\)、指数衰减 以及理想计数可得。

用固定的光滑二进划分将 \(q_l\asymp D\)、\(q_k\asymp N\) 划分。相关的对共有 \(O((\log U)^2)\) 个， 其支集满足 \[D\ll D_*,\qquad DN\gg D_*,\qquad DN\ll U^{21}.\] 以 \(x=q_l/D\)、\(y=q_k/N\)，一对的剖面为 \[W_1(x)V_{\le}(Dx/D_*)\,W_2(y)\,H_{D,N}(xy),\] 其中 \(\Omega\) 是一个固定的环形截断函数，在 \(W_1,W_2\) 的支集之积上等于一，且 \[H_{D,N}(s)=\Omega(s)
   [1-V_{\le}(2DNs/D_*)]e^{-DNs/Y_*}
   V_{\rm term}(DNs/U^{21}).\] 每个固定的对数导数在 \(D,N,U\) 中一致有界。在截断过渡处其自变量有界，而 指数的对数导数等于其自变量的一个多项式乘以该指数。 对数 Fourier 反演因此给出 \[\begin{split}
 H_{D,N}(xy)&=\frac1{2\pi}\int_{\mathbb R}
      \widehat H_{D,N}(\nu)x^{i\nu}y^{i\nu}\,d\nu,\\
 \int_{|\nu|>cT_1}|\widehat H_{D,N}(\nu)|
       (1+|\nu|)^J\,d\nu&\ll_{J,N_0,c}T_1^{-N_0}
 \end{split}\] 对每个固定的 \(J,N_0\)。整条直线上的系数 \(L^1\)-范数 也一致有界。两个 有限多项式的平凡界具有固定的 \(U\)-幂，因为它们的长度 被 \(U^{21+o(1)}\) 界住。在 \(\tau>0\) 固定之后，选取 \(N_0\) 使得被丢弃的 Fourier 尾部为 \(o(1)\)。

剩余积分之和的绝对值有 正的下界。二进对的数目与 一致的 \(L^1\)-范数表明，对一对以及一个 \(|\nu|\le cT_1\)，两个未正规化块之积具有 绝对值 \(\gg(\log U)^{-2}\)。两个剖面都具有 相同的高度 \(\gamma-\nu\)： \[\begin{split}
 W_M(x)&=W_1(x)V_{\le}(Dx/D_*)x^{-\sigma-i(\gamma-\nu)},\\
 W_S(y)&=W_2(y)y^{-\sigma-i(\gamma-\nu)}.
 \end{split}\] 第一个额外的截断函数仍属于逆环形剖面 且不产生第二个频率。通过中心正规化移除因子 \(D^{1/2-\sigma}\) 与 \(N^{1/2-\sigma}\) 得到 \[|M_rS_m|^2\gg(\log U)^{-4}(DN)^{2\sigma-1}
 \ge U^{\delta(r+m)-\epsilon}\] 对充分大的 \(U\)。支集不等式给出 方程 [\[eq:detector-note\]](#eq:detector-note) 中的两个长度界。

对这些剖面应用引理 [\[lem:detector-dyads\]](#lem:detector-dyads)，选取其 损失小于当前的 \(\epsilon\)。将 乘积下界与两个上界比较给出 \[\delta\{m-\min(m,1-m)\}
   =2\delta(m-1/2)_+\ll\epsilon.\] 由于 \(\delta\ge1/50\)，这蕴含 \(m\le1/2+O(\epsilon)\)，其中常数为绝对常数。 支集不等式随后给出 \(r\ge t-1/2-O(\epsilon)\)。 将乘积下界依次除以各个上 界，即得 方程 [\[eq:saturated-witness\]](#eq:saturated-witness) 中的两个各自下界。只有二进支集 误差是 \(O(1/\log U)\)；所有其他损失都是任意小的 固定幂。引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 允许所述的 逐行选择，且带有一个固定的多项式高度因子。

### 六次筛法的行计数

零点探测器为底箱之上的每一行提供一个大的逆多项式。我们现在把该下界 转化为物理行的计数。我们首先按主约定证明所需的无平方因子六次大筛法， 使用 Blomer、Goldmakher 与 Louvel  的范数递归方法。然后我们 固定一个物理行中素因子赋值至少为二的部分，并把该筛法应用于其无平方因子 因子。固定部分的大小也给出行数的一个独立上界；两个界中较好的一个给出所需的 指数。

#### 主约定下的六次大筛法

我们继续使用固定的有限素理想集合 \(S\)，它包含 \(6\) 之上的素理想以及所有固定的导子素理想。下一个引理中所有理想指标 都与 \(S\) 互素，并由其主生成元表示。特别地，“无平方因子”指的是 \(\mathcal O=\mathbb Z[\omega]\) 的理想，而非其有理范数。

<span id="lem:sextic-large-sieve" label="lem:sextic-large-sieve">\[lem:sextic-large-sieve\]</span> 设 \(K,D\ge1\)，设 \(\varsigma\in\{-1,1\}\)，并设 \((c_n)\) 为以 \(S\) 之外的无平方因子理想为指标的任意 复数列。该数列独立于行 \(k\) 而固定。对每个 \(\epsilon>0\)， \[\label{eq:sextic-large-sieve}
 \sum_{\substack{k\ {\rm sf}\\q_k\le K}}
 \left|\sum_{\substack{n\ {\rm sf}\\q_n\le D}}
       c_n\chi_n(k)^{\varsigma}\right|^2
 \ll_{S,\epsilon}(KD)^\epsilon
       \bigl\{K+D+(KD)^{2/3}\bigr\}
       \sum_{\substack{n\ {\rm sf}\\q_n\le D}}|c_n|^2.\] 本公式中的每个符号在非单位元上取原来的零值。 允许对行集合作固定的限制。允许通过对该系数列作零延拓来 限制系数支集。这样的限制可以依赖于在行和之前固定的对象， 但系数不得在其他方面依赖于 \(k\)。

我们遵循 Blomer、Goldmakher 与 Louvel  的高阶大筛法递归，为当前的 主正规化作局部验证。在有限 Fourier 计算中， 各个剩余特征作用于元素；它们的单位平凡商 就是我们把 Poisson 求和应用于其上的理想特征。

对由主生成元表示的好理想 \(a,b\)，令 \[F_b(a)=\chi_a(b),\qquad J=\{1,2,4\}.\] 这里使用的是原来的零延拓符号，即便当 \(a\) 非无平方因子时也是如此。 它在 \(a\) 与 \(b\) 中都是乘性的。在下面的每个幂中，包括六的倍数， 非单位元仍然取值为零。 对 \(M>0\) 令 \[\mathcal I_M=\{a\text{ good}:M<q_a\le2M\},\qquad
 \mathcal A_M=\{a\in\mathcal I_M:a\text{ squarefree}\}.\] 对支集在 \(\mathcal A_N\) 上的列写 \(\|\lambda\|_2^2=\sum_{b\in\mathcal A_N}|\lambda_b|^2\)，并定义 \[\begin{aligned}
 D_j(M,N)&=\sup_{\|\lambda\|_2=1}
  \sum_{a\in\mathcal A_M}
  \left|\sum_{b\in\mathcal A_N}\lambda_bF_b(a)^j\right|^2,\\
 E_j(M,N)&=\sup_{\|\lambda\|_2=1}
  \sum_{a\in\mathcal I_M}
  \left|\sum_{b\in\mathcal A_N}\lambda_bF_b(a)^j\right|^2.\end{aligned}\] 空支集给出范数零。这些范数包含所有有限射线 类。我们将为 \(D_1\) 证明对称界；引理中的矩阵是它的转置， 且两个长度互换。

无平方因子范数 \(D_j\) 是我们的目标。我们还需要 \(E_j\)，因为 Poisson 求和会产生任意的求值理想。在其定义和中展开平方 并对列特征配对，将把行长 \(M\) 替换为一个阶为 \(N^2/M\) 的对偶 长度。然后幂分解把无限制的行和重新化为无平方因子范数。 它选取一次幂或二次幂因子，因此指数 \(j\in\{1,2,4\}\) 被保持在一起： 该集合在 \(j\mapsto2j\pmod6\) 下封闭。我们将利用这一循环来 改进 \(D_j\) 界中的一个临时指数。

*配对求和公式。* 使用固定的有限群 \[\mathcal T=\ker\bigl((\mathcal O/36\mathcal O)^\times
              \longrightarrow(\mathcal O/3\mathcal O)^\times\bigr),
 \qquad t(b)=b\bmod36\mathcal O.\] 主正规化将它们与模 \(36\mathcal O\) 的射线类等同起来：每个单位轨道都有一个模 \(3\) 等于一的 唯一代表。特别地 \(t\) 是乘性的。这一细分 是固定的，因为 \(2\) 与 \(3\) 之上的素理想属于 \(S\)。

对全局单位 \(u\) 与好素理想 \(p\)，模 \(p\) 的约化给出 \(\chi_p(u)=u^{(q_p-1)/6}\)。由于 \(q_p\equiv1\pmod6\)，对 \(b\) 的素因子相乘给出 \[\label{eq:sextic-sieve-unit-class}
 \chi_b(u)=u^{(q_b-1)/6}.\] 指数按模六来读：展开整数 \(1+6h\) 的乘积即证明指数的相等。因此相等的 \(t\)-类在 六个全局单位上具有相同的限制。它们也具有相同的模 \(4\) 剩余，这控制着引理 [\[lem:fixed-gauss-phase\]](#lem:fixed-gauss-phase) 的互反因子 \(\mathcal R\)。

设 \(b,c\) 为互素的无平方因子好理想，满足 \(t(b)=t(c)\)，并设 \(j\in J\)。元素上的原始特征 \[\Theta_{b,c}^{(j)}(z)=\chi_b(z)^j\overline{\chi_c(z)^j}
       \quad (z\bmod bc)\] 由方程 [\[eq:sextic-sieve-unit-class\]](#eq:sextic-sieve-unit-class) 在全局单位上平凡。 因此它通过 \[\Psi_{b,c}^{(j)}((z))=\Theta_{b,c}^{(j)}(z).\] 在理想上定义一个有限阶射线特征。 对与 \(bc\) 互素的分数理想，剩余符号在局部单位分数上求值； 同样的单位相消使该定义与生成元无关。在每个好素理想处，六次剩余 特征具有恰好为六的阶，因为剩余乘法群是 循环的。因此其幂 \(j\) 与 \(-j\) 非平凡。CRT 表明 \(\Theta_{b,c}^{(j)}\) 具有原始导子 \(bc\)，且该射线特征具有 相同的导子：略去一个素理想将会仅变化其剩余从而与这一非平凡性矛盾。 它在与 \(bc\) 相交的理想上作零延拓。 对 \(b=c=1\) 的一对，定义 \(\Psi_{1,1}^{(j)}\) 为主特征。

六次互反律，其因子由 \(t(b)=t(c)\) 固定，对每个 好理想 \(a\) 给出 \[\label{eq:sextic-sieve-pair-values}
 \Psi_{b,c}^{(j)}(a)=F_b(a)^j\overline{F_c(a)^j}.\] 对互素的输入两个互反因子相消；在其他输入上 两边均为零。利用算术预备中已定义的 Gauss 和，使用 \(z=cv+bw\) 的 CRT 给出 \[\label{eq:sextic-sieve-pair-gauss}
 \begin{split}
 \Gamma_{b,c}^{(j)}
 &:=q_{bc}^{-1/2}\sum_{z\bmod bc}\Theta_{b,c}^{(j)}(z)e(z/(bc))\\
 &=\chi_b(c)^j\overline{\chi_c(b)^j}\gamma_j(b)\gamma_{-j}(c)
  =\eta_{t(b),j}\gamma_j(b)\gamma_{-j}(c),
 \end{split}\] 其中 \(\eta_{t(b),j}=\mathcal R(b,c)^j\) 只依赖于公共类。 这里每个 \(\gamma_{\pm j}\) 由素 Gauss 正交性与 CRT 具有模一。 公式 [\[eq:sextic-sieve-pair-gauss\]](#eq:sextic-sieve-pair-gauss) 保留了 \(\gamma_{-j}\) 本身，包括它在共轭下 \(-1\) 处的因子。

固定选取一个非负的 \(W\in C_c^\infty((0,\infty))\)，满足在 \([1,2]\) 上 \(W\ge1\)。对算术预备中的 Fourier 变换与自对偶测度， 令 \(w(z)=W(|z|^2)\) 并通过 \[\widehat w(y)=\mathscr W(|y|^2).\] 定义 \(\mathscr W\)。 该变换是径向的、在零处光滑且快速递减。于是 \[\label{eq:sextic-sieve-transform-bounds}
 \mathscr W(x)\ll_A(1+x)^{-A},\qquad
 \int_{\mathbb R}|\mathcal M\mathscr W(\sigma+it)|\,dt<\infty
       \quad(\sigma>0).\] 这里 \(\mathcal M\) 表示 Mellin 变换。第二个断言 由 Mellin 积分中的分部积分得到；所有对数 导数在零处有界、在无穷处快速 递减。对 Fourier 变换作伸缩，\(z\mapsto W(|z|^2/M)\) 给出 \(M\mathscr W(M|y|^2)\)。

对 \(bc\ne1\)，本原原始特征的有限 Fourier 反演为 \[\sum_{v\bmod bc}\Theta_{b,c}^{(j)}(v)e(vy/(bc))
 =\overline{\Theta_{b,c}^{(j)}(y)}\sqrt{q_{bc}}\,
       \Gamma_{b,c}^{(j)}.\] 对非单位元 \(y\)，左边为零，因为一个非平凡的局部 特征被对平凡的加性特征求和。对所给的 \(e\) 与 \(d\mu\)，基 \((1,\omega)\) 上的迹配对具有矩阵 \(\left(\begin{smallmatrix}0&1\\1&-1\end{smallmatrix}\right)\)，行列式为 \(-1\)，且 \(\mathcal O\) 的 \(d\mu\)-余体积为一。于是 \(bc\mathcal O\) 的对偶为 \((bc)^{-1}\mathcal O\)，而 \(bc\mathcal O\) 的余体积为 \(q_{bc}\)。 陪集 Poisson 求和，随后除以每个理想的六个生成元， 因此给出 \[\label{eq:sextic-sieve-pair-poisson}
 \sum_{\mathfrak a\ne0}W(q_{\mathfrak a}/M)\Psi_{b,c}^{(j)}(\mathfrak a)
 =\frac{M\Gamma_{b,c}^{(j)}}{\sqrt{q_{bc}}}
   \sum_{\mathfrak a\ne0}\mathscr W(Mq_{\mathfrak a}/q_{bc})
                 \overline{\Psi_{b,c}^{(j)}(\mathfrak a)}.\] 这里两个和都在所有非零整理想上取。除以六 利用了 \(\Theta_{b,c}^{(j)}\) 的单位平凡性与权重的径向性。 零频率消失，因为该特征非平凡。

*平方范数的 Poisson 变换。* 对支集在 \(\mathcal A_N\) 中一个 \(t\)-类上的 \(\lambda\)，令 \[Q_j(M,N;\lambda)=
 \sum_{\substack{b,c\in\mathcal A_N\\(b,c)=1}}
   \lambda_b\overline{\lambda_c}
   \sum_{\mathfrak a\ne0}W(q_{\mathfrak a}/M)
                         \Psi_{b,c}^{(j)}(\mathfrak a).\] 我们断言，对每个 \(\varepsilon>0\)， \[\label{eq:sextic-sieve-pair-norm}
 \begin{split}
 |Q_j(M,N;\lambda)|
 &\ll_{S,\varepsilon}(2+MN)^\varepsilon\|\lambda\|_2^2\\
 &\quad\times
 \left\{M+\frac MN
   \max_{\substack{1\le H\\
       H\ll_{S,\varepsilon}(2+MN)^\varepsilon N^2/M}}
       E_j(H,N)\right\}.
 \end{split}\] 最大值在二进壳层上取，若为空则为零。若 \(N\le1\)， 只可能出现单位好理想，环形理想计数即证明 \(M\) 项。此外当 \(M\) 低于某个固定正常数时 \(Q_j=0\)， 因为 \(W\) 具有固定的支集上端点，而非零理想的范数 至少为一。

设 \(N>1\) 并正规化 \(\|\lambda\|_2=1\)。则 \(Q_j\) 中的每一对 都是非平凡的且 \(q_{bc}\asymp N^2\)。应用 方程 [\[eq:sextic-sieve-pair-poisson\]](#eq:sextic-sieve-pair-poisson) 并对对偶理想取三角 不等式。对小的 \(\delta>0\) 令 \(Z=(2+MN)^\delta\)。Cauchy 给出 \((\sum_b|\lambda_b|)^2\ll N\)。 由方程 [\[eq:sextic-sieve-transform-bounds\]](#eq:sextic-sieve-transform-bounds)， \(q_{\mathfrak a}>ZN^2/M\) 的部分，对任意 \(A>1\)，至多为 \[M\sum_{q_{\mathfrak a}>ZN^2/M}(Mq_{\mathfrak a}/N^2)^{-A}
 \ll N^2Z^{1-A}.\] 若截断低于一，同样的界成立。取 \(A\) 大便使 其成为任意负幂误差。

在剩余的求和中写 \(\mathfrak a=a_0\mathfrak s\)，其中 \(a_0\) 为好理想、 \(\mathfrak s\) 的支集在 \(S\) 上，并为每个固定的 \(\mathfrak s\) 选取一个生成元 \(s_0\)。 方程 [\[eq:sextic-sieve-pair-values\]](#eq:sextic-sieve-pair-values) 与 [\[eq:sextic-sieve-pair-gauss\]](#eq:sextic-sieve-pair-gauss) 给出分离的因子 \[\overline{\Psi_{b,c}^{(j)}(a_0\mathfrak s)}
 =\overline{F_b(a_0)^j}F_c(a_0)^j
       \overline{\chi_b(s_0)^j}\chi_c(s_0)^j.\] 所有 \(\chi_b(s_0)\) 具有模一。将 \(a_0\) 分成壳层 \(a_0\in\mathcal I_H\)，其中 \(H\ll ZN^2/(Mq_{\mathfrak s})\)，并 在 \(\Re w=\delta\) 上插入 \(\mathscr W\) 的 Mellin 反演。除一个依赖于 \(M,q_{a_0},q_{\mathfrak s}\) 的有界因子外，两个 系数列为 \[A_b=\lambda_b\gamma_j(b)\overline{\chi_b(s_0)^j}
                    q_b^{-1/2+\delta+it},\qquad
 B_b=\overline{\lambda_b}\gamma_{-j}(b)\chi_b(s_0)^j
                    q_b^{-1/2+\delta+it}.\] 它们在 \(a_0\) 求和过程中固定，且具有绝对值 \(\ll N^{-1/2+\delta}|\lambda_b|\)。通过 Möbius 反演 检测 \((b,c)=1\) 并在 \(a_0\) 中应用 Cauchy 给出 \[\begin{aligned}
 &\sum_{a_0\in\mathcal I_H}
  \left|\sum_{\substack{b,c\in\mathcal A_N\\(b,c)=1}}
       A_bB_c\overline{F_b(a_0)^j}F_c(a_0)^j\right|\\
 &\quad\le E_j(H,N)\sum_{\mathfrak d}
   \left(\sum_{\mathfrak d\mid b}|A_b|^2\right)^{1/2}
   \left(\sum_{\mathfrak d\mid b}|B_b|^2\right)^{1/2}
 \ll N^{-1+3\delta}E_j(H,N).\end{aligned}\] 这里除数界吸收了关于 \(\mathfrak d\) 的求和。对整个 第一个多项式取共轭使用相同的 \(E_j\) 范数。满足 \(H<1\) 的因子只有单位求值理想，并满足 \(E_j(H,N)\ll N\)。 \(\mathfrak s\) 与二进壳层的选择只有 \(\log(2+ZN^2)\) 的固定幂次 多种，因为 \(S\) 固定且非零 \(Q_j\) 有 \(M\) 有下界。方程 [\[eq:sextic-sieve-transform-bounds\]](#eq:sextic-sieve-transform-bounds) 对 \(t\) 变量求积分。以 \(\varepsilon\) 为准取 \(\delta\) 足够小 即证明方程 [\[eq:sextic-sieve-pair-norm\]](#eq:sextic-sieve-pair-norm)， 包括其 \(M\) 项上允许的全局损失。

我们现在把这一配对估计应用于 \(E_j\)。按 \(t\) 划分其内和，插入 \(W\)，并展开平方。将两个无平方因子指标写为 \(db,dc\)，其中 \(d\) 是它们的 gcd、\((b,c)=1\) 且 \((d,bc)=1\)。它们的剩余 类一致，因为 \(t\) 是乘性的。指标乘性与 方程 [\[eq:sextic-sieve-pair-values\]](#eq:sextic-sieve-pair-values) 在每个好理想 \(a\) 上给出 \[F_{db}(a)^j\overline{F_{dc}(a)^j}
   =1_{(a,d)=1}\Psi_{b,c}^{(j)}(a).\] 令 \(\mathfrak s_S=\prod_{\mathfrak p\in S}\mathfrak p\)。对 \((a,\mathfrak s_Sd)=1\) 作 Möbius 反演 将 \(a\) 写为 \(a=\mathfrak r\mathfrak a\)，其中 \(\mathfrak r\mid\mathfrak s_Sd\)。为每个固定的 \(\mathfrak r\) 选取一个生成元 \(r_0\)。 \(\Psi\) 在 \(\mathfrak r\) 处的值分离为 \(\chi_b(r_0)^j\overline{\chi_c(r_0)^j}\)，于是公共剩余列为 \[\lambda'_b=\lambda_{db}1_{(b,d)=1}\chi_b(r_0)^j,
 \qquad |\lambda'_b|\le|\lambda_{db}|.\] 它的支集在 \(\mathcal A_{N/q_d}\) 中一个类上。以长度 \(M/q_{\mathfrak r}\) 与 \(N/q_d\) 应用方程 [\[eq:sextic-sieve-pair-norm\]](#eq:sextic-sieve-pair-norm)。求和后的系数 质量为至多 \[\sum_d\sum_{\mathfrak r\mid\mathfrak s_Sd}\sum_b|\lambda_{db}|^2
 \le d_{\mathcal O}(\mathfrak s_S)
       \sum_m d_{\mathcal O}(m)^2|\lambda_m|^2
 \ll_{S,\delta}(2+N)^\delta\|\lambda\|_2^2.\] 写 \(\Delta_{\mathrm r}=q_{\mathfrak r}\) 与 \(\Delta_{\mathrm d}=q_d\)，我们有 \(1\le\Delta_{\mathrm d}\le2N\) 与 \(1\le\Delta_{\mathrm r}\le q_{\mathfrak s_S}\Delta_{\mathrm d}\)。 我们得到递归接口 \[\label{eq:sextic-sieve-norm-reflection}
 \begin{split}
 E_j(M,N)
 &\ll_{S,\varepsilon}(2+MN)^\varepsilon
 \max_{\substack{1\le\Delta_{\mathrm d}\le2N\\
                 1\le\Delta_{\mathrm r}\le q_{\mathfrak s_S}\Delta_{\mathrm d}}}
 \left\{\frac M{\Delta_{\mathrm r}}\right.\\
 &\qquad\left.+
 \frac{M\Delta_{\mathrm d}}{N\Delta_{\mathrm r}}
 \max_{\substack{1\le H\\
       H\ll_{S,\varepsilon}(2+MN)^\varepsilon
              N^2\Delta_{\mathrm r}/(M\Delta_{\mathrm d}^2)}}
       E_j(H,N/\Delta_{\mathrm d})\right\}.
 \end{split}\] 最大值可以限制在非空范围上。这是  中 gcd 与 Poisson 步骤的组合；这里使用的每个序列在其范数 和内都是公共的，且 \(S\) 保持固定。

*初始界与幂界。* 行包含给出 \(D_j\le E_j\)。Hilbert 空间对偶性与六次 互反律，按有限 \(t\)-类分裂一个矩阵变量，给出 \[\label{eq:sextic-sieve-norm-symmetry}
 D_j(M,N)\ll_S D_j(N,M).\] 相位取单位值，且非互素元素在两个方向上都为零。 我们还有初始估计 \[\label{eq:sextic-sieve-norm-initial}
 D_j(M,N)\ll_S M^2+N\qquad(M,N\ge1).\] 事实上，对无平方因子行 \(a\)，有限 Fourier 反演在每个 \(b\) 上， 包括非单位元，给出 \[\chi_a(b)^j=\frac1{\sqrt{q_a}\gamma_{-j}(a)}
       \sum_{x\bmod a}\overline{\chi_a(x)^j}e(xb/a).\] Cauchy 至多耗费 \(\#(\mathcal O/(a))^\times/q_a\le1\)。来自 \(a\in\mathcal A_M\) 的既约分数 \(x/a\) 在模 \(\mathcal O\) 下互不相同 且彼此间隔 至少 \(1/(2M)\)：\(x/a-y/c-h\) 的一个非零分子具有绝对值 至少为一，而 \(|ac|\le2M\)；模 \(\mathcal O\) 的相等迫使 相同的主分母与剩余。引理 [\[lem:planar-additive-sieve\]](#lem:planar-additive-sieve) 的对偶， 其系数生成元位于球 \(q_b\le2N\) 内，证明了方程 [\[eq:sextic-sieve-norm-initial\]](#eq:sextic-sieve-norm-initial)。

我们需要如下近单调性，它在大筛法递推中也被用到，见  与 ： \[\label{eq:sextic-sieve-norm-monotone}
 D_j(M_1,N)\ll_S D_j(M_2,N)
 \quad\text{if }M_2\ge C M_1\log(2M_1N),\quad M_1,M_2,N\ge1.\] 下面给出一个直接验证。对于零范数，该断言是显然的。 否则，为 \(D_j(M_1,N)\) 选取一个使系数取极大的单位系数向量， 并在 \(3M_1/2\) 处把行壳层拆分；其中一部分 至少承载其一半的质量。令 \(L=M_2/M_1\)。对第一部分使用范数落在 \((L,4L/3]\) 中的好素理想，对第二部分使用范数落在 \((2L/3,L]\) 中的素理想。于是当 \(p\nmid a\) 时 \(ap\in\mathcal A_{M_2}\)。固定域上的 素理想定理给出 \(P\gg_S L/\log L\) 个这样的素数。范数不超过 \(2x\) 的理想至多包含其中 \(d_x=\log(2x)/\log(2L/3)\) 个。对 \(S_a(v)=\sum_bv_bF_b(a)^j\) 与 \(p\nmid a\)，乘性给出 \[S_a(\lambda)=S_{ap}\bigl((\lambda_b\overline{F_b(p)^j})_b\bigr)
                  +S_a\bigl((\lambda_b1_{p\mid b})_b\bigr).\] 第一个系数在 \(p\mid b\) 处为零，否则消去 \(p\) 处的因子。对所选取的行与 素数取平方并求和，得到 \[\frac{P-d_{M_1}}2D_j(M_1,N)
 \le2P D_j(M_2,N)+2d_ND_j(M_1,N).\] 对所述的阈值，当 \(C\) 充分大时 \(d_{M_1}+4d_N\le P/2\)，这就证明了 方程 [\[eq:sextic-sieve-norm-monotone\]](#eq:sextic-sieve-norm-monotone)。

我们以  的幂分解与递推作结。假设对 \(j\in J\) 同时地， 对每个正的损失 \[\label{eq:sextic-sieve-inductive-bound}
 D_j(M,N)\ll_{S,\varepsilon}(MN)^\varepsilon
       \{M^\alpha+N+(MN)^{2/3}\},\qquad \alpha>4/3,\] 对 \(M,N\ge1\) 成立；单位壳层直接满足同样的界。初始估计以 \(\alpha=2\) 给出这一情形。 把好的赋值理想唯一地写成 \[a=a_1a_2^2a_3^3a_4^4a_5^5a_6^6,\] 其中 \(a_1,\ldots,a_5\) 两两互素且无平方因子，\(a_6\) 任意。代入 \(a_i\in\mathcal I_{X_i}\) 并令 \(X=\prod_iX_i\)；这里 \(X_i\ge1/2\) 且 \(\prod_iX_i^i\asymp M\)。选取 \(\ell\in\{1,2\}\) 使得 \(X_\ell=\max(X_1,X_2)\)。在其余各因子固定后，系数 \[\lambda'_b=\lambda_b\prod_{i\ne\ell}F_b(a_i)^{ij}\] 的绝对值至多为 \(|\lambda_b|\)，而剩余的核恰为 \(D_{j\ell\bmod6}(X_\ell,N)\) 的核。 放大其固定的正行限制便得到这个范数界。这包含了六次幂因子的零点。 集合 \(J\) 在映射 \(j\mapsto j\ell\bmod6\) 下封闭。 对固定的理想计数，并在正和式中忽略它们的互素性，得到 \[\label{eq:sextic-sieve-norm-power}
 E_j(M,N)\ll_{S,\varepsilon}(MN)^\varepsilon
 \max_{\boldsymbol X}
 \min\left\{M^{1/3},(M/X_\ell)^{2/3}\right\}
             D_{j\ell\bmod6}(X_\ell,N).\] 为验证该因子，固定选择的数目是 \(O(X/X_\ell)\)。 当 \(\ell=1\) 时，它至多为一个常数倍的同时满足 \((M/X_1)^{1/2}\ll(M/X_1)^{2/3}\) 与 \((MX_2/X_1)^{1/3}\le M^{1/3}\) 的量；当 \(\ell=2\) 时，它至多为一个常数 倍的 \((MX_1^2/X_2^2)^{1/3}\le M^{1/3}\ll(M/X_2)^{2/3}\)。 盒子的数目是 \(\log(2+M)\) 的一个固定幂。

把方程 [\[eq:sextic-sieve-inductive-bound\]](#eq:sextic-sieve-inductive-bound) 代入 方程 [\[eq:sextic-sieve-norm-power\]](#eq:sextic-sieve-norm-power)，得到 \[E_j(M,N)\ll_{S,\varepsilon}(MN)^\varepsilon
                    (M^\alpha+M^{1/3}N).\] 化简前的三项分别被 \(M^\alpha\)、\(M^{1/3}N\) 与 \((MN)^{2/3}\) 界住； 最后一项依 \(N\le M\) 或 \(N\ge M\) 分别被前两项之一界住。把这一估计用于 方程 [\[eq:sextic-sieve-norm-reflection\]](#eq:sextic-sieve-norm-reflection)。所有辅助的非空 尺度都被 \(2+MN\) 的固定幂界住：这里 \(N/\Delta_{\mathrm d}\ge1/2\) 且 \(H(N/\Delta_{\mathrm d})\ll_{S,\varepsilon}(2+MN)^{3+\varepsilon}\)。 单位列壳层直接满足同样的估计。因此 可以把预备损失取得更小，以给出任意指定的最终损失。 两个尺度因子为 \[\Delta_{\mathrm r}^{\alpha-1}\Delta_{\mathrm d}^{1-2\alpha}
       \ll_S\Delta_{\mathrm d}^{-\alpha}\le1,
 \qquad (\Delta_{\mathrm r}\Delta_{\mathrm d})^{-2/3}\le1.\] 因此，对 \(M,N\ge1\)， \[\label{eq:sextic-sieve-norm-recurrence}
 D_j(M,N)\le E_j(M,N)\ll_{S,\varepsilon}(MN)^\varepsilon
       \{M+N^{2\alpha-1}M^{1-\alpha}+(MN)^{2/3}\}.\]

令 \(h=2-3/(3\alpha-1)=(2\alpha-5/3)/(\alpha-1/3)\) 且 \(\beta=2-2/(3\alpha-1)\)。若 \(M\ge N^h\)， 则方程 [\[eq:sextic-sieve-norm-recurrence\]](#eq:sextic-sieve-norm-recurrence) 中的中间项 至多为 \((MN)^{2/3}\)。若 \(M<N^h\)，则把 方程 [\[eq:sextic-sieve-norm-monotone\]](#eq:sextic-sieve-norm-monotone) 中的 \(M\) 换成 \(N^h\log(2MN)\) 的一个固定倍数后应用之。那里的方程 [\[eq:sextic-sieve-norm-recurrence\]](#eq:sextic-sieve-norm-recurrence) 给出 \((MN)^\varepsilon N^\beta\)，因为 \(2(h+1)/3=\beta\) 且 \(h<\beta\)。于是两种情形下都有 \[D_j(M,N)\ll_{S,\varepsilon}(MN)^\varepsilon
                   \{M+N^\beta+(MN)^{2/3}\}.\] 对称性以 \(\beta\) 代替 \(\alpha\) 给出方程 [\[eq:sextic-sieve-inductive-bound\]](#eq:sextic-sieve-inductive-bound)， 且对每个 \(j\in J\) 同时成立。 从 \(2\) 出发，映射 \(\alpha\mapsto2-2/(3\alpha-1)\) 递减趋于 \(4/3\)。对于所要求的损失，取有限多次迭代，直到 剩余的指数间隙小于该损失的一个固定比例，再 把它吸收进 \((MN)^\varepsilon\)。结合该界与其对称 形式，在 \(M\le N\) 时利用 \(M^{4/3}\le(MN)^{2/3}\)，在 \(N\le M\) 时利用相应的不等式， 即证得 \[\label{eq:sextic-sieve-norm-shell}
 D_j(M,N)\ll_{S,\varepsilon}(MN)^\varepsilon
               \{M+N+(MN)^{2/3}\}\qquad(j\in J).\]

对两个范数球作二进细分，并沿列 壳层使用 Cauchy 不等式，可把方程 [\[eq:sextic-sieve-norm-shell\]](#eq:sextic-sieve-norm-shell) 转化为元素为 \(F_b(a)=\chi_a(b)\) 的球矩阵的同样 界。对数 因子被一个更小的预备损失吸收，而单位壳层 则直接界住。方程 [\[eq:sextic-large-sieve\]](#eq:sextic-large-sieve) 中 \(\varsigma=1\) 的矩阵是这一矩阵在长度 \((D,K)\) 处的转置。 复矩阵与其转置具有相同的算子范数，这由 伴随恒等式继之以全向量共轭得到。该界关于两个长度 对称，因此它恰好给出 \(K+D+(KD)^{2/3}\)。对整个内和取共轭得到 \(\varsigma=-1\)，零点不变。最后，固定的行限制 只会去掉非负项，而固定的系数限制通过 零延拓来实现。这就证明了引理的全部断言。

#### 物理行及其逆见证

大筛法既已证得，剩下的就是把它应用于探测器见证。 我们仅把该引理应用于物理行的无平方因子部分。无平方因子行因子与幂次行因子的 分离也用于  的推论 1.4 的 证明；这里我们保留幂次因子的实际范数，因为它同时控制矩与行的数目。

<span id="prop:sextic-row-count" label="prop:sextic-row-count">\[prop:sextic-row-count\]</span> 固定算术数据 \(\mathcal A\)、有界的物理范围 \(d_{\min}\le d\le d_{\max}\)，以及引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 与 [\[lem:detector-dyads\]](#lem:detector-dyads) 的高度与损失假设。令 \(U=Z^d\) 并沿用这些引理中的记号 \(T_1\)。设 \(\mathcal B\) 为任意一组被保留的无六次幂因子元素行 \(u\)，满足 \(q_u\asymp U\)，且全部落在同一个分箱 \((i,a)\) 中，其中 \(a>51/100\)。令 \(\delta=2a-1\)，从而 \(1/50<\delta\le1\)。

对每个 \(\epsilon>0\)，在减小命题 [\[prop:detector-witness\]](#prop:detector-witness) 中的预备损失之后，对所有充分大的 \(Z\)， \[\label{eq:sextic-row-count}
 \#\mathcal B\ll_{\mathcal A,\epsilon}
 U^{R(\delta)+\epsilon}(1+T_1)^{A_{\mathcal A}},
 \qquad
 R(\delta)=\min\left\{1,
       \max\left(1-\frac\delta2,\frac43-\delta\right)\right\}.\] 有限的阶 \(A_{\mathcal A}\) 关于物理二进区间、分箱以及所有移动的行都是一致的。 它可以在 \(T_1=Z^\tau\) 中的正指数被选定之前就固定下来。该估计对 每一组固定的被保留外部参数以及原本的行限制都成立。隐含常数 可以依赖于固定的比较常数以及有限多个共享剖面半范数。逐行的剖面选择 恰为命题 [\[prop:detector-witness\]](#prop:detector-witness) 与 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 所允许的那些；不允许任意的依赖于行的 系数。

下限分箱 \(a=51/100\) 被排除在见证断言之外。对该 分箱，初等界 \(\#\mathcal B\ll_{\mathcal A}U\) 适用；它与数值 \(R(1/50)=1\) 相符。

固定一个小的预备损失 \(\epsilon_0>0\)。对 \(\mathcal B\) 中的每一行以 \(t=1\) 应用 命题 [\[prop:detector-witness\]](#prop:detector-witness)。按其表示标签 \(\psi_{u,\nu,\varsigma}(n)=\nu(n)\chi_n(u)^{\varsigma}\) 及其多项式的二进长度对进行 细分。表示标签只有固定有限多个， 而数对则有 \(O_{\mathcal A}((\log U)^2)\) 个。在其中一个这样的 细分内，逆长度 \(D=U^r\) 与数对 \((\nu,\varsigma)\) 都是固定的。在此细分中记 \[M_u(D;W)=D^{-1/2}\sum_n\mu(n)\nu(n)\chi_n(u)^{\varsigma}W(q_n/D)\] 为该表示的逆多项式。见证给出 \[\label{eq:sextic-witness-spike}
 \frac12-O(\epsilon_0)\le r\le1+O(1/\log U),
 \qquad |M_u(D;W_u)|^2\gg_{\mathcal A,\epsilon_0}
       U^{\delta r-\epsilon_0}.\] 记号 \(W_u\) 保留了被允许的逐行范数剖面参数。 这里的多项式是所展示表示的原本多项式， 而不是其本原诱导特征的多项式。我们首先在这些参数固定时对它取 界，然后处理它们的逐行选择。

对每个无六次幂因子的行，将其理想唯一地分解为 \[(u)=\mathfrak s\mathfrak w\mathfrak k,
 \quad
 \mathfrak s=\prod_{p\in S}p^{v_p(u)},\quad
 \mathfrak w=\prod_{\substack{p\notin S\\2\le v_p(u)\le5}}p^{v_p(u)},
 \quad
 \mathfrak k=\prod_{\substack{p\notin S\\v_p(u)=1}}p.\] 于是 \(\mathfrak k\) 无平方因子，\((\mathfrak k,\mathfrak w)=1\)，且 \(\mathfrak w\) 是幂次的，即其每个正的素 赋值至少为二。\(\mathfrak s\) 只有有限多种可能， 因为它在固定集合 \(S\) 上的赋值落于 \(\{0,\ldots,5\}\)。 为这些理想各选取一个生成元 \(s_{\mathfrak s}\)。以 \(w,k\) 记 \(\mathfrak w,\mathfrak k\) 的主生成元，则存在唯一的单位 \(\upsilon\) 使得 \[u=\upsilon s_{\mathfrak s}wk.\] 每当取行和时，我们都固定 \(\mathfrak s\) 与 \(\upsilon\)。

插入二进区间 \(q_{\mathfrak w}\asymp V\)，其中把单位理想 包含在有界区间 \(V=1\) 内。只可能有 \(1\le V\ll_{\mathcal A}U\)， 且这样的区间有 \(O_{\mathcal A}(\log U)\) 个。原本的圆环 \(q_u\asymp U\) 给出实际的剩余圆环 \[\label{eq:sextic-actual-row-annulus}
 q_{\mathfrak k}=\frac{q_u}{q_{\mathfrak s}q_{\mathfrak w}}
       \asymp_{\mathcal A}\frac UV.\] 在构成和式时我们保留这一限制。只有在应用一个正的行界时， 它才会被放大为球 \(q_k\ll_{\mathcal A}U/V\)。 以 \(\mathcal U_V\) 记当前见证细分中落在这一幂次部分 二进区间内的行，并保留全部原有的物理限制。

范数不超过 \(V\) 的幂次理想的数目为 \(O(V^{1/2})\)。 事实上，每个幂次理想都有唯一的表达式 \(\mathfrak v^2\mathfrak y^3\)，其中 \(\mathfrak y\) 无平方因子；这两个 因子不必互素。由算术预备得到的理想计数给出 \[\#\{\mathfrak w:q_{\mathfrak w}\le V,\ \mathfrak w\ {\rm powerful}\}
 \ll V^{1/2}\sum_{\mathfrak y}q_{\mathfrak y}^{-3/2}
 \ll V^{1/2}.\] 最后一个级数由同样的理想计数收敛。对于其所在二进区间内每一个固定的 \(\mathfrak w\)，包含 方程 [\[eq:sextic-actual-row-annulus\]](#eq:sextic-actual-row-annulus) 的球有 \(O_{\mathcal A}(U/V)\) 个理想。非空的圆环使 \(U/V\) 被一个固定正 常数从下界住，这也涵盖了单位剩余理想。由于 \((u)\) 的 分解及其单位都是唯一的，这一幂次部分二进区间内的行的数目满足 \[\label{eq:sextic-stratum-cardinality}
 \#\mathcal U_V\ll_{\mathcal A}U V^{-1/2}.\] 在这个上界计数中丢弃任何定义 \(\mathcal U_V\) 的限制 只会增加行数。

对固定的 \(\mathfrak w,\mathfrak s,\upsilon\)，令 \(v=\upsilon s_{\mathfrak s}w\)。分子的乘性给出 精确恒等式 \[\label{eq:sextic-frozen-mask}
 \chi_n(u)^{\varsigma}
   =\chi_n(v)^{\varsigma}\chi_n(k)^{\varsigma}.\] 它包含了零延拓：若 \(n\) 与任一因子有公共因子，则两端 都为零，否则它就是通常的乘性。特别地， 对固定的剖面 \(W\)，逆多项式是 引理 [\[lem:sextic-large-sieve\]](#lem:sextic-large-sieve) 中的行和，其系数为 \[c_n=D^{-1/2}\mu(n)\nu(n)\chi_n(v)^{\varsigma}W(q_n/D).\] 因子 \(\mu(n)\) 使各列保持无平方因子。因子 \(\chi_n(v)^{\varsigma}\) 保留了 \((n,v)>1\) 处的每一个原本的零点，且关于 剩余行 \(k\) 是固定的。唯一剩下的同时依赖于 \(n\) 与 \(k\) 的零点是所展示的筛核自身的零点。 限制 \((k,w)=1\)，以及对固定外部参数从物理 行集继承来的任何限制，在本应用中都是固定的行限制。 我们不扩大 \(S\) 使其包含 \(w\) 的素因子。 因此筛中的常数与 \(w\) 无关，尽管 其固定的系数掩码可能有很大的范数。

公共的圆环支集与理想计数给出，关于固定的剖面参数一致地， \[\sum_n|c_n|^2
 \le D^{-1}\sum_{q_n\asymp D}|W(q_n/D)|^2\ll_{\mathcal A}1.\] 同样的陈述对下面用到的有限多个剖面导数也成立， 并带有相应的固定半范数。在把正剩余 行和从其实际圆环放大到 \(q_k\ll_{\mathcal A}U/V\) 之后应用 引理 [\[lem:sextic-large-sieve\]](#lem:sextic-large-sieve)。一个固定的 放大使得行界在每个非空的商区间上至少为一，并 包含圆环状的列支集。把结果对 \(\mathfrak w\) 的 \(O(V^{1/2})\) 种选择与 \(\mathfrak s,\upsilon\) 的有限多种选择求和，得到 \[\label{eq:sextic-stratum-fixed-moment}
 \sum_{u\in\mathcal U_V}|M_u(D;W)|^2
 \ll_{\mathcal A,\epsilon_1}(UD)^{\epsilon_1}V^{1/2}
 \left\{\frac UV+D+\left(\frac{UD}{V}\right)^{2/3}\right\}.\] 这一推导中的所有系数序列在应用筛法的那个行 和内部都是固定的。它们对 \(\mathfrak w\) 的不同冻结取值可以不同， 而这些取值只在那些正界之后才被求和。

现在我们恢复方程 [\[eq:sextic-witness-spike\]](#eq:sextic-witness-spike) 中 \(W_u\) 的逐行选择。 这里探测器以 \(t=1\) 使用，故 \(D_*=U\)。在表示与二进对固定 之后，其逆剖面具有形式 \[W_{\rm dyad}(x)V_{\le}(Dx/U)x^{-\sigma-i\omega},
 \qquad \omega=\gamma-\nu_F,\] 其中 \(W_{\rm dyad}\) 是固定的光滑二进截断，\(\nu_F\) 是 来自探测器的 Fourier 频率。 因子 \(V_{\le}(Dx/U)\) 对行和是公共的；变化的参数 是 \(\sigma\in[51/100,1]\) 与 \(|\omega|\le(3i+1)T_1\)。 对任一参数求导会引入一个 \(\log x\) 的幂，它在 固定圆环上有界。用单位盒子覆盖这两个参数区间。这样的盒子至多有 \(1+T_1\) 的一个固定幂那么多。引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中的参数 Sobolev 不等式用剖面导数平方的积分的有限 和界住一个盒子上的上确界。在这些积分之前先对行 求和。在每个固定的参数取值处，求导只改变 固定的剖面系数，引入所允许的对数 权重或剖面导数。因此方程 [\[eq:sextic-stratum-fixed-moment\]](#eq:sextic-stratum-fixed-moment) 适用于每个这样的积分。这就证明了 \[\label{eq:sextic-stratum-moment}
 \sum_{u\in\mathcal U_V}|M_u(D;W_u)|^2
 \ll_{\mathcal A,\epsilon_1}(UD)^{\epsilon_1}(1+T_1)^{A_{\mathcal A}}
 V^{1/2}\left\{\frac UV+D+
       \left(\frac{UD}{V}\right)^{2/3}\right\}.\] 导数的阶以及由此的 \(A_{\mathcal A}\) 在选取 \(\tau\) 之前就已固定。高度区间与额外频率的 总容许量恰为共享探测器估计中的那些；Sobolev 步骤既不赋予新的频率容许量，也不改变围道。 它不允许对每个 \(k\) 分别选取系数。

剩下的是把这个矩与独立的计数 方程 [\[eq:sextic-stratum-cardinality\]](#eq:sextic-stratum-cardinality) 结合起来。记 \[V=U^o,\qquad D=U^r,\qquad
 e_o(r)=\frac o2+\max\left\{1-o,r,\frac{2(1-o+r)}3\right\}.\] 这些是实际二进区间的参数。非空的二进区间有 \(0\le o\le1+O_{\mathcal A}(1/\log U)\)；单位二进区间有 \(o=0\)。 由于见证长度保持有界，方程 [\[eq:sextic-stratum-moment\]](#eq:sextic-stratum-moment) 中 \(UD\) 的任意小幂 可以写成 \(U\) 的任意小幂。用 方程 [\[eq:sextic-witness-spike\]](#eq:sextic-witness-spike) 中的尖峰去除该方程， 并同时使用 方程 [\[eq:sextic-stratum-cardinality\]](#eq:sextic-stratum-cardinality)，对这一细分给出 \[\label{eq:sextic-stratum-envelope}
 \#\mathcal U_V
 \ll U^{\min\{1-o/2,e_o(r)-\delta r\}+O(\epsilon_0)+\epsilon_1}
       (1+T_1)^{A_{\mathcal A}},\] 在必要时把记作 \(\epsilon_1\) 的筛损失减小之后。

我们首先在 \(0\le o\le1\) 与 \(1/2\le r\le1\) 上计算此表达式中最大的指数。令 \(x=1-o\) 且 \(A=(1+x)/2\)。则 \[e_o(r)-\delta r
 =\max\left\{
 A-\delta r,\quad
 \frac{1-x}{2}+(1-\delta)r,\quad
 \frac12+\frac x6+\left(\frac23-\delta\right)r
 \right\}.\] \(A\) 与三个实数的最大值的最小值，等于 \(A\) 分别与这三个数的最小值的最大值。第一个这样的最小值是 \(A-\delta r\le1-\delta/2\)。对固定的 \(r\)，第二个是 \(x\) 的一个递增与一个递减仿射函数的最小值。它们 在 \(x=(1-\delta)r\in[0,1]\) 处相交，故其关于 \(x\) 的最大值为 \[\frac{1+(1-\delta)r}{2}\le1-\frac\delta2.\] 第三个最小值中的两个函数都随 \(x\) 增大。因此它关于 \(x\) 的最大值为 \[\min\left\{1,\frac23+\left(\frac23-\delta\right)r\right\}.\] 这个关于 \(r\) 的仿射表达式在两个端点处取值 \(1-\delta/2\) 与 \(4/3-\delta\)。由此推出，且等号在其中一个端点处取得， \[\label{eq:sextic-envelope-optimization}
 \max_{\substack{0\le o\le1\\1/2\le r\le1}}
 \min\{1-o/2,e_o(r)-\delta r\}
 =\min\left\{1,\max\left(1-\frac\delta2,\frac43-\delta\right)\right\}.\] 这一计算关于 \(0\le\delta\le1\) 是一致成立的。

刚刚用到的函数是仿射函数的最大值与最小值，这些 仿射函数的斜率在这些紧区间的固定邻域上一致有界。 把实际的 \(o\) 换成它在 \([0,1]\) 中的最近点，把 实际的见证 \(r\) 换成它在 \([1/2,1]\) 中的最近点，由 方程 [\[eq:sextic-witness-spike\]](#eq:sextic-witness-spike) 与实际二进界，至多使 指数改变 \(O_{\mathcal A}(\epsilon_0+1/\log U)\)。 因此这一替换只在最后的优化中进行，而不在 行和或其筛法应用中进行。就所指定的 \(\epsilon\) 而言，选取 \(\epsilon_0\) 与预备 筛损失足够小。\(O((\log U)^2)\) 个见证对与 \(O(\log U)\) 个幂次部分二进区间只需 再付出一个任意小的幂。对 方程 [\[eq:sextic-stratum-envelope\]](#eq:sextic-stratum-envelope) 求和即证得 方程 [\[eq:sextic-row-count\]](#eq:sextic-row-count)。

最后，分箱 \(a=51/100\) 不必包含实际的零点，因此那里 不使用命题 [\[prop:detector-witness\]](#prop:detector-witness)。对其物理圆环中的 所有元素计数得到 \(O_{\mathcal A}(U)\) 行。由于 \(1/50<1/3\)，所展示的 \(R\) 的公式给出 \(R(1/50)=1\)，与断言一致。

为在高估计中使用，行包络具有如下显式形式 \[R(\delta)=
 \begin{cases}
  1,&0\le\delta\le1/3,\\
  4/3-\delta,&1/3\le\delta\le2/3,\\
  1-\delta/2,&2/3\le\delta\le1.
 \end{cases}\] 论证只用到逆见证。在这个行计数中，不需要关于 与普通见证之乘积的任何估计。

### 高展开的解析估计

行包络现在进入基础探针的 Poisson 表示。 对于第一阶段的应应用，保留假设 \(\Delta_1=\beta_*-11/12>0\) 并令 \(X=Y=Z^{1/2}\)。以 \(s\) 记 节 [5.2](#sec:local-euler) 中称为 \(x\) 的第一个 Mellin 变量。方程 [\[eq:probe-poisson-identity\]](#eq:probe-poisson-identity) 与 [\[eq:probe-high\]](#eq:probe-high) 给出待估计的实际积分： \[\begin{split}
 I_\eta(Z^{1/2},Z^{1/2},Z)
 =\frac1{(2\pi i)^3}\int_{(3)}\int_{(3)}\int_{(2)}
 &\mathcal W(Z^{1/2},Z^{1/2},Z;s,w,z)\\
 &\cdot\sum_u^{(6)}q_u^{-z}\overline{\xi(u)}
 \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
      {L^S(s,\eta\overline{\chi_\bullet(u)})}
 \mathcal H_{\eta,u}(s,w,z)\,dz\,dw\,ds.
\end{split}\] 这里 \[\mathcal W(X,Y,Z;s,w,z)=X^{1/2-z}Z^{s+z-1}Y^{w-1}
 e^{(s+z-1)^2}M(z)\widehat W_1(w).\] 各行是非零的无六次幂因子元素，带有其单位因子 以及物理限制 \((u,S)=1\)。两种特征表示都保留 它们在整除 \(u\) 的素数处的原本零点。基础探针的逐系数校准 已包含在这一恒等式中。

行 \(u=1\) 包含目标函数的倒数。对于中间行范数，我们将固定一个带缓冲的分箱，把它的积分移到 \[\Re s=a+16e,\qquad \Re w=1-a-6e,\qquad \Re z=17/50,\] 并在那里应用包络 \(R(2a-1)\)。除小的实部损失与一个固定的高度因子外， 该围道上的分子对行范数 \(q_u\asymp U\) 付出 \(U^{a-1/2}\) 的代价；行包络控制 这样的项出现多少。我们首先辨识主信号，然后实施 这一移动围道及其具体的第一阶段估计。主留数 与外层行范数的直接界完成了比较。

#### 主行与正规化

我们辨识其分子为主的行。含有一个 \(S\) 之外素因子的物理行， 由 可知其分子非主。 由于物理掩码强制 \((u,S)=1\)， 其余的行都是单位。若单位 \(u\ne1\) 在 \(F\) 中有六次根， 则该根在每个素数处的赋值都为零，从而是 \(F\) 的一个 单位；而 \(F\) 的每个单位的六次幂都为一。于是 \(F(u^{1/6})/F\) 是非平凡的。它是有限 Galois 扩张，因为 \(F\) 包含 六次单位根。对非单位 Frobenius 类应用 Chebotarev 定理 可给出一个固定集合 \(S\) 之外的素数，使得相应的 六次特征非平凡 。由 引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 中的 Kummer 描述，这就是 \(\chi_\bullet(u)\)。因此 \(u=1\) 是唯一的主分子行。 附着于一个有界单位行的分母可能是主的；它的 倒数在一处有零点，将在下面保持在一条整体直线上。

定义 \[H_\eta(s)=\mathcal H_{\eta,1}(s,1,1/6),\qquad
 c_S=\widehat W_1(1)M(1/6)
       \left(\operatorname*{Res}_{v=1}\zeta_F^S(v)\right)^2/6.
 \label{eq:shared-principal-data}\] 引理 [\[lem:local-euler\]](#lem:local-euler) 使 \(H_\eta\) 在 \(\Re s>7/8\) 上全纯。 其一致估计 \(H_\eta=1+O(P_0^{-4/5})\) 允许在目标之前 选取 \(P_0\)，因为局部界关于目标单位 相位是一致的。固定 \(P_0\) 足够大，使得 \[\sup_{\Re s>7/8}|H_\eta(s)-1|\le\frac12.
 \label{eq:shared-principal-nonvanishing}\] 用这些素数扩大 \(S\) 不改变固定的射线类群 \(T\)， 因为局部恒等式中的校准是逐系数成立的。被 排除的集合以及由此的特定函数 \(H_\eta\) 可以在不同 应用之间不同，但在一个应用内部，它们恰为 所使用的那一个精确高表示的那些。

常数 \(c_S\) 为正。事实上 \(\widehat W_1(1)>0\)，因为 \(W_1\) 非负且非零，而由 方程 [\[eq:radial-mellin-positive\]](#eq:radial-mellin-positive) 有 \(M(1/6)>0\)。\(\zeta_F^S\) 的 单极点具有正的留数：删除把 \(\zeta_F\) 的正留数 乘以 \(\prod_{p\in S}(1-q_p^{-1})>0\)。

对第一阶段，令 \[C_{\mathrm I}(s)=s-\frac23,\qquad
 J_{\mathrm I,\eta}(Z)=\frac{I_\eta(Z^{1/2},Z^{1/2},Z)}{c_S}.\] 设 \(f_{\mathrm I,\eta}\) 为 方程 [\[eq:common-residue\]](#eq:common-residue) 中的积分，其中 \(C=C_{\mathrm I}\)、 \(\mathcal S=S\)，且函数 \(H_\eta\) 如上定义。\(w=1\) 与 \(z=1/6\) 处的两个标量极点 将给出 \(c_S f_{\mathrm I,\eta}\)；我们剩余的 目标是为其他每一项取得一个公共的幂次节省，相对于 \(Z^{C_{\mathrm I}(\beta_*)}\) 来度量。

#### 移动围道所用的精确恒等式

围道证明使用所示积分中完整的全纯修正。为把 该证明复用于补偿探针，我们记下它所要求的 恒等式与界。在当前的应应用中，修正 是 \(\mathcal H_{\eta,u}\)，与 \(Z\) 无关，而下面的参数 是 \(l_x=l_y=h=1/2\) 与 \(\ell=0\)。

方程 [\[eq:probe-high\]](#eq:probe-high) 中的标量商是高展开中 同时决定移动围道与主留数的那一部分。我们保持该商 固定，并明确陈述围绕它可以改变什么。令 \[\begin{split}
 \mathcal D_1(\epsilon_0)=\{(s,w,z):{}&\Re s\ge51/100,\quad
       \Re z\ge17/50,\quad \Re w\ge-1/100,\\
       &\Re(s+w)\ge1+\epsilon_0\},\qquad \epsilon_0>0,\\
 \mathcal D_2=\{(s,w,z):{}&\Re s\ge7/8,\quad
       \Re z\ge33/200,\quad \Re w\ge19/20\}.
 \end{split}\] 这些是引理 [\[lem:local-euler\]](#lem:local-euler) 中的两个区域。下面所谓的实盒子， 指的是 \((\Re s,\Re w,\Re z)\) 的 \(\mathbb R^3\) 的一个紧矩形子集。

<span id="def:stage-high-data" label="def:stage-high-data">\[def:stage-high-data\]</span> 固定实数 \(l_x,l_y>0\) 与 \(\ell\ge0\)，使得 \[X=Z^{l_x},\qquad Y=Z^{l_y},\qquad h=1-l_x+\ell>0,
 \qquad
 C(s)=s+\frac{l_x}{2}-1+\frac h6
     =s-\frac56+\frac{l_x}{3}+\frac\ell6.
 \label{eq:stage-mellin-exponent}\] 这些实数在目标特征之前固定。对每个本原有限阶目标 \(\eta\)，固定节 [4](#sec:probe) 的 数据 \(S,\xi,W_0,W_1\)，它与 \(Z\) 无关。精确高表示的数据由以下对象与断言构成。

首先，对每个充分大的实数 \(Z\)，\(\mathscr I_\eta(Z)\) 是一个独立指定的复值 量。在每次应用中，它由该 \(Z\) 下方程 [\[eq:general-probe\]](#eq:general-probe) 中完备化和的有限 线性组合给出，允许对完备化指标 \(A\) 作指定限制，并对其三个正尺度作指定的 重标度。该有限组合中的项数与系数可依赖于 \(Z\)。任何对 \(\mathscr I_\eta\) 的直接 估计都指这一表达式，而非某个另行定义的高积分。

其次，对每个满足 \((u,S)=1\) 的非零无六次幂因子元素 \(u\) 及每个这样的 \(Z\)， 存在函数 \(\mathfrak H_{\eta,u,Z}(s,w,z)\)。它在 \(\mathcal D_2\) 的每一点以及每个 \(\mathcal D_1(\epsilon_0)\) 的每一点的邻域上全纯。对每个 \(D>0\) 及包含于这些 区域之一的每个实长方体 \(\mathcal K\)，存在有限常数 \(B_{\eta,\mathcal K,D}\) 与 \(J_{\eta,\mathcal K,D}\)，使得对 \(1\le q_u\le Z^D\)、所有虚部以及 \(\mathcal K\) 中的 实部一致地有 \[|\mathfrak H_{\eta,u,Z}(s,w,z)|
 \ll_{\eta,\mathcal K,D}
 Z^{B_{\eta,\mathcal K,D}}
 (1+|\Im s|+|\Im w|+|\Im z|)^{J_{\eta,\mathcal K,D}}.
 \label{eq:stage-all-height-majorant}\] 这些常数与指数独立于 \(Z,u\) 以及任何后续的分部积分次序。不假设 \(\mathfrak H\) 或其任何局部因子非零。

最后，对独立给定的 \(\mathscr I_\eta(Z)\) 断言如下恒等式，其中和式与积分在所示 直线上绝对收敛： \[\begin{split}
 \mathscr I_\eta(Z)=\frac1{(2\pi i)^3}
 \int_{(3)}\int_{(3)}\int_{(2)}
 &\mathcal W(X,Y,Z;s,w,z)
 \sum_u^{(6)}q_u^{-z}\overline{\xi(u)}\\
 &\cdot
 \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
      {L^S(s,\eta\overline{\chi_\bullet(u)})}
 \mathfrak H_{\eta,u,Z}(s,w,z)\,dz\,dw\,ds,
\end{split}
\label{eq:stage-high-identity}\] 其中和式具有方程 [\[eq:probe-poisson-identity\]](#eq:probe-poisson-identity) 的物理限制，并且 \[\mathcal W(X,Y,Z;s,w,z)
 =X^{1/2-z}Z^{s+z-1}Y^{w-1}
       e^{(s+z-1)^2}M(z)\widehat W_1(w).\] 因此方程 [\[eq:stage-high-identity\]](#eq:stage-high-identity) 是对物理表达式待证明的一个假设，而非 其定义。

对基础探针，物理表达式为 \(I_\eta(Z^{l_x},Z^{l_y},Z)\)、\(\ell=0\) 以及 \(\mathfrak H_{\eta,u,Z}=\mathcal H_{\eta,u}\)。 方程 [\[eq:probe-poisson-identity\]](#eq:probe-poisson-identity) 与 [\[eq:probe-high\]](#eq:probe-high) 证明所需的恒等式，而引理 [\[lem:local-euler\]](#lem:local-euler) 给出全纯性以及 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant)。更一般地，定义中的函数 \(\mathfrak H\) 始终指 *所示标量商被除去之后的完整修正*。 若该修正是局部因子乘积之和，则这些乘积本身 在所述区域上必须全纯。用个别局部因子在其零点处 作商不能确立这一条件。仅用于估计被保留围道的 分解将在下文单独陈述。

#### 竖直线上的外部尾部与水平衔接

我们三个 Mellin 检验函数的乘积在三个独立的高度方向上衰减。下述估计把这一 衰减转化为大长方体之外以及围道矩形水平边上的界。

<span id="lem:external-contour-tails" label="lem:external-contour-tails">\[lem:external-contour-tails\]</span> 设 \(m\ge2\)，设 \(\mathcal K\) 为实围道参数的紧集，且对 \(\boldsymbol r\in\mathcal K\) 与 \(Z\ge2\)，设 \(K_{\boldsymbol r,Z}\) 为 \(\mathbb R^m\) 上的非负 Borel 可测核。假设它在 \((\boldsymbol r,\boldsymbol t)\) 中联合 Borel 可测，且对每个整数 \(L\ge0\)， \[K_{\boldsymbol r,Z}(\boldsymbol t)
 \ll_L(1+|\boldsymbol t|)^{-L}\] 对 \(\boldsymbol r,Z,\boldsymbol t\) 一致成立。设 \(\mathcal D\subseteq\mathbb R^m\) 为 Borel 可测，并假设 Borel 可测因子 \(F_Z\) 在 \(\mathcal D\) 上满足 \[|F_Z(\boldsymbol t)|\le C Z^B(1+|\boldsymbol t|)^J,
 \label{eq:external-arithmetic-majorant}\] 其中 \(B,J,C\) 固定，独立于 \(Z\) 与下文整数 \(N\) 之下。 用 \(\widehat{\boldsymbol t}_j\) 表示略去 \(\boldsymbol t\) 的 第 \(j\) 个坐标所得的向量。对 \(T\ge1\) 与 \(\boldsymbol r\in\mathcal K\) 一致地， \[\begin{aligned}
 \int_{\mathcal D\cap\{\max_j|t_j|>T\}}
 K_{\boldsymbol r,Z}(\boldsymbol t)|F_Z(\boldsymbol t)|\,d\boldsymbol t
 &\ll_N Z^B T^{-N},
 \label{eq:external-integrated-tail}\\
 \int_{\mathcal D\cap\{t_j=T\}}
 K_{\boldsymbol r,Z}(\boldsymbol t)|F_Z(\boldsymbol t)|\,
 d\widehat{\boldsymbol t}_j
 &\ll_N Z^B(1+|T|)^{-N}.
 \label{eq:external-trace-tail}\end{aligned}\] 第二个断言对 \(T\) 的任一符号与每个 \(j\) 成立，在 \(t_j=T\) 上使用坐标 Lebesgue 测度。当假设在该处一致成立，且核、区域指示函数与 算术因子在该实参数与其余坐标中联合 Borel 可测时，两个断言在关于 有界长度实围道区间积分之后仍成立。

把核的界乘以 方程 [\[eq:external-arithmetic-majorant\]](#eq:external-arithmetic-majorant)。在长方体之外对 \((1+|\boldsymbol t|)^{J-L}\) 积分，当 \(L>N+J+m\) 时证明 方程 [\[eq:external-integrated-tail\]](#eq:external-integrated-tail)。 在 \(t_j=T\) 上，对其余 \(m-1\) 个坐标积分给出 \[\int_{\mathbb R^{m-1}}
 (1+|T|+|\widehat{\boldsymbol t}_j|)^{J-L}
 d\widehat{\boldsymbol t}_j
 \ll(1+|T|)^{J-L+m-1}.\] 取 \(L>N+J+m-1\) 证明方程 [\[eq:external-trace-tail\]](#eq:external-trace-tail)。 限制到 \(\mathcal D\) 会减小这些正积分，而有界 实区间只贡献其长度。

对我们的三重积分，取 \[(y_1,y_2,y_3)=(\Im(s+z),\Im z,\Im w),\qquad
 K_{\boldsymbol r,Z}(\boldsymbol t)
 =e^{-y_1^2}|M(r_z+iy_2)|\,|\widehat W_1(r_w+iy_3)|.\] 高度变量的变换的行列式为 1。在固定的实长方体上，其中 \(r_z\) 属于 \((0,\infty)\) 的紧子区间，节 [5](#sec:poisson-representation) 的 Mellin 估计给出 \(M\) 与 \(\widehat W_1\) 的任意多项式衰减。Gaussian 具有同样的性质。因此它们的乘积 对每个 \(L\) 为 \(O_L((1+|\boldsymbol y|)^{-L})\)，从而也是 \(O_L((1+|\boldsymbol t|)^{-L})\)。被略去的因子 \(e^{(\Re(s+z)-1)^2}\) 在该实长方体上有界。

取 \(w\) 的留数之后只剩下 \(s,z\)。同样的证明适用于核 \[K^{(2)}_{\boldsymbol r,Z}(\boldsymbol t)
 =e^{-y_1^2}|M(r_z+iy_2)|,
 \qquad(y_1,y_2)=(\Im(s+z),\Im z).
 \label{eq:external-two-dimensional-kernel}\] 这提供了后续 \(z\)-衔接所需的迹界。

同样的核检验处理额外的外部分离变量。 对 \(m\ge3\)，设 \(\boldsymbol y=A\boldsymbol t\)，其中 \(A\in\mathrm{GL}_m(\mathbb R)\) 固定， 并把三因子核乘以 Borel 密度 \(|v_{\boldsymbol r,Z}(y_4,\ldots,y_m)|\)， 它在 \((\boldsymbol r,\boldsymbol v)\) 中联合 Borel，满足 \[\sup_{\boldsymbol r,Z,\boldsymbol v}
 (1+|\boldsymbol v|)^L|v_{\boldsymbol r,Z}(\boldsymbol v)|<\infty
 \quad\text{对每个整数 }L\ge0.
 \label{eq:external-density-contract}\] 对 \(m=3\)，该密度在零维空间上为 1。由于 \(A\) 及其逆固定，乘积 在所有 \(m\) 个坐标中仍快速衰减。对二因子核，相同的论证在 \(\mathbb R^{m-2}\) 上使用密度并要求 \(m\ge2\)，当 \(m=2\) 时密度为 1。 因此两种乘积核形式都具有上述积分界与迹界。

由对数 Fourier 反演分离的一致环形剖面通过反复 分部积分满足方程 [\[eq:external-density-contract\]](#eq:external-density-contract)，如引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中 那样。首先把每个纯范数扭转翻译为其 Mellin 变元。额外的坐标高度 随后向三维变量变换附加一个具有固定逆的块三角矩阵。

仅通过固定的加权 \(L^1\) 范数而知的内部系数测度并不 因此被逐点密度假设或其迹结论所覆盖。这样的测度在因子 \(F_Z\) 内部 仍以其已经固定的矩阶被积分。任何使用迹估计的额外外部 坐标必须单独满足方程 [\[eq:external-density-contract\]](#eq:external-density-contract)。

引理中的区域 \(\mathcal D\) 很重要。假设某个倒数仅在其变元 \(\gamma+\sum_j a_jt_j\) 的虚部位于带缓冲区间内时才有界。具有 \(a_j\ne0\) 的坐标只能在保持这一条件的范围内积分；引理不会把 倒数的界扩展到该范围之外。当其他因子在该处满足 方程 [\[eq:external-arithmetic-majorant\]](#eq:external-arithmetic-majorant) 时，具有 \(a_j=0\) 的坐标可以被扩展。 扩展轴上的所有因子必须使用其全局或绝对估计，而非仅在保留 区间上成立的估计。特别地，仅凭积分尾部不足以证明水平衔接的 合理性：该衔接使用方程 [\[eq:external-trace-tail\]](#eq:external-trace-tail)。

在本引理中增大 \(N\) 只会增大外部光滑检验函数的衰减阶。 它不对 \(F_Z\) 求导。因此，当 \(N\) 稍后被选取时，\(F_Z\) 中 固定的矩剖面阶或固定的算术高度指数保持不变。这与 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中所作的阶的区分相同。

#### 移动一个固定分箱

我们首先移动整个行积分。行包络只会在这一步之后， 在被保留的围道上应用。

<span id="lem:fixed-bin-contour" label="lem:fixed-bin-contour">\[lem:fixed-bin-contour\]</span> 假设定义 [\[def:stage-high-data\]](#def:stage-high-data)。固定 \(\sigma_0\in[7/8,1)\) 且 \(\beta_*>\sigma_0\)，令 \(z_0=17/50\)，并设 \(U=Z^d\)，其中 \(0<d_{\min}\le d\le d_{\max}<\infty\)。 设 \(\mathcal B\) 为引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 的某个分箱 \((i,a)\) 中满足 \(q_u\asymp U\) 的被保留物理行的有限集，它在任何 Mellin 变量被移动之前固定。该环形区域中的比较常数 固定。取 \(0<e<10^{-3}\) 与 \(T_1=Z^\tau>2\)，其中 \(0<\tau\le d_{\min}/100\)。实范围与 \(e\) 独立于 目标。

固定正常数 \(c_s,c_w,c_z\le1/2\)，独立于 \(Z\) 与 各行。保留原始高度 \(|\Im s|\le c_sT_1\)、\(|\Im w|\le c_wT_1\) 与 \(|\Im z|\le c_zT_1\)。\(\mathcal B\) 在方程 [\[eq:stage-high-identity\]](#eq:stage-high-identity) 中 起始直线上的贡献等于其在这些保留线段上的积分 \[\Re s=a+16e,\qquad \Re w=1-a-6e,\qquad \Re z=z_0,
 \label{eq:stage-central-contours}\] 误差至多 \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\)，对每个固定的 \(N\)。有限 指数 \(B_\eta\) 在 \(N\) 之前固定。空的行集贡献为零。 该变换使用完整的全纯修正；不需要对该修正 作分解，也不需要依赖于围道点的细分。

节 [6](#sec:detector) 给出 \(a\le\beta_*\)，包括地板分箱。 在方程 [\[eq:stage-high-identity\]](#eq:stage-high-identity) 的绝对直线上隔离出关于 \(\mathcal B\) 的有限和。把 \(z\) 从 \(2\) 移动到 \(z_0\)，保持 \(w=3\)，并把 \(s\) 从 \(3\) 移动到 \(\beta_*+20e\)。这些移动对某个固定的正 \(\epsilon_0\) 保持在 \(\mathcal D_1(\epsilon_0)\) 内，两个分子变元保持在其极点右侧，且倒数保持在 \(\Re s>\beta_*\)。其全局界由引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control) 与 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors) 得出，使用节 [6](#sec:detector) 中的 导子与删除根式界。该修正服从 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant)。因此 \(T\to\infty\) 的 引理 [\[lem:external-contour-tails\]](#lem:external-contour-tails) 证明这些移动是合理的。

现在把 \(w\) 从 \(3\) 移动到 \(1-a-6e\)，而 \(s\) 保持在该全局直线上。 在整个移动过程中， \[\Re(s+w)\ge1+(\beta_*-a)+14e\ge1+14e.\] 每个被保留行的分子特征是非主的，因此其 \(L\) 函数是整函数。又有 \(\Re w\ge-6e>-1/100\) 与 \(\Re z=z_0\)。于是该修正在 \(\mathcal D_1(\epsilon_0)\) 中保持全纯，例如取 \(\epsilon_0=10e\)，且不跨 越任何极点。在 \(w\)-衔接上倒数仍是全局的。分子的 全局上带形域界、删除因子界以及 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant) 给出在该处所积分坐标轴上的形如 方程 [\[eq:external-arithmetic-majorant\]](#eq:external-arithmetic-majorant) 的优函数。迹估计使这些衔接趋于零。

在把 \(s\) 移动得更远之前，把三个原始 Mellin 高度限制到所述长方体。在被丢弃的 部分上保持 \(s\) 在 \(\Re s=\beta_*+20e\)。在那里，全局倒数界、 全局分子界、删除因子以及全高度 修正界给出 \(Z^{B_\eta}\) 乘以高度的固定多项式： 行范围由 \(q_u\ll Z^{d_{\max}}\) 界定，而行数 为 \(O(U)\)。引理 [\[lem:external-contour-tails\]](#lem:external-contour-tails) 中的积分尾部给出 \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\)。

只把被保留的 \(s\) 线段移动到 \(a+16e\)。在这个矩形上， \[\Re(s+w)\ge1+10e,\] 且定义 \(\mathcal D_1(10e)\) 的其他不等式仍然成立。 倒数变元的实部至少为 \(a+16e>a+6e\)。 所述高度长方体对充分大的 \(Z\) 把两个标量变元 严格置于 \(|\Im v|\le(3i+2)T_1\) 内部。 因此引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 在整个 被保留矩形上排除其零点。由于 \(6z_0>1\)，标量 zeta 因子在此移动上 没有极点。于是不跨越任何极点。

对 \(s\)-衔接，其虚坐标固定为 \(T_1\) 的常数倍。 方程 [\[eq:stage-high-identity\]](#eq:stage-high-identity) 中的标量分母 只依赖于 \(s\)，因此当 \(\Im z\) 与 \(\Im w\) 的积分扩展到其整个坐标轴时，其带缓冲的估计仍然有效。 在这些扩展轴上使用全局分子估计与 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant)。迹估计于是给出 \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\)。本论证中没有任何 \(w\)- 或 \(z\)-衔接 扩展一个已被移动到仅是带缓冲区域的 \(s\)-轴。

精确高表示是一个三重积分，带有一个关于其 完整修正的优函数。因此我们可以在 引入任何辅助分离变量之前执行这一变换。若某个中心估计稍后 使用这类变量，则其保留区域与丢弃部分必须 在该估计中得到证明；它们不是刚刚证明的围道 恒等式的新坐标。

#### 应用行包络

对基础修正，引理 [\[lem:local-euler\]](#lem:local-euler) 验证 引理 [\[lem:fixed-bin-contour\]](#lem:fixed-bin-contour) 的假设。事实上 \(|\mathcal H_{\eta,u}|\ll_\epsilon q_u^\epsilon\) 在两个 Euler 区域中对所有三个 高度一致成立；对 \(q_u\le Z^D\)，取 \(\epsilon=1\) 给出 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant)，其中 \(B=D\) 且高度阶 为零。我们现在估计被保留的积分，在本小节中始终使用 \(l_x=l_y=h=1/2\) 与 \(\ell=0\)。

固定 \[d_{\min}=\frac1{63},\qquad \zeta=\frac1{1000},\qquad
 d_{\max}=h+\zeta=\frac{501}{1000}.\] 对该范围内的一个二元组 \(U=Z^d\)，在移动 任何 Mellin 变量之前固定一个动态分箱 \((i,a)\)，并令 \(\delta=2a-1\)。 命题 [\[prop:sextic-row-count\]](#prop:sextic-row-count) 在请求损失 \(\epsilon_r>0\) 下给出其基数至多 \(U^{R(\delta)+\epsilon_r}(1+T_1)^{A_\eta}\)，相差一个固定常数。 对地板而言这是直接计数 \(O_\eta(U)\)，因为 \(R(1/50)=1\)；它不使用见证。

分子 \(L^S(w,\chi_\bullet(u))\) 正是节 [6](#sec:detector) 中 \(\nu=1\) 的原始零扩展表示。 在被保留直线 \(\Re w=1-a-6e\) 上，引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 对任意 \(\epsilon_n>0\) 给出界 \(U^{\delta/2+12e+\epsilon_n}(3+T_1)^C\)。 这在地板分箱中也成立。中心点位于 \(\mathcal D_1(10e)\) 内，因此引理 [\[lem:local-euler\]](#lem:local-euler) 中更强的局部估计给出 该处 \(|\mathcal H_{\eta,u}|\ll_{e,\epsilon_H}U^{\epsilon_H}\)，对任意 \(\epsilon_H>0\)。于是 \[\sum_{u\in\mathcal B}
 |L^S(w,\chi_\bullet(u))\mathcal H_{\eta,u}(s,w,z)|
 \ll_\eta
 U^{R(\delta)+\delta/2+12e+\epsilon_r+\epsilon_n+\epsilon_H}
 (1+T_1)^{A'_\eta}.\] 这里 \(A'_\eta\) 有限，并在最终外部尾部阶之前固定。

令 \(\varepsilon_c=12e+\epsilon_r+\epsilon_n+\epsilon_H\)。 带缓冲的倒数对任意 \(\varepsilon_d>0\) 耗费 \(U^{\varepsilon_d}\)，且 \(\zeta_F^S(6z_0)\) 绝对有界。 这些检验函数在上述三个独立高度 坐标中具有有界的联合 \(L^1\) 范数。外部幂，包括 \(q_u^{-z_0}\)，为 \[Z^{a/2-3/4+z_0/2+13e}U^{-z_0}.\] 把这些界相乘，对每个 \(\varepsilon_p>0\) 给出至多的被保留 分箱贡献 \[\ll_\eta Z^{1/4+E_{\mathrm I}(d)+13e
       +(1+d)\varepsilon_c+d\varepsilon_d+\varepsilon_p}
 (1+T_1)^{A'_\eta}.
 \label{eq:balanced-central-contribution}\] 这里我们无害地 把这界扩大了 \(Z^{\varepsilon_c+\varepsilon_p}\)，使得各项损失使用与 后续一般估计相同的形式，并且 \[E_{\mathrm I}(d)=-\frac34+\frac{\delta+R(\delta)}2
 +\left(d-\frac12\right)
       \left(R(\delta)+\frac\delta2-\frac{17}{50}\right).\] 在此应用中没有额外的 Mellin 积分。其标量 带缓冲变元具有高度 \(\Im s\) 与 \(\Im w\)。行计数中的见证 频率与剖面选择保持在该探测器已有的 容许范围之内，并且不进入任何一个标量变元。

在 \(d=h=1/2\) 处，行包络的三片分别给出 \[E_{\mathrm I}(h)=
 \begin{cases}
  -1/4+\delta/2,&0\le\delta\le1/3,\\
  -1/12,&1/3\le\delta\le2/3,\\
  -(1-\delta)/4,&2/3\le\delta\le1.
 \end{cases}\] 前两片至多为 \(-1/12\)。在第三片中，节 [6](#sec:detector) 的精确分箱 上界为 \[\delta\le2\beta_*-1=\frac56+2\Delta_1.\] 由此在每一片中都有 \[E_{\mathrm I}(h)-\Delta_1
 \le-\frac1{24}-\frac{\Delta_1}{2}.\] 这就是此处所需的与 \(C_{\mathrm I}(\beta_*)\) 的比较； \(E_{\mathrm I}(h)\) 本身不必为负。 频率斜率为三种形式 \[R(\delta)+\frac\delta2-\frac{17}{50}
 =\begin{cases}
  33/50+\delta/2,&0\le\delta\le1/3,\\
  149/150-\delta/2,&1/3\le\delta\le2/3,\\
  33/50,&2/3\le\delta\le1.
 \end{cases}\] 因此它位于 \([33/50,62/75]\) 内。正性控制所有 \(d\le h\)， 而到 \(d\le h+\zeta\) 的延拓最多耗费 \((62/75)\zeta\)。 于是，在可调损失之前，每个中心二元组至少有节省 \[m_c=\frac1{24}-\frac{62}{75}\zeta=\frac{1021}{25000}\] 相对于 \(C_{\mathrm I}(\beta_*)\)。

#### 把修正分成若干片段的中心估计

前面的计算把一个总体的绝对行界乘以 外部 Mellin 幂。我们记录当完整修正由 若干片段估计、且可用界在行集之间变化时它的形式。 围道对固定分箱已经得到证明；这些集合 只用于估计其被保留的被积函数。

<span id="lem:bin-contour-accounting" label="lem:bin-contour-accounting">\[lem:bin-contour-accounting\]</span> 假设定义 [\[def:stage-high-data\]](#def:stage-high-data) 的数据。固定 \(\sigma_0\in[7/8,1)\) 且 \(\beta_*>\sigma_0\)，并令 \(z_0=17/50\)。 设 \(0<d_{\min}<d_{\max}<\infty\)，\(U=Z^d\) 且 \(d_{\min}\le d\le d_{\max}\)，并设 \(\mathcal B\) 为 引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 的某个被保留分箱 \((i,a)\) 中满足 \(q_u\asymp U\) 的 物理行 \(u\) 的有限集。\(q_u\asymp U\) 中的比较常数固定。令 \(\delta=2a-1\)，取如该引理中的 \(0<e<10^{-3}\)， 并设 \(T_1=Z^\tau>2\)，其中 \(0<\tau\le d_{\min}/100\)。 实范围与 \(e\) 的选取独立于目标。

分箱 \(\mathcal B\) 在任何 Mellin 变量被移动之前固定。在 方程 [\[eq:stage-central-contours\]](#eq:stage-central-contours) 的被保留中心围道上，假设存在分解 \[\mathfrak H_{\eta,u,Z}(s,w,z)
       =\sum_{\lambda\in\Lambda}
             \mathfrak H^{(\lambda)}_{\eta,u,Z}(s,w,z),\] 其中 \(\Lambda\) 有限、非空且在 \(Z\) 之前固定。这一等式 只在被保留围道上要求；各求和项不必在远离 这些围道处全纯。对每个 \(\lambda\) 与每个被保留的 \((s,w,z)\)，假设 \(\mathcal B\) 被划分成至多 \(C(1+\log Z)^D\) 个集合 \(\mathcal B_{\lambda,\nu}(s,w,z)\)，其中 \(C,D\) 固定。对每个集合在 每个被保留点，设 \(R,g\) 为某个固定有界范围内的实数。假设，对固定的 \(\varepsilon_c\ge0\) 与有限的 \(A_\eta\ge0\)， \[\sum_{u\in\mathcal B_{\lambda,\nu}(s,w,z)}
  \left|L^S(w,\chi_\bullet(u))
       \mathfrak H^{(\lambda)}_{\eta,u,Z}(s,w,z)\right|
 \ll_\eta U^{R+\delta/2+\varepsilon_c}
 Z^{\ell(z_0-1/2)+g+\varepsilon_c}(1+T_1)^{A_\eta}.
 \label{eq:stage-central-bound}\] 该界在被保留点、行集与移动标签中一致。 数 \(\varepsilon_c\) 与 \(R,g\) 的有界范围在 目标之前固定；\(R,g\) 可依赖于 \(d,a\)、逐点集合与全局数 \(\beta_*\)，但不以其他方式依赖于 \(\eta\)。设 \(\mathcal P_Z\) 为 该分解中在任何被保留点出现的所有 数对 \((R,g)\) 的集合。

这里“被保留”具有如下精确的高度含义。一次列出 在验证 方程 [\[eq:stage-central-bound\]](#eq:stage-central-bound) 时进入某个带缓冲的 \(L\)-值、 倒数或对数导数的所有外部坐标 \(v_1,\ldots,v_m\)，并 包含所有三个原始 Mellin 高度，当它们不出现在某个变元中时系数取零。经过 纯扭转平移之后，每个这样的变元 具有虚部 \(\gamma_j+\sum_{k=1}^m a_{jk}v_k\)，其中有限矩阵 \((a_{jk})\) 固定且 \(|\gamma_j|\le(3i+1)T_1\)。限制 \[|v_k|\le c_kT_1,\qquad
 c_k=\frac1{2m(1+\max_j|a_{jk}|)}.
 \label{eq:stage-height-allocation}\] 系数为零的坐标可以按同样的规则限制。 于是每个新增高度的总和至多为 \(T_1/2\)。 固定的有界扩大通过提高 \(Z\) 的下阈值来纳入。 若使用额外的 Mellin 积分来确立 方程 [\[eq:stage-central-bound\]](#eq:stage-central-bound)，则该不等式在那些积分之后 对其整个左侧被要求成立。任何被丢弃的部分都必须 留在其全局或绝对直线上，由 引理 [\[lem:external-contour-tails\]](#lem:external-contour-tails) 或 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 界定，并在 假设被断言之前包含在所示界中。容许量 \(T_1/2\) 在 接连的估计中不会被更新。

与数对 \((R,g)\) 相关联的公共理想指数为 \[E_{\sigma_0}(d;R,g)=a-\sigma_0+h(z_0-1/6)-a l_y-\ell/2+g
                  +d(R+\delta/2-z_0).
 \label{eq:stage-high-exponent}\] 若 \(\mathcal B\) 为空，则其贡献为零。否则令 \[E^{\max}_{\sigma_0,Z}(d)
   =\sup_{(R,g)\in\mathcal P_Z}E_{\sigma_0}(d;R,g).\] 对每个 \(\varepsilon_d,\varepsilon_p>0\)，\(\mathcal B\) 在中心围道上的 总贡献对充分大的 \(Z\) 为 \[\begin{split}
 \ll_\eta{}& Z^{C(\sigma_0)+E^{\max}_{\sigma_0,Z}(d)+(16-6l_y)e}\\
 &\cdot Z^{(1+d)\varepsilon_c+d\varepsilon_d+\varepsilon_p}
       (1+T_1)^{A_\eta}.
 \end{split}
 \label{eq:stage-central-contribution}\] 上确界有限，因为这些数对位于一个固定有界范围内。 幂 \(\varepsilon_p\) 吸收逐点对数重数。 不声明关于逐点片段或行集的单独积分。 此围道移动中所有被丢弃部分与水平衔接对每个固定 \(N\) 都是 \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\)，其中 \(B_\eta\) 有限且在 \(N\) 之前固定。

把引理 [\[lem:fixed-bin-contour\]](#lem:fixed-bin-contour) 应用于原始三重积分， 对其三个长方体常数使用方程 [\[eq:stage-height-allocation\]](#eq:stage-height-allocation) 中 相应的 \(c_k\)。这些常数为正且至多为 \(1/2\)。 因此完整修正与固定分箱在任何逐点片段 被引入之前给出被保留积分与所断言的误差。任何用于中心界的 辅助积分都受陈述中额外假设的约束。

现在使用中心分解并构造 逐点集合 \(\mathcal B_{\lambda,\nu}\)。在每个被保留点对 原始行和施加三角不等式，然后对 该点存在的集合应用 方程 [\[eq:stage-central-bound\]](#eq:stage-central-bound)。 逐点至多有 \((1+\log Z)^D\) 的固定倍数个这样的集合。 把它们的每个指数用 \(\mathcal P_Z\) 上的上确界来界定，并 只对原始全纯行和积分。于是既不需要个别逐点细分的 可测性，也不需要横跨围道点的一个公共标签集。在 被保留围道上， 引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 把倒数界定为 \(O_{\eta,e,\varepsilon_d}(U^{\varepsilon_d})\)。这些检验函数具有 一致有界的联合 \(L^1\) 范数，因为变换 \((\Im s,\Im z,\Im w)\mapsto(\Im(s+z),\Im z,\Im w)\) 可逆。 标量因子 \(\zeta_F^S(6z_0)\) 绝对有界。剩下要 计算 \(Z\) 的实幂。

外部因子，包括 \(q_u^{-z_0}\) 以及 方程 [\[eq:stage-central-contours\]](#eq:stage-central-contours) 中的实位移，贡献 \[l_x(1/2-z_0)+a+z_0-1-a l_y-dz_0+(16-6l_y)e.\] 方程 [\[eq:stage-central-bound\]](#eq:stage-central-bound) 增加 \(d(R+\delta/2+\varepsilon_c)+\ell(z_0-1/2)+g+\varepsilon_c\)。 倒数增加 \(d\varepsilon_d\)。减去 \(C(\sigma_0)=\sigma_0+l_x/2-1+h/6\) 并利用 \(h=1-l_x+\ell\)，给出方程 [\[eq:stage-high-exponent\]](#eq:stage-high-exponent) 以及 方程 [\[eq:stage-central-contribution\]](#eq:stage-central-contribution) 中的其余项。 逐点对数重数被 \(Z^{\varepsilon_p}\) 界住，对充分大的 \(Z\)。这就证明了该断言。

该引理把修正的两种用途区分开来。它的全纯性以及 全高度优势函数为在按逐点大小细分各行之前所进行的围道移动提供了依据。 方程 [\[eq:stage-central-bound\]](#eq:stage-central-bound) 中的各片段仅在移动之后使用；它们 可以用局部除法来定义，而这类除法的非零性已在那个被保留的区域上得到证明。 这样的除法在该区域之外不提供任何延拓或尾部界。对于基础修正仅有一个 片段，而引理 [\[lem:buffered-bins\]](#lem:buffered-bins) 给出中心假设中出现的反射分子 因子 \(U^{\delta/2+12e+\epsilon}\)。

#### 提取主信号

中间行估计剩下主行以及两个外部范数区间。我们首先跨过主行中的 两个标量极点。下面的表述还记录了另一个修正具有相同目标信号的 精确条件。

<span id="lem:principal-residue-interface" label="lem:principal-residue-interface">\[lem:principal-residue-interface\]</span> 假设定义 [\[def:stage-high-data\]](#def:stage-high-data) 与 方程 [\[eq:shared-principal-nonvanishing\]](#eq:shared-principal-nonvanishing)。固定 \(\sigma_0\in[7/8,1)\)，其中 \(\beta_*>\sigma_0\)，且 \(0<e<10^{-3}\)。 假设对每个 \(\epsilon>0\)，关于 \[\Re s=\beta_*+e,\qquad 19/20\le\Re w\le1+e,
 \qquad 33/200\le\Re z\le1/6+e,\] 上的所有虚部一致地，有 \[|\mathfrak H_{\eta,1,Z}(s,w,z)|
 \ll_{\eta,e,\epsilon} Z^{\ell\Re z+\epsilon}
  (1+|\Im s|+|\Im w|+|\Im z|)^{J_{\eta,e,\epsilon}},
 \label{eq:principal-correction-bound}\] 其中 \(J_{\eta,e,\epsilon}\) 有限，并在任何外部尾部阶之前固定。 还假设对每个充分大的实 \(Z\) 有 \(A_\eta(Z)\ne0\)， 对每个 \(\epsilon>0\) 有 \(|A_\eta(Z)|^{-1}\ll_{\eta,\epsilon}Z^\epsilon\)，并且在 \(\Re s=\beta_*+e\) 上关于 \(\Im s\) 一致地， \[\mathfrak H_{\eta,1,Z}(s,1,1/6)
 =H_\eta(s)Z^{\ell/6}A_\eta(Z)(1+\mathcal R_{\eta,Z}(s)).
 \label{eq:principal-correction-residue}\] 这里或者 \(\mathcal R_{\eta,Z}\) 恒等于零，或者存在一个数 \(\mu>0\)，独立于 \(\eta\) 选取，使得 \(|\mathcal R_{\eta,Z}(s)|\ll_\eta Z^{-\mu}\) 在该整条直线上成立。

设 \(\mathscr P_\eta(Z)\) 为 方程 [\[eq:stage-high-identity\]](#eq:stage-high-identity) 的 \(u=1\) 项，并定义 \[f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
    Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds.\] 于是 \(c_S>0\)，且对每个 \(\epsilon>0\)， \[\begin{aligned}
 \frac{\mathscr P_\eta(Z)}{c_SA_\eta(Z)}-f_\eta(Z)
 \ll_{\eta,e,\epsilon}{}&
 Z^{C(\beta_*)+(1+h)e-l_y/20+\epsilon}
 +Z^{C(\beta_*)+e-h/600+\epsilon}\notag\\
 &+Z^{C(\beta_*)+e-\mu+\epsilon}.
 \label{eq:principal-remainder-bound}\end{aligned}\] 当 \(\mathcal R_{\eta,Z}\) 恒等于零时，最后一项被省略。 隐含常数与下阈值可以依赖于目标，但所显示的实指数不依赖。

对 \(u=1\)，高恒等式中的标量因子是 \[\frac{\zeta_F^S(6z)\zeta_F^S(w)}{L_F^S(s,\eta)}.\] 在绝对围道上分离出该项。移动到 \(\Re s=\beta_*+e\)、\(\Re w=1+e\) 以及 \(\Re z=1/6+e\)。 倒数保持在 \(\Re s>\beta_*\) 中，且两个 zeta 自变量都保持在 1 的右侧。 这些路径位于 \(\mathcal D_2\) 中，故修正全纯。全高度优势函数以及 引理 [\[lem:external-contour-tails\]](#lem:external-contour-tails) 为水平极限提供了依据。

将 \(w\) 移到 \(19/20\)，跨过它在 \(w=1\) 处的单极点。在该留数中把 \(z\) 移到 \(33/200=1/6-1/600\)，跨过它在 \(z=1/6\) 处的单极点。 未取留数的 \(w\) 积分保持 \(\Re z=1/6+e\)。所有这些路径都位于 \(\mathcal D_2\) 中，且 \(M(z)\) 在 \(\Re z>0\) 上全纯。 于是所陈述的两个标量极点是仅被跨过的极点。倒数始终保持在 它的全局直线上，即使当 \(\eta\) 是主特征时也是如此。 用于界定尾部的每一条延拓的竖直 \(w\)- 轴或 \(z\)- 轴都严格位于其标量极点的 一侧；\(w=1\) 与 \(z=1/6\) 只作为留数出现，且水平连接具有大的非零高度。 在这些轴上 zeta 函数具有固定的多项式界。因此 引理 [\[lem:external-contour-tails\]](#lem:external-contour-tails) 的积分估计与迹估计可以在其优势函数中 没有未移除极点的情况下适用。 在 \(w\) 留数之后，它的 Mellin 因子已成为常数 \(\widehat W_1(1)\)。剩余的高度使用 方程 [\[eq:external-two-dimensional-kernel\]](#eq:external-two-dimensional-kernel) 中的二维核，其中 \((y_1,y_2)=(\Im(s+z),\Im z)\)；它的迹估计为随后的 \(z\)-连接提供了依据。

在主围道上，方程 [\[eq:principal-correction-bound\]](#eq:principal-correction-bound) 与外部幂给出原始指数 \[\frac{l_x}{2}+\Re s-1+h\Re z+l_y(\Re w-1).\] 对未取留数的 \(w\) 积分这是 \(C(\beta_*)+(1+h)e-l_y/20\)；对 \(w\) 留数中剩余的 \(z\) 积分它是 \(C(\beta_*)+e-h/600\)。\(\Re s=\beta_*+e\) 上的倒数具有其固定目标导子的 任意小幂次以及高度的固定多项式，依据 引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control) 和 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors)。 检验函数对这些高度幂进行积分。要求修正中与 \(A_\eta^{-1}\) 中的小幂次 充分小，即给出方程 [\[eq:principal-remainder-bound\]](#eq:principal-remainder-bound) 的前两项。

标量留数的乘积是 \(c_S\)：\(\zeta_F^S(6z)\) 在 \(1/6\) 处的留数是 \(\zeta_F^S(v)\) 在 1 处的留数的六分之一。\(c_S\) 的正性在定义正规化时 已被证明。

在双重留数处，外部幂是 \[X^{1/3}Z^{s-5/6}Z^{\ell/6}=Z^{C(s)},
 \qquad \Phi(s+1/6-1)=e^{(s-5/6)^2}.\] 因此方程 [\[eq:principal-correction-residue\]](#eq:principal-correction-residue) 使正规化的双重留数成为 \[\frac1{2\pi i}\int_{(\beta_*+e)}
 Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}
          (1+\mathcal R_{\eta,Z}(s))\,ds.\] 当存在时，误差因子在该直线上被估计；全局倒数界与 Gauss 函数给出 \(O_{\eta,e,\epsilon}(Z^{C(\beta_*)+e-\mu+\epsilon})\)。 不需要对该误差因子作延拓。

只把主积分向右移到 \(\Re s=2\)。由 \(\beta_*\) 的定义以及在一之外的 绝对 Euler 收敛性，倒数在 \(\Re s>\beta_*\) 上全纯。在主极点处它的倒数 有一个零点，因此该情形不增加留数。函数 \(H_\eta\) 由 引理 [\[lem:local-euler\]](#lem:local-euler) 在该处全纯，并由 方程 [\[eq:shared-principal-nonvanishing\]](#eq:shared-principal-nonvanishing) 在该处有界。全局倒数估计在 固定的实带形域上关于高度是一致多项式的，而 Gauss 函数是 \(O(e^{-(\Im s)^2})\)。因此矩形围道的水平边趋于零，移动后的积分恰好是 \(f_\eta(Z)\)。 这也涵盖 \(\beta_*=1\) 的情形。三个余项给出所断言的界。

本引理中的函数 \(H_\eta\) 是未修改的标量 Euler 乘积在双重留数处的修正。 只有当另一个完整修正以非零正规化因子验证 方程 [\[eq:principal-correction-residue\]](#eq:principal-correction-residue) 时，它才被允许使用。对基础修正， 该方程以 \(A_\eta=1\) 与 \(\mathcal R_{\eta,Z}=0\) 成立。在任何应用中正规化的 物理量是 \(\mathscr I_\eta/(c_SA_\eta)\)；对它的直接估计以及这一主比较都必须 使用同一正规化因子。在此除法之后，原始的中央界与外部行界只获得一个 任意小的附加幂次，依据关于 \(A_\eta^{-1}\) 的假设。

###### 基础修正。

取 \(l_x=l_y=h=1/2\) 与 \(\ell=0\)。在 引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 的主矩形上，局部修正对每个高度 一致有界，因为该矩形位于 \(\mathcal D_2\) 中。因此 方程 [\[eq:principal-correction-bound\]](#eq:principal-correction-bound) 以 \(\ell=0\) 与高度阶零成立。 在双重留数处它恰好满足 \[\mathfrak H_{\eta,1,Z}(s,1,1/6)=H_\eta(s)
       =H_\eta(s)Z^{\ell/6}\cdot1\cdot(1+0).\] 因此 \(A_\eta=1\)，且留数误差恒等于零。在行 \(u=1\) 中，外部因子 \(q_u^{-z}\overline{\xi(u)}\) 为 1；唯一的因子 \(1/6\) 已由 \(\zeta_F^S(6z)\) 的留数包含在 \(c_S\) 中。因此 引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 仅有它的两个余项。 它们在损失之前的节省是 \[m_w=\frac{l_y}{20}=\frac1{40},\qquad
 m_z=\frac h{600}=\frac1{1200}.\]

#### 小行范数与大行范数

带缓冲的分箱估计仅在正行指数的有界区间上需要。下面的直接界覆盖它的 两个补集。它们要求对完整修正给出显式的绝对估计，并且不使用它的中央分解。

<span id="lem:outer-row-tails" label="lem:outer-row-tails">\[lem:outer-row-tails\]</span> 假设定义 [\[def:stage-high-data\]](#def:stage-high-data)。固定 \(\sigma_0\in[7/8,1)\)，其中 \(\beta_*>\sigma_0\)，\(0<e<10^{-3}\)， \(z_0=17/50\)，以及 \(d_{\min}>0\)。对一个二进数 \(U\ge1\)，设 \(\mathscr R_\eta(U;Z)\) 表示方程 [\[eq:stage-high-identity\]](#eq:stage-high-identity) 中物理行 \(U\le q_u<2U\) 的贡献，省略 \(u=1\)。

假设对每个 \(\epsilon>0\)，对所有满足 \(q_u\le2Z^{d_{\min}}\) 的这样的行， 并且在 \((\Re s,\Re w,\Re z)=(\beta_*+e,1/2,z_0)\) 上关于所有虚部一致地， \[|\mathfrak H_{\eta,u,Z}(s,w,z)|
 \ll_{\eta,e,\epsilon}
 Z^{\ell z_0+\epsilon}q_u^\epsilon
 (1+|\Im s|+|\Im w|+|\Im z|)^{J_{\eta,e,\epsilon}}.
 \label{eq:small-correction-bound}\] 于是，对每个 \(\epsilon>0\) 与 \(1\le U\le Z^{d_{\min}}\)， \[|\mathscr R_\eta(U;Z)|
 \ll_{\eta,e,\epsilon}
 Z^{C(\beta_*)+h(z_0-1/6)-l_y/2+e+\epsilon}
       U^{63/50+\epsilon}.
 \label{eq:small-row-bound}\] 特别地，这些二进块的和是 \[\ll_{\eta,e,\epsilon}
 Z^{C(\beta_*)+h(z_0-1/6)-l_y/2+e+(63/50)d_{\min}+\epsilon}.
 \label{eq:small-row-sum}\]

对另一端，假设对每个固定的 \(v>2\) 与 \(\epsilon>0\)，对每个物理行， 在 \((\Re s,\Re w,\Re z)=(2,2,v)\) 上关于所有虚部一致地， \[|\mathfrak H_{\eta,u,Z}(s,w,z)|
 \ll_{\eta,v,\epsilon}
 Z^{\ell v+\epsilon}q_u^\epsilon
 (1+|\Im s|+|\Im w|+|\Im z|)^{J_{\eta,v,\epsilon}}.
 \label{eq:large-correction-bound}\] 记 \(B_0=l_x/2+1+l_y\)。于是，对每个二进块 \(U\)， \[|\mathscr R_\eta(U;Z)|
 \ll_{\eta,v,\epsilon}Z^{B_0+hv+\epsilon}U^{1+\epsilon-v}.
 \label{eq:large-row-bound}\] 对每个固定的 \(\zeta>0\)，若 \(\epsilon<v-1\)，它在 \(U>Z^{h+\zeta}\) 上的和是 \[\ll_{\eta,v,\epsilon}
 Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta v+\epsilon}.
 \label{eq:large-row-sum}\] 因此，固定一个充分大的 \(v\) 可使这最后一项贡献小于 \(Z\) 的任意预定幂。

由引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 之前的分类，所考虑的每一行 都具有非主分子。 对有界的单位行，分母可能是主特征；然而由 引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control) 的主特征特化，它的倒数在 \(\Re s=\beta_*+e\) 上全纯且有界。 对所有行，节 [6](#sec:detector) 中的导子界与删除根式界，连同 引理 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors)，给出 \(q_u\) 的任意小幂次以及该倒数的 固定高度多项式。

对一个小的二进块，把它的有限和移到 \((\Re s,\Re w,\Re z)=(\beta_*+e,1/2,z_0)\)。 倒数保持全局。分子是整函数，且标量 zeta 自变量保持在 1 的右侧。 这些路径可以取在 \(\mathcal D_1(3/8)\) 中：在终点处 \(\Re(s+w)=\beta_*+e+1/2>1+3/8\)，其余不等式是直接的。 全高度修正界以及引理 [\[lem:external-contour-tails\]](#lem:external-contour-tails) 为这些移动提供了 依据。在最终直线上，方程 [\[eq:hecke-growth\]](#eq:hecke-growth) 与删除界给出非主分子的 \(U^{3/5+\epsilon}\) 乘以固定高度多项式。该二进块中有 \(O(U)\) 个元素行 （包含单位因子），且 \(q_u^{-z_0}\ll U^{-z_0}\)。修正由 方程 [\[eq:small-correction-bound\]](#eq:small-correction-bound) 界住。检验函数对所有固定高度幂 进行积分。所得的行幂之外的指数，相对于 \(C(\beta_*)\)，是 \[h(z_0-1/6)-l_y/2+e,\] 而行幂是 \(1+3/5-z_0=63/50\)。要求各分量的小幂次之和等于所显示的 \(\epsilon\) 即证明方程 [\[eq:small-row-bound\]](#eq:small-row-bound)。行指数是正的，因此 在减小预备损失之后，到 \(Z^{d_{\min}}\) 的二进求和给出 方程 [\[eq:small-row-sum\]](#eq:small-row-sum)。

对每个固定的 \(Z\) 与大的二进块，把它的有限行和移到绝对直线 \((2,2,v)\)。从 \((3,3,2)\) 出发的路径保持在 \(\Re s,\Re w\ge2\) 与 \(\Re z\ge2\) 中，因此标量因子在该处全纯。对这个固定的二进块，选取 \(D\) 足够大以使其各行包含在 \(q_u\le Z^D\) 中； 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant) 与外部迹界使其水平极限趋于零。 仅用于证明这一等式成立的常数可以依赖于该固定的二进块。由 方程 [\[eq:large-correction-bound\]](#eq:large-correction-bound)，最终直线上的估计关于该二进块一致。 标量 \(L\)-因子在该处绝对有界，\(\zeta_F^S(6z)\) 也如此，且 方程 [\[eq:large-correction-bound\]](#eq:large-correction-bound) 适用。外部幂，包括修正但不包括 行计数，是 \[l_x(1/2-v)+1+v+l_y+\ell v=B_0+hv.\] \(O(U)\) 个行与 \(q_u^{-v}\) 给出 \(U^{1-v}\)；检验函数对固定高度多项式 进行积分。这就证明了方程 [\[eq:large-row-bound\]](#eq:large-row-bound)。因为 \(1+\epsilon-v<0\)，对其几何二进尾部求和给出 方程 [\[eq:large-row-sum\]](#eq:large-row-sum)。对固定的 \(\zeta>0\)，该指数中 \(v\) 的系数是 \(-\zeta\)，这就证明了最后一个断言。 原始行级数在其起始直线上绝对收敛，且所显示的界给出一个绝对可求和的 最终尾部，因此各个二进围道恒等式可以相加。数 \(v\) 以及它所要求的有限 检验阶在 \(Z\) 趋于无穷之前固定。

###### 第一阶段的各外部区间。

取 \(l_x=l_y=h=1/2\)、\(\ell=0\)、\(d_{\min}=1/63\) 与 \(\zeta=1/1000\)，如同在中间行估计中一样。对小行，直线 \((\beta_*+e,1/2,z_0)\) 位于 \(\mathcal D_1(3/8)\) 中，因为 \(\beta_*>11/12\)。局部界 \(\mathcal H_{\eta,u}\ll_\epsilon q_u^\epsilon\)， 关于所有高度一致，对所有指定的行验证了 方程 [\[eq:small-correction-bound\]](#eq:small-correction-bound)，其高度阶为零。 于是方程 [\[eq:small-row-sum\]](#eq:small-row-sum) 在损失之前具有如下相对指数： \[h(z_0-1/6)-\frac{l_y}{2}+\frac{63}{50}d_{\min}
 =\frac{13}{150}-\frac14+\frac1{50}
 =-\frac{43}{300}.\] 对大行，\((2,2,v)\) 且 \(v>2\) 位于 \(\mathcal D_2\) 中。相同的全高度局部界 对每个物理行验证了方程 [\[eq:large-correction-bound\]](#eq:large-correction-bound)。这里 \(B_0=l_x/2+1+l_y=7/4\)，因此方程 [\[eq:large-row-sum\]](#eq:large-row-sum) 具有指数 \[\frac74+\frac{501}{1000}(1+\epsilon)-\frac v{1000}+\epsilon.\] 当固定的数 \(v\) 增大时它趋于 \(-\infty\)。例如，当 \(\epsilon\le10^{-6}\) 时 \(v=4000\) 使它小于 \(-1\)，而 \(C_{\mathrm I}(\beta_*)\ge1/4\)。这绰绰有余地提供了下面所需的节省。 三个区间 \(U\le Z^{d_{\min}}\)、\(Z^{d_{\min}}<U\le Z^{h+\zeta}\) 与 \(U>Z^{h+\zeta}\) 覆盖每个物理二进块。行 \(u=1\) 已被指派给主项。

### \(11/12\) 结论

对正规化的基础探针，中央估计、主项提取与外部行估计现在给出如下 在可调损失之前的余量： \[\begin{array}{c|c}
 \text{contribution}&\text{相对于 }C_{\mathrm I}(\beta_*)\\\hline
 \text{intermediate rows}&1021/25000\\
 \text{unresidued principal }w\text{ integral}&1/40\\
 \text{remaining principal }z\text{ integral}&1/1200\\
 \text{small rows}&43/300\\
 \text{large rows }(v=4000)&>1
\end{array}\] 最小的余量来自主 \(z\) 余项。在所有实损失之后我们保留一个公共的正余量， 然后对每个目标选取分析高度。物理和与信号不依赖于该高度。

#### 选取最终高度

前面的估计把实幂次与分析高度 \(T_1\) 的有限幂次分离开来。下面的初等步骤 记录了为对每个目标获得一个幂次节省所需的选择次序。

<span id="lem:late-height-closure" label="lem:late-height-closure">\[lem:late-height-closure\]</span> 固定 \(\sigma_0\in(1/2,1)\)，其中 \(\Delta_0=\beta_*-\sigma_0>0\)， 以及一个仿射函数 \(C(s)=s+c\)。假设某应用中所有实参数与有限结构选择 都已被固定，独立于 \(\eta\)。假设存在公共的数 \(m>0\) 与 \(0<\omega<\Delta_0\)，使得对每个本原有限阶目标，独立于 \(T_1\) 的函数 \(J_\eta,f_\eta\) 满足 \[|J_\eta(Z)|\ll_\eta Z^{C(\sigma_0)+\omega}.\] 假设在经过有限次估计求和之后，对每个整数 \(N\ge0\)， \[|J_\eta(Z)-f_\eta(Z)|
 \ll_{\eta,N} Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}
       +Z^{B_\eta}T_1^{-N},
 \label{eq:late-height-hypothesis}\] 其中 \(A_\eta\ge0\) 且 \(B_\eta\) 有限且独立于 \(N\)。 假设存在一个数 \(\tau_{0,\eta}>0\)，它在该目标的实选择与有限剖面阶之后、 但在 \(N\) 与 \(Z\) 之前固定，使得只要 \(T_1=Z^\tau\) 且 \(0<\tau\le\min\{d_{\min}/100,\tau_{0,\eta}\}\)，该估计对充分大的 \(Z\) 成立， 其中 \(d_{\min}>0\) 固定。 这个附加的上限可以编码某个先前估计中的高度条件，例如 引理 [\[lem:detector-dyads\]](#lem:detector-dyads) 中的那个。 下阈值可能依赖于 \(\eta,N,\tau\)。增大 \(N\) 被假定只改变外部检验半范数， 而不改变 \(A_\eta\) 或方程 [\[eq:late-height-hypothesis\]](#eq:late-height-hypothesis) 中已固定的实幂次。

于是 \(\tau\) 与 \(N\) 可以在 \(\eta\) 之后选取，使得 \[|J_\eta(Z)-f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-m/2}.\] 特别地，公共节省 \(\sigma=m/2\) 与所显示的低估计一起，具有 命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion) 所要求的目标量词。

对该固定的目标选取 \[0<\tau_\eta\le
 \min\left\{\frac{d_{\min}}{100},\tau_{0,\eta},
                 \frac{m}{4(A_\eta+1)}\right\},
 \qquad T_1=Z^{\tau_\eta}.\] 于是 \((1+T_1)^{A_\eta}\ll_\eta Z^{m/4}\)，因此 方程 [\[eq:late-height-hypothesis\]](#eq:late-height-hypothesis) 中的第一项是 \(O_\eta(Z^{C(\beta_*)-3m/4})\)。接着选取一个固定的整数 \(N\)，使得 \[B_\eta-N\tau_\eta<C(\beta_*)-m/2.\] 这是可能的，因为 \(\tau_\eta>0\) 且 \(B_\eta\) 有限。第二项随后由所需的 幂次界住。在这些选择之后提高对 \(Z\) 的下阈值。\(m\) 与 \(\omega\) 都在 目标之前固定，而 \(\tau_\eta,N\) 与阈值可以依赖它。由于 \(J_\eta\) 与 \(f_\eta\) 不含 \(T_1\)，这就在不改变任一函数的情况下证明了所断言的 族范围指数。

<span id="prop:balanced-high" label="prop:balanced-high">\[prop:balanced-high\]</span> 在假设 \(\Delta_1>0\) 之下，对每个本原有限阶目标 \(\eta\) 与所有充分大的 \(Z\)， \[|J_{\mathrm I,\eta}(Z)-f_{\mathrm I,\eta}(Z)|
 \ll_\eta Z^{C_{\mathrm I}(\beta_*)-1/4800}.\] 所显示的节省独立于目标；隐含常数与下阈值可以依赖它。

取 \(l_x=l_y=h=1/2\)、\(\ell=0\) 与 \(C=C_{\mathrm I}\)。 精确恒等式与局部修正在节 [8](#sec:shared-analytic-estimates) 的开头 已被验证；方程 [\[eq:balanced-central-contribution\]](#eq:balanced-central-contribution) 估计它的中间行， 而该处的主项与外部的特化给出上面列出的余量。剩下的是选取它们的损失。

###### 选择次序。

我们给出一个公共损失预算。置 \[m_0=\frac1{1200},\qquad \epsilon_*=10^{-6},\qquad
 m=\frac1{2400},\qquad \omega=\frac{\Delta_1}{2}.\] 刚刚证明的无误差的中央、小、主与大的节省都至少是 \(m_0\)。在目标之前 固定所显示的几何、行区间与 \(v=4000\)。在行计数、分子、局部修正、 带缓冲的倒数、中央重数以及每个主或外部估计中要求损失 \(\epsilon_*\)。 为 \(O(\log Z)\) 个物理二进块保留进一步的损失 \(\epsilon_*\)。见证对与 幂部分的相对数已被包含在所要求的行计数损失中；\(O_e(1)\) 个分箱与固定的 呈现选择只付出常数。

为获得所要求的行计数损失，首先依据 \(\epsilon_*\) 选取它的预备见证、 二进与筛法损失，使其充分小。这些选择独立于目标。 确实，见证长度误差具有绝对的系数，而 命题 [\[prop:sextic-row-count\]](#prop:sextic-row-count) 的优化中的仿射斜率是一致有界的。 实际二进端点中依赖目标的常数只乘以 \(1/\log U\)，这只会改变一个固定 常数或下阈值。在包络的预饱和区间 \(0\le r,m\le22\) 上应用 引理 [\[lem:detector-dyads\]](#lem:detector-dyads)：零点探测器的末尾乘积截断在它证明较短的 见证长度之前是 \(O(U^{21})\)。它的数 \(e_0\) 只依赖于所要求的二进损失与 这些有界区间。因此我们仍可以在目标之前固定 \[0<e<\min\{10^{-3},\epsilon_*,e_0\}.\]

以 \(\epsilon_r=\epsilon_n=\epsilon_H=\epsilon_*\)，这给出 \(\varepsilon_c\le15\epsilon_*\)。由于 \(d\le501/1000<1\)， 方程 [\[eq:balanced-central-contribution\]](#eq:balanced-central-contribution) 中的显式中央损失，连同保留的 物理二进块损失，至多为 \[13\epsilon_*+2(15\epsilon_*)+\epsilon_*+\epsilon_*+\epsilon_*
 =46\epsilon_*<\frac1{4800}=\frac{m_0}{4}.\] 两个主损失至多为 \((3/2+1)\epsilon_*\) 与 \(2\epsilon_*\)；小行损失至多为 \(2\epsilon_*\)。每一个都小于 \(m_0/4\)。所显示的大行估计已经用掉了它要求的 损失。因此所有这些项，在除以固定的 \(c_S\) 之后，保留 至少 \(3m_0/4=1/1600\)（在高度因子之前）。我们只使用 \(m=1/2400\)，在下面留出进一步的幂次 \(1/4800\)。

剩下要检查高度假设何时成立。设 \(\epsilon_{\rm det}>0\) 为上面所选定的固定二进损失，并且，在 固定一个目标之后，设 \(A_{{\rm det},\eta}\) 支配它使用 引理 [\[lem:detector-dyads\]](#lem:detector-dyads) 时的有限多个阶。置 \[\tau_{0,\eta}
 =\frac{d_{\min}\epsilon_{\rm det}}
        {20(A_{{\rm det},\eta}+1)}>0.\] 对 \(0<\tau\le\tau_{0,\eta}\) 与充分大的 \(Z\)， \[(1+Z^\tau)^{A_{{\rm det},\eta}}
 \le Z^{d_{\min}\epsilon_{\rm det}/10}
 \le U^{\epsilon_{\rm det}/10}
 \qquad(d\ge d_{\min}).\] 这在物理范围上一致地验证了探测器高度条件。来自 \(1+Z^\tau\le2Z^\tau\) 的固定因子被下阈值吸收。我们还如分箱所要求地 施加 \(\tau\le d_{\min}/100\)。 用于建立各见证的内部尾部阶是在这个 \(\tau\) 之后选取的，并且与下面的 最终外部阶 \(N\) 分开。 它们的增大不会改变所保留的剖面或高度阶。那些内部选择所引入的任何固定 常数都通过提高下阈值而被吸收进未使用的幂次 \(1/4800\) 中，而下阈值可以 依赖于 \(\eta\) 与 \(\tau\)。

对每个最终的整数 \(N\ge0\)，引理 [\[lem:fixed-bin-contour\]](#lem:fixed-bin-contour) 把被丢弃的高部分与连接界住为 \(O_{\eta,N}(Z^{B_\eta}T_1^{-N})\)，其中 \(B_\eta\) 在 \(N\) 之前固定。 有界的实区间与行区间以及有限的分箱集合允许对所有中央二进块取同一个 \(B_\eta\)。 把 \(O(\log Z)\) 个二进块求和可以通过把 \(B_\eta\) 增加一来吸收， 同样在 \(N\) 之前。合并前面的估计给出 \[|J_{\mathrm I,\eta}(Z)-f_{\mathrm I,\eta}(Z)|
 \ll_{\eta,N}Z^{C_{\mathrm I}(\beta_*)-m}(1+T_1)^{A_\eta}
       +Z^{B_\eta}T_1^{-N}\] 对某个有限的 \(A_\eta,B_\eta\)，只要 \(0<\tau\le\min\{d_{\min}/100,\tau_{0,\eta}\}\) 且 \(Z\) 充分 大。两个函数都独立于 \(T_1\)。 命题 [\[prop:balanced-low\]](#prop:balanced-low)，以损失 \(\omega\) 应用并除以 同一个固定的 \(c_S\)，提供 \[|J_{\mathrm I,\eta}(Z)|\ll_\eta
 Z^{1/4+\omega}=Z^{C_{\mathrm I}(11/12)+\omega},
 \qquad 0<\omega<\Delta_1.\] 引理 [\[lem:late-height-closure\]](#lem:late-height-closure) 的所有假设现在都被验证。 它给出命题中所断言的节省 \(m/2=1/4800\)。

#### 向 Dirichlet \(L\) 函数 的转移

延拓准则涉及 \(F\) 上的 Hecke 族。我们证明一次：该族的严格无零点半平面具有相应的 Dirichlet 推论。

<span id="prop:hecke-dirichlet-transfer" label="prop:hecke-dirichlet-transfer">\[prop:hecke-dirichlet-transfer\]</span> 设 \(\sigma_0\in[1/2,1)\)。假设 \(F=\mathbb Q(\sqrt{-3})\) 上的每个本原有限阶 Hecke \(L\) 函数在 \(\Re s>\sigma_0\) 上无零点，允许其在 \(1\) 处的主极点。那么 \(F\) 上的每个 有限阶 Hecke \(L\) 函数以及每个 Dirichlet \(L\) 函数在同一严格半平面上无零点，同样 允许在 \(1\) 处的主极点。

从本原 Hecke 特征过渡到它所诱导的特征，只改变有限多个因子 \(1-\eta(\mathfrak p)N\mathfrak p^{-s}\)。它们在 \(\Re s>0\) 上非零，因此 Hecke 论断延伸到所有有限阶特征。对因子 \(1-\chi(p)p^{-s}\) 的相同观察把 Dirichlet 论断归约为导子为 \(q\) 的本原 Dirichlet 特征 \(\chi\)。

设 \(\chi_{-3}\) 为导子为三的二次特征，设 \(\eta\) 为通过与 \(3q\) 互素的理想上的 \(\mathfrak a\mapsto\chi(N\mathfrak a)\) 给出的有限阶 Hecke 特征。 它是射线特征：若 \(\alpha\equiv1\pmod{q\mathcal O}\)，则 \(N\alpha\equiv1\pmod q\)，所以范数特征在相应的主射线子群上平凡。设 \(S_{\mathbb Q}\) 为整除 \(3q\) 的有理素数，设 \(\mathcal S_{\mathbb Q}\) 为 \(F\) 上位于其上的素数。以这些集合作上标 表示删去这些 Euler 因子。

对 \(p\notin S_{\mathbb Q}\)，局部因子如下相符。若 \(p\) 在 \(F\) 中分裂，则 \(\chi_{-3}(p)=1\)，两个素理想的范数为 \(p\)， Hecke 因子为 \((1-\chi(p)p^{-s})^{-2}\)。这是 \(\chi\) 与 \(\chi\chi_{-3}\) 的 Dirichlet 因子之积。若 \(p\) 是惰性的， 则 \(\chi_{-3}(p)=-1\)，唯一素理想的范数为 \(p^2\)，其 因子为 \[(1-\chi(p)^2p^{-2s})^{-1}
  =(1-\chi(p)p^{-s})^{-1}(1+\chi(p)p^{-s})^{-1}.\] 这些穷尽了 \(S_{\mathbb Q}\) 之外的素数。\(\Re s>1\) 上的绝对 Euler 收敛性，继之以亚纯延拓的唯一性，给出 \[L_F^{\mathcal S_{\mathbb Q}}(s,\eta)
 =L^{S_{\mathbb Q}}(s,\chi)
      L^{S_{\mathbb Q}}(s,\chi\chi_{-3}).
 \label{eq:hecke-dirichlet-factorization}\] 右端的乘积特征可能是非本原的；删去 \(S_{\mathbb Q}\) 使该恒等式不依赖于这一选择。每个 被删去的因子在 \(\Re s>0\) 上非零。

两个 Dirichlet 因子在 \(0<\Re s<1\) 上全纯。因此 \(L(s,\chi)\) 在 那里的零点将给出 Hecke 因子的零点，且 不被极点抵消，而当 \(\Re s>\sigma_0\) 时假设的 Hecke 半平面排除了它。 绝对 Euler 收敛性处理 \(\Re s>1\)。 在 \(s=1+it\)（\(t\ne0\)）上，两个 Dirichlet 因子都没有极点，所以同样的 乘积论证适用。

在 \(s=1\) 处，只有当 \(\chi\) 与 \(\chi\chi_{-3}\) 中有一个本原 诱导特征是主特征时，才可能发生极点-零点相消。那么 另一个将是 \(\chi_{-3}\)。其 Dirichlet 级数在 \(1\) 处收敛， 这是由非主周期特征的有界部分和保证的，将连续项 分组给出 \[\begin{split}
 L(1,\chi_{-3})
 &=\sum_{n\ge0}\left(\frac1{3n+1}-\frac1{3n+2}\right)\\
 &=\int_0^1\frac{1-x}{1-x^3}\,dx
   =\int_0^1\frac{dx}{1+x+x^2}
   =\frac{\pi}{3\sqrt3}>0.
 \end{split}\] 第一个积分由非负配对被积函数的单调收敛性得到。因此在这最后一种情形 也没有零点；允许主极点。这证明了严格半平面论断， 而对其边界不作任何断言。

假设 \(\beta_*>11/12\)。引理 [\[lem:local-euler\]](#lem:local-euler) 与 方程 [\[eq:shared-principal-nonvanishing\]](#eq:shared-principal-nonvanishing) 对每个 本原目标给出 \(\Re s>11/12\) 上所需的、全纯且非零的 \(H_\eta\)。 命题 [\[prop:balanced-high\]](#prop:balanced-high) 及其证明中建立的低界与高界验证了 命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion)，其中 \[\sigma_0=\frac{11}{12},\qquad C=C_{\mathrm I},\qquad
 \omega=\frac{\Delta_1}{2},\qquad \sigma=\frac1{4800}.\] 这两个正损失与目标无关，而允许的 常数、排除集与阈值可以依赖于它。延拓 准则与假设矛盾。因此 \(\beta_*\le11/12\)。 按定义以及 \(\Re s>1\) 中的绝对 Euler 收敛性，\(F\) 上的每个 本原有限阶 Hecke \(L\) 函数在严格 半平面 \(\Re s>11/12\) 上无零点，允许主极点。

命题 [\[prop:hecke-dirichlet-transfer\]](#prop:hecke-dirichlet-transfer) 在同一边界处应用， 把该论断延伸到所有有限阶 Hecke 特征与所有 Dirichlet \(L\) 函数，包括 \(\zeta(s)\)。它保持严格半平面与 允许的主极点。这证明了定理。

# 八分之七无零点半平面

### 补偿探针

定理 [\[thm:eleven-twelfths\]](#thm:eleven-twelfths) 适用于进入方程 [\[old-eq:1.1b\]](#old-eq:1.1b) 中上确界的 每个本原特征，因此给出 \(\beta_*\le11/12\)。在整个第 II 部分中反设 \(\beta_*>7/8\)，并令 \[\label{eq:part-II-bootstrap}
 \Delta:=\beta_*-\frac78,\qquad 0<\Delta\le\frac1{24},
 \qquad
 \kappa:=2\beta_*-1=\frac34+2\Delta\le\frac56.\] 节 [6](#sec:detector) 中精确的分箱上界适用，因为 \(\beta_*>7/8>51/100\)。对每个保留的非主行及其分箱 \((i,a)\)，它给出 \[\label{eq:part-II-bin-ceiling}
 a\le\beta_*,\qquad \delta=2a-1\le\kappa\le\frac56.\] 确实，定义 \(M_i(u)\) 的有限集由下限 \(51/100\) 与 真实零点的实部构成，全都至多为 \(\beta_*\)。这只用到 上确界的定义，而非其达到。边界情形 \(\delta=5/6\) 仍是论证的一部分。

对于命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion) 的第二次应用， 在整个第 II 部分中记 \[\label{eq:part-II-mellin-target}
 C(s)=C_{\mathrm{II}}(s):=s-\frac{11}{16},\qquad
 C(7/8)=\frac3{16}.\] 我们的任务是由下面的有限表达式构造一个正规化探针 \(J_{\mathrm{II},\eta}\)。 它不同于平衡探针 \(J_{\mathrm I,\eta}\)。其低端目标是 \(|J_{\mathrm{II},\eta}(Z)|\ll_\eta Z^{3/16+\omega}\)，其中 \(0<\omega<\Delta\) 为公共的；其高端必须满足 方程 [\[eq:high-probe-contract\]](#eq:high-probe-contract) 中带有该 \(C\) 的信号估计。非零标量 正规化将在主项求值后指定。

对每个本原目标 \(\eta\)，使用节 [4](#sec:probe) 中 数据 \(T,S,b_*,\xi,\tau,\Xi,W_0,W_1\) 的一个容许的固定实例。 \(P_0\) 的允许选择将按下面的参数顺序作出。这些 数据可以不同于第 I 部分中所用的数据，但在本应用内它们 与 \(Z\) 无关，且在物理探针与其高 表示中相同。

我们先在原探针上定义两项修正，然后再 移动任何围道。随后的低端与高端估计将涉及 这同一个有限表达式。

使用固定的几何 \[\begin{gathered}
 b=\frac18,\qquad h=\frac{13}{16},\qquad \ell=\frac16,\\
 l_x=1+\ell-h=\frac{17}{48},\qquad
 l_y=l_x+b=\frac{23}{48},\\
 X=Z^{l_x},\qquad Y=Z^{l_y},\qquad
 M=l_x+l_y=\frac56,\qquad M+\ell=1.
 \end{gathered}
 \label{old-eq:5.1}\] 固定总长度为 \(\ell\) 的正槽长 \(\ell_1,\ldots,\ell_K\)， 并令 \(P_i=Z^{\ell_i}\)。每个物理槽具有 非负、非零的光滑环形权重 \(W_i(q_p/P_i)\)。其允许的 素数集为 \[\mathcal P_i(Z)=\{p\text{ prime}:p\notin S,\ p\in1_T,
                         \ q_p/P_i\in\operatorname{supp}W_i\}.\] 在施加射线与 \(S\) 限制之前，要求不同槽的 底层窗口集 \(\{p\text{ prime}:q_p/P_i\in\operatorname{supp}W_i\}\) 互不相交。 特别地，集合 \(\mathcal P_i(Z)\) 互不相交，且 \(\prod_i\mathcal P_i(Z)\) 中的每个元组都由不同的素数组成。 槽的数目与长度将在后面选择，但它们 独立于 \(Z\) 而固定。下面对槽 \(i\) 的 \(p\in1_T\) 求和 始终保留这同样的排除与环形支撑。

对槽素数的无平方因子乘积 \(D\)，用 \(I_{\eta;D}(X,Y,Z)\) 表示在其完备化行中插入 指示函数 \(1_{D\mid cn^3}\) 的方程 [\[eq:general-probe\]](#eq:general-probe)。 于是 \(I_{\eta;1}=I_\eta\)。对元组 \((p_1,\ldots,p_K)\in\prod_i\mathcal P_i(Z)\) 与 \(J\subseteq\{1,\ldots,K\}\)，记 \(p_J=\prod_{i\in J}p_i\)，其中 \(p_\varnothing=1\)。子集 \(J\) 索引重标度的槽，\(J^c\) 索引带标记的槽；这一子集记号不同于正规化 探针 \(J_{\mathrm{II},\eta}\)。由有限恒等式定义修正探针 \[\label{eq:compensated-probe-definition}
\begin{split}
 I_{\eta,\mathrm{modified}}(Z)
 =\sum_{(p_i)\in\prod_i\mathcal P_i(Z)}\prod_{i=1}^K W_i(q_{p_i}/P_i)
 \sum_{J\subseteq\{1,\ldots,K\}}&(-1)^{|J|}q_{p_J}^{-3/2}
          \overline{\eta(p_{J^c})}\\
 &\cdot I_{\eta;p_{J^c}}
       (X/q_{p_J},Y/q_{p_J},Zq_{p_{J^c}}).
\end{split}\] 等价地，在每个素数 \(p\) 处，该运算为带标记项 \(\overline{\eta(p)}I_{\eta;p}(X,Y,Zq_p)\) 减去重标度项 \(q_p^{-3/2}I_\eta(X/q_p,Y/q_p,Z)\)。公式 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 规定了它们的复合： 每个槽窗口停留在其原始尺度 \(P_i\)，包括当 另一个槽改变了完备化尺度时。在 \(1_T\) 上，对每个 \(\theta\in\widehat T\) 有 \(\theta(p)=1\)。因此带标记与 \(\overline G\) 的 Fourier 分解 可交换，并在每个被加项中保持 同样的排除集与零点掩码。 该减法旨在抵消高端上的标量素数贡献， 留下矩估计所用的六次特征素因子。节 [5](#sec:local-compensation) 证明精确 恒等式并界定剩余的局部误差。

### 系数约定与有限相关性

我们记录关于素因子的补充系数约定， 然后证明一个固定射线素数正规化因子以及下面所需的完整有限 Fourier 相关性。后者保留共享的素数幂，并将 用于加性 Gram 界以及四阶矩。第 I 部分的 剩余符号与固定数据约定仍然有效。

#### 补充系数条件

我们使用节 [2](#sec:arithmetic) 中的普通多项式与逆多项式、环形剖面以及固定算术 数据 \(\mathcal A\)。以下条件 规定了本部分所用的额外素因子与移动零点支撑。

对数长度为 \(z_i\) 的素数槽为 \[Q_{\psi,i}=Z^{-z_i/2}\sum_{p\ {\rm prime}}
       \psi(p)\nu_i(p)W_i(q_p/Z^{z_i}).
 \label{old-eq:1.2}\] 这里 \(\nu_i\) 是一个固定的有限射线特征，或这类特征的固定有限线性 组合。它独立于该行以及 其它所选素数。在施加任何公共掩码或行零点延拓之前，不同的槽具有互不相交的底层素数 支撑。对于 节 [7](#sec:plain) 的四阶矩，一个固定的有限射线特征群 \(\Theta\) 是数据的一部分，且在每个正长度槽中系数 非零的每个特征分量都必须属于 \(\Theta\)。 节 [6](#sec:inverse) 的逆矩还允许一个有界 系数 \(a_i(p)\)，它为每个槽独立选取，并独立于 该行及所有其它列；素数元组的系数于是为 其各个槽系数之积。\(\Theta\) 限制 不适用于这些单独的逆矩权重。

对于一个辅助四阶矩，各行是元素 \(0<q_k\ll Z^m\)，且 \[\psi_k(n)=\tau(n)\chi_n(k),\qquad M=m+q.
 \label{old-eq:1.3}\] 扭曲 \(\tau\) 在其外标签固定后对其行和是公共的， 其分解为固定有限射线因子与移动 剩余符号因子的显示分解是数据的一部分。设 \(D_{\mathrm{mov}}\) 为 所有好素数的无平方因子乘积，在这些素数处至少有一个显示的移动 因子在非单位元上有其自然零点。这包括一个素数，即使 该因子有可被六整除的指数（包括指数为零），或当 局部特征在相乘后相消时。我们要求 \(q_{D_{\mathrm{mov}}}\le Z^q\)，重迭的素数只计一次。

一个附加穿孔是一个指示函数 \(1_{(n,R)=1}\)，其中 \(R\) 无平方因子， \(q_R\le Z^B\)，且 \(B\) 在一个先给定的有界范围内。它必须对 当前行和以及该和中每个普通因子与素因子都是公共的；它 可以依赖于先前冻结的外标签。一个素数只有通过将其 显示的局部因子精确分解为该互素指示函数与所保留的局部或 固定射线特征相位，才能从 \(D_{\mathrm{mov}}\) 中移出并放入 \(R\)。那些相位必须保留， 重构后的零点必须从显示的移动因子中移除，并且 公共穿孔要在节 [7](#sec:plain) 中的自然反射之前删除。 任何零点素数都不得从两个支撑中被省略。 若一个在该素数处仍然分歧的移动特征保留下来，该素数就留在 \(D_{\mathrm{mov}}\) 中；只有多余的零点可以转移到 \(R\)。 这里一个固定的有限射线特征具有其完整的零点延拓表示， 且其射线群按前述意义固定；一个具有移动导子的特征 不能被重新标记为固定。一个局部冻结的移动扭曲因子或 多余零点掩码保留所述的移动支撑与穿孔 要求。特别地，一个随 \(Z\) 变化的多余掩码不能包含 在固定算术数据中。\(\chi_n(k)\) 的零点延拓允许 随 \(k\) 自然变化，但该变化行因子 与固定扭曲之间的相消不可以被改写为每一行单独选取的穿孔。外部 选取的依赖行的穿孔与依赖行的列系数 不属于此类。这个全支撑约定支配 节 [7](#sec:plain) 中的每一次四阶矩调用。

公共一致性约定对这些系数类有以下附加条款。 任何所需的槽网格只依赖于固定的 实对数长度范围、严格余量与指定的正幂 损失。有限半范数阶、多项式高度阶、隐含常数 与下阈值也可以依赖于一个指定的固定槽数。 它们在移动模、包含于 \(M\) 中的根式、 容许穿孔以及处于其所述范围内的外标签上一致，即使 某个外标签在一次行和期间被固定。除子有界重数定义中的 常数 \(C\) 也可以依赖于这个固定槽数。 \(C\) 与 \(Z\)、当前各行以及被平均标签的独立性， 以及重数只依赖于 \(f\) 的任何单独要求，都保持 如节 [2](#sec:arithmetic)。槽数是一个单独的固定 参数，移动标签仍在 \(\mathcal A\) 之外。

#### 固定射线类中的素数计数

<span id="lem:ray-prime-normalizer" label="lem:ray-prime-normalizer">\[lem:ray-prime-normalizer\]</span> 设 \(T\) 为 \(F\) 的射线类群的一个固定商，当某个非分歧素理想的像是单位元时 记 \(p\in1_T\)。 对一个固定的非负、非零光滑环形权重 \(W\)， \[\label{eq:ray-prime-normalizer}
 \sum_{p\in1_T}W(q_p/P)q_p^{-5/6}
 \sim\frac{P^{1/6}}{|T|\log P}
      \int_0^\infty W(y)y^{-5/6}\,dy.\] 删去任何进一步的固定有限素数集不改变这一 渐近。其下阈值可以依赖于所有固定数据。

对于对应于 \(T\) 的 \(F\) 的固定阿贝尔扩张，固定 Frobenius 类中的素理想 定理给出 \[\pi_{1_T}(x):=\#\{p\in1_T:q_p\le x\}
       \sim\frac{\operatorname{Li}(x)}{|T|}.\] 这是  中 Chebotarev 的固定扩张推论； 该扩张及其导子在 \(x\to\infty\) 时固定。若 \(\operatorname{supp}W\subset[a,b]\subset(0,\infty)\)， 则当 \(P\to\infty\) 时误差 \(o(x/\log x)\) 对 \(aP\le x\le bP\) 一致。 因此当 \(d\pi_{1_T}(x)\) 被 \(dx/(|T|\log x)\) 替换时，Stieltjes 分部积分把 方程 [\[eq:ray-prime-normalizer\]](#eq:ray-prime-normalizer) 的左端改变 \(o(P^{1/6}/\log P)\)。所得积分是 \[\frac{P^{1/6}}{|T|\log P}
 \int_a^b W(y)y^{-5/6}\frac{\log P}{\log(Py)}\,dy.\] 最后的比值一致地趋于一。这证明了该公式及其 正性。一个固定有限集最终位于环形窗口之外。 没有使用关于射线导子一致的误差指数。

#### 完整有限 Fourier 相关性

我们现在允许模中有任意素数幂。下面的二元记号 \(G(a,k)\) 是一个有限 Fourier 和；它不同于引理 [\[lem:fixed-gauss-phase\]](#lem:fixed-gauss-phase) 的一元有限射线函数 \(G(a)\)。定义 \[G(a,k)=q_a^{-1/2}\sum_{x\bmod a}\chi_a(x)e(kx/a),\qquad G(1,k)=1.
 \label{old-eq:2.4}\] 本小节中所有特征都具有节 [2](#sec:arithmetic) 中指定的零点延拓， 且我们令 \(v_p(0)=+\infty\)。

<span id="lem:prime-power-fourier" label="lem:prime-power-fourier">\[lem:prime-power-fourier\]</span> 对 \(P=q_p\) 与每个整数 \(a\ge1\)， \[\begin{aligned}
 |G(p^a,k)|&=P^{(a-1)/2}1_{v_p(k)=a-1},&&6\nmid a,\\
 G(p^a,k)&=P^{a/2}1_{p^a\mid k}
             -P^{a/2-1}1_{p^{a-1}\mid k},&&6\mid a.
 \end{aligned}
 \label{eq:gauss-local}\]

把模 \(p^a\) 的剩余写成 \(x_0+py\)，其中 \(x_0\bmod p\)， \(y\bmod p^{a-1}\)。当且仅当 \(p^{a-1}\mid k\) 时对 \(y\) 的求和为零， 否则等于 \(P^{a-1}\)。在后一情形写 \(k=p^{a-1}k_0\)。 剩下的正规化和为 \[P^{a/2-1}\sum_{x_0\bmod p}\chi_p(x_0)^a e(k_0x_0/p).\] 若 \(6\nmid a\)，其内和当 \(p\mid k_0\) 时为零，否则 绝对值为 \(\sqrt P\)。若 \(6\mid a\)，内和是 加性特征在单位元上的和，即 \(P1_{p\mid k_0}-1\)。这些 恰好是命题中的两种情形。

<span id="lem:full-correlation" label="lem:full-correlation">\[lem:full-correlation\]</span> 对 \(S\) 之外的本原模 \(u,v\) 与 \(j\in\mathcal O\)，令 \[F(u,v;j)
 =\sum_{\substack{x\bmod u,\ y\bmod v\\
                    vx-uy\equiv j\pmod{uv}}}
       \chi_u(x)\overline{\chi_v(y)}.
 \label{old-eq:2.11}\] 则 \[F(u,v;j)=\frac1{\sqrt{q_uq_v}}\sum_{h\bmod uv}
 G(u,h)\overline{G(v,h)}e(-jh/(uv)).\] 在零频率处，除非 \(u=v\) 否则 \(F(u,v;0)=0\)，且 \(F(u,u;0)=\varphi(u)\)，其中 \(\varphi(u)\) 是模 \(u\) 的单位元个数。

设 \(C=(u,v)\) 并写 \(u=Cn_1\)，\(v=Cn_2\)，其中 \((n_1,n_2)=1\)。 则除非 \(C\mid j\) 否则 \(F(u,v;j)=0\)。对 \(j=Ck\)， \[\begin{aligned}
 F(Cn_1,Cn_2;Ck)
 &=\chi_{n_1}(k)\overline{\chi_{n_2}(-k)}
      \mathcal R(n_1,n_2)L_C(n_1,n_2;k),\\
 L_C(n_1,n_2;k)
 &=\sum_{\substack{x,y\bmod C\\n_2x-n_1y\equiv k\pmod C}}
       \chi_C(x)\overline{\chi_C(y)}
   =\prod_{p^c\parallel C}L_{p^c}.
 \end{aligned}
 \label{eq:correlation-lift}\] 对 \(P=q_p\) 与 \(p\nmid n_1n_2\)，局部因子为 \[L_{p^c}=P^{c-1}\chi_p(n_1/n_2)^c
 \begin{cases}
 P-1,&p\mid k,\\
 -1,&p\nmid k,\ 6\nmid c,\\
 P-2,&p\nmid k,\ 6\mid c.
 \end{cases}
 \label{eq:correlation-local}\] 若 \(p\) 恰好整除 \(n_1,n_2\) 之一，局部因子为 \(P^{c-1}(P-1)1_{6\mid c}1_{p\nmid k}\)。在真实剩余轨迹 \((n_1,n_2)=1\) 上，\(L_C\) 意指 方程 [\[eq:correlation-lift\]](#eq:correlation-lift) 中的同余和。当 \(L_C\) 用于所有剩余 对时，它反而表示这些局部 公式的人为乘积延拓，当 \(p\mid(n_1,n_2)\) 时局部值定义为零。 在真实剩余轨迹之外，这不是原来的同余和。 真实函数与这一人为延拓都满足 \(|L_C|\le q_C\)，且该延拓在每个剩余列中模 \(\operatorname{rad}C\) 周期。

在所显示的 Fourier 变换中展开两个 Gauss 和，留下 \[\frac1{q_uq_v}\sum_{x\bmod u,y\bmod v}\chi_u(x)\overline{\chi_v(y)}
 \sum_{h\bmod uv}e\bigl(h(vx-uy-j)/(uv)\bigr).\] 加性正交性使内和在同余成立时 为 \(q_uq_v\)，否则为零。若 \(j=0\) 且某个被加项非零，则 \(x\) 与 \(y\) 是 模 \(u\) 与 \(v\) 的单位元。将同余模 \(u\) 约化得 \(u\mid v\)， 模 \(v\) 约化得 \(v\mid u\)。由于生成元是本原的， \(u=v\)。该同余于是说明 \(x=y\bmod u\) 并给出 \(\varphi(u)\)。这一 论证在局部特征幂为主特征时也用到零点掩码。

\(C\) 的可除性立即可得。除以 \(C\) 后，\(j=Ck\) 的同余 为 \[n_2x-n_1y\equiv k\pmod{Cn_1n_2}.\] 模 \(n_1\) 与 \(n_2\) 的约化给出（保留零值） \[\chi_{n_1}(x)=\chi_{n_1}(k)\overline{\chi_{n_1}(n_2)},\qquad
 \overline{\chi_{n_2}(y)}
 =\overline{\chi_{n_2}(-k)}\chi_{n_2}(n_1).\] 两个单位因子之积为 \(\mathcal R(n_1,n_2)\)。 剩下的是确定模 \(C\) 同余的升高的重数。这可以 逐个素数检验。若 \(c=v_p(C)\) 且两个剩余 模都不含 \(p\)，则没有额外的升高。若比方说 \(d=v_p(n_1)>0\) 且 \(p\nmid n_2\)，则 \(y\bmod p^c\) 自由，且同余 由它唯一确定 \(x\bmod p^{c+d}\)。模 \(p^c\) 的约化 恰好是方程 [\[eq:correlation-lift\]](#eq:correlation-lift) 中的公共同余。 \(p\mid n_2\) 的情形是对称的，且这一论证包含 \(c=0\)。 因此中国剩余定理给出与 \(L_C\) 中所用公共解之间的一个 双射，即使 \(C\) 与一个剩余模相交。

对于局部计算，置 \(k_p=\mathcal O/(p)\) 与 \(A=\chi_p^c\)，即 \(k_p^\times\) 的一个零延拓特征。由于 \(n_1,n_2\) 中至少有一个 在 \(p\) 处是单位元，模 \(p\) 的每个 解有 \(P^{c-1}\) 个模 \(p^c\) 的升高。若两者都是单位元且 \(p\mid k\)，单位变量成比例，域和为 \(A(n_1/n_2)(P-1)\)。若 \(p\nmid n_1n_2k\)，置 \(y=(k/n_1)t\) 与 \(x=(k/n_2)(1+t)\)。域和变为 \[A(n_1/n_2)\sum_{t\ne0,-1}A((1+t)/t)
 =A(n_1/n_2)\sum_{z\in k_p^\times\setminus\{1\}}A(z).\] 当 \(A\) 非主时它为 \(-A(n_1/n_2)\)，当 \(A\) 为主时 为 \((P-2)A(n_1/n_2)\)。若 \(p\mid n_1\) 且 \(p\nmid n_2\)， 域方程迫使 \(x=k/n_2\)。当 \(p\mid k\) 时其特征为零。当 \(p\nmid k\) 时，对 \(y\) 的剩余求和除非 \(A\) 为主否则为零， 此时它为 \(P-1\)。另一情形是对称的。这证明了真实剩余轨迹上的所有局部 公式。当两个剩余都与 \(p\) 相交时按所规定的零 延拓它们，得到剩余列模 \(p\) 的函数， 每个的绝对值至多为 \(P^c\)。它们之积也证明了 人为延拓的最终论断；在一个新加入的对处不宣称 同余和恒等式。

对某些应用，更可取的是移除两个完整模公共的所有素数 及其全部重数。下一种形式在每个剩余乘积上留下一个 公共行特征。

<span id="lem:complete-support-correlation" label="lem:complete-support-correlation">\[lem:complete-support-correlation\]</span> 假设 \(u=Da\)，\(v=Eb\) 是本原的且在 \(S\) 之外，其中 \((a,b)=1\) 且 \((ab,DE)=1\)。则对每个 \(j\in\mathcal O\)， \[\begin{split}
 F(Da,Eb;j)={}&F(D,E;j)\mathcal R(a,E)
       \overline{\mathcal R(b,D)}\mathcal R(a,b)\\
 &\hspace{8mm}\cdot\chi_a(j)\overline{\chi_b(-j)}.
 \end{split}
 \label{eq:correlation-child-character}\] 模 \(D,E\) 可以包含任意素数幂，包括共享的辅助 素因子。

在 \(a\) 与 \(b\) 的素数处，解 方程 [\[old-eq:2.11\]](#old-eq:2.11) 中的同余分别给出 \(\chi_a(j)\overline{\chi_a(Eb)}\) 与 \(\overline{\chi_b(-j)}\chi_b(Da)\)。当 \(j\) 的某个 特征为零时，这些陈述仍然有效；只有所显示的单位因子被求逆。 在 \(DE\) 的素数处作变量替换 \(x'=bx\bmod D\)，\(y'=ay\bmod E\)。 同余变为 \(Ex'-Dy'\equiv j\pmod{DE}\)，其特征因子 改变 \(\overline{\chi_D(b)}\chi_E(a)\)。剩下的单位因子是 \[\frac{\chi_E(a)}{\chi_a(E)}
 \frac{\chi_b(D)}{\chi_D(b)}
 \frac{\chi_b(a)}{\chi_a(b)}
 =\mathcal R(a,E)\overline{\mathcal R(b,D)}\mathcal R(a,b).\] 由假设，这里所有分母都是单位元的符号。中国 剩余定理与 \(F(D,E;j)\) 的定义完成证明。

方程 [\[eq:correlation-child-character\]](#eq:correlation-child-character) 的假设不会 因把 \(\mathcal R\) 延拓为双特征而消除。为确切陈述与 Möbius 反演一起使用的延拓，固定 \(D,E,j\) 并定义 \(\widetilde F_{D,E}(a,b;j)\) 为该方程右端对所有满足 \((ab,DE)=1\)、 在 \(S\) 之外的本原 \(a,b\) 的取值，即使 \((a,b)>1\) 也保留其零符号。对此轨迹上任意有限系数阵列 \(c(a,b)\)， \[\sum_{(a,b)=1}c(a,b)F(Da,Eb;j)
 =\sum_{a,b}c(a,b)\widetilde F_{D,E}(a,b;j)
                \sum_{t\mid a,\ t\mid b}\mu(t).\] 确实，完整的内除子和为 \(1_{(a,b)=1}\)，且两个相关 表达式在该轨迹上一致。\(\widetilde F_{D,E}\) 在别处的值 是人为的，并非 \(F(Da,Eb;j)\) 的公式。特别地， 必须在逐因子估计分离两个 剩余列之前插入完整除子和；由单个除子 项引入的额外公共素数不会成为真实 \(D,E\) 相关性的素数。

### 带标记的完备化与反射行能量

<span id="sec:marked-energy" label="sec:marked-energy">\[sec:marked-energy\]</span>

补偿的低估计与逆矩使用同一个带标记的完备化。我们在此建立其反射均方。低估计将使用没有额外无平方因子标记或穿刺的情形；更一般的形式允许由逆矩的 Poisson 变换所引入的标记与掩码。

我们沿用节 [2](#sec:arithmetic) 的记号。特别地，理想变量取其乘性主生成元，固定排除集 \(S\) 包含 \(6\) 之上的素理想，且剩余符号的任意幂在非单位元上为零，即使其指数可被六整除。元素行不必无平方因子，也不必与 \(S\) 互素。

#### 完备化和与积形式的标记

固定一个有限指标集 \(I\) 以及 \(S\) 之外素理想的配对不交列表 \(\mathcal P_i\)，其中对 \(p\in\mathcal P_i\) 有 \(q_p\asymp Z^{z_i}\)。这些列表及其有界的单个系数 \(a_i(p)\) 独立于当前行与无平方因子标记。它们的名义长度 \(z_i\) 落在固定有界的区间内。

此处及下文，*固定穿刺* 指一个函数 \[\rho(n)=1_{(n,\mathfrak r_\rho)=1},\] 其中 \(\mathfrak r_\rho\) 无平方因子，且仅要求在所指示的当前行与标记求和内固定。此类函数的有界乘积具有同样形式，其中 \(\mathfrak r_\rho\) 等于其模之积的根式。该根式的范数将被显式地界住。它可以依赖于先前固定的外部理想，但不依赖于当前的任一平均变量。

设 \(f\) 为 \(S\) 之外的无平方因子理想，其中对固定有界区间内的非负 \(V\) 有 \(q_f\asymp Z^V\)，并设 \(k\in\mathcal O\)。对一个固定的乘性有限射线特征 \(\nu\)，其完整的零延拓定义模的素支集在 \(S\) 中，仅对 \(S\) 之外的无平方因子主理想 \(n\) 定义 \(a(n)\)，并对 \(S\) 之外的每个主理想 \(n\) 通过下式定义 \(\Psi_k(n)\) \[a(n)=\bar\alpha(n)\gamma_2(n)\nu(n)\rho(n),\qquad
 \Psi_k(n)=\nu(n)\rho(n)\chi_n(k)\chi_n(f)^4.\] 有限特征、穿刺以及所有槽列表均独立于 \(k,f\)。有限射线群上的固定函数在使用此定义之前总是展开为真正的群特征；因此，即使先前某一步产生了特征的有限线性组合，\(\nu\) 仍是乘性的。

对具有有界系数的配对不交素理想列表的子集 \(I'\subset I\)，通过下式定义其标记 \[\label{old-eq:4.2}
 \mathfrak d_{I'}(A)=
 \sum_{(p_i)\in\prod_{i\in I'}\mathcal P_i}
      \prod_{i\in I'}a_i(p_i)1_{p_i\mid A}.\] 当 \(I'\) 不言自明时，我们将其从记号中省略。由于这些列表配对不交，一个元组具有无平方因子的乘积。对每个固定的 \(\epsilon>0\)，整除 \(A\) 的元组数目为 \(O_\epsilon(q_A^\epsilon)\)。方程 [\[old-eq:4.2\]](#old-eq:4.2) 中的系数是个别素理想函数之积；当某些槽被分配到某个提取出的因子时，所利用的正是这一性质，而不仅仅是逐点的除子界。

对一个光滑环形 \(W\)，置 \(V_*(y)=y^{1/2}W(y)\)，并定义完备化带标记和 \[\label{eq:marked-completion}
 \mathcal T_{\mathfrak d}(X;k)=
 \sum_{\substack{n\ {\rm sf}\\b}}
 \frac{\bar\alpha(n)\gamma_2(n)\Psi_k(n)\,
       \bar\alpha(b)^3\Psi_k(b)^3}{\sqrt{q_n}\,q_b}
 \mathfrak d(nb^3)V_*(q_nq_b^3/X).\] 两个原始理想都避开 \(S\)；它们可以共享素理想。标记属于整个指标 \(nb^3\)。当 \(\mathfrak d=1\) 时，这就是方程 [\[eq:reflection\]](#eq:reflection) 左侧的 Mellin 完备化。当只使用完备化估计时，来自该方程的 Gaussian Mellin 检验也是允许的。

对于反射公式，我们使用引理 [\[lem:reflection-row-sectors\]](#lem:reflection-row-sectors)，仅对一个非零行。如该引理中那样写 \(k=u k_S k_{\rm good}\)。在固定单位、模六的 \(S\)-赋值以及好行射线类之后，其字面扇形特征为 \[\Psi_0^{[k]}(A)=
 \begin{cases}
 \nu(A)\chi_A(u k_S)\mathcal R(A,k_{\rm good}),
       &A\equiv1\pmod3,\ (A,S)=1,\\
 0,&\text{otherwise}.
 \end{cases}\] 零分支在任一特征之前求值。该引理在好素理想变动之前提供了一个有限族，从而提供了一个共同的 \(L\)，其素支集为 \(S\)。写 \(M_{\rm ref}=\lambda^{12}L^4\)；完整的反射扇形模为 \(M_{\rm ref}^2\)。\(k,f,\mathfrak r_\rho\) 的所有好素理想都保留在局部素理想集中，其指数按模六合并，且所有零都保留。\(f\) 处的四次方不产生额外的互反符号，因为 \(\mathcal R(A,f)^4=1\)。穿刺是其好素理想处局部零幂之积。因此，局部的表述在所声明的原始支集上恰好给出 \(\Psi_k(n)\Psi_k(b)^3\)，包括在共享的好素理想处；没有变动的好素理想进入 \(L\)。

#### 整指标的带标记反射

下一个推论把积形式的标记加入到第 I 部分中的精确反射之中。其分支数据很重要：一个非活跃的带标记素理想不出现在导子中，因此带标记的变换不能通过将一个固定导子的对偶和乘以独立的局部因子而得到。

<span id="cor:marked-reflection" label="cor:marked-reflection">\[cor:marked-reflection\]</span> 固定命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 的一次调用，其基局部素理想集为 \(\mathcal P_0\)、幂为 \(j_p\)、固定乘子为 \(\phi\)、检验为 \(V\)。对此调用置 \(M_{\rm ref}=\lambda^{12}L^4\)。设 \(\mathcal Q\) 为与 \(\mathcal P_0\) 不交的互异好素理想的有限集。在直接的完备化系数和中，插入因子 \(\prod_{q\in\mathcal Q}1_{q\mid nb^3}\)；将此和记作 \(\mathcal T_{\mathcal Q}(X;\Psi,V)\)。它与方程 [\[eq:marked-completion\]](#eq:marked-completion) 具有相同的正规化，其中 \(\Psi_k,V_*\) 被替换为 \(\Psi,V\)。原始的无平方因子理想与立方理想可以共享素理想。

存在一个精确的有限展开 \[\label{eq:marked-reflection}
 \begin{split}
 \mathcal T_{\mathcal Q}(X;\Psi,V)
 =\sum_{\mathcal B}\zeta_{\mathcal Q}
 \sum_{0\ne\mu\in\lambda^{-4}\mathcal O}
 &\frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}
 \prod_{p\in\mathcal A_0}B_p(\lambda^4\mu)\\
 &\cdot\prod_{q\in\mathcal A_{\mathcal Q}}
       q_q^{-1/2}\chi_q(\lambda^4\mu)^{-2}
 V^\sharp\!\left(\frac{q_\mu X}{q_c^2}\right).
 \end{split}\] 这里一个分支 \(\mathcal B\) 指定 \(h_0\bmod L\)、基活跃集与非活跃集 \(\mathcal A_0,\mathcal I_0\)，以及一个划分 \(\mathcal Q=\mathcal A_{\mathcal Q}\sqcup\mathcal I_{\mathcal Q}\)。所有满足 \(j_p\ne0\) 的基素理想都是活跃的。置 \[r=\prod_{p\in\mathcal A_0\cup\mathcal A_{\mathcal Q}}p,
 \qquad c=c_F(h_0)r.\] 基因子 \(B_p\) 以及典范函数 \(d,\vartheta\) 就是命题 [\[prop:completed-reflection\]](#prop:completed-reflection) 对此活跃根式所给出的那些。当每个 \(\sigma_p,\epsilon_p,\omega_{p,j}\) 都使用该分支的整个 \(c\) 计算时，标量为 \[\label{eq:marked-reflection-phase}
 \begin{split}
 \zeta_{\mathcal Q}={}&-\frac{i}{81}\bar\alpha(c)^2
       \widehat\phi(h_0)\bar\kappa_F
       \prod_{p\in\mathcal I_0}(1-q_p^{-1})
       \prod_{q\in\mathcal I_{\mathcal Q}}q_q^{-1}\\
 &\cdot\prod_{p\in\mathcal A_0}\chi_p(\sigma_p)^{-2}\omega_{p,j_p}
       \prod_{q\in\mathcal A_{\mathcal Q}}
             \chi_q(\sigma_q)^{-2}(-\omega_{q,0}).
 \end{split}\] 特别地 \(|\zeta_{\mathcal Q}|\le1/81\)。函数 \(d,\vartheta\) 与标量 \(\kappa_F\) 具有源自第 I 部分的、对 \(h_0\) 与 \(r\bmod M_{\rm ref}^2\) 的典范依赖性。每个对偶和都绝对收敛，并且与那里具有相同的完整源支集。若某个带标记素理想反而属于基局部集，则相应的原始项恒为零，并在使用此公式之前被移除。

对每个好素理想和每个 \(A\in\mathcal O\)，零约定给出逐点恒等式 \(1_{q\mid A}=1-\chi_q(A)^0\)。将它在 \(\mathcal Q\) 上的乘积展开，并对所得到的有限多个完备化和中的每一个应用命题 [\[prop:completed-reflection\]](#prop:completed-reflection)。对固定的 \(h_0\) 与活跃根式，无论一个缺失的素理想是从局部集中被省略，还是以其非活跃分支中指数零的形式被纳入，该命题都使用相同的 \(c_F,c,d,\vartheta,\kappa_F\)、其他局部相位以及核。于是 \(q\) 处的两个非活跃贡献以系数 \(1-(1-q_q^{-1})=q_q^{-1}\) 合并。活跃贡献仅来自被减去的零掩码变换，其局部因子为 \(q_q^{-1/2}\chi_q(\lambda^4\mu)^{-2}\)，标量为 \(-\omega_{q,0}=\tau_{q,2}^{+}\chi_q(\epsilon_q)^{-2}\)。在所有带标记素理想处汇集这些选择即证明了方程 [\[eq:marked-reflection\]](#eq:marked-reflection) 与 [\[eq:marked-reflection-phase\]](#eq:marked-reflection-phase)。非活跃素理想不出现在 \(r\) 中，从而不出现在该分支的导子与核尺度中。这是相容分支之间的有限容斥，而不是一个新的 theta 恒等式。

若某个带标记素理想是基局部素理想，则该标记迫使它整除 \(nb^3\)，而此时该素理想处的零延拓基因子为零，包括指数为零的情形。这就证明了最后一个断言，而无需对零符号作任何除法。它还涵盖了原始的无平方因子理想与立方理想共享该带标记素理想的情形。

对于行范数，本推论的相位推论必须在其精确范围内陈述。对互异的活跃好素理想 \(p,q\)，方程 [\[eq:reflection-cross-prime-phase\]](#eq:reflection-cross-prime-phase) 与三次互反律给出 \[\label{eq:reflection-pair-phase}
 \chi_p(q)^{2j_p+2}\chi_q(p)^{2j_q+2}
       =\left(\frac qp\right)_3^{j_p+j_q+2}.\] 对一个活跃标记，指数为 \(j_q=0\)；其符号的改变仅出现在其单素理想标量中。因此，一个 \(j_p=1\) 的剩余行素理想与一个带标记素理想的配对因子为 \((q/p)_3^3=1\)。而一个 \(j_p=1\) 的行素理想与一个变动的 \(j_q=4\) 素理想则会留下 \((q/p)_3\)，它未必等于一。因此所有非剩余基素理想，尤其是每个 \(j=4\) 素理想，都在内层行范数之前固定。

记 \(R\) 为剩余 \(j=1\) 行素理想之积，\(P\) 为活跃带标记素理想之积。原始的行-标记冲突首先由推论的最后一个断言移除，随后由 \(1_{(P,R)=1}\) 表示。若冻结的活跃基乘积为 \(F_{\rm act}\)，则 \(r=F_{\rm act}RP\)。分别固定 \(R\) 与 \(P\) 模完整 \(M_{\rm ref}^2\) 的类，而不仅仅是它们乘积的类，也不仅仅是它们较小的互反类。这样就在不添加配对相关限制的情况下固定了尖点数据。行-行相位是行标量，标记-标记相位是元组标量，它们与冻结素理想的相互作用仅依赖于这些集合中的一个。角向导子标量以同样的方式分解。

在固定对偶单位、其 \(\lambda\)-赋值以及提取出的冻结因子之后，将剩余的对偶部分写作 \(nb^3\)。变动的列恰好为 \[\chi_R(nb^3)^3=\chi_R(nb)^3,\qquad
 \chi_P(nb^3)^{-2}=\chi_P(n)^{-2}1_{(P,b)=1}.\] 这些恒等式包含每一个零。由某个行或某个元组与某个提取出的冻结因子相遇所造成的零，是对该行或元组的固定限制。源系数、固定加性因子以及所有冻结的局部列因子都是完整提取对偶指标的函数。因此，在共同的光滑分离之后，元组系数可以是元组的、独立于 \(R,n,b\) 的一般有界函数，而对偶系数独立于 \(R,P\)。当槽被分配到提取出的因子时，标记先前的积形式仍然是必需的。

#### 一个二次–三次范数估计

第 I 部分确立了 Goldmakher–Louvel 的二次大筛法所需的方向，并在引理 [\[lem:completed-quadratic-reduction\]](#lem:completed-quadratic-reduction) 中证明了保零的完备化归约。我们加入 Heath–Brown 的三次大筛法： \[\label{eq:cubic-large-sieve}
 \sum_{\substack{a\equiv1\ (3)\\q_a\le U}}^{*}
 \left|\sum_{\substack{b\equiv1\ (3)\\q_b\le V}}^{*}
           c_b\left(\frac ba\right)_3\right|^2
 \ll_\epsilon (UV)^\epsilon
       \{U+V+(UV)^{2/3}\}\sum_b^{*}|c_b|^2,\] 其中两个星号都表示在 \(\mathcal O\) 中无平方因子，且系数是任意复数 。指标不必具有无平方因子的有理范数，也不排除有理素因子。共轭与三次互反律允许相反的方向。在此筛法与方程 [\[eq:quadratic-large-sieve\]](#eq:quadratic-large-sieve) 中，对行集的固定限制使正的外部和减小。而对系数支集的固定限制则通过将省略的系数置零并应用同一定理来实现；不声称列支集的单调性。这一观察不允许任意的配对相关掩码；下一个引理解它所使用的两个此类掩码。

<span id="lem:hybrid-energy" label="lem:hybrid-energy">\[lem:hybrid-energy\]</span> 设 \(K,N,B,L\ge1\)。设 \(k,n,P\) 为无平方因子主理想，满足 \(q_k\ll K\)、\(q_n\asymp N\)、\(q_P\asymp L\)；设 \(b\) 为任意主理想，满足 \(q_b\asymp B\)。理想 \(k,P\) 避开当前的排除集 \(S\)；允许额外的固定排除。源理想 \(n,b\) 可以含有 \(S\) 中除 \(\lambda\) 之外的素理想。设 \(a(P)\) 与 \(\beta(n,b)\) 满足 \[|a(P)|\le1,\qquad |\beta(n,b)|\le1.\] 这里 \(a\) 独立于 \(k,n,b\)，\(\beta\) 独立于 \(k,P\)。则 \[\label{old-eq:4.6b}
 \begin{split}
 &\sum_k\left|
 \sum_P\frac{a(P)}{\sqrt{q_P}}1_{(P,k)=1}
 \sum_{n,b}\beta(n,b)\chi_k(nb)^3
                 \chi_P(n)^{-2}1_{(P,b)=1}
 \right|^2\\
 &\qquad\ll_\epsilon
 (KNBL)^\epsilon(K+NB)B\{N+L+(NL)^{2/3}\}.
 \end{split}\] 允许对 \(k\)-集的固定限制，以及对 \((n,b)\)-支集或 \(P\)-支集的固定限制，也允许固定的射线扇形。所有此类限制都必须保持上述两个系数独立性条件。若除子有界的重数保持这些条件，则可以包含它们；否则必须先用证明中的除子 Cauchy 不等式将其移除。

将方程 [\[old-eq:4.6b\]](#old-eq:4.6b) 的左侧记作 \(\mathcal H\)。首先移除完整的变动行-标记掩码： \[1_{(P,k)=1}=\sum_{D\mid(P,k)}\mu(D).\] 对每一行，此类除子的数目至多为 \(d_{\mathcal O}(k)\)。逐行的除子 Cauchy 不等式，随后是对行取正的和，因此花费一个允许的因子 \((KNBL)^\epsilon\)。在固定 \(D\)-被加项中写 \(P=DP'\) 与 \(k=Dk'\)。无平方因子性给出固定限制 \((D,P')=(D,k')=1\)。定义 \[\begin{split}
 a_D(P')&=a(DP')1_{(D,P')=1},\\
 \beta_D(n,b)&=\beta(n,b)\chi_D(nb)^3\chi_D(n)^{-2}1_{(D,b)=1}.
 \end{split}\] 所有这些因子都保留它们的零，且 \(|\beta_D|\le1\)。将 \(q_P^{-1/2}=q_D^{-1/2}q_{P'}^{-1/2}\) 分解出来给出 \[\label{eq:hybrid-mark-mask-reduction}
 \begin{split}
 \mathcal H\ll (KNBL)^\epsilon\sum_D\frac1{q_D}
 \sum_{k'}\left|
 \sum_{n,b}\beta_D(n,b)\chi_{k'}(nb)^3
 \sum_{P'}\frac{a_D(P')}{\sqrt{q_{P'}}}
       \chi_{P'}(n)^{-2}1_{(P',b)=1}
 \right|^2.
 \end{split}\] 这里 \(q_{k'}\ll K/q_D\)、\(q_{P'}\asymp L/q_D\)，且所有继承的固定限制都被保留。外层的 \(D\) 是该分解所允许的无平方因子好除子，因此 \(q_D\ll\min(K,L)\)。特别地，在单个 \(D\)-被加项内部不会恢复任何 \((P',k')\) 掩码。其抵消属于已经被逐行 Cauchy 界定过的完整 Möbius 和。

对固定 \(D\)，\(\beta_D(n,b)\) 与内层 \(P'\)-和的乘积是一个独立于 \(k'\) 的任意复系数。以行长 \(K/q_D\) 应用方程 [\[eq:completed-quadratic-reduction\]](#eq:completed-quadratic-reduction)。使用其记号 \[b=gt^2,\qquad c=(n,g),\qquad n=cm,\qquad g=ch,
 \qquad q_c\asymp C,\quad q_g\asymp G,\quad q_t\asymp T,\] 于是 \(B\asymp GT^2\)，并对其完整的 \(c\)-掩码除子写 \(c=rc'\)。理想 \(c,m,h\) 两两互素且无平方因子；不施加 \(g\) 与 \(t\) 之间的互素性。所引用的归约已经包含了自然的 \(k'\)-\(t\) 限制以及 \(k'\)-\(c\) 掩码的完整 Möbius 展开。它不会在剩余的行与 \(c'\) 之间恢复掩码。

对一个 \(C,G,T\) 块，其插入到方程 [\[eq:hybrid-mark-mask-reduction\]](#eq:hybrid-mark-mask-reduction) 中的正输出至多为 \[\label{eq:hybrid-after-quadratic-reduction}
 \begin{split}
 (KNBL)^\epsilon\sum_D\frac1{q_D}T\sum_{q_t\asymp T}
 \sum_{\substack{r\ {\rm sf},\ (r,S)=1\\q_r\ll\min(K/q_D,C)}}
 &\left\{\frac K{q_Dq_r}+\frac{NG}{C^2}\right\}\frac C{q_r}
 \sum_{c',m,h}|\beta_D(rc'm,rc'ht^2)|^2\\
 &\quad\cdot\left|
 \sum_{P'}\frac{a_{D,r}(P')}{\sqrt{q_{P'}}}
       \chi_{P'}(c'm)^{-2}1_{(P',ht)=1}
 \right|^2,
 \end{split}\] 其中正的 \(c',m,h\)-和保持原支集，并且 \[a_{D,r}(P')=a_D(P')\chi_{P'}(r)^{-2}.\] 这里所使用的分解，包含所有零，为 \[\chi_{P'}(rc'm)^{-2}1_{(P',rc'ht^2)=1}
 =\chi_{P'}(r)^{-2}\chi_{P'}(c'm)^{-2}1_{(P',ht)=1}.\] 特征已经提供了 \(r,c'\) 与 \(m\) 处缺失的零。因此 \(r\)-因子只与元组有关，包括当 \((P',r)\ne1\) 时它的零。固定的 \(D\)-相位在此正界之前一直留在 \(\beta_D\) 内。二次归约在对 \(m,h\) 的好乘积进行筛分之前，已经分离出它们有限多个无平方因子的 \(S\)-部分；方程 [\[eq:hybrid-after-quadratic-reduction\]](#eq:hybrid-after-quadratic-reduction) 中的 \(m,h\) 是原来的理想。

我们现在可以舍弃 \(|\beta_D|^2\le1\)。对固定的 \(h,t,D,r\)，\(P'\)-系数独立于 \(j=c'm\)，理想计数给出 \[\sum_{P'}\frac{|a_{D,r}(P')|^2\,1_{(P',ht)=1}}{q_{P'}}
 \ll_\epsilon (KNBL)^\epsilon.\] 乘积 \(j=c'm=n/r\) 是无平方因子主理想，其范数为 \(O(N/q_r)\)。它可以含有 \(S\) 中除 \(\lambda\) 之外的允许素理想，因为只有二次的列被剥去其固定的 \(S\)-部分。按 \(j\) 对 \(c',m\) 分组至多花费一个除子因子。只扩大这个正的无平方因子 \(j\)-区间。三次互反律、共轭以及方程 [\[eq:cubic-large-sieve\]](#eq:cubic-large-sieve)，随后是 \(O(G/C)\) 个 \(h\) 的选择，在 \(q_D\asymp D_0,\ q_r\asymp r_0\) 上给出 \[\label{old-eq:4.6c}
 (KNBL)^\epsilon\frac GC
 \left\{\frac N{r_0}+\frac L{D_0}
       +\left(\frac{NL}{r_0D_0}\right)^{2/3}\right\}.\] \(ht\) 处的固定掩码在此三次筛法中是一个系数限制，而不是行相关的掩码。

该归约提供 \(T\sum_t\)，其中 \(t\) 有 \(O(T)\) 种可能，并提供因子 \(C/q_r\)。与 \(h\)-计数一起，它们贡献 \[T^2(C/r_0)(G/C)\asymp B/r_0.\] 在其二进区间中有 \(O(r_0)\) 个可能的 \(r\)，而在其区间上 \(q_D^{-1}\) 之和为 \(O(1)\)，至多相差一个允许的小幂。当 \(D_0,r_0\) 被替换为 \(1\) 时，两个筛因子都增大，且 \(NG/C^2\ll NB\)。对对数多个二进区间求和即证明了方程 [\[old-eq:4.6b\]](#old-eq:4.6b)。亚单位商区间为空，有界区间通过改变固定的环形常数被纳入。此论证既未引入 \((g,t)=1\) 条件，也未引入新的配对相关掩码。

#### 反射能量界

我们接下来量化方程 [\[eq:marked-completion\]](#eq:marked-completion) 的反射。下面的描述也规定了陈述中所使用的二进贡献。

###### 反射块数据.

固定 \(f,\rho\) 并置 \(Q=\log_Zq_{\mathfrak r_\rho}\)。对一个元素行 \(0<q_k\ll Z^M\)，通过下式定义其理想的极大幂强部分 \[k_{\rm pow}=\prod_{v_p(k)\ge2}p^{v_p(k)}.\] 将赋值一的素理想分成支集在 \(S\cup\operatorname{supp}(f\mathfrak r_\rho)\) 上的无平方因子乘积 \(k_{\rm sup}\)，以及该集合之外的无平方因子乘积 \(k_{\rm res}\)。这三个素理想支集两两不交，且它们的乘积是 \(k\) 的理想。此处一个幂强理想意指每个正的素理想赋值至少为二。固定 \(k\) 的单位。在 \[q_{k_{\rm pow}}\asymp Z^O,\qquad q_{k_{\rm res}}\asymp Z^H.\] 中插入光滑二进划分。选择这些理想中心为非负，单位二进区间的中心为零。特别地，一个实际的环形因子 \(\chi_{\rm row}(q_{k_{\rm res}}/Z^H)\) 被保留在行和中。有界二进区间包含 \(k_{\rm res}=1\)。从这些支集中选取固定常数 \(C_k,C_O,C_H\ge1\)，使得 \[q_k\le C_kZ^M,\qquad q_{k_{\rm pow}}\ge Z^O/C_O,\qquad
 q_{k_{\rm res}}\ge Z^H/C_H.\] 由于 \(q_{k_{\rm sup}}\ge1\)，一般范数不等式方程 [\[eq:actual-residual-row-dyad\]](#eq:actual-residual-row-dyad) 在此给出 \[H\le M-O+\frac{\log C_{\rm res}}{\log Z},
 \qquad C_{\rm res}=C_HC_kC_O.\] 此不等式不必是等号，因为 \(k_{\rm sup}\) 可能具有正的范数长度。

冻结实际的理想 \(k_{\rm pow},k_{\rm sup}\)。在 \(S\) 之外的每个素理想处，将 \(\rho(n)\chi_n(k)\chi_n(f)^4\) 的局部指数按模六合并，始终保留零延拓。\(k_{\rm res}\) 的素理想具有指数 \(j=1\)。所有其他此类素理想，包括每个指数 \(j=4\) 的非槽素理想，现在都被固定。在反射公式中，当一个素理想出现在 \(c\) 中时称其为活跃的。对活跃零指数素理想的一个固定选择以及每个 \(j=4\) Ramanujan 因子的一个固定分裂，令：

|         |                                         |
| :------ | :-------------------------------------- |
| \(A_0\) | 为 \(k_{\rm res}\) 之外所有活跃非槽素理想的对数范数,     |
| \(S_0\) | 为其中小 Ramanujan 项与活跃零掩码项的对数范数,           |
| \(N_0\) | 为分配到无平方因子对偶理想的 \(j=4\) 整除项的对数范数,        |
| \(B_0\) | 为分配到立方理想但不分配到无平方因子理想的 \(j=4\) 整除项的对数范数. |

这里一个对数范数是指所示乘积范数的 \(\log_Z\)。该分配使用 \(1_{p\mid nb^3}=1_{p\mid n}+1_{p\nmid n}1_{p\mid b}\)。 设 \(z_a=\sum_{i\ {\rm active}}z_i\) 为其名义槽长度之和。活跃素理想之积的范数除以 \(Z^{z_a}\) 落在一个固定的紧区间内，包括名义长度为零或空列表的情形。在提取出被迫的无平方因子素理想与立方素理想之后，将剩余的对偶理想限制为 \[q_n\asymp Z^v,\qquad q_b\asymp Z^{\ell_b},\qquad
 q_{\lambda^{h_\lambda}}=Z^{e_\lambda}.\] 选择理想中心 \(v,\ell_b\) 为非负。这些是源对偶理想：它们保留方程 [\[old-eq:4.3\]](#old-eq:4.3) 所允许的每个 \(S\) 素理想；不在其上放置额外的 \(S\)-掩码。只施加所显示的 \(\lambda\)-赋值支集。单位以及整数 \(h_\lambda\ge-4\) 在此二进区间中被固定。对这些选择，记 \(\mathcal U_{v,\ell_b,e_\lambda}(k_{\rm res})\) 为方程 [\[eq:marked-reflection\]](#eq:marked-reflection) 的右侧，连同积形式的元组系数求和，并带上所指定的局部选择与对偶限制，以及实际因子 \(\chi_{\rm row}(q_{k_{\rm res}}/Z^H)\)。在此定义中活跃槽元组仍被求和。此定义对每个固定的、幂强且被支撑的行部分，以及对通过固定剩余行乘积与活跃槽乘积模完整反射模 \(M_{\rm ref}^2\) 的各自类而得到的每个扇形，分别作出。

<span id="lem:reflected-energy" label="lem:reflected-energy">\[lem:reflected-energy\]</span> 沿用上文的 。设 \(Z\ge2\)，并假设它们的对数长度在固定有界集合中变动。在方程 [\[eq:marked-completion\]](#eq:marked-completion) 的完备化和中，固定的特征、穿刺与槽系数独立于 \(k,f\)，槽支集不交，且槽系数如方程 [\[old-eq:4.2\]](#old-eq:4.2) 那样为乘积。在冻结 \(k_{\rm pow},k_{\rm sup}\) 之后的固定行限制必须独立于活跃槽与对偶变量，除了显式的零掩码 \(1_{(P,k_{\rm res})=1}\) 之外。固定一个小的 \(\tau_{\rm ref}>0\)，置 \(X=Z^{N_*}\)。定义 \(T_d\)，并按下式称一个二进区间被保留： \[\label{old-eq:4.4}
 \begin{gathered}
 T_d=2H+2A_0+2z_a-N_*-N_0-3B_0,\\
 v+3\ell_b+e_\lambda\le T_d+\tau_{\rm ref}
 \quad\text{对一个被保留的二进区间}.
 \end{gathered}\] 满足 \[v+3\ell_b+e_\lambda>T_d+\tau_{\rm ref}\] 的项具有任意小的总大小，代价是一个固定的多项式高度成本，这要在足够远的核围道移动之后，并且 \(Z\) 的阈值仅依赖于固定的支集区间与 \(\tau_{\rm ref}\)。每个被保留的二进区间，对每个活跃元组，其系数指数为 \[\label{old-eq:4.5}
 -v/2-\ell_b-e_\lambda/3-(S_0+B_0+z_a)/2.\] 定义 \[\label{old-eq:4.7}
 u=\min\{v,z_a,(v+z_a)/3\},\] 以及 \[\label{old-eq:4.6}
 \begin{split}
 E_{\rm ref}={}&O/2+\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b
                     -2e_\lambda/3\\
 &-\tfrac12(T_d-v-3\ell_b-e_\lambda)_+.
 \end{split}\] 对每个 \(\epsilon>0\)，具有固定 \(k_{\rm pow},k_{\rm sup}\) 的贡献满足 \[\sum_{k_{\rm res}\ {\rm sf}}
       |\mathcal U_{v,\ell_b,e_\lambda}(k_{\rm res})|^2
 \ll Z^{E_{\rm ref}-O/2+\epsilon}.\] 对其 \(O\)-二进区间中的固定部分以及局部选择求和，将此变为 \(O(Z^{E_{\rm ref}+\epsilon})\)。这些界在所声明的区间内对变动的理想与穿刺是一致成立的，带有限多个光滑半范数以及范数扭动高度的一个固定多项式成本。当 \(e_\lambda\) 为负时，其值为 \(O(1/\log Z)\)。特别地，该公式仅用于满足方程 [\[eq:actual-residual-row-dyad\]](#eq:actual-residual-row-dyad) 的实际剩余行二进区间。

首先，利用行 Hilbert 空间中的三角不等式移除不活跃的槽位。在这样的槽位上， 绝对系数质量为 \[\sum_{p\in\mathcal P_i}q_p^{-1}\ll_\epsilon Z^\epsilon,\] 在任何固定限制下都一致成立，包括有界或零长度列表的情形。因此只需证明这些 素数固定时的一致界。每个这样的分支都有各自的导子、尖点扇形与核尺度，且不活 跃素数不出现在导子中。它先前的碰撞排除现在成为一个固定的行限制。

固定 \(f,\rho,k_{\rm pow},k_{\rm sup}\)、非槽位的局部选择、\(h_0\)，以及残余 行乘积与活跃槽位乘积模整个 \(M_{\rm ref}^2\) 的各个类。同时固定对偶指标的 单位和分歧指数。不再有非槽位的 \(j=4\) 标号被平均。我们只在对活跃多元组的 原始求和内部，使用方程 [\[eq:unmarked-structural-block\]](#eq:unmarked-structural-block) 中的代数冻结基提取。 推论 [\[cor:marked-reflection\]](#cor:marked-reflection) 及随后的相位分离使得这一提取在各个多元组之间是 同时的：在各自分离的扇形固定后，基系数对于残余行和多元组是共同的，而其余标量 分离为一个行因子和一个多元组因子。我们并不对每个多元组分别应用数值的无标记估计。

该结构提取给出公共中心系数 \[Z^{-v/2-\ell_b-e_\lambda/3-(S_0+B_0)/2}\] 乘以正规化的逆根因子和有界系数。其 \(N_0\)-指派仅从无平方因子的对偶理想中提取 一个被迫的 \(j=4\) 素数，即使立方理想与之共享该素数；整个共享的立方部分仍保留 在其残余范数与系数中。其 \(B_0\)-指派从立方理想中提取一次出现，并留下因子 \(q_p^{-1/2}\)。这些都是关于完整源支撑的陈述，包括 \(S\) 的允许素数。方程  [\[eq:marked-reflection\]](#eq:marked-reflection) 中的每个活跃标记列贡献 \(q_p^{-1/2}\)。由于 \(q_P/Z^{z_a}\) 落在一个固定紧区间内，这证明了方程 [\[old-eq:4.5\]](#old-eq:4.5) 中的 逐多元组系数指数。

我们现在记录公共剖面的精确标记实例。设 \(F_{\rm act},N_F,B_F\) 为具有对数 范数 \(A_0,N_0,B_0\) 的实际冻结乘积。令 \(R=k_{\rm res}\)， \(P=\prod_{i\ {\rm active}}p_i\)。分支分母与一个被支撑的对偶指标为 \[c=c_FF_{\rm act}RP,\qquad
 \mu=u\lambda^{h_\lambda}N_Fn(B_Fb)^3.\] 取固定的分块中心，定义 \[\begin{gathered}
 y_R=q_R/Z^H,\quad y_n=q_n/Z^v,\quad
 y_b=q_b/Z^{\ell_b},\quad y_i=q_{p_i}/Z^{z_i},\\
 Y=\frac{q_{\lambda^{h_\lambda}N_FB_F^3}X Z^vZ^{3\ell_b}}
          {q_{c_FF_{\rm act}}^2Z^{2H}\prod_{i\ {\rm active}}Z^{2z_i}}
   =q_{c_F}^{-2}Z^{v+3\ell_b+e_\lambda-T_d}.
 \end{gathered}\] 乘性给出精确恒等式 \[\label{eq:reflection-actual-annuli}
 \frac{q_\mu X}{q_c^2}
       =Yy_ny_b^3y_R^{-2}\prod_{i\ {\rm active}}y_i^{-2}.\] 即使 \(N_F\) 与 \(b\) 共享素数，它仍然成立。\(Y\) 中所有冻结因子都是其实际 乘积，而每个移动的范数仍是一个坐标。因此，实际的行截断以及各个对偶与槽位截断 将核自变量置于 \[[C_{\rm ker}^{-1},C_{\rm ker}]
       Z^{v+3\ell_b+e_\lambda-T_d}\] 之中，其中 \(C_{\rm ker}\ge1\) 仅依赖于固定支撑区间与公共固定模。特别地，这一 比较没有使用任何由正性添加的较短行。

令 \(D_{\rm ker}=T_d-v-3\ell_b-e_\lambda\)。在这个实际圆环域的完整乘积上， 引理 [\[lem:reflection-common-profile\]](#lem:reflection-common-profile) 允许从整个齐次线性行向量中提取出因子 \[m_{\rm ker}=Z^{-(D_{\rm ker})_+/4}\] 出来，其固定半范数常数至多乘上一个因子 \(C_{\rm ker}^{1/4}\)。正规化剖面具有 有界的固定 Euler 半范数；并不声称任何非齐次的多元组半范数会变小。该剖面包含 来自结构提取的正规化逆根，以及所有其他公共光滑范数窗口。

尾部在真正的、未分离的求和上被移除。若 \(\log Z\ge2\log C_{\rm ker}/\tau_{\rm ref}\)，则每个中心超出量大于 \(\tau_{\rm ref}\) 的整个二进块都具有大于 \(Z^{\tau_{\rm ref}/2}\) 的实际核 自变量。以格 \(\lambda^{-4}\mathcal O\)、\(a=X/q_c^2\) 和 \(U=Z^{\tau_{\rm ref}/2}\) 应用引理 [\[lem:lattice-kernel-tail\]](#lem:lattice-kernel-tail)。在完整源 支撑上，第 I 部分所用的系数界给出 \[|d(\mu)|/\sqrt{q_\mu}\le27q_\lambda^{4/3}.\] 每个基或标记局部因子在丢弃其指示函数后至多为 \(q_p^{1/2}\)。有界的行、多元组 与局部对数长度区间、局部分支计数以及 \(1+a^{-1}\) 具有固定的多项式代价 \(Z^{B_{\rm tail}}\)，其中 \(B_{\rm tail}\) 的选取独立于核的阶。对于任何期望的 节省 \(D>0\)，在该壳引理中选择 \[A>1+\frac{2(B_{\rm tail}+D)}{\tau_{\rm ref}}\] 可使这些整个二进块的绝对总和为 \(O(Z^{-D})\) 乘以一个有限的检验半范数。范数 扭转为该半范数带来固定的多项式高度代价。壳求和计入了所有被丢弃的对偶指标， 因此对于该尾部没有使用任何在保留对偶长度处的计数。它在 Fourier 绝对化之前被 移除。

对于保留下来的二进块，对那一个联合剖面应用公共剖面引理与方程  [\[eq:reflection-common-minkowski\]](#eq:reflection-common-minkowski)，该联合剖面位于方程  [\[eq:reflection-actual-annuli\]](#eq:reflection-actual-annuli) 中。其密度 对整个当前行 Hilbert 空间（包括活跃多元组求和）是共同的：实际的行、对偶与 各个槽位范数是它的坐标，而不是分别选取的测度的参数。完整的固定支撑盒控制 每一个被调用的加权 Fourier 范数与高度代价。在分离模式处，范数幂的绝对值为一， 并保持行、多元组与对偶系数之间的独立性。只有在分离的非负行范数内部，才允许 将行集从原来的圆环域扩大为 \(q_R\ll Z^H\)，对新增的行使用相同的分离公式。 那里从不计算核。

在提取公共系数之后、使用 \(m_{\rm ker}^2\) 之前，分离后的平方范数被如下量界住 \[Z^{-v-2\ell_b-2e_\lambda/3-S_0-B_0+\epsilon}\mathcal N,\] 其中 \[\label{old-eq:4.6a}
 \begin{split}
 \mathcal N={}&
 \sum_{\substack{k_{\rm res}\ {\rm sf}\\q_{k_{\rm res}}\ll Z^H}}
 \left|
 \sum_{\boldsymbol p}
 \frac{a(\boldsymbol p)}{\sqrt{q_P}}1_{(P,k_{\rm res})=1}
 \sum_{\substack{n\ {\rm sf}\\b}}
 \beta(n,b)\chi_{k_{\rm res}}(nb)^3
              \chi_P(n)^{-2}1_{(P,b)=1}
 \right|^2,\\
 &P=\prod_{i\ {\rm active}}p_i,\qquad q_P\asymp Z^{z_a}.
 \end{split}\] 理想 \(n,b\) 保持其所述二进范数与固定系数限制。在提取公共界之后， \(|a(\boldsymbol p)|,|\beta(n,b)|\le1\)。

在调用范数界之前，我们验证两条独立性假设。每个残余素数都具有指数 \(j=1\)， 每个活跃槽位都是一个整指标的 \(j=0\) 标记，而所有其他活跃素数都被冻结。分离的 完整 \(M_{\rm ref}^2\) 类固定了尖点系数与加性因子。方程  [\[eq:reflection-pair-phase\]](#eq:reflection-pair-phase) 消去每个行-槽位相位，而前面的标记反射讨论将 所有行-行、槽位-槽位与冻结相互作用指派给一个行标量或一个多元组标量。角向导子 标量以同样的方式分离。剩余的源与冻结局部列仅依赖于完整提取出的对偶指标；它们 在某个冻结因子处的零点给出固定的行、多元组或对偶限制。最后，精确的保零列恒等 式除特征零点外只留下 \(1_{(P,k_{\rm res})=1}\) 与 \(1_{(P,b)=1}\)。因此 \(a\) 独立于 \(k_{\rm res},n,b\)，而 \(\beta\) 独立于 \(k_{\rm res},\boldsymbol p\)， 恰如方程 [\[old-eq:4.6a\]](#old-eq:4.6a) 所要求。函数 \(a\) 在这一范数步骤不必保持乘积形式。

以 \[K=Z^H,\qquad N=Z^v,\qquad B=Z^{\ell_b},\qquad L=Z^{z_a}.\] 应用引理 [\[lem:hybrid-energy\]](#lem:hybrid-energy)。将具有相同 \(P\) 的多元组归类只花费一个除数 因子。由于 \[v+z_a-u=\max\{v,z_a,2(v+z_a)/3\},\] 混合界与外部系数给出指数 \[\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b-2e_\lambda/3.\] 直到此时，平方标量 \(m_{\rm ker}^2\) 才提供方程 [\[old-eq:4.6\]](#old-eq:4.6) 中的最后 一项。这证明了固定部分的断言。

每个幂数理想都唯一地可以写为 \(x^2y^3\)，其中 \(y\) 无平方因子。理想计数与 \(\sum_yq_y^{-3/2}<\infty\) 给出 \(O\)-二进块中有 \(O(Z^{O/2})\) 个这样的 理想。被支撑的无平方因子部分整除 \(S f\mathfrak r_\rho\) 的根基，因此在所述 区间中有 \(O(Z^\epsilon)\) 种选择；局部选择具有相同的除数界。对局部展开逐行 应用除数 Cauchy，随后对这些固定部分作正求和，因此使 \(O/2+\epsilon\) 只增加 一次。活跃多元组已在混合范数内部，不再计入。这证明了聚合断言。

对原始行长度的依赖可以在不将 \(H\) 与 \(M-O\) 等同的情况下被界住。在一个 活跃非槽位素数处，对 \(2A_0-N_0-S_0-4B_0\) 的贡献如下： \[\begin{array}{c|c}
 \text{local choice}&\text{其对数范数的系数}\\ \hline
 j\text{ odd, or }j=2&2\\
 j=0\text{ active}&1\\
 j=4\text{ 小或指派给 }n&1\\
 j=4\text{ assigned to }b&-2\\
 j=0\text{ inactive}&0.
 \end{array}\] 一个残余行素数通过 \(2H\) 贡献二。逐素数地，这些系数被以下估值所界 \[(q_k^2/q_{k_{\rm pow}})\,q_fq_{\mathfrak r_\rho}.\] 确实，行估值为 \(e\ge2\) 的幂数素数在第一个因子中具有估值 \(e\)，一个无平方 因子的行素数具有估值二，而一个仅属于无平方因子的 \(f\) 或属于 \(\mathfrak r_\rho\) 的素数具有估值一。交叠只会增大这一上界的估值。固定的被 排除素数只贡献一个固定因子 \(C_S\ge1\)。等价地，对素数求和给出实际的范数 不等式 \[q_{k_{\rm res}}^2 Z^{2A_0-N_0-S_0-4B_0}
 \le C_S\frac{q_k^2}{q_{k_{\rm pow}}}\,q_fq_{\mathfrak r_\rho}.\] 选取固定的 \(C_f\ge1\) 使得 \(q_f\le C_fZ^V\)，并令 \(C_{\rm width}=C_H^2C_SC_k^2C_OC_f\)。前面的不等式与 \(T_d\) 的定义蕴含 \[\label{eq:common-width-charge}
 T_d-S_0-B_0
 \le 2M-O+Q+V-N_*+2z_a+
       \frac{\log C_{\rm width}}{\log Z}.\]

对于空的槽位列表，\(z_a=u=0\)。选取 \(\eta>0\)，然后取 \(Z\) 充分大，使得 两个已展示的常数误差至多为 \(\eta\)，且 \(e_\lambda\ge-\eta\)；后者由 \(\log Z\ge4\log q_\lambda/\eta\) 推出。在一个保留下来的二进块上，方程  [\[old-eq:4.6\]](#old-eq:4.6) 与 \(v+3\ell_b+e_\lambda\le T_d+\tau_{\rm ref}\) 给出 \[E_{\rm ref}
 \le O/2+\max\{H,T_d-S_0-B_0\}+\tfrac53\eta+\tau_{\rm ref}.\] 对于第一个分支，在使用 \(e_\lambda\) 的下界后丢弃非正项；对于第二个分支，使用 \(v\le T_d-3\ell_b-e_\lambda+\tau_{\rm ref}\)。该最大值对每个自变量都是递增的。 因此我们可以对其第一个自变量使用方程 [\[eq:actual-residual-row-dyad\]](#eq:actual-residual-row-dyad)， 对其第二个自变量使用方程 [\[eq:common-width-charge\]](#eq:common-width-charge)，然后对对数多个实际 \(H\)-二进块求和。取 \(\eta,\tau_{\rm ref}\) 以及局部小幂次损失关于 \(\epsilon\) 充分小，即证明 \[\label{eq:completed-moment}
 \sum_{0<q_k\ll Z^M}'|\mathcal T_1(Z^{N_*};k)|^2
 \ll Z^{O/2+\max\{M-O,\,2M-O+Q+V-N_*\}+\epsilon}.\] 求和上的撇号将幂数部分限制在其 \(O\)-二进块内。一个有界的对偶区间包含在 第一项中；空区间可忽略。没有使用任何等式 \(H=M-O\)。

### 补偿的低阶估计

我们现在界住方程 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 中定义的有限补偿探针。 它的精确低阶分离有两个因子。我们首先通过直接应用引理 [\[lem:reflected-energy\]](#lem:reflected-energy)， 在求和标记槽位之后界住完备化行。然后我们为来自节 [4](#sec:probe) 的加性多项式 证明一个定量的 Gram 界。Cauchy–Schwarz 将把这些估计结合起来给出指数 \(3/16\)。

#### 标记的完备化行

对于一个固定的重标子集 \(J\)，其标记子集为 \(J^c\)，令 \[\begin{gathered}
 d=\sum_{i\in J}\ell_i,\qquad
 X'=X/q_{p_J}\asymp XZ^{-d},\qquad
 Y'=Y/q_{p_J}\asymp YZ^{-d},\\
 M'=M-2d,\qquad \ell'=\ell-d,\qquad 0\le d\le\ell=1/6.
 \end{gathered}
 \label{old-eq:5.2}\] 对于槽位素数的无平方因子乘积 \(D\)，定义标记的完备化级数 \[T_D(s_0,\psi)=\sum_{\substack{c\ {\rm sf}\\n}}
 \gamma_2(c)\overline{\alpha(cn^3)}\psi(cn^3)
 1_{D\mid cn^3}q_c^{-s_0}q_n^{-3s_0+1/2}.\] 理想 \(c,n\) 是与 \(S\) 互素的原始理想，由它们的主生成元表示，其中 \(c\) 无平方 因子；它们可以共享素数。所有特征幂保持其原始的零延拓。对于空乘积 \(D=1\)， 这就是完备化的 \(T(s_0,\psi)\)。 对于这个固定的 \(J\)，令 \[\begin{split}
 B^J_{m,\sigma}(Z)=
 \sum_{p_i\in\mathcal P_i(Z),\ i\notin J}
 \prod_{i\notin J}\overline{\eta(p_i)}W_i(q_{p_i}/P_i)
 \sum_{\theta\in\widehat T}a_\theta\frac1{2\pi i}
 \int_{(4)} &(Zq_{p_{J^c}})^t\Phi(t)\\
 &\cdot T_{p_{J^c}}(t+1/2,
             \nu_\sigma\theta\chi_\bullet(m))\,dt.
\end{split}\] 因此，在标记槽位求和之后，\(B^J\) 恰好是方程  [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 的 \(J\) 求和项的完备化行因子。固定 多元组 \(p_J\) 在其低阶分离中只影响 \(X',Y'\)。

<span id="lem:probe-row-norm" label="lem:probe-row-norm">\[lem:probe-row-norm\]</span> 对每个 \(\epsilon>0\)、每个固定的重标子集 \(J\) 以及每个 \(\sigma\in T\)，其中 \(Q=q_{b_*}X'Y'\asymp Z^{M'}\)， \[\sum_{0<q_m\ll Q}|B^J_{m,\sigma}(Z)|^2
       \ll Z^{M'+((d-1/6)/4)_++\epsilon}
       =Z^{M'+\epsilon}.
 \label{old-eq:5.4}\] 该界对于固定的重标多元组是一致的，并且没有依赖于幸存槽位网格的损失。

令 \(A=cn^3\)，并对 \(i\notin J\) 令 \(\varrho_i=q_{p_i}/P_i\)。由于即使 \(c,n\) 共享素数也有 \(q_A=q_cq_n^3\)，且 \(q_{p_{J^c}}=Z^{\ell'}\prod_{i\notin J}\varrho_i\)，对定义 \(B^J\) 的已展示 积分作 Mellin 反演，即给出物理光滑因子 \[\begin{gathered}
 V\!\left(\frac{q_A}{Zq_{p_{J^c}}}\right)
 =W_{\mathrm G}\!\left(\frac{r}{\prod_{i\notin J}\varrho_i}\right),\\
 r=\frac{q_A}{Z^{1+\ell'}}.
 \end{gathered}\] 这里 \(V=W_{\mathrm G}\) 是引理 [\[lem:gaussian-annular\]](#lem:gaussian-annular) 的 Gauss 函数。 空乘积等于一。

对该引理中固定的平移分划 \(\chi\) 作用于 \(r\)。在圆环域 \(r=e^kx\) 上，保留 单一联合剖面 \[w_{k,J}(x,\boldsymbol\varrho)
 =\chi(\log x)W_{\mathrm G}\!\left(
       \frac{e^kx}{\prod_{i\notin J}\varrho_i}\right)
       \prod_{i\notin J}W_i(\varrho_i).\] \(x\) 及所有 \(\varrho_i\) 的对数在该支撑上都落在固定的紧集中。因此 Gauss 函数自变量的对数为 \(k+O_{\rm fixed}(1)\)。引理 [\[lem:gaussian-annular\]](#lem:gaussian-annular) 中的导数估计，结合这一有界平移与固定槽位窗口，对每个固定的 \(\kappa_{\mathrm G}>0\)、\(A_{\rm cnt},B_{\rm cnt},C_{\rm ann}\ge0\)、 \(D_{\rm tail}>0\) 以及固定半范数阶 \(j\) 给出 \[\begin{gathered}
 \sum_{k\in\mathbb Z}e^{A_{\rm cnt}|k|}p_j(w_{k,J})<\infty,
 \\
 Z^{B_{\rm cnt}}
 \sum_{|k|>\kappa_{\mathrm G}\log Z-C_{\rm ann}}
       e^{A_{\rm cnt}|k|}p_j(w_{k,J})
       \ll Z^{-D_{\rm tail}}.
 \end{gathered}\] 这些常数可以依赖于固定的槽位系统，但不依赖于其移动的素数标号。在一个圆环域 \(\log r=k+O(1)\) 上，行 \(\ell^2\) 范数的一个绝对界至多为 \(Z^{B_{\rm cnt}}e^{A_{\rm cnt}|k|}p_j(w_{k,J})\)，其中指数固定，这由初等的 行、槽位与理想计数得到。选取 \(C_{\rm ann}\) 大于 \(\chi\) 的固定对数半径，并且 只丢弃满足 \(|k|>\kappa_{\mathrm G}\log Z+C_{\rm ann}\) 的整个圆环域。对它们的 范数界求和后再平方，得到小于任何给定 \(Z^{-1}\) 的幂次。每个满足 \(|\log_Z r|\le\kappa_{\mathrm G}\) 的圆环域都被保留。

对于每个剩余的圆环域，保留在 \(w_{k,J}\) 的支撑上等于一的固定各个环形截断， 并对这一完整剖面应用引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus)。它的对数 Fourier 反演 使用一个对每一行和每个幸存槽位多元组都共同的系数密度。正规化的槽位比值在 分离之前仍是联合剖面的变量；它们并不索引分别选取的密度。对于固定的 Fourier 变量，所得每个槽位系数是原始算术系数 \(\overline{\eta(p_i)}\) 与一个个环形截断 及范数幂的乘积。它保持有界，并且独立于该行以及所有其他槽位。完备化因子是在 长度 \[N_*=1+\ell'+\theta_N,\qquad
 \theta_N=\frac{k}{\log Z},\qquad
 |\theta_N|\le\kappa_{\mathrm G}+O_{\rm fixed}(1/\log Z).\] 处的一个环形检验。这些保留下来的长度落在固定的有界区间内。由已展示的 Gauss 估计，加权 Fourier 范数具有可和的总量；小的环形权重留在这个齐次的单剖面 Fourier 范数中，而不在一个非齐次的多元组半范数中。Minkowski 不等式将分离的 行范数穿过这一公共密度。当检验尺度被重新居中时，现有的 \(q_c^{-1/2}q_n^{-1}\) 正规化保持不变，因此不引入 \(e^k\) 的额外幂次。选取 \(\kappa_{\mathrm G}\) 处于最终的 \(\epsilon\) 余量之内。对每个固定的 \(\theta\)， 引理 [\[lem:reflection-row-sectors\]](#lem:reflection-row-sectors) 提供 \(\nu_\sigma\theta\chi_\bullet(m)\) 的行-扇形归约，并带有每个原始零掩码。它覆盖所有非零元素行，包括与 \(S\) 相交 的那些；在这一行范数中没有使用因子 \(\xi(m)\)。行球仅通过 \(Q=q_{b_*}X'Y'\) 依赖于固定的重标多元组 \(p_J\)，并且独立于幸存的标记槽位与 对偶变量。物理槽位集保持互不相交，其分离系数为乘积形式。因此，对 \(\theta\) 作有限三角不等式并应用引理 [\[lem:reflected-energy\]](#lem:reflected-energy)，即给出方程  [\[old-eq:4.6\]](#old-eq:4.6) 在这一实际 \(N_*\) 处的指数，其中保留参数 \(\tau_{\rm ref}\) 以及独立规定的输出与分离损失全都至多为小的 \(\epsilon_0>0\)。我们在固定行部分求和之后使用指数 \(E_{\rm ref}\)；它们的计数 已包含在 \(E_{\rm ref}+\epsilon_0\) 中，主指数为 \(O/2\)，不再重复计入。

这里 \(f=1\)，且穿刺点为 \(\rho=1\)，因此唯一移动的非槽位素数就是该行的素数。 在引理 [\[lem:reflected-energy\]](#lem:reflected-energy) 的有限单位与反射扇形分裂之后，冻结其范数 长度为 \(O\) 的幂数部分以及其支撑在 \(S\) 上的估值一部分，并将其残余的无平方 因子良好乘积分裂为范数 \(\asymp Z^H\) 的*实际*二进块。设 \(\epsilon_Z=O_{\rm fixed}(1/\log Z)\) 非负且充分大，以包含本计算中所有固定的 环形与固定导子对数偏移。则 \[H\le M'-O+\epsilon_Z,\qquad
 \Delta_H=M'-O-H\ge-\epsilon_Z,\qquad O\ge-\epsilon_Z.\] 实际的行与对偶环形截断被保留在一个联合剖面中，而其公共 Fourier 密度被分离。 小的核振幅在行范数平方之前从该齐次密度中提取，只有到那时才可以按方程  [\[eq:reflection-common-minkowski\]](#eq:reflection-common-minkowski) 那样扩大正的筛法求和。特别地，方程  [\[old-eq:4.6\]](#old-eq:4.6) 中的核节省使用这一 \(H\)；它不会在任何由正扩大新增的较短 行上重新计算。

在该能量估计的记号中，计入 \(A_0\) 的每个移动非槽位素数都以至少二的指数整除 幂数行部分。因此，将其精确范数与幂数二进块相比较，以及任何固定导子的贡献， 给出 \[2A_0\le O+\epsilon_Z,\qquad N_0\le A_0,\qquad z_a\le\ell'.\] 在实际完备化尺度处可用的对偶长度为 \[T_d=2H+2A_0+2z_a-1-\ell'-\theta_N-N_0-3B_0.\] 由于 \(M'+\ell'-1=-3d\)，直接相减给出 \[T_d-(H-3d)
 =H-M'+2A_0+2(z_a-\ell')-N_0-3B_0-\theta_N
 \le 2\epsilon_Z+|\theta_N|.\] 如同反射能量的证明中那样，在正的 Mellin 平移之后，低于某个固定负长度的对偶 区间可忽略，而有界的边界区间只花费任意小的幂次。这些二进块中的源对偶理想 \(n,b\) 保持方程 [\[old-eq:4.3\]](#old-eq:4.3) 的支撑：它们可以共享素数，并且可以含有 \(S\) 的允许素数；不施加 \(n\) 与 \(b\) 之间任何额外的 \(S\)-掩码或互素条件。在每个 剩余的对偶二进块上，令 \(y=v+3\ell_b+e_\lambda\)。保留性给出 \(y\le T_d+\epsilon_0\)，而非零单位区间在增大其固定常数后给出 \(v,\ell_b,e_\lambda\ge-\epsilon_Z\)。由此推出 \[\max(H,v+\ell_b)=H+O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z).\]

记 \(s_{\rm hyb}=\min\{v,z_a,(v+z_a)/3\}\)，即方程 [\[old-eq:4.7\]](#old-eq:4.7) 中称为 \(u\) 的量。若 \(s_{\rm hyb}=z_a\)，则 \(-S_0-B_0+z_a-s_{\rm hyb}\le0\)，核项 非正，且 \[-\ell_b-\frac{2e_\lambda}{3}\le\frac53\epsilon_Z.\] 这里单独的 \(O\) 是幂数行的对数长度。由此推出 \[\begin{aligned}
 E_{\rm ref}&\le O/2+H+O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z)\\
 &=M'-O/2-\Delta_H+O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z).
 \end{aligned}\] 否则 \(s_{\rm hyb}\ge v/2-O(\epsilon_Z)\)，而有界的单位区间蕴含 \[s_{\rm hyb}+\ell_b+\frac{2e_\lambda}{3}
       +\frac{(T_d-y)_+}{2}
 \ge \frac y4+\frac{(T_d-y)_+}{2}-O(\epsilon_Z)
 \ge \frac{T_d}{4}-O(\epsilon_Z).\] 最后一个不等式对 \(y\le T_d\) 与 \(y\ge T_d\) 分别成立。这里，平方后的核节省是 这样得到的：先从公共 Fourier 密度中提取 \(\min\{1,Z^{(y-T_d)/4}\}\)，然后才 对行范数平方。相对于 \(M'\)，在剩余的 \(+z_a\) 之前的节省恰好为 \[\begin{split}
 O/2+\Delta_H+S_0+B_0+T_d/4
 ={}&\frac{2M'+2z_a-1-\ell'+2\Delta_H-\theta_N}{4}\\
    &+\frac{2A_0-N_0+B_0+4S_0}{4}.
 \end{split}
 \label{old-eq:5.3}\] 第二个分子非负。由于 \(z_a\le\ell'\)，这一分支中的能量至多为 \[\begin{aligned}
 &M'+\frac{1+3\ell'-2M'-2\Delta_H+\theta_N}{4}
       +O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z)\\
 &\qquad=M'+\frac{d-1/6-2\Delta_H+\theta_N}{4}
       +O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z).
 \end{aligned}\] 在使用 \(O\ge-\epsilon_Z\) 并吸收 \(\theta_N\) 之后，两个上界为 \[\begin{gathered}
 M'-\Delta_H+O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z),\\
 M'+\frac{d-1/6-2\Delta_H}{4}
       +O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z).
 \end{gathered}\] 它们关于 \(\Delta_H\) 非增。由于 \(\Delta_H\ge-\epsilon_Z\)，其形式的 \(\Delta_H=0\) 取值将每个实际二进块界到至多 \(O(\epsilon_Z)\)，无论是否出现端点 二进块。因此它们的最大值至多为 \(M'+((d-1/6)/4)_++O(\epsilon_0+\kappa_{\mathrm G}+\epsilon_Z)\)。在 \(d=1/6\) 时有 \(\ell'=z_a=0\)，而被截断的单位区间落在第一个分支中；有界的负单位二进块 只改变 \(\epsilon_Z\)。在规定的 \(\epsilon\) 余量内选取 \(\epsilon_0\) 与 \(\kappa_{\mathrm G}\)，然后增大固定数据下阈值，使得 \(\epsilon_Z\) 也落在其中。 对对数多个行与对偶二进块求和即证明该引理。

#### 加性 Gram 界

我们接下来估计区间 \(Y'^2/Q\ge1\) 中的加性因子。引理  [\[lem:full-correlation\]](#lem:full-correlation) 的完整相关性保留了决定其消去与例外频率二者的 碰撞零点。

<span id="prop:probe-gram" label="prop:probe-gram">\[prop:probe-gram\]</span> 固定算术数据 \(S,T,b_*,\xi\)、环形权重 \(W_1\)，以及一个射线类 \(\sigma\in T\)。 设 \(Q,Y'\ge1\) 处于 \(Z\) 中固定的多项式区间内，并假设 \[P_a=Y'^2/Q\ge1.\] 对于实高度 \(\nu\)，按节 [4](#sec:probe) 中的定义令 \(A_m=A_{m,\sigma,\nu}(Y')\)。 对每个固定的行球 \(q_m\ll Q\) 和每个 \(\epsilon>0\)，有 \[\sum_{q_m\ll Q}|A_m|^2
 \ll (1+|\nu|)^{J_{\mathrm{Gr}}}\frac Q{Y'}
       \left(1+P_a^{1/6}+\frac{P_a^2}{Y'}\right)Z^\epsilon.
 \label{eq:gram-quantitative}\] 这里 \(J_{\mathrm{Gr}}\) 是一个固定半范数阶，独立于移动尺度以及 \(\nu\)。同一 断言对射线系数 \(1_{s\in\sigma}\chi_s(b_*)/\xi(s)\) 的任意固定有限线性组合也 成立。不声称任何任意的、依赖于行的算术系数。

用固定的非负径向 Schwartz 函数对行球作控制。 令 \(r_s=q_s/Y'\)，并在与 \(S\) 互素的主元素上令 \(c_\sigma(s)=1_{s\in\sigma}\chi_s(b_*)/(\tau\xi(s))\)，在求逆特征之前于其他地方 以零延拓。该多项式的精确环形改写为 \[A_m=Y'^{-3/2}\sum_s c_\sigma(s)W_1(r_s)r_s^{-1+i\nu}
                          g_{\chi_s}(s,-m).\] 因此展开后的平方具有公共正规化 \(Y'^{-3}\)，联合环形剖面包含因子 \(W_1(r_{s_1})r_{s_1}^{-1+i\nu}W_1(r_{s_2})r_{s_2}^{-1-i\nu}\)。 记 \(s_1=Cn_1\)、\(s_2=Cn_2\)，其中 \((n_1,n_2)=1\)。对行变量作 Poisson 求和得到 因子 \(Q/(q_{s_1}q_{s_2})\)，而两个未正规化的 Gauss 和的完备 变换为 \(q_{s_1}q_{s_2}F(s_1,s_2;j)\)。因此它给出精确的前置因子 \(Q/Y'^3\) 以及方程 [\[eq:correlation-lift\]](#eq:correlation-lift) 的相关性 \(F(Cn_1,Cn_2;Ck)\)。 这里 \(F\) 再次表示方程 [\[old-eq:2.11\]](#old-eq:2.11) 的完整相关性， 而不是方程 [\[eq:local-F\]](#eq:local-F) 的局部系数。 第一个 Fourier 核的宗量与 \(q_Cq_k/P_a\) 同阶。

在互素的剩余上，该相关性中的因子 \(L_C\) 满足 \(|L_C|\le q_C\)。对于随后的带符号延拓，使用其指定的 有界延拓，它在两列上都以模 \(\operatorname{rad}C\) 为周期，包括 \(C\) 与某一列 有公共素因子的情形。当 \(C\) 的某个素因子同时整除两列时，其值 定义为零；这是对该延拓的定义，而非关于此处真实 相关性的断言。在作任何逐因子的估计之前，插入完整的 Möbius 恒等式 \[1_{(n_1,n_2)=1}=\sum_{d\mid n_1,\ d\mid n_2}\mu(d)\] 并记 \(n_i=dm_i\)。此时不对 \(m_1,m_2\) 施加互素条件。 非零项满足 \((d,Ck)=1\)。在整个这一步中使用 \(\mathcal R(n_1,n_2)\) 的固定 射线延拓；零剩余特征之商将没有定义。

我们为该系数指定一个公共固定模。对 \(k\ne0\) 利用单位约定和引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 的固定 \(S\)-素生成元，记 \(k=\zeta k_Sk_{\mathrm{good}}\)，其中 \(k_S=\prod_{\mathfrak p\in S}\pi_{\mathfrak p}^{e_{\mathfrak p}}\) 且 \(k_{\mathrm{good}}=\prod_{p\notin S}p^{e_p}\)。对于 \(S\) 之外的某个主 剩余理想 \(m\)，互反律给出 \[\begin{split}
 \chi_m(k)&=\kappa_{\zeta,\boldsymbol e}(m)
       \mathcal R(k_{\mathrm{good}},m)
       \prod_{p\mid k_{\mathrm{good}}}\chi_p(m)^{e_p},\\
 \kappa_{\zeta,\boldsymbol e}(m)
       &=\chi_m(\zeta)\prod_{\mathfrak p\in S}
             \chi_m(\pi_{\mathfrak p})^{e_{\mathfrak p}\bmod6}.
 \end{split}\] 每个显式给出的好的局部幂在公共素因子上都保留其零点， 包括 \(6\mid e_p\) 的情形。引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 把这有限多个 \(\kappa_{\zeta,\boldsymbol e}\) 放在一个支撑于 \(S\) 的固定 射线群中。此外 \(\mathcal R(k_{\mathrm{good}},m)\) 属于一个关于 \(m\) 的固定有限族。

一次性选取 \(\mathfrak l_{\rm fixed}\)，使其包含主类 模与 \(S\) 零掩码、\(A_m\) 中每个固定射线 系数的模、\(\mathcal R\) 在每个变量中的一个周期， 以及前面所有 \(\kappa_{\zeta,\boldsymbol e}\) 特征的导子。该 延拓系数在主类之外，或在求逆特征之前的某个固定 非单位元处取零。该模与 \(C,d,k\) 无关，且 它在 \(S\) 处可能有比 \(\operatorname{rad}(k)\) 更高的幂次。在应用互反律之后， 关于 \(m_1,m_2\) 的联合算术 系数以如下模为周期 \[\mathfrak r=\operatorname{lcm}
   (\mathfrak l_{\rm fixed},\operatorname{rad}C,\operatorname{rad}(k)),
 \qquad q_{\mathfrak r}\ll_{\rm fixed}q_Cq_k.\] 若 \(k\) 在 \(C\) 与 \(\mathfrak l_{\rm fixed}\) 之外的一个素因子处有不可被六整除的 赋值 \(e_p\)，则称 \(k\) 为非例外的。在该 素因子处，第一剩余列具有非主零延拓 因子 \(\chi_p(m_1)^{e_p}\)，至多相差一个单位标量。提升、固定 相位以及其他素因子在模 \(p\) 下与 \(m_1\) 无关。 它的完备均值，从而由中国剩余定理得到的完备联合均值， 为零。用 \(d\) 作代换 不改变这一结论，因为 \((d,k)=1\)。赋值可被六整除处的 主零掩码在例外情形中仍然存在。

频率 \(k=0\) 只贡献对角项：相关性 强制 \(n_1=n_2=1\)，且等于 \(\varphi(C)\)。范数与 \(Y'\) 同阶的可能 \(C\) 有 \(O(Y')\) 个，每个满足 \(\varphi(C)\le q_C\ll Y'\)。因此其贡献为 \(O(Q/Y')\)。

对 \(k\ne0\)，把 Fourier 宗量分成二进壳层 \(q_Cq_k/P_a\asymp R\)，其中 \(R=1,2,4,\ldots\)，且第一个壳层 包含所有至多为二的宗量。为 \(q_C\asymp C_0\) 与 \(q_d\asymp D_0\) 选取二进中心 \(C_0,D_0\in\{1,2,4,\ldots\}\)， 其中第一个二进段包含有界的单位范围。 使用名义正剩余尺度 \[N=Y'/(C_0D_0),\qquad
 \mathcal Q=q_{\mathfrak r}\ll_{\rm fixed}RP_a.\] 实际剩余范数落在 \(N\) 的固定倍数之内；名义值 \(N\) 允许小于一。固定任意 \(A>2\) 与 \(B>2\)。 对每个固定的 \(C,d,k\)，两列的那个联合环形剖面 \(W_R\) 使下文所用的有限多个齐次单剖面半范数被 \(O_{B,J_{\mathrm{Gr}}}((1+|\nu|)^{J_{\mathrm{Gr}}} R^{-B})\) 所界，其中固定了一个 \(J_{\mathrm{Gr}}\)，它是在选定这些导数阶数以及 \(A,B\) 之后选取的。这 可由对第一个 Fourier 核求导得到，其 Schwartz 衰减吸收由此产生的每个 \(R\) 的幂次；范数幂次的导数只付出 \(1+|\nu|\) 的固定幂次。这个因子 \(R^{-B}\) 保留在单剖面 Fourier 估计中，并在下文的线性格和中出现一次； 不使用小的非齐次元组半范数。

设 \(a_{C,d,k}\) 为该周期算术系数。对 非例外频率，其正规化完备 Fourier 变换， 在两个剩余变量上取正规化 \(\mathcal Q^{-2}\)， 绝对值至多为 \(q_C\)，并在 \((0,0)\) 处取零。由于 \(\mathcal O\) 的每个理想都是主理想，周期格具有 线性尺度 \(\mathcal Q^{1/2}\)。因此四维格 Poisson 求和 给出，对上述 \(A\)， \[\left|\sum_{\mathbf m\in\mathcal O^2}
       a_{C,d,k}(\mathbf m)W_R(\mathbf m/\sqrt N)\right|
 \ll (1+|\nu|)^{J_{\mathrm{Gr}}} R^{-B}q_C N^2
             \min\{1,(\mathcal Q/N)^A\}.
 \label{eq:gram-periodic-poisson}\] 当 \(N\ge\mathcal Q\) 时，零频率消失，其他 对偶向量的线性尺度为 \((N/\mathcal Q)^{1/2}\)。阶为 \(2A>4\) 的 Fourier 衰减把它们的和界定在 \((\mathcal Q/N)^A\) 之内。 当 \(N<\mathcal Q\) 时，使用两个环形区域中的点计数。非空的 次单位圆环有 \(N\) 被一个固定正常数从下方界定， 因此它仍包含 \(O(N)\) 个格点；低于该常数时它 是空的。这就在对 \(a_{C,d,k}\) 不作任何本原性或张量积假设的情况下 证明了方程 [\[eq:gram-periodic-poisson\]](#eq:gram-periodic-poisson)。

令 \(K_R=RP_a/C_0\)。固定的壳层比较常数给出 \(q_k\le C_{\rm sh}K_R\)，其中 \(C_{\rm sh}>0\) 固定。因此 当 \(K_R<C_{\rm sh}^{-1}\) 时非零频率范围为空。在 非空范围上，初等的格计数给出 \[\#\{k:0<q_k\le C_{\rm sh}K_R\}
       \ll_{\rm fixed}K_R+\sqrt{K_R}+1\ll_{\rm fixed}K_R.\] 因此在这些二进段上 \(C,d,k\) 有 \(O(C_0D_0K_R)\) 种选择。把 方程 [\[eq:gram-periodic-poisson\]](#eq:gram-periodic-poisson) 乘以这个计数以及 公共前置因子，至多得到 \[(1+|\nu|)^{J_{\mathrm{Gr}}} R^{-B}\frac Q{Y'}\frac{RP_a}{C_0D_0}
       \min\left\{1,\left(\frac{RP_aC_0D_0}{Y'}\right)^A\right\}.\] 对 \(\Lambda=Y'/(RP_a)\)，所需的二进正和为 \[\sum_{i,j\ge0}2^{-i-j}\min\{1,(2^{i+j}/\Lambda)^A\}
 =\sum_{n\ge0}(n+1)2^{-n}\min\{1,(2^n/\Lambda)^A\}
 \ll_A\frac{1+\log(2+\Lambda)}{\Lambda}.\] 当 \(\Lambda\ge1\) 时，在 \(2^n\asymp\Lambda\) 处把两个几何尾部 拆开；当 \(\Lambda<1\) 时，左边有界，而 显式给出的右边大于一个正常数。 因此非例外频率贡献 \[\ll (1+|\nu|)^{J_{\mathrm{Gr}}}\frac Q{Y'}\frac{P_a^2}{Y'}Z^\epsilon\] 在求和 \(R\) 之后，选取固定的 \(B>2\)。

剩下的是计数例外非零频率。它们满足 \((k)=a_1^6e\)，其中 \(e\) 无六次幂因子，且支撑在 \(C\) 的 素因子与固定支撑上。可能的 \(e\) 至多有 \(6^{\omega(C)+O_S(1)}\ll_\epsilon q_C^\epsilon\) 个。 对其中每个，壳层界 \(q_k\le C_{\rm sh}K_R\) 只允许 \(q_{a_1}\le(C_{\rm sh}K_R/q_e)^{1/6}\)。若该范围非空， 其上界至少为一，理想计数给出 \(O_{\rm fixed}(K_R^{1/6})\) 种选择；若 \(q_e>C_{\rm sh}K_R\) 则 它为空。单位因子只付出一个固定因子。因此这样 的元素 \(k\) 有 \(O_\epsilon(K_R^{1/6}q_C^\epsilon)\) 个，包括 \(K_R\) 的有界次单位范围。

使用 \(K_R=RP_a/C_0\)、\(|L_C|\le q_C\) 以及平凡的 两列点计数。在乘以 \(Q/Y'^3\) 之前，这些二进段上的 贡献为 \[\ll (1+|\nu|)^{J_{\mathrm{Gr}}} R^{-B}Z^\epsilon
       Y'^2(RP_a)^{1/6}C_0^{-1/6}D_0^{-1}.\] 在缩减任意小幂次之后，关于 \(C_0,D_0\) 的求和收敛， 且对同一个固定的 \(B>2\)，关于 \(R\) 的求和也收敛。这 给出项 \((Q/Y')P_a^{1/6}Z^\epsilon\)。加上对角项 与非例外项即证明了该命题。

#### 下界的完成

现在把前面两个估计应用于精确低分离格式中同一个 重标度和式的两个因子。

<span id="prop:probe-low" label="prop:probe-low">\[prop:probe-low\]</span> 对于方程 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 中的探针、 方程 [\[old-eq:5.1\]](#old-eq:5.1) 中的几何构型以及每个 \(\epsilon>0\)， \[|I_{\eta,\mathrm{modified}}(Z)|
       \ll Z^{l_x/2+b/12+\epsilon}=Z^{3/16+\epsilon}.
 \label{old-eq:5.10}\] 该指数与目标及槽网格无关；常数与下阈值可以 依赖于固定的算术数据、槽系统以及光滑检验函数。

对于固定的重标度子集与元组，令 \(Q=q_{b_*}X'Y'\)。 其分离为方程 [\[eq:low-separated\]](#eq:low-separated)，其中含 \(A_{m,\sigma,v}(Y')\) 与 \(B^J_{m,\sigma}(Z)\)。令 \(r_J=q_{p_J}/Z^d\)；固定的环形支撑给出 \(0<c_J\le r_J\le C_J<\infty\)，且对元组一致成立。确切地说， \[\begin{gathered}
 X'=Z^{l_x-d}/r_J,\qquad Y'=Z^{l_y-d}/r_J,\\
 Q=q_{b_*}Z^{M'}/r_J^2,\qquad
 P_a=Y'^2/Q=q_{b_*}^{-1}Z^{1/8}.
 \end{gathered}\] 特别地，当 \(Z\ge q_{b_*}^8\) 时 \(P_a\ge1\)。放大所允许的 固定数据下阈值，使得 \(Q,Y'\ge1\) 对元组比值也一致 成立；这是可能的，因为 \(M'\ge1/2\) 且 \(l_y-d\ge5/16\)。剩余的长度不等式为 \[l_x-d\ge3/16,\qquad l_y-d\ge5/16,
 \qquad l_y-d-11b/6\ge1/12.\] 最后一个给出 \[\frac{Y'}{P_a^{11/6}}
 =q_{b_*}^{11/6}r_J^{-1}Z^{l_y-d-11b/6}
       \gg_{\rm fixed}Z^{1/12},\] 从而 \(P_a^2/Y'\ll P_a^{1/6}\)。因此命题 [\[prop:probe-gram\]](#prop:probe-gram) 给出 \[\sum_{q_m\ll Q}|A_{m,\sigma,v}(Y')|^2
 \ll (1+|v|)^{J_{\mathrm{Gr}}}(Q/Y')P_a^{1/6}Z^\epsilon.
 \label{old-eq:5.6}\] 在行和上应用 Cauchy–Schwarz、引理 [\[lem:probe-row-norm\]](#lem:probe-row-norm)， 以及 \((1+|v|)^{J_{\mathrm{Gr}}/2}|\widehat W_0(iv)|\) 的可积性，现在 把该元组的未重标度分离界定在 \(Z^\epsilon\) 乘以 \[\begin{aligned}
 Q^{-1/2}\bigl[(Q/Y')P_a^{1/6}\bigr]^{1/2}
       \bigl[Z^{M'}\bigr]^{1/2}
 &=\bigl[Z^{M'}/Y'\bigr]^{1/2}P_a^{1/12}\\
 &=r_J(X')^{1/2}P_a^{1/12}.
 \end{aligned}\] 由于 \(r_J\) 有界，这等于 \(O((X')^{1/2}P_a^{1/12}Z^\epsilon)\)。

对 \(d=\sum_{i\in J}\ell_i\)，重标度元组至多有 \(Z^{d+\epsilon}\) 个， 系数为 \(O(Z^{-3d/2})\)，且 \((X')^{1/2}\asymp X^{1/2}Z^{-d/2}\)。因此总的 附加指数为 \[f(d)=d-3d/2-d/2=-d\le0.
 \label{old-eq:5.5}\] 选取各分量估计中的小幂次，使其总和落在 指定的 \(\epsilon\) 之内。对有限多个子集求和即证明 方程 [\[old-eq:5.10\]](#old-eq:5.10)。对于方程 [\[eq:part-II-mellin-target\]](#eq:part-II-mellin-target) 中 已定义的 \(C=C_{\mathrm{II}}\)，用于主信号的 正规化满足 \[\begin{gathered}
 C_{\mathrm{II}}(s)=l_x/2+s-1+h/6=s-11/16,\\
 C_{\mathrm{II}}(7/8)=3/16=l_x/2+b/12.
 \end{gathered}
 \label{old-eq:5.11}\] 因此，在第 II 部分所假设的矛盾之下，这个下界比 \(Z^{C_{\mathrm{II}}(\beta_*)}\) 小一个精确幂次 \(\Delta=\beta_*-7/8\)，至多相差任意指定的 \(\epsilon\)。

### 局部补偿及其误差

节 [1](#sec:compensation) 中的物理修正已经 由其分离的低表示作了估计。我们现在确定其 完整的 Euler 修正，并界定两式运算所留下的局部误差。 全文之中，局部记号 \(P_p,P_p^*,H_p,V,W,D,R\) 沿用 引理 [\[lem:local-euler\]](#lem:local-euler) 中的含义；在共享的解析估计中，其变量 \(x\) 记作 \(s\)。固定一个非零且无六次幂因子的物理行 \(u\)，满足 \((u,S)=1\)。所有槽素因子都属于节 [1](#sec:compensation) 的集合 \(\mathcal P_i(Z)\)；对每个这样的素因子令 \(Q=q_p\)。如 引理 [\[lem:local-euler\]](#lem:local-euler) 那样，记 \(x_r=\Re x\)、\(w_r=\Re w\)、\(z_r=\Re z\)。 \(P_p^*\) 中的因子 \(W_{\rm loc}=\rho Q^{-w}\) 与 \(W=\chi_p(u)Q^{-w}\) 不同：当 \(p\mid u\) 时，后者与 \(D\) 都为零，而 前者保留其单位相位。

#### 完整的全纯修正

对固定的槽素因子 \(p\)，把完备化指标限制在 \(p\mid A\) 会在高次级数中把 \(P_p\) 换成 \(P_p^*\)。把 \(Z\) 变为 \(ZQ\) 会使其 Mellin 权乘以 \(Q^{x+z-1}\)。因此 在 \(P_p\) 有定义且非零的点处，方程 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 的标记项具有乘子 \(\overline{\eta(p)}Q^{x+z-1}P_p^*/P_p\)。重标度项具有乘子 \[Q^{-3/2}Q^{-(1/2-z)}Q^{-(w-1)}=Q^{z-w-1}.\] 因此，在同一轨迹上，两式运算的精确局部乘子为 \[\label{old-eq:5.13}
 Q^{z-1}\mathcal B_p,\qquad
 \mathcal B_p=\overline{\eta(p)}Q^xP_p^*/P_p-Q^{-w}.\] 把联合局部替换定义为 \[\label{old-eq:5.13c}
 G_p=
 \frac{(\overline{\eta(p)}Q^x-Q^{-w})(1-V)(1-W)P_p^*
       -Q^{-w}(1-VW)}{1-D}.\] 在 Euler 区域内使方程 [\[old-eq:5.13\]](#old-eq:5.13) 中原始商有定义的 点处，有 \(G_p=H_p\mathcal B_p\)。 所显示的公式在该商无定义处也定义了 \(G_p\)。右边既没有 \(P_p\) 分母，也没有 \(1-W\) 分母。引理 [\[lem:local-euler\]](#lem:local-euler) 中的界 \(|R|,|V|,|D|<1\) 连同其关于 \(P_p^*\) 的公式表明， \(G_p\) 在两个所述的 Euler 区域内全纯，包括在 \(P_p\) 或 \(H_p\) 的零点处。

在 Euler 区域内使所选商有定义的点处， 把完整的槽 乘子记作 \[\mathcal B_i(u;x,w,z)=\sum_{p\in\mathcal P_i(Z)}
           W_i(q_p/P_i)q_p^{z-1}\mathcal B_p.\] 用于移动围道的修正是在不使用这些商的情况下定义的： \[\label{eq:holomorphic-selected-tuple}
 \mathfrak H_{\eta,u,Z}(x,w,z)=
 \sum_{(p_i)\in\prod_i\mathcal P_i(Z)}
 \prod_{i=1}^K\bigl[W_i(q_{p_i}/P_i)q_{p_i}^{z-1}G_{p_i}\bigr]
 \prod_{\substack{p\notin S\\p\notin\{p_1,\ldots,p_K\}}}H_p.\] 这是在提取出方程 [\[eq:probe-high\]](#eq:probe-high) 中标量商之后的完整修正。为验证这一断言， 固定一个允许的元组并令 \(\mathcal P=\{p_1,\ldots,p_K\}\)。在 绝对起始线上，所选运算把 \(P_p\) 换成 \[\label{eq:selected-local-operation}
 \overline{\eta(p)}Q^{x+z-1}P_p^*-Q^{z-w-1}P_p
 =\frac{1-D}{(1-V)(1-W)}Q^{z-1}G_p.\] 该等式来自把 \(P_p-P_p^*=(1-V)^{-1}+W/(1-W)\) 代入 方程 [\[old-eq:5.13c\]](#old-eq:5.13c)。它提取出与在未被选中的素因子处相同的标量局部因子 \((1-V)^{-1}(1-W)^{-1}(1-D)\)。每个被选中的 素因子恰出现一次，因为槽 支撑互不相交。因此该元组的完备因子是 方程 [\[eq:probe-high\]](#eq:probe-high) 中的标量商乘以方程  [\[eq:holomorphic-selected-tuple\]](#eq:holomorphic-selected-tuple) 中它对应的被加项。这一推理不涉及 除以 \(P_p\) 或 \(H_p\)。在 Euler 区域内使所有 原始被选商都有定义的点处，同一个有限和也分解为 \(\mathcal H_{\eta,u}\prod_i\mathcal B_i\)。

每个被加项中未被选中的乘积在两个 Euler 区域内都正规收敛。更定量地，在方程  [\[eq:local-region-one\]](#eq:local-region-one) 的任意固定子区域中，令 \(\epsilon_H=\min(\epsilon_0,1/50)>0\)。引理  [\[lem:local-euler\]](#lem:local-euler) 中逐素因子的缺陷界给出，且对所选元组一致成立， \[\label{eq:unselected-local-product}
 \prod_{\substack{p\notin S\\p\notin\mathcal P}}|H_p|
 \le
 \prod_{\substack{p\notin S\\p\nmid u}}
       (1+Cq_p^{-1-\epsilon_H})
 \prod_{p\mid u}(1+Cq_p^{-\epsilon_H})
 \ll_\epsilon q_u^\epsilon.\] 第一个正乘积由理想计数收敛，第二个 满足除数乘积界。略去被选中的因子只会从这些 正控制项中去掉因子。在第二个 Euler 区域中，同样的 论证使用相应的缺陷指数 \(-363/200\) 与 \(-33/40\)。 因此方程 [\[eq:unselected-local-product\]](#eq:unselected-local-product) 在那里也成立， 并有相应的正控制项。这些上界并不 断言 \(H_p\) 非零。

对每个固定的 \(Z\)，方程 [\[eq:holomorphic-selected-tuple\]](#eq:holomorphic-selected-tuple) 是 若干个乘积的有限和，这些乘积由全纯的被选因子与正规 收敛的未被选乘积组成。因此它在两个 Euler 区域内每一点的 某个邻域上全纯。它还满足 定义 [\[def:stage-high-data\]](#def:stage-high-data) 中的全高度要求。 事实上，在任一区域内的固定实盒上，\(P_p^*\) 的公式以及 有界地远离零的分母给出 \(|G_p|\ll Q^B\)，其中 \(B\) 固定，且对所有虚部与单位相位一致成立。一个槽中有 \(O(P_i)\) 个理想，且在那里 \(q_p\asymp P_i\)。因此有限元组 和与方程 [\[eq:unselected-local-product\]](#eq:unselected-local-product) 给出 \[\label{eq:compensated-all-height-majorant}
 |\mathfrak H_{\eta,u,Z}(x,w,z)|
 \ll_\epsilon q_u^\epsilon\prod_iP_i^{z_r+B}
 \ll_\epsilon q_u^\epsilon Z^{B'}.\] 其中 \(B'\) 在该盒上固定。对 \(q_u\le Z^D\)，这就是 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant)，即便高度指数 为零。这里的所有常数都在以后任何分部积分阶数之前 固定。

现在把精确有限运算与 方程 [\[eq:probe-poisson-identity\]](#eq:probe-poisson-identity) 及 [\[eq:probe-high\]](#eq:probe-high) 结合，给出 \[\label{eq:compensated-poisson-identity}
\begin{split}
 I_{\eta,\mathrm{modified}}(Z)
 ={}&\frac1{(2\pi i)^3}\int_{(3)}\int_{(3)}\int_{(2)}
       \mathcal W(X,Y,Z;x,w,z)\\
 &\quad\cdot\sum_u^{(6)}q_u^{-z}\overline{\xi(u)}
       \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
       {L^S(x,\eta\overline{\chi_\bullet(u)})}
       \mathfrak H_{\eta,u,Z}(x,w,z)\,dz\,dw\,dx.
\end{split}\] 该恒等式在所示直线上绝对收敛，因为对 固定的 \(Z\)，它由有限多个绝对收敛的重标度 基础探针恒等式得到。它没有额外的外部 Euler 因子。它 对物理表达式 \(I_{\eta,\mathrm{modified}}\) 验证了定义 [\[def:stage-high-data\]](#def:stage-high-data) 的精确高表示，其几何构型为方程 [\[old-eq:5.1\]](#old-eq:5.1)。特别地， \(l_x/2-1+h/6=17/96-1+13/96=-11/16\)，正如 方程 [\[eq:part-II-mellin-target\]](#eq:part-II-mellin-target) 所要求。它正是 命题 [\[prop:probe-low\]](#prop:probe-low) 中所界定的那个探针的恒等式。每个延拓 都使用方程 [\[eq:holomorphic-selected-tuple\]](#eq:holomorphic-selected-tuple) 中的完整修正， 而不是各个商的某个整体定义乘积。

#### 动态局部误差

在恒等射线素因子处，来自 \(T\) 的每个固定相位都等于一，尽管 \(\eta(p)\) 可以是任意单位。先假设 \(p\nmid u\) 并令 \(v=\chi_p(u)\)。则 \(D=\eta(p)v^{-1}Q^{-x}\)，且 \(\overline{\eta(p)}Q^xD=v^{-1}\)。利用 \(v^{-1}W=Q^{-w}\) 与 \(\mathcal E_p=P_p^*+D\) 可得到精确的 正规化相消 \[\label{old-eq:5.13b}
\begin{split}
 G_p+v^{-1}H_p={}&
 \frac{(1-V)(1-W)}{1-D}
 \Bigl[(v^{-1}-Q^{-w})\{V/(1-V)-D\}\\
 &\hspace{17mm}+(\overline{\eta(p)}Q^x+v^{-1}-Q^{-w})
                    \mathcal E_p\Bigr].
\end{split}\] 这是一个关于 Euler 区域内全纯局部表达式的恒等式。 在这些区域内，在原始商的轨迹上其左边为 \(H_p(\mathcal B_p+v^{-1})\)。 为在该轨迹上直接看出相消，在正规化之前把 \(P_p^*=-D+\mathcal E_p\) 与 \(P_p=(1-V)^{-1}+W/(1-W)+P_p^*\) 代入左边。 常数 \(-v^{-1}\)、\(v^{-1}-Q^{-w}\) 与 \((v^{-1}-Q^{-w})W/(1-W)=Q^{-w}\) 之和为零。 所得有理恒等式只含分母 \(1-R\)、\(1-V\) 与 \(1-D\)，它们在 Euler 区域内非零；因此它给出 那里所显示的全纯恒等式。 对 \(p\mid u\)，主项由原来的零延拓为零， 方程 [\[old-eq:5.13c\]](#old-eq:5.13c) 反而变为 \[G_p=
 \overline{\eta(p)}Q^x(1-V)\mathcal E_p-Q^{-w}H_p.\]

我们现在给出对剩余误差槽的界。其解析 输入被明确陈述：反射的本原分子在 所保留的高度处必须很小。用当前的固定数据以及 \(\Theta=\langle\eta,\widehat T\rangle\) 实例化节 [6](#sec:detector)， 并使用其零延拓表示 \(\nu(n)\chi_n(u)^\varsigma\)，其中 \(\nu\in\Theta\) 且 \(\varsigma\in\{-1,1\}\)。分子 \(\chi_\bullet(u)\) 及其共轭属于 \(\mathcal X_u\)， 固定乘子为 \(1\in\Theta\)；而分母 \(\eta\overline{\chi_\bullet(u)}\) 属于 \(\mathcal X_u\)，固定 乘子为 \(\eta\in\Theta\)。因此那里的带缓冲估计，连同 引理 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors) 的逆删除因子界， 在保留高度处提供了下文所需的反射分子假设：对于 下文所用的点，\(\Re(1-w)=a+6e\) 且 \(|\Im(1-w)|\le T_1\)，位于带缓冲的矩形内。恒等射线 限制使每个固定的 \(T\) 相位在 槽素因子处都等于一，同时不改变物理行或任何非单位零点。

<span id="prop:probe-errors" label="prop:probe-errors">\[prop:probe-errors\]</span> 设 \(51/100\le a\le1\)、\(0<e\le10^{-3}\)，并取 \[x_r=a+16e,\qquad w_r=1-a-6e,\qquad z_r=17/50.\] 选择 \(P_0\) 关于 \(e\) 与固定数据充分大。 对于 \(U,T_1\ge1\) 以及无六次幂因子、满足 \((u,S)=1\)、 \(q_u\asymp U\) 的行 \(u\)，设 \(\psi_u^*\) 为诱导 \(\chi_\bullet(u)\) 的本原特征。设 \(\mathcal W_u\) 为 \(\{w:\Re w=w_r,\ |\Im w|\le T_1\}\) 的任意子集。假设 \(\psi_u^*\) 非主，且对 \(w\in\mathcal W_u\) 一致成立， \[|L(1-w,\overline{\psi_u^*})|\ll U^\epsilon\] 其中幂次为任意指定的小量。 对于该行在所示动态区域上，用其前面的槽和定义 \(\mathcal B_i\)， 把每个 \(\mathcal B_p\) 解释为 \(G_p/H_p\)， 其中 \(G_p\) 来自方程 [\[old-eq:5.13c\]](#old-eq:5.13c)。所述的 \(P_0\) 选取使那里对每个槽素因子都有 \(H_p\ne0\)，正如证明开头 所证。该命题只在这个动态区域上断言各别的延拓。 把一个槽的主部与误差部分别定义为 \[\mathcal Q_i(u;z)=
       -\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)q_p^{z-1}\overline{\chi_p(u)},
 \qquad
 \mathcal D_i(u)=\mathcal B_i(u;x,w,z)-\mathcal Q_i(u;z).\] 则对槽的每个子集 \(I\) 以及同样的点 \(w\in\mathcal W_u\)， \[\label{old-eq:5.13e}
 \left|L^S(w,\chi_\bullet(u))\prod_{i\in I}\mathcal D_i(u)\right|
 \ll U^{a-1/2+O(e)+\epsilon}(3+T_1)^C
       \prod_{i\in I}P_i^{z_r-1/2+O(e)+\epsilon}.\] 主部保留物理行、所有零掩码以及 固定的恒等射线限制。特别地，其中心 正规化为 \[\mathcal Q_i(u;z)=-P_i^{z-1/2}
       \left(P_i^{-1/2}\sum_{p\in\mathcal P_i(Z)}
          \overline{\chi_p(u)}W_i(q_p/P_i)(q_p/P_i)^{z-1}\right).\] 在同样的点 \(w\in\mathcal W_u\) 处，且仅在这个动态区域上， 完整修正是有如下有限分解 \[\label{eq:dynamic-compensated-decomposition}
 \mathfrak H_{\eta,u,Z}
 =\mathcal H_{\eta,u}\prod_{i=1}^K(\mathcal Q_i+\mathcal D_i)
 =\mathcal H_{\eta,u}
   \sum_{I\subseteq\{1,\ldots,K\}}
       \prod_{i\in I}\mathcal D_i\prod_{i\notin I}\mathcal Q_i.\]

在这个区域中 \(\vartheta=(-w_r)_+\le6e\)。引理 [\[lem:local-euler\]](#lem:local-euler) 的 证明中的估计强化为：当 \(p\nmid u\) 时 \(H_p-1=O(Q^{-1-10e})\)，当 \(p\mid u\) 时 \(H_p-1=O(Q^{-10e})\)。增大固定的 \(P_0\)，使 所有这些素因子满足 \(|H_p-1|<1/2\)。方程 [\[old-eq:5.13c\]](#old-eq:5.13c) 中的全纯 因子 \(G_p\) 除以 \(H_p\)， 现在在整个区域上定义了 \(\mathcal B_p\)。当 \(w_r<0\) 时有界地远离零的 是 \(H_p\)，而不是可能奇异的原始因子 \(P_p\)。

因此，方程 [\[eq:holomorphic-selected-tuple\]](#eq:holomorphic-selected-tuple) 中的元组和在这个动态 区域上分解为 \(\mathcal H_{\eta,u}\prod_i\mathcal B_i\)。代入 \(\mathcal B_i=\mathcal Q_i+\mathcal D_i\) 证明了 方程 [\[eq:dynamic-compensated-decomposition\]](#eq:dynamic-compensated-decomposition)。这一分解 不会被用来把修正延拓到当前区域之外。

对 \(p\nmid u\)，方程 [\[old-eq:5.13b\]](#old-eq:5.13b) 以及关于 \(\mathcal E_p\) 的估计给出 \[|H_p(\mathcal B_p+\overline{\chi_p(u)})|
 \ll Q^{-x_r+2\vartheta}+Q^{-6z_r+2\vartheta}
       +Q^{4-5x_r-6z_r+2\vartheta}
       +Q^{1-w_r-6z_r+\vartheta}
 \ll Q^{-51/100}.\] 这四个指数分别被 \(-a-4e\)、\(-51/25+12e\)、\(49/25-5a-68e\)，以及 \(a-51/25+12e\) 所界。除以有界的 \(H_p\) 保持这一 估计。每个槽中素数的个数依理想 计数为 \(O(P_i)\)；因此其来自 \(p\nmid u\) 的总贡献，包括 \(Q^{z-1}\)，为 \(O(P_i^{z_r-51/100+\epsilon})\)。

对 \(p\mid u\)，可能的标记只有除子那么多个。一个 \(\mathcal E_p\) 中的单项式在 \(Q^{z-1}\mathcal B_p\) 中被乘以 \(Q^{z-1+x}\)，所以 在分离出 \(Q^z\) 之后，其指数为 \(x_r-1\) 加上该单项式的指数。对于六次赋值表的 非尾部边界项，这些指数在 \(e=0\) 时为 \[\begin{array}{c|ccccc}
 j&1&2&3&4&5\\\hline
 &a-2&1/2-2a&-a,\ 1-3a&1/2-2a&2-5a.
\end{array}\] 在正的 \(e\) 处，它们的变化分别是 \(+6e,-32e,(-26e,-48e),-42e,-80e\)。在所述范围内它们都严格 小于 \(-1/2\)。公共的 \(R\) 项还要更小： 它分离出 \(Q^z\) 之后的指数至多为 \(49/25-1-5a-80e<-1/2\)。 额外的赋值对与 \(m\) 值的比值为 \(|R|\le Q^{-11/10}\) 与 \(|V|=Q^{-51/25}\)，所以它们的几何和 保持这些界。带有额外 \(V\) 的严格第二族项在这一 正规化之后也小于 \(Q^{-1/2}\)。

唯一剩余的项是严格的 \((e_0,l,k,m)=(1,0,1,0)\) 项，它对 \(j\ge2\) 出现，为 \(-\eta(p)(Q-1)Q^{-x-w}\)。它在分离出 \(Q^z\) 之后的指数为 \(-w_r\)。 显式的重标度项 \(-Q^{-w}\) 在分离出 \(Q^z\) 之后的指数为 \(-1-w_r<-1/2\)，所以它无需进一步的估计。

设 \(\mathfrak f_u\) 为 \(\psi_u^*\) 的导子。写 \(u=\epsilon_u\prod_{p\mid u}p^{j_p}\)，其中 \(\epsilon_u\) 是一个单位。 对与 \(uS\) 互素的主的 \(n\)，互反律给出 \[\chi_n(u)=\epsilon_u^{(q_n-1)/6}
       \prod_{p\mid u}\mathcal R(p,n)^{j_p}\chi_p(n)^{j_p}.\] 单位指数按模六来读。素因子公式可延拓到 合数 \(n\)：当 \(A\equiv B\equiv1\pmod6\) 时， \[\frac{AB-1}{6}\equiv\frac{A-1}{6}+\frac{B-1}{6}\pmod6.\] 因此单位因子只依赖于 \(q_n\) 模 \(36\)，而 \(\mathcal R\) 乘积只依赖于 \(n\) 模 \(4\)。结合 \(\mathcal R\) 与局部符号的乘性， 所展示的范数同余式使右端在与 \(6u\) 互素的 整理想上具有乘性；将它延拓到它们的分式理想 群。一个模 \((36)\operatorname{rad}(u)\) 同余于一的生成元已经是主的，并使每个 所展示的因子为一。因此这个特征有一个射线 表示，其模为该固定的 \(2,3\) 模乘以 \(\operatorname{rad}(u)\)。它与 引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray) 的 Kummer 特征 \(\chi_\bullet(u)\) 在避开 \(S\) 的理想上一致。这些特征诱导 同一个本原特征：在主理想环 \(\mathcal O\) 中，中国剩余定理在共同模的每个射线类中 提供一个避开额外有限集 \(S\) 的表示元。在一个好的 素数 \(p\mid u\) 处，把该类以及所有其他好的剩余类固定为一， 并通过中国剩余定理改变模 \(p\) 的剩余。 剩余的局部特征 \(\chi_p^{j_p}\) 具有精确阶 \(6/\gcd(6,j_p)>1\)。因此它在 \(p\) 处的导子指数 恰好为一：所展示的射线模只含 \(p\) 的一次幂， 而该特征不能下降到省略 \(p\) 的模。 这是一个局部断言；理想特征可能仍然需要 \(2,3\) 处固定的正规化模。

由此可得，对任何由互不相同的选定分歧 标记构成的集合 \(J_0\)， \[\label{old-eq:5.13d}
 q_{\mathfrak f_u}\ll_S q_{\operatorname{rad}(u)}
       \le q_u\prod_{p\in J_0}q_p^{-(j_p-1)}.\] 本原分子的函数方程 、所假设的反射界，以及 Stirling 给出一项代价 \(q_{\mathfrak f_u}^{A_*}U^\epsilon(3+T_1)^C\)，其中 \[A_*=1/2-w_r=a-1/2+6e>0.\] 在一个选定的 \(p\mid u\) 处，本原特征已经取值 为零，所以在那里恢复原来的局部因子恰好 乘以一。其余被删去的 Euler 因子的根为 \(O_S(U)\)，代价至多为 \(U^{6e+\epsilon}\)，因为 \(w_r\ge-6e\)。

把一个误差槽的乘积展开为它们的互素素因子项、 它们已经受界的分歧项，以及它们的严格分歧 项。对于这一三角展开中的每个固定元组，设 \(J_0\) 恰为其严格分歧标记。它们是互不相同的，因为 槽的支撑彼此不交。在求和标记之前，把单一不等式 方程 [\[old-eq:5.13d\]](#old-eq:5.13d) 应用于整个 \(J_0\)。 分子连同这些局部因子， 包括每个选定素数处的 \(q_p^{z-1}\)，随后被以下诸式所界 \[U^{A_*+6e+\epsilon}(3+T_1)^C
 \prod_{p\in J_0}q_p^{z_r-w_r-(j_p-1)A_*}
 \le U^{a-1/2+12e+\epsilon}(3+T_1)^C
       \prod_{p\in J_0}q_p^{z_r-1/2},\] 因为 \(j_p\ge2\) 且 \(-w_r-A_*=-1/2\)。因此不同的选定 标记使用导子亏空的不同因子，并且这些 界同时成立。对除子那么多个分歧标记求和代价为 \(U^\epsilon\)，而互素标记具有更强的指数 \(z_r-51/100\)。这证明了方程 [\[old-eq:5.13e\]](#old-eq:5.13e)。

这一论证只在误差标记上使用三角不等式。它从不改变 物理行，也不改变任何主槽中的系数与掩码。 与元组无关的因子 \(\mathcal H_{\eta,u}\) 单独地 依引理 [\[lem:local-euler\]](#lem:local-euler) 代价为 \(U^\epsilon\)。相对于主槽的 中心尺度 \(P_i^{z_r-1/2}\)，一个误差槽因此在 后续的行计数中没有正的振幅指数。

###### 主局部因子。

在引理 [\[lem:local-euler\]](#lem:local-euler) 的第二 Euler 区域中，取 \(u=1\) 且 \(p\in1_T\)。于是方程 [\[old-eq:5.13b\]](#old-eq:5.13b) 中 \(v=1\)， 且在对 \(P_0\) 作同样固定的扩大之后 \(H_p\) 有正下界。对于这一区域上的 这条主行，定义 \(\mathcal B_p=G_p/H_p\)，并以与上面相同的槽和定义 \(\mathcal B_i\)。下界与不交支撑给出分别的主分解 \[\label{eq:principal-slot-factorization}
 \mathfrak H_{\eta,1,Z}(x,w,z)
 =\mathcal H_{\eta,1}(x,w,z)\prod_{i=1}^K\mathcal B_i(1;x,w,z)
 \qquad\text{在第二 Euler 区域中}.\] 这并不把中心的主/误差分解延拓到其所述的 动态区域之外。四个误差 指数现在是 \[-x_r,\qquad -6z_r,\qquad 4-5x_r-6z_r,
       \qquad 1-w_r-6z_r.\] 在那个区域中每一个至多为 \(-7/8\)。因此主 乘子满足 \[\label{eq:principal-local-approximation}
 \mathcal B_p=-1+O(Q^{-7/8}),\] 对所有虚部与目标单位相位一致。这 是用于正规化主留数的局部估计。

它也给出共享留数估计所需的绝对主修正。 事实上这里 \(G_p=H_p\mathcal B_p=O(1)\)，而 未选乘积依方程 [\[eq:unselected-local-product\]](#eq:unselected-local-product) 的第二区域 形式有一个有界的正优函数。每个环形槽中的理想 计数因此在第二 Euler 区域的每个固定实盒上，且对所有虚部一致地，给出 \[\label{eq:principal-local-tuple-bound}
 |\mathfrak H_{\eta,1,Z}(x,w,z)|
 \le\sum_{(p_i)\in\prod_i\mathcal P_i(Z)}
       \prod_i\bigl[|W_i(q_{p_i}/P_i)|q_{p_i}^{z_r-1}|G_{p_i}|\bigr]
       \prod_{\substack{p\notin S\\p\notin\{p_1,\ldots,p_K\}}}|H_p|
 \ll \prod_iP_i^{z_r}=Z^{\ell z_r}.\] 这里只用了分别的主行下界来获得局部 逼近；它并未断言一般 \(H_p\) 的非零性。

#### 其余围道的绝对界

动态分解并非在共享解析估计所用的每条围道上都可用。 下面的界转而保留每个 选定因子 \(G_p\)，然后再取绝对值。

<span id="lem:compensated-absolute-local-bounds" label="lem:compensated-absolute-local-bounds">\[lem:compensated-absolute-local-bounds\]</span> 设 \(Z\ge2\)，并设 \(u\) 是非零的无六次幂因子行，满足 \((u,S)=1\) 且 \(q_u\asymp U\ge1\)，比较常数为固定值。保留节 [1](#sec:compensation) 的 固定物理槽系统。以下 界对所有虚部与单位相位都一致。

1.  在 \[x_r=\beta_*+e,\qquad w_r=1/2,\qquad z_r=17/50,
     \qquad 0<e\le10^{-3},\] 有 \(G_p=O(1)\) 在选定素数 \(p\nmid u\) 处，且 在选定素数 \(p\mid u\) 处 \(G_p\ll Q^{1/2}\)。

2.  对每个固定的 \(z_\infty>2\)，在 \[x_r=w_r=2,\qquad z_r=z_\infty,\] 有 \(G_p=O_{z_\infty}(1)\) 在每个选定素数处。

在任一情形下，对全部选定元组的正和满足 \[\label{eq:absolute-local-tuple-bound}
 \sum_{(p_i)\in\prod_i\mathcal P_i(Z)}
       \prod_i\bigl[|W_i(q_{p_i}/P_i)|q_{p_i}^{z_r-1}|G_{p_i}|\bigr]
       \prod_{\substack{p\notin S\\p\notin\{p_1,\ldots,p_K\}}}|H_p|
 \ll_\epsilon U^\epsilon\prod_iP_i^{z_r}.\] 常数可能依赖于固定数据、\(e\)，以及在第二种情形下 依赖于 \(z_\infty\)，但不依赖于 \(Z,u\) 或诸虚部。这些估计在 \(P_p\) 或 \(H_p\) 的零点处仍然有效。

两组直线都位于 \(\epsilon_0=3/8\) 的第一 Euler 区域中。 其逐素数的亏量估计给出 \(H_p=O(1)\)，而 方程 [\[eq:unselected-local-product\]](#eq:unselected-local-product) 把所有未选因子的 正乘积界为 \(O_\epsilon(U^\epsilon)\)。

先考虑 \(x_r=\beta_*+e\)、\(w_r=1/2\) 与 \(z_r=17/50\)。 对选定的 \(p\nmid u\)，方程 [\[old-eq:5.13b\]](#old-eq:5.13b) 给出 \[|G_p+\overline{\chi_p(u)}H_p|
 \ll Q^{-x_r}+Q^{-6z_r}
       +Q^{4-5x_r-6z_r}+Q^{1-w_r-6z_r}.\] 这四个指数至多分别为 \(-7/8-e,-51/25,-483/200-5e,-77/50\)。 因此在不含 \(u\) 处 \(G_p=O(1)\)，无需除以 \(H_p\)。

对选定的 \(p\mid u\)，有 \(W=D=0\) 且 \(\mathcal E_p=P_p^*\)。方程 [\[old-eq:5.13c\]](#old-eq:5.13c) 变为 \[G_p=\overline{\eta(p)}Q^x(1-V)\mathcal E_p-Q^{-w}H_p.\] 在乘以 \(Q^{x_r}\) 之后，局部表的严格项 的指数至多为 \(1-w_r=1/2\)；对 \(j=1\) 它还含有因子 \(V\)。边界项 \(J_j\) 的指数，按 \(j=1,\ldots,5\) 的顺序， 为 \[-\frac12,\quad \frac32-2x_r,\quad
 \left(\frac32-2x_r,\,2-3x_r\right),\quad
 2-3x_r,\quad 3-5x_r.\] 它们分别被 \(-1/2,-1/4-2e,(-1/4-2e,-5/8-3e),-5/8-3e,-11/8-5e\) 从上界。公共的 \(R\) 项的指数为 \(4-5x_r-6z_r\le-483/200-5e\)。几何族中所有进一步的项 都减小这些幂次，因为 \(|R|\le Q^{-329/100-6e}\) 且 \(|V|=Q^{-51/25}\)。 最后 \(Q^{-w}H_p=O(Q^{-1/2})\)。因此在 \(u\) 上 \(G_p\ll Q^{1/2}\)， 在 \(H_p\) 的零点处亦然。

整除 \(u\) 的标记有除子那么多个，而一个槽含有 \(O(P_i)\) 个理想。因此它的正和为 \[\label{eq:small-line-positive-slot}
 \sum_{p\in\mathcal P_i(Z)}
       |W_i(q_p/P_i)|q_p^{z_r-1}|G_p|
 \ll P_i^{z_r}+U^\epsilon P_i^{z_r-1/2}
 \ll U^\epsilon P_i^{z_r}.\] 利用未选乘积的正优函数，并把所要求的 \(\epsilon\) 分配在固定数目的槽之间，证明了 第一组直线上的方程 [\[eq:absolute-local-tuple-bound\]](#eq:absolute-local-tuple-bound)。

现在固定 \(x_r=w_r=2\) 且 \(z_r=z_\infty>2\)。对不含 \(u\) 的选定素数，方程 [\[old-eq:5.13b\]](#old-eq:5.13b) 中的四个指数为 \(-2,-6z_\infty,-6-6z_\infty,-1-6z_\infty\)，所以 \(G_p=O_{z_\infty}(1)\)。在 \(u\) 上，乘以 \(Q^{x_r}\) 之后的严格项指数至多为 \(1-w_r=-1\)。边界指数为 \(-2,-5/2,(-4,-4),-11/2,-7\)，公共的 \(R\) 指数为 \(-6-6z_\infty\)，且 \(|R|=Q^{-8-6z_\infty}\)、\(|V|=Q^{-6z_\infty}\)。 重标度项为 \(O(Q^{-2})\)。于是 \(G_p=O_{z_\infty}(1)\) 在 \(u\) 上 也成立。一个正的槽和因此为 \(O_{z_\infty}(P_i^{z_\infty})\)。 结合方程 [\[eq:unselected-local-product\]](#eq:unselected-local-product)，这证明了 第二组直线上的方程 [\[eq:absolute-local-tuple-bound\]](#eq:absolute-local-tuple-bound)。

方程 [\[eq:compensated-poisson-identity\]](#eq:compensated-poisson-identity) 提供刚刚在低端受界的物理函数的完整高 表示。 命题 [\[prop:probe-errors\]](#prop:probe-errors) 与分子联合控制误差因子， 而引理 [\[lem:compensated-absolute-local-bounds\]](#lem:compensated-absolute-local-bounds) 提供 其余围道上的界。主要因子是命题 [\[prop:probe-errors\]](#prop:probe-errors) 中所展示的 素多项式。为计数那些这些因子与一个探测器见证 都很大的行，我们接下来证明 节 [8](#sec:refined-row-counts) 中所用的逆矩与四阶矩估计。

### 带素因子的逆矩

我们现在对一个乘以独立加权素数和的 逆 Dirichlet 多项式作界。该估计适用于节 [6](#sec:detector) 中的逆见证 连同来自局部补偿的选定主因子。 其证明使用节 [\[sec:marked-energy\]](#sec:marked-energy) 的完备化行能量。 最后一次放大给出在更长列长度上无六次幂因子行的 无标记估计。

#### 带标记估计的陈述

设 \(\nu\) 是一个固定的有限阶射线特征，其完整的 零延拓定义模的素支撑在 \(S\) 中。这整个 表示属于固定的算术数据；一个局部冻结的 移动零点支撑转而作为穿刺保留，其根 包含在下面的显式范数界中。 固定一个符号 \(\varepsilon_\chi\in\{1,-1\}\)，并令 \[\psi_u(n)=\nu(n)\chi_n(u)^{\varepsilon_\chi}.\] 这一定义中仅有的掩码是固定的排除以及 \(\chi_n(u)\) 的零延拓。 对光滑环形函数 \(W\)，定义 \[M_u(Z^r;W)=Z^{-r/2}\sum_n\mu(n)\psi_u(n)W(q_n/Z^r).\] 对固定的有限槽集合 \(I\)，设 \(\mathcal P_i\) 是 \(S\) 之外互不相交的 素数集，满足对 \(p\in\mathcal P_i\) 有 \(q_p\asymp Z^{z_i}\)。这些集合与系数 \(a_i(p)\) 与 \(u\) 无关，且 \(|a_i(p)|\le1\)。给定固定的光滑环形 函数 \(W_i\)，令 \[Q_u=\prod_{i\in I}Z^{-z_i/2}
       \sum_{p\in\mathcal P_i}a_i(p)\psi_u(p)W_i(q_p/Z^{z_i}),
 \qquad z=\sum_{i\in I}z_i.\] 空乘积为一。 由三角不等式，整个乘积 \(M_uQ_u\) 的固定有限和也是允许的， 只要每个求和项在其逆与其所有槽中使用一个共同的 \(\nu\)。

<span id="lem:marked" label="lem:marked">\[lem:marked\]</span> 固定非负参数 \(m,r,z_i\) 的有界范围、\(|I|\) 的一个界， 以及正常数 \(c_1,c_2\)。假设 \[r+2z\le m-c_1,\qquad 2r+8z\le3m-c_2.\] 则对每个 \(\epsilon>0\)， \[\label{old-eq:4.1}
 \sum_{\substack{u\in\mathcal O\\0<q_u\ll Z^m}}
       |M_u(Z^r;W)Q_u|^2\ll Z^{m+\epsilon}.\] 隐含常数可能依赖于固定算术数据、\(c_1,c_2\)、 有界参数范围，以及检验函数的有限多个光滑半范数， 但对素支撑及其有界系数一致。 该断言对任一公共符号 \(\varepsilon_\chi\) 成立，且对 槽的每个子集族成立。检验函数的范数扭曲对其高度 具有固定的多项式代价。对单个 槽长度除其所述素支撑的存在性外没有下界， 对这些长度也没有网格条件。

证明经过下面定义的典范族，其中 一个四次幂剩余符号在一个额外的无平方因子 理想上取平均。引理 [\[lem:canonical-moment\]](#lem:canonical-moment) 通过最终应用 引理 [\[lem:reflected-energy\]](#lem:reflected-energy) 以及一个使用两次带掩码 Poisson 变换的递归步骤来证明。在主贡献与尾部 被处理之后，保留部分用该族的、具有更短行范围的新的可容许和来界。 一个使用一次带掩码 Poisson 变换的单独初始化 随后推出引理 [\[lem:marked\]](#lem:marked)，而 最后一小节给出其对无六次幂因子行的更长无标记 推论。

#### 典范估计

使用节 [\[sec:marked-energy\]](#sec:marked-energy) 中定义的固定穿刺、无平方因子系数、行特征， 以及乘积形式标记。额外的 无平方因子标记现在被取平均，权重为除子有界的且 仅依赖于该标记。

下面是由两次 Poisson 变换所封闭的陈述。 其穿刺界是假设的一部分，因为一个冻结的移动 模不能当作固定算术数据的一部分来处理。 关于递归 Poisson 大筛框架，可比较 、，以及 ；当前的带标记递归将在下面证明。

<span id="lem:canonical-moment" label="lem:canonical-moment">\[lem:canonical-moment\]</span> 固定 \(M,N,V,z_0\) 的有界非负范围、槽数的一个界， 以及 \(c_*>0\)。设 \(f\) 取遍 \(S\) 之外、 满足 \(q_f\asymp Z^V\) 的无平方因子理想。设 \(w\) 是仅依赖于 \(f\) 的非负函数，满足对某个固定的 \(C\ge1\) 有 \(w(f)\le C d_{\mathcal O}(f)^C\)。\(C\) 与 \(w\) 的选择都不依赖于 \(Z\)、 当前各行，或任何其他被平均的变量。下面的隐含常数 可能依赖于 \(C\)，但对所有满足这一 固定界的 \(w\) 一致。设 \(\nu\) 是一个固定的 乘性有限射线特征，其完整的零延拓定义 模的素支撑在 \(S\) 中，并设 \(\rho(n)=1_{(n,\mathfrak r_\rho)=1}\) 是一个固定穿刺。二者都 与 \(k,f\) 无关。设 \(\mathfrak d\) 具有方程 [\[old-eq:4.2\]](#old-eq:4.2) 中的 乘积形式，其不交固定素数表的总 长度至多为 \(z_0\)，系数有界且与 \(k,f\) 无关。 不允许其他依赖于行的列系数或穿刺。 不存在额外的剩余系数 \(b(n)\)，即使是 与 \(k,f\) 无关的也没有：任意有界权重仅 允许作为所述单个素槽系数的乘积出现。

令 \(F_0=N+V\)。假设 \[\label{eq:invariant}
 \begin{gathered}
 q_{\mathfrak r_\rho}\le Z^{F_0-M-z_0-c_*},\\
 3M+6z_0+c_*\le4F_0.
 \end{gathered}\] 对每个光滑环形 \(W\) 与每个 \(\epsilon>0\)，定义 \[\label{eq:canonical-energy}
 \begin{split}
 \mathcal E={}&Z^{-V}\sum_f w(f)
 \sum_{\substack{k\in\mathcal O\\0<q_k\ll Z^M}}
 \Biggl|Z^{-N/2}\sum_{n\ {\rm sf}}
 \bar\alpha(n)\gamma_2(n)\nu(n)\rho(n)\\
 &\hspace{24mm}\times
 \chi_n(k)\chi_n(f)^4\mathfrak d(n)W(q_n/Z^N)\Biggr|^2.
 \end{split}\] 则 \(\mathcal E\ll Z^{F_0+\epsilon}\)。该常数在所述范围内对所有移动模 与冻结的外部理想一致。 它依赖于有限多个光滑半范数，并对分离的范数扭曲高度 具有固定的多项式依赖。对槽的所有子集族（使用原来的上界 \(z_0\)）， 包括空集族，同样的结论成立。

节 [\[sec:marked-energy\]](#sec:marked-energy) 中的反射能量为该族提供 最终估计。其余范围将被归约到 具有更短行的同一族。在两次 Poisson 变换之前，我们给出在有限归纳中传播光滑 半范数与高度阶的通用解析法则。

#### 半范数与高度阶的有限传播

我们使用下面关于有限估计序列的抽象陈述。它 并不断言任何特定的算术归约具备其假设。 其目的是精确地陈述，对变换后的剖面与 Fourier 系数测度，哪些一致界足以在外部高度截断之前 选定所有内部的导数阶。

记 \(\langle\boldsymbol t\rangle=1+|\boldsymbol t|\)。设一个有限有根 有向图没有有向环，且每条有向路径至多有 \(D\) 条边。在每个顶点 \(v\) 处设 \(\mathcal N_v(Z,\boldsymbol w,\boldsymbol t)\) 是一个非负量，其中 \(Z\ge1\)，\(\boldsymbol w\) 是固定的有限环形剖面元组， 而 \(\boldsymbol t\) 是有限维高度向量。剖面 维数、支撑与高度维数可能依赖于 \(v\)，但在整个 图中固定。这些量中允许有额外的标记； 下面每个界都要求对那些标记一致。

<span id="lem:finite-seminorm-propagation" label="lem:finite-seminorm-propagation">\[lem:finite-seminorm-propagation\]</span> 假设在每个顶点处有一个终端界 \[\mathcal T_v(Z,\boldsymbol w,\boldsymbol t)
 \le C_v Z^{a_v}p_{j_v}(\boldsymbol w)^{b_v}
                   \langle\boldsymbol t\rangle^{h_v}\] 其中 \(a_v\) 为固定实数，\(j_v,b_v,h_v\) 为有限非负数。再假设 \[\begin{split}
 \mathcal N_v(Z,\boldsymbol w,\boldsymbol t)
 \le{}&\mathcal T_v(Z,\boldsymbol w,\boldsymbol t)\\
 &+\sum_{e:v\to v'}Z^{a_e}\int_{\mathbb R^{d_e}}
 |K_e(Z,\boldsymbol w,\boldsymbol t;\boldsymbol\xi)|
 \mathcal N_{v'}\bigl(Z,\boldsymbol W_e,
       A_e\boldsymbol t+B_e\boldsymbol\xi\bigr)\,d\boldsymbol\xi,
 \end{split}\] 其中 \(A_e,B_e\) 是固定有界线性映射，而 \(\boldsymbol W_e=\boldsymbol W_e(Z,\boldsymbol w,\boldsymbol t,
\boldsymbol\xi)\) 是子剖面元组。允许空边和。 假设对每条边成立以下两个界。

对每个固定的 \(j\)，存在有限非负数 \(m_e(j),b'_e(j),c'_e(j)\) 与常数 \(C_{e,j}\) 使得 \[p_j(\boldsymbol W_e)
 \le C_{e,j}p_{m_e(j)}(\boldsymbol w)^{b'_e(j)}
       \langle\boldsymbol t\rangle^{c'_e(j)}
       \langle\boldsymbol\xi\rangle^{c'_e(j)}.\] 对每个固定的 \(H\ge0\)，存在有限非负数 \(\ell_e(H),b_e(H),c_e(H)\) 与常数 \(C_{e,H}\) 使得 \[\int_{\mathbb R^{d_e}}|K_e(Z,\boldsymbol w,\boldsymbol t;
            \boldsymbol\xi)|\langle\boldsymbol\xi\rangle^H
                         \,d\boldsymbol\xi
 \le C_{e,H}p_{\ell_e(H)}(\boldsymbol w)^{b_e(H)}
                 \langle\boldsymbol t\rangle^{c_e(H)}.\] 半范数指标可以向上取整为整数。所有这些常数与 指标对 \(Z\) 与额外标记一致；指数 \(a_v,a_e\) 是固定实数，与所要求的半范数与高度阶无关。

则存在有限的 \(J,B,H\) 与 \(C\)，使得在根 \(v_0\) 处， \[\mathcal N_{v_0}(Z,\boldsymbol w,\boldsymbol t)
 \le C Z^E p_J(\boldsymbol w)^B\langle\boldsymbol t\rangle^H,
 \qquad
 E=\max_{v_0\to\cdots\to v}
       \left(a_v+\sum_{e\text{ 在路径上}}a_e\right).\] 指标 \(J,B,H\) 可以沿至多 \(D\) 个阶段向后选取。 特别地，它们在施加任何限制 \(|\boldsymbol t|\le T_1=Z^\tau\) 之前就已固定。

对积分中有限个子乘积，同样的结论成立。 确切地说，一个边项可以改为具有以下形式 \[Z^{a_e}\int_{\mathbb R^{d_e}}|K_e|
 \prod_{r=1}^{r_e}
 \mathcal N_{v_{e,r}}\bigl(Z,\boldsymbol W_{e,r},
       A_{e,r}\boldsymbol t+B_{e,r}\boldsymbol\xi\bigr)^{\theta_{e,r}}
 \,d\boldsymbol\xi,\] 其中 \(r_e\ge1\) 是固定整数，\(\theta_{e,r}\ge0\) 固定，所有子项都有更小的 剩余深度，且每个子剖面满足其自身版本的 所述剖面界。联合系数测度满足同样的 加权界。在此情形下，由下式递归定义范数指数 \[E_v=\max\left\{a_v,\ \max_e
             \left(a_e+\sum_{r=1}^{r_e}\theta_{e,r}E_{v_{e,r}}\right)\right\}.\] 结论在 \(E=E_{v_0}\) 时成立。这一形式包含来自 Cauchy–Schwarz 的两个非负 子估计的平方根。

在终端顶点处，该断言就是其所述界。假设某个子项 已经被以下诸式所界 \(C Z^{E'}p_{J'}(\boldsymbol W_e)^{B'}
 \langle A_e\boldsymbol t+B_e\boldsymbol\xi\rangle^{H'}\)。 由于线性映射有界， \[\langle A_e\boldsymbol t+B_e\boldsymbol\xi\rangle^{H'}
 \ll_e\langle\boldsymbol t\rangle^{H'}
              \langle\boldsymbol\xi\rangle^{H'}.\] 子剖面界把幂 \(B'c'_e(J')\) 加到这两个高度指数中的每一个上， 并把其剖面因子替换为 \(p_{m_e(J')}(\boldsymbol w)^{B'b'_e(J')}\)。使用系数测度 界，取 \(H_e=H'+B'c'_e(J')\)。这条边的贡献至多为 \[C_e Z^{a_e+E'}
 p_{\max\{m_e(J'),\ell_e(H_e)\}}(\boldsymbol w)^{B'b'_e(J')+b_e(H_e)}
 \langle\boldsymbol t\rangle^{H_e+c_e(H_e)}.\] 每个所展示的指标都是有限的。在这些指标与 有限多条出边上的终端指标中取最大值，必要时增大 剖面指数，因为 \(p_j(\boldsymbol w)\ge1\)。 这证明了父界，其指数等于经过该顶点的 最大路径指数。对无环图作反向归纳完成了 证明。这些选择都没有涉及外部截断或滞后的 导数阶。

对于乘积形式，代入每个子结点已经证明的界，并将其提升到 \(\theta_{e,r}\)。系数测度必须积分的 \(\langle\boldsymbol\xi\rangle\) 的总幂次为 \[H_e=\sum_{r=1}^{r_e}\theta_{e,r}
       \bigl(H_r+B_r c'_{e,r}(J_r)\bigr).\] 父剖面的幂次和 \(\langle\boldsymbol t\rangle\) 的幂次是对应的有限和，随后是在 \(H_e\) 处的单个 系数测度界。\(Z\) 的幂次按 \(E_v\) 的显示递推式相加。对有限多项取最大值，即以同样的反向归纳 证明这一推广。

<span id="cor:indexed-seminorm-propagation" label="cor:indexed-seminorm-propagation">\[cor:indexed-seminorm-propagation\]</span> 在引理 [\[lem:finite-seminorm-propagation\]](#lem:finite-seminorm-propagation) 中，设 \(\boldsymbol\ell\) 表示顶点 \(v\) 处的任意 容许长度和外标签，并设 \(\Phi_v(\boldsymbol\ell)\) 为其所需的范数指数。假设在除以 \(Z^{\Phi_v(\boldsymbol\ell)}\) 之后，终端界具有该引理中的形式，且指数 \(\delta_v\) 固定。一条边 可以由依赖于 \(Z\) 的族 \(\Gamma_e\) 以及非负测度 \(\nu_e\) 作为指标，且可以具有形式 \[\int_{\Gamma_e}\int_{\mathbb R^{d_e}}
 Z^{a_e(\boldsymbol\ell,\gamma)}|K_{e,\gamma}|
 \prod_{r=1}^{r_e}\mathcal N_{v_{e,r}}
  \bigl(Z,\boldsymbol\ell_{e,r},\boldsymbol W_{e,r},
        A_{e,r}\boldsymbol t+B_{e,r}\boldsymbol\xi\bigr)^{\theta_{e,r}}
 \,d\boldsymbol\xi\,d\nu_e(\gamma),\] 其中子标签 \(\boldsymbol\ell_{e,r}\) 可以依赖于 \(\boldsymbol\ell,\gamma\)。假设关于这些标签 一致地有 \[\label{eq:indexed-exponent-defect}
 a_e(\boldsymbol\ell,\gamma)
   +\sum_r\theta_{e,r}\Phi_{v_{e,r}}(\boldsymbol\ell_{e,r})
   -\Phi_v(\boldsymbol\ell)\le\delta_e,\] 且 \(\delta_e\) 固定，并且该引理的子剖面界成立。还假设对每个固定的 \(H\ge0\)， \[\label{eq:indexed-coefficient-measure}
 \int_{\Gamma_e}\int_{\mathbb R^{d_e}}|K_{e,\gamma}|
       \langle\boldsymbol\xi\rangle^H\,d\boldsymbol\xi\,d\nu_e(\gamma)
 \le C_{e,H}Z^{\delta_e^{\mathrm{mass}}}
       p_{\ell_e(H)}(\boldsymbol w)^{b_e(H)}
       \langle\boldsymbol t\rangle^{c_e(H)},\] 其中 \(\delta_e^{\mathrm{mass}}\) 与 \(H\) 无关地固定。当这些量是通过分离一个剖面而得到的平方 后的 Hilbert 空间行范数时，本假设必须使用这些行共同的系数测度。在有限多个深度的每一个处 只需有有限多种边类型；\(\Gamma_e\) 的基数可以随 \(Z\) 变化。

于是 \(\mathcal N_v/Z^{\Phi_v(\boldsymbol\ell)}\) 具有 引理 [\[lem:finite-seminorm-propagation\]](#lem:finite-seminorm-propagation) 的结论，关于 \(\boldsymbol\ell\) 一致，终端指数为 \(\delta_v\)，边指数为 \(\delta_e+\delta_e^{\mathrm{mass}}\)。特别地，所有所需的半范数和高度 阶数都是有限的且独立于外部截断。

置 \(\overline{\mathcal N}_v=Z^{-\Phi_v(\boldsymbol\ell)}\mathcal N_v\)。在某条边中的代入与 方程 [\[eq:indexed-exponent-defect\]](#eq:indexed-exponent-defect) 将其范数幂次界定为 \(Z^{\delta_e}\) 乘以正规化子结点 之积。代入它们的归纳界。如同引理 [\[lem:finite-seminorm-propagation\]](#lem:finite-seminorm-propagation) 的乘积证明，所需的 系数矩为 \[H_e=\sum_r\theta_{e,r}
              \bigl(H_r+B_r c'_{e,r}(J_r)\bigr),\] 它是有限的且与 \(\gamma\) 无关。方程 [\[eq:indexed-coefficient-measure\]](#eq:indexed-coefficient-measure) 在此阶数处贡献 \(Z^{\delta_e^{\mathrm{mass}}}\) 以及仅有限的剖面和高度阶数。因此关于有限多种边类型的反向 归纳恰好给出所述的归一化递推。在子结点内部被平均的标签在整个论证过程中都留在该子结点内部； 它不是 \(\nu_e\) 的第二个积分变量。

我们明确说明本推论中离散标签是如何归一化的。在相关的加权 Cauchy 不等式之后，假设非负外测度 满足 \(\sum_{\gamma\in\Gamma}w_\gamma\le C Z^{c+\epsilon}\)，其中固定的 \(c\) 和 \(\epsilon\) 在选择高度阶数之前选定。对于该块上共同的逐标签前因子 \(Z^{a_{\mathrm{raw}}}\)，置 \[d\nu_\Gamma(\gamma)=Z^{-c}
             \sum_{\gamma\in\Gamma}w_\gamma\,\delta_\gamma,
 \qquad \nu_\Gamma(\Gamma)\le C Z^\epsilon.\] 这里 \(\delta_\gamma\) 表示单位点质量。对于使所示积分为有限的非负 \(B_\gamma\)，精确恒等式为 \[\label{eq:normalized-label-measure}
 \begin{split}
 &Z^{a_{\mathrm{raw}}}\sum_{\gamma\in\Gamma}w_\gamma
              \int |K_\gamma(\boldsymbol\xi)|B_\gamma(\boldsymbol\xi)
                                      \,d\boldsymbol\xi\\
 &\qquad=Z^{a_{\mathrm{raw}}+c}
       \int_\Gamma\int |K_\gamma(\boldsymbol\xi)|B_\gamma(\boldsymbol\xi)
                                      \,d\boldsymbol\xi\,d\nu_\Gamma(\gamma).
 \end{split}\] \(K_\gamma\) 的一致加权矩现在给出方程 [\[eq:indexed-coefficient-measure\]](#eq:indexed-coefficient-measure)，只留下剩余的 \(Z^\epsilon\) 质量。因此，已经包含计数 \(c\) 的显示指数必须使用这个归一化测度；保留未归一化的 和会把相同的标签计算两次。该规则涉及的是加权质量，而不是在该质量之外的基数。它仅在行相关的 可选择性仍留在子结点内部、或已被某个非负不等式移除之后才被应用。仍在子范数中被平均的标签 不包含在 \(\Gamma\) 中。

对于小的核振幅有一个单独的归一化。单剖面半范数 \(p_j(w)\) 是齐次的，而 \(p_j(\boldsymbol w)=1+\sum p_j(w_i)\) 不是。假设固定块上的联合环形剖面满足：对标量 \(0<m_R\le1\)， \[p_j(F_R)\le m_R C_j p_{\ell(j)}(\boldsymbol w)^{b(j)}
                         \langle\boldsymbol t\rangle^{h(j)}
       \qquad(j\ge0).\] 可以把 \(F_R\) 保留在 Fourier 系数测度中，其加权 \(L^1\) 范数此时包含因子 \(m_R\)。或者，写 \(F_R=m_R\widetilde F_R\) 并把 \(m_R\) 放到该测度之外。若多项式或行向量 \(\mathcal P(F_R)\) 关于整个剖面是线性的，则 \[\mathcal P(F_R)=m_R\mathcal P(\widetilde F_R),\qquad
 \|\mathcal P(F_R)\|_2^2=m_R^2\|\mathcal P(\widetilde F_R)\|_2^2.\] 含 \(\widetilde F_R\) 的元组具有有界的（而非小的）半范数。标量只有在乘以整个差时才能从中心差中 移除。在已展开的二次表达式中出现一次的核贡献一个因子 \(m_R\)，而不自动是其平方。这些约定要么 使用小测度，要么使用外部标量，绝不两者兼用。如果正的行范围稍后将被扩大，则先在实际环带上固定 该标量与共同剖面，并在扩大之前得到包含该标量的范数不等式。

以下是验证这两条边假设的充分解析方法。设 \(m(\boldsymbol y)\) 为固定的范数单项式，\(\chi\) 为在 固定环带之积中具有紧对数支集的光滑截断。假设一个归一化核具有 Euler 界 \[|(r\partial_r)^jK(r)|\le C_{A,j}\mathfrak S_{m(A,j)}
                                      \min(1,r^{-A}),\] 其中 \(\mathfrak S_k\) 是指定的有限输入半范数与多项式高度界的一个递增族，且 \(m(A,j)\) 关于 \(j\) 取非减。乘积法则和链式法则给出，对 \(R>0\) 一致地， \[\label{eq:normalized-kernel-profile}
 p_j\bigl(\chi(\boldsymbol y)K(Rm(\boldsymbol y))\bigr)
 \le C'_{A,j}\mathfrak S_{m(A,j)}\min(1,R^{-A}).\] 确实，作用于核的 \(y_i\partial_{y_i}\) 等于 \(m\) 中 \(y_i\) 的固定指数乘以 \(r\partial_r\)，且 \(m\) 在截断支集上有上界和下界。微分不会产生额外的因子 \(R\)。当这三个核估计可用时，同样的论证 保持带有 \(\min(R^{1/4},1,R^{-A})\) 的界。衰减阶 \(A\) 在每个所要求的 \(j\) 处相同；只有输入阶 及其有限的高度次数增加。对于 \(c>0\) 的旧窗 \(w(c m(\boldsymbol y))\)，Euler 导数由 \(w\) 的整体 对数半范数界定，且不引入依赖于导数阶的 \(c\) 的幂。诸如 \(y^{-1/2}\) 的归一化实幂遵循同样的规则。 归一化范数的纯扭转只插入其高度的固定幂。

普通的径向 Fourier 半范数必须在径向尺度被归一化之后才能使用。对于两个实维数中的固定环形 \(w\)， \(f_R(x)=w(R|x|^2)\) 满足 \[\|\partial^j f_R\|_1=R^{j/2-1}\|\partial^j f_1\|_1\] 对任意阶为 \(j\) 的固定方向导数，由 \(x\mapsto\sqrt R x\) 得到。因此一个未归一化的收缩径向试验 可能引入依赖于 \(j\) 的尺度幂。充分的假设是在其所述行尺度处具有固定形状的径向 Schwartz 试验， 或者在该尺度处为零附近常值的径向 \(C_c^\infty\) 试验。归一化之后， 引理 [\[lem:kernel-seminorms\]](#lem:kernel-seminorms) 应用于其固定变换，移动的尺度比只以 方程 [\[eq:normalized-kernel-profile\]](#eq:normalized-kernel-profile) 中的方式出现。例如在 \(q_u=U_0y\) 上 \(q_u^{-1/2}=U_0^{-1/2}y^{-1/2}\)；中心幂属于范数指数，而环形因子具有与阶无关的尺度界。同样 \(q_u^{it}=U_0^{it}y^{it}\)，且在对归一化剖面微分之前，把中心单位相位作为标量分离出来。

对数 Fourier 分离在一个坐标表内使用联合截断，该坐标表包含耦合光滑因子中出现的每个归一化范数。 导出的非光滑行掩码和标签掩码留在该因子之外，不需要坐标。一个用作此类坐标、初始范围从某个球 一直到范数 1 的非零范数，必须首先被划分成针对当前扇区固定的共同整环带；零频率是单独的。在有界 对数范围内，对于固定数量的 \(d\) 个变量，有 \(O((1+\log Z)^d)\) 个这样的块，因此它们的计数花费 一个预先选定的小幂。截断及其整个支集只依赖于块中心和固定数据，而不依赖于行范数内标签的个别值。 只要耦合光滑因子是这单个联合函数且不再依赖于个别标签，其 Fourier 密度就对这些行是共同的，正如 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 所要求的；对行相关密度的分别一致界不能推出同样的 Hilbert 空间 不等式。非光滑掩码通过精确的算术恒等式被保留或消解，绝不被微分，也绝不被并入为依赖于标签的 尖锐 Fourier 选择子。

最后，假设一个固定的 \(\xi>0\)，内部二分比 \(R>Z^\xi\) 的绝对算术计数至多为 \(Z^B R^b\)。带有 因子 \(R^{-A}\) 的系数界给出，对 \(A>b\)， \[\sum_{\substack{R\ \mathrm{dyadic}\\R>Z^\xi}}Z^B R^{b-A}
       \ll Z^{B-\xi(A-b)}.\] 从固定的 \(B,b,\xi\) 和所需的内部节省中选择 \(A\)。实际的界还可能含有有限输入半范数和多项式高度 因子；它们进入有限传播图。这一尾部估计不是对所有高度都一致的无高度断言。参数 Sobolev 只增加 固定数量的剖面导数和高度维数，且所有这些内部阶数都在外部截断之前选定。

最后假设图及其所有核与环形阶数都已被固定，给出高度次数 \(H\)。假设一个额外的、外部的分离使用环形 剖面，其 \(p_j\) 对每个固定 \(j\) 关于 \(Z\) 一致有界，或使用前面各引理中的加权 Mellin 范数或环形 范数在每个固定阶处一致有界的非环形剖面，并且其被丢弃的被积函数具有界 \(Z^{B_0}\langle\boldsymbol t\rangle^{J_0}\)，其中 \(B_0,J_0\) 固定。外部截断被要求留在图之外： 它不会用依赖于截断的剖面来替换剖面 \(\boldsymbol w\) 或核 \(K_e\)。给定保留的允许高度 \(\delta>0\)， 先选择 \(0<\tau<\delta/(1+H)\)。于是对 \(T_1=Z^\tau\) 有 \((1+T_1)^H\le2^H Z^\delta\)。在此选择 之后，以权 \(J_0\) 和任意满足 \(N>(B_0+M)/\tau\) 的固定整数 \(N\)， 方程 [\[eq:late-fourier-tail\]](#eq:late-fourier-tail) 使积分后的外部尾为 \(O(Z^{-M})\)，对任意给定的 \(M>0\)。对于 水平连接，使用方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 并加上该额外的固定高度权，或对联合高斯切片 使用方程 [\[eq:joint-gaussian-slice\]](#eq:joint-gaussian-slice)。当这样的切片上其它坐标被延拓到整个实轴时，伴随的算术 因子必须在这些坐标上有整体界；进入分母且仅在带缓冲区域内被控制的坐标必须保持限制在该区域内。 外部常数可以依赖于 \(N\) 和固定数据。这一较晚的选择不改变任何内部剖面或内部阶数 \(J,H\)，这正是 所断言的依赖次序。

#### 带掩码的有限 Poisson 求和

我们现在证明引理 [\[lem:marked\]](#lem:marked)，使用节 [2](#sec:arithmetic) 的算术约定以及 引理 [\[lem:reflected-energy\]](#lem:reflected-energy) 处理终端情形。递归归约使用下面这种 Poisson 求和形式的两次 应用，初始化使用一次。其显式的除数变量保留每个零延拓。

<span id="lem:masked-poisson" label="lem:masked-poisson">\[lem:masked-poisson\]</span> 设 \(\psi\) 为模理想 \(m\) 的本原有限特征，在非单位上以零延拓，并设 \(R\) 为任意理想。设 \(\Phi(q_z)\) 为 \(\mathbb C\) 上的径向 Schwartz 函数，并设 \(\mathcal F\Phi(q_y)\) 表示其对 自对偶测度和核 \(e(-zy)\) 的 Fourier 变换。对 \(K>0\)， \[\label{eq:masked-poisson}
 \begin{split}
 &\sum_{k\in\mathcal O}\psi(k)1_{(k,R)=1}\Phi(q_k/K)\\
 &\quad=\frac{K\gamma(\psi;m)}{\sqrt{q_m}}
 \sum_{d\mid\operatorname{rad}R}\frac{\mu(d)\psi(d)}{q_d}
 \sum_{h\in\mathcal O}\bar\psi(h)
       \mathcal F\Phi\!\left(\frac{Kq_h}{q_dq_m}\right),
 \end{split}\] 其中 \(\gamma(\psi;m)=q_m^{-1/2}\sum_{x\bmod m}\psi(x)e(x/m)\)。 对非主本原特征，\(|\gamma(\psi;m)|=1\) 且 \(h=0\) 项为零。对主本原特征，约定为 \(m=1,\ \gamma(1;1)=1,\ \psi(h)=1\)，包括在 \(h=0\) 处。

将掩码展开为 \(\sum_{d\mid\operatorname{rad}R,\ d\mid k}\mu(d)\) 并写 \(k=dk'\)。尺度变为 \(K/q_d\)，而特征贡献 \(\psi(d)\)。模 \(m\) 的剩余类中的 Poisson 求和有前因子 \(K/(q_dq_m)\)。 其有限变换为 \[\sum_{x\bmod m}\psi(x)e(hx/m)
   =\sqrt{q_m}\gamma(\psi;m)\bar\psi(h).\] 对单位 \(h\)，这由变量替换得到。对非单位 \(h\)，由本原性变换为零；对 \(m=1\)，所述的通常 约定适用。这证明了方程 [\[eq:masked-poisson\]](#eq:masked-poisson)。对非主本原特征，有限 Parseval 给出 \(\sum_h|\sum_x\psi(x)e(hx/m)|^2=q_m\sum_x|\psi(x)|^2\)。写 \(\phi(m)=|(\mathcal O/m)^\times|\)，有 \(\phi(m)\) 个单位 \(h\)，其模均为 \(\sqrt{q_m}|\gamma(\psi;m)|\)，且 \(\sum_x|\psi(x)|^2=\phi(m)\)。因此 \(|\gamma(\psi;m)|=1\)。

一个固定的射线限制可以首先展开为有限多个特征。每一个随后被其本原诱导特征替代，被移除的局部零 延拓保留在 \(R\) 中；同一公式逐项适用。对主模，非零频率的绝对和是 \(O_\Phi(d_{\mathcal O}(\operatorname{rad}R))\)。确实，对所有 \(A>0\)， \[A\sum_{h\ne0}|\mathcal F\Phi(Aq_h)|\ll_\Phi1.\] 当 \(A\le1\) 时格点计数证明这一点，当 \(A\ge1\) 时 Schwartz 衰减证明之。以 \(A=K/q_d\) 对 \(d\) 求和此界。在下面每次使用时，相关的非空行尺度都有 \(K\ge1\)，因此这同样是 \(O(KZ^\epsilon)\)。当在分离一个非主和时加入或移去主的非零频率时，它们将携带与该和相同的 外行掩码；它们的绝对贡献不大于这个完整的主界。

#### 典范归约及其归纳

我们现在证明引理 [\[lem:canonical-moment\]](#lem:canonical-moment)。反射能量处理短完备化；剩余的块经过两次 Poisson 变换以产生具有较短行的容许典范和。

解析选择的次序由推论 [\[cor:indexed-seminorm-propagation\]](#cor:indexed-seminorm-propagation) 组织，该推论见 节 [6.3](#sec:moment-propagation)。其带指标的结论将分别用于每个正的 Cauchy 侧和；下面的证明验证所需的共同系数测度、固定范数损失和有限深度。

在每个结点处，每个联合 \((f,k)\) Hilbert 空间使用当前的标签测度 \(w(f)\)，并且该因子在每个 父 \(f\)-和中恰好保留一次，直到方程 [\[eq:inverse-old-label-fibre\]](#eq:inverse-old-label-fibre) 移除旧标签。

在每个结点处保持参数 \(N,V,M\) 固定，并写 \[F=N+V,\qquad Q=\log_Zq_{\mathfrak r_\rho}.\] 这里 \(F\) 是实长度和 \(N+V\)，故在起始结点处 \(F=F_0\)。在具有余量 \(c_{\rm node}\) 的 结点处的两个假设恰好是 \[\label{eq:inverse-fixed-invariant}
 F-M-Q-z_0\ge c_{\rm node},\qquad
 4F-3M-6z_0\ge c_{\rm node}.\] 特别地 \(M+z_0+c_{\rm node}\le F\)。数 \(Q\) 是已固定穿孔根式的实际对数范数，而不是二分中心。 参数 \(M\) 是固定的对数行长；第一次 Poisson 试验的尺度为 \(Z^M\)。

设 \(M_{\max}\) 界定起始行长。选择 \(0<d\le c_*/200\) 并置 \[D=\left\lceil\frac{M_{\max}+2}{d}\right\rceil+1.\] 我们使用正参数 \(\eta,\tau,\pi,\tau_{\rm ref},\pi_{\rm ref}\)，按证明末尾的量词次序选取。 这里 \(\eta\) 是仅界定固定环形比之对数的局部化容差，\(\tau\) 是两个 Poisson 尾部比较中的共同 容差，\(\pi\) 界定自由选择的局部小幂损失之总和。在深度 \(h\) 处置 \[c_h=c_*-7h\eta,\qquad c_{\rm node}=c_h,\] 并施加行上限 \(M\le M_{\max}-hd\)。我们通过对 \(h\le D\) 的反向归纳证明该估计。下面每个保留 的行参数都是非负的。我们将证明，非终端的一步至少使其减少 \(d\)，在两个所需余量中的任一个至多 损失 \(7\eta\)，并使能量指数至多增加 \(40\eta+\tau+\pi\)。不会有任何不变量从固定的 \(F=N+V\) 传递到实际的列范数。

###### 短完备化。

方程 [\[eq:marked-completion\]](#eq:marked-completion) 中立方因子的 Möbius 反演给出精确恒等式 \[\label{eq:marked-completion-inversion}
 \begin{split}
 &Z^{-N/2}\sum_{n\ {\rm sf}}a(n)\chi_n(k)\chi_n(f)^4
       \mathfrak d(n)W(q_n/Z^N)\\
 &\quad=
 \sum_h\frac{\mu(h)\bar\alpha(h)^3\Psi_k(h)^3}{q_h}
       \mathcal T_{\mathfrak d_h}(Z^N/q_h^3;k),
 \qquad \mathfrak d_h(A)=\mathfrak d(h^3A).
 \end{split}\] 为了检查标记和归一化，展开右边并置 \(c=hb\)。因子 \(V_*(y)=y^{1/2}W(y)\) 把绝对系数变为 \[Z^{-N/2}\bar\alpha(c)^3\Psi_k(c)^3q_c^{1/2}
       \sum_{h\mid c}\mu(h).\] 标记是 \(\mathfrak d(nc^3)\)，与除数 \(h\) 无关。除数和除非 \(c=1\) 外为零，这证明了该恒等式。 这里使用了 \(\Psi_k\) 的乘性，包括其穿孔。

使用一个固定的光滑二分剖分，其理想中心非负，单位二分元的中心为零。假设 \(V<d\) 且 \(h\)-二分元的中心 \(\ell_1\) 小于 \(d\)。冻结 \(h\)，把其整除的槽位分配给它，并将其余的保留 在完备化指标上。一个存活下来的槽位此时具有单独的系数 \(a_i(p)1_{p\nmid h}\)。由于 \(h\) 固定，这是一个有界的系数，与当前的 \(k,f\) 无关，在相同的名义环带上并具有相同的上限。它不是 无限制的原始系数；下面的递归分支通过子零点分别恢复其原始的槽位表。对一个活跃的子集定义 \(z_a\) 为其名义槽位长度之和。分配只会删除槽位，故恰有 \(0\le z_a\le z_0\)；实际的元组范数 从不被用作这个上限。联合 \((f,k)\) Hilbert 空间中的三角不等式对固定环带使用 \(\sum_{q_h\asymp Z^{\ell_1}}q_h^{-1}\ll1\)，除了单独选取的分配除子损失之外。有界因子 \(\Psi_k(h)^3\) 是该空间中的一个压缩。

写 \(\widehat h=\log_Zq_h\)。完备化在实际尺度 \(N_*=N-3\widehat h\) 处。其固定支集给出 \(\widehat h\le\ell_1+\eta<d+\eta\)，一旦施加下面指定的固定环形阈值。在 引理 [\[lem:reflected-energy\]](#lem:reflected-energy) 中，保留实际的剩余行二分元并选取相同的阈值使得 \[\label{eq:inverse-terminal-width}
 H\le M-O+\eta,\qquad
 T_d-S_0-B_0\le2M-O+Q+V-N_*+2z_a+\eta.\] 这些是方程 [\[eq:actual-residual-row-dyad\]](#eq:actual-residual-row-dyad) 和 [\[eq:common-width-charge\]](#eq:common-width-charge)，而不是对于 扩大后的行范围的估计。代入 \(N_*=N-3\widehat h\) 和 方程 [\[eq:inverse-fixed-invariant\]](#eq:inverse-fixed-invariant) 中的第一个不等式给出 \[\label{old-eq:4.9}
 T_d-S_0-B_0
 \le M-O+2z_a-z_0-c_{\rm node}+5d+4\eta.\] 确实，附加项为 \(2V+3\widehat h+\eta<5d+4\eta\)。

同时选取阈值使得 \(e_\lambda\ge-\eta\)，并如引理 [\[lem:reflected-energy\]](#lem:reflected-energy) 那样丢弃整个 反射尾部二分元。于是每个保留的二分元满足 \(v+3\ell_b+e_\lambda\le T_d+\tau_{\rm ref}\)。方程 [\[old-eq:4.6\]](#old-eq:4.6) 的行分支在去掉其 非正项后满足 \[E_{\rm ref}\le M+z_a+\tfrac53\eta
       \le F-c_{\rm node}+\tfrac53\eta.\] 对于 \(u=z_a\) 的列分支，保留的对偶界首先给出 \(E_{\rm ref}\le O/2+(T_d-S_0-B_0)+5\eta/3+\tau_{\rm ref}\)。 方程 [\[old-eq:4.9\]](#old-eq:4.9) 和第一个不变量随后给出 \[\label{old-eq:4.10}
 E_{\rm ref}\le F-2c_{\rm node}+5d+\tfrac{17}{3}\eta+\tau_{\rm ref}.\] 若 \(u\ne z_a\)，其定义蕴含 \(u\ge v/2\)。保留的对偶界现在首先给出 \[E_{\rm ref}\le O/2+(T_d-S_0-B_0)/2+z_a
                    +\tfrac76\eta+\tfrac12\tau_{\rm ref}.\] 利用方程 [\[old-eq:4.9\]](#old-eq:4.9)、\(z_a\le z_0\)，然后利用第二个不变量可推出 \[\label{old-eq:4.11}
 E_{\rm ref}\le F-M/4-3c_{\rm node}/4+(5/2)d
                    +\tfrac{19}{6}\eta+\tfrac12\tau_{\rm ref}.\] 使用带有总局部损失 \(\pi_{\rm ref}\) 的反射估计，包括其自由选择的指数、标签除子界以及有限 多个对数和。若 \[c_{\rm node}\ge c_*/2,\qquad
 d\le c_*/200,\qquad \eta,\tau_{\rm ref},\pi_{\rm ref}\le c_*/1000,\] 则加上 \(\pi_{\rm ref}\) 之后，三个界都严格小于 \(F\)。在最后一个界中 \(M\ge0\)。当 \(z_0=0\) 时只出现 \(u=z_a=0\)。反射估计是对每个固定的 \(f\) 施加的；加权质量界 \(\sum_f w(f)\ll Z^{V+\pi_{\rm ref}}\) 表明，对其平方后的界关于 \(f\) 求和至多花费这个量， 该量已包含在总损失中，并抵消了外部的 \(Z^{-V}\)。因此没有移动的四次幂标签进入混合范数， 且这些终端项满足典范估计。

###### 剩余项及其标记。

在每次分解时，先把一个槽位分配给其素因子整除它的已提取因子，否则将其保留在剩余列上。完备化的 基本恒等式是 \[\label{old-eq:4.12}
 1_{p\mid nb^3}=1_{p\mid b}+1_{p\nmid b}1_{p\mid n}.\] 更一般地，对于已提取因子的有序列表 \(D_1,\ldots,D_h\)，精确的优先权恒等式是 \[\label{eq:inverse-slot-priority}
 1_{p\mid D_1\cdots D_hn}
 =\sum_{j=1}^h1_{p\mid D_j}\prod_{a<j}1_{p\nmid D_a}
   +1_{p\mid n}\prod_{a\le h}1_{p\nmid D_a}.\] 即使已提取因子共享素因子它也成立。将其应用于每个槽位和平方的每个副本，对每个素因子元组给出 一个不相交的划分；一个槽位的两个副本具有独立的素因子选择。在一次单因子分配中至多有 \(2^{|I|}\) 种选择，对所示有序列表至多有 \((h+1)^{|I|}\) 种。被分配的槽位在已提取因子上具有 除子有界的系数。由于原始系数是 \(\prod_i a_i(p_i)\)，移除被分配的槽位恰好留下一个具有其原始 乘积系数的子集。一个将继续作为平均变量的理想并不仅因为某个槽位被分配给它就被固定。

若 \(V<d\) 且 \(\ell_1\ge d\)，在方程 [\[eq:marked-completion-inversion\]](#eq:marked-completion-inversion) 的右侧重新 展开完备化。若其立方理想为 \(h'\)，则先通过在联合 Hilbert 空间中的三角不等式，在平方之前隔离 其中心为 \(\ell_2\ge0\) 的二分元和 \(h\)-二分元。置 \(b=hh'\) 并定义固定中心 \[\ell=\ell_1+\ell_2,\qquad r=N-3\ell.\] 所得平方中的两个副本 \(b_1,b_2\) 具有相同的名义中心 \(\ell\)；它们的实际范数不必一致。标记是 \(\mathfrak d(nb^3)\)，与 \(b\) 的除数 \(h\) 的选择无关。乘性给出因子 \(\chi_b(k)^3\)； \(\Psi_k(b)^3\) 中的四次幂恰好是掩码 \(1_{(b,f)=1}\)。对 \(b\) 的除数 \(h\) 的剩余和绝对值 至多是一个除数函数。在二分分解并分离 \(q_nq_b^3/Z^N\) 之后，每个平方后的块被一个小幂次乘以 \[\tag{A}\label{eq:canonical-block}
 \begin{split}
 &Z^{-r-2\ell-V}\sum_f w(f)\sum_{k\in\mathcal O}\Phi(q_k/Z^M)
 \Biggl|\sum_{q_b\asymp Z^\ell}\beta(b,f)\chi_b(k)^3\\
 &\hspace{26mm}\times
       \sum_{n\ {\rm sf}}a(n)\chi_n(k)\chi_n(f)^4
       \mathfrak d(nb^3)W(q_n/Z^r)\Biggr|^2 .
 \end{split}\] 所界定。这里 \(\Phi\) 是固定非负的径向 Schwartz 函数，控制原始行球，且 \(|\beta(b,f)|\ll Z^\epsilon\) 与 \(k,n\) 无关。其 \(f\)-依赖性包含原始掩码 \(1_{(b,f)=1}\)；所有其它原始立方掩码都被保留。没有条件 \((b,n)=1\)。前面的指数是正确的， 因为原始归一化为 \(Z^{-N/2}q_b^{1/2}\asymp Z^{-r/2-\ell}\)。若 \(V\ge d\)，使用同一块并取 \(\ell=0,\ b=1,\ r=N\)。于是由中心分类和 \(\ell_2\ge0\)，每个剩余的块都恰好有 \(V+\ell\ge d\)。所添加的行 \(k=0\) 只能在下面所计的主情形中有所贡献。

###### 两次变换的归约。

我们对方程 [\[eq:canonical-block\]](#eq:canonical-block) 中的每个剩余块证明下面的条件估计。设 \(\epsilon_{\rm child}\ge0\)。假设每个形如 [\[eq:canonical-energy\]](#eq:canonical-energy) 的能量 \(\mathcal E'\)，具有引理 [\[lem:canonical-moment\]](#lem:canonical-moment) 的全部系数与支集假设、相同的固定槽位 上限、参数 \[0\le M'\le M-d,\qquad 0\le N',V',\qquad F'=N'+V'\le F+11\eta,\] 以及两个余量都至少为 \(c_{\rm node}-7\eta\)，都满足 \(\mathcal E'\ll Z^{F'+\epsilon_{\rm child}}\)。该假设在本次归纳所用有界范围内是一致成立的， 具有如该引理中那样的有限半范数和固定多项式高度依赖性。对 \(\eta\le d/16\)，剩余的块满足 \[\label{eq:canonical-reduction-contract}
 \text{方程~\eqref{eq:canonical-block} 中的块}
 \ll Z^{F+40\eta+\tau+\pi+\epsilon_{\rm child}},\] 具有同类的统一依赖性。自由选择的局部损失之和为 \(\pi\)；主项和被丢弃的尾部都包含在此估计中。 因此该归约恰好提供了反向归纳所需的蕴含。其证明占据下面的两次变换：第一次产生一个正的逆多项式 范数，第二次构造假设所适用的较小典范能量。

我们接下来说明两种变换中所使用的支集与局部化约定。对实际的理想或非零元素 \(a\)，记 \(\widehat a=\log_Zq_a\)。对于已命名的标量中心，一个带上标的量表示其所示理想的实际对数范数。下面引入的所有理想中心 都是来自固定二进分划的非负中心。已经固定的穿刺点以及下方引入的理想 \(q_0\)，均按其实际对数范数使用， 而不使用独立取整的中心。

两种变换中引入的每一个单独二进区间都有一个固定的紧归一化支集。若 \(a\) 是它的理想而 \(a_{\rm cen}\) 是其已命名的对数中心，则我们使用 \[\label{eq:inverse-ratio-bounds}
 |\log_Zq_a-a_{\rm cen}|\le\eta.\] 这一约定适用于原来的 \(n_i,b_i,f\) 窗口，也适用于每个被提取的理想二进区间在其引入之时。乘积 与商的误差是这些单个误差之和；下方的新的剩余窗口具有明确陈述的界 \(4\eta\)、\(6\eta\) 和 \(4\eta\)。这些估计涉及固定的紧归一化比值区间，而不是比值为 \(Z^\eta\) 的圆环。

为清楚起见，这些区间在整个有限深度上被一致地固定如下。在每一次因式分解处，选取新的单独光滑 截断，使其在商的支集上等于一，并把这些截断的完整支集、Fourier 分离中所用的较大截断的完整支集、 以及放大后的标号窗口的完整支集都包含进来。还要包含下方所用的有界裁剪族。端点的乘积与商 定位初始商支集，例如 \(b=hh'\) 的、剩余 \(n\) 的、以及子列与标号的支集。将此构造迭代 \(D\) 层得到紧归一化比值区间的一个有限集合 \(\mathcal I_D\)。若 \(L_{\rm win}\) 是它们端点的最大绝对 对数，则阈值 \(\log Z\ge L_{\rm win}/\eta\) 蕴含 方程 [\[eq:inverse-ratio-bounds\]](#eq:inverse-ratio-bounds) 以及下方指定的所有新支集界。当一个正和被放大后，其新加入的 列或标号不必再满足某个旧父乘积恒等式。它们在此结点与下一结点处的范数界直接来自 \(\mathcal I_D\) 中 完整独立的新窗口。分离出的范数幂不改变这些支集。

我们使用引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus)中公共同联合 Fourier 演算的如下特殊化。 在某个待从列中分离的耦合光滑因子中出现的每个归一化范数，都是某一环境剖面的坐标 \(y_1,\ldots,y_d\)。 留在权重中的一个导出的外掩码或标号截断仍处于外部，不需要剖面坐标。把当前的 单个二进截断和新的列截断保持在反演之外，直到使用它们的加权 Cauchy 不等式处。将 耦合剖面乘以更大的单个截断 \(\Omega_j\)，后者在这些保留下来的截断的完整支集上等于一。 对所得的紧剖面 \(\mathfrak H\)，在求和任何当前行或标号之前定义 \[\label{eq:inverse-log-fourier}
 \begin{split}
 \widehat{\mathfrak H}(\boldsymbol t)
   &=\int_{\mathbb R^d}\mathfrak H(e^{u_1},\ldots,e^{u_d})
             e^{-i\boldsymbol t\cdot\boldsymbol u}\,d\boldsymbol u,\\
 \mathfrak H(\boldsymbol y)
   &=(2\pi)^{-d}\int_{\mathbb R^d}\widehat{\mathfrak H}(\boldsymbol t)
          \prod_{j=1}^dy_j^{it_j}\,d\boldsymbol t.
 \end{split}\] 范数之间的算术关系限制此恒等式的取值点，而不限制其密度。外模态留在外权重中；对于 两个列坐标，第一个测试接收 \(y_1^{it_1}\)，第二个接收 \(y_2^{-it_2}\)，其共轭提供 \(y_2^{it_2}\)。所有归一化实逆根幂都包含在耦合剖面中，因此最终的列测试不包含第二份拷贝。

这一约定还使一致性定量化。记 \(D_j=y_j\partial_{y_j}\)。在固定的对数矩形上，用 \((1-\Delta)^{m_0}\) 分部积分，对 \(2m_0>J+d\)，给出 \[\label{eq:inverse-fourier-moment}
 \int_{\mathbb R^d}|\widehat{\mathfrak H}(\boldsymbol t)|
        (1+|\boldsymbol t|)^J\,d\boldsymbol t
 \ll_{J,d,\mathrm{box}}\max_{|\boldsymbol a|\le2m_0}
             \|D^{\boldsymbol a}\mathfrak H\|_\infty.\] 对于一个固定的径向 Schwartz Fourier 核 \(K\)，每个 \(\sup_{x\ge0}|(x\partial_x)^jK(x)|\) 都有限，并且 \[D^{\boldsymbol a}K\!\left(A\prod_jy_j^{e_j}\right)
 =\left(\prod_je_j^{a_j}\right)
   (x\partial_x)^{|\boldsymbol a|}K(x)
       \big|_{x=A\prod_jy_j^{e_j}}.\] 因此这些分离半范数对每个标量 \(A>0\) 都是一致的， 而不含 \(Z\) 的导数阶幂。归一化实幂在固定盒上具有 有界的 Euler 导数，而继承的范数挠动只有固定的多项式高度代价。没有把列相关核比值中的 锐截断放进这样的剖面里。 对于 Poisson 步骤中的径向 Fourier 核，这些正是引理 [\[lem:kernel-seminorms\]](#lem:kernel-seminorms)的 归一化核界与方程 [\[eq:normalized-kernel-profile\]](#eq:normalized-kernel-profile)。

我们将使用的粗略尾部估计是，对 \(Y\ge1\) 与 \(A>1\)， \[\label{eq:inverse-raw-tail}
 \sum_{h\ne0:\,a q_h>Y}|K(aq_h)|
 \ll_A(1+a^{-1})Y^{1-A}\qquad(a>0).\] 事实上，壳层 \(2^jY<a q_h\le2^{j+1}Y\) 包含 \(O(1+2^jY/a)\) 个格点，而核在该处为 \(O_A((2^jY)^{-A})\)。对两个几何级数求和即证明该 展示式；同样的论证适用于固定格 \(\lambda^{-4}\mathcal O\)。该证明只用了大自变量 界 \(|K(x)|\ll_Ax^{-A}\)（\(x\ge1\)），因此它也适用于该尾部上的 反射核。下文只用一个实际比值不等式来证明：对一个扇区固定的外行球，其补集对每个 被支持的原始列对都包含在此尾部中。该补集在非互素延拓之前、以及 Fourier 取绝对值之前 被移除。完整光滑核保留在球内，其非光滑掩码 保持在 Fourier 反演之外，直到相关的加权 Cauchy 不等式处。尾部阶数与粗略原始计数在最后固定。

###### 第一次 Poisson 变换。

展开方程 [\[eq:canonical-block\]](#eq:canonical-block) 中的平方。置 \[\mathfrak B=\operatorname{rad}(b_1b_2),\qquad
 n_i=\mathfrak A_i C u_i\quad(i=1,2),\] 其中 \(\mathfrak A_i=(n_i,\mathfrak B)\)，而 \(C\) 是 \(n_1/\mathfrak A_1\) 与 \(n_2/\mathfrak A_2\) 的最大公因数。则 \(\mathfrak A_i\mid\mathfrak B\)，而 \(u_1,u_2\) 是无平方因子的， 彼此互素，且与 \(C\mathfrak B\) 互素。设 \(A_i,B\) 为 \(\mathfrak A_i,C\) 的固定中心，并记 \(\widehat A_i=\log_Zq_{\mathfrak A_i}\)，\(\widehat B=\log_Zq_C\)。 对 \(p\mid\mathfrak B\)，定义 \[a_{ip}=1_{p\mid\mathfrak A_i},\qquad
 \pi_p=v_p(b_1b_2)\bmod2,\qquad
 t_p=a_{1p}-a_{2p}+3\pi_p\bmod6,\] 并置 \(R_1=\prod_{t_p\ne0}p\)。其中心为 \(R\)，且 \(\widehat R=\log_Zq_{R_1}\)。 行特征及其剩余的零掩码恰为 \[\label{eq:first-masked-data}
 \psi_1=\chi_{u_1}\bar\chi_{u_2}
               \prod_{t_p\ne0}\chi_p^{t_p},\qquad
 m_1=u_1u_2R_1,\qquad
 R_{\rm mask}=C\mathfrak B/R_1.\] 事实上，\(u_1,u_2\) 处的指数为 \(1,-1\)；共同的 非 \(\mathfrak B\) 因子 \(C\) 的指数为零但保留其 掩码；而 \(p\mid\mathfrak B\) 处的指数为 \(t_p\)。每个 非零局部幂都是非主的、模 \(p\) 本原的，且具有 互不相交的支集。因此除非 \(m_1=1\)，\(\psi_1\) 是本原的。 每个原始列掩码与两个因子 \(\beta(b_1,f)\overline{\beta(b_2,f)}\) 都保留在表达式中。

以 \(K=Z^M\) 应用引理 [\[lem:masked-poisson\]](#lem:masked-poisson)，并记其 除子为 \(d_k\mid C\mathfrak B/R_1\)，中心为 \(\delta\) 且 \(\widehat\delta=\log_Zq_{d_k}\)。在这个真正的互素表达式上， 实际导子长度为 \[\label{eq:first-poisson-lengths}
 \widehat L_1=\widehat n_1+\widehat n_2-\widehat A_1-\widehat A_2
                    -2\widehat B+\widehat R.\] 实际的核自变量为 \(Z^Mq_h/(q_{d_k}q_{m_1})\)，而 Poisson 前因子的指数为 \(M-\widehat\delta-\widehat L_1/2\)。 我们尚未截断或对该核做 Fourier 分离。

若 \(m_1=1\)，则 \(u_1=u_2=1\) 且对每个 \(p\mid\mathfrak B\) 有 \(t_p=0\)。后一条件迫使 \(\pi_p=0\) 且 \(a_{1p}=a_{2p}\)。因此 \(n_1=n_2\) 且 \(b_1b_2\) 是 一个平方。即使计及全部 \(O(Z^{2\ell+\epsilon})\) 对 \(b_1,b_2\)、 全部 \(O(Z^{r+\epsilon})\) 个相等列、全部 \(O(Z^{V+\epsilon})\) 个标号、以及 \(O(Z^M)\) 行，方程 [\[eq:canonical-block\]](#eq:canonical-block) 中的 归一化也给出 \(O(Z^{M+\epsilon})\)。 若 \(r<0\) 但其固定圆环列窗口非空，则 \(Z^{-r}\) 由其固定上端点界定，因此其理想计数 仍为 \(O(Z^r)\)，常数固定。 标记与保留下来的掩码不会使此界超出一个小幂。 当非零主项在下方被恢复时，它们 将带有与非主项相同的外球掩码；引理 [\[lem:masked-poisson\]](#lem:masked-poisson) 的最后一 部分以同样的代价界定它们。

我们接下来识别其列系数。对于互素的无平方因子主元 \(a,b\)， CRT 与互反律给出 \[\gamma_2(ab)=\gamma_2(a)\gamma_2(b)
       \chi_a(b)^2\chi_b(a)^2
 =\gamma_2(a)\gamma_2(b)\chi_b(a)^4.\] 在第一个 Poisson 根中，涉及 \(u_1\) 的因子（包括 除子与频率）为 \[\gamma_1(u_1)\overline{\chi_{u_1}(h)}
 \chi_{u_1}(d_kR_1)\prod_{t_p\ne0}\chi_{u_1}(p^{t_p}),\] 至多相差一个固定射线因子。这可通过把 \(u_1\) 与 \(p\) 之间的 CRT 因子写成 \(\chi_{u_1}(p)\chi_p(u_1)^{t_p}\) 并利用互反律得到。在 共轭的第二侧，\(t_p\) 被替换为 \(-t_p\)。\(u_1,u_2\) 之间的交叉 因子是互反律因子 \(\mathcal R(u_1,u_2)\)，而不是零延拓符号的商。

置 \(P_T=\prod_{t_p\ne0}p^{t_p}\)，视其在固定射线群中。 方程 [\[eq:signal\]](#eq:signal) 与 方程 [\[eq:G-quadratic-refinement\]](#eq:G-quadratic-refinement) 表明剩余的 双列射线因子是 \[G(u_1u_2^{-1})\mathcal R(u_1u_2^{-1},P_T).\] 例如，在把因子放入共轭的第二 多项式之前，原始的第二个 Gauss-信号因子为 \(\mu(u_2)\chi_{u_2}(-1)\overline{G(u_2)}\)。其相应的 写在该多项式内的因子为 \(\mu(u_2)\chi_{u_2}(-1)G(u_2)\)。又有 \(G(u_2^{-1})=\chi_{u_2}(-1)\overline{G(u_2)}\)。 这些恒等式给出所展示的商。固定 \(P_T\) 的射线类，并在有限射线群上对所示函数做 Fourier 展开。其每一侧的因子都是真正的乘法射线 特征，记作 \(\nu_i\)。它们的个数与系数的范数 只依赖于固定射线群。

定义 \[E=\prod_{\pi_p=1}p^{a_{1p}+a_{2p}},\qquad
 \widetilde h=hf^2E.\] \(f\) 处的原始四次幂等于 \(\overline{\chi_{u_i}(f^2)}\)，包含零点。把位置 先分配给 \(b_i,\mathfrak A_i,C\)。在 \(p\mid\mathfrak B\) 处、侧 \(i\) 上剩余的局部因子具有指数 \[4a_{ip}+1_{t_p\ne0}(1\mathbin{\pm}t_p)
          +\pi_p(a_{1p}+a_{2p})\pmod6.\] 正号属于第一侧。直接化简在两侧给出相同的 答案： \[\begin{array}{c|cc|c|c}
 \pi_p&a_{1p}&a_{2p}&t_p&\text{两侧的指数}\\ \hline
 0&0&0&0&0\\
 0&1&0&1&0\\
 0&0&1&5&0\\
 0&1&1&0&4\\
 1&0&0&3&4\\
 1&1&0&4&4\\
 1&0&1&2&4\\
 1&1&1&3&4
 \end{array}\] 定义 \(\xi(n)\) 为对 \(p\mid\mathfrak B\) 取 \(\chi_n(p)\) 的乘积，其指数取最后一列中相应的指数。 指数零仍表示 \(p\) 处的穿刺点。该计算 证明 \(\xi\) 对两侧是公共的，且不依赖于 \(h,f,C\)。 在这些分配之后，侧 \(i\) 上的非主系数为 \[\tag{C}\label{eq:first-poisson-column}
 \mu(u_i)\nu_i(u_i)\rho(u_i)
 \overline{\chi_{u_i}(\widetilde h)}
 \chi_{u_i}(C)^4\chi_{u_i}(d_k)\xi(u_i)\mathfrak d_i(u_i).\] 它还表明，涉及变动 \(b_i,\mathfrak A_i\) 的每个特征都属于 \(\xi\) 或 \(\widetilde h\) 中的某一个； 它们的其他因子是外系数。

第一次变换产生了方程 [\[eq:first-poisson-column\]](#eq:first-poisson-column) 中的 逆型列系数。我们接下来在形成第二次变换的 正行范数之前，把其四次幂因子收集进一个无平方因子标号。

###### 从立方中保留四次幂标号。

唯一地写 \(b_1b_2=q^2s\)，其中 \(s\) 无平方因子，并定义 \[J_2=\prod_{\substack{\pi_p=0\\a_{1p}=a_{2p}=1}}p,\qquad
 J=sJ_2,\qquad q=J_2q_0.\] \(J_2\) 的每个素数在 \(b_1b_2\) 中都具有正的偶赋值， 故 \(J_2\mid q\)。理想 \(s,J_2\) 互素且无平方因子； 因此 \(J\) 无平方因子。设 \(j\ge0\) 为 \(J\) 的中心，并置 \[\widehat s=\log_Zq_s,\quad \widehat j_2=\log_Zq_{J_2},\quad
 \widehat j=\log_Zq_J=\widehat s+\widehat j_2,\quad
 \widehat\ell_{\rm pair}=(\widehat b_1+\widehat b_2)/2.\] 理想恒等式 \(b_1b_2=q_0^2J_2^2s\) 恰好给出 \[\label{eq:inverse-cube-actual}
 \widehat c:=\log_Zq_{q_0}
   =\widehat\ell_{\rm pair}-\widehat s/2-\widehat j_2\ge0,
 \qquad
 4\widehat\ell_{\rm pair}-2\widehat s+\widehat j_2
   =4\widehat c+5\widehat j_2\ge0.\] 上面的表现在证明精确的零延拓恒等式 \[\label{eq:retained-cube-label}
 \xi(n)=\chi_n(J)^4\,1_{(n,\operatorname{rad}q_0)=1}.\] 事实上，指数为四的素数恰是 \(sJ_2\) 的那些； \(\mathfrak B\) 的每一个其他素数都整除 \(q_0\)。同时属于 \(J\) 与 \(q_0\) 的素数只是重复了已由 \(\chi_n(J)^4\) 提供的零。我们将固定 \(q_0\)，但把 \(J\) 留到稍后的 平均中。模 \(q_0\) 贡献一个穿刺点，且不 属于固定射线群。 对固定的 \(J,q_0\)，\(s,J_2\) 的选取、因式分解 \(b_1b_2=q_0^2J_2^2s\)、以及理想 \(\mathfrak A_i\) 都只有 除子重数。

我们现在局部化真正的第一次 Poisson 表达式，在其延拓 互素支集或取绝对 Fourier 积分之前。局部表给出 精确的实际范数恒等式 \[\widehat R-\widehat A_1-\widehat A_2+\widehat E
       =\widehat s-2\widehat j_2.\] 对 \(y=hf^2E\)，蕴含 \(Z^Mq_h/(q_{d_k}q_{m_1})\le Z^\tau\) 与 方程 [\[eq:first-poisson-lengths\]](#eq:first-poisson-lengths) 给出 \[\begin{split}
 \widehat y
 &\le \widehat n_1+\widehat n_2-2\widehat B-M
       +\widehat s-2\widehat j_2+\widehat\delta+2\widehat f+\tau\\
 &\le \widehat n_1+\widehat n_2-2\widehat B-M
       +4\widehat\ell_{\rm pair}-\widehat j
       +\widehat\delta+2\widehat f+\tau.
 \end{split}\] 第二个不等式是方程 [\[eq:inverse-cube-actual\]](#eq:inverse-cube-actual)。 按如下定义形式中心与包住它的外行尺度 \[\label{eq:enlarged-first-frequency}
 H_c=2r-2B-M+4\ell+2V+\delta-j,\qquad
 H_{\rm use}=H_c+12\eta+\tau.\] 相对于 \(H_c\)，最后一个实际上界具有误差 \[(\widehat n_1-r)+(\widehat n_2-r)-2(\widehat B-B)
 +2(\widehat b_1-\ell)+2(\widehat b_2-\ell)
 -(\widehat j-j)+(\widehat\delta-\delta)+2(\widehat f-V),\] 其在方程 [\[eq:inverse-ratio-bounds\]](#eq:inverse-ratio-bounds) 下的正最大值为 \(12\eta\)。因此实际比值不等式对每个被支持的原始列对 蕴含 \(q_y\le Z^{H_{\rm use}}\)。

在该原始表达式上只插入外掩码 \[\mathcal B_1(h)=1_{0<q_{hf^2E}\le Z^{H_{\rm use}}}.\] 对每个被支持的对，其补集包含在实际核 尾部 \(Z^Mq_h/(q_{d_k}q_{m_1})>Z^\tau\) 中；应用 方程 [\[eq:inverse-raw-tail\]](#eq:inverse-raw-tail) 舍弃该补集，其中 原始计数与阶数在下方固定。不插入比值不等式的 示性函数。在 \(\mathcal B_1=1\) 内保留完整光滑核， 包括比值大于 \(Z^\tau\) 的那些对。该掩码依赖于 \(h,f,E\) 与固定扇区，但在所指出的提取之后， 不依赖于 \(u_1,u_2\)。若 \(H_{\rm use}<0\)，其非零球为空， 同样的尾部比较舍弃每个非零频率。任何为了统一公式而 现在被恢复的主非零项都带有这同一个掩码。 它们的绝对贡献由已经估计过的完整主项恢复所界定。

通过 \[1_{(u_1,u_2)=1}=\sum_{t'\mid(u_1,u_2)}\mu(t'),\qquad u_i=t'x_i,
 \qquad \widehat t=\log_Zq_{t'}.\] 移除条件 \((u_1,u_2)=1\)。 设 \(t\) 为其固定的非负中心。 此反演是在交叉相位已被替换为 上述固定射线函数之后进行的。这些函数、不变的外 掩码 \(\mathcal B_1\)、所有剩余的 零延拓局部因子、以及光滑核中的形式乘积 \(q_{u_1}q_{u_2}q_{R_1}\) 也为非互素的 \(u_1,u_2\) 定义了一个表达式。 它在互素支集上与 Poisson 求和一致；所展示的除子恒等式随后恰好恢复 该支集。对新引入的非互素对，不宣称任何本原 Poisson 公式。 无平方因子性保留了穿刺点 \((x_i,t')=1\)。在 \(t'\) 处分配的位置是外 系数，而其他位置构成 \(x_i\) 上的标记。

插入 \(q_h\) 的二进区间，来自一个对所有 \(f,E\) 公共的固定分划， 而不是为那些标号重新取心的分划。掩码 \(\mathcal B_1\) 蕴含 \(q_h\le q_{hf^2E}\le Z^{H_{\rm use}}\)，因此在有界保留尺度范围内只有 对数多个这样的二进区间。 把 \(\mathcal B_1\) 保持在每次 Fourier 反演之外。定义 \[s_i=r-A_i-B-t,\qquad
 \kappa_i=M-2r-2\ell-V-\delta+A_i+B-R/2.\] 在因式分解表达式上的恒等式 \(n_i=\mathfrak A_iCt'x_i\) 给出 \(|\widehat x_i-s_i|\le4\eta\)。完整的新的 \(x_i\)-支集 包含在 \(\mathcal I_D\) 中，因此同一界在分离之后直接 在该支集上成立，而不只在原来的乘积支集上成立。 当前前因子中所用的重构形式乘积也 包含在那里。

###### 分离第一次变换后的乘积。

我们在应用 Cauchy 之前记录实际前因子。它恰好 按两个列侧分裂为 \[Z^{-r-2\ell-V}Z^{M-\widehat\delta-\widehat L_1/2}
       =Z^{\widehat\kappa_1/2}Z^{\widehat\kappa_2/2},
 \quad
 \widehat\kappa_i=M-r-2\ell-V-\widehat\delta-\widehat n_i
                  +\widehat A_i+\widehat B-\widehat R/2.\] 方程 [\[eq:inverse-ratio-bounds\]](#eq:inverse-ratio-bounds) 在每一侧给出 \[\label{eq:inverse-first-prefactor-error}
 \widehat\kappa_i\le\kappa_i+\tfrac92\eta.\] 五个误差权重是 \(1,1,1,1,1/2\)。我们现在用一个联合剖面中的所有实逆根来实现此 归一化。 固定第一个二进、射线与位置模式 \(\sigma\)，并设 \(h_1\) 为其裸-\(h\) 二进区间的中心。使用九个独立的 归一化坐标 \[\boldsymbol y=(y_{A_1},y_{A_2},y_C,y_d,y_R,y_t,y_h,y_{x_1},y_{x_2})
 =\left(\frac{q_{\mathfrak A_1}}{Z^{A_1}},
 \frac{q_{\mathfrak A_2}}{Z^{A_2}},\frac{q_C}{Z^B},
 \frac{q_{d_k}}{Z^\delta},\frac{q_{R_1}}{Z^R},\frac{q_{t'}}{Z^t},
 \frac{q_h}{Z^{h_1}},\frac{q_{x_1}}{Z^{s_1}},\frac{q_{x_2}}{Z^{s_2}}\right).\] 在形式 \(u_a=t'x_a\) 表达式上的精确完整根与核自变量为 \[\label{eq:inverse-first-root-kernel}
 \begin{split}
 \frac{Z^{-r-2\ell-V}Z^M}
 {q_{d_k}\sqrt{q_{R_1}}q_{t'}\sqrt{q_{x_1}q_{x_2}}}
 &=Z^{(\kappa_1+\kappa_2)/2}
 y_d^{-1}y_R^{-1/2}y_t^{-1}(y_{x_1}y_{x_2})^{-1/2},\\
 \frac{Z^Mq_h}{q_{d_k}q_{R_1}q_{t'}^2q_{x_1}q_{x_2}}
 &=A_{{\rm ker},1}\frac{y_h}{y_dy_Ry_t^2y_{x_1}y_{x_2}},\\
 A_{{\rm ker},1}&=Z^{M+h_1-\delta-R-2t-s_1-s_2}.
 \end{split}\] 选取新的截断 \(\omega_{x,a}\)，使其在旧的 \(W\)-支集除以单个 \(\mathfrak A_a,C,t'\) 支集上等于一，并 将它们保留在列中。把每个当前外 二进截断保留在反演之外。设 \(\Omega_{1,\alpha}\) 为更大的 截断，在这些保留下来的截断的完整支集上等于一。 以 \(\mathcal K_1=\mathcal F\Phi\)，定义单个紧剖面 \[\label{eq:inverse-first-profile}
 \begin{split}
 \mathfrak H_{1,\sigma}(\boldsymbol y)={}&Z^{-9\eta/2}
 \prod_\alpha\Omega_{1,\alpha}(y_\alpha)
 y_d^{-1}y_R^{-1/2}y_t^{-1}(y_{x_1}y_{x_2})^{-1/2}\\
 &\times W(y_{A_1}y_Cy_ty_{x_1})
       \overline{W(y_{A_2}y_Cy_ty_{x_2})}
 \mathcal K_1\!\left(A_{{\rm ker},1}
       \frac{y_h}{y_dy_Ry_t^2y_{x_1}y_{x_2}}\right).
 \end{split}\] 此剖面外的标量恰为 \(\prod_{a=1}^2Z^{(\kappa_a+9\eta/2)/2}\)。 特别地，剖面包含每个实根一次，即便 实际列范数不同时也是如此。其变换由 方程 [\[eq:inverse-log-fourier\]](#eq:inverse-log-fourier) 在环境九维 盒上定义，早于任何实际 \(f,h\) 或外理想被求和。 \(b_a,f,J,E,q_0\) 的范数在方程 [\[eq:first-poisson-column\]](#eq:first-poisson-column) 之后只出现在外系数、特征、掩码 或单个截断中；它们不需要额外的耦合剖面坐标。

为在 \(t'\) 处揭示算术提取，置 \(y=hf^2E\) 并 \[B_{1,a}(t';y)=\mu(t')\nu_a(t')\rho(t')\overline{\chi_{t'}(y)}
       \chi_{t'}(CJ)^4\chi_{t'}(d_k)1_{(t',\operatorname{rad}q_0)=1}.\] 设 \(\varepsilon_1=1\) 且 \(\varepsilon_2=-1\)。对于一个固定的第一 Fourier 模态 \(\boldsymbol t\)，剩余的多项式恰为 \[\label{eq:inverse-first-polynomial}
 \begin{split}
 P_a(y)={}&\sum_{x\ {\rm sf}}\mu(x)\nu_a(x)\rho(x)
       \overline{\chi_x(y)}\chi_x(CJ)^4\chi_x(d_k)
       1_{(x,\operatorname{rad}q_0t')=1}\\
 &\qquad\times\mathfrak d_{I_a}(x)\omega_{x,a}(q_x/Z^{s_a})
                  (q_x/Z^{s_a})^{\varepsilon_a it_{x_a}}.
 \end{split}\] 乘法性用在无平方因子互素因子上，然后通过 所展示的零延拓使用；没有特征在零点处被除。 互 gcd 反演带来的那一个额外 \(\mu(t')\) 是外的。 以有序列表 \((b_a,\mathfrak A_a,C,t';x)\) 应用方程 [\[eq:inverse-slot-priority\]](#eq:inverse-slot-priority)。整除 \(x\) 的一个存留素数 已经与 \(b_a,\mathfrak A_a,C,t'\) 互素：\(\mathfrak B\) 的每个素数 都在 \(J\operatorname{rad}q_0\) 中，而所展示的 四次幂与穿刺点提供这些零点。因此 \(\mathfrak d_{I_a}\) 具有原来的单个系数与 列表，而分配得到的素数恒等式与优先掩码留在外部。

以下是第一次分离分量的完整结构。设 \(\Omega_\sigma\) 由 \(b_1,b_2,\mathfrak A_1,\mathfrak A_2,C,d_k,t',f,h\) 以及分配得到的 位置素数组成，受其重构关系与单个 支集约束。特别地 \(\mathfrak A_a\mid\mathfrak B\)、\((C,\mathfrak B)=1\)，且 \(d_k\mid C\mathfrak B/R_1\)，而 \(R_1,E,J,q_0\) 是导出的， 不是自由指标。 设 \(\mathcal A_{1,\sigma}\) 为分配得到的原始 系数与优先掩码的乘积，在第二侧取共轭，并设 \(\psi_{1,\sigma}^{\rm out}\) 为所有保留下来的外 二进截断的乘积。设 \(e_\sigma\) 为在前面 旧重数 \(w(f)\) 的无商 CRT 提取中得到的乘积，即两个原始 \(\beta\) 因子、其包含 \((b_a,f)=1\) 的立方掩码、 提取出的零掩码、以及在旧外理想处的 有限 Gauss、单位、互反律与第一射线因子，排除所展示的 \(\mu(d_k)\) 与 \(B_{1,a}\)。 它不依赖于 \(x_1,x_2\)；其定义由该乘积给出， 而不是由除以方程 [\[eq:inverse-first-polynomial\]](#eq:inverse-first-polynomial) 给出。 记 \(\mathcal O_1=\{A_1,A_2,C,d,R,t,h\}\)，置 \[w_{1,\sigma}(\omega;\boldsymbol t)
 =e_\sigma(\omega)\mu(d_k)\mu(t')B_{1,1}(t';y)
       \overline{B_{1,2}(t';y)}\mathcal B_1(h)
       \mathcal A_{1,\sigma}(\omega)\psi_{1,\sigma}^{\rm out}(\omega)
       \prod_{\alpha\in\mathcal O_1}y_\alpha^{it_\alpha}.\] 对于带掩码、恢复主项的形式第一分量，Fourier 反演给出精确恒等式 \[\label{eq:inverse-first-separated}
 \begin{split}
 \mathcal T_{1,\sigma}=(2\pi)^{-9}\int_{\mathbb R^9}
 &\widehat{\mathfrak H}_{1,\sigma}(\boldsymbol t)
 \sum_{\omega\in\Omega_\sigma}w_{1,\sigma}(\omega;\boldsymbol t)\\
 &\times Z^{(\kappa_1+9\eta/2)/2}P_1(y)
       \overline{Z^{(\kappa_2+9\eta/2)/2}P_2(y)}\,d\boldsymbol t.
 \end{split}\] 展开这两个多项式恢复两个列模态；七个 外模态恢复方程 [\[eq:inverse-first-profile\]](#eq:inverse-first-profile) 的其他坐标。 其较大的截断在保留支集上等于一，而新的截断在 旧窗口非零处等于一。这逐项验证了该恒等式。 原始 \(\beta\) 因子与每个外掩码仍在该 完整和中。

###### 第一个正优函数。

对任何有限或绝对收敛的加权和，我们使用 \[\tag{D}\label{eq:weighted-cauchy}
 \left|\sum_\omega w_\omega U_1(\omega)\overline{U_2(\omega)}\right|
 \le\prod_{i=1}^2
       \left(\sum_\omega|w_\omega||U_i(\omega)|^2\right)^{1/2}.\] 首先在整个 \(\Omega_\sigma\) 上对每个固定模态以 \(U_i=Z^{(\kappa_i+9\eta/2)/2}P_i\) 应用此式。只有现在才绝对地界定外因子。其纯算术量至多是一个单独分配的 \(Z^{\pi_\beta}\) 乘以旧重数 与绝对位置乘积；保留支集给出 \(\mathcal B_1(h)1_{(C,J)=1}\)。特别地，尚未假定 \(\beta(b,f)\) 的任何因式分解。

对每个固定旧外重构与非零 \(y=\widetilde h\)， 关系 \(y=hf^2E\) 蕴含 \(f^2E\mid(y)\)。若其重数 至多 \(C_0d_{\mathcal O}(f)^{C_0}\)，则 \[\label{eq:inverse-old-label-fibre}
 \sum_{f^2E\mid(y)}w(f)
 \le C_0d_{\mathcal O}((y))^{C_0+1}
 \le C_{\pi_{\rm old}}Z^{\pi_{\rm old}}
 \qquad(0<q_y\le Z^{H_{\rm use}}).\] 最后这个界是一致的，因为 \(H_{\rm use}\) 保持在有界 范围内；\(h=y/(f^2E)\) 于是作为元素被唯一确定。 这是一个旧标号纤维界，而不是依赖于 后来新标号的重数。 多项式 \(P_i(y)\) 不再依赖于 \(f\) 或 单个 \(b_i,\mathfrak A_i\)，只依赖于 \(J,q_0\)、固定 二进长度 \(A_i\) 以及固定射线扇区：这正是 方程 [\[eq:first-poisson-column\]](#eq:first-poisson-column) 与 [\[eq:retained-cube-label\]](#eq:retained-cube-label)，其中范数剖面已分离。 在第一次加权 Cauchy 不等式之后，\(\mathcal B_1\) 就是 \(1_{0<q_y\le Z^{H_{\rm use}}}\)。在此正和阶段，且只有现在，用固定的非负径向 Schwartz 函数 \(\Phi_+(q_y/Z^{H_{\rm use}})\) 优控它，后者对至多为一的自变量 至少为一。非空球有 \(H_{\rm use}\ge0\)，因此第二个 Poisson 尺度恰为 \(Z^{H_{\rm use}}\ge1\)。该优函数不是作为 等式替换到原来的带符号表达式中。更精确地说，设 \(\mathfrak O_\sigma\) 由 \[o=(b_1,b_2,\mathfrak A_1,\mathfrak A_2,C,d_k,t';
       \text{旧分配位置素数}),\] 组成，保留其完整的单个支集、不依赖于 \(f,h,x\) 的源重构 关系、分配得到的优先掩码以及 \((C,J)=1\)。设 \(w_o^+\) 为其分配素数的绝对原始 系数的乘积，并在此集合外取零。它是 非负的且不依赖于 \(y\)。每个第一正侧至多 为 \(C Z^{\pi_\beta+\pi_{\rm old}}\)，乘以其标量 \(Z^{\kappa_i+9\eta/2}\)，再乘以显式正优函数 \[\label{eq:inverse-first-majorant}
 \mathcal S_{i,\sigma,\boldsymbol t}
 =\sum_{o\in\mathfrak O_\sigma}w_o^+
    \sum_{y\in\mathcal O}\Phi_+(q_y/Z^{H_{\rm use}})|P_i(y)|^2.\] 在此正步骤，旧的 \(h\) 截断与模态、以及依赖于 \(y\) 的 \(B_{1,a}\) 的零点，可通过其上界移除。 因此第一次加权 Cauchy 不等式与旧标号纤维界 已从此正优函数以及每个 后续外集合中移除了旧的 \(f,h\)；它们原来的 \(-V\) 归一化仍留在 \(\kappa_i\) 中。在接下来的计数之后，我们对它的 \(y\)-和 应用第二次 Poisson 变换。

设 \(\widehat r_{\rm diff}\ge0\) 为具有偶奇偶性且 \(a_{1p}\ne a_{2p}\) 的素数的 实际对数范数。表中给出 \(\widehat R=\widehat s+\widehat r_{\rm diff}\)，因此 \[\label{eq:fixed-cube-count}
 \widehat c=\widehat\ell_{\rm pair}+\widehat R/2-\widehat j
                  -\widehat r_{\rm diff}/2
 \le\ell+R/2-j+\tfrac52\eta.\] 以此实际上界进行的理想计数在保留 \(J\) 的同时计数固定的 \(q_0\)。 对于一个同时也计数 \(J\) 的对角界， 其完整窗口的指数至多为 \(j+\eta\)，给出合并的 上界计数 \(Z^{\ell+R/2+7\eta/2+\epsilon}\)。\(\mathfrak A_i\) 的 选取以及 \(d_k\mid C\mathfrak B/R_1\) 的选取在 \(b_1,b_2,C\) 给定后只 增加除子因子。

结合方程 [\[eq:inverse-first-separated\]](#eq:inverse-first-separated)、加权 Cauchy 不等式 与旧标签纤维界，得到第一次 变换的显式输出： \[\label{eq:inverse-first-transform-output}
 \begin{split}
 |\mathcal T_{1,\sigma}|\ll{}&Z^{\pi_\beta+\pi_{\rm old}}
 \int_{\mathbb R^9}|\widehat{\mathfrak H}_{1,\sigma}(\boldsymbol t)|\\
 &\quad\times\prod_{i=1}^2
 \left(Z^{\kappa_i+9\eta/2}\mathcal S_{i,\sigma,\boldsymbol t}\right)^{1/2}
 \,d\boldsymbol t.
 \end{split}\] 每个 \(\mathcal S_{i,\sigma,\boldsymbol t}\) 是方程 [\[eq:inverse-first-majorant\]](#eq:inverse-first-majorant) 中的正和：其行多项式带有 方程 [\[eq:inverse-first-polynomial\]](#eq:inverse-first-polynomial) 中的 Möbius 系数，由立方体导出的标签 \(J\) 被保留，而旧的 \(f,h\) 不再 出现在平均指标之中。以下变换应用于 这些正的行范数。

###### 第二次 Poisson 变换。

固定由第一个 Cauchy 不等式得到的两个正和之一。其多项式具有形式 \[P_i(y)=\sum_x c_i(x)\overline{\chi_x(y)}.\] 系数 \(c_i(x)\) 由方程 [\[eq:first-poisson-column\]](#eq:first-poisson-column) 的其余因子组成， 其中 \(u_i=t'x\)、在 \(t'\) 处的刺点以及分离出的权重。它与 \(y\) 无关。特别地 \(x\) 无平方因子且 \[c_i(x)=0\quad\text{unless}\quad
 (x,CJ)=1,\quad (x,\operatorname{rad}q_0t')=1.\] 刺点 \(\rho\) 以及 \(\chi_x(d_k)\) 的零点也 被保留。\(y\)-和使用了尺度为 \(Z^{H_{\rm use}}\) 的 固定形状光滑正球。

在其展开的平方中令 \[g'=(x_1,x_2),\qquad x_j=g'z_j,\qquad
 \widehat g=\log_Zq_{g'}.\] 设 \(g\ge0\) 为其固定中心。 则 \(z_1,z_2\) 无平方因子且互素，且各自与 \(g'\) 互素。引理 [\[lem:masked-poisson\]](#lem:masked-poisson) 的行数据为 \[\label{eq:second-masked-data}
 K=Z^{H_{\rm use}},\qquad
 \psi_2=\bar\chi_{z_1}\chi_{z_2},\qquad
 m_2=z_1z_2,\qquad R_{\rm mask}=g'.\] 公因子 \(\bar\chi_{g'}(y)\chi_{g'}(y)\) 正是这个 掩码。该特征在 \(m_2=1\) 之外是本原的，因为其 两个非零局部幂具有不相交的支集。对 \(d_2\mid g'\)， 设 \(\theta\ge0\) 为其中心并记 \(\widehat\theta=\log_Zq_{d_2}\)。实际的导子长度为 \[\widehat L_2=\widehat x_1+\widehat x_2-2\widehat g,
 \qquad |\widehat L_2-2(s_i-g)|\le10\eta.\] 最后一个不等式使用了每个副本的完整新 \(x\)-支集界 \(|\widehat x_a-s_i|\le4\eta\) 以及 \(|\widehat g-g|\le\eta\)。对 \(k_{\rm new}=d_kd_2k''\)，蕴含式 \(Z^{H_{\rm use}}q_{k''}/(q_{d_2}q_{m_2})\le Z^\tau\) 给出 \[\begin{split}
 \widehat{k_{\rm new}}
 &\le2(s_i-g)-H_{\rm use}+\delta+2\theta+13\eta+\tau\\
 &=M_c+\eta,
 \end{split}\] 其中 \[\label{eq:second-poisson-lengths}
 \begin{split}
 M_c&=2(s_i-g)-H_c+\delta+2\theta\\
    &=M-4\ell-2A_i-2t-2g+2\theta-2V+j,\qquad
 M_{\rm ch}=M_c+\eta.
 \end{split}\] \(13\eta\) 由来自导子的 \(10\eta\)、来自 \(d_k\) 的一个以及来自 \(d_2\) 的两个组成。减去 \(H_{\rm use}=H_c+12\eta+\tau\) 抵消了在这第二次 Poisson 比较中 所用的同一容差 \(\tau\)。因此不需要单独的行裁剪 或未记录的边界误差。

将原来的主贡献分离出来，用于下面的直接计数。 在任何非互素扩展或 Fourier 绝对化之前，仅在 真正的非主第二次 Poisson 表达式上保留外掩码 \[\mathcal B_2(k'')=1_{0<q_{d_kd_2k''}\le Z^{M_{\rm ch}}}.\] 对每个被支集的配对，其余集包含在刚刚考虑的实际比值 尾部中，因此方程 [\[eq:inverse-raw-tail\]](#eq:inverse-raw-tail) 以 下面固定的阶将其丢弃。在掩码内部保留完整的光滑核。 掩码依赖于 \(d_k,d_2,k''\) 及固定扇区，而不依赖于剩余的 \(z_1,z_2\)。若 \(M_{\rm ch}<0\)，非零球为空，同样的 尾部比较丢弃每一个非零频率。在保留的非空 通道中 \(M_{\rm ch}\ge0\)。

实际的第二个前因子具有精确的侧分解 \[Z^{H_{\rm use}-\widehat\theta-\widehat L_2/2}
       =Z^{\widehat\lambda_1/2}Z^{\widehat\lambda_2/2},
 \qquad \widehat\lambda_a=H_{\rm use}-\widehat\theta-\widehat x_a+
                           \widehat g.\] 对 \(\lambda_c=H_c-\theta-(s_i-g)\)，同样的支集界给出 \[\label{eq:inverse-second-prefactor-error}
 \widehat\lambda_a\le\lambda_c+18\eta+\tau.\] 这里 \(18=12+1+4+1\)。如同第一次分解，所有正规化的实 逆根将保留在联合光滑剖面中直至 Fourier 反演；它们也不会被追加到最终的子测试中。 所有原系数掩码都保留。特别地 \[(g',CJ)=1,\qquad (z_j,g'CJ)=1\] 在其非零支集上成立。

主情形为 \(z_1=z_2=1\)，等价地 \(x_1=x_2\)。 其计数的名义恒等式为 \[\label{eq:second-principal-exponent}
 \kappa_i+H_c+s_i+B+t+\ell+R/2=F-B-j,
 \qquad F=N+V=r+3\ell+V.\] 实际上界计数加上来自第一个前因子的 \(9\eta/2\)、 来自行尺度 \(H_{\rm use}\) 的 \(12\eta+\tau\)、来自 对角 \(x\)-窗口的 \(4\eta\)、来自 \(C,t'\) 的各 \(\eta\)，以及来自 合并 \(q_0,J\) 计数的 \(7\eta/2\)。它们的和为 \(26\eta+\tau\)。以 聚合局部损失 \(\pi\) 计，该主贡献因此 至多为 \(Z^{F-B-j+26\eta+\tau+\pi}\le Z^{F+26\eta+\tau+\pi}\)。 任何被恢复到形式表达式中的非零主频率都带有 相同的 \(\mathcal B_2\) 掩码；其绝对和由引理 [\[lem:masked-poisson\]](#lem:masked-poisson) 中的完整主恢复所界定，因为 \(Z^{H_{\rm use}}\ge1\)。

对于非主项，我们现在识别新的系数 类。对无平方因子的 \(z\)，本原 Gauss 和的复共轭与方程 [\[eq:signal\]](#eq:signal) 给出 \[\gamma_{-1}(z)=\chi_z(-1)\overline{\gamma_1(z)},\qquad
 \mu(z)\gamma_{-1}(z)
 =\bar\alpha(z)\gamma_2(z)\chi_z(-1)\overline{G(z)}.\] 原始的第二个因子为 \(\mu(z)\gamma_1(z)=\overline{\bar\alpha(z)\gamma_2(z)}G(z)\)； 写在共轭的第二个 多项式内的对应因子具有射线因子 \(\overline{G(z)}\)。两个本原 根的 CRT 交叉因子为 \(\mathcal R(z_1,z_2)\)。因此它们合并的射线因子为 \[\mathfrak G(a,b)=\chi_a(-1)\overline{G(a)}G(b)\mathcal R(a,b)
       =G(ba^{-1}).\] 最后一个等式来自 方程 [\[eq:G-quadratic-refinement\]](#eq:G-quadratic-refinement) 以及 \(\mathcal R(a,a)=\chi_a(-1)\)，先在素数上由 方程 [\[eq:fixed-gauss-phases\]](#eq:fixed-gauss-phases) 得到，然后乘性地推广。 此式中的所有商都在固定有限射线群中。 特别地， \[\mathfrak G(v'n_1,v'n_2)=\mathfrak G(n_1,n_2).\] 公乘性特征 \(\nu_i(v')\) 也在 两边之间抵消。

从对所有 \(d_k,d_2\) 公共的一个划分插入 \(q_{k''}\) 的二分块。 掩码 \(\mathcal B_2\) 蕴含 \(q_{k''}\le Z^{M_{\rm ch}}\)，因此在 有界保留区间内其 数目是对数的。设 \(h_2\) 为 这样一个裸频率二分块的中心。我们现在记录要分离的精确 分量。固定第一个模式与选定的侧 \(i\)， 记 \[H_o=CJ,\qquad r_0=\operatorname{rad}q_0t',\qquad d_0=d_k,
 \qquad a_0(z)=\bar\alpha(z)\gamma_2(z),\qquad
 \mathcal K_2=\mathcal F\Phi_+,\] 并保留来自 方程 [\[eq:second-masked-data\]](#eq:second-masked-data) 的 \(K=Z^{H_{\rm use}}\)。对无平方因子的自变量令 \[\label{eq:inverse-second-outer-coefficients}
 \begin{split}
 B_o(g')&=\mu(g')\nu_i(g')\rho(g')1_{(g',r_0)=1}
              \chi_{g'}(H_o)^4\chi_{g'}(d_0),\\
 L_{o,d_2,k''}(z)&=a_0(z)\nu_i(z)\rho(z)1_{(z,r_0)=1}
       \chi_z(H_o)^4\chi_z(d_0)\overline{\chi_z(d_2)}\chi_z(k'').
 \end{split}\] \(P_i\) 中旧的分离测试记为 \(W_i\)，因此 \(W_i(x)=\omega_{x,i}(x)x^{\varepsilon_iit_{x_i}}\)。 设 \(\psi_g,\psi_{d_2},\psi_{k''}\) 表示在固定 \(g',d_2,k''\) 二分块上 保留的各个截断，取其正规化 范数处的值。对于这个初步模式 \(\sigma_0\)，方程 [\[eq:inverse-first-majorant\]](#eq:inverse-first-majorant) 中带掩码的 主恢复非零分量恰好为 \[\label{eq:inverse-second-formal-component}
 \begin{split}
 \mathcal T_{2,\sigma_0,i}={}&
 \sum_{\substack{o\in\mathfrak O_\sigma,\ g'\ {\rm sf}\\
d_2\mid g',\ k''\ne0}}
 w_o^+\psi_g\psi_{d_2}\psi_{k''}\mu(d_2)\mathcal B_2(k'')|B_o(g')|^2\\
 &\times\sum_{\substack{z_1,z_2\ {\rm sf}\\
(z_1z_2,g')=1}}
 1_{(z_1,z_2)=1}L_{o,d_2,k''}(z_1)\overline{L_{o,d_2,k''}(z_2)}
       G([z_2][z_1]^{-1})\\
 &\times\mathfrak d_{I_i}(g'z_1)\overline{\mathfrak d_{I_i}(g'z_2)}
       W_i(q_{g'}q_{z_1}/Z^{s_i})
       \overline{W_i(q_{g'}q_{z_2}/Z^{s_i})}\\
 &\times\frac{K}{q_{d_2}\sqrt{q_{z_1}q_{z_2}}}
       \mathcal K_2\!\left(\frac{Kq_{k''}}{q_{d_2}q_{z_1}q_{z_2}}\right).
 \end{split}\] 这里括号表示固定有限射线群中的类。的确，\(c_i(g'z)\) 的 算术部分分解为 \(B_o(g')\) 及其 在 \((g',z)=1\) 上的剩余 \(\mu(z)\) 系数。公行因子 是在 \(g'\) 处的掩码，其 Poisson 展开给出一个除子 \(d_2\)，而上面的信号计算给出所示的两个 \(L\) 因子与射线商。被恢复的主配对 \(z_1=z_2=1\) 由 \(G(1)=1\) 相合。其单独的代价，以及在此公式之前 移除的原始补集，已经得到界定。 因此这是对正 优函数指定分量的等式，而不是对原始带符号块的等式。

用其所示的无商 \(L\) 因子、固定射线商、形式乘积范数、 完整核以及不变的 \(\mathcal B_2\)，在 所有各自容许的无平方因子 \(z_1,z_2\) 上定义方程 [\[eq:inverse-second-formal-component\]](#eq:inverse-second-formal-component) 的被加项。它在互素配对上与 真正的公式一致。在任何逐因子估计之前插入完整恒等式 \[1_{(z_1,z_2)=1}=\sum_{v'\mid(z_1,z_2)}\mu(v'),\qquad z_a=v'n_a,\] 设 \(v\ge0\) 为 无平方因子 \(v'\)-二分块的中心，\(\widehat v=\log_Zq_{v'}\)。 \(n_a\) 无平方因子，且 \((v',n_a)=1\)；它们不必互相 互素。在此扩展上不使用本原 Poisson 公式。 对无平方因子的 \(v'\) 令 \[D_o(v';d_2,k'')=a_0(v')\nu_i(v')\rho(v')1_{(v',r_0)=1}
   \chi_{v'}(H_o)^4\chi_{v'}(d_0)\overline{\chi_{v'}(d_2)}\chi_{v'}(k'').\] 在对无平方因子且互素的 \(v',n\) 上，精确提取为 \[\label{eq:inverse-second-extraction}
 \begin{split}
 L_{o,d_2,k''}(v'n)={}&D_o(v';d_2,k'')a_0(n)\nu_i(n)\rho(n)1_{(n,r_0)=1}\\
 &\times\chi_n(H_o)^4\chi_n(d_0)\overline{\chi_n(d_2)}
          \chi_n(k'')\chi_n(v')^4.
 \end{split}\] 这使用了 \(a_0(v'n)=a_0(v')a_0(n)\chi_n(v')^4\)。在重叠处， 右端通过 \(\chi_n(v')^4\) 定义该扩展为零， 而不去计算非无平方因子的 Gauss 和。两个公因子 给出 \(|D_o(v';d_2,k'')|^2\)，其中包括零点 \((v',k'')=1\) 及其 固定刺点、\(d_0\) 以及标签零点。它们通过 Cauchy 保留在外 权重中。旧的最大公因子还留下 \(1_{(v',g')=1}\)。 由于 \(D_o\) 在 \((v',CJ)>1\) 上为零，我们等价地保留 显式外因子 \(1_{(v',g'CJ)=1}\)，它重复了那个标签零点。

令 \(r_g=g'/d_2\)、\(k_{\rm new}=d_kd_2k''\) 以及 \(f_{\rm new}=JCd_2v'\)。所有关于 \(n\) 的变动因子满足 完整的零扩展恒等式 \[\label{eq:inverse-moving-characters}
 \chi_n(d_k)\chi_n(k'')\overline{\chi_n(d_2)}
       \chi_n(CJ)^4\chi_n(v')^4
 =\chi_n(k_{\rm new})\chi_n(f_{\rm new})^4.\] 它使用了 \(\overline{\chi_n(d_2)}=\chi_n(d_2)\chi_n(d_2)^4\)，在 非单位元上也成立。与 \(g'=d_2r_g\) 的剩余最大公因子分解为在 \(d_2\) 处重复的 零点以及在 \(r_g\) 处的固定刺点。在 \(q_0,t'\) 处的旧刺点 保持不变。若 \(\mathcal C_{\rm ray}\) 表示 \(G\) 通过其分解的固定 群，令 \[\widehat G(\vartheta)=|\mathcal C_{\rm ray}|^{-1}
       \sum_{c\in\mathcal C_{\rm ray}}G(c)\overline{\vartheta(c)}.\] 则 \[G([n_2][n_1]^{-1})=\sum_{\vartheta\in\widehat{\mathcal C}_{\rm ray}}
   \widehat G(\vartheta)\overline{\vartheta(n_1)}\vartheta(n_2).\] 因此在固定射线被加项中的两个新多项式使用相同的 \(\nu_i\overline\vartheta\)，而其唯一有界系数 \(\widehat G(\vartheta)\) 保持在外层。

###### 新的典范数据及其容许性。

第二次变换已将变动特征恢复到典范 形式。我们现在识别哪些数据将被固定、哪些将保持 平均。这一区分也决定了子的刺点。 对两侧令 \(\nu_a'=\nu_i\overline\vartheta\) 并定义 \[\label{eq:canonical-child-data}
 \begin{gathered}
 \gamma=(q_0,t',r_g),\qquad r_g=g'/d_2,\\
 k_{\rm new}=d_kd_2k'',\qquad f_{\rm new}=JCd_2v',\\
 \rho'(n)=\rho_\gamma(n)=\rho(n)1_{(n,\operatorname{rad}q_0t'r_g)=1}.
 \end{gathered}\] 在非零系数支集上，\(J,C,d_2,v'\) 无平方因子 且两两互素：\((C,J)=1\) 属于 \(\mathfrak O_\sigma\)， \(|B_o(g')|^2\) 迫使 \((g',CJ)=1\)、\(d_2\mid g'\)，而 \(D_o\) 被 保留的零点连同旧的最大公因子限制给出 \((v',g'CJ)=1\)。因此 \(f_{\rm new}\) 在该支集上无平方因子。 这些公因子通过 Cauchy 保留在外权重中。

三元组 \(\gamma\) 将在子行和标签求和之前被固定。 其刺点 \(\rho_\gamma\) 因此独立于这两个 平均变量。理想 \(J,C,d_2,v'\) 保留在新的 平均标签中；它们不被计作额外的固定标签。

在每个选定侧的 副本上，以有序列表 \((d_2,r_g,v';n_a)\) 应用方程 [\[eq:inverse-slot-priority\]](#eq:inverse-slot-priority)。 设 \(I_a'\) 为副本 \(a\) 中在 \(n_a\) 上保留的选定侧槽位的 子集。被指定的素数及其优先级掩码保持在外层。 整除 \(n\) 的存活素数 已由四次幂零点与 \(JCd_2v'\) 互素，并 由固定刺点与 \(\operatorname{rad}q_0,t',r_g\) 互素。这些也 提供了所有更早的存活排除，因为 \(\operatorname{supp}\mathfrak B\subset\operatorname{supp}(Jq_0)\)。 存活的标记因此是一个原有的乘积形式子集。 一个被描述为指派给 \(J\) 的旧槽位，只是由这个导出的支集对 旧 \(b_a,\mathfrak A_a\) 指派的重分组，而不是 一个新的独立素数选择。

将 \(\mathcal B_2\) 保持在完整核 与旧窗口的 Fourier 分离之外。设 \(I_g,I_d,I_v,I_k\) 为 当前各个二分块截断 \(\psi_g,\psi_{d_2},\psi_v,\psi_{k''}\) 的完整支集。 选取新的截断 \(\omega_{n,a}\)，使其在 \(W_i\) 的支集除以 \(I_gI_v\) 上等于一，并在区间 \([a,b]\) 内具有固定的完整支集，其中 \(b\ge1\)。选取一个非负的 \(\omega_f\)，使其在 \(I_JI_CI_dI_v\) 上等于一，并具有固定的完整支集 \(I_f\)。将这些 完整支集，以及在其上重构的形式乘积 \(g'v'n\)， 纳入上述指定的有限窗口族 \(\mathcal I_D\)。 这些完整的全新子窗口给出形式中心与支集界 \[\label{eq:canonical-child-lengths}
 \begin{gathered}
 N_c=r-A_i-B-t-g-v,\qquad V_c=B+\theta+v+j,\qquad F_c=N_c+V_c,\\
 |\widehat n_{\rm child}-N_c|\le6\eta,\qquad
 |\widehat f_{\rm new}-V_c|\le4\eta.
 \end{gathered}\] 在因式分解表达式上，这些界来自精确乘积 \(n_i=\mathfrak A_iCt'g'v'n_{\rm child}\) 与 \(f_{\rm new}=JCd_2v'\)。完整的全新子截断与完整扩大的 标签窗口包含在 \(\mathcal I_D\) 中，因此当稍后由 正性加入独立项时，同样的界直接在其支集上成立。那些加入的项 并不被断言来自父因式分解。在当前分离过程中，在完整全新截断上 重构的形式乘积 \(x=g'v'n\) 也包含在 \(\mathcal I_D\) 中；因此第二次前因子中所用的 \(4\eta\) 界 在整个分离侧上成立。

保持非负标签中心 \(V_c\)，不向上取整。 仅当保留的行分量非零时才进入子；此时 外球有 \(M_{\rm ch}\ge0\)。这个门控独立于任何 结构外指标集，后者即使在 \(\mathcal B_2\) 恒为零时也可能包含零权元组。类似地，若一个完整的全新 子列窗口不包含无平方因子理想，则其多项式为零 且该分量被省略。若 \(N_c<0\) 且存在子列，则其范数至少为一，且 方程 [\[eq:canonical-child-lengths\]](#eq:canonical-child-lengths) 给出 \(-6\eta\le N_c<0\)。 对一个被保留的非空子定义 \[\label{eq:inverse-child-clipping}
 N_{\rm ch}=\max(0,N_c),\qquad \delta_N=N_{\rm ch}-N_c\in[0,6\eta],
 \qquad F_{\rm ch}=N_{\rm ch}+V_c=F_c+\delta_N.\] 这是测试的有界改变，而不是 \(Z^\eta\) 宽度的支集 扩大。使用上面选取的固定包围支集区间 \([a,b]\)。若 \(N_c<0\)，非空性给出 \(Z^{\delta_N}\le b\)；若 \(N_c\ge0\)， 则 \(\delta_N=0\)，同样的界由 \(b\ge1\) 得到。 因此在两种情形下都有 \(1\le Z^{\delta_N}\le b\)。新的环形截断 \(\omega_{n,a}(Z^{\delta_N}y)\) 在 \([a/b,b]\) 中有支集且具有一致 有界的 Euler 半范数。它们的尺度只依赖于固定的扇区 中心，而不依赖于当前的行或标签。这些裁剪 支集的完整并集包含在 \(\mathcal I_D\) 中。

通过 \(v'\)-二分块、 第二个射线被加项与槽位分支固定 \(\sigma_0\) 的一个细化 \(\sigma\)。 令 \(\Xi_\sigma\) 由 \[\xi=(o,g'\ {\rm sf},d_2\mid g',v'\ {\rm sf},k''\ne0;
               \text{新指派的槽位素数})\] 组成，带有保留的各个支集与槽位分支。它既不含 旧的 \(f,h\)，也不含当前的列指标 \(n_1,n_2\)。 定义 \(R_1,E,J,q_0\) 的恒等式继承自 \(o\)， 而 \(\gamma,k_{\rm new},f_{\rm new}\) 是 \(\xi\) 的所示函数。 该集合可以在施加 \(\mathcal B_2\) 与 \((v',g'CJ)=1\) 之前取定，将这些掩码保留在带符号的外权重中。令 \(\mathcal A_{2,\sigma}(\xi)\) 为所有新指派的 原槽位系数及其优先级掩码的乘积，在 侧二上取共轭。

设 \(\mathfrak X_\sigma^{\rm src}\) 为 这个变换分量的结构外集合，在加入任何独立子行 或标签之前。它保留 \(o\in\mathfrak O_\sigma\)，特别是精确重构 \(b_1b_2=q_0^2J_2^2s\)、导出的 \(J=sJ_2,q_0\)，以及完整的 固定 \(b_1,b_2,t'\) 二分块支集；它还保留固定的 \(g',d_2\) 支集、\(d_2\mid g'\)，以及它的其他外算术 与槽位条件。零权元组可以被保留，而单位 Fourier 相位在定义这个结构集时被忽略。用 下式定义不同三元组的集合，不含见证重数： \[\label{eq:inverse-source-triples}
 \Gamma_\sigma=
 \{(q_0,t',r_g=g'/d_2):\xi\in\mathfrak X_\sigma^{\rm src}\}.\] 这个投影在所有可能的当前行与 标签上一次取定，在固定任何 \(k_{\rm new},f_{\rm new}\) 或 Fourier 模式之前。每个非零变换项都映入其中。每个元素 都有一个源见证，给出 \(\widehat c\le\ell+\eta\)、\(\widehat t\le t+\eta\) 以及 \(\log_Zq_{r_g}\le g-\theta+2\eta\)。这些界中的第一个 将为子刺点所需要；用于计数的包围范数球 并不蕴含它。上面陈述的非空行与子列门控 保持与这个结构投影分离。

令 \[D_c=\ell+A_i+t+g-\theta+V.\] 由于 \(r=N-3\ell\) 是联系到固定父的一个精确定义， 在方程 [\[eq:canonical-child-lengths\]](#eq:canonical-child-lengths) 与 [\[eq:second-poisson-lengths\]](#eq:second-poisson-lengths) 中代入给出精确的形式恒等式 \[\label{eq:canonical-transition}
 \begin{gathered}
 F_c=F-D_c-2\ell+j,\qquad M_c=M-2D_c-2\ell+j,\\
 F_c-M_c=F-M+D_c,\\
 4F_c-3M_c=4F-3M+2(A_i+t+g-\theta+V)+j.
 \end{gathered}\] 这些恒等式涉及与 方程 [\[eq:inverse-fixed-invariant\]](#eq:inverse-fixed-invariant) 相同的固定 \(F=N+V\)，而不是实际的父范数。

对每个 \(\gamma\in\Gamma_\sigma\)，任取一个源见证。 其实际的整除性 \(d_2\mid g'\) 与 方程 [\[eq:inverse-cube-actual\]](#eq:inverse-cube-actual) 给出 \[\widehat\theta\le\widehat g,\qquad
 \widehat j\le2\widehat\ell_{\rm pair},\qquad
 \widehat c\le\widehat\ell_{\rm pair}.\] 因此这里所需的唯一实际到中心的不等式为 \[\label{eq:inverse-center-inequalities}
 g-\theta\ge-2\eta,\qquad j\le2\ell+3\eta,\qquad
 \widehat c\le\ell+\eta.\] 前两个并不以零误差成立。特别地， 第三个不等式对其源见证的每个固定三元组成立， 尽管它不必在整个包围计数 球内成立。方程 [\[eq:canonical-child-data\]](#eq:canonical-child-data) 中的新根式 具有实际对数范数 \(Q_{\rm new}=Q_\gamma\)，满足 \[\label{eq:inverse-new-puncture}
 \begin{split}
 Q_{\rm new}&\le Q+\widehat c+\widehat t+\widehat g-\widehat\theta\\
 &\le Q+\ell+t+g-\theta+4\eta\le Q+D_c+4\eta.
 \end{split}\] 这在其因子与旧刺点共有素数时也成立， 因为取根式只会减小范数。最后一个不等式 使用了 \(A_i,V\ge0\)。

在方程 [\[eq:canonical-transition\]](#eq:canonical-transition) 中使用 \(F_{\rm ch}=F_c+\delta_N\)、\(M_{\rm ch}=M_c+\eta\) 以及 \(2(A_i+t+g-\theta+V)+j\ge-4\eta\)。两个子余量满足 \[\label{eq:inverse-child-margins}
 \begin{aligned}
 F_{\rm ch}-M_{\rm ch}-Q_{\rm new}-z_0
   &\ge c_{\rm node}+\delta_N-5\eta\ge c_{\rm node}-5\eta,\\
 4F_{\rm ch}-3M_{\rm ch}-6z_0
   &\ge c_{\rm node}+4\delta_N-7\eta\ge c_{\rm node}-7\eta.
 \end{aligned}\] 名义上界 \(z_0\) 不变，因为存活的标记是一个 子集。此外 \(D_c\ge\ell+V-2\eta\) 且 \(2\ell-j\ge-3\eta\)，于是 \[\label{eq:inverse-row-decrease}
 M-M_{\rm ch}=2D_c+2\ell-j-\eta
       \ge2(\ell+V)-8\eta\ge2d-8\eta.\] 对 \(\eta\le d/16\)，这至少为 \(3d/2\)，因此至少为 \(d\)。 同样的恒等式给出 \(F_c\le F-\ell-V+5\eta\)，故 \(F_{\rm ch}\le F+11\eta\)。由于其两个被加项都非负， 这在有限深度内界定了子 \(N_{\rm ch},V_c\)。

算术构造因此产生了具有更小行长度的容许子 区间。我们接下来用它们的 典范多项式来表示变换后的和。所需的 Fourier 密度对所有 三元组 \(\gamma\)、行和标签都是公共的；只有在那个恒等式之后我们才 应用 Cauchy 并控制重构重数。

###### 第二次变换和的公共密度。

在对任何实际外理想求和之前，使用六个独立坐标 \[(y_g,y_d,y_v,y_k,y_1,y_2)
 =\left(\frac{q_{g'}}{Z^g},\frac{q_{d_2}}{Z^\theta},
 \frac{q_{v'}}{Z^v},\frac{q_{k''}}{Z^{h_2}},
 \frac{q_{n_1}}{Z^{N_c}},\frac{q_{n_2}}{Z^{N_c}}\right).\] 使用已经选取的新截断 \(\omega_{n,a},\omega_f\)。 将四个当前二分块截断 与 \(\omega_f\) 保留在反演之外，而将 \(\omega_{n,a}\) 保留在两个 列中。设 \(\Omega_{2,\alpha}\) 为更大的截断，在相应四个二分块与两个列 截断的完整支集上等于一。这些完整支集、\(I_f\)，以及在其上的形式乘积 \(g'v'n\)，就是已经包含在 \(\mathcal I_D\) 中的窗口。

精确的第二根与核自变量为 \[\label{eq:inverse-second-root-kernel}
 \begin{split}
 \frac{K}{q_{d_2}q_{v'}\sqrt{q_{n_1}q_{n_2}}}
 &=Z^{\lambda_c+12\eta+\tau}y_d^{-1}y_v^{-1}(y_1y_2)^{-1/2},\\
 \frac{Kq_{k''}}{q_{d_2}q_{v'}^2q_{n_1}q_{n_2}}
 &=A_{{\rm ker},2}\frac{y_k}{y_dy_v^2y_1y_2},\\
 A_{{\rm ker},2}&=Z^{H_{\rm use}+h_2-\theta-2v-2N_c}.
 \end{split}\] 的确 \(N_c=s_i-g-v\) 且 \(\lambda_c=H_c-\theta-(s_i-g)\)。定义单一的环境剖面 \[\label{eq:inverse-second-profile}
 \begin{split}
 \mathfrak H_{2,\sigma,\boldsymbol t}(\boldsymbol y)={}&Z^{-6\eta}
 \prod_\alpha\Omega_{2,\alpha}(y_\alpha)
 y_d^{-1}y_v^{-1}(y_1y_2)^{-1/2}\\
 &\times W_i(y_gy_vy_1)\overline{W_i(y_gy_vy_2)}
 \mathcal K_2\!\left(A_{{\rm ker},2}\frac{y_k}{y_dy_v^2y_1y_2}\right).
 \end{split}\] 其外的标量恰好为 \(Z^{\lambda_c+18\eta+\tau}\)。 完整的 \(q_{d_2}\) 分母与两个正规化的实列根 都在这个剖面中，且没有这样的根被追加到最终测试中。

对 \(\boldsymbol\zeta=(\zeta_g,\zeta_d,\zeta_v,\zeta_k,
\zeta_1,\zeta_2)\)，令 \(z_n=q_n/Z^{N_{\rm ch}}\) 并定义 \[W_a'(z)=\omega_{n,a}(Z^{\delta_N}z)z^{\varepsilon_a i\zeta_a},
 \qquad \nu_a'=\nu_i\overline\vartheta,\qquad
 \mathfrak d_a'=\mathfrak d_{I_a'}.\] 则任一新 Cauchy 侧上的多项式恰好为 \[\label{eq:canonical-child-polynomial}
 \begin{split}
 Q_{a,\gamma,\boldsymbol\zeta}(k_{\rm new},f_{\rm new})={}&
 \sum_{n\ {\rm sf}}\bar\alpha(n)\gamma_2(n)\nu_a'(n)\rho'(n)
 \chi_n(k_{\rm new})\\
 &\times\chi_n(f_{\rm new})^4
 \mathfrak d_a'(n)W_a'(q_n/Z^{N_{\rm ch}}).
 \end{split}\] 在 \(q_0,t',g'/d_2\) 与有限射线扇区固定之后， \(\nu_a'\) 与 \(\rho'\) 独立于 \(J,C,d_2,v'\) 以及 新行。关于 \(n\) 的唯一新特征是显式 所示的行因子与四次幂因子；所有涉及 旧 \(b_i,\mathfrak A_i\) 的其他相位都被放入 方程 [\[eq:retained-cube-label\]](#eq:retained-cube-label) 或旧行 \(\widetilde h\) 中。分离出的环形权重 \(W_a'\) 也 独立于新行与标签。 完整的剩余外权重为 \[\label{eq:inverse-second-outer-weight}
 \begin{split}
 V_\sigma(\xi;\boldsymbol\zeta)={}&w_o^+\mu(d_2)\mu(v')\widehat G(\vartheta)
 |B_o(g')|^2|D_o(v';d_2,k'')|^2
 1_{(v',g'CJ)=1}\mathcal B_2(k'')\\
 &\times\mathcal A_{2,\sigma}(\xi)
 \psi_g(y_g)\psi_{d_2}(y_d)\psi_v(y_v)\psi_{k''}(y_k)
 \omega_f(q_{f_{\rm new}}/Z^{V_c})\\
 &\times y_g^{i\zeta_g}y_d^{i\zeta_d}y_v^{i\zeta_v}y_k^{i\zeta_k}
       Z^{i\delta_N(\zeta_1+\zeta_2)}.
 \end{split}\] 所有旧的纯算术与优先级掩码都保留在 \(\mathfrak O_\sigma\) 中，带有其非负的旧系数权重 \(w_o^+\)。所示的两个公共模保留其他每一个 公共系数零点，包括依赖于 \(k''\) 的那个。 有一个 \(\mu(d_2)\)、一个 \(\mu(v')\) 以及一个射线系数。 标签截断作为等式插入到原乘积 支集上并保持在外层。

令 \(\mathcal T_{\sigma,i}\) 为由上述完整的 Möbius 与槽展开从方程 [\[eq:inverse-second-formal-component\]](#eq:inverse-second-formal-component) 得到的固定 \(v'\)-二进段、射线与槽求和项。子式所需的精确恒等式为 \[\label{eq:inverse-xi-identity}
 \begin{split}
 \mathcal T_{\sigma,i}={}&Z^{\lambda_c+18\eta+\tau}(2\pi)^{-6}
 \int_{\mathbb R^6}\widehat{\mathfrak H}_{2,\sigma,\boldsymbol t}
       (\boldsymbol\zeta)\\
 &\quad\times\sum_{\xi\in\Xi_\sigma}V_\sigma(\xi;\boldsymbol\zeta)
 Q_{1,\gamma,\boldsymbol\zeta}(k_{\rm new},f_{\rm new})
 \overline{Q_{2,\gamma,\boldsymbol\zeta}(k_{\rm new},f_{\rm new})}
 \,d\boldsymbol\zeta.
 \end{split}\] 为了验证它，展开这两个 \(Q\)。由于 \(y_a=Z^{\delta_N}z_{n_a}\)，它们的模式连同方程 [\[eq:inverse-second-outer-weight\]](#eq:inverse-second-outer-weight) 的最后一个因子恰好是 \(y_1^{i\zeta_1}y_2^{i\zeta_2}\)。其余四个模式是外部的。 方程 [\[eq:inverse-log-fourier\]](#eq:inverse-log-fourier) 恢复完整剖面， 其较大的截断在保留的支集上等于一。全新的 列截断在旧 \(W_i\) 因子非零处等于一， 而 \(\omega_f=1\) 在每个原始标号乘积上。因此标量与 剖面恢复了完整根、完整核以及旧窗口。 方程 [\[eq:inverse-second-extraction\]](#eq:inverse-second-extraction)、 [\[eq:inverse-moving-characters\]](#eq:inverse-moving-characters) 和 [\[eq:inverse-slot-priority\]](#eq:inverse-slot-priority) 逐项恢复算术因子。 固定盒求和是有限的，而 方程 [\[eq:inverse-fourier-moment\]](#eq:inverse-fourier-moment) 为该积分提供依据。 完整新窗口中的额外组合在此复 Fourier 恒等式中通过旧 窗口在 Cauchy 之前相消；只有在稍后 它们才被独立地保留在一个正和中。

方程 [\[eq:inverse-xi-identity\]](#eq:inverse-xi-identity) 中的密度依赖于 固定的扇区、\(Z\)、固定的检验函数与 \(\boldsymbol t\)，而不依赖于 实际的 \(\gamma,k_{\rm new},f_{\rm new}\)。耦合核使用的是 裸 \(k''\) 坐标，而非导出的行；后者只 出现在特征与 \(\mathcal B_2\) 中。导出的标号只 出现在特征及其外截断中。诸如 \(g'=d_2r_g\) 的关系式限制的是求值点，而非变换。 对每个固定的 \(B_{\rm ht},J_{\rm ht}\ge0\)，方程 [\[eq:inverse-fourier-moment\]](#eq:inverse-fourier-moment) 中的 Euler 计算 给出某个固定的 \(b\)，使得 \[\label{eq:inverse-joint-fourier-moments}
 \int_{\mathbb R^9}\int_{\mathbb R^6}
 |\widehat{\mathfrak H}_{1,\sigma}(\boldsymbol t)|
 |\widehat{\mathfrak H}_{2,\sigma,\boldsymbol t}(\boldsymbol\zeta)|
 (1+|\boldsymbol t|)^{B_{\rm ht}}(1+|\boldsymbol\zeta|)^{J_{\rm ht}}
 \,d\boldsymbol\zeta\,d\boldsymbol t\ll p_b(W)^2.\] 事实上，内层加权积分关于 \(\boldsymbol t\) 是多项式， 因为 \(W_i\) 是一个固定截断乘以单位范数模式；将 第一变换的界应用于该多项式阶再加 \(B_{\rm ht}\)。 这些常数对每个实际理想和每个正 核标量都是一致的，不含 \(Z\) 的高度阶幂。

###### 第二个 Cauchy 不等式与外层计数。

对每个固定的 Fourier 模式，以 \(U_a=Z^{(\lambda_c+18\eta+\tau)/2}Q_{a,\gamma,\boldsymbol\zeta}\) 在完整集合 \(\Xi_\sigma\) 上把方程 [\[eq:weighted-cauchy\]](#eq:weighted-cauchy) 应用于第二个变换后的 和。特别地，\(\mathcal B_2\)、\(|B_o|^2\)、\(|D_o|^2\) 与 \(1_{(v',g'CJ)=1}\) 仍然在其权重中。它们保留了 上面证明的 \(f_{\rm new}\) 的无平方因子性。权重中所有其他因子都由 一个固定常数界定， 包括原始指派槽系数的有界个数、 固定射线系数、各个截断以及单位模式。 因此，只有在 Cauchy 之后，绝对权重才满足 \[|V_\sigma(\xi;\boldsymbol\zeta)|
 \ll \mathcal B_2(k'')\mu^2(f_{\rm new}).\] 这一步使得新平均后的理想得以保持在 无平方因子类中。

我们首先记录控制一个纤维所需的精确重构。 \[\label{eq:poisson-divisor-reconstruction}
 d_k\mid C\mathfrak B/R_1
 \quad\Longrightarrow\quad
 d_k\mid f_{\rm new}\operatorname{rad}q_0.\] 为证明这一点，\(\mathfrak B/R_1\) 的一个素数有 \(t_p=0\)。 局部表表明它具有偶奇偶性且 \(a_{ip}\) 相等。 若两者都为一，它属于 \(J_2\)；若两者都为零，它属于 \(\operatorname{rad}q_0\)。\(C\) 的素数已在 \(f_{\rm new}\) 中。这就证明了该蕴含关系。因此 \(d_k\) 也 在 \(f_{\rm new},q_0\) 被指定之后具有除子重数。 一旦这些因子固定，\(k''\) 就由 元素 \(k_{\rm new}=d_kd_2k''\) 唯一确定。

设 \(K_{\rm slot}\) 界定原始的槽个数。在固定的 \(\gamma=(q_0,t',r_g)\)、无平方因子的 \(f=f_{\rm new}\) 以及元素 \(k=k_{\rm new}\) 下，权重非零的可能的 \(\xi\in\Xi_\sigma\) 的个数 至多为一个固定常数乘以 \(D_{K_{\rm slot}}(f)C_{K_{\rm slot}}(\gamma)\)，其中 \[\label{eq:inverse-new-fibre}
 \begin{split}
 D_{K_{\rm slot}}(f)&=d_{\mathcal O}(f)^{9+4K_{\rm slot}},\\
 C_{K_{\rm slot}}(\gamma)&=
 d_{\mathcal O}(q_0)^{5+2K_{\rm slot}}
 d_{\mathcal O}(t')^{2K_{\rm slot}}
 d_{\mathcal O}(r_g)^{2K_{\rm slot}},
 \end{split}\] 这里及下文 \(d_{\mathcal O}\) 表示理想除子计数。 为完整起见，把 \(f\) 有序分配到 \(J,C,d_2,v'\) 的代价为 \(4^{\omega(f)}=d_{\mathcal O}(f)^2\)，而 拆分 \(J=sJ_2\) 的代价至多为 \(d_{\mathcal O}(f)\)。 满足 \(b_1b_2=q_0^2J_2^2s\) 的 \(b_1,b_2\) 的选择 至多耗 \(d_{\mathcal O}(q_0)^2d_{\mathcal O}(f)^3\)；\(\mathfrak A_a\mid\operatorname{rad}(b_1b_2)\) 的两种选择 至多耗 \(d_{\mathcal O}(q_0)^2d_{\mathcal O}(f)^2\)。这些估计用到 \(d_{\mathcal O}(IJ)\le d_{\mathcal O}(I)d_{\mathcal O}(J)\) 与 \(d_{\mathcal O}(I^2)\le d_{\mathcal O}(I)^2\)。 方程 [\[eq:poisson-divisor-reconstruction\]](#eq:poisson-divisor-reconstruction) 为 \(d_k\) 至多耗 \(d_{\mathcal O}(q_0)d_{\mathcal O}(f)\) 种选择。 于是 \(g'=d_2r_g\) 固定，而若其为整元素，则 \(k''=k/(d_kd_2)\) 是唯一的 元素。至多 \(2K_{\rm slot}\) 个旧指派 素数整除 \(q_0ft'\)，故它们的选择至多耗 \([d_{\mathcal O}(q_0)d_{\mathcal O}(f)d_{\mathcal O}(t')]^{2K_{\rm slot}}\)。 至多 \(2K_{\rm slot}\) 个新指派素数整除 \(fr_g\)， 至多耗 \([d_{\mathcal O}(f)d_{\mathcal O}(r_g)]^{2K_{\rm slot}}\)。 另一个第一侧存活的槽在选取 第一正侧时消失；被选中的存活槽在其 新平方中出现两次，恰如这里所计。因此所展示的乘积 控制该纤维，即使其实际大小依赖于 \(k\)。 这里没有对旧 \(f,h\) 的计数，没有对 \(J,C,d_2,v'\) 的独立计数，也没有第二次频率计数。

方程 [\[eq:fixed-cube-count\]](#eq:fixed-cube-count) 与相同的源见证 把 \(\Gamma_\sigma\) 置于三个范数球的乘积之内 \[q_{q_0}\le Z^{\ell+R/2-j+5\eta/2},\qquad
 q_{t'}\le Z^{t+\eta},\qquad q_{r_g}\le Z^{g-\theta+2\eta}.\] 我们使用这些球仅为了界定不同三元组的个数，而非 作为子式估计的替代区域。理想计数给出 \[\label{eq:canonical-fixed-count}
 \#\Gamma_\sigma\le C Z^{C_c+11\eta/2+\pi_{\rm count}},\qquad
 C_c=\ell+R/2-j+t+g-\theta.\] 这里 \(\pi_{\rm count}\) 是单独选取的聚合量 \(\pi\) 的一部分。在非空扇区中，这三个球的每个上指数 都非负，因为它界定了一个存在理想的范数； 因此理想计数中的常数项不增添边界幂。 特别地，这里不计 \(J\)。这三个 理想的区间都是有界的，故可调除子界在 包含球上一致地给出 \(C_{K_{\rm slot}}(\gamma)\ll Z^{\pi_{\rm fib}}\)。 令 \(c_\sigma=C_c+11\eta/2\)，并引入 真正与行和标号无关的测度 \[\label{eq:inverse-normalized-triples}
 d\nu_\sigma(\gamma)=Z^{-c_\sigma}
 \sum_{\gamma\in\Gamma_\sigma}C_{K_{\rm slot}}(\gamma)\delta_\gamma,
 \qquad \|\nu_\sigma\|\ll Z^{\pi_{\rm count}+\pi_{\rm fib}}.\]

###### 正规范子式。

对固定的 Fourier 模式，定义正子式和 \[\label{eq:inverse-positive-child}
 \begin{split}
 \mathcal H_{a,\gamma}={}&
 \sum_{\substack{f\ {\rm sf}\\q_f/Z^{V_c}\in I_f}}
 D_{K_{\rm slot}}(f)
 \sum_{\substack{k\in\mathcal O\\0<q_k\le Z^{M_{\rm ch}}}}
 |Q_{a,\gamma,\boldsymbol\zeta}(k,f)|^2
 =Z^{F_{\rm ch}}\mathcal E_{a,\gamma}.
 \end{split}\] 该等式是方程 [\[eq:canonical-energy\]](#eq:canonical-energy) 用同一行球、标号权重 \(D_{K_{\rm slot}}\) 以及 方程 [\[eq:canonical-child-polynomial\]](#eq:canonical-child-polynomial) 与 [\[eq:canonical-child-data\]](#eq:canonical-child-data) 中检验函数与穿刺的正规化；若那里 使用更大的固定行球，则该等式改为所需 上界方向的一个不等式。权重仅依赖于 \(f\)。 重指标之后，\(\mathcal B_2\) 恰是所展示的行球。 只有如今为正的外层行和标号和 被扩大为其完整固定窗口。各列使用其完整固定新 窗口，但其穿刺、标记与检验函数未被删除或 改变。刚证明的实际纤维控制给出 \[\begin{split}
 \left|\sum_{\xi\in\Xi_\sigma}V_\sigma Q_1\overline{Q_2}\right|
 &\le\prod_{a=1}^2
       \left(\sum_{\xi\in\Xi_\sigma}|V_\sigma||Q_a|^2\right)^{1/2}\\
 &\ll Z^{c_\sigma}\prod_{a=1}^2
       \left(\int_{\Gamma_\sigma}\mathcal H_{a,\gamma}
                    \,d\nu_\sigma(\gamma)\right)^{1/2}.
 \end{split}\] 这里 \(Q_a=Q_{a,\gamma,\boldsymbol\zeta}(k_{\rm new},f_{\rm new})\)。 两个平方根各提供 \(Z^{c_\sigma/2}\)，因此有 一个固定计数因子。一致子式界提供一份总 质量 \(\|\nu_\sigma\|\)，而非其平方。子式界将 仅用于 \(\gamma\in\Gamma_\sigma\)，利用已在 方程 [\[eq:inverse-child-margins\]](#eq:inverse-child-margins) 中验证的假设。

###### 能量指数。

形式中心满足精确恒等式 \[\label{eq:canonical-prefactor}
 \kappa_i+\lambda_c+C_c+2F_c=F.\] 这通过代入它们的定义与 \(H_c=2r-2B-M+4\ell+2V+\delta-j\) 得出；所有抽取出的长度相消，结果 为 \(r+3\ell+V=N+V\)。

我们现在仅对 \(\gamma\in\Gamma_\sigma\) 使用子式估计，因为对其已证明了前述的余量与行 下降。若它在其中一致地给出 \(\mathcal E_{a,\gamma}\ll C(\boldsymbol t,\boldsymbol\zeta)
Z^{F_{\rm ch}+\epsilon_{\rm child}}\)，并具有其 固定的多项式高度依赖，则由 方程 [\[eq:inverse-positive-child\]](#eq:inverse-positive-child) 与上面最终加权 Cauchy 界可得 \[\left|\sum_{\xi\in\Xi_\sigma}V_\sigma Q_1\overline{Q_2}\right|
 \ll C(\boldsymbol t,\boldsymbol\zeta)
 Z^{c_\sigma+2F_{\rm ch}+\epsilon_{\rm child}}\|\nu_\sigma\|.\] 正规化质量就是 方程 [\[eq:inverse-normalized-triples\]](#eq:inverse-normalized-triples) 中的那个；见证重数 已在其纤维权重中。然后利用方程 [\[eq:inverse-joint-fourier-moments\]](#eq:inverse-joint-fourier-moments) 对 公共 Fourier 密度积分一次。 它不属于离散测度，也不为 任何行或标号重新选取。因此真正的外层计数与其正规化 质量各出现一次。平均后的 \(J,C,d_2,v'\) 留在正 子式和中，不被另外计数。

若某个子式被 \(Z^{F_{\rm ch}+\epsilon_{\rm child}}\) 界定，则 第一前因子误差、第二前因子误差、固定计数以及 恢复的正规化在每个正的第二个 Cauchy 侧给出 \[\label{eq:inverse-step-loss}
 \begin{split}
 &\kappa_i+\lambda_c+C_c+2F_{\rm ch}
      +(\tfrac92+18+\tfrac{11}2)\eta+\tau+\pi+\epsilon_{\rm child}\\
 &\qquad=F+28\eta+2\delta_N+\tau+\pi+\epsilon_{\rm child}\\
 &\qquad\le F+40\eta+\tau+\pi+\epsilon_{\rm child}.
 \end{split}\] \(\delta_N\) 的两份副本都出现：一份恢复子式列 正规化，另一份出现在其断言的指数中。两个加权 Cauchy 不等式各取其正侧的几何平均，故 不会使这一损失加倍。第一个主界是 \(Z^{M+\pi}\)，而上面第二个主界至多为 \(Z^{F+26\eta+\tau+\pi}\)；两者都符合同一配额。

参数 \(\pi\) 有一个独立的量词。设 \(J_{\rm step}\) 为在一个固定的双 Poisson、双 Cauchy 分解树中使用某个自由除子或筛法指数、以及对数二进计数的因子的最大次数， 并在至多具有固定槽界的有穷多个指派上 取最大。一旦 \(L_{\rm pow}\) 界定这类使用中每个尺度乘积的对数长度， 就取每个自由输入指数至多为 \(\pi/(2J_{\rm step}\max(1,L_{\rm pow}))\)。对充分大的 \(Z\)， 至多 \(J_{\rm step}\) 个对数因子的乘积至多为 \(Z^{\pi/2}\)。这些选择使所有非中心、非频率的局部 损失至多为 \(CZ^\pi\)。它们包括被保留的公共频率 二进段以及重构除子界。特别地，不同的 配额 \(\pi_\beta,\pi_{\rm old},\pi_{\rm count},\pi_{\rm fib}\) 以及有限并的二进配额都是这个单一聚合量的一部分，而不是重复的 大小为 \(\pi\) 的配额。固定射线和与固定 半范数常数是常数。同一约定定义了 聚合终端损失 \(\pi_{\rm ref}\)。特别地，\(\pi\) 不隐藏 \(\eta\) 或 \(\tau\) 的任何倍数。

这就证明了条件化归约估计 [\[eq:canonical-reduction-contract\]](#eq:canonical-reduction-contract)，包括在作出下述选择后其公共测度与 有限阶的一致性。剩下的是统一固定 这些选择，并通过有限深度应用该归约。

###### 选择的次序与终止。

对所要求的规范指数 \(\epsilon_c=\epsilon\)，首先固定 起始区间、检验函数、槽界、\(c_*\)，然后像证明开头那样固定 \(d,D\)。选取 \[\label{eq:inverse-parameter-order}
 \begin{gathered}
 \eta\le\min\{d/16,c_*/(14D),\epsilon_c/(160D),c_*/1000,1/100\},\\
 \tau\le\min\{\epsilon_c/(4D),c_*/1000,1/100\},\qquad
 \pi\le\epsilon_c/(4D),\qquad
 \tau_{\rm ref},\pi_{\rm ref}\le c_*/1000.
 \end{gathered}\] 在两个 Poisson 比较中使用同一个 \(\tau\)。此时 \(\pi\) 是目标聚合损失；其子输入指数只在此有界尺度 区间已知后才选取。

选取一直到深度 \(D\) 的各个截断，包括每个完整较大的或 全新的支集以及上述有界裁剪族，并形成 \(\mathcal I_D,L_{\rm win}\)。包括活跃槽的乘积 区间以及终端常数 \(C_{\rm res},C_{\rm width},C_{\rm ker}\)，并在整个深度上取最大。 这是有限的，因为每段有有穷多个分解类型 且有有穷多段。令 \[F_{\max}=N_{\max}+V_{\max}+11D\eta,\qquad
 L_{\rm all}=100(1+M_{\max}+F_{\max}+z_{0,\max}+c_*).\] 这些界定了所有被保留的尺度长度。确实， 方程 [\[eq:inverse-row-decrease\]](#eq:inverse-row-decrease) 及其后的界给出 \(M\le M_{\max}\) 与 \(N,V\le F_{\max}\)。非空列窗口有 \(r\ge-\eta\)，故 \(\ell\le(F_{\max}+\eta)/3\)。所展示的父 乘积把每个抽取出的除子长度界定为 \(2F_{\max}+6\eta\)。 例如 \(d_k\mid C\operatorname{rad}(b_1b_2)\) 给出 \(\delta\le r+2\ell+4\eta\)，而方程 [\[eq:enlarged-first-frequency\]](#eq:enlarged-first-frequency) 随后给出 \(H_{\rm use}\le7F_{\max}+18\eta+\tau\)。终端活跃 导子支撑在行、\(f\)、穿刺与槽上；其 总长度至多为 \(M_{\max}+2F_{\max}+z_{0,\max}\) 再加上 已展示的比例配额。方程 [\[eq:inverse-terminal-width\]](#eq:inverse-terminal-width) 与 [\[old-eq:4.4\]](#old-eq:4.4) 把被保留的终端对偶长度界定为 \(4M_{\max}+4F_{\max}+2z_{0,\max}+3d+12\eta+\tau_{\rm ref}\)。 在方程 [\[eq:inverse-parameter-order\]](#eq:inverse-parameter-order) 之下，所有这些界以及 精确的导子乘积长度都低于 \(L_{\rm all}\)。 我们现在可以取 \(L_{\rm pow}=L_{\rm all}\) 并选取 实现 \(\pi\) 与 \(\pi_{\rm ref}\) 的子小指数。

定义 \(B_{\rm crude}\) 为如下得到的最大指数：把任一原始 Poisson 展开中每个有界的非频率理想或元素和（包括 两个列和）替换为长度 \(L_{\rm all}\) 处的格计数，并把每个显式范数因子（包括方程 [\[eq:inverse-raw-tail\]](#eq:inverse-raw-tail) 中的 \(1+a^{-1}\)） 替换为其绝对上界。 也把除子有界的系数与标记替换为其平凡多项式 范数界。 只排除频率核本身。这些展开含有 固定有限个因子，故此定义了一个有限的统一数。

对反射尾部，类似地用其有界的 行、局部与活跃乘积计数以及 \(1+a^{-1}\)（其中 \(a=X/q_c^2\)）定义 \(B_{\rm ref}\)。 不要在保留长度处计入被舍弃的对偶指标。 相反，方程 [\[old-eq:4.3\]](#old-eq:4.3) 在其支集上给出 \[\frac{|d(\mu)|}{\sqrt{q_\mu}}
 \le27q_\lambda^{-k/3}q_n^{-1/2}q_b^{-1}
 \le27q_\lambda^{4/3}\qquad(k\ge-4).\] 其他每个局部因子都由有界活跃素数上 \(q_p^{1/2}\) 的乘积界定， 并在舍弃其指示函数后与 \(\mu\) 无关。因此 \(B_{\rm ref}\) 覆盖所有非核系数与 有界计数，而剩余的 \(\mu\)-和是 \(\lambda^{-4}\mathcal O\) 上无限制的格和。

固定一个尾部节省 \(T>1+B_{\rm crude}+B_{\rm ref}\)。对每个 Poisson 尾部，选取一个 Schwartz 阶 \[A>1+(B_{\rm crude}+T)/\tau.\] 取 \(Y=Z^\tau\) 的方程 [\[eq:inverse-raw-tail\]](#eq:inverse-raw-tail) 随后使 被舍弃的原始外球补集为 \(O(Z^{-T})\)，至多相差有穷多个 输入半范数以及任何挠高中的一个固定多项式。对 反射的整二进段尾部，实际辐角至少为 \(Z^{\tau_{\rm ref}/2}\)；对 \(\lambda^{-4}\mathcal O\) 使用同一格壳界并选取 \[A_{\rm ref}>1+2(B_{\rm ref}+T)/\tau_{\rm ref}.\] 这就证明了被舍弃尾部的断言，而无需预设有 对被舍弃对偶长度的任何界。

接着，通过深度 \(D\) 反向选取有穷多个 Fourier 高度与光滑半范数阶， 位于所选尾部阶与 终端输入阶之上。正规化逆根是圆环上的固定实幂， 而完整核在范数单项式处的 Euler 微分 不引入尺度幂。方程 [\[eq:inverse-joint-fourier-moments\]](#eq:inverse-joint-fourier-moments) 与 [\[eq:inverse-normalized-triples\]](#eq:inverse-normalized-triples) 为每个正指标化 Cauchy 侧和提供 公共系数测度。对这些和分别应用 推论 [\[cor:indexed-seminorm-propagation\]](#cor:indexed-seminorm-propagation)， 使用刚由引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 证明的子式剖面界， 然后取所展示的几何 平均。如已所示，两个平方根保留一份正规化离散质量， 故真正的外层标号只被计一次。 后续应用中任何外部高度截断 都在此内部有限传播之后选取，而不插入其中。

最后选取 \(Z\) 足够大，使 \(\log Z\ge L_{\rm win}/\eta\)、 方程 [\[eq:inverse-terminal-width\]](#eq:inverse-terminal-width) 中 \(C_{\rm res},C_{\rm width}\) 的阈值、 \(\log Z\ge2\log C_{\rm ker}/\tau_{\rm ref}\)、 \(\log Z\ge4\log q_\lambda/\eta\)，以及短完备化中使用的固定 \(h\)-圆环阈值 均成立。还要施加定义 聚合局部损失的对数界以及输入引理的阈值。 所有选择都先于此最终阈值，且只依赖于固定 数据。有界的较小 \(Z\) 通过增大最终常数来处理。

现在对 \(h\le D\) 有 \(c_h=c_*-7h\eta\ge c_*/2\)。 方程 [\[eq:inverse-child-margins\]](#eq:inverse-child-margins) 与 [\[eq:inverse-row-decrease\]](#eq:inverse-row-decrease) 把每个被保留的非终端子式送到 下一深度及其行上界。在深度 \(D\)，该上界为负， 而每个被保留的行参数都非负。终端界 至多为 \(Z^F\)；主项与递归项在指数上至多耗 \(L_{\rm step}=40\eta+\tau+\pi\)。反向归纳在深度 \(h\) 给出 \(Z^{F+(D-h)L_{\rm step}}\)，且 \[D L_{\rm step}\le\epsilon_c/4+\epsilon_c/4+\epsilon_c/4<\epsilon_c.\] 这就证明了 \(\mathcal E\ll Z^{F_0+\epsilon}\)，并具有所声称的 一致有限半范数与多项式高度依赖。

#### 带标记矩的初始化

我们现在把引理 [\[lem:marked\]](#lem:marked) 中的逆多项式转换为 规范族。只需一次 Poisson 变换。

在乘积 \(M_u(Z^r;W)Q_u\) 中，令 \(P\) 为其 槽素数的乘积，并置 \(j=(n,P)\)。\(n\) 与 \(P\) 都是 无平方因子的。固定出现在 \(j\) 中的槽的子集，并写出 \[n=jn_0,\qquad P=jP_0,\qquad (n_0,P_0)=1.\] 乘积 \(c=n_0P_0\) 是无平方因子的。恒等式 \[\mu(n_0)=\mu(c)\mu(P_0),\qquad
 \psi_u(n)\psi_u(P)=\psi_u(j)^2\psi_u(c)\] 在所有零延拓下成立。符号 \(\mu(P_0)\) 是 存活槽上符号的乘积，可并入它们的 有界系数。因此系数仍保持 方程 [\[old-eq:4.2\]](#old-eq:4.2) 中的形式。

对这个固定的指派子集，由其名义槽中心定义 \(G\)： \[G=\sum_{i\ {\rm assigned}}z_i,\qquad
 z_0=z-G,\qquad D'=r+z-2G.\] 于是 \(G,z_0\ge0\)，而 \(z_0\) 恰是存活的名义上界。 正规化满足 \[Z^{-(r+z)/2}=Z^{-G}Z^{-D'/2}.\] 实际的 \(j\) 是指派素数的乘积，故 \(q_j/Z^G\) 落在一个固定乘积区间中。理想计数至多给出 \(CZ^G\) 种选择，尚需加上为指派单独选取的除子损失。 行 Hilbert 空间中的三角不等式用 \(Z^{-G}\) 抵消这一计数。整个因子 \(\psi_u(j)^2\) 是 有界的行标量（包括其零点），并且是 该空间中的一个压缩。剩余列与 \(j\) 互素，给出固定 穿刺 \(1_{(c,j)=1}\)。

以下是这一重叠归约所依据的精确恒等式。设 \(I_0\) 为存活子集，并置 \(y_j=q_j/Z^G\)、\(y_c=q_c/Z^{D'}\)，以及对 每个槽 \(y_i=q_{p_i}/Z^{z_i}\)。在原始支集上， \[\frac{q_n}{Z^r}=\frac{y_jy_c}{\prod_{i\in I_0}y_i}.\] 对一个固定的指派元组，其对 \(M_u(Z^r;W)Q_u\) 的贡献 \(\mathcal U_{u,j}\) 恰为 \[\label{eq:initial-overlap-polynomial}
 \begin{split}
 \mathcal U_{u,j}={}&\mu(j)
 \prod_{i\notin I_0}a_i(p_i)W_i(y_i)\,
 Z^{-G}\psi_u(j)^2 Z^{-D'/2}
 \sum_{\substack{c\ {\rm sf}\\(c,j)=1}}\mu(c)\psi_u(c)\\
 &\quad\times
 \sum_{\substack{(p_i)\in\prod_{i\in I_0}\mathcal P_i\\P_0\mid c}}
 \mu(P_0)\prod_{i\in I_0}a_i(p_i)W_i(y_i)
 W\!\left(\frac{y_jy_c}{\prod_{i\in I_0}y_i}\right).
 \end{split}\] 确实，一个与 \(j\) 互素的无平方因子 \(c\)，连同 满足 \(P_0\mid c\) 的存活元组，唯一地重构出 \(n=j(c/P_0)\) 以及所规定的重叠。\(c\) 的 无平方因子性已给出 \((c/P_0,P_0)=1\)，故未丢失进一步的 条件。符号 \(\mu(P_0)\) 是各素数符号的乘积。 这也表明，后续每个平方两侧的 \(j\) 是同一个固定理想：前面的三角不等式是在 该平方之前取的。

恒等式 \(c=nP/j^2\) 把 \(y_c\) 置于一个固定紧区间中。 若 \(D'\) 在有界 非空窗口中略微为负，这仍有意义；\(D'\) 还不是规范参数。选取一个 新的个体截断 \(\omega_c\)，在此完整商 支集上等于一。对固定的 \(j\)，令 \(\Omega_c\) 在 \(\omega_c\) 的完整支集上 等于一，并令 \(\Omega_i\) 在每个完整存活 个体槽支集上等于一。单一的联合剖面 \[\mathfrak H_{{\rm ov},j}(y_c,(y_i)_{i\in I_0})
 =\Omega_c(y_c)\prod_{i\in I_0}\Omega_i(y_i)
 W\!\left(\frac{y_jy_c}{\prod_{i\in I_0}y_i}\right)\] 在这些独立坐标中紧支撑。当前的 截断 \(\omega_c\) 与个体因子 \(W_i(y_i)\) 留在 其变换之外。因此，在维数 \(1+|I_0|\) 下，方程 [\[eq:inverse-log-fourier\]](#eq:inverse-log-fourier) 把方程 [\[eq:initial-overlap-polynomial\]](#eq:initial-overlap-polynomial) 精确地表示为同一指派标量与 \(Z^{-G}\psi_u(j)^2\) 乘以 \[(2\pi)^{-1-|I_0|}\int_{\mathbb R^{1+|I_0|}}
 \widehat{\mathfrak H}_{{\rm ov},j}(\boldsymbol\upsilon)
 Z^{-D'/2}\sum_{c\ {\rm sf}}\mu(c)\psi_u(c)1_{(c,j)=1}
 \mathfrak d_{\boldsymbol\upsilon}(c)
 \omega_c(y_c)y_c^{i\upsilon_c}\,d\boldsymbol\upsilon,\] 其中 \(\mathfrak d_{\boldsymbol\upsilon}\) 具有原始存活 列表与个体系数 \(\mu(p)a_i(p)W_i(y_i)y_i^{i\upsilon_i}\)。展开标记并 反转联合变换即可逐项证明该等式。 不为实际存活元组选取测度。该测度可 依赖于已固定的 \(j\)，但方程 [\[eq:inverse-fourier-moment\]](#eq:inverse-fourier-moment) 对其 \(y_j\) 在固定乘积区间中是一致的。对这一测度， 在整个行 Hilbert 空间中使用 Minkowski 不等式。 在选用最终阈值之前，把 \(\omega_c\) 的完整支集、其较大的截断、 存活槽支集以及 \(j\)-乘积区间纳入有限 集合 \(\mathcal I_D\)。 采用与规范证明相同的 \(\eta\) 约定，于是我们有 \[|\widehat c-D'|\le\eta,\qquad |\widehat j-G|\le\eta\] 在下文实际使用的完整支集上成立，其中 \(\widehat c=\log_Zq_c\)。 对符号 \(\varepsilon_\chi=1\)，取整个剩余多项式的共轭， 包括其有限特征、标记与检验函数；其行范数不变。 对另一符号，保持不变。因此只需估计 一个恰具有如下形式的多项式 \[\label{eq:initial-residual-polynomial}
 \mathcal R_0(u)=Z^{-D'/2}\sum_{c\ {\rm sf}}
 \mu(c)\nu_0(c)1_{(c,j)=1}\overline{\chi_c(u)}
 \mathfrak d_0(c)W_0(q_c/Z^{D'}).\] 这里 \(\nu_0\) 是一个固定的有限射线特征，\(\mathfrak d_0\) 是上界 \(z_0\) 与那些个体系数 或其共轭的乘积标记，而 \(W_0\) 是 \(\omega_c(y)y^{i\upsilon_c}\) 或其共轭。它们都与行无关。

用一个固定的非负径向 Schwartz 函数 \(\Phi_{\rm init}\) 在尺度 \(Z^m\) 上控制原始行球，并展开其平方。设 \(C\) 为两列的 最大公因子，并写出 \(c_i=Cz_i\)，其中 \(z_1,z_2\) 无平方因子 且互素。置 \(\widehat c_i=\log_Zq_{c_i}\)，故前述 支集界对每个 \(i=1,2\) 都适用。设 \(B\ge0\) 为 \(C\) 的中心，并写出 \(\widehat B=\log_Zq_C\)。行特征具有本原模 \(z_1z_2\) 与剩余零掩码 \(C\)。应用 引理 [\[lem:masked-poisson\]](#lem:masked-poisson)，其中 \(d'\mid C\)。设 \(\theta\ge0\) 为其中心，\(\widehat\theta=\log_Zq_{d'}\)。置 \[P_1=B-\theta\ge-2\eta,\] 其中该不等式由 \(\widehat\theta\le\widehat B\) 以及 两个 \(\eta\)-比例界推出。实际导子长度为 \[\widehat L_{\rm init}=\widehat c_1+\widehat c_2-2\widehat B,
 \qquad |\widehat L_{\rm init}-2(D'-B)|\le4\eta.\] 对正容差 \(\tau_{\rm init}\)，蕴含关系 \(Z^mq_{h'}/(q_{d'}q_{z_1z_2})\le Z^{\tau_{\rm init}}\) 给出 \[\widehat{d'h'}\le2D'-m-2P_1+6\eta+\tau_{\rm init}.\] 定义固定的形式行尺度与包围行尺度 \[\label{eq:inverse-initial-row}
 M_c^{\rm init}=2D'-m-2P_1,\qquad
 M_{\rm init}=M_c^{\rm init}+6\eta+\tau_{\rm init}.\] 其中的 \(6\eta\) 有 \(4\eta\) 来自导子，\(2\eta\) 来自新行界中 \(d'\) 的两份副本。

为下面的直接计数分离出原有的主贡献。在真正的非主、互素 Poisson 表达式上， 在作任何非互素延拓或 Fourier 取绝对值之前，只保留外掩码 \[\mathcal B_{\rm init}(h')=1_{0<q_{d'h'}\le Z^{M_{\rm init}}}.\] 对每一对受支持的配对，其余集都包含在上面的实际比值尾部中。方程 [\[eq:inverse-raw-tail\]](#eq:inverse-raw-tail) 连同下面指定的独立初始原始计数与阶，恰好把该余集舍弃掉。在掩码内部保留完整的光滑核，不使用 依赖于列的比值选择子。该掩码依赖于 \(d',h'\)、固定的重叠与扇区，但不依赖于残余列。若 \(M_{\rm init}<0\)，其非零球为空，同样的尾部比较会舍弃每个非零频率；否则所保留的行参数非负。

实际的归一化因子与 Poisson 前因子按如下方式在两侧分裂 \[Z^{-D'}Z^{m-\widehat\theta-\widehat L_{\rm init}/2}
   =Z^{\widehat\kappa_1^{\rm init}/2}
      Z^{\widehat\kappa_2^{\rm init}/2},
 \quad
 \widehat\kappa_i^{\rm init}=m-D'-\widehat\theta-\widehat c_i+\widehat B.\] 因此实际的侧指数满足 \[\label{eq:initial-poisson-prefactor}
 \widehat\kappa_i^{\rm init}\le\kappa_c^{\rm init}+3\eta,
 \qquad \kappa_c^{\rm init}=m-2D'+P_1.\] 所有归一化的实逆根都将保留在下面的单个联合剖面中，而不再出现在最终的子检验中。主列具有 直接的对角界 \(O(Z^{m+\epsilon})\)，对于有界非空的负 \(D'\)-窗口亦然。任何被恢复到形式公式中的 主非零频率都带有相同的 \(\mathcal B_{\rm init}\) 掩码，并由引理 [\[lem:masked-poisson\]](#lem:masked-poisson) 中的 完整主恢复所界定，因为 \(Z^m\ge1\)。

插入来自对所有 \(d'\) 都相同的某一划分的 \(q_{h'}\) 频率二进块，而不是按标号重新中心的 划分。外掩码蕴含 \(q_{h'}\le Z^{M_{\rm init}}\)，因此在有界的保留范围内只有对数多个二进块。 设 \(H\) 为这样一个裸频率二进块的中心，并设 \(\psi_C,\psi_{d'},\psi_{h'}\) 为当前 \(C,d',h'\) 二进块上保留的各个截断函数，在其归一化范数处取值。

方程 [\[eq:initial-residual-polynomial\]](#eq:initial-residual-polynomial) 中的定向现已固定。第二次典范 Poisson 变换中的 计算把 \(\mu(z)\gamma_{-1}(z)\) 替换为 \(\bar\alpha(z)\gamma_2(z)\chi_z(-1)\overline{G(z)}\)。在第二侧，共轭内的因子具有射线因子 \(\overline{G(z)}\)；结合 CRT 交叉相位，相对射线因子为 \(G([z_2][z_1]^{-1})\)。用上面固定的 群公式展开它，并在一个固定的射线被加项中置 \[\nu_*=\nu_0\overline\vartheta,\qquad
 A_*(z)=\bar\alpha(z)\gamma_2(z)\nu_*(z),\qquad
 \mathcal K_{\rm init}=\mathcal F\Phi_{\rm init}.\] 对于固定重叠、这些二进块与射线被加项的预备图案 \(\Sigma_0\)，并在较早的模式固定不变的 情况下，带掩码且恢复主项后的非零分量恰为 \[\label{eq:initial-formal-component}
 \begin{split}
 \mathcal T^{\rm init}_{\Sigma_0}={}&
 \sum_{\substack{C\ {\rm sf},\ d'\mid C\\h'\ne0}}
 \psi_C\psi_{d'}\psi_{h'}\mu(d')\widehat G(\vartheta)
 \mathcal B_{\rm init}(h')1_{(C,j)=1}\\
 &\times\sum_{\substack{z_1,z_2\ {\rm sf}\\(z_1z_2,Cj)=1}}
 1_{(z_1,z_2)=1}
 A_*(z_1)\overline{A_*(z_2)}
 \overline{\chi_{z_1}(d')}\chi_{z_1}(h')
 \chi_{z_2}(d')\overline{\chi_{z_2}(h')}\\
 &\times\mathfrak d_0(Cz_1)\overline{\mathfrak d_0(Cz_2)}
 W_0(q_Cq_{z_1}/Z^{D'})\overline{W_0(q_Cq_{z_2}/Z^{D'})}\\
 &\times\frac{Z^{-D'}Z^m}{q_{d'}\sqrt{q_{z_1}q_{z_2}}}
 \mathcal K_{\rm init}\!\left(
       \frac{Z^mq_{h'}}{q_{d'}q_{z_1}q_{z_2}}\right).
 \end{split}\] 确实，对于 \(S\) 之外的无平方因子 \(C\)，有 \(|\mu(C)\nu_0(C)|^2=1\)，公共行因子恰为 \(1_{(u,C)=1}\)，其 Poisson 展开贡献了那个 \(\mu(d')\)。所展示的两个分子因子分别是本原特征 \(\overline{\chi_{z_1}}\chi_{z_2}\) 及其 Fourier 变换的因子。有限射线和通过 \(G(1)=1\) 恢复主 配对。该恢复的代价以及在此等式之前被去掉的原始余集已在上面分别界定。

对与 \(Cj\) 互素的所有单独无平方因子 \(z_1,z_2\)，用所展示的各个 \(A_*\) 因子、特征、 形式乘积范数、完整核与不变的外球来定义方程 [\[eq:initial-formal-component\]](#eq:initial-formal-component) 中的被加项。 它在互素区域上一致。插入完整的恒等式 \[1_{(z_1,z_2)=1}=\sum_{s\mid(z_1,z_2)}\mu(s),\qquad z_a=sn_a,\] 在作任何逐因子界定之前。设 \(v\ge0\) 为一个无平方因子 \(s\)-二进块的中心， \(\widehat v=\log_Zq_s\)，\(\psi_s\) 为其保留的各个截断函数。诸 \(n_a\) 无平方因子且与 \(s\) 互素，但不必彼此互素。这一形式延拓并不对非互素导子应用 Poisson 求和。对于无平方因子且互素的 \(s,n\)，CRT 与保零恒等式 \(\overline{\chi_n(d')}=\chi_n(d')\chi_n(d')^4\) 恰好给出 \[\label{eq:initial-common-extraction}
 \begin{split}
 A_*(sn)\overline{\chi_{sn}(d')}\chi_{sn}(h')
 ={}&A_*(s)\overline{\chi_s(d')}\chi_s(h')\\
 &\times A_*(n)\chi_n(d'h')\chi_n(d's)^4.
 \end{split}\] 四次幂包含了 CRT 因子 \(\chi_n(s)^4\)。在重叠上它把残余系数定义为零，而不必在非 无平方因子的理想上计算 \(\gamma_2\)。由于在 \(S\) 之外 \(|A_*(s)|=1\)，所提取的两个标量给出 \[|A_*(s)\overline{\chi_s(d')}\chi_s(h')|^2
 =1_{(s,d'h')=1}=1_{(s,h')=1}
 \quad\text{when }d'\mid C,\ (s,C)=1.\] 原有的残余与重叠排除条件还给出 \(1_{(C,j)=1}1_{(s,Cj)=1}\)。因此，除所指定的系数、 各个截断函数与单位相位之外，外算术权重恰为 \[\label{eq:initial-outer-arithmetic}
 \mu(d')\mu(s)\widehat G(\vartheta)\mathcal B_{\rm init}(h')
 1_{(C,j)=1}1_{(s,Cj)=1}1_{(s,h')=1}.\] 所有这些因子在加权 Cauchy 中始终保留。置 \[t=C/d',\qquad k=d'h',\qquad f=d's,\qquad
 \rho_{t,j}(n)=1_{(n,\operatorname{rad}(tj))=1}.\] 方程 [\[eq:initial-common-extraction\]](#eq:initial-common-extraction) 中关于 \(n\) 的因子，连同 \(\rho_{t,j}\)， 恰好提供了在 \(C,s,j\) 处的原有排除条件以及 \(d',h'\) 处的分子零点。在非零支集上，\(t,d',s,n\) 两两互素。对这一有序列表中的每个标记应用方程 [\[eq:inverse-slot-priority\]](#eq:inverse-slot-priority)。所指定的素数 及其优先掩码保持在外侧。一个存活的素数已通过 \(\chi_n(f)^4\) 与 \(d's\) 互素，并通过 \(\rho_{t,j}\) 与 \(tj\) 互素，因此其原有的各个列表与系数可以保留。其标记是容量为 \(z_0\) 的 原有子搜集，而非依赖于行或标号的残余系数。

因此，替换 \(k=d'h'\)、\(f=d's\) 以及穿刺 \(\rho_{t,j}\) 已经提供了典范的特征类与系数 类。我们仍需要一个公共的分离剖面、外重数界，以及所得区间的容许性。

把 \(\mathcal B_{\rm init}\) 保持在完整核与旧窗口的公共 Fourier 分离之外。精确的形式子中心 与完整的新支集界为 \[\label{eq:initial-canonical-lengths}
 \begin{gathered}
 N_c^{\rm init}=D'-B-v,\qquad V_c^{\rm init}=\theta+v,\qquad
 F_c^{\rm init}=D'-P_1,\\
 |\widehat n-N_c^{\rm init}|\le3\eta,\qquad
 |\widehat f-V_c^{\rm init}|\le2\eta.
 \end{gathered}\] 在已因子化的项上，这些界由 \(c=Csn\) 与 \(f=d's\) 得到。完整的新列截断与放大的标号窗口 也包含在 \(\mathcal I_D\) 中，因此同样的界对之后由正性加入的独立项也直接成立。新截断上重构的 形式乘积 \(c=Csn\) 也被包含在其中，因此初始前因子界在其整个分离侧上成立。

通过 \(s\)-二进块与槽分支固定一个加细 \(\Sigma\)，并保持较早的模式 \(\boldsymbol\upsilon\) 固定不变。在求和任何实际的外理想之前，使用六个独立坐标 \[(x_C,x_d,x_s,x_h,x_1,x_2)
 =\left(\frac{q_C}{Z^B},\frac{q_{d'}}{Z^\theta},
 \frac{q_s}{Z^v},\frac{q_{h'}}{Z^H},
 \frac{q_{n_1}}{Z^{N_c^{\rm init}}},
 \frac{q_{n_2}}{Z^{N_c^{\rm init}}}\right).\] 设 \(I_C,I_d,I_s,I_h\) 为四个当前各个截断函数的完整支集。选取 \(\omega_{n,a}\)，使其在 \(W_0\) 的支集除以 \(I_CI_s\) 上等于一，其固定完整支集位于一个包络区间 \([a,b]\) 中，且其上 端点满足 \(b\ge1\)。选取非负的 \(\omega_f\)，使其在 \(I_dI_s\) 上等于一，并具有固定的完整支集 \(I_f\)。当前的四个二进块截断与 \(\omega_f\) 保持在求逆之外，而 \(\omega_{n,a}\) 保持在列中。 设 \(\Omega_{{\rm init},\alpha}\) 为更大的截断函数，使其在相应的四个当前截断与两个新截断的完整 支集上等于一。这些完整支集、\(I_f\) 以及其上的形式乘积 \(Csn\) 就是已经包含在 \(\mathcal I_D\) 中的窗口。这些支集没有一个依赖于当前的外元组或 Fourier 模式。

保持 \(V_c^{\rm init}\ge0\)。仅当所保留的行分量非零时才进入某个子项，这蕴含 \(M_{\rm init}\ge0\)。这与下面结构性的外集合是分开的关口，后者即使当行球为空时也可能包含零权重 的元组。独立地，若某个完整的新子列窗口不包含无平方因子理想，则其多项式为零，该分量被略去。 对保留的非空子项定义 \[N_{\rm init}=\max(0,N_c^{\rm init}),\qquad
 \delta_{\rm init}=N_{\rm init}-N_c^{\rm init}\in[0,3\eta],\qquad
 F_{\rm init}=N_{\rm init}+V_c^{\rm init}=F_c^{\rm init}+\delta_{\rm init}.\] 对于非空的负中心窗口，\(q_n\ge1\) 且方程 [\[eq:initial-canonical-lengths\]](#eq:initial-canonical-lengths) 给出 \(\delta_{\rm init}\le3\eta\)，而其支集上端点给出 \(Z^{\delta_{\rm init}}\le b\)。若 \(N_c^{\rm init}\ge0\)，则 \(\delta_{\rm init}=0\)，且后一不等式由 \(b\ge1\) 得到。因此在每个 保留情形中都有 \(1\le Z^{\delta_{\rm init}}\le b\)。截断函数 \(\omega_{n,a}(Z^{\delta_{\rm init}}y)\) 的支集在 \([a/b,b]\) 中，且具有一致有界的 Euler 半范数。 其重标度只依赖于固定的中心，而不依赖于当前的行或标号，其完整的截断族包含在 \(\mathcal I_D\) 中。

在形式分解 \(z_a=sn_a\) 上，完整的根与核自变量恰为 \[\label{eq:initial-root-kernel}
 \begin{split}
 \frac{Z^{-D'}Z^m}{q_{d'}q_s\sqrt{q_{n_1}q_{n_2}}}
 &=Z^{\kappa_c^{\rm init}}x_d^{-1}x_s^{-1}(x_1x_2)^{-1/2},\\
 \frac{Z^mq_{h'}}{q_{d'}q_s^2q_{n_1}q_{n_2}}
 &=A_{{\rm ker},{\rm init}}\frac{x_h}{x_dx_s^2x_1x_2},\\
 A_{{\rm ker},{\rm init}}&=Z^{m+H-\theta-2(D'-B)}.
 \end{split}\] 对于第一个等式，使用 \(N_c^{\rm init}=D'-B-v\) 与 \(\kappa_c^{\rm init}=m-2D'+B-\theta\)。等价地，其根为 \(x_d^{-1}x_C(x_{c_1}x_{c_2})^{-1/2}\)，其中 \(x_{c_a}=x_Cx_sx_a\)。定义这个联合剖面 \[\label{eq:initial-joint-profile}
 \begin{split}
 \mathfrak H_{{\rm init},\Sigma,\boldsymbol\upsilon}(\boldsymbol x)
 ={}&Z^{-3\eta}\prod_\alpha\Omega_{{\rm init},\alpha}(x_\alpha)
 x_d^{-1}x_s^{-1}(x_1x_2)^{-1/2}\\
 &\times W_0(x_Cx_sx_1)\overline{W_0(x_Cx_sx_2)}
 \mathcal K_{\rm init}\!\left(
 A_{{\rm ker},{\rm init}}\frac{x_h}{x_dx_s^2x_1x_2}\right).
 \end{split}\] 其外侧标量恰为 \(Z^{\kappa_c^{\rm init}+3\eta}\)。旧的 \(c\)-窗口是耦合的，因此位于此 剖面中，所有归一化实逆根与完整核亦然。没有实根同时也被放入子检验中。

对 \(\boldsymbol\xi=(\xi_C,\xi_d,\xi_s,\xi_h,\xi_1,\xi_2)\)，置 \(z_n=q_n/Z^{N_{\rm init}}\)，再次令 \(\varepsilon_1=1,\varepsilon_2=-1\)，并定义 \[W_a^{\rm init}(z)=\omega_{n,a}(Z^{\delta_{\rm init}}z)
                       z^{\varepsilon_a i\xi_a}.\] 若 \(\mathfrak d_a'\) 为 \(a\) 侧上存活的子搜集，则精确的未归一化子多项式为 \[\label{eq:initial-child-polynomial}
 Q^{\rm init}_{a,t,j,\boldsymbol\xi}(k,f)
 =\sum_{n\ {\rm sf}}A_*(n)\rho_{t,j}(n)
 \chi_n(k)\chi_n(f)^4\mathfrak d_a'(n)
 W_a^{\rm init}(q_n/Z^{N_{\rm init}}).\] 其固定的有限特征、穿刺、乘积标记与检验都独立于 \(k,f\)。两侧可以有不同的检验与子搜集， 但二者具有相同的典范系数类。

设 \(\Omega_\Sigma\) 由 \[\omega=(C\ {\rm sf},d'\mid C,s\ {\rm sf},h'\ne0;
                      \text{所指定的槽素数})\] 组成，带有保留的各个支集与槽分支。它没有当前列指标。函数 \(t,k,f\) 是上面定义的乘积； 该集合可以在施加所展示的外零掩码之前取定，后者将出现在权重中。设 \(\mathcal A_\Sigma^{\rm init}(\omega)\) 为 \(\mathfrak d_0\) 的所有指定系数及其优先掩码的乘积， 在第二侧取共轭。剩余的完整外权重为 \[\label{eq:initial-outer-weight}
 \begin{split}
 V_\Sigma^{\rm init}(\omega;\boldsymbol\xi)={}&
 \mu(d')\mu(s)\widehat G(\vartheta)\mathcal B_{\rm init}(h')
 1_{(C,j)=1}1_{(s,Cj)=1}1_{(s,h')=1}
 \mathcal A_\Sigma^{\rm init}(\omega)\\
 &\times\psi_C(x_C)\psi_{d'}(x_d)\psi_s(x_s)\psi_{h'}(x_h)
 \omega_f(q_f/Z^{V_c^{\rm init}})\\
 &\times x_C^{i\xi_C}x_d^{i\xi_d}x_s^{i\xi_s}x_h^{i\xi_h}
 Z^{i\delta_{\rm init}(\xi_1+\xi_2)}.
 \end{split}\] 截断函数 \(\omega_f\) 在每个原标号乘积上等于一，因此其插入在分离之前是一个等式。每个 Möbius 因子有一份拷贝，射线系数也各有一份。特别地，\((s,h')\) 处的公共零点仍然存在。

设 \(\mathcal T_\Sigma^{\rm init}\) 为由方程 [\[eq:initial-formal-component\]](#eq:initial-formal-component) 通过完整的 Möbius 与优先展开得到的固定 \(s\)-二进块与槽被加项。其精确的分离恒等式为 \[\label{eq:initial-separated-identity}
 \begin{split}
 \mathcal T_\Sigma^{\rm init}={}&
 Z^{\kappa_c^{\rm init}+3\eta}(2\pi)^{-6}
 \int_{\mathbb R^6}
 \widehat{\mathfrak H}_{{\rm init},\Sigma,\boldsymbol\upsilon}
       (\boldsymbol\xi)\\
 &\quad\times\sum_{\omega\in\Omega_\Sigma}
 V_\Sigma^{\rm init}(\omega;\boldsymbol\xi)
 Q^{\rm init}_{1,t,j,\boldsymbol\xi}(k,f)
 \overline{Q^{\rm init}_{2,t,j,\boldsymbol\xi}(k,f)}
 \,d\boldsymbol\xi.
 \end{split}\] 确实 \(x_a=Z^{\delta_{\rm init}}z_{n_a}\)。两个列模式，连同方程 [\[eq:initial-outer-weight\]](#eq:initial-outer-weight) 的最后一个因子，恰为 \(x_1^{i\xi_1}x_2^{i\xi_2}\)，而其余四个模式为外侧的。Fourier 反演恢复 完整的剖面；其更大的截断函数在保留支集上等于一，而新列截断在旧的 \(W_0\) 窗口非零处等于一。 方程 [\[eq:initial-root-kernel\]](#eq:initial-root-kernel) 恢复完整的前因子与核。方程 [\[eq:initial-common-extraction\]](#eq:initial-common-extraction) 与优先展开逐项恢复每个算术因子。完整新窗口中的额外组合在此复恒等式中通过旧窗口在 Cauchy 之前相消。

方程 [\[eq:initial-separated-identity\]](#eq:initial-separated-identity) 中的变换是从固定环境剖面中选取的，先于任何实际 \(C,d',s,h'\) 的求值，因而也先于任何 \(t,k,f\) 的求值。它依赖于 \(\Sigma,Z\)、固定的检验， 以及较早的模式 \(\boldsymbol\upsilon\)，且可能依赖于已经冻结的 \(j\)，但不依赖于任何当前外 理想或重编号的行或标号。裸的 \(h'\) 范数是一个坐标；导出的行与标号只出现在外掩码或所展示的 特征中。关系 \(C=td'\) 仅限制求值点。由方程 [\[eq:inverse-fourier-moment\]](#eq:inverse-fourier-moment)，对每个固定的 \(J\)，存在固定的 \(L,b_0\) 使得 \[\int_{\mathbb R^6}
 |\widehat{\mathfrak H}_{{\rm init},\Sigma,\boldsymbol\upsilon}
       (\boldsymbol\xi)|(1+|\boldsymbol\xi|)^J\,d\boldsymbol\xi
 \ll (1+|\boldsymbol\upsilon|)^L,\qquad
 \int_{\mathbb R^{1+|I_0|}}|\widehat{\mathfrak H}_{{\rm ov},j}(\boldsymbol\upsilon)|
       (1+|\boldsymbol\upsilon|)^L\,d\boldsymbol\upsilon
 \ll p_{b_0}(W).\] 第一个界使用了固定的归一化根以及完整核对于每个正 \(A_{{\rm ker},{\rm init}}\) 的一致 Euler 界；\(W_0\) 只有多项式级的 \(\boldsymbol\upsilon\)-依赖性。第二个界在固定的 \(j\)-乘积区间 上一致。在需要时取更大的 \(L\)，也能控制较早的行空间 Minkowski 不等式。任何导数阶数都不 引入 \(Z\) 的幂。

方程 [\[eq:initial-separated-identity\]](#eq:initial-separated-identity) 现在把该分量表示为具有典范形状的多项式，其公共 Fourier 密度在当前外理想求值之前就已选定。剩下的工作是界定正纤维与源测度、由源见证验证子项的 容许性，并在引理 [\[lem:marked\]](#lem:marked) 中恢复归一化。

在确定用于子项的某个商之前，先在整个 \(\Omega_\Sigma\)（包括所有商 \(t\)）上应用 方程 [\[eq:weighted-cauchy\]](#eq:weighted-cauchy)。只有在此之后才取绝对权重。所保留的 \((s,C)=1\) 与 \(d'\mid C\) 使 \(f=d's\) 无平方因子，权重的所有其他因子都由一个固定常数界定。因此 \[|V_\Sigma^{\rm init}(\omega;\boldsymbol\xi)|
 \ll\mathcal B_{\rm init}(h')\mu^2(f).\] 对固定的 \(t,f,k\)，恒等式 \[d'\mid f,\qquad s=f/d',\qquad C=td',\qquad h'=k/d'
       \quad\text{若该商是一个元素}\] 表明该重构在槽之前至多有 \(d_{\mathcal O}(f)\) 种选择。这里 \(K_{\rm slot}\) 再次表示原槽数 的固定界。至多 \(2K_{\rm slot}\) 个所指定的残余素数整除 \(tf\)。它们的选取至多花费 \([d_{\mathcal O}(t)d_{\mathcal O}(f)]^{2K_{\rm slot}}\)。较早的重叠素数已经冻结，并在重叠 三角形中被计数。因此，即便纤维的实际大小依赖于 \(k\)，它也被下式界定： \[\label{eq:initial-fibre}
 D_{\rm init}(f)C_{\rm init}(t),\qquad
 D_{\rm init}(f)=d_{\mathcal O}(f)^{1+2K_{\rm slot}},\qquad
 C_{\rm init}(t)=d_{\mathcal O}(t)^{2K_{\rm slot}}.\] 不存在独立的 \(d',s\) 计数，也不存在第二个频率计数。

设 \(\Omega_\Sigma^{\rm src}\) 为刚才使用的结构性外集合，在独立的正行或标号加入之前， 并忽略单位 Fourier 相位，定义互异源商之集 \[\mathfrak T_\Sigma=\{t=C/d':\omega\in\Omega_\Sigma^{\rm src}\}.\] 它在所有当前行与标号上一次性投影得到，而不对固定的 \(k,f\) 重新定义。每个成员在 \(C,d'\) 二进块上都有一个源见证，因此 \(\log_Zq_t=\widehat B-\widehat\theta\le P_1+2\eta\)。所含的 范数球把它的基数界定为 \(\#\mathfrak T_\Sigma\ll Z^{P_1+2\eta+\pi_{{\rm count},{\rm init}}}\)；它不被用作替代的子 区域。在非空扇区中 \(P_1+2\eta\ge0\)，因为它界定了某个存在理想的范数。 在这一有界范围上的除数界给出归一化测度 \[\label{eq:initial-normalized-quotients}
 d\nu_\Sigma^{\rm init}(t)
 =Z^{-P_1-2\eta}\sum_{t\in\mathfrak T_\Sigma}C_{\rm init}(t)\delta_t,
 \qquad
 \|\nu_\Sigma^{\rm init}\|
 \ll Z^{\pi_{{\rm count},{\rm init}}+\pi_{{\rm fib},{\rm init}}}.\] 此集合与测度忽略单位 Fourier 相位，并对整个当前行与标号求和是公共的。非空关口与这一 结构投影保持分离。

对固定模式，令 \[\label{eq:initial-positive-child}
 \mathcal H_{a,t}^{\rm init}
 =\sum_{\substack{f\ {\rm sf}\\q_f/Z^{V_c^{\rm init}}\in I_f}}
 D_{\rm init}(f)\sum_{\substack{k\in\mathcal O\\0<q_k\le Z^{M_{\rm init}}}}
 |Q^{\rm init}_{a,t,j,\boldsymbol\xi}(k,f)|^2
 =Z^{F_{\rm init}}\mathcal E_{a,t}^{\rm init}.\] 这是具有相同行球的方程 [\[eq:canonical-energy\]](#eq:canonical-energy)；若取更大的固定典范球，该等式被相应的 上界取代。纤维估计与加权 Cauchy 给出 \[\label{eq:initial-weighted-count}
 \left|\sum_{\omega\in\Omega_\Sigma}V_\Sigma^{\rm init}Q_1\overline{Q_2}\right|
 \ll Z^{P_1+2\eta}
 \prod_{a=1}^2
 \left(\int_{\mathfrak T_\Sigma}\mathcal H_{a,t}^{\rm init}
                         \,d\nu_\Sigma^{\rm init}(t)\right)^{1/2}.\] 这里 \(Q_a=Q^{\rm init}_{a,t,j,\boldsymbol\xi}(k,f)\)。只有正的外 \(f,k\) 求和被放大到其 完整的固定窗口；内部的 \(\rho_{t,j}\)、标记与新检验保持不变。权重 \(D_{\rm init}\) 只依赖于 \(f\)。新的外球恰为 \(1_{0<q_k\le Z^{M_{\rm init}}}\)。因此使用一致子项界时，所展示的商计数 指数引入一次，归一化质量也引入一次。

固定的穿刺恰在 \(\operatorname{rad}(tj)\) 处。对每个 \(t\in\mathfrak T_\Sigma\)，其源界 与固定重叠界给出 \[\label{old-eq:4.13}
 Q_{\rm init}:=\log_Zq_{\mathfrak r_\rho}
 \le\widehat B-\widehat\theta+\widehat j\le P_1+G+3\eta.\] 共享的穿刺素数只会减小这个界。当加入正的新标号或行时它仍然成立，因为这些加入不改变 \(t,j\)，也不删除它们内部的穿刺。

固定的形式中心满足 \[\begin{aligned}
 F_c^{\rm init}-M_c^{\rm init}-(P_1+G)-z_0&=m-r-2z+2G,\\
 4F_c^{\rm init}-3M_c^{\rm init}-6z_0&=3m-2r-8z+10G+2P_1.
 \end{aligned}\] 利用带标记的前提、\(G\ge0\)、\(P_1\ge-2\eta\)、方程 [\[eq:inverse-initial-row\]](#eq:inverse-initial-row) 与 [\[old-eq:4.13\]](#old-eq:4.13)，以及有利的截断符号。实际的典范余量为 \[\label{eq:inverse-initial-margins}
 \begin{aligned}
 F_{\rm init}-M_{\rm init}-Q_{\rm init}-z_0
   &\ge c_1+\delta_{\rm init}-9\eta-\tau_{\rm init}
     \ge c_1-9\eta-\tau_{\rm init},\\
 4F_{\rm init}-3M_{\rm init}-6z_0
   &\ge c_2+4\delta_{\rm init}-22\eta-3\tau_{\rm init}
     \ge c_2-22\eta-3\tau_{\rm init}.
 \end{aligned}\] 其中的 \(22\eta\) 由可能为负的 \(2P_1\) 贡献的 \(4\eta\) 与行的包围三份拷贝贡献的 \(18\eta\) 组成。

还有一个显式的能量计算。仅对 \(t\in\mathfrak T_\Sigma\) 应用典范界，因为在那里前面的穿刺 与余量检查成立。方程 [\[eq:initial-positive-child\]](#eq:initial-positive-child) 与 [\[eq:initial-weighted-count\]](#eq:initial-weighted-count) 于是把未缩放的带符号外和界定为 \[C(\boldsymbol\upsilon,\boldsymbol\xi)
 Z^{P_1+2\eta+2F_{\rm init}+\epsilon_c}
 \|\nu_\Sigma^{\rm init}\|.\] 那一个质量是方程 [\[eq:initial-normalized-quotients\]](#eq:initial-normalized-quotients) 的质量；标号 \(d's\) 仍留在 子平均之中。公共 Fourier 密度用上面的统一加权界单独积分一次。这把互异的冻结商计数一次， 其见证重数已经包含在纤维权重中。 形式恒等式 \[\kappa_c^{\rm init}+P_1+2F_c^{\rm init}=m\] 在恢复子归一化并应用带损失 \(\epsilon_c\) 的典范界之后给出每侧的指数 \[\label{eq:inverse-initial-energy}
 \begin{split}
 &m+3\eta+2\eta+2\delta_{\rm init}+\pi_{\rm init}+\epsilon_c\\
 &\qquad\le m+11\eta+\pi_{\rm init}+\epsilon_c.
 \end{split}\] 这里 \(\pi_{\rm init}\) 是自由选取的局部分歧、二进与分离损失的合计，包括所指定重叠的 分歧损失与互异分配 \(\pi_{{\rm count},{\rm init}},\pi_{{\rm fib},{\rm init}}\)。它们是一个合计 的各部分，而不是重复的容许量。两份截断拷贝来自恢复的归一化和子指数。不存在 \(\tau_{\rm init}\) 能量因子：行的放大发生在典范子项内部，并在其余量检验中被计入。初始加权 Cauchy 取几何平均， 且重叠三角形已由 \(Z^{-G}\) 相消。

我们明确给出参数与尾部的阶。设 \(r_{\max},z_{\max},m_{\max}\) 界定带标记的范围，设 \(s_{\rm slot}\) 界定槽数，并置 \(D_{\max}=r_{\max}+z_{\max}\)。置 \(\bar c=\min(c_1,c_2)\) 并选取典范余量 \(c_*=\bar c/2\)。对 \(\eta,\tau_{\rm init}\le1/100\)，适用于该应用的先验有效 起始界为 \[M_{\max}=2D_{\max}+1,\qquad N_{\max}=V_{\max}=D_{\max}+1.\] 确实，\(P_1\ge-2\eta\) 给出 \(M_{\rm init}\le2D_{\max}+10\eta+\tau_{\rm init}\)，而 \(F_{\rm init}\le D_{\max}+5\eta\) 界定了两个非负的子参数。在方程 [\[eq:inverse-parameter-order\]](#eq:inverse-parameter-order) 中以 \(\epsilon_c=\epsilon/2\) 作出选择，并额外施加 \[\eta,\tau_{\rm init}\le\bar c/100,\qquad
 \eta\le\epsilon/88,\qquad \pi_{\rm init}\le\epsilon/8.\] 在施加这两组界之后，可以取 \(\tau_{\rm init}=\tau\)。方程 [\[eq:inverse-initial-margins\]](#eq:inverse-initial-margins) 于是给出两个余量至少为 \(3\bar c/4>c_*\)，因此引理 [\[lem:canonical-moment\]](#lem:canonical-moment) 适用。方程  [\[eq:inverse-initial-energy\]](#eq:inverse-initial-energy) 至多给其 \(\epsilon_c=\epsilon/2\) 损失增加 \(\epsilon/4\)。

在这些有界初始范围固定之后，选取能实现目标 \(\pi_{\rm init}\) 的辅助输入指数，然后再选取 初始尾部与 Fourier 高度的阶。

对于独立的初始原始尾部，受支持的列满足 \(q_{c_i}\le C Z^{D_{\max}}\)，而 \(D'\in[-z_{\max},D_{\max}]\)。在真正的初始展开上置 \(a=Z^m/(q_{d'}q_{z_1z_2})\)。由于 \(m\ge0\)、\(d'\mid C\) 且 \(c_i=Cz_i\)， \[a^{-1}\le q_{d'}q_{z_1z_2}
       \le q_{c_1}q_{c_2}/q_C\le C Z^{2D_{\max}}.\] 显式的粗略指数 \[B_{\rm crude,init}=10\{1+m_{\max}+(s_{\rm slot}+1)(D_{\max}+1)\}\] 即使没有相消也界定了所有原始的非频率因子。为验证这一点，归一化至多花费 \(z_{\max}\)， 两个列计数花费 \(2D_{\max}\)，\(d'\)-除数计数至多 \(D_{\max}\)，而 \(1+a^{-1}\) 至多 \(2D_{\max}\)。两个残余标记至多花费 \(2s_{\rm slot}D_{\max}\)，用到 \(d_{\mathcal O}(c)^{s_{\rm slot}}\le q_c^{s_{\rm slot}}\)。即便在计入重叠对及其所指定系数 而不计其相消权重时，也至多花费 \(2z_{\max}+2s_{\rm slot}z_{\max}\)。Poisson 前因子至多花费 \(m_{\max}\)。其和至多为 \(m_{\max}+(8+4s_{\rm slot})D_{\max}<B_{\rm crude,init}\)。

选择 \(T_{\rm init}>1+B_{\rm crude,init}\)，然后 \[A_{\rm init}>1+(B_{\rm crude,init}+T_{\rm init})/\tau_{\rm init}.\] 方程 [\[eq:inverse-raw-tail\]](#eq:inverse-raw-tail) 使原始 \(\mathcal B_{\rm init}=0\) 补集为 \(O(Z^{-T_{\rm init}})\)，其中 半范数与多项式高度因子固定。该阶数在 带标记区间与 \(\tau_{\rm init}\) 之后选取，但在初始 Fourier 高度阶数之前、最终 \(Z\) 阈值之前选取。若 \(\tau_{\rm init}=\tau\)，则取这个 单独的粗略界与规范尾部所要求的阶数之最大值。外球内保留的 完整核具有在规范分离中已使用的统一 Euler 界。最终阈值还强制 \(\mathcal I_D\) 中完整的初始支撑 比。

主计数具有指数 \(m\)，每个非主项现在 已被 \(Z^{m+\epsilon}\) 界定。该论证保留所有元素 行与每个原始掩码，适用于子集以及任一公共 定向，并保持任意有界且行无关的素 系数。公共分离测度给出所述的有限 半范数与多项式高度一致性。这证明了 方程 [\[old-eq:4.1\]](#old-eq:4.1)。

#### 无六次幂因子行上的放大

我们首先在所有元素行上提取一个无标记的推论。在 引理 [\[lem:marked\]](#lem:marked) 中，取 \(Z=H,\ m=1\)、无槽位，且 \(r=\log_H D\)。若对某个固定 \(c>0\) 有 \(H\ge D^{1+c}\)，则 \(1-r\ge c/(1+c)\)；第二个所需余量也为正。 对 \(D\le H^{\epsilon/4}\)，直接界 \(|M_u(D;W)|^2\ll D\) 已足够。否则起始长度 位于一个远离零的固定有界区间内。有界的 \(H,D\) 直接处理。对 \(H,D\ge1\)，我们得到 \[\label{eq:raw-moment}
 \sum_{\substack{u\in\mathcal O\\0<q_u\le H}}
 \left|D^{-1/2}\sum_n\mu(n)\nu(n)\chi_n(u)^{\varepsilon_\chi}
                         W(q_n/D)\right|^2
 \ll_{c,\epsilon,W} H(HD)^\epsilon,\qquad H\ge D^{1+c}.\] 固定的算术数据与所述的半范数包含在 常数的依赖关系中。

<span id="lem:inverse-amplification" label="lem:inverse-amplification">\[lem:inverse-amplification\]</span> 设 \(\nu,W,\varepsilon_\chi\) 与零延拓如 引理 [\[lem:marked\]](#lem:marked) 所述，无素槽位。设 \(U,D\ge1\)，并对满足 \(q_u\asymp U\)、且理想 \((u)\) 的每个素 赋值至多为五的元素 \(u\) 求和。对每个固定的 \(c>0\) 与 \(\epsilon>0\)，置 \[H=\max(2U,D^{1+c}),\qquad P=(H/U)^{1/6}.\] 则 \[\label{eq:amplified-note}
 \sum_u|M_u(D;W)|^2
 \ll \frac HP(UD)^\epsilon
 \ll \max\{U,U^{1/6}D^{5(1+c)/6}\}(UD)^\epsilon.\] 隐含常数只依赖于 \(c,\epsilon\)、固定的 算术数据以及 \(W\) 的有限多个半范数。特别地， 对 \(D=U^r\)，其中 \(r\) 属于一个固定有界非负区间，对 每个 \(\epsilon>0\)，指数可写为 \[\sum_u|M_u(U^r;W)|^2\ll U^{e(r)+\epsilon},
 \qquad e(r)=\max\{1,(1+5r)/6\}.\] 两个断言都允许在每一行中使用单独的检验函数 \(W_{\sigma_u,t_u}(y)=W(y)y^{-\sigma_u+it_u}\)，其中 \(\sigma_u\) 位于一个固定紧区间、\(|t_u|\le T_1\)， 代价为 \((1+T_1)^A\)，\(A\) 固定。

首先，方程 [\[eq:raw-moment\]](#eq:raw-moment) 与 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 蕴含逐行尺度界 \[\label{eq:inverse-scale-supremum}
 \sum_{\substack{v\in\mathcal O\\0<q_v\le C H}}
       \sup_{0<D'\le D}|M_v(D';W)|^2
 \ll H(HD)^\epsilon,\qquad H\ge\max(2,D^{1+c}).\] 事实上，足够小的尺度在环形 支撑内没有理想。关于 \(\log D'\) 的求导将 \(W(y)\) 替换为 \(-W(y)/2-yW'(y)\)。引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中的 一维 Sobolev 不等式，继之以对这两个检验函数使用的 方程 [\[eq:raw-moment\]](#eq:raw-moment)，控制了 单位对数区间上的上确界。这样的区间有 \(O(\log(2+D))\) 个。对 \(H\) 的一个固定放大 处理它们的端点，直接的小尺度界处理 初始区间。这证明了 方程 [\[eq:inverse-scale-supremum\]](#eq:inverse-scale-supremum)。

在固定集合 \(S\) 之外的理想计数给出至少 \(c_S P\) 个 满足 \(q_a\le P\) 的主理想 \(a\)，其中固定的 \(c_S>0\)。 对有界的 \(P\)，这可在缩小 \(c_S\) 之后得到，因为 单位理想可用；对大的 \(P\)，它由去掉有限多个素数后的 正密度理想计数得到。

对无平方因子的 \(n\)，通过 \(n=dm\) 分离整除 \(a\) 的素数，其中 \(d\mid\operatorname{rad}a\) 且 \((m,a)=1\)。 借助零延拓， \[\psi_{ua^6}(m)=\psi_u(m)1_{(m,a)=1}.\] 当 \(u,a\) 共享素数时这也成立：两侧在 整除 \(m\) 且整除 \(u\) 或 \(a\) 的素数处同时为零，否则 六次幂为一。因此分离后的列给出 恒等式 \[\label{eq:sixth-power-column-identity}
 M_u(D;W)=\sum_{d\mid\operatorname{rad}a}
       \mu(d)\psi_u(d)q_d^{-1/2}M_{ua^6}(D/q_d;W).\] 系数质量至多为 \(d_{\mathcal O}(a)\ll_\delta P^\delta\)。 由此 \[|M_u(D;W)|^2\ll_\delta
 P^{2\delta}\sup_{0<D'\le D}|M_{ua^6}(D';W)|^2.\]

对这些 \(a\) 平均该界并对 \(u\) 求和。映射 \((u,a)\mapsto ua^6\) 在这些对上单射。事实上，在 每个素数处，模六的赋值恢复 无六次幂因子理想 \((u)\) 的赋值，而它除以六的商 恢复 \(a\) 的赋值。\(a\) 的主生成元 随后确定元素 \(u\)，包括其单位。该论证 不要求 \((u,a)=1\)。又 \(q_{ua^6}\ll UP^6\ll H\)。因此 方程 [\[eq:inverse-scale-supremum\]](#eq:inverse-scale-supremum) 给出 \[\sum_u|M_u(D;W)|^2
 \ll \frac HP(UD)^\epsilon
 =U^{1/6}H^{5/6}(UD)^\epsilon,\] 只要预先选取的 \(\delta\) 与幂次损失足够小。由于 \(H=\max(2U,D^{1+c})\)，这就是 方程 [\[eq:amplified-note\]](#eq:amplified-note)。对有界的 \(r\)，选取 \(c>0\) 充分小，其依据是 \(r\) 的界与 所需的幂次损失；所述的 \(e(r)\) 公式随之成立。

最后，在固定环形支撑上，\(W_{\sigma,t}\) 关于 \(\sigma,t\) 的 导数插入 \(\log y\) 的有界幂。在 \(\sigma\) 上的一个 有界覆盖与 \(t\) 中 \(O(1+T_1)\) 个单位区间上应用 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中的参数 Sobolev 不等式， 在积分导数之前先对行矩求和。已经证明的有限半范数界 具有固定的多项式高度阶数。该覆盖与 这些导数因而给出因子 \((1+T_1)^A\)，其中 \(A\) 固定，且对每一行中单独的 \((\sigma_u,t_u)\) 一致成立。 同样的论证适用于带标记估计，其中检验参数为任意 固定有限个数，而其素系数 在各行间保持固定。

在后续应用中，\(T_1=Z^{\tau_\eta}\) 中的正指数 在固定阶数 \(A\) 之后选取。 因此它可取得足够小，以适配预留的幂次 损失。这种使用逐行检验参数的做法不允许任意 依赖于行的素系数。

### 带短素因子的四阶矩

精细化的行计数需要对两个普通 特征多项式之积与短素多项式之积给出一个四阶矩估计。我们在此 证明该估计。当没有素多项式时，两个普通多项式无长度限制； 否则允许的长度位于 一个仿射区域中。两个有限 Fourier 变换在较小的有效宽度下返回 同类乘积。然而某些变换后的行 诱导出一个固定 有限族中的特征。它们的普通乘积可以有体积量级的主项。 因此对较长的输入，我们减去一个与之有相同 尺度乘积的比较乘积。通过变换保持其公共特征、掩码与范数 幂，使那些主项相消。该估计 本身针对原始的、未中心化的乘积。

我们使用节 [2](#sec:arithmetic) 的记号与节 [2](#sec:additional-arithmetic) 的 系数约定。特别地， 各行为元素 \(k\in\mathcal O\)，其中 \(0<q_k\ll Z^m\)，且 \[\psi_k(n)=\tau(n)\chi_n(k),\qquad M=m+q.\] 特征 \(\tau\) 在行和内部固定。其所有展示的移动剩余符号因子的 素支撑，在约去因子或将指数模六约简之前的并集， 范数至多 为 \(Z^q\)。每个展示的因子都保留其零延拓， 包括被约去或被六整除的因子。冗余的零 只有在精确 因式分解保留每个存活的局部与固定射线相位时，才可用一个额外的穿孔掩码表示。该 掩码是与一个范数至多 为 \(Z^B\) 的无平方因子理想互素的指示函数，其中 \(B\) 有界，在当前行和内固定； 同一掩码用于两个普通因子以及每个素因子。 它可依赖于先前冻结的标记，但不依赖于变化中的行。 多项式中的所有理想都在固定集合 \(\mathcal S\) 之外。

固定一个由有限阶射线特征组成的有限群 \(\Theta\)，其 导子素数属于 \(\mathcal S\)。它包含固定的 扭以及用于分离固定互反 相位的所有特征。因此它亦包含补充特征 \(n\mapsto\chi_n(-1)\)：由 方程 [\[eq:fixed-gauss-phases\]](#eq:fixed-gauss-phases) 与固定的双特征 表，该特征为对角特征 \(n\mapsto\mathcal R(n,n)\)。一个诱导特征属于 \(\Theta\) 意味着它等于 \(\Theta\) 某个成员的 本原诱导特征，而非所选零延拓 表示相等。那些表示的所有零仍留在多项式中。 设 \(\mathcal R_0\) 为使 \(\psi_k\) 诱导非主特征的行。对 \(z>0\)，设 \(\mathcal R_z\) 为使 \(\psi_k\) 的诱导特征 不属于 \(\Theta\) 的行。记 \[A=n_1+n_2+z.
 \label{old-eq:3.1}\]

<span id="lem:plain" label="lem:plain">\[lem:plain\]</span> 设 \(3/4\le\kappa\le1\)。设 \(n_1,n_2\ge0\)，并设 \(Q=\prod_{i\in\mathcal I}Q_{\psi_k,i}\) 为方程 [\[old-eq:1.2\]](#old-eq:1.2) 中 素多项式的一个有限乘积，长度为 \(z_i\ge0\)，总长度为 \(z=\sum_{i\in\mathcal I}z_i\)。 它们的底层素支撑在施加公共 掩码与行零延拓之前两两不交。它们的系数是 有限射线特征的固定有限线性组合。对每个 正长度槽位，其展开具有形式 \[\nu_i(n)=\sum_{j=1}^{J_i}c_{ij}\vartheta_{ij}(n),
 \qquad\vartheta_{ij}\in\Theta,\] 其中该有限列表及其系数独立于 \(Z\) 与行而固定。行与掩码假设即为刚刚所述的。

对每个 \(\epsilon>0\)，存在槽位网格 \(\eta>0\)，使得 若对每个 \(i\) 有 \(z_i\le\eta\)，则 \[\sum_{k\in\mathcal R_z}
 \left|S_{\psi_k}(n_1;W_1)S_{\psi_k}(n_2;W_2)Q\right|^2
 \ll Z^{M+\epsilon}
 \label{old-eq:2.1}\] 在以下任一情形下成立：

1.  \(z=0\)。对有限非负 长度 \(n_1,n_2\) 无限制，对导子也无下界。

2.  \(z>0\) 且 \[n_1+n_2+6\kappa z=A+(6\kappa-1)z\le M.
     \label{old-eq:3.9}\] 若 \(\kappa<1\)，另外假设 \(\beta_*\le(1+\kappa)/2\)。若 \(\kappa=1\)，则无需 无零点假设。

对空槽位列表，\(Q=1\)。若 \(z=0\) 且列表包含 零长度槽位，则它们的尺度有界，绝对计数 将它们吸收进常数；因此零槽位断言 具有同样的强度。所有实长度参数在给定的有界 集合中取值。网格只依赖于这些集合与 \(\epsilon\)，对 \(\kappa\in[3/4,1]\) 一致成立。对每个固定的与 \(Z\) 无关的算术 数据 \(\mathcal A\) 与固定槽位数，该界使用有限多个 光滑半范数以及分离范数扭 高度中的一个固定多项式。它们的阶数以及该界本身，对所述范围内的 所有移动模、容许掩码与冻结外标记 一致成立。

对 \(7/8\) 界的应用取 \(\kappa=2\beta_*-1\)，故 本引理中的无零点假设以等号成立。我们保留这个 动态值，而不将它替换为 \(11/12\) 界提供的值 \(5/6\)， 因为精细化的行计数使用由此得到的仿射 容量。下面的证明使用 节 [2.3](#sec:finite-correlations) 的有限 Gauss 恒等式、 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 与引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control)。 在其有界尺度上通过绝对计数吸收任何零长度槽位； 此后 \(z=0\) 表示没有存活槽位剩余。我们首先 作两个保持行族的化归。

后续的归纳针对有效宽度 \(M=m+q\)，其中所有零槽位 带在正槽位带之前完成。在每个带内先证明区间 \(A\le5M/6\)。这个阈值来自那些 诱导特征属于 \(\Theta\) 的变换后的行：计数 它们的六次幂形式并 用体积界定它们的普通乘积，在公共支撑节省之前留下超额 \(A-5M/6\)。反射处理 某些较长的输入；其余的化归为等乘积尺度 差，其相消去除了该超额。

#### 固定掩码与反射

当一个特征的零恰好由它的 本原导子素数、它的冗余行根与所声明的移动 根素数以及 \(\mathcal S\) 中的固定素数组成时，称它是*自然的*。这里 冗余素数是使诱导特征非分歧、 但展示的零延拓乘积仍为零的素数。展示的 被六整除的幂在非单位元上仍为零。若固定扭的一个冗余因子 未包含在所声明的移动根中， 则先将它精确分解为其剩余相位与一个互素 指示函数，并把该指示函数放入一个无平方因子理想 \(\mathfrak R\)，其中 \(q_{\mathfrak R}\le Z^B\)，在整个 行和内固定。特别地，固定扭 与变化因子 \(\chi_n(k)\) 之间的相消不会被重新归类为 每一行单独选取的额外穿孔。

设 \(\psi_k^0\) 为删去这些 额外穿孔后所得的自然特征，并设 \(T_k(X)\) 表示其在尺度 \(X\) 处的中心 正规化普通和。记 \(S_{k,\mathfrak R}(X)\) 为带额外掩码的和。乘性，包括零 延拓，给出恒等式 \[\begin{aligned}
 S_{k,\mathfrak R}(X)
 &=\sum_{d\mid\mathfrak R}\mu(d)\psi_k^0(d)q_d^{-1/2}
                  T_k(X/q_d),
 \label{old-eq:2.1a}\\
 Q_{k,i,\mathfrak R}
 &=Q_{k,i}^{\,0}
   -P_i^{-1/2}\sum_{\substack{p\mid\mathfrak R\\p\ {\rm prime}}}
       \psi_k^0(p)\nu_i(p)W_i^{\rm slot}(q_p/P_i),
 \qquad P_i=Z^{z_i}.
 \label{eq:prime-mask-erasure}\end{aligned}\] 例如，第一个恒等式可由代入 \(\sum_{d\mid(n,\mathfrak R)}\mu(d)\) 并记 \(n=dl\) 得到。 商 \(l\) 在 \(d\) 的素数处不受限制；其上保留着原来的 自然零延拓。

将这些恒等式同时应用于两个普通因子与所有 槽位。若冻结槽位构成 \(J\subseteq\mathcal I\)，普通 除数为 \(d_1,d_2\)，则依赖于行的标量其 模至多为一。剩余系数之绝对值至多 为一个固定剖面常数乘以 \[q_{d_1d_2}^{-1/2}\prod_{i\in J}P_i^{-1/2}.\] 所得自然乘积的长度为 \[A'=A-\log_Zq_{d_1d_2}-\sum_{i\in J}z_i,\qquad
 z'=z-\sum_{i\in J}z_i.\] 其诱导特征不变。若 \(z'>0\)，则 方程 [\[old-eq:3.9\]](#old-eq:3.9) 的左侧已减小；若 \(z'=0\)，则零槽位 断言无长度限制，且 \(\mathcal R_z\subseteq\mathcal R_0\)。

对每个固定的 \(\epsilon_1>0\)， \[\sum_{d\mid\mathfrak R}q_d^{-1/2}
 \le \prod_{p\mid\mathfrak R}(1-q_p^{-1/2})^{-1}
 \ll_{\epsilon_1,B} Z^{\epsilon_1}.
 \label{old-eq:2.1b}\] 这由引理 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors) 得到。冻结槽位对应的 质量也是 \(Z^{\epsilon_1}\)：在其环形支撑上， \(P_i^{-1/2}\ll q_p^{-1/2}\)，同一个乘积界定对 \(p\mid\mathfrak R\) 的求和。槽位数固定。Minkowski 不等式因此将方程 [\[old-eq:2.1\]](#old-eq:2.1) 化归为 同一宽度下的自然断言，代价为任意小的幂次 损失。低于一的非空环形尺度有一个 正且依赖于剖面的下界，并可重新标度为一。 在这次重新标度之后，其新的非负长度为 \(\max\{n_i-\log_Zq_{d_i},0\}\le n_i\)，故所断言的 仿射表达式不增仍然成立。

我们接着精确记录用于自然特征的反射。 设 \(\psi_k^*\) 为诱导 \(\psi_k^0\) 的本原特征， 并设 \(\mathfrak R_{0,k}\) 为其冗余自然根。 \(\mathfrak R_{0,k}\) 的素数与本原 导子不交。若 \(Q_k\) 为该导子范数，置 \(C_k=3Q_k/(2\pi)^2\)，即函数 方程中的导子尺度。\(\mathcal S\) 之外素数处的驯顺性给出 \[C_kq_{\mathfrak R_{0,k}}
 \ll_{\mathcal S,\tau_{\rm fixed}} Z^M.
 \label{old-eq:2.1c}\] 事实上，每个好的素数至多贡献一次，或贡献给 本原导子，或贡献给冗余根。它们的并 包含在行根与所声明的移动 根之并中，其范数至多为 \(q_kZ^q\)。由 引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray)，一行的单位部分与 \(\mathcal S\) 支撑部分，当在主且与 \(\mathcal S\) 互素的元素上求值时若赋值模六约简， 则取值于一个固定有限射线 族。因此 \(\mathcal S\) 中所有素数只贡献一个固定 因子。

将引理 [\[lem:hecke-strip-growth\]](#lem:hecke-strip-growth) 的证明中所记录的本原 Hecke 函数方程 应用于 \(\psi_k^*\)，利用其中所述的 \(L(s,\psi_k^*)\) 的整性。设 \(\varepsilon_k\) 为其根数， 故 \(|\varepsilon_k|=1\)。Mellin 反演与一次围道移动表明 \(\psi_k^*\) 在 \(X\) 处的正规化普通和等于根数乘以 \(C_k/X\) 处的共轭 特征和，其变换后的剖面 \(W^\sharp\) 由下式定义 \[\mathcal M W^\sharp(s)
 =\mathcal M W(1-s)\frac{\Gamma(s)}{\Gamma(1-s)}.\] Mellin 变换约定采用 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中的约定。伽马函数之商只在 非正整数处有极点、在正整数处有零点。将反 Mellin 围道向左移动给出 在零处的非负整数幂展开；向右移动给出 在无穷处的任意衰减。因此 \(W^\sharp\) 及其 Euler 导数在零处有界且在 无穷处快速递减。高度断言也是定量的。对 \(W_\omega(y)=W(y)y^{i\omega}\)，恒等式 \(\mathcal M W_\omega(s)=\mathcal M W(s+i\omega)\) 将所有 高度依赖性放入快速递减 Mellin 变换的一个平移中。在每条固定竖直线上，伽马之商与 每个固定数目的 Euler 导数在 积分高度上具有多项式增长。因此对平移后的 Mellin 衰减 积分给出 \(1+|\omega|\) 的一个固定多项式，其 次数只依赖于固定围道与导数阶数。 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中在紧实带形域上的逐点 Mellin 分部积分估计 保证这些移动中的水平 连接；并不使用积分后的 Fourier 尾部来 界定固定的水平迹。这证明了反射所需的 有限半范数与多项式高度界。

在反射之前删去冗余 Euler 因子并在之后以 几何方式恢复它们，给出 \[T_k(X;W)
 =\varepsilon_k
 \sum_{\substack{d_0\mid\mathfrak R_{0,k}\\
                  \operatorname{rad}(h_0)\mid\mathfrak R_{0,k}}}
 \frac{\mu(d_0)\psi_k^*(d_0)\overline{\psi_k^*(h_0)}}
      {\sqrt{q_{d_0}q_{h_0}}}\,
 T_{\overline{\psi_k^0}}
   \left(\frac{C_kq_{d_0}}{Xq_{h_0}};W^\sharp\right),
 \qquad |\varepsilon_k|=1.\] 该几何级数被 \(\prod_{p\mid\mathfrak R_{0,k}}(1-q_p^{-1/2})^{-1}\) 绝对界定。 因此其总系数质量，连同 \(d_0\) 求和，为 \(Z^{\epsilon_1}\)。各尺度为 \[Y=\frac{C_kq_{d_0}}{Xq_{h_0}},\qquad
 d_0\mid\mathfrak R_{0,k},\quad
 \operatorname{rad}(h_0)\mid\mathfrak R_{0,k}.
 \label{old-eq:2.1d}\] 由方程 [\[old-eq:2.1c\]](#old-eq:2.1c)，存在固定的 \(C_{\mathcal A}\ge1\) 使得 \[C_kq_{\mathfrak R_{0,k}}\le C_{\mathcal A}Z^M,\qquad
 Y\le C_{\mathcal A}Z^{M-\log_ZX}.\]

剖面 \(W^\sharp\) 可划分为光滑环带。 在其主尺度之下，中心正规化在相对尺度为 \(2^{-j}\) 的环带上 给出可和系数 \(O(2^{-j/2})\)。 在该尺度之上，快速衰减给出任意可和的幂。 固定一个小长度容差 \(\xi>0\)。在上方环带经过 放大 \(Z^{\xi/2}\) 后截断；足够多的固定导数 通过绝对计数使被略去的部分可忽略。主尺度 低于 \(Z^{-\xi}\) 者同样可忽略。若某个保留的环带 剖面具有固定的上支撑端点 \(B\)，则能 包含非零整理想的尺度 \(S\) 满足 \(SB\ge1\)。在这样的 尺度上， \[\max(S,1)\le\max(1,B)S.\] 因此将一个保留的次单位尺度替换为尺度一，代价为这个固定 乘性因子。所有这些断言对移动标记都一致成立。

依赖于行的选择 \(d_0,h_0\) 由其系数 质量处理，随后在所得到的尺度上取逐行上确界。 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 使用 \(O((\log Z)^2)\) 个单位盒 与剖面的导数，界定两个 多项式范围尺度上的上确界。行特征及其自然零 保持不变：反射之后，在该整个因子的绝对值内部 取其共轭，将共轭特征替换为 原特征并共轭其剖面。该操作 有效，因为乘积的绝对值在 共轭一个因子时不变。

设 \(C_{\rm ref}\ge1\) 包含 \(C_{\mathcal A}\)、固定的环形 端点乘子、一个反射因子与任何配对未反射因子的 对数盒乘子，以及保留剖面类型的 \(\max(1,B)\)。 该常数在数据与剖面类型确定之后固定，独立于 \(Z\) 与移动标记。对 \(n=\log_ZX\)，每个满足前述支撑 检验的保留尺度，在允许的裁剪与盒放大之后，其声明的 非负长度为 \[n_{\rm ref}\le M-n+\frac\xi2+\frac{\log C_{\rm ref}}{\log Z}
 \le M-n+\xi
 \qquad\left(\frac{\log C_{\rm ref}}{\log Z}\le\frac\xi2\right).
 \label{eq:centered-reflection-length}\] 当 \(M-n\) 略微为负时这也是一个线性界；若其 右侧为负，则不存在这样的保留尺度。较小的 上方环带范围只改变用于被丢弃尾部的固定衰减、半范数与高度 阶数。

对 \(z=0\)，将每个长度超过 \(M/2\) 的原始因子 反射一次，另一个因子保持不变。方程 [\[eq:centered-reflection-length\]](#eq:centered-reflection-length) 界定每个保留的反射因子；未反射因子的固定盒乘子 包含在 \(C_{\rm ref}\) 中。在前述 环形截断与尺度盒放大之后，所得长度 满足 \[n_i^*\le M/2+\xi,\qquad
 A^*=n_1^*+n_2^*\le M+2\xi\le M+\delta,
 \label{old-eq:2.1h}\] 只要 \(2\xi\le\delta\)。我们称其为带衬垫的零槽位核心。 这里 \(\delta\) 是在 宽度下界与步长之后于下文选取的正衬垫参数。 在边界 \(M/2\) 处没有重复反射。反射 与尺度上确界在中心化之前取；对更晚的、其本原诱导特征 位于 \(\Theta\) 之外的已中心化项，先 对其两个矩形应用三角不等式。对 本原诱导特征属于 \(\Theta\) 的中心化差，不应用这样的上确界。

#### 素估计与归纳次序

对 \(\kappa<1\)，置 \(s_\kappa=(1+\kappa)/2\)。在假设 \(s_\kappa\ge\beta_*\) 下，引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control) 的 全局部分给出，对每个固定的 \(e>0\)， \[\frac{L'}{L}(s_\kappa+e+it,\psi)
 \ll_e \log\!\bigl(2Q_\psi(3+|t|)^2\bigr)
 \label{old-eq:3.4}\] 其中 \(\psi\) 为本原非主诱导特征。 为估计尺度为 \(P\) 的素环带，对 一个光滑 von Mangoldt 和作 Mellin 反演并将其围道移到 \(\Re s=s_\kappa+e\)。移动区域内没有极点， 且 Mellin 变换具有任意衰减，故 方程 [\[old-eq:3.4\]](#old-eq:3.4) 将新积分界定为 \(P^{s_\kappa+e}\) 乘以导子的一个对数与 高度的一个固定多项式。指数至少为二的素幂 贡献 \(O(P^{1/2+\epsilon_1})\)。对大的 \(P\)，将 环形权除以 \(\log(Py)\) 便将 von Mangoldt 权替换为 素权；其光滑半范数在环带有界。 有界的 \(P\) 由绝对计数估计。将每个 正长度系数按命题中的特征 \(\vartheta_{ij}\) 展开。若本原诱导行特征 \(\psi\notin\Theta\) 使 \(\psi\vartheta_{ij}\) 为主，则 \(\psi=\vartheta_{ij}^{-1}\in\Theta\)，矛盾。故 所得每个槽位特征在 \(\mathcal R_z\) 上都是非主的。

在抹去额外掩码之后，固定一个正槽位列表并置 \(\boldsymbol W=(W_i^{\rm slot})_{i\in\mathcal I}\)。对正规化 扭高度 \(\boldsymbol\omega=(\omega_i)_{i\in\mathcal I}\)，定义 \[Q_{\boldsymbol\omega}
 =\prod_{i\in\mathcal I}\left\{P_i^{-1/2}
   \sum_{p\ {\rm prime}}\psi_k^0(p)\nu_i(p)W_i^{\rm slot}(q_p/P_i)
                       (q_p/P_i)^{i\omega_i}\right\}.\] 对每个 \(\epsilon_1>0\)，中心正规化与在这个 固定列表上的乘法，在 \(e\) 与所有附属损失足够小时， 给出有限的 \(j,b,h\ge0\) 与一个常数 \(C\)，使得 \[|Q_{\boldsymbol\omega}|^2
 \le C Z^{\kappa z+\epsilon_1}p_j(\boldsymbol W)^b
                 (1+|\boldsymbol\omega|)^h
 \qquad(k\in\mathcal R_z,\ z>0).
 \label{old-eq:3.5}\] 这里 \(j\) 可向上取整为一个整数，且 \(2s_\kappa-1=\kappa\)。 各阶数与 \(C\) 可依赖于固定数据、槽位数、损失 以及任何固定的所要求内部对数或正规化扭 导数，但不依赖于 \(Z\)、移动标记、行或数值 高度。指数 \(\kappa z+\epsilon_1\) 独立于 这些导数与高度阶数。事实上，在分部积分之前将每个纯扭 在其 Mellin 变量中平移。未扭 Mellin 变换的加权 积分随后贡献一个有限 半范数与 \(\boldsymbol\omega\) 中的一个固定多项式，而 围道位移对平方指数恰好贡献 \(2ez\)。 对数导数保持环形，正规化扭 导数只插入对数剖面变量的幂。 冗余自然根只包含 \(O(\log Z)\) 个素数，故删去它使一个正规化槽位 改变 \(O(P_i^{-1/2}\log Z)\) 乘以其固定剖面因子；这 在所声明的幂次损失之内，因为 \(P_i\ge1\)。对 \(\kappa=1\)， 绝对素计数给出方程 [\[old-eq:3.5\]](#old-eq:3.5)，无需 无零点假设，且对未微分的纯扭有 \(h=0\)， 其模为一。对 \(\kappa<1\)，假设仍为 \(\beta_*\le(1+\kappa)/2\)。损失的选择对 \(\kappa\in[3/4,1]\) 一致，因为长度区间有界。在 方程 [\[old-eq:3.5\]](#old-eq:3.5) 的每一次后续使用中，其固定半范数与高度 因子保留在加权 Fourier 估计中；它不被包含 在 \(Z\) 的指数中。

现在我们来具体说明该归纳法，包括在其最小宽度处的估计。选取一个宽度下限 \(\rho>0\)、一个宽度步长 \(\sigma>0\)， 然后取 \(\delta>0\)，它们相对于最终的 \(\epsilon\) 都很小，且 \(\delta\ll\min(\rho,\sigma)\)。精确的损失 选取将在深度被界定之后进行。将 \(M\) 的有界 范围划分为长度为 \(\sigma/4\) 的连续带。 首先按宽度递增的顺序证明所有零槽带，然后 证明所有正槽带。在零槽带内，首先证明 \(A\le5M/6\) 的非中心化断言，然后证明 方程 [\[old-eq:2.1h\]](#old-eq:2.1h) 中的带填充核心。反射随后给出该带内 所有零槽长度。在正槽带内，首先 证明在方程 [\[old-eq:3.9\]](#old-eq:3.9) 约束下 \(A\le5M/6\) 的非中心化断言，然后 通过中心化证明该区域的剩余部分。因此，一个已完成的前一带 包含了无限制的零槽断言。设 \(M_{\max}\) 界定 初始宽度范围，并定义 \[D=2+\left\lceil 2M_{\max}/\sigma\right\rceil.\] 下文证明的严格宽度递减将表明，在一条分支上至多出现 \(D-2\) 次非终端调用。

当 \(M\le\rho\) 时，带填充的零槽核心可由绝对 计数得到：有 \(O(Z^m)\) 行，且平方乘积为 \(O(Z^{A+\epsilon_1})\)。它在 \(M\) 之上的指数至多为 \(A-q\le\rho+\delta\)。对于正槽，将已完成的 零槽估计与方程 [\[old-eq:3.5\]](#old-eq:3.5) 结合起来。在 方程 [\[old-eq:3.9\]](#old-eq:3.9) 的区域内，\(A\ge z\)，从而 \[z\le\frac{M}{6\kappa}\le\frac{2M}{9},
 \qquad \kappa z\le\frac M6.
 \label{old-eq:3.6}\] 因此正槽的额外终端指数至多为 \(\rho/6\)。通过选取足够小的 \(\rho,\delta\)，可以使这些终端指数小于 保留的最终损失。

对于高于下限的宽度，下文的两变换估计将 首先证明非中心化范围 \(A\le5M/6\)。我们现在解释为什么 剩余的输入可以与该范围进行比较。设 \[L=M/4.
 \label{old-eq:2.2}\] 对于 \(A>5M/6\)，比较长度 \(L,A-z-L\) 都至少 为 \(L\)。在正槽情形下， \((6\kappa-1)z\le M-A<M/6\)，且 \(6\kappa-1\ge7/2\)；因此 \(z<M/21<M/20\)。这也表明 \(A-z>2L\)。

如果一个原始素长度是 \(b<L\)，则反射另一个因子。 如果两者都至少为 \(L\)，则引入 其长度 \(L,A-z-L\) 且具有相同两个剖面的比较； 仅当单独估计该比较时才反射其较长的因子。在两种情形下， 经过该反射后的总长度至多为 \[b+\{M-(A-z-b)\}+z+\xi
 \le 3M/2-A+2z+\xi,\] 其中 \(b\le L\)。方程 [\[eq:centered-reflection-length\]](#eq:centered-reflection-length) 将截断的反射尺度与成对的未反射盒 乘子包含在同一个 \(\xi\) 中；被丢弃的尾部具有所述 固定阶的界。因此 \[A_{\rm comp}\le3M/2-A+2z+\xi.
 \label{old-eq:3.11}\] 对于 \(z=0\)，这给出 \(5M/6-A_{\rm comp}\ge M/6-\xi\)。对于 \(z>0\)，利用 \((6\kappa-1)z\le M-A\)、\(A>5M/6\) 和 \(z<M/20\) 得到 \[\begin{aligned}
 A_{\rm comp}&\le\frac{23}{30}M+\xi,\\
 A_{\rm comp}+(6\kappa-1)z
 &\le\frac52M-2A+2z+\xi\le\frac{14}{15}M+\xi.
 \end{aligned}
 \label{eq:comparison-uncentered-margin}\] 在 \(\xi\) 项之前，每个所需边界都有至少 \(M/15\) 的余量。 选取 \(\xi\le\rho/30\)。在 方程 [\[eq:centered-reflection-length\]](#eq:centered-reflection-length) 中的阈值之后，单位盒乘子 已包含在 \(\xi\) 中，因此每个保留的反射 比较都在该相同宽度处调用先前证明的非中心化断言。 这也完成了具有短于 \(L\) 的因子的原始情形。

在剩余的情形下，令 \(X_i=Z^{n_i}\)， \(Y_1=Z^L\)，以及 \(Y_2=X_1X_2/Y_1\)。则 \(X_1X_2=Y_1Y_2\)，且四个素长度都至少为 \(L\)。 从原始乘积中减去未反射的比较， 留下各槽的公共乘积 \(Q\)；将结果记为 \(\Delta_k\)。乘性与等乘积正规化 给出显式公式 \[\begin{split}
 \Delta_k
 =\frac{Q}{\sqrt{X_1X_2}}\sum_{l_1,l_2}\psi_k(l_1l_2)
 \bigl\{
 &W_1(q_{l_1}/X_1)W_2(q_{l_2}/X_2)\\
 -{}&W_1(q_{l_1}/Y_1)W_2(q_{l_2}/Y_2)
 \bigr\}.
 \end{split}\] 比较在原始允许 行上有界。整个 \(\Delta_k\) 的平方范数非负， 因此随后可以将其扩大到光滑行球中的所有行。在 非中心化情形下，改为扩大原始 乘积的平方范数。因此下文的 Poisson 变换从不 应用于选择例外或非例外行的指示函数。

#### 中心化系数及其支集

我们在变换其行范数的同时，将减法保留为一个系数。对于固定的理想 \(\mathbf b=(\mathfrak b_1,\mathfrak b_2)\)，定义 \[D_{\mathbf b}(l_1,l_2)
 =
 \prod_{i=1}^2W_i(q_{\mathfrak b_i}q_{l_i}/X_i)
 -
 \prod_{i=1}^2W_i(q_{\mathfrak b_i}q_{l_i}/Y_i),
 \qquad X_1X_2=Y_1Y_2.
 \label{old-eq:2.18a}\] 一个分配 \(\mathbf b\) 记录了已从两个素 变量中提取的素幂。如果它的条件对 某个矩形不可能成立，则该矩形在相应的 和上的剖面为零；但方程 [\[old-eq:2.18a\]](#old-eq:2.18a) 中的形式差 仍被保留。

保留这些公共数据的理由在 例外情形中已经显现。对于固定的 \(\vartheta\in\Theta\)、公共掩码 \(\mathfrak R_*\) 和公共范数幂 \(q_l^{it}\)，下文证明的格点 估计有主项 \[\sum_l\vartheta(l)1_{(l,\mathfrak R_*)=1}q_l^{it}W_i(q_l/T)
 =c_{\vartheta,\mathfrak R_*}T^{1+it}I_i(t)+\text{error},\] 其中 \(c_{\vartheta,\mathfrak R_*}\) 不依赖于 \(T\) 或 \(t\)。 这里 \(I_i(t)\) 是一个固定的测度常数乘以 \(\int_0^\infty W_i(y)y^{it}\,dy\)。 因此乘积主项为 \(c_{\vartheta,\mathfrak R_*}^2T_1^{1+it}T_2^{1+it}I_1(t)I_2(t)\)， 当 \(T_1T_2\) 一致时，两个矩形一致。 引理 [\[lem:centered-lattice-cancellation\]](#lem:centered-lattice-cancellation) 将量化剩余的 误差。该消去仅用于在 \(\Theta\) 中诱导 特征的变换行上；下文的公共系数在所有行上都被保留， 直到稍后进行情形划分。

对于剩余的槽集合 \(\mathcal I'\)，记 \(\Pi=\prod_{i\in\mathcal I'}p_i\)。具有公共 特征和掩码的系数指的是如下形式的系数 \[\begin{split}
 &\left(\prod_{i\in\mathcal I'}
       \nu_i(p_i)W_i^{\rm slot}(q_{p_i}/P_i)\right)
 D_{\mathbf b}(l_1,l_2)\,
 \tau_1(u)q_u^{it}
 1_{(u,\mathfrak R)=1}1_{s\mid u},\\
 &\hspace{40mm}u=\Pi l_1l_2.
 \end{split}
 \label{eq:centered-coefficient-form}\] 这里 \(\tau_1\) 是一个固定的有限射线 特征与移动剩余符号因子的零延拓乘积；\(\mathfrak R\) 是一个 固定的无平方因子额外掩码；\(s\) 是一个固定的无平方因子理想；且 \(t\in\mathbb R\)。当 \(s=1\) 时，条件 \(s\mid u\) 被省略。 各槽保留其原初互不相交的基础 支集。它们可以与任一素变量共享素因子。

这些公共数据在 *完整* 乘积上按乘法分解。 对于任意理想 \(v_1,\ldots,v_r\)，即使有公共素因子， \[\chi_{\prod v_i}(h)=\prod_i\chi_{v_i}(h),\quad
 q_{\prod v_i}^{it}=\prod_iq_{v_i}^{it},\quad
 1_{(\prod v_i,\mathfrak R)=1}
   =\prod_i1_{(v_i,\mathfrak R)=1}.\] 第一个恒等式包含所有零：一个出现的素因子若其总 指数被六整除，则给出零延拓的主 因子，而非常数一。同样的乘性对 \(\tau_1\) 成立。在完整乘积上取值的固定射线特征也 按每个变量上相同的特征进行分解。

我们固定一个支集约定，它也将控制槽网格 量词。设 \(N\) 为原始的固定槽数，并 选取包含每个 \(W_i^{\rm slot}\) 支集的固定区间 \([a_i,b_i]\)。令 \(h_i=\max\{|\log a_i|,|\log b_i|\}\)。选取一个固定数 \(H_N\)，至少为 \(\sum_i h_i\)，将其扩大以包含两个素 剖面窗、\(\log C_{\rm ref}\)、固定的算术正规化、相对的二进 盒，以及经过 \(D\) 个运算阶段的有限多个支集扩大。数 \(H_N\) 可以 依赖于所有固定数据和 \(N\)，但不依赖于 \(Z\) 或任何移动标签。 对于活或冻结槽的每个子集 \(I\)， \[\left|\log\prod_{i\in I}\frac{q_{p_i}}{P_i}\right|
 \le\sum_{i\in I}h_i\le H_N,
 \qquad \theta_N:=\frac{H_N}{\log Z}.
 \label{eq:centered-aggregate-support}\] 每个残差完整乘积除以其名义乘积尺度都落在 \(\exp([-H_N,H_N])\) 中，其中 \(H_N\) 就固定的运算列表 被增大一次。两个矩形都使用同一个盒。提取出的 素素幂使用其精确范数，且一个冻结槽仅贡献 其比值 \(q_p/P_i\) 一次。如果一个非空且小于一的素尺度 被截断为一，则其误差至多为该素 窗固定端点的对数除以 \(\log Z\)，每个素计一次。 因此，一个完整的槽子集或一次完整的除子提取贡献 一个聚合的 \(O(\theta_N)\) 边界误差，而不是为每个槽或素各贡献一份 预设容差。

#### 第一个 Poisson 变换及其目标界

我们现在估计非中心化乘积或上面选定的中心化 差二者之一。令 \(H=Z^m\) 和 \(X=Z^A\)。选取一个 固定的非负光滑径向函数，它支配行球。 任一矩形中的完整指标乘积的范数落在一个固定的 \(X\) 倍数内。本小节中所有指数的比较 首先在固定的二进范数区间上进行。它们有界的 相对宽度使对数长度改变 \(O(1/\log Z)\)； 最终损失讨论包含这些改变。

我们对两个 Poisson 公式使用以下公共局部化。 固定一个对 \(q>0\) 的非负光滑二进划分 \(\sum_\lambda\omega_\lambda(q/T_\lambda)=1\)， 其中每个权支撑在 \(C_d^{-1}\le q/T_\lambda\le1\) 内， \(C_d\) 固定。一个 扇区为有限的聚合外范数列表固定二进盒， 而非为每个槽单独设一个盒。设 \(T_{\rm sec}\) 为 该扇区中名义频率尺度的上确界。它与 任一组外标签处尺度之比至多为一个固定的 \(C_{\rm sec}\)。恰好保留其支集满足 下式的那些完整权 \[0<q\le T_{\rm sec}Z^{\xi/2}.\] 它们的并集包含在 \(q\le C_dT_{\rm sec}Z^{\xi/2}\) 中； 每个被丢弃的权都支撑在 \(T_{\rm sec}Z^{\xi/2}\) 之上。 该选取仅依赖于扇区，从不依赖于活列。 在 \(N\) 和支集数据固定之后，取 \(Z\) 足够大使得 \[2\theta_N+\frac{\log(C_dC_{\rm sec})}{\log Z}<\frac\xi4.
 \label{eq:centered-localization-threshold}\] 对 \(C_{\rm sec}\) 做一次固定扩大即可覆盖所有有限多个 扇区端点因子。

下面给出一个直接的尾部界，它为在 真实和上进行此运算提供依据。在两个应用中，核自变量都至少为 \(q/(e^{2H_N}T_{\rm sec})\)。因此在每个被丢弃的权上，由 方程 [\[eq:centered-localization-threshold\]](#eq:centered-localization-threshold)，它至少为 \(Z^{\xi/4}\)。 引理 [\[lem:kernel-seminorms\]](#lem:kernel-seminorms) 给出任意衰减 \((1+\text{argument})^{-B}\)。对第一个公式使用 \(|G(a,h)|\le q_a^{1/2}\)，对第二个使用有限 定义 \(|F(u,v;j)|\le q_uq_v\)。绝对理想计数和 固定因子数的除子界将一个扇区中所有原始 列和前因子界在 \(C_NZ^{B_0}\) 乘以一个关于所保留高度的固定 多项式之内，其中 \(B_0\) 仅依赖于 有界的总长度和所选取的辅助幂份额。尺度为 \(T\) 的 格范数二阶有 \(O(1+T)\) 个频率。 因此对被丢弃的二阶求和径向衰减给出 \(C_{N,B}Z^{B_1-B\xi/4}\) 乘以该高度多项式，其中有界 \(B_1\) 不依赖于 \(B\) 和 \(N\)，且当 \(B>1\) 时几何和 收敛。选取 \(B\) 足够大以获得任意指定的幂次 节省，包括冻结外标签的多项式个数。 这是对原始项的绝对界，在任何 非互素延拓或 Fourier 绝对化之前。它既不使用 稍后的 \(s\)-根式节省，也不使用分解的非互素恒等式。 在保留的权上，完整的平滑核被保留；没有插入将 行范数与两个活列范数相比较的尖锐 条件。低于第一个非零格范数的保留范围 是空的，除了一个由下文截断 约定覆盖的有界边界二阶。

在第一个行 Poisson 公式的零频率处，一个特征均值 非零仅当它在每个素因子处的指数模 六为零。特别地，在两个完整指标乘积的乘积中， 没有素因子以总重数一出现。因此该乘积 是一个幂理想。范数为 \(O(X^2)\) 的这类乘积有 \(O_\epsilon(X^{1+\epsilon})\) 个：每个幂理想是一个平方 乘以一个无平方因子理想的立方，对后者求和给出 通常的直到范数 \(Y\) 的 \(O(Y^{1/2+\epsilon})\) 界。 对固定因子数的分配是除子有界的。 中心因子为 \(X^{-1}\)，且行均值的大小至多 为 \(H\)。因此零频率为 \(O(Z^{m+\epsilon_1})\)。

对于非零频率，将两个完整乘积写为 \(Ca,Db\)， 其中 \(C,D\) 包含它们完整的公共素支撑，且 \[(a,b)=1,\qquad (ab,CD)=1.\] 在每个公共素处，固定它在每个素变量中的精确 赋值，以及它是否由某个槽提供。除掉这些赋值 会将该素加到该侧 *每个* 剩余因子的掩码中。 提供该素的槽被冻结并移除。此描述 即使某个槽和一个或两个素变量都提供了该素时仍然有效。 分配是对系数一次性作出的，因此同样的理想 \(\mathfrak b_i\) 出现在 \(D_{\mathbf b}\) 的两项中。 不可能的分配是零项。特别地，一个被旧的移动零或公共掩码 强制为零的标量，在施加这些支集条件之前 不会被替换为其绝对上界。

设 \(c,d\) 为 \(C,D\) 的对数范数，\(p\) 为 它们公共根式的对数范数。设 \(\mathfrak r\) 为 净指数模六非零的公共素的乘积；它的对数 范数为 \(R\)。相应的特征 \(\xi_{\mathfrak r}\) 模 \(\mathfrak r\) 本原。 在互补公共行掩码的 Möbius 展开中， 记 \(\mathfrak e\) 为所选除子，\(E\) 为其 对数范数。特别地 \[R\le p,\qquad E\le p-R.\]

设 \(A_C(a)\) 和 \(A_D(b)\) 为所分配的卷积 系数，其中公共特征 \(\tau\) 被省略。它们 包含所有剖面、活槽系数和固定掩码；在 中心化情形下，每个都包含整个所分配的差。 设 \[\tau_C(a)=\tau(a)\chi_a(\mathfrak e\mathfrak r)
                       \xi_{\mathfrak r}(a),\qquad
 \tau_D(b)=\tau(b)\chi_b(\mathfrak e\mathfrak r)
                       \overline{\xi_{\mathfrak r}(b)}.\] 剩余类 Poisson，连带来自节 [2](#sec:arithmetic) 的自对偶格 测度，对此分配给出如下非零频率表达式， 至多相差一个在冻结标签中有界模的标量： \[\begin{split}
 \frac{H}{Xq_{\mathfrak e}\sqrt{q_{\mathfrak r}}}
 \sum_{h\ne0}G_{\xi_{\mathfrak r}}(\mathfrak r,h)
 \sum_{(a,b)=1}
 &\frac{A_C(a)\overline{A_D(b)}}{\sqrt{q_aq_b}}\,
 \tau_C(a)\overline{\tau_D(b)}
 \overline{\mathcal R(a,b)}\,
 G(a,h)\overline{G(b,-h)}
 \\
 &\quad\cdot
 \widehat\Phi_1\left(
    \frac{Hq_h}{q_{\mathfrak e}q_{\mathfrak r}q_aq_b}
                    \right).
 \end{split}
 \label{eq:first-poisson-bridge}\] 这里 \(G_{\xi_{\mathfrak r}}\) 是正规化的本原 Gauss 和，其模至多为一。为验证正规化，代换 \(k=\mathfrak e k'\) 和模 \(\mathfrak r ab\) 的 Poisson 给出 \(H/(q_{\mathfrak e}q_{\mathfrak r}q_aq_b)\)。 三个未正规化的 Gauss 和恢复 \(\sqrt{q_{\mathfrak r}q_aq_b}\)。全局平方中心 正规化为 \(X^{-1}\)。对于相位，对两两互素的模 \(a,b,\mathfrak r\) 的 CRT 给出 \[\chi_a(b\mathfrak r)\overline{\chi_b(a\mathfrak r)}
       \xi_{\mathfrak r}(ab).\] 代换 \(k=\mathfrak e k'\) 给出 \(\chi_a(\mathfrak e)\overline{\chi_b(\mathfrak e)}\)，至多相差一个 在冻结标签中的标量。互反律将 \(\chi_a(b)\overline{\chi_b(a)}\) 变为 \(\overline{\mathcal R(a,b)}\)；剩余的因子恰为 \(\tau_C(a)\overline{\tau_D(b)}\)。这证明了 方程 [\[eq:first-poisson-bridge\]](#eq:first-poisson-bridge)。每个新特征作用于 其整个残差乘积。它新的移动素属于 所提取的支集，并穿刺每个残差因子。它们完整的所示 并集被计入，即便在 \(\mathfrak r\) 处的因子在单位上相消。

新的完整所示移动支集的对数范数至多为 \(\widetilde q=q+R+E\)，包括在 \(\mathfrak r\) 处任何相消的因子。它的名义频率尺度恰为 \[T_1(C,D,\mathfrak e,\mathfrak r)
 =\frac{q_{\mathfrak e}q_{\mathfrak r}X^2}
        {Hq_Cq_D}=Z^{K_0},
 \qquad K_0=2A-c-d+R+E-m.\] 乘积支集约定给出 \(q_a/(X/q_C),q_b/(X/q_D)\in\exp([-H_N,H_N])\)，因此对于 外扇区中 \(T_1\) 的上确界，方程 [\[eq:first-poisson-bridge\]](#eq:first-poisson-bridge) 中的 自变量至少为 \(q_h/(e^{2H_N}T_{\rm sec})\)。将前述整二进局部化 应用于此真实的互素桥。如果 \(K=\log_ZT_\lambda\) 是一个保留二进的上长度，则 \[\widetilde q=q+R+E,\qquad
 K\le K_0+\delta_{{\rm fr},1},\qquad
 0\le\delta_{{\rm fr},1}:=\frac\xi2+
       \frac{\log(C_dC_{\rm sec})}{\log Z}<\xi.
 \label{old-eq:2.3}\] 上面已估计的零频率是 原始公共光滑行球的零项；它不会在截断的 行区域上被恢复。稍后的账目保留可能的不等式 \(K_0-K\ge-\delta_{{\rm fr},1}\)。

对于每个保留的二进和每个真实的公共支撑分配，定义 \(\mathcal C_1(a,b;h)\) 为完整的桥求和项，它也适用于各自 与 \(CD\) 不交且被旧掩码允许的非互素 残差对。使用固定的双特征 \(\mathcal R(a,b)\)、完整的 零延拓 \(G(a,h),G(b,-h)\)、所示整乘积特征， 以及相同的二进权、核、逆根和形式乘积范数。 CRT 仅在 \((a,b)=1\) 时将此定义与 真实求和项等同。在每个有限列壳上，精确恒等式为 \[\sum_{(a,b)=1}\mathcal C_1(a,b;h)
 =\sum_{a,b}\mathcal C_1(a,b;h)\sum_{s\mid a,b}\mu(s).\] 完整的无平方因子 Möbius 和消去人为的非互素 对。在估计独立因子之前插入它，并令 \(s_0=\log_Zq_s\)。 在正规化的行范数与两个整乘积范数中分离固定射线相位 和所有光滑因子。在这些变量中，核为固定对数盒上的 \(\widehat\Phi_1(R_{\rm sc}x/(y_1y_2))\)。如果它的聚合尺度比 \(R_{\rm sc}\) 在该扇区上变化，则将那单个正规化的外比作为另一个坐标 纳入。截断值在 方程 [\[eq:centered-aggregate-support\]](#eq:centered-aggregate-support) 的公共乘积圆环上选取，且在固定活槽 标签之前。因此一个 Fourier 系数测度对各行和 所有活标签都是公共的。它提供行相位以及每个 整列上仅一个范数幂，连同冻结外范数中的相位。它不 在两个素变量或两个矩形上引入单独的幂。 完整的核和逆根一直保留到此分离为止； 在 \(D_{\mathbf b}\) 内取它们的绝对上确界将不会 保持该系数。仅在此分离之后对 \(h\) 应用 Cauchy–Schwarz， 也只有到这时才使用 \(|G_{\xi_{\mathfrak r}}|\le1\)。在 \(C\) 侧所得的正是范数为 \[\mathcal N_C=
 \sum_{h\ne0}\omega_K(q_h/Z^K)
 \left|Z^{-(A-c)/2}
   \sum_{s\mid a}A_C(a)\tau_C'(a)q_a^{it}G(a,h)\right|^2,
 \qquad \omega_K\ge0,\] 且有一个类似的 \(D\) 范数。这里 \(\tau_C'\) 包含 一个分离的固定射线特征。\(A_C\) 中所有固定掩码 仍然存在。因此完整提取和乘性使 方程 [\[eq:centered-coefficient-form\]](#eq:centered-coefficient-form) 中的系数保持不变，现在 乘以 \(G(a,h)\)。特别地，两个矩形保留 相同所分配的素幂、特征、穿刺和范数幂。

这两个范数之外的因子的指数为 \(m-A-R/2-E\)。公共支撑标签和 Möbius 标签的绝对数量具有指数 \(p+s_0+\epsilon_1\)。为一致地证明 公共支撑计数的合理性，首先计数其根式，给出 \(O(Z^{p+\epsilon_1})\)。对于多项式范数的固定根式 \(\mathfrak c\) 和 任意固定的 \(T\)，Rankin 界给出 \[\#\{v:\operatorname{rad}(v)\mid\mathfrak c,\ q_v\le Z^T\}
 \le Z^{aT}\prod_{\substack{r\mid\mathfrak c\\r\ {\rm prime}}}
             (1-q_r^{-a})^{-1}
 \ll Z^{aT+\epsilon_1}\] 对每个固定的 \(a>0\)。选取 \(a\) 小，并使用 多项式规模的 Euler 乘积估计。这将 \(C,D\) 中 幂的选择界在任意小的幂之内。它们的 分配以及 \(\mathfrak e\) 的选择具有除子有界的 重数。最后有 \(O(Z^{s_0+\epsilon_1})\) 个可能的 \(s\)。

下文的容许量 \(\epsilon_G\) 表示 当前归纳深度的误差包络，连同其局部小幂份额。 这些包络将在有限归纳完成时相容地选取， 整个过程使用相同的槽网格。 我们将为平方 \(C\) 范数证明以下充分界： \[\mathcal N_C\ll
 Z^{A-c+\widetilde q+\mathcal B_c-s_0+\epsilon_G},
 \qquad
 \mathcal B_c=\max\{0,(3c-5d-R)/6\}.
 \label{old-eq:2.5}\] 类似的量为 \(\mathcal B_d=\max\{0,(3d-5c-R)/6\}\)。 此蕴含的完整指数账目为 \[\begin{aligned}
 &(m-A-R/2-E)+(p+s_0)\\
 &\quad+\tfrac12\{A-c+\widetilde q+\mathcal B_c-s_0
                  +A-d+\widetilde q+\mathcal B_d-s_0\}\\
 &=M+\tfrac12\{\mathcal B_c+\mathcal B_d-(c+d-2p-R)\}.
 \end{aligned}\] 最后一个花括号非正： \[\mathcal B_c+\mathcal B_d\le c+d-2p-R.
 \label{old-eq:2.6}\] 事实上，在重数为 \(i\ge j\ge1\) 的公共素处，令 \(r=1_{6\nmid i-j}\)。只有 \(i\) 侧可以有正的 局部分子。它的贡献至多为 \((3i-5j-r)_+/6\)，而右侧贡献 \(i+j-2-r\)。后者非负。如果前者为 正，则它们的差的六倍为 \(3i+11j-12-5r\)，它非负：当 \(r=0\) 时它至少为 \(2\)，当 \(r=1\) 时有 \(i\ge j+1\)，给出至少 \(0\)。一个和的正部至多为各部分正部之和。乘以 每个素的对数范数并求和即证明方程 [\[old-eq:2.6\]](#old-eq:2.6)。因此只剩下 建立方程 [\[old-eq:2.5\]](#old-eq:2.5)。

#### 扩大 Gauss 行范数

本小节描述第二个变换将应用于其上的三个可能的正范数。 设 \(w\) 表示从 \(C\) 列中移除的长度，\(w_o\le w\) 为 该移除所产生的额外移动根式长度。令 \(a_0=A-c-w\)。当大小为 \(Z^{-w_o}\) 的平方提取系数已被移除时，方程 [\[old-eq:2.5\]](#old-eq:2.5) 允许无权的剩余范数具有指数 \[\Lambda_c=
 a_0+\widetilde q+w_o+w+\mathcal B_c-s_0+\epsilon_G.
 \label{old-eq:2.7}\] 这恰为 \(A-c+\widetilde q+\mathcal B_c-s_0+\epsilon_G+w_o\)。

对于初始范数，当 \(w=w_o=0\) 且 \(a_0=A-c\) 时，第一个 变换在固定 \(\Pi\) 并省略其外标量后 给出如下条件求和项： \[Z^{-a_0/2}\sum_{l_1,l_2}
 D_{\mathbf b}(l_1,l_2)\tau_1(l_1l_2)q_{l_1l_2}^{it}
 1_{(\Pi l_1l_2,\mathfrak R)=1}1_{s\mid\Pi l_1l_2}
 G(\Pi l_1l_2,h).
 \label{old-eq:2.18c}\] 在此多项式被平方之前，各槽和被恢复。 省略第二个矩形的同样陈述适用于 非中心化乘积。下文的局部计算将表明， 所提取的项在其缩短后的长度 \(a_0=A-c-w\) 处保持此形式。

定义 \[J=d-c+(K_0-K)-2w+w_o,\qquad J_+=\max(J,0).
 \label{old-eq:2.8}\]

在零槽证明中取 \(w=w_o=0\)，并令 \[\ell=0,\qquad g=J_++\sigma.\] 正范数 \(\mathcal N_C\) 至多是长度为 \(K+g\) 的光滑球上的相应 范数。此情形下行之间不相乘。

对于正槽，从 \(w=w_o=0\) 开始。令 \(\ell_*=\sigma/3\)，选择槽网格 \(\eta<\sigma/6\)， 并取固定池 \[\mathcal P=\{p: Z^{\ell_*}/2<q_p\le Z^{\ell_*},\
                    p\notin\mathcal S\}.\] 固定域中的素理想定理，等价地其固定 射线类形式 ，给出 \(|\mathcal P|=Z^{\ell_*+o(1)}\)。因为活跃槽长度 至多为 \(\eta\) 且其相对环形支集固定， 单个不等式 \(Z^{\ell_*-\eta}>2\max_i b_i\) 使该池与 每个活跃槽窗口不相交。其指数间隔至少为 \(\sigma/6\)， 与 \(N\) 无关；只有阈值依赖于固定 窗口。对于行 \(h\ne0\)，略去整除 \(h\)、\(s\) 或任何冻结支集的池素数。每个这样的整数或理想 具有多项式范数，因此略去 \(O(\log Z)\) 个素数。 剩余集合 \(\mathcal P_h\) 的大小与 \(|\mathcal P|\) 相当，且关于该行与冻结标签一致。

为比较行 \(h\) 与 \(hp^6\)，将完整模写作 \(p^iu\)，其中 \((p,u)=1\)。CRT 与互反律给出精确公式 \[G(p^iu,h)
 =\mathcal R(p,u)^i\chi_p(u)^{2i}G(p^i,h)G(u,h).\] 又有 \(G(u,hp^6)=G(u,h)\)，因为 \(p\) 是模 \(u\) 的单位 且 \(\chi_u(p^6)=1\)。 对于 \(p\nmid h\)，方程 [\[eq:gauss-local\]](#eq:gauss-local) 表明 将 \(h\) 替换为 \(hp^6\) 只改变 \(i=1,6,7\)。 出现的因子 \(G(p^i,h)\) 是行与 \(p\) 中的标量；所显示的剩余因子是整 \(u\) 上的一个固定射线特征 乘以一个剩余特征。因为 \(p\) 在每个活跃槽窗口之外，\(p^i\) 只分配给两个 素朴变量。剩余乘积在 \(p\) 处被穿孔，且 同一分配在两个矩形中更新 \(D_{\mathbf b}\)。 因为 \(p\nmid s\)，条件 \(s\mid u\) 仍然成立。

以下是精确的平均论证。将 \(\mathcal N_C\) 中的 正规化多项式写作 \(\mathcal H(h)\)。对每个 合格 \(p\)，局部 Gauss 求值给出 \(\mathcal H(h)=\mathcal H(hp^6)\) 加上具有 \(p\) 进列赋值 \(1,6,7\) 的抽取项。将这些赋值中每一个 分配到两个素朴变量只有有限多种方式。 Jensen 不等式——先对 \(p\) 再对此 固定有限和——给出 \[|\mathcal H(h)|^2\ll
 \frac1{|\mathcal P_h|}\sum_{p\in\mathcal P_h}
 \left\{|\mathcal H(hp^6)|^2+
        \sum_{i=1,6,7}\sum_{\rm allocations}
        |c_{p,i}(h)|^2|\mathcal H_{p,i}(h)|^2\right\}.\] \(\mathcal H_{p,i}\) 在其缩短的列 尺度上被正规化。刚才描述的局部恒等式与分配 应用于整个中心化系数，因此每个误差保持 方程 [\[eq:centered-coefficient-form\]](#eq:centered-coefficient-form)。

在原行权重的支集上，新行 \(hp^6\) 具有范数 \(O(Z^{K+6\ell_*})\)。固定输出行作为 \(hp^6\)（其中 \(p\in\mathcal P_h\)）只有有限多种表示： 每个这样的 \(p\) 整除该行，且所有这样的素数具有范数 至少 \(Z^{\ell_*}/2\)，而输出范数具有有界 对数长度。因此对 \(h\) 求和第一项 给出因子 \(|\mathcal P|^{-1}=Z^{-\ell_*+o(1)}\) 乘以新行上的正范数。对此主项令 \[\ell=\ell_*,\qquad g=J_++2\sigma.\] 由于 \(6\ell_*=2\sigma\)，长度为 \(K+g\) 的光滑球 包含所有新行。

对于抽取项令 \(P=q_p\)。当 \(p\nmid h\) 时， 方程 [\[eq:gauss-local\]](#eq:gauss-local) 给出以下中心 系数。在赋值一时，旧 Gauss 和具有模一 而新的为零，故抽取给出平方系数 \(P^{-1}\)。在赋值六时，新 Gauss 和为 \(P^3(1-P^{-1})\)；其中心因子为 \(P^{-3}\)，给出 \((1-P^{-1})^2\)。在赋值七时，新 Gauss 和具有 模 \(P^3\)，中心因子 \(P^{-7/2}\) 给出 \(P^{-1}\)。行相位为 \(\overline{\chi_p(h)}\)，对 赋值一与七而言；而对赋值六为一。它 乘以两个矩形。

令 \(\ell_p=\log_ZP\)。对充分大的 \(Z\)， \(\ell_*/2\le\ell_p\le\ell_*\)。三项的 移除长度与新移动根式长度为 \[(w,w_o)=(i\ell_p,e_i\ell_p),\qquad
 i=1,6,7,\quad e_1=e_7=1,\quad e_6=0.
 \label{old-eq:2.9}\] 两个平方因子 \(P^{-1}\) 恰好给出 \(Z^{-w_o}\)。 对赋值六项，精确因子 \(\chi_p(u)^{12}=1_{(u,p)=1}\) 由在 \(p\) 处 已经是公共的固定穿孔表示，且其固定射线相位 \(\mathcal R(p,u)^6\) 被保留。 在赋值一与七时，所显示的局部因子仍保留，且其 素数计入移动根式。在每个 误差中，冻结 \(p\)，保留其公共 列穿孔，并且仅在取正范数之后才丢弃其行资格限制。 平均值仍为 \(|\mathcal P|^{-1}\sum_{p\in\mathcal P}\)，因此关于 冻结 \(p\) 一致的界不引入素数计数因子。对每个误差 令 \[\ell=0,\qquad g=J_++\sigma\] 并将其原始行直接放大为长度为 \(K+g\) 的光滑球。误差不再被放大。三种类型的 范数均满足 \[0\le w_o\le w\le7\sigma/3.
 \label{old-eq:2.10}\]

行零仅在最终光滑球处加入。令 \(Y_{\rm col}=e^{H_N}Z^{a_0}=Z^{a_0+\theta_N}\)。非空列 壳满足 \(Y_{\rm col}\ge1\)，从而 \(a_0\ge-\theta_N\)。 由方程 [\[eq:gauss-local\]](#eq:gauss-local)，除非 \(u\) 为 六次幂，否则 \(G(u,0)=0\)，且 \(|G(u,0)|\le q_u^{1/2}\le Y_{\rm col}^{1/2}\)。 该支集上有 \(O(Y_{\rm col}^{1/6})\) 个六次幂。 若 \(s\mid u\)，则 \(q_s^6\le q_u\le Y_{\rm col}\)，故 \(s_0\le(a_0+\theta_N)/6\)。计入所分配的除子有界 卷积损失，中心正规化后的平方贡献为 \[\ll Z^{-a_0}\bigl(Y_{\rm col}^{1/6}Y_{\rm col}^{1/2}\bigr)^2
          Z^{\epsilon_1}
 =Z^{a_0/3+4\theta_N/3+\epsilon_1}
 \le Z^{a_0-s_0+2\theta_N+\epsilon_1}.\] 最后一个不等式由 \(a_0\ge-\theta_N\) 与所显示的 \(s_0\) 界得出。因此方程 [\[old-eq:2.7\]](#old-eq:2.7) 界定此新增 行，其中数值修正 \(2\theta_N\) 已包含在 \(C_*\xi\) 阶段余量中。这里 \(C_*\ge1\) 表示 一个阶段中累积支集误差的公共 常数，选取时与槽数 \(N\) 无关。下面的估计确立：一个这样的 选择覆盖一个阶段中的所有运算。零从不乘以 池素数。

#### 第二变换与较小宽度的乘积

在展开平方之前恢复所有活跃槽求和。令 \(B(u)\) 表示前述某个 Gauss 多项式中完整分配的卷积系数， 包括其固定掩码 与 \(s\) 整除条件。当使用中心化时它包含整个差。 其模满足 \(q_u/Z^{a_0}\in\exp([-H_N,H_N])\)。令 \(\Phi_2\) 为 定义最终行球的非负光滑径向函数。除 素密度中的 \(Z^{o(1)}\) 损失外，待界定的范数为 \[Z^{-\ell}\sum_h\Phi_2(q_h/Z^{K+g})
 \left|Z^{-a_0/2}\sum_u B(u)\tau_1(u)q_u^{it}G(u,h)\right|^2.\] 引理 [\[lem:full-correlation\]](#lem:full-correlation) 中的 Fourier 恒等式给出其 精确展开 \[\begin{split}
 Z^{K+g-\ell-a_0}\sum_{u,v}
 \frac{B(u)\overline{B(v)}\tau_1(u)\overline{\tau_1(v)}
       q_u^{it}q_v^{-it}}{\sqrt{q_uq_v}}
 \sum_j F(u,v;j)
 \widehat\Phi_2\left(\frac{Z^{K+g}q_j}{q_uq_v}\right).
 \end{split}\] 此处出现的核为 \[\widehat\Phi_2\left(\frac{Z^{K+g}q_j}{q_uq_v}\right).
 \label{old-eq:2.18b}\] 所显示的逆平方根与此核都作为整个 \(u,v\) 的 函数保留，直到下面进行整积分离。特别地 该公式包含每个活跃素数及每个 共享素数的重数。

在 \(j=0\) 时，引理 [\[lem:full-correlation\]](#lem:full-correlation) 只留下 \(u=v\)， 且 \(F(u,u;0)=\varphi(u)\le q_u\)。受支撑的 可被 \(s\) 整除的模，在非空壳上，至多为 \[C\frac{Y_{\rm col}}{q_s}=C Z^{a_0-s_0+\theta_N},\] 因为写作 \(u=sv\) 在该壳上给出 \(Y_{\rm col}/q_s\ge1\)。 除子有界系数使用其单独的 \(\epsilon_1\) 份额。因此对角指数为 \(K+g-\ell-s_0+\theta_N\)，包括 \(a_0-s_0\) 略微 为负时。从方程 [\[old-eq:2.7\]](#old-eq:2.7) 的余量中减去其名义部分（不含 \(\epsilon_G\)），给出 \[\begin{split}
 &(K+g-\ell-s_0)
 -(a_0+\widetilde q+w_o+w+\mathcal B_c-s_0)\\
 &\quad=(A-M)-d-(K_0-K)-w_o-\mathcal B_c+g-\ell\\
 &\quad\le A-M+5\sigma/3+\delta_{{\rm fr},1}.
 \end{split}
 \label{old-eq:2.12}\] 对于该不等式，令 \(D_0=d+K_0-K\)。贡献 \(-D_0-w_o+J_+\) 至多为 \(\delta_{{\rm fr},1}\)：当 \(J\ge0\) 时 至多为 \(-c-2w\)，而当 \(J<0\) 时使用 \(D_0\ge-\delta_{{\rm fr},1}\)。 最大剩余增量在被放大的主范数中为 \(2\sigma-\ell_*=5\sigma/3\)； 其他范数的增量为 \(\sigma\)。因此对角 仅需要所显示的末端损失 \(5\sigma/3\)，加上 已保留的频率扰动 \(\delta_{{\rm fr},1}\) 与数值支集修正 \(\theta_N\)，当 \(A\le M\) 时， 以及在带填充的零槽核心中的一个附加 \(\delta\)。 \(\theta_N\) 修正包含在 \(C_*\xi\) 阶段余量中。

对于 \(j\ne0\)，首先在这个真正的完整 \((u,v,j)\) 和上进行整二进局部化，然后才抽取任何公共支集。 名义尺度为 \(T_2=Z^{2a_0-K-g}\)，核的幅角在其 当前 Gauss 扇区中的上确界至少为 \(q_j/(e^{2H_N}T_{\rm sec})\)。上述尾部估计适用，使用 \(|F(u,v;j)|\le q_uq_v\)，且字面条件 \(s\mid u,v\) 仍然存在。记 \[\Omega_{\rm ret}(q_j)
 :=\sum_{\lambda\ {\rm retained}}\omega_\lambda(q_j/T_\lambda).\] 此公共行权重满足 \(0\le\Omega_{\rm ret}\le1\)。 方程 [\[old-eq:2.18b\]](#old-eq:2.18b) 中的完整核保留在 每个保留项上。所有后续带符号 Fourier 分离每次 对一个保留的 \(\lambda\) 进行，因此正规化行变量 停留在一个固定对数盒上；\(\Omega_{\rm ret}\) 记录它们的和与 公共定义域。在有界多项式范围内有 \(O(\log Z)\) 个 相关的保留二进块。前面的 \(j=0\) 项正是 同一最终 \(\Phi_2\) 球的对角，包括先前加入的 Gauss 行零；两个零项都不在不同定义域上恢复。

现在记 \(u=D_2a,\ v=E_2b\)，抽取真正的完备 公共支集，使得 \((a,b)=1\) 且 \((ab,D_2E_2)=1\)。 按第一变换那样将所有抽取的幂分配给素朴变量与槽。 引理 [\[lem:complete-support-correlation\]](#lem:complete-support-correlation) 在此真正 轨迹上适用，给出 \[F(D_2a,E_2b;j)=F(D_2,E_2;j)\mathcal R(a,E_2)
   \overline{\mathcal R(b,D_2)}\mathcal R(a,b)
   \chi_a(j)\overline{\chi_b(-j)}.\] 它允许所有四个模中的任意素数幂，并在公共素数处 留下一个行标量。每个被抽取的素数在其一侧 穿孔所有剩余因子，且供给该素数的每个槽都被 冻结。

这也显式解释了槽与素朴变量 共享素数的情形。若 \(p\) 只出现在一侧，具有 全重数 \(i\)，则其剩余因子为 \(\chi_p(j)^i\)。将 \(i\) 在两个素朴变量与 可能的槽之间拆分，由乘性恰好给出相同的因子， 包括当 \(6\mid i\) 且 \(p\mid j\) 时。例如，一个素朴 \(p^5\) 与一个槽 \(p\) 给出零扩张因子 \(\chi_p(j)^6\)。若 \(p\) 出现在两侧，则其全部幂被 移除。在不相等情形 \(i>j_0\ge1\)，局部相关性 除非 \(6\mid j_0\) 且频率为 \(p^{j_0}k\) （其中 \(p\nmid k\)）外为零；当它非零时等于 \[P^{j_0-1}(P-1)\chi_p(k)^{i-j_0},\qquad P=q_p.\] 这是一个行标量，即使第一侧的超额赋值 部分来自活跃槽。例如 \(i=7,j_0=6\) 与一个 素朴 \(p^6\) 及槽 \(p\) 留下标量 \(P^5(P-1)\chi_p(k)\)，冻结该槽，并在 \(p\) 处穿孔两个 剩余的素朴变量。相等重数具有 方程 [\[eq:correlation-local\]](#eq:correlation-local) 中的标量因子与 相同的穿孔结论。完备而非仅 gcd 的抽取 正是使这些局部因子独立于剩余 变量的原因。

定义 \[c_2=\log_Zq_{D_2},\quad d_2=\log_Zq_{E_2},\quad
 b_2=(c_2+d_2)/2.\] 令 \(p_2\) 为其公共根式的对数范数， 令 \(G_c=(D_2,E_2)\)，并令 \(g_2=\log_Zq_{G_c}\)。 除非 \(G_c\mid j\)，相关性为零。在具有 相等重数 \(i\not\equiv0\pmod6\) 的公共 素数处，根据该素数不整除或整除相除后的频率 \(j/G_c\)，称其为单位或非单位。令 \(t_2\) 为这些 单位素数的总根式长度。令 \(V_{\rm id}\) 为 这些非单位素数的乘积并令 \(V=\log_Zq_{V_{\rm id}}\)。

方程 [\[eq:correlation-local\]](#eq:correlation-local) 给出以下绝对 局部界： \[\begin{array}{c|c}
 \text{公共重数与相除后的频率}&
       \text{绝对相关性界}\\ \hline
 i=i,\ 6\nmid i,\ \text{unit}&P^{i-1}\\
 i=i,\ 6\nmid i,\ \text{nonunit}&P^i\\
 i=i,\ 6\mid i,\ \text{either}&P^i\\
 i>j_0,\ 6\mid j_0,\ \text{unit}&P^{j_0}.
 \end{array}\] 不在最后一行的每个不相等情形均为零。固定 所指明的单位/非单位划分，并记 \(j=G_cV_{\rm id}h'\)。 划分标量 \[1_{\rm part}(h')
 \frac{F(D_2,E_2;G_cV_{\rm id}h')}{Z^{g_2-t_2}}\] 定义为在该划分之外为零，且在此定义下 处处模至多为一。我们不断言其他行上未划分 相关性的单位界。被旧掩码强制为零的每个冻结分配 在使用此绝对界之前仍被丢弃。

完备支集恒等式在每个整剩余列上 留下行因子 \(\chi_n(G_cV_{\rm id}h')\)。 为计数其固定移动支集，令 \(v=G_cV_{\rm id}\) 并 \(e_p=v_p(v)\bmod 6\)。这些好理想的标准主 生成元的乘积是主的，因此精确的全输入 恒等式为 \[\chi_n(v)=
   \prod_{\substack{p\mid v\\e_p\ne0}}\chi_n(p)^{e_p}
   \prod_{\substack{p\mid v\\e_p=0}}1_{(n,p)=1},\] 而原行的任何单位保留在 \(h'\) 中。此恒等式中的所有素数 已经穿孔每个剩余因子，因为它们属于 真正的抽取支集。活跃的 \(e_p\ne0\) 素数 包含在由 \(t_2\) 计数的单位集与由 \(V\) 计数的非单位集中。相等六可除与不相等最小六可除 素数具有 \(e_p=0\)，且在此固定因子中仅由公共 穿孔表示。非单位素数也可以具有 \(e_p=0\)，此时在 \(V\) 中计数它只会扩大 界。这只分解 \(\chi_n(v)\)：自然行因子 \(\chi_n(h')\) 及其全部零点，以及所有固定射线互反 相位均保留。它不会将随变化行的抵消重新归类 为额外穿孔。因此完整的新移动支集 长度至多为 \(\widetilde q+w_o+t_2+V\)。

定义名义行宽度与总宽度为 \[\begin{aligned}
 m'&=2a_0-K-g-g_2-V,&
 q'&=\widetilde q+w_o+t_2+V,\\
 M'&=m'+q'
    =M+J-g-g_2+t_2
    \le M-\sigma.
 \end{aligned}
 \label{old-eq:2.13}\] 这里 \(g_2\ge t_2\)，且 \(g\) 的定义给出 \(g-J\ge\sigma\)。这些恒等式通过代入 \(a_0=A-c-w\) 以及方程 [\[old-eq:2.3\]](#old-eq:2.3) 之前的 \(K_0\) 的定义得到。令 \[0\le\delta_{{\rm fr},2}:=\frac\xi2+
       \frac{\log(C_dC_{\rm sec})}{\log Z}<\xi.\] 这里的扇区常数是第二变换的那些常数。 保留的行权重恰好拉回到 \(\Omega_{\rm ret}(q_{G_cV_{\rm id}}q_{h'})\)。在其支集上， \[q_{h'}\le
 \frac{C_dT_{\rm sec}Z^{\xi/2}}{q_{G_cV_{\rm id}}}
 \le\frac{C_dC_{\rm sec}Z^{2a_0-K-g+\xi/2}}
          {q_{G_cV_{\rm id}}}
 =Z^{m'+\delta_{{\rm fr},2}}.\] 因此它位于那个公共包络行球中。在 非空保留范围上定义所声明的非负行长度 \(m'_{\rm act}=\max\{0,m'+\delta_{{\rm fr},2}\}\) 与 \(M'_{\rm act}=m'_{\rm act}+q'\)。非空性蕴含 \(m'+\delta_{{\rm fr},2}\ge0\)，故 \(0\le M'_{\rm act}-M'\le\delta_{{\rm fr},2}\)。 在整个带符号计算中，将此包络 球其余部分的拉回权重视为零，并对 划分标量同样处理。这是一个精确的零扩张。它们 只有在形成非负子范数或例外绝对乘积之后 才会被其绝对界替换。 完备抽取仅缩短一个素朴变量或冻结 整个槽，因此存活的槽长度满足 \(z'\le z\)。

我们记录第二变换中所有其他指数。 条件 \(s\mid u,v\) 未被丢弃：它蕴含 \(s\) 的 每个素数都属于第二个完备公共根式。因此 完备抽取之后，剩余列上不存在剩余的 \(s\) 整除条件。对于此固定的 \(s\)，长度为 \(p_2\) 的可能根式个数为 \(O(Z^{p_2-s_0+\epsilon_1})\)：将该根式写作 \(s\mathfrak r_2\)，其中 \((s,\mathfrak r_2)=1\)，并计数 剩余范数的无平方因子 \(\mathfrak r_2\)。若在固定壳边界之外 \(p_2<s_0\)，则没有。用于 \(C,D\) 的同一 Rankin 论证界定其幂与分配重数。选择单位/非单位 划分的代价至多为 \(2^{\omega(\operatorname{rad}(D_2E_2))}\)，这是另一个除子有界 因子，包含在 \(\epsilon_1\) 中。这些指数为 \[\begin{array}{l|r}
 \text{factor}&\text{exponent}\\ \hline
 \text{平方中心正规化}&-a_0\\
 \text{行 Poisson 因子与正规化逆根}&K+g-a_0\\
 \text{素密度（当出现时）}&-\ell\\
 \text{固定 }s\text{ 的公共支集计数}&p_2-s_0\\
 \text{common correlation}&g_2-t_2\\
 \text{转换为正规化剩余乘积}&a_0-b_2
 \end{array}\] 最后一行为 \(\{(a_0-c_2)+(a_0-d_2)\}/2\)。 它们的和为 \[K+g-\ell-a_0+p_2-s_0+g_2-t_2-b_2.\] 从余量 方程 [\[old-eq:2.7\]](#old-eq:2.7) 中减去此和，得到 内层素朴乘积所允许的指数。这是要由 更小宽度矩或由例外行估计提供的界： \[M'+\Delta_{\rm child},\qquad
 \Delta_{\rm child}=b_2-p_2+w+\mathcal B_c+\ell
                   \ge w+\ell.
 \label{old-eq:2.14}\] 该不等式使用 \(b_2\ge p_2\)，因为每个公共素数处的 两个重数都至少为一。

我们现在在形成独立子之前移除剩余互质性。 对于固定的真正 \(D_2,E_2\)，定义 \[\widetilde F_{D_2,E_2}(a,b;j)
 :=F(D_2,E_2;j)\mathcal R(a,E_2)
   \overline{\mathcal R(b,D_2)}\mathcal R(a,b)
   \chi_a(j)\overline{\chi_b(-j)}\] 在所有各自与 \(D_2E_2\) 互素且被旧掩码允许的 剩余对上。仅当 \((a,b)=1\) 时它等于 真正的相关性。 通过所分配的卷积公式与旧公共掩码，在所有 各自允许的剩余对上定义剩余的 \(\mathcal C_2(a,b;j)\)，包括 \((ab,D_2E_2)=1\)。 保持形式整乘积范数 \(q_{D_2}q_a,q_{E_2}q_b\)、两个逆根、完整光滑 核，以及在其包络球上以零扩张的相同拉回行权重。 对每个保留行，精确恒等式为 \[\begin{split}
 \sum_{(a,b)=1}\mathcal C_2(a,b;j)F(D_2a,E_2b;j)
 &=\sum_{\mathfrak t\ {\rm squarefree}}\mu(\mathfrak t)
   \sum_{\mathfrak t\mid a,b}\mathcal C_2(a,b;j)
                \widetilde F_{D_2,E_2}(a,b;j).
 \end{split}\] 这是完整的 Möbius 指示函数，而非截断。各个 列壳与保留行球是有限的。因此其相等性 通过交换有限和并仅在 \((a,b)=1\) 时 使用真正相关性恒等式得到。\(\mathfrak t\) 的额外公共 素数不属于真正 \(D_2,E_2\) 支集或 其频率限制。由于剩余掩码已经 排除该支集，每个非零 \(\mathfrak t\) 与它及与 \(s\) 都不相交。

在每个保留二进块上，如第一变换那样，在 正规化 \(h'\) 范数与两个整乘积范数中分离完整核与逆根。 冻结因子 \(G_cV_{\rm id}\) 只对行 Fourier 幂贡献 一个外部相位。固定支集盒在当前活跃标签之前 选定，因此所得到的系数测度对它们、对 两个矩形以及对行都是公共的。然后固定 \(\mathfrak t\)。 对其每个素数 \(p\)， 使用精确的因子分配恒等式 \[1_{p\mid\prod_i n_i}
 =\sum_{\varnothing\ne J}(-1)^{|J|+1}
       \prod_{i\in J}1_{p\mid n_i},\] 其中因子 \(n_i\) 是两个素朴变量与活跃 槽。对选中的素朴变量记 \(n_i=pl_i\)，对 \(l_i\) 无 限制。这只抽取一个行标量及 \(q_p^{it}\)，并将两个 \(X_i,Y_i\) 替换为 \(X_i/q_p,Y_i/q_p\)。它不引入单变量穿孔。 选中的槽被冻结。若两个不同的除子素数选中 同一个素数槽，则该为零。商与未选中的 因子仍可包含 \(p\)，并可与对侧重叠； 不施加新的互质性。旧公共掩码保持公共，且 两个新素朴尺度的乘积在两个矩形中相等。 抽取的行标量，包括零标量，保留在 带符号恒等式中。

只有在现在，对于固定的保留二进块与固定 Fourier 参数， 每个分离出的被加项才是两个独立剩余 卷积的乘积，其中 \(\mathbf J\) 记录因子分配。 它们的行特征为 \[\tau_1(n)\rho(n)\chi_n(G_cV_{\rm id}h'),\qquad
 \tau_1(n)\rho'(n)\chi_n(-G_cV_{\rm id}h'),
 \quad \rho,\rho'\in\Theta.\] 它们通过上述固定因子支集表示来理解。特别地 它们的诱导特征之比属于 \(\Theta\)，包括补充因子 \(n\mapsto\chi_n(-1)\)；此断言在零点处不取商。 它们的自然行零点被保留。抽取 选中的因子贡献行标量，而非剩余特征的 新因子，也不是 \(q'\) 中的新支集。这些标量， 包括零点，保留在带符号恒等式中。

<span id="lem:centered-coefficient-invariant" label="lem:centered-coefficient-invariant">\[lem:centered-coefficient-invariant\]</span> 对于中心化输入，两个变换以及刚构造的中间 Gauss 行 放大保持以下系数数据。 每个 Gauss 多项式与每个放大器误差保持 方程 [\[eq:centered-coefficient-form\]](#eq:centered-coefficient-form)，乘以 \(G(u,h)\)， 除有界冻结标量与模至多为一的行标量外。 对于非中心化输入，全程省略第二个矩形。 在第二变换与完整 Möbius 因子分配之后，每个 分离的子侧具有该系数形式，但不含 \(G\) 且不含 \(s\mid u\)。每个存活槽具有子侧的一个整乘积 特征及其原始系数 \(\nu_i\)，不含 Gauss 系数。 在一侧内，素朴变量在两个矩形中具有相同的特征、穿孔掩码 与范数幂。一个平方 Gauss 范数的两侧 可以有不同的范数幂；它们的诱导特征相差 \(\Theta\) 中的一个成员。

若新的诱导特征属于 \(\Theta\)，则固定活跃槽 标签留下素朴系数 \[\vartheta(l_1)\vartheta(l_2)
 1_{(l_1l_2,\mathfrak R_*)=1}q_{l_1l_2}^{it}D_{\mathbf b}(l_1,l_2)\] 对某个 \(\vartheta\in\Theta\)、某个多项式范数的无平方因子掩码 \(\mathfrak R_*\) 及某个实数 \(t\)。 掩码可以依赖于冻结行，但对两个变量 与两个矩形都是公共的。所有系数都以其保留的 冻结标量（包括零点）以及下面记录的精确正规化来理解。

第一变换的计算证明了 Gauss 系数形式；局部 \(p\) 幂计算对每个放大器误差证明了它。 上述真正的完备支集恒等式与完整 Möbius 分配 证明了子形式，在每个整剩余乘积上 保持一个特征与范数幂。因此“公共”涉及一个分离的侧； 所显示的特征比是两侧之间的关系。 当诱导特征属于 \(\Theta\) 时，它在单位上等于某个 \(\vartheta\in\Theta\)。其冗余的自然零点 与固定穿孔合并为一个多项式范数的 \(\mathfrak R_*\)。对每个固定的 \(\Pi\)，乘性把它在 \(\Pi l_1l_2\) 上的值、掩码与范数幂分解为 \(\Pi\) 中的一个标量乘以结论中陈述的三个因子。这证明了 例外断言。

下面我们记录两个剩余卷积的精确正规化。令 \[\alpha_1=a_0-c_2,\qquad \alpha_2=a_0-d_2,\qquad
 \frac{\alpha_1+\alpha_2}{2}=a_0-b_2.\] 在当前双变换阶段的入口处，令 \(\mathcal I_{\rm in}\) 为其活动槽集，并令 \(X_1,X_2\) 为其第一个矩形的形式尺度。它们的精确约定为 \(X_1X_2\prod_{i\in\mathcal I_{\rm in}}P_i=Z^A\)。 对于边 \(j\in\{1,2\}\)，令 \(\mathcal F_j\) 为来自该入口集、被第一次和第二次真正的公共支集抽取所冻结的槽，令 \(\mathcal I_j\) 为在最终 \(\mathfrak t\)-分配之前仍然活动的槽，并令 \(Q_{{\rm plain},j}\) 为在这些步骤以及放大器处抽取出的 plain 幂的精确范数之积。在祖先阶段被移除的槽不包含在 \(\mathcal F_j\) 中。令 \(T_j\) 为其矩形中两个 plain 尺度的公共形式 pre-\(\mathfrak t\) 乘积；对于非中心化输入则使用其唯一的形式 plain 乘积。在使用槽比值之前，丢弃一个冻结槽的剖面为零的项，该项由其冻结数据恒为零，与行标号和活动标号无关。 完全抽取给出精确恒等式 \[\begin{aligned}
 Z^{A-\alpha_j}
   &=Q_{{\rm plain},j}\prod_{i\in\mathcal F_j}q_{p_i},\\
 T_j\prod_{i\in\mathcal I_j}P_i
   &=\frac{Z^A}{Q_{{\rm plain},j}\prod_{i\in\mathcal F_j}P_i}
     =Z^{\alpha_j+e_j},\\
 e_j&=\sum_{i\in\mathcal F_j}\log_Z(q_{p_i}/P_i),
 \qquad |e_j|\le\theta_N.
 \end{aligned}\] 放大器对此计算只贡献精确的 plain 幂。每个较早的冻结槽只出现一次，即使它与某个 plain 共享其素因子。已经分离出去的逆根、核以及固定的正规化常数仍位于 \(e_j\) 之外。

对于边 \(j\)，令 \(d_{j,i}\) 为在 plain \(i\) 中选出的最终 \(\mathfrak t\)-素因子之积，并令 \(\mathcal J_j\subseteq\mathcal I_j\) 为新冻结的槽。令 \[a_{j,i}=\log_Zq_{d_{j,i}},\qquad
 \widetilde r_j=a_{j,1}+a_{j,2}+\sum_{i\in\mathcal J_j}z_i\ge0,
 \qquad
 \omega_j=\sum_{i\in\mathcal J_j}\log_Z(q_{p_i}/P_i).\] 相应的形式尺度在两个矩形中都除以 \(q_{d_{j,i}}\)。一个在两个不同 \(\mathfrak t\)-素因子处选取同一个素槽的分配，或一个剖面值为零的新冻结槽，由冻结数据恒为零，并在使用这些比值界之前被丢弃。其他所有被抽取出的零点都保留，直到下文所述的非负或绝对值估计。

使用下端点除子二进区间 \(T\le q_{\mathfrak t}<2T\)，\(T\ge1\)，并令 \(t_-:=\log_ZT\)。每个二进区间包含 \(O(Z^{t_-})\) 个理想。边 \(j\) 上实际选出的乘积被 \(\mathfrak t\) 整除，故 \[\begin{aligned}
 \widetilde r_j+\omega_j
 &=\log_Z\left(q_{d_{j,1}d_{j,2}}
                  \prod_{i\in\mathcal J_j}q_{p_i}\right)
 \ge\log_Zq_{\mathfrak t}\ge t_-,\\
 |\omega_j|&\le\theta_N,\qquad |e_j+\omega_j|\le\theta_N
 \quad(j=1,2).
 \end{aligned}
 \label{eq:centered-divisor-boundary}\] 最后一个不等式使用了当前阶段入口槽的不相交子集 \(\mathcal F_j\) 与 \(\mathcal J_j\)。它不包含祖先槽或固定的分离常数。

记 \(T'_j=T_j/q_{d_{j,1}d_{j,2}}\)，则 post 形式因子之积与名义原始子尺度为 \[T'_j\prod_{i\in\mathcal I_j\setminus\mathcal J_j}P_i
   =Z^{\alpha_j+e_j-\widetilde r_j},\qquad
 N_{{\rm post},j}=Z^{\alpha_j-\widetilde r_j}.
 \label{eq:centered-raw-normalization}\] 定义 \(P_{C,\mathfrak t,\mathbf J}(h')\) 与 \(P_{D,\mathfrak t,\mathbf J}(h')\) 为其剩余卷积乘以 \(N_{{\rm post},j}^{-1/2}\)。相对于名义 pre-正规化因子 \(Z^{-\alpha_j/2}\)，边 \(j\) 上的精确抽取系数为 \(Z^{-\widetilde r_j/2}\)，除去冻结槽的幅度、保留的抽取行标量以及已经分离的外因子。这些原始子项保留形式带符号矩形，并非矩引理的调用；其形式对数长度可能为负。尚未发生裁剪。

因子分配对固定的 \(N\) 是除子有界的；其总和使用 \(C_N^{\omega(\mathfrak t)}
\ll_{N,a}q_{\mathfrak t}^a\)（对任意固定的 \(a>0\)）来界定，而不是在每个素因子处花费一个固定指数。有界列范围中的 \(O(\log Z)\) 个除子二进区间使用其现有的对数份额。这些离散损失与数值项 \(\theta_N\) 分开。

为精确起见，抽取 \(Z^{g_2-t_2}\) 之后的另一个公共行标量为 \[v_{{\rm part},\lambda}(h')=
 \omega_\lambda(q_{G_cV_{\rm id}}q_{h'}/T_\lambda)
 1_{\rm part}(h')
 \frac{F(D_2,E_2;G_cV_{\rm id}h')}{Z^{g_2-t_2}}\zeta(h'),
 \qquad |\zeta(h')|\le1,\] 其中 \(\zeta\) 包含该二进区间与这些 Fourier 参数的分离行相位。它在保留的划分与包围球之外为零，且 \(|v_{{\rm part},\lambda}|\le1\)。 随后的估计逐个二进区间地进行，然后用已经允许的 \(O(\log Z)\) 质量求和。按照诱导特征是否属于 \(\Theta\) 来拆分已经因子化的行和。在 \(\Theta\) 之外的行上，Cauchy–Schwarz 给出两个非负子范数；在 \(\Theta\) 中的行上，取逐点的绝对乘积。只有在这些步骤中，才可以把公共行权、划分标量或抽取行标量的绝对值界以 1，并把行放大到公共的 \(m'_{\rm act}\) 球。这可能会纳入违反先前单位限制的额外例外行，但下文的仅关于特征的计数把它们包含在内。两侧使用相同的合格类，并与方程 [\[old-eq:2.14\]](#old-eq:2.14) 比较。

首先考虑其子诱导特征位于 \(\Theta\) 之外的行。两侧具有相同的合格条件，因为它们的特征相差 \(\Theta\) 中的一个成员。 在这样的行上，首先用一个中心化子范数以其两个矩形的范数之和为其界；对于非中心化子项则只有一个矩形。对于固定的一边 \(j\) 与矩形 \(\varrho\)，将其 pre 与 post 形式 plain 尺度写为 \(S_{\varrho,i}\) 与 \(S'_{\varrho,i}=S_{\varrho,i}/q_{d_{j,i}}\)。在当前行、除子与活动标号之前，为每个当前的 plain 剖面类型选择一个固定的上支集端点 \(B_i\)。仅当对某个 \(i\) 有 \(S'_{\varrho,i}B_i<1\) 时才略去该矩形；此时那个 plain 因子在每个非零整理想上为零。保留等号以及所有其他的剖面、掩码、行标量或算术零点。此检验与行标号和活动标号无关。

对于保留的矩形，令 \(x_i=\log_ZS_{\varrho,i}\) 与 \(y_i=x_i-a_{j,i}\)。固定的端点检验与 \(a_{j,i}\ge0\)，在把 \(H_N\) 放大以包含上端点对数的两个正部之后，给出精确的裁剪恒等式 \[\begin{aligned}
 \pi_{0,j,\varrho}&=\sum_{i=1}^2(-x_i)_+,\qquad
 \pi_{j,\varrho}=\sum_{i=1}^2(-y_i)_+,
 \qquad 0\le\pi_{0,j,\varrho}\le\pi_{j,\varrho}\le\theta_N,\\
 r_{{\rm clip},j,\varrho}
 &=\sum_{i\in\mathcal J_j}z_i+
       \sum_{i=1}^2\bigl((x_i)_+-(y_i)_+\bigr)
 =\widetilde r_j-(\pi_{j,\varrho}-\pi_{0,j,\varrho})\ge0,\\
 A_{{\rm clip},j,\varrho}
 &=\sum_{i=1}^2(y_i)_++\sum_{i\in\mathcal I_j\setminus\mathcal J_j}z_i
 =\alpha_j+e_j-\widetilde r_j+\pi_{j,\varrho}\\
 &=\alpha_j+e_j+\pi_{0,j,\varrho}-r_{{\rm clip},j,\varrho}.
 \end{aligned}
 \label{eq:centered-clipped-rectangle}\] 特别地，裁剪后的总和从其自身的裁剪前总和 \(\alpha_j+e_j+\pi_{0,j,\varrho}\) 减少了 \(r_{{\rm clip},j,\varrho}\)。不同的矩形可以有不同的裁剪后总和。一个保留的亚单位尺度位于固定区间 \([1/B_i,1]\) 内，因此其膨胀到尺度一保持有限的半范数界。行特征、公共掩码以及存活的槽权不变。从 pre-正规化因子 \(Z^{-\alpha_j/2}\) 到该标准裁剪乘积的精确系数为 \[Z^{(A_{{\rm clip},j,\varrho}-\alpha_j)/2}
 =Z^{(-r_{{\rm clip},j,\varrho}+e_j+\pi_{0,j,\varrho})/2}.\] 对于固定的一对保留矩形，略去其矩形下标。于是方程 [\[eq:centered-divisor-boundary\]](#eq:centered-divisor-boundary) 把配对的除子计数与这些系数界以 \[\begin{split}
 t_- -\frac{r_{{\rm clip},1}+r_{{\rm clip},2}}2
     +\frac{e_1+\pi_{0,1}+e_2+\pi_{0,2}}2
 &\le\frac{(e_1+\omega_1)+\pi_1+(e_2+\omega_2)+\pi_2}{2}\\
 &\le2\theta_N.
 \end{split}
 \label{eq:centered-clipped-shell}\] 每边至多有两个矩形，因此至多四对这样的配对；它们的三角因子固定。对于带符号的差，不使用公共的裁剪缩减。

在 \(c_2\) 一侧，在最后一次互素抽取之前，名义总长度为 \(A'=\alpha_1=A-c-w-c_2\)。对于正槽参数， \[\begin{split}
 (A'-M')-(A-M)
 &=g+w-d-c_2-(K_0-K)-w_o+g_2-t_2\\
 &\le6(w+\ell)+\delta_{{\rm fr},1}.
 \end{split}
 \label{old-eq:3.14}\] 为证明该不等式，首先使用 \(g_2-t_2\le c_2\)。 在放大的主范数中，\(w=w_o=0\)，且 \[g=J_++2\sigma
 \le d+(K_0-K)+6\ell+\delta_{{\rm fr},1}.\] 对于误差，\(g\le d+(K_0-K)+\sigma+\delta_{{\rm fr},1}\)，故超出量至多为 \(w-w_o+\sigma+\delta_{{\rm fr},1}\)。这些不等式使用了 \(d+K_0-K\ge-\delta_{{\rm fr},1}\) 以及正部的 \(1\)-Lipschitz 性质。方程 [\[old-eq:2.9\]](#old-eq:2.9) 中的三种选择，连同 \(\ell_p\ge\sigma/6\)，给出 \(w-w_o+\sigma\le6w\)。这就证明了方程 [\[old-eq:3.14\]](#old-eq:3.14)。

对于每个保留的裁剪矩形，如果没有槽存活，则在所声明的宽度 \(M'_{\rm act}\) 处应用已完成的、无限制的零槽断言。如果槽存活，首先应用方程 [\[old-eq:2.1a\]](#old-eq:2.1a)–[\[old-eq:2.1b\]](#old-eq:2.1b) 中的代数掩码删除。它把该标准裁剪乘积表示为自然乘积，并且只减小其非负仿射表达式。对于每个实际乘积，在两个频率包络、\(\mathfrak t\)-分配以及掩码删除之后，令 \(A_{\rm act},z_{\rm act}\) 为其所声明的总和与槽长度，并令 \[F_{\rm act}
 =\bigl(A_{\rm act}-M'_{\rm act}+(6\kappa-1)z_{\rm act}\bigr)_+.\] 父项满足方程 [\[old-eq:3.9\]](#old-eq:3.9)。在此掩码删除之前，令 \(z'\le z\) 为裁剪矩形的存活槽长度。方程 [\[old-eq:3.14\]](#old-eq:3.14) 与 [\[eq:centered-clipped-rectangle\]](#eq:centered-clipped-rectangle)，连同 \(M'_{\rm act}\ge M'\)，给出 \[\begin{split}
 A_{{\rm clip},j,\varrho}-M'_{\rm act}+(6\kappa-1)z'
 &\le \alpha_j-M'+(6\kappa-1)z
       +e_j+\pi_{j,\varrho}-\widetilde r_j-(M'_{\rm act}-M')\\
 &\le6(w+\ell)+\delta_{{\rm fr},1}+e_j+\pi_{j,\varrho}.
 \end{split}\] 在另一侧互换 \(c_2,d_2\) 后同样的计算成立。 取正部然后删除固定掩码因此给出 \[F_{\rm act}\le6(w+\ell)+\delta_{{\rm fr},1}
                 +(e_j+\pi_{j,\varrho})_+
 \le6(w+\ell)+\delta_{{\rm fr},1}+2\theta_N.\] 这里 \(z_{\rm act}\le z'\le z\)。所有展示的账目都使用固定的一列聚合长度 \[A,z,c,d,p,R,E,s_0,K,w,w_o,g,\ell,c_2,d_2,p_2,g_2,t_2,V.\] 它们的仿射系数与正部 Lipschitz 常数是数值的，且与 \(N\) 无关。因此，一旦施加了聚合阈值，所展示的频率、原始正规化以及矩形裁剪界就被包含在 \(C_*\xi\) 中，其中 \(C_*\ge1\) 固定且与 \(N\) 无关。此固定误差界的存在性在比较长度之前使用单个 \(\theta_N=H_N/\log Z\)，而不是 \(N\) 个独立的 \(\xi\) 副本。我们在下文放大 \(C_*\)，以覆盖一个阶段中固定数目的运算。

如果 \(F_{\rm act}>0\)，则从该乘积中移除整槽，直到剩余乘积满足方程 [\[old-eq:3.9\]](#old-eq:3.9) 或直到没有槽剩余。这里的移除指对整条选出的素多项式应用逐点界方程 [\[old-eq:3.5\]](#old-eq:3.5)；不冻结任何素标号。一个被移除的长度为 \(d\) 的槽使 \(A_{\rm act}+(6\kappa-1)z_{\rm act}\) 减少 \(6\kappa d\)，并对平方的 \(Z\)-指数贡献 \(\kappa d\)，而固定的半范数与高度因子单独保留。由于每个槽的长度至多为 \(\eta\)，把正的活动长度排序，并取达到 \(F_{\rm act}/(6\kappa)\) 的第一个前缀。其前一个前缀小于该阈值，且其最后一个槽的长度至多为 \(\eta\)。如果没有前缀达到该阈值，则移除所有槽，其总和更小。因此恰好只有一个槽会造成超调，且总移除长度 \(d_z\) 满足 \[\begin{split}
 d_z&\le\min\left\{z_{\rm act},
                     \frac{F_{\rm act}}{6\kappa}+\eta\right\},\\
 \kappa d_z&\le\frac{F_{\rm act}}6+\kappa\eta
 \le\Delta_{\rm child}+\frac{\delta_{{\rm fr},1}}6
                       +\frac{\theta_N}{3}+\eta.
 \end{split}
 \label{old-eq:3.16}\] 如果在到达仿射边界之前槽就消失，则剩余的 plain 长度可以任意；这正是已完成的、较小宽度的零槽断言包含所有长度的原因。否则对剩余乘积应用正槽归纳。其槽仍然具有原来的系数类，其诱导行仍然位于 \(\Theta\) 之外。Cauchy–Schwarz 对两个分别裁剪的子项的误差取平均，因此它们可能不同的矩形与槽集不会使 \(\eta\) 加倍。将方程 [\[old-eq:3.16\]](#old-eq:3.16) 与方程 [\[eq:centered-clipped-shell\]](#eq:centered-clipped-shell) 中的配对系数界以及 \(M'_{\rm act}-M'\le\delta_{{\rm fr},2}\) 结合，超出子包络的严格边界尺度代价至多为 \[\delta_{{\rm fr},2}+\frac{\delta_{{\rm fr},1}}6
        +\eta+\frac{7\theta_N}{3}.
 \label{eq:centered-child-edge-cost}\] 如果没有槽存活，同样的界成立，而无需贪心代价。数值项 \(\theta_N\) 与两个频率修正在使用方程 [\[old-eq:2.14\]](#old-eq:2.14) 时，给出继承自方程 [\[old-eq:2.7\]](#old-eq:2.7) 的 \(\epsilon_G\) 储备中的单个 \(O(\xi+\eta)\) 边界损失；现有的局部小幂与固定解析因子保持分开。逐点估计对整个被移除的乘积只请求一次；其内部的小幂份额可能依赖于 \(N\)。这一次贪心运算只在实际子项的所有边界缺陷都已被纳入 \(F_{\rm act}\) 之后才发生。对于 \(d_2\) 一侧的论证与互换 \(c_2,d_2\) 后相同。

我们现在仅使用更小的宽度就界定了所有诱导特征位于 \(\Theta\) 之外的子行。对于剩余的行，接下来的计数与体积界处理非中心化范围；中心化范围使用系数引理中保留的减项。

#### 诱导特征位于 \(\Theta\) 的行

在本小节中，当子行的诱导特征属于 \(\Theta\) 时，称其为*例外*的。由系数引理，两个分离边要么都是例外的，要么都不是。现有的完整展示移动支集中的每个素因子都是一个公共列零点，每个额外的公共穿刺点亦然。这在起初成立，在第一个变换中对 \(\mathfrak e,\mathfrak r\) 仍然成立，并且对放大器的素因子仍然成立。对于一个非零的真正第二分配，因子 \(\tau_1(D_2),\tau_1(E_2)\) 以及旧的公共掩码因此迫使其完全的根基与所有那些支集不相交。此结论是在把任何冻结标量替换为上界之前得出的。人为的剩余延拓保持 \(D_2,E_2\) 与那些掩码固定，无法使一个不可能的分配复活。

我们明确给出固定素因子处行因子的有限射线约化。如方程 [\[eq:row-fixed-ray-reduction\]](#eq:row-fixed-ray-reduction) 中那样，把一个非零行写为 \(h'=\varepsilon h_{\mathcal S}h_{\rm good}\)，其中 \(\varepsilon\) 是一个单位，另外两个因子分别支在 \(\mathcal S\) 及其补集上。对于与 \(\mathcal S\) 互素的原始元素 \(n\)，互反律给出（保留每个零点） \[\chi_n(h')=\chi_n(\varepsilon h_{\mathcal S})
   \mathcal R(n,h_{\rm good})
   \prod_{p\mid h_{\rm good}}\chi_p(n)^{v_p(h')}.\] 由引理 [\[lem:fixed-numerator-ray\]](#lem:fixed-numerator-ray)，在固定单位以及 \(\mathcal S\)-赋值模六之后，第一个因子属于一个支在 \(\mathcal S\) 上的有限射线特征族。在固定好射线扇区之后，第二个因子属于固定的互反族。我们不把任何移动的好素因子吸收进这个固定族。第一个因子所提供的族不必包含于 \(\Theta\) 中；这样的选择只是有限多个。每个剩余的展示好素因子都具有其实际的局部六次指数，非平凡指数在该素因子处分歧。

令 \(v_1\) 为在 \(V\) 中计数的、其相等重数为 1 的素因子的根基长度，并令 \(f=2v_1\)。在这样的素因子处，行中的固定因子 \(G_cV_{\rm id}\) 的赋值为 2。该素因子处不存在现有的移动特征，而 \(\Theta\) 的每个特征在那里都是非分歧的。因此六次互反律表明，例外诱导要求 \[v_p(h')+2\equiv0\pmod6,\qquad\text{that is,}\qquad
 v_p(h')\equiv4\pmod6.\] 更一般地，在 \(\mathcal S\) 之外的每个素因子处，例外诱导为 \(v_p(h')\) 指定一个模六的单剩余类，由冻结的移动特征与 \(G_cV_{\rm id}\) 决定。在它们的支集之外该剩余为零。对于在 \(\mathcal S\) 处的有限多个选择以及单位与固定射线数据，\(h'\) 的理想因此具有唯一形式 \[(h')=\mathfrak h_0\mathfrak v^6,\] 其中 \(\mathfrak h_0\) 固定且无六次幂因子。所展示的赋值四条件给出 \(q_{\mathfrak h_0}\ge Z^{4v_1}=Z^{2f}\)。在通常的有界尺度约定下，到 \(q_{h'}\ll Z^{m'_{\rm act}}\) 为止的理想计数现在对每个非空范围给出更强的界 \(O(Z^{(m'_{\rm act}-2f)/6+\epsilon_1})\)。我们只使用较弱的界 \[\#\{h':q_{h'}\ll Z^{m'_{\rm act}},\ \text{exceptional}\}
 \ll Z^{(m'_{\rm act}-f)/6+\epsilon_1}
 \le Z^{(m'-f)/6+\delta_{{\rm fr},2}/6+\epsilon_1}.
 \label{eq:exceptional-row-count}\] 如果该指数描述的是小于 1 的尺度，则被强制的理想 \(\mathfrak h_0\) 使该范围除在同一个有界尺度边界处之外为空。此论证包含主特征以及 \(\Theta\) 的所有其他成员。在旧的移动素因子处的附加条件只能使计数减小。它还覆盖了在正性之后把划分标量界住时所纳入的行。在单位素因子处，这样的新增行可以是例外的，即便它在原划分中缺失；不使用来自单位集 \(t_2\) 的任何额外强制节省。

在例外行上，对每一对已经分配的子项取绝对乘积，并乘以方程 [\[eq:exceptional-row-count\]](#eq:exceptional-row-count)。令 \(c_{\mathfrak t,\mathbf J}(h')\) 表示其中心抽取系数与有界的抽取标量。对于具有原始减项 \(\widetilde r_1,\widetilde r_2\) 的分配，取绝对值后 \(|c_{\mathfrak t,\mathbf J}(h')|\ll_N
 Z^{-(\widetilde r_1+\widetilde r_2)/2}\)。使用绝对体积而非抵消，边 \(j\) 上未正规化的 plain 差在每个正形式尺度处都是 \(O(T'_j)\)，包括亚单位尺度，且未正规化的活动槽贡献 \(O_N(\prod_{i\in\mathcal I_j\setminus\mathcal J_j}P_i)\)。因此方程 [\[eq:centered-raw-normalization\]](#eq:centered-raw-normalization) 给出原始正规化体积 \[|P_{j,\mathfrak t,\mathbf J}(h')|
 \ll_N N_{{\rm post},j}^{-1/2}T'_j
             \prod_{i\in\mathcal I_j\setminus\mathcal J_j}P_i
 =Z^{(\alpha_j-\widetilde r_j)/2+e_j}\] 至相差固定的半范数与高度因子，其中 \(j\) 表示其 \(C\) 或 \(D\) 一侧。因此，对于一个已分配对与一个下端点除子二进区间（包括其计数），指数为 \[a_0-b_2+e_1+e_2+t_- -\widetilde r_1-\widetilde r_2
 \le a_0-b_2+e_1+(e_2+\omega_2)
 \le a_0-b_2+2\theta_N.\] 这里方程 [\[eq:centered-divisor-boundary\]](#eq:centered-divisor-boundary) 给出 \(t_- -\widetilde r_2\le\omega_2\)，且 \(\widetilde r_1\ge0\)。从而 \[\sum_{\mathfrak t,\mathbf J}
 |c_{\mathfrak t,\mathbf J}(h')|
 |P_{C,\mathfrak t,\mathbf J}(h')
       P_{D,\mathfrak t,\mathbf J}(h')|
 \ll Z^{a_0-b_2+2\theta_N+\epsilon_1}.\] 所展示的和对一个固定的下端点除子二进区间求和；其分配已经被包含在 \(\epsilon_1\) 中。它并未断言在 Möbius 分配之前存在独立的乘积。从参考体积与名义例外计数中减去内部允许量，给出精确的代数恒等式 \[\frac{m'-f}{6}+a_0-b_2-(M'+\Delta_{\rm child})
 =A-\frac56M-F_1-F_2,
 \label{old-eq:2.15}\] 其中 \[\begin{aligned}
 F_1&=c/6+5\{d+(K_0-K)\}/6+w/3+\widetilde q/6
       +w_o+\mathcal B_c-5g/6+\ell,\\
 F_2&=2b_2-\tfrac56g_2-p_2+t_2+V/6+f/6.
 \end{aligned}
 \label{old-eq:2.16}\] 实际超出量由方程 [\[old-eq:2.15\]](#old-eq:2.15) 中的名义表达式加上 \(\delta_{{\rm fr},2}/6+2\theta_N+\epsilon_1\) 为其界。 为显式验证，方程 [\[old-eq:2.15\]](#old-eq:2.15) 的左端首先等于 \[a_0-2b_2+p_2-w-\mathcal B_c-\ell
       -\tfrac56m'-q'-f/6.\] 代入方程 [\[old-eq:2.13\]](#old-eq:2.13) 与 \(K=2A-c-d+R+E-m-(K_0-K)\) 给出方程 [\[old-eq:2.15\]](#old-eq:2.15)–[\[old-eq:2.16\]](#old-eq:2.16)。

以下下界正是完全的公共支集不消耗可用指数的原因： \[F_1\ge\tfrac23(c+w)-3\sigma-\tfrac56\delta_{{\rm fr},1},\qquad
 F_2\ge\tfrac23b_2.
 \label{old-eq:2.17}\] 为证明第一个，令 \(D_0=d+K_0-K\)，初始设 \(g=J_+\) 与 \(\ell=0\)，并回忆 \(J=D_0-c-2w+w_o\)。当 \(J\ge0\) 时，直接化简给出 \[F_1=c+2w+\widetilde q/6+w_o/6+\mathcal B_c
       \ge c+2w.\] 当 \(J<0\) 时，使用 \(\widetilde q\ge R\) 与 \[\mathcal B_c+\widetilde q/6
 \ge (3c-5D_0)_+/6-\tfrac56\delta_{{\rm fr},1}.\] 事实上，左端至少为 \(\{(3c-5d-R)_++R\}/6\)，而它至少为 \((3c-5d)_+/6\)，同时 \(D_0\ge d-\delta_{{\rm fr},1}\)。正部是 \(1\)-Lipschitz 的，给出所展示的修正。由此推出 \[F_1\ge
 \frac{c+5D_0+(3c-5D_0)_+}{6}+\frac w3
       -\frac56\delta_{{\rm fr},1}
 \ge\frac23(c+w)-\frac w3-\frac56\delta_{{\rm fr},1}.\] 实际选择满足 \(g\le J_++2\sigma\) 与 \(\ell\ge0\)。因此方程 [\[old-eq:2.10\]](#old-eq:2.10) 把来自 \(2(c+w)/3\) 的额外损失界以 \[w/3+5\sigma/3+\tfrac56\delta_{{\rm fr},1}
 \le22\sigma/9+\tfrac56\delta_{{\rm fr},1}
 <3\sigma+\tfrac56\delta_{{\rm fr},1}.\]

对于方程 [\[old-eq:2.17\]](#old-eq:2.17) 中的第二个不等式，从 \(F_2\) 的定义逐素因子计算。以该素因子的对数范数为单位，贡献为 \[\begin{array}{c|c|c}
 \text{common case}&F_2&b_2\\ \hline
 i=i,\ 6\nmid i,\ \text{unit}&7i/6&i\\
 i=i,\ 6\nmid i,\ \text{nonunit}
       &(7i-5)/6+\tfrac13 1_{i=1}&i\\
 i=i,\ 6\mid i,\ \text{either}&7i/6-1&i\\
 i>j_0,\ 6\mid j_0,\ \text{unit}
       &i+j_0/6-1&(i+j_0)/2 .
 \end{array}\] 第二行中额外的 \(1/3\) 是 \(f/6\)。第一行超过 \(2b_2/3\)。在第二行，等号在 \(i=1\) 处成立，且对于 \(i\ge2\)，差为 \((3i-5)/6\ge0\)。在第三行，差为 \((i-2)/2\ge0\)，因为 \(i\ge6\)。在最后一行，差为 \((4i-j_0-6)/6\ge0\)，因为 \(j_0\ge6\) 且 \(i\ge j_0+1\)。求和即证明该断言。

对于非中心化范围 \(A\le5M/6\)，方程 [\[old-eq:2.15\]](#old-eq:2.15)–[\[old-eq:2.17\]](#old-eq:2.17) 把名义例外超出量界以 \(3\sigma+5\delta_{{\rm fr},1}/6\)。上文记录的实计数与聚合支集修正是在固定的阶段允许量中的进一步 \(O(\xi)\) 项。连同对角估计与较小宽度的估计，这就在当前宽度处以保留的终端损失证明了非中心化阶段。因此先前构造的比较可以使用该阶段。剩下要估计的是当 \(A>5M/6\) 时的中心化例外项。

对于一个固定例外行的一个分离边，固定活动槽标号。于是引理 [\[lem:centered-coefficient-invariant\]](#lem:centered-coefficient-invariant) 给出在两个 plain 变量中以及在两个矩形项中相同的特征、穿刺点与范数幂。下一个引理表明，每个 plain 和中 \(X^{1+it}\) 的系数与 \(X\) 无关，因此两个乘积主项在尺度之积相等时一致。

<span id="lem:centered-lattice-cancellation" label="lem:centered-lattice-cancellation">\[lem:centered-lattice-cancellation\]</span> 设 \(\vartheta\) 取遍一个固定的有限集合，其元素为导子素理想 属于 \(\mathcal S\) 的有限阶射线特征。设 \(\mathfrak R_*\) 无平方因子且 \(q_{\mathfrak R_*}\le Z^{B_*}\)， 其中 \(B_*\) 固定，并设 \(W_1,W_2\) 为固定圆环上的 光滑剖面。对 \(X>0\) 与 \(t\in\mathbb R\)，定义 \[\mathcal L_i(X,t):=
 \sum_l\vartheta(l)1_{(l,\mathfrak R_*)=1}
           q_l^{it}W_i(q_l/X).\] 则 \[\begin{aligned}
 \mathcal L_i(X,t)
 &=c_{\vartheta,\mathfrak R_*}X^{1+it}I_i(t)
   +O\left(Z^{\epsilon_1}(1+|t|)^J\right),
 \label{old-eq:2.18d}\\
 |\mathcal L_i(X,t)|&\ll X.
 \label{old-eq:2.18e}\end{aligned}\] 这里 \(J\) 固定，各常数只用到有限多个半范数， \(c_{\vartheta,\mathfrak R_*}\) 与 \(X,t\) 无关，而 \(I_i(t)\) 等于一个固定测度常数乘以 \(\int_0^\infty W_i(y)y^{it}\,dy\)。 这两个估计对 \(X>0\)、对所述的掩码以及对所述有限 特征集都一致。

设 \(D_{\mathbf b}\) 如 方程 [\[old-eq:2.18a\]](#old-eq:2.18a) 中那样，并令 \[U_i=X_i/q_{\mathfrak b_i},\qquad
 V_i=Y_i/q_{\mathfrak b_i},\qquad
 T=U_1U_2=V_1V_2.\] 若对 \(i=1,2\) 及某个 \(r\ge0\) 有 \(U_i,V_i\ge Z^r\)， 则 \[\begin{split}
 T^{-1/2}\left|
 \sum_{l_1,l_2}
 \vartheta(l_1)\vartheta(l_2)
 1_{(l_1l_2,\mathfrak R_*)=1}
 q_{l_1l_2}^{it}D_{\mathbf b}(l_1,l_2)
 \right|
 \ll Z^{\epsilon_1}(1+|t|)^{2J}T^{1/2}Z^{-r}.
 \end{split}
 \label{old-eq:2.18f}\] 若没有非负的下方长度，则同一表达式为 \(O(T^{1/2})\)。

首先略去掩码。表示 \(\mathcal S\) 之外的理想的那些主生成元， 连同固定的特征权 \(\vartheta\)，构成固定格中的有限加权剩余类 集合。在该格上应用 Poisson 求和于 \[f_{X,t}(z)=q_z^{it}W_i(q_z/X)
           =X^{it}f_t(z/\sqrt X),\qquad
 f_t(z)=q_z^{it}W_i(q_z).\] Fourier 变换为 \(X^{1+it}\widehat f_t(\sqrt X\,\xi)\)。 由于 \(f_t\) 支在固定圆环上，对任意固定的 \(J_0>2\) 分部 积分给出 \[|\widehat f_t(\xi)|
 \ll_{J_0} (1+|t|)^{J_0}(1+|\xi|)^{-J_0},\] 这里用到 \(W_i\) 的有限多个半范数。对 \(X\ge1\)，在固定对偶格的 非零点上的求和因此为 \[\ll (1+|t|)^{J_0} X
       \sum_{\xi\ne0}(1+\sqrt X|\xi|)^{-J_0}
 \ll (1+|t|)^{J_0}\] 必要时增大 \(J_0\)。对 \(0<X<1\)，格和及其零频主项都由固定 圆环上的绝对计数知为 \(O(1)\)。零频为 \(c_\vartheta X^{1+it}I_i(t)\)，其中 \(c_\vartheta\) 是这些 剩余类的固定加权平均。这就证明了 方程 [\[old-eq:2.18d\]](#old-eq:2.18d) 的无掩码版本。

现用容斥插入掩码。首先从 \(\mathfrak R_*\) 中去掉它位于 \(\mathcal S\) 中的素理想，因为每个 求和理想已经避开它们。于是下文用到的所有除子 都在 \(\mathcal S\) 之外。记 \(\mathcal L_i^0\) 为 无掩码的和，由积性给出 \[\mathcal L_i(X,t)
 =\sum_{d\mid\mathfrak R_*}
       \mu(d)\vartheta(d)q_d^{it}\mathcal L_i^0(X/q_d,t).\] 主系数为 \[c_{\vartheta,\mathfrak R_*}
 =c_\vartheta\sum_{d\mid\mathfrak R_*}
             \frac{\mu(d)\vartheta(d)}{q_d}.\] 提取出的 \(q_d^{it}\) 抵消了 \(X/q_d\) 处主项中的 \(q_d^{-it}\)。这证明 该系数与 \(X\) 和 \(t\) 都无关。 各误差至多乘以除子的个数 \(\#\{d:d\mid\mathfrak R_*\}\ll_{\epsilon_1,B_*}Z^{\epsilon_1}\)。 系数本身也由多项式大小的 Euler 乘积估计而有 \(Z^{\epsilon_1}\) 界。这证明了 方程 [\[old-eq:2.18d\]](#old-eq:2.18d)。

对方程 [\[old-eq:2.18e\]](#old-eq:2.18e)，在原和中取绝对值。 它在一个固定的正常数尺度以下为空；只要 它非空，固定圆环上的理想计数就给出 \(O(X)\) 个点。这对 \(t\) 和掩码都一致。

方程 [\[old-eq:2.18f\]](#old-eq:2.18f) 中的带掩码和恰为 \[\mathcal L_1(U_1,t)\mathcal L_2(U_2,t)
 -\mathcal L_1(V_1,t)\mathcal L_2(V_2,t).\] 方程 [\[old-eq:2.18d\]](#old-eq:2.18d) 中的两个乘积主项都为 \(c_{\vartheta,\mathfrak R_*}^2T^{1+it}I_1(t)I_2(t)\)。 它们相互抵消。每个含有一个误差的交叉项被 \(Z^{\epsilon_1}(1+|t|)^{2J}\) 乘以 \(U_1,U_2,V_1,V_2\) 之一 所界，而误差的乘积在减弱次要幂损失后有同样的 界。若四个尺度都不小于 \(Z^r\)，则每个至多为 \(TZ^{-r}\)， 且由 \(T\ge Z^{2r}\) 有 \(1\le TZ^{-r}\)。 因此差为 \(O(Z^{\epsilon_1}(1+|t|)^{2J}TZ^{-r})\)。 除以 \(T^{1/2}\) 即证得 方程 [\[old-eq:2.18f\]](#old-eq:2.18f)。当没有非负的下方长度 可用时，方程 [\[old-eq:2.18e\]](#old-eq:2.18e) 将每个乘积界为 \(O(T)\)， 即得最后一项断言。

将此引理应用于每个已分配的例外子结点。关于其系数 与公共掩码的假设由 引理 [\[lem:centered-coefficient-invariant\]](#lem:centered-coefficient-invariant) 得到；特别地，主项 在同一行、掩码与整体乘积范数 幂下、在取任何绝对值之前就相互抵消。初始时四个普通长度 都不小于 \(L\)。在所选的 \(\mathfrak t\)-因子 被移去之前，\(c_2\) 一侧的下方普通长度至少为 \(L-c-w-c_2\)，名义总长度为 \(\alpha_1=a_0-c_2\)： 没有任何一个普通长度损失超过由 两个真正的公共支撑与放大器所提取的总量 \(c+w+c_2\)。另一侧 有关于 \(d_2\) 的类似界。令 \[r=(L-c-w-\min(c_2,d_2))_+,\] 并称具有此参考节省的一侧为第一侧，同时一并重标 其相关的原始数据。若 \(\widetilde r_1<r\)，则每个 所选的普通长度满足 \(a_{1,i}\le\widetilde r_1\)，于是 四个形式上的后普通尺度都有对数长度至少 \(r-a_{1,i}\ge r-\widetilde r_1>0\)。在这些精确的等乘积形式尺度上 应用方程 [\[old-eq:2.18f\]](#old-eq:2.18f)。 若 \(\widetilde r_1\ge r\)（含相等），或若 \(r=0\)，则使用 同一引理中全尺度绝对体积的兜底。在此分支中没有形式 中心尺度被截断，且一个恒为零的 矩形保留在形式差中。由此得到的节省为 \((r-\widetilde r_1)_+\)。以另一侧的绝对体积， 这给出对每个低端点除子二进段的聚合界， \[\begin{split}
 &\sum_{\mathfrak t,\mathbf J}
 |c_{\mathfrak t,\mathbf J}(h')|
 |P_{C,\mathfrak t,\mathbf J}(h')
       P_{D,\mathfrak t,\mathbf J}(h')|\\
 &\hspace{15mm}\ll
 Z^{a_0-b_2-r+2\theta_N+\epsilon_1}.
 \end{split}
 \label{old-eq:2.18}\] 这里及以下均理解为分离高度中的一个固定多项式。为验证 该界，原始系数与体积给出 参考指数 \(a_0-b_2+e_1+e_2\) 与减少量 \(-\widetilde r_1-\widetilde r_2\)，而除子计数给出 \(t_-\)。方程 [\[eq:centered-divisor-boundary\]](#eq:centered-divisor-boundary) 给出 单行不等式 \[\begin{split}
 t_- -\widetilde r_1-\widetilde r_2-(r-\widetilde r_1)_+
 &=(t_- -\widetilde r_2)-\max(r,\widetilde r_1)\\
 &\le\omega_2-r.
 \end{split}
 \label{old-eq:2.18h}\] 加上 \(e_1+e_2\) 后至多剩下 \(e_1+(e_2+\omega_2)-r\le2\theta_N-r\)。 受除子界约束的分配只贡献 \(\epsilon_1\)， 这就证明了方程 [\[old-eq:2.18\]](#old-eq:2.18)。 这适用于人工项，即使商仍保留 \(\mathfrak t\)-素理想，因为系数引理在每个 矩形差内保持公共掩码、相等的乘积尺度与一个范数幂。

活跃槽只在有限变换移去其 Gauss 系数之后才求和。 它们未正规化的绝对和贡献 \(O_N(\prod_{i\ {\rm live}}P_i)\)。将其与名义 原始正规化因子结合，就给出 方程 [\[eq:centered-raw-normalization\]](#eq:centered-raw-normalization) 中完整的 \(e_j\) 体积因子，如上面 所包含；它不会被替换为因子乘积的正规化因子。Fourier 测度在其 标签之前就已固定，因此对这些标签取条件既不改变公共掩码 也不改变中心节省。零条件槽标量 仅在本绝对界中被丢弃。

令 \(v=c+w+\min(c_2,d_2)\)。由 方程 [\[old-eq:2.17\]](#old-eq:2.17)，\(F_1+F_2\) 至少为 \(2v/3-3\sigma-5\delta_{{\rm fr},1}/6\)，因为 \(b_2\ge\min(c_2,d_2)\)。 方程 [\[old-eq:2.18\]](#old-eq:2.18) 中的中心节省现在把 例外亏空（除 \(3\sigma\) 以及所记录的 频率与聚合支撑扰动之外）界为 \[A-\tfrac56M-\tfrac23v-(L-v)_+
 \le (A-M)_+.
 \label{old-eq:2.19}\] 事实上，对 \(0\le v\le L\) 左端为 \(A-5M/6-L+v/3\)，它随 \(v\) 递增；对 \(v\ge L\) 它为 \(A-5M/6-2v/3\)，它递减。 其最大值在 \(v=L=M/4\) 处取得，等于 \(A-M\)。 对正槽，方程 [\[old-eq:3.9\]](#old-eq:3.9) 蕴含 \(A\le M\)。对零槽核心， 方程 [\[old-eq:2.1h\]](#old-eq:2.1h) 给出 \(A-M\le\delta\)。 因此中心例外项只需要终端 损失 \(3\sigma\)，或在填充核心中为 \(\delta+3\sigma\)。 额外的 \(\delta_{{\rm fr},1}\)、\(\delta_{{\rm fr},2}\)、 与 \(\theta_N\) 项包含在同一个 \(C_*\xi\) 阶段余量中。 连同方程 [\[old-eq:2.12\]](#old-eq:2.12)，这就在当前宽度下完成了 中心阶段。

#### 有限归纳的完成

我们通过验证量词次序与有限归纳来收尾。 每个非终端调用都指向一个子结点，其名义宽度 \(M'\) 见 方程 [\[old-eq:2.13\]](#old-eq:2.13)，至少比其父结点低 \(\sigma\)。 所声明的行宽为 \(M'_{\rm act}\)，且所有非例外 矩输入长度都在指定的支撑与截断 操作之后取定。例外原始尺度保持为形式的，不被截断。 两个频率包围、聚合支撑误差以及这些 截断至多把宽度比较改变 \(C_*\xi\)。将其 选在 \(\sigma/2\) 以下。于是每个非空子结点都有非负 宽度，并留出其长度为 \(\sigma/4\) 的带。空的 非零频率区间被丢弃；恰在尺度一以下的非空形式区间已由其 外含长度与截断误差所包含。

在每个更小的宽度处，方程 [\[old-eq:2.1a\]](#old-eq:2.1a)–[\[old-eq:2.1b\]](#old-eq:2.1b) 在自然正槽估计之前删除固定的额外掩码。 无限制的零槽 断言通过对至多两个平面作反射而从填充核心一次性 地推出。中心比较只在其带中调用较早的非中心 阶段，并利用其严格余量。每个 Gauss 范数至多 有一次放大，其误差直接进入第二 变换。方程 [\[old-eq:3.16\]](#old-eq:3.16) 对每个 实际自然子结点调用一次，且在 其所有边界缺陷都已包含在 \(F_{\rm act}\) 中之后。因此没有同带循环。 上面定义的整数 \(D\) 把严格调用界为 \(D-2\)， 因为每次都将宽度从至多为 \(M_{\max}\) 的初始 宽度降低至少 \(\sigma/2\)。

这里说明为何 \(C_*\) 与网格可以独立于 固定的槽数来选取。方程 [\[eq:centered-aggregate-support\]](#eq:centered-aggregate-support) 把任意槽子集的整个对数误差界为 \(\theta_N=H_N/\log Z\)。每个被提取的普通幂都被精确 度量，且一个非例外矩形中两种可能的普通截断中的每一种， 在三角不等式之后，都有一个固定的 端点误差。例外计算使用原始减少量与 不交子集界，而不作截断。第一与第二频率包围只用到 它们各自的一个聚合外尺度与一个公共行二进段。所有 局部账本都是上面所展示的固定聚合长度列表中 仿射表达式的仿射部分或正部。它们的数值 Lipschitz 常数不依赖于 \(N\)；局部 \(F_2\) 不等式与根式计数使用精确的素理想范数。特别地， 正槽仿射表达式的变化至多为 \[|\Delta M|+|\Delta A|+5|\Delta z|,
 \label{old-eq:2.1j}\] 因为 \(0\le6\kappa-1\le5\)。\(z\) 的总变化在 使用此不等式之前已被聚合。这些观察给出 一个数值 \(C_*\)，并按每阶段固定的运算次数 而放大，使得所有频率、正规化与边界 误差都被 \(C_*\xi\) 覆盖。单个贪心前缀至多贡献 \(\eta\)，而非每个被移除的槽贡献一个 \(\eta\)。

解析分离不引入 \(\xi\) 的导数阶数倍数。 在固定的全乘积对数盒上，径向核为 \(\widehat\Phi_i(R_{\rm sc}\exp(L(\mathbf x)))\)，其中 \(L\) 是 行对数范数与整列对数范数中的一个固定 线性型。每个导数都是 \(\widehat\Phi_i\) 的 Euler 导数的一个固定组合。 引理 [\[lem:kernel-seminorms\]](#lem:kernel-seminorms) 对所有 \(R_{\rm sc}>0\) 一致地界住它们，并具有任意指定的径向下衰减与导数阶数。 对 \(R_{\rm sc}\le Z^\xi\) 不使用较弱的界 \(R_{\rm sc}^J\)。 在其所展示的中心幂被提取之后，一个逆根 在固定盒上为 \((q_u/Z^{a_0})^{-1/2}\)；其导数只付出 依赖于 \(H_N\) 与其阶数的固定常数。 引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 使用完整的加权 Fourier 积分，而非在 \(Z^\xi\) 以下高度上的上确界。所需的某个 高度阶数 \(J\) 可以依赖于 \(N\)，它提高一个输入 半范数阶数与一个固定常数，而不提高一个 \(Z^{J\xi}\) 指数。 反射类似地作用在至多两个具固定 gamma 形状的平面上；更大的导数阶数提高有限的半范数与高度 阶数，而上圆环的子份额 \(\xi/2\) 保持固定。 方程 [\[old-eq:3.5\]](#old-eq:3.5) 中的固定多项式高度因子 以所需有限阶数由这些加权 Fourier 测度积分，而不改变先前选定的 \(Z\) 的指数。

离散标签计数也只使用一次。对一族公共支撑、除子或 分配提取其所展示的指数后，在应用分离元组半范数之前， 将其绝对加权计数测度除以该 总质量。这就留下一个质量至多为 1 的 测度；其已提取的指数不再在光滑范数中计入。 每个 Fourier 测度由全乘积构造而对 活跃标签是公共的。

###### 在指定槽数之前的选择。

按以下次序选取参数。首先，从有界 实范围与 \(\epsilon\) 出发，选取 \(\rho,\sigma,\delta>0\)，其中 \(\delta\) 相对于 \(\rho,\sigma\) 很小，使得 \[T_{\rm term}:=\rho+\delta+\rho/6+3\sigma+5\sigma/3<\epsilon/4.\] 这界住一个终端宽度下界、对角或例外损失； 所展示的频率与数值支撑修正则属于每阶段的 \(\xi\) 余量。取如上所述的 \(D\) 与 \(C_*\ge1\)， 仍在指定 \(N\) 或其固定剖面之前，选取 \[\begin{aligned}
 \xi&<\min\left\{\frac\delta2,\frac\rho{30},
                  \frac{\sigma}{4C_*},
                  \frac{\epsilon}{16C_*D}\right\},\\
 \eta&<\min\left\{\frac\sigma6,
                   \frac{\epsilon}{16C_*D}\right\},\qquad
 \epsilon_0<\frac{\epsilon}{16C_*D}.
 \end{aligned}
 \label{old-eq:2.1i}\] 这些选择使严格下降至少为 \(\sigma/2\)，保持 比较余量与填充核心，并对 \(\kappa\in[3/4,1]\) 一致。

###### 固定槽系统的选择。

现在固定任一个不依赖 \(Z\) 的 \(N\)、算术数据与剖面 窗口。构造 \(H_N\) 以及直至深度 \(D\) 的有限 全支撑盒。它们的固定因子 \(\exp(O(H_N))\) 归入 常数。在施加最终阈值 \(\log Z\ge C H_N/\xi\)、 方程 [\[eq:centered-reflection-length\]](#eq:centered-reflection-length) 中的阈值以及 方程 [\[eq:centered-localization-threshold\]](#eq:centered-localization-threshold) 之后，所有出现的 列、根式与掩码范数都有有界的对数范围， 且与移动标签无关。在这些范围内，用局部份额选取每一个 任意小的幂估计，使得一阶段内份额之和至多为 \(\epsilon_0\)。 这些份额可以依赖于 \(N\)。 例如，掩码删除中两个除子质量与至多 \(N\) 个冻结槽 质量可以各用一个份额 \(\epsilon_0/(10(N+2))\)。在素理想估计中，主 平方指数恰为 \(\kappa z\)，围道位移 代价为 \(2e z\)，其中 \(z\) 总量有界，而非 \(N\eta\)。为 \(e\) 选取其被分配的份额；固定的特征展开与 \(\log Z\) 的幂在一个依赖于 \(N\) 的阈值之后被吸收。 同样的推理在个别 \(z_i\) 趋于零时适用， 因为 \(P_i\ge1\)。对除子分配使用全局界 \(\tau_{N+2}(v)^C\ll_{N,C,a}q_v^a\) 与 \(C_N^{\omega(v)}\ll_{N,a}q_v^a\)，其中 \(a>0\) 充分小， 而非在每个素理想处有固定损失。Rankin 的固定根式 界用同样的局部份额处理。一个正规化的池 平均在一阶段中只有其单次密度损失。

归纳对这些原始 \(N\) 个槽的每个存活子集 同时进行，且使用同一网格。为使这一点精确，对 \(0\le d\le D-2\)，令 \[\mathcal E_d
 :=T_{\rm term}+(d+1)C_*(\eta+\xi+\epsilon_0)\] 为至多剩下 \(d\) 次严格调用时所允许的误差。 一个终端组（含其有界的反射或比较 预处理）的误差至多为 \(\mathcal E_0\)。一条严格边 及其固定数目的同带运算使用子包络 \(\mathcal E_{d-1}\) 加上至多 \(C_*(\eta+\xi+\epsilon_0)\)，给出 \(\mathcal E_d\)。 方程 [\[old-eq:2.5\]](#old-eq:2.5) 中的 Gauss 余量 \(\epsilon_G\) 表示这个合适的包络与 当前的局部份额；它并非要求用一个依赖于 \(N\) 的损失与一个新网格重新应用矩 引理。三角 不等式把最大误差取到已计入的质量， 而 Cauchy–Schwarz 对两个子结点的误差取平均。 因此沿一条分支只发生一次终端损失，而不是在每个 祖先处。由方程 [\[old-eq:2.1i\]](#old-eq:2.1i)，最大路径误差至多为 \(T_{\rm term}+C_*D(\eta+\xi+\epsilon_0)<\epsilon\)。

最后，逆向穿过这 \(D\) 个阶段来选取所需有限核、反射、素理想与 终端半范数以及多项式高度阶数。上面的完整加权 Fourier 估计与一致 Euler 核估计使每个这样的选择都是有限的。为聚合支撑不等式、 池分离与密度、原始频率尾部以及所有固定 对数损失选取一个最终的下阈值。阶数、常数与阈值可以随 \(N\) 与固定数据增长，但指数比较中的 \(\eta,\xi,D,C_*\) 不增长。

每个新的额外掩码支在冻结列或一个冻结 放大器素理想上，且其对数范数在一阶段内按有界 总长度增加。它在每个子行和中固定。 那里唯一依赖于行的零点是该行的自然零点； 所声明的移动零点保留在固定扭转中并仍被计数。 在深度 \(D\) 上掩码保持为多项式范数。 在例外行上，完整移动并集的冗余部分 与行根式，连同这些额外掩码，构成 公共的多项式大小 \(\mathfrak R_*\)；对它的格抵消 是一致的。固定分子的射线引理控制 \(\mathcal S\) 处的有限选择，而不把移动的好 素理想吸收进固定模。

当此估计与逆矩一起应用时，两个变量中的所有内部 阶数（包括反射核阶数）都先被固定。引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus) 中较晚的外部 Fourier 尾部阶数 位于这一内部传播之外：它只提高 外部输入半范数，而不改变先前固定的内部高度阶数。这就证明了 所断言的有限阶一致性。有限归纳证明了 自然断言，而初始的掩码删除以其完整陈述形式证明了 引理 [\[lem:plain\]](#lem:plain)。

对于后面的物理应用，\(q=0\) 且行 \(u\) 无六次幂因子。若 \(\mathcal S\) 之外的一个素理想在 \(u\) 中的 赋值属于 \(1,\ldots,5\)，则其局部特征的阶为 \(6/\gcd(6,v_p(u))>1\)，于是诱导特征不能属于 \(\Theta\)。因此例外的物理行 支在 \(\mathcal S\) 上；无六次幂因子性使这成为一个 有限集，至多相差有限单位群。对于抽象的移动 扭转，额外的例外行可以通过抵消产生。 它们已被包含在方程 [\[eq:exceptional-row-count\]](#eq:exceptional-row-count) 与固定特征体积论证中。

### 素理想振幅与精化行计数

我们使用当前部分 II 的算术数据与 方程 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 的物理槽。用这些相同的固定 数据实例化节 [6](#sec:detector) 的共享 零点探测器。下文的主因子与误差因子属于 方程 [\[eq:dynamic-compensated-decomposition\]](#eq:dynamic-compensated-decomposition) 中所保留的动态分解； 在该区域之外不宣称任何个别的局部 商。每个所保留的外部坐标都服从 方程 [\[eq:stage-height-allocation\]](#eq:stage-height-allocation) 中的单一高度分配。

#### 素理想振幅

对尺度为 \(P_i=Z^{\ell_i}\) 的一个主物理槽，将其 中心因子写为 \[Q_i(u;z)=P_i^{-1/2}\sum_{p\in1_T}
   \overline{\chi_p(u)}W_i(q_p/P_i)(q_p/P_i)^{z-1}.\] 命题 [\[prop:probe-errors\]](#prop:probe-errors) 中的主部分 \(\mathcal Q_i\) 恰为 \[\mathcal Q_i(u;z)=-\sum_{p\in1_T}\overline{\chi_p(u)}q_p^{z-1}W_i(q_p/P_i)
 =-P_i^{z-1/2}Q_i(u;z).\] 如节 [1](#sec:compensation) 中那样，每个对 \(p\in1_T\) 的求和都保留 同样的允许集 \(\mathcal P_i(Z)\)，包括它对 \(S\) 的排除。 原始零延拓被保留，因此整除 \(u\) 的素理想 不对此主槽有贡献。\(z\) 的实部 位于一个固定有界范围内，其虚部是由 公共高度余量限制的外部频率之一。

<span id="lem:bin-prime-bound" label="lem:bin-prime-bound">\[lem:bin-prime-bound\]</span> 在引理 [\[lem:detector-dyads\]](#lem:detector-dyads) 的假设下，且素理想 圆环的 Mellin 频率已包含在其累积余量中， 对每个 \(\epsilon_1>0\) \[|Q_i(u;z)|\ll_{\mathcal A,e,\epsilon_1}
 U^{\epsilon_1}P_i^{a-1/2+O(e)}.\] 隐含的 \(O(e)\) 对 \(51/100\le a\le1\) 与 固定实范围一致。它对行中的每个主槽都 成立。

展开 \(1_{p\in1_T}=|T|^{-1}\sum_{\theta\in\widehat T}\theta(p)\)。 每个所得的素理想特征都属于 \(\mathcal X_u\)。 引理 [\[lem:logarithmic-control\]](#lem:logarithmic-control) 应用于带缓冲的圆盘， 把其在 \(\Re s=a+8e\) 上的对数导数界为 \(O_{\mathcal A,e}(\log U)\)；被删除乘积的对数导数 有同样的界。相应的光滑 von Mangoldt 圆环的 Mellin 反演只在所保留的中心范围内平移，在 正规化之后给出 \(U^{\epsilon_1}P_i^{a-1/2+O(e)}\)。 纯扭转 \((q_p/P_i)^{i\Im z}\) 在附加的 Mellin 频率 被截断之前被转译为对数导数变量。连接段的实 长度有界。在它们之上，对数导数为 \(O_{\mathcal A,e}(\log U)\)，位于其所分配的缓冲内，而 在起始直线 \(\Re s=2\) 上它 是绝对有界的。对连接段的无扭转变换应用 方程 [\[eq:pointwise-mellin-tail\]](#eq:pointwise-mellin-tail) 中的逐点估计， 对绝对直线尾部应用方程 [\[eq:late-fourier-tail\]](#eq:late-fourier-tail)。 在它们的固定 多项式尺度与高度界之后选取外部阶数，即得所断言的估计。

要从 von Mangoldt 系数过渡到素理想，将 圆环权除以 \(\log(P_i y)\)。在固定圆环上， \[(y\partial_y)^j\frac1{\log(P_i y)}
 =\frac{(-1)^j j!}{\{\log(P_i y)\}^{j+1}},\] 因此对充分 大的 \(P_i\) 这保持每个固定的光滑半范数，而不引入依赖 导数阶数的 \(P_i\) 幂。有界的 \(P_i\) 由绝对 计数处理。素理想幂 在中心正规化之后贡献 \(P_i^{o(1)}\)，因为它们在 范数圆环中的个数为 \(O(P_i^{1/2+o(1)})\)。 多项式大小的穿刺及其零延拓已 包含在对数导数中。这证明了该界。

下面是一个精确的振幅细分。选取固定的分箱宽度 \(\vartheta>0\)。在槽长度固定之后，先减小 \(e\) 与 \(\epsilon_1\)， 使得对所有充分大的 \(Z\)，前面的界至多为 \(P_i^{\delta/2+\vartheta}\)。 这是可能的，因为 \(\log U/\log P_i=d/\ell_i\) 对每个固定网格保持在 一个固定有界范围内。对一个满足 \(Q_i\ne0\) 的主槽，令 \[g_i=\min\left\{\frac{\delta}{2},
   \max\left(0,\vartheta
     \left\lfloor\frac{\log|Q_i|}{\vartheta\log P_i}\right\rfloor
   \right)\right\}.\] 若 \(Q_i=0\) 则令 \(g_i=0\)，并且对来自 方程 [\[old-eq:5.13e\]](#old-eq:5.13e) 的误差槽也令 \(g_i=0\)。则对一个主槽， \[|Q_i|\le P_i^{g_i+\vartheta},\qquad
 g_i>0\ \Longrightarrow\ |Q_i|\ge P_i^{g_i}.\] 对 \(g_i=0\) 的槽不宣称下界。 有限多个可能的向量 \((g_i)\)（端点值可能取 \(\delta/2\)） 将各行划分为振幅 分箱。用下式定义它们的长度加权平均： \[q=\frac{\sum_i\ell_i g_i}{\ell},\qquad
 0\le q\le\delta/2,\qquad \ell=\sum_i\ell_i.
 \label{old-eq:6.6}\] 此 \(q\) 记录素理想振幅；它不是辅助四阶矩中记为 \(q\) 的导子 指数。

#### 选定的素槽位与行计数

使用方程 [\[eq:part-II-bootstrap\]](#eq:part-II-bootstrap) 中的 \(\Delta\) 与 \(\kappa\)： \[0<\Delta\le\frac1{24},\qquad
 \kappa=2\beta_*-1=\frac34+2\Delta\in(3/4,5/6],\qquad
 \alpha:=\frac56.\] 参数 \(\kappa\) 保持动态；\(\alpha\) 是来自六次幂放大的固定斜率。由于 \(\kappa<1\) 且 \(\beta_*=(1+\kappa)/2\)，引理 [\[lem:plain\]](#lem:plain) 的正槽位假设以等号成立。方程 [\[eq:part-II-bin-ceiling\]](#eq:part-II-bin-ceiling) 对当前的 Part II 分箱给出 \(\delta\le\kappa\le\alpha\)，包括 可能的端点 \(\delta=\alpha\)。

固定一个动态与幅度分箱，并固定外部物理 Mellin 参数。用 \(z_{\rm phys}\) 表示固定的第三个 Mellin 参数，于是物理槽位为 \(Q_i(u;z_{\rm phys})\)。 所有 \(g_i\)，从而 \(q\)，现在都在其行和内固定。 在基 \(U\) 处，槽位 \(i\) 的长度为 \(w_i=\ell_i/d\)，可用总长度为 \(\ell/d\)。 对于请求的长度 \(0\le z\le\ell/d\)，将正的 \(g_i\) 按递减顺序排列，并按该顺序以分数方式填充 \(z\)。 所获得的指数至少为 \(qz\)：若正槽位足以 填满 \(z\)，其初始加权平均至少为所有槽位的 平均 \(q\)；否则将它们全部保留给出 增益 \(q\ell/d\ge qz\)。去掉那个可能为分数的 槽位至多损失 \((\max_i w_i)\delta/2\)。因此，长度至多为 \(z\) 的 整正槽位的一个固定子集满足 \[\left|\prod_{i\ {\rm selected}}Q_i\right|^2
 \ge U^{2qz-\delta\max_iw_i}.\] 当需要一个严格矩不等式时，我们先将 \(z\) 替换为 \(z-\nu_0\)，其中 \(\nu_0>0\) 为固定的小量，或当 \(z\le\nu_0\) 时不选取任何槽位。在此显示式中所致的损失至多为 \(2q\nu_0+\delta\max_iw_i\)，除所述的零容量 邻域之外，在那里将使用未加权矩。两种损失 都可以做得比任何预先给定的正幂更小。

选定的因子恰好具有矩所要求的系数类。 如有必要，对两个见证因子（包括其 剖面）取共轭，并将其行特征写为 \(\psi(n)=\nu(n)\overline{\chi_n(u)}\)，\(\nu\in\Theta\)。 相对于此行，一个物理素数的系数为 \[\overline{\nu(p)}1_{p\in1_T}
 =\frac1{|T|}\sum_{\theta\in\widehat T}
       (\overline{\nu}\theta)(p).\] 这是 \(\Theta\) 中成员的固定有限组合； 它独立于固定行和中的移动行。 没有要求 \(\eta(p)=1\)。 因子 \((q_p/P_i)^{z_{\rm phys}-1}\) 是其光滑剖面的一部分。 在掩码之前，底层的素支撑保持不相交。 带标记的矩允许此负的公共行定向。 为应用引理 [\[lem:plain\]](#lem:plain)（其行特征具有正 定向），对两个 plain 见证因子与所有选定的素因子的 整体乘积取共轭。其绝对平方 不变，且其公共行特征变为 \(\overline{\psi(n)}=\overline{\nu(n)}\chi_n(u)\)。 两个见证剖面与每个选定的槽位剖面都被共轭， 且每个选定的槽位系数变为 \(\nu(p)1_{p\in1_T}\)，再次是 \(\Theta\) 中成员的 固定有限组合。取共轭保留所有零延拓与底层 素支撑。它还保持诱导特征是否 属于 \(\Theta\)，因为 \(\Theta\) 是一个群。 见证高度与物理高度不必相等。对逐行见证参数 应用引理 [\[lem:smooth-calculus\]](#lem:smooth-calculus)， 在固定物理参数与选定指标之后。 对这些参数的求导只插入对数剖面 权重。代价是 \(1+T_1\) 的固定幂，对 移动行与外部标签一致。每个保留的大行都在 \(\Theta\) 之外诱导，因为它在 \(S\) 之外的某个素数处分歧。 因此引理 [\[lem:plain\]](#lem:plain) 的 \(z>0\) 族条件成立。

对于实际的 plain 长度 \(m\le1/2\)，其在有效行宽为一处 来自引理 [\[lem:plain\]](#lem:plain) 的最大零损失 容量为 \[z_P(m)=\frac{1-2m}{6\kappa}
       =\frac{1-2m}{9/2+12\Delta}.
 \label{eq:plain-zero-loss-capacity}\] 的确，该矩被应用于 plain 见证的两份拷贝， 因此其条件为 \(2m+6\kappa z\le1\)。 对于长度为 \(r<1\) 的逆见证，令 \(z_M(r)=(1-r)/2\)。我们只在引理 [\[lem:marked\]](#lem:marked) 中的第二个 严格不等式也具有固定余量处使用此容量。

<span id="prop:detector-counts" label="prop:detector-counts">\[prop:detector-counts\]</span> 设 \(\mathcal B\) 为一个固定的动态与幅度分箱，由保留的 无六次幂因子的物理行 \(q_u\asymp U=Z^d\) 组成，其中 \(a>51/100\)、\(0<\delta=2a-1\le\alpha\)，平均幅度 \(q\in[0,\delta/2]\)。令 \(x=q/\delta\)，故 \(0\le x\le1/2\)， 并定义 \[D_x=3-\frac{17x}{9},\qquad
 P_x=\left(2-\frac{8x}{9}\right)(1-x).\] 假设可用的总素长度以固定的正量超过 \(7/37\)。 对每个 \(t\in[1,3/2]\) 与每个 \(\epsilon>0\)，可仅用 \(\epsilon,\Delta\) 及有界实范围选取 容量减量与槽位网格，使得 \[\#\mathcal B\ll_{\mathcal A,\epsilon}
 U^{\max\{R_{\rm short}(t),L(t)\}+\Delta/4+\epsilon}
 (1+T_1)^{A_{\mathcal A}},\] 其中 \(A_{\mathcal A}<\infty\) 对移动行一致，且 \[R_{\rm short}(t)=1-\delta+\frac{\delta P_x}{D_x}(3/2-t),
 \qquad
 L(t)=1-\delta+(\alpha-\delta)(t-1).\] 该估计对命题 [\[prop:detector-witness\]](#prop:detector-witness) 的逐行见证成立， 并带有其高度条件。若未选取任何素槽位，则 \(t=1\) 转而给出 \[\#\mathcal B\ll_{\mathcal A,\epsilon}
 U^{1-2\delta/3+\epsilon}(1+T_1)^{A_{\mathcal A}},\] 无需素供给假设。在零逆容量处使用 引理 [\[lem:inverse-amplification\]](#lem:inverse-amplification)；在零 plain 容量处使用 引理 [\[lem:plain\]](#lem:plain) 的零槽位情形。

按见证表示与二进对进行细分。选择数 为 \(O_{\mathcal A}((\log U)^2)\)；余下的 逐行光滑参数由前述 Sobolev 论证处理。在一个细分中进行，仍将其记为 \(\mathcal B\)，并设 \(r,m\) 为命题 [\[prop:detector-witness\]](#prop:detector-witness) 中的 实际长度。每当所选 槽位满足相应的矩假设且总请求 容量为 \(z\) 时，其尖峰与各个见证 尖峰蕴含，在扣减预备损失之后， \[\begin{array}{ll}
 \#\mathcal B
 \ll U^{1-\delta r-2qz+\epsilon}(1+T_1)^{A_{\mathcal A}},
 &\text{来自引理~\ref{lem:marked}},\\[2mm]
 \#\mathcal B
 \ll U^{1-2\delta m-2qz+\epsilon}(1+T_1)^{A_{\mathcal A}},
 &\text{来自引理~\ref{lem:plain}}.
 \end{array}\] 在第二行中使用 \(S_m\) 的两份拷贝，因此分母 为 \(|S_m|^4\)，而非 \(|S_m|^2\)。有效宽度为一， 因为扭 \(\nu\) 在行和内固定且无 移动的导子根式。每个公式都包含任意 小的容量、取整、矩与见证损失。

###### 未选素数的逆见证。

每当未选取任何逆槽位时，转而使用引理 [\[lem:inverse-amplification\]](#lem:inverse-amplification) 的 六次幂放大。它适用于 这些物理行，因为它们的理想赋值至多为 五，且其原始零延拓不变。在当前 细分之后，\(U,t,D,D_*\) 是公共的，且逆基 剖面为 \[W_{\rm base}(y)=W_1(y)V_{\le}(Dy/D_*).\] 其固定的对数半范数一致有界：第二个 因子的导数在其缩放自变量位于 固定紧区间处有支撑。余下的逐行参数为 固定紧区间内的 \(\sigma\) 以及纯扭 \(-(\gamma-\nu)\)，其绝对值至多为 \((3I+1)T_1\)。 因此引理 [\[lem:inverse-amplification\]](#lem:inverse-amplification) 的逐行断言 在该高度范围内适用。将其因子 \((1+(3I+1)T_1)^A\) 替换为 \((3I+2)^A(1+T_1)^A\) 只改变一个固定常数。

为清晰起见，即便 \(r\) 随 \(U\) 趋于一， 此用法也是一致的。若 \(0\le r\le R_0\)，带有预备损失 \(\epsilon_0\) 的 方程 [\[eq:amplified-note\]](#eq:amplified-note) 的指数为 \[\max\left\{1,\frac{1+5(1+c)r}{6}\right\}
       +(1+r)\epsilon_0
 \le e(r)+\frac{5cR_0}{6}+(1+R_0)\epsilon_0,
 \qquad e(r)=\max\left\{1,\frac{1+5r}{6}\right\}.\] 对于请求的损失 \(\epsilon_m>0\)，例如取 \(c=3\epsilon_m/(10\max\{R_0,1\})\) 与 \(\epsilon_0=\epsilon_m/(4(1+R_0))\)。它们在 \(U\) 之前固定，且两个额外项至多为 \(\epsilon_m/2\)。 因此除以逆见证尖峰给出 \[\label{eq:no-slot-inverse-count}
 \begin{aligned}
 \#\mathcal B&\ll
 U^{e(r)-\delta r+\epsilon}(1+T_1)^{A_{\mathcal A}},\\
 e(r)-\delta r&=
 \begin{cases}
  1-\delta r,&0\le r\le1,\\
  1-\alpha+(\alpha-\delta)r,&r\ge1.
 \end{cases}
 \end{aligned}\] 特别地，这不是对具有收缩余量 \(1-r\) 的严格带标记 矩的应用。

###### 无需选定素数的情形。

我们首先处理见证已在未选取素数的情况下给出 所需计数的情形。 对 \(r\ge1\)，方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count) 使用有效 矩指数 \((1+5r)/6=1-\alpha+\alpha r\)。 除以逆尖峰给出 \(1-\alpha+(\alpha-\delta)r\)。 由于 \(\delta\le\alpha\) 且 \(r\le t+O(\epsilon)\)，这至多 为 \[L(t)=1-\alpha+(\alpha-\delta)t
     =1-\delta+(\alpha-\delta)(t-1)
 \label{eq:long-count}\] 精确到 \(O(\epsilon)\)。这包括 \(r=1\)，此时 方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count) 中的两个 分支一致。 若 \(m\ge1/2\)，引理 [\[lem:plain\]](#lem:plain) 的零槽位情形 给出计数指数 \(1-2\delta m\le1-\delta\)。 由于 \(R_{\rm short}(t)\ge1-\delta\)，这也满足 所述的界。因此，对于余下的论证我们可以假设 \[r<1,\qquad m<1/2.\] 此时两个容量 \(z_M(r)\) 与 \(z_P(m)\) 都是正的； 当其中任一相对于固定减量太小时，我们将在下文使用其 未加权估计。

###### 比较正容量。

对于逆容量 \(z_M(r)\)，所得到的理想指数 为下文的 \(A_I(r)\)。为比较 plain 指数，先将 \(z_P(m)\) 替换为其在 \(\Delta=0\) 处的值，即 \(2(1-2m)/9\)。由于实际的 \(m\) 至少为 \(t-r-O(\epsilon)\)，所得理想比较指数为 \[\begin{aligned}
 A_I(r)&=1-\delta\{x+(1-x)r\},\\
 S_t(r)&=1-\delta\left\{\frac{4x}{9}
          +\left(2-\frac{8x}{9}\right)(t-r)\right\}.
 \end{aligned}
 \label{eq:selected-counts}\] 实际的 plain 指数 \(1-2\delta m-2q(1-2m)/(9/2+12\Delta)\) 及其基线 版本都关于 \(m\) 递减：它们的导数分别为 \[-2\delta+\frac{4q}{9/2+12\Delta}<0,\qquad
 -2\delta+\frac{8q}{9}<0.\] 因此对 \(m\) 作 \(O(\epsilon)\) 替换是合法的。

方程 [\[eq:selected-counts\]](#eq:selected-counts) 中的两个仿射表达式 相交于 \[r_*(t)=
 \frac{(2-8x/9)t-5x/9}{D_x}.\] 这里 \(D_x\ge37/18>0\)。直接计算， \[r_*(3/2)=1,\qquad
 r_*(1)=\frac{2-13x/9}{3-17x/9}\ge\frac{23}{37},\] 且 \[t-r_*(t)=\frac{(1-x)t+5x/9}{D_x}.\] 最后一个表达式关于 \(t\) 递增，在 \(t=3/2\) 处等于 \(1/2\)，而在 \(t=1\) 处为 \((1-4x/9)/(3-17x/9)\ge1/3\)。 因此，在所述范围内， \[r_*(t)\ge\frac{23}{37},\qquad
 \frac13\le t-r_*(t)\le\frac12,\qquad r_*(t)\le1.\]

当 \(r\le r_*(t)\) 时使用 plain 计数，当 \(r_*(t)\le r<1\) 时使用逆计数，固定小的 零容量邻域内除外。在逆的一侧 \(r\ge23/37\)。 将 \(z_M(r)\) 减去 \(\nu_0\) 后， \[1-r-2z\ge2\nu_0>0,\qquad
 3-2r-8z=4(1-r-2z)+(2r-1)>0.\] 第二个不等式在其正的首项之前具有至少 \(9/37\) 的 余量。这些恰是引理 [\[lem:marked\]](#lem:marked) 在行宽为一处的两个严格宽度 条件。 逆容量至多为 \((1-23/37)/2=7/37\)。在 plain 一侧， \(m\ge1/3-O(\epsilon)\)，故其容量至多为 \(2/27+O(\epsilon)\)。在 \(d=h\) 处可用长度为 \[\frac{\ell}{h}=\frac8{39},\qquad
 \frac8{39}-\frac7{37}=\frac{23}{1443}>0.\] 因此，所假设的正供给余量与足够精细的网格 允许刚刚作出的每一次选取。

在 plain 一侧，将基线容量替换为 方程 [\[eq:plain-zero-loss-capacity\]](#eq:plain-zero-loss-capacity) 中的实际容量，会使 计数指数提高 \[\begin{split}
 2q(1-2m)
 \left(\frac29-\frac1{9/2+12\Delta}\right)
 &=\frac{24q(1-2m)\Delta}{(9/2)(9/2+12\Delta)}\\
 &\le\frac{\Delta}{4}+O(\epsilon).
 \end{split}
 \label{eq:capacity-comparison}\] 对于该不等式，使用 \(m\ge1/3-O(\epsilon)\)、\(2q\le1\)， 以及每个分母的下界四。\(O(\epsilon)\) 项中的 常数是一致的。

加权平均 \[\begin{aligned}
 R_{\rm short}(t)
 &=\frac{(2-8x/9)A_I(r)+(1-x)S_t(r)}{D_x}\\
 &=1-\delta+\frac{\delta P_x}{D_x}(3/2-t)
 \end{aligned}
 \label{eq:short-crossing-count}\] 独立于 \(r\)：\(r\) 的系数相消，且 权重之和为 \(D_x\)。它是在 \(r_*(t)\) 处的公共值。 由于 \(S_t\) 关于 \(r\) 递增而 \(A_I\) 递减， 所选的短计数至多为 \(R_{\rm short}(t)+\Delta/4+O(\epsilon)\)。

###### 小容量与结论。

若 \(r<1\) 但 \(z_M(r)\le\nu_0\)，使用 \(e(r)=1\) 的同一无槽位 估计给出 \[1-\delta r\le1-\delta+2\delta\nu_0.\] 若 \(z_P(m)\le\nu_0\)，则 \(1-2m\le6\kappa\nu_0\le6\nu_0\)，其计数至多为 \(1-\delta+6\delta\nu_0\)。由于 \(R_{\rm short}(t)\ge1-\delta\)， 在给定的 \(\epsilon\) 内选取 \(\nu_0\) 可保持 短界。最后，\(r=1/2-O(\epsilon)\) 与 \(t\ge1\) 迫使 \(m\ge1/2-O(\epsilon)\)，故同样的未加权 plain 估计适用。不请求任何负容量。 连同无需选定素数的情形，在加上有限多个细分之后， 这就证明了所述的选定计数。

最后，不使用素槽位并取 \(t=1\)。对逆的 一侧使用方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count)，包括 对所有 \(r\le1\) 的 \(e(r)=1\)；对 plain 一侧使用 引理 [\[lem:plain\]](#lem:plain) 的零槽位情形。取选择增益为零， 即在两条比较式中取 \(x=0\)，作同样的短计算， 给出 \(R_{\rm short}(1)=1-2\delta/3\)；长界为 \(L(1)=1-\delta\)。两个输入都没有素供给假设， 从而证明了最后的断言。

方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count) 的推导只用到 命题 [\[prop:detector-witness\]](#prop:detector-witness) 与 引理 [\[lem:inverse-amplification\]](#lem:inverse-amplification) 中的逆尖峰。因此它可以对满足这些假设的 共享探测器的任意实例重复，独立于 当前的 Part II 分箱上限。从而，对每个固定的 \(t\in[1,3/2]\)，方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count) 中的界 在具有来自该命题的实际见证的固定保留行动态 分箱的每个固定表示/二进细分上成立，每当 \[a>51/100,\qquad 1/50<\delta=2a-1\le1,\] 且 \(r\) 位于给定的有界非负范围内。它使用 公共逆剖面 \(W_{\rm base}\)、逐行参数界， 以及前述证明中用到的见证损失与高度假设， 但既不要求 \(\delta\le\alpha\) 也不要求素供给假设。此结论 不包含下界分箱 \(a=51/100\) 中的所有行，这些行不必 具有实际见证。

命题 [\[prop:detector-counts\]](#prop:detector-counts) 中的公式描述了下文所需的 唯一行指数。基数因子 \((1+T_1)^{A_{\mathcal A}}\) 在此保持显式。我们验证 引理 [\[lem:late-height-closure\]](#lem:late-height-closure) 所要求的 额外依目标的高度上限。设 \(\epsilon_{\rm ht}>0\) 为 已与实损失一同选取的有限多个探测器高度容差 的最小值。对固定目标，在内部剖面 阶数固定之后，设 \(A_{{\rm ht},\eta}\ge0\) 支配其有限多个 高度阶。令 \[\tau_{0,\eta}:=
 \frac{d_{\min}\epsilon_{\rm ht}}{20(A_{{\rm ht},\eta}+1)}>0.\] 对 \(0<\tau\le\tau_{0,\eta}\)，\(T_1=Z^\tau\)，且 \(Z\) 充分大 时，不等式 \(U\ge Z^{d_{\min}}\) 给出 \[(1+T_1)^{A_{{\rm ht},\eta}}
 \le 2^{A_{{\rm ht},\eta}}Z^{d_{\min}\epsilon_{\rm ht}/20}
 \le U^{\epsilon_{\rm ht}/10}.\] 因此此上限强制所有前述的探测器高度假设。 它在外部尾部阶与 \(Z\) 之前固定；增大该 阶只改变外部检验半范数，而不改变这些内部高度 阶。于是引理 [\[lem:late-height-closure\]](#lem:late-height-closure) 作出最终高度 选择，而不改变正实余量或槽位网格。

### 八分之七界

我们完成 Part II 中所假设的矛盾。回顾 方程 [\[eq:part-II-bootstrap\]](#eq:part-II-bootstrap) 与 [\[eq:part-II-bin-ceiling\]](#eq:part-II-bin-ceiling) 可知 \[0<\Delta=\beta_*-\frac78\le\frac1{24},\qquad
 \kappa=\frac34+2\Delta\le\frac56,\qquad
 \delta=2a-1\le\kappa\] 对每个保留的分箱成立。补偿低估计是 命题 [\[prop:probe-low\]](#prop:probe-low)。对同一物理探针，我们先将 其高展开式的主项正规化，然后界定余下的 行，并验证命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion) 所要求的 与目标无关的余量。

几何量与 Mellin 指数为 \[h=\frac{13}{16},\qquad \ell=\frac16,\qquad
 l_x=\frac{17}{48},\qquad l_y=\frac{23}{48},\qquad
 h=1-l_x+\ell,\] \[C(s)=C_{\mathrm{II}}(s)=s-\frac{11}{16},
 \qquad C(7/8)=\frac3{16}.\] 这些就是方程 [\[old-eq:5.1\]](#old-eq:5.1) 与 [\[eq:part-II-mellin-target\]](#eq:part-II-mellin-target) 中的值。将节 [5](#sec:local-compensation) 中 称为 \(x\) 的局部变量记作 \(s\)；下文的幅度比 \(x=q/\delta\) 是另一个不同的实数。

使用定义 [\[def:stage-high-data\]](#def:stage-high-data)，取 \[\mathscr I_\eta(Z)=I_{\eta,\mathrm{modified}}(Z),\qquad
 \mathfrak H_{\eta,u,Z}(s,w,z)
     \ \text{如方程~\eqref{eq:holomorphic-selected-tuple} 中}.\] 在共享解析引理中取 \(\sigma_0=7/8\)。 节 [5](#sec:local-compensation) 验证这些数据的每一部分： 方程 [\[eq:compensated-poisson-identity\]](#eq:compensated-poisson-identity) 是对 方程 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 中独立定义的有限表达式的绝对 收敛高恒等式，且全修正项在两个所需的 Euler 区域内 全纯，并满足 方程 [\[eq:stage-all-height-majorant\]](#eq:stage-all-height-majorant)。排除集、物理 行掩码与校准均不变。特别地，在此全修正项之外没有 额外的 Euler 因子。其标量 分母为 \(L_F^S(s,\eta\overline{\chi_\bullet(u)})\)，其 Gaussian 为 \(\Phi(s+z-1)\)。

在下文的估计中，\(0<e<10^{-3}\) 是一个容许的探测器宽度。 它的最终选取，连同余下的实损失，在 结尾的选择次序中作出。

#### 主正规化因子

我们验证引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 的两个修正假设。 首先，方程 [\[eq:principal-local-tuple-bound\]](#eq:principal-local-tuple-bound) 给出 \[|\mathfrak H_{\eta,1,Z}(s,w,z)|\ll Z^{\ell\Re z}\] 在第二个 Euler 区域内的每个固定实盒上对所有虚部一致成立。 特别地，它在方程 [\[eq:principal-correction-bound\]](#eq:principal-correction-bound) 中的整个 矩形上以高度阶零成立。 这是对完整元组修正项的界。

对于留数值，定义 \[S_i(Z)=\sum_{p\in\mathcal P_i(Z)}W_i(q_p/P_i)q_p^{-5/6},
 \qquad P_i=Z^{\ell_i}.\] 引理 [\[lem:ray-prime-normalizer\]](#lem:ray-prime-normalizer)（包括其关于删去 一个固定有限集的断言）给出 \[S_i(Z)\sim\frac{P_i^{1/6}}{|T|\log P_i}
       \int_0^\infty W_i(y)y^{-5/6}\,dy.\] 每个首项常数都是正的。由于槽位数固定， 对所有充分大的 \(Z\)，所有 \(S_i(Z)\) 都是正的，允许 一个依赖于固定数据的公共下阈值。令 \[\label{eq:principal-scalar}
 A_T(Z)=(-1)^K Z^{-\ell/6}\prod_{i=1}^K S_i(Z).\] 利用 \(\log P_i=\ell_i\log Z\) 与 \(\sum_i\ell_i=\ell\)，我们得到 \[A_T(Z)\sim
 \frac{(-1)^K}{|T|^K(\log Z)^K}
 \prod_{i=1}^K\left\{\frac1{\ell_i}
       \int_0^\infty W_i(y)y^{-5/6}\,dy\right\}.\] 从而在该范围内 \(A_T(Z)\ne0\)，且 \[|A_T(Z)|\asymp_{T,K,(\ell_i,W_i)}(\log Z)^{-K},
 \qquad |A_T(Z)|^{-1}\ll_\epsilon Z^\epsilon\] 对每个 \(\epsilon>0\)。下阈值可以依赖于目标的 有限排除集；这里没有使用移动的射线导子中的 一致素数渐近。

在主第二 Euler 区域上，节 [5](#sec:local-compensation) 定义 \(\mathcal B_p=G_p/H_p\)，其中 \(H_p\ne0\)，且 方程 [\[eq:principal-local-approximation\]](#eq:principal-local-approximation) 给出 \(\mathcal B_p=-1+O(q_p^{-7/8})\)，对所有虚部与 目标单位相位一致成立。将方程 [\[eq:principal-slot-factorization\]](#eq:principal-slot-factorization) 中的 主因子分解在 \(w=1,z=1/6\) 处应用， 即便原先对 \(P_p\) 的商未定义它仍然成立。 它给出 \[\mathfrak H_{\eta,1,Z}(s,1,1/6)
 =H_\eta(s)\prod_{i=1}^K
       \left(\sum_{p\in\mathcal P_i(Z)}
           W_i(q_p/P_i)q_p^{-5/6}\mathcal B_p\right),\] 其中 \(H_\eta\) 是方程 [\[eq:shared-principal-data\]](#eq:shared-principal-data) 中 针对同一排除集 \(S\) 的函数。由 \(W_i\) 的非负性，其第 \(i\) 个 槽位等于 \[-S_i(Z)\{1+\rho_i(s)\},\qquad
 |\rho_i(s)|\ll P_i^{-7/8}
 \quad(\Re s=\beta_*+e,\ \Im s\in\mathbb R).\] 的确，绝对局部误差之和至多为 \(P_i^{-7/8}S_i(Z)\) 的固定倍数。选取任意预目标数 \[0<\kappa_P<\frac78\min_i\ell_i.\] 由于 \(K\) 固定，\(\mathcal R_{\eta,Z}(s):=\prod_i(1+\rho_i(s))-1\) 在该整条直线上满足 \(|\mathcal R_{\eta,Z}(s)|\ll Z^{-\kappa_P}\)。 因此精确的留数修正为 \[\mathfrak H_{\eta,1,Z}(s,1,1/6)
 =H_\eta(s)Z^{\ell/6}A_T(Z)\{1+\mathcal R_{\eta,Z}(s)\},\] 即方程 [\[eq:principal-correction-residue\]](#eq:principal-correction-residue)，其中 \(A_\eta=A_T\) 且 \(\mu=\kappa_P\)。此因子分解只在 主留数处断言；它不是用于一般 围道移动的修正。

设 \(c_S>0\) 为方程 [\[eq:shared-principal-data\]](#eq:shared-principal-data) 中的标量， 其正性是引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 的一部分。 对充分大的 \(Z\)，定义正规化物理探针 \[J_{\mathrm{II},\eta}(Z)
   =\frac{I_{\eta,\mathrm{modified}}(Z)}{c_S A_T(Z)}.\] 它不同于 \(J_{\mathrm I,\eta}\)，且其分子与 正规化因子都独立于分析高度 \(T_1\)。 命题 [\[prop:probe-low\]](#prop:probe-low) 与 \(A_T^{-1}\) 的次幂界 给出，对每个 \(\epsilon>0\)， \[\label{eq:part-II-normalized-low}
 |J_{\mathrm{II},\eta}(Z)|
 \ll_{\eta,\epsilon} Z^{C(7/8)+\epsilon}.\] 同一个标量被用于高比较。

按照方程 [\[eq:shared-principal-nonvanishing\]](#eq:shared-principal-nonvanishing) 所需选取固定截断。相关的 \(H_\eta\) 在 \(\Re s>7/8\) 上全纯，在该处满足收缩性，并使用同一个 \(S\)。令 \(\mathscr P_{\mathrm{II},\eta}\) 表示方程 [\[eq:compensated-poisson-identity\]](#eq:compensated-poisson-identity) 中 \(u=1\) 的项，并置 \[f_{\mathrm{II},\eta}(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds.\] 引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 的所有假设现已在 \(\sigma_0=7/8\) 下得到验证。其余项估计为 \[\begin{split}
 \left|\frac{\mathscr P_{\mathrm{II},\eta}(Z)}{c_S A_T(Z)}
       -f_{\mathrm{II},\eta}(Z)\right|
 \ll{}&
 Z^{C(\beta_*)+(1+h)e-m_w+\epsilon}
 +Z^{C(\beta_*)+e-m_z+\epsilon}\\
 &+Z^{C(\beta_*)+e-\kappa_P+\epsilon},
 \end{split}\] 其中两个几何余量为 \[\label{old-eq:5.14}
 m_w:=\frac{l_y}{20}=\frac{23}{960},\qquad
 m_z:=\frac h{600}=\frac{13}{9600}.\] 引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 包含留数路径、标量 Jacobian 以及主积分的右移。特别地，最后一项是在其原始全局线上估计的误差； 它不属于 \(f_{\mathrm{II},\eta}\)。该信号与物理探针都独立于 \(T_1\)。

#### 补偿后的高指数

低阶估计与主行比较现在涉及延拓准则所需的函数 \(J_{\mathrm{II},\eta}\) 与 \(f_{\mathrm{II},\eta}\)。尚需证明，对某个公共的 \(\sigma>0\)， \[\left|\frac{I_{\eta,\mathrm{modified}}(Z)
                -\mathscr P_{\mathrm{II},\eta}(Z)}{c_S A_T(Z)}\right|
 \ll_\eta Z^{C(\beta_*)-\sigma}.\] 我们首先相对于原始尺度 \(Z^{C(7/8)}\) 估计这些非主贡献。除以 \(c_S A_T(Z)\) 的代价是一个任意小的幂，在最终选取余量时一次性预留。

<span id="lem:high-bin" label="lem:high-bin">\[lem:high-bin\]</span> 设 \(0<d_{\min}<d_{\max}<\infty\)，令 \(U=Z^d\) 且 \(d_{\min}\le d\le d_{\max}\)，并令 \(\mathcal B\) 为一个固定动态分箱 \((i,a)\) 中保留的非主物理行 \(q_u\asymp U\) 的有限集。置 \(\delta=2a-1\)。假设引理 [\[lem:buffered-bins\]](#lem:buffered-bins)、[\[lem:detector-dyads\]](#lem:detector-dyads) 与 [\[lem:bin-prime-bound\]](#lem:bin-prime-bound) 的分箱与高度假设成立，其中 \(0<e<10^{-3}\)、\(T_1=Z^\tau>2\)、\(0<\tau\le d_{\min}/100\)，且采用 方程 [\[eq:stage-height-allocation\]](#eq:stage-height-allocation) 中的累积分配。 有界实范围、正的损失 \(e,\vartheta,\epsilon\) 以及槽位系统都在目标之前固定。

对每个保留的外部参数元组与每个误差槽位子集，把 \(\mathcal B\) 逐点划分为节 [8.1](#sec:amplitudes) 的振幅集，以及（当使用见证计数时） 节 [8.2](#sec:selection) 的见证细分。假设每个这样的集合 \(\mathcal C\) 具有主槽位均值 \(q\in[0,\delta/2]\)，如方程 [\[old-eq:6.6\]](#old-eq:6.6) 中那样，并且 \[\#\mathcal C\ll_{\mathcal A,\epsilon}
 U^{R+\epsilon}(1+T_1)^{A_{\mathcal A}},\] 在保留的元组与移动标号上一致。出现的 \(R,q\) 取值范围为一个固定有界集， 可以依赖于逐点集、\(d,a\) 与 \(\beta_*\)，但除此之外不依赖于目标。 对每个出现的对，定义 \[\label{eq:common-high-exponent}
 \begin{split}
 E(d)
 &=a-\frac78+h\left(\frac{17}{50}-\frac16\right)
       -a l_y-(1-a)\ell-(\delta/2-q)\ell
       +d\left(R+\frac\delta2-\frac{17}{50}\right)\\
 &=C_0+\frac23\delta+\frac q6-h(1-R)
       +(d-h)\left(R+\frac\delta2-\frac{17}{50}\right),
       \qquad C_0=-\frac1{48}.
 \end{split}\] 若 \(\mathcal B\ne\varnothing\)，令 \(E_{\max,Z}(d)\) 为在所有保留元组上、 对所有逐点集取这些值的上确界。

在中心围道 \[\Re s=a+16e,\qquad \Re w=1-a-6e,\qquad \Re z=\frac{17}{50},\] 上，原始固定动态分箱和的贡献被 \[Z^{C(7/8)+E_{\max,Z}(d)+O(e+\vartheta+\epsilon)}
 (1+T_1)^{A'_{\mathcal A}},\] 所界，其中 \(\vartheta\) 是振幅分箱宽度，且 \(A'_{\mathcal A}<\infty\) 在移动标号上一致。空分箱的贡献为零。 \(O(e+\vartheta+\epsilon)\) 项中的常数只依赖于有界实范围与固定槽位系统， 而不依赖于目标。不宣称单个逐点集的单独积分。固定 \(\tau>0\) 之后， 所有被舍弃的外部片段与衔接都是 \(O_{\mathcal A,N}(Z^B T_1^{-N})\)， 对某个固定的 \(B\) 与每个固定的 \(N\)。

我们验证引理 [\[lem:bin-contour-accounting\]](#lem:bin-contour-accounting) 的中心假设，它为刚才指定的 完整修正提供围道移动及其尾部。其分箱上界由 方程 [\[eq:part-II-bin-ceiling\]](#eq:part-II-bin-ceiling) 成立。物理的 \(\Im z\) 坐标包含在其高度分配中，因为它进入素剖面。其余见证、二进与 素环带坐标就是节 [8.2](#sec:selection) 的估计中所用的固定有限列表。 其完整的逐点界包含在全局线或绝对线上被舍弃的辅助积分。因此 方程 [\[eq:stage-height-allocation\]](#eq:stage-height-allocation) 中的单一累积分配适用， 而无需在之后的估计中重新申请配额。

仅在保留的围道上，命题 [\[prop:probe-errors\]](#prop:probe-errors) 给出 方程 [\[eq:dynamic-compensated-decomposition\]](#eq:dynamic-compensated-decomposition) 中的分解。 对 \(I\subseteq\{1,\ldots,K\}\)，其被加项为 \[\mathfrak H_{\eta,u,Z}^{(I)}
 =\mathcal H_{\eta,u}(s,w,z)
       \prod_{i\in I}\mathcal D_i(u)
       \prod_{i\notin I}\mathcal Q_i(u;z).\] 所需的反射本原分子界由分子表示及其共轭的带缓冲估计，连同 引理 [\[lem:deleted-euler-factors\]](#lem:deleted-euler-factors) 得出，正如命题 [\[prop:probe-errors\]](#prop:probe-errors) 之前所验证的。保留的 \(w\) 高度落在其允许集内。每个保留的分子都是非主的。

固定一个保留元组上的一个振幅集。对一个主槽位， \(\mathcal Q_i=-P_i^{z-1/2}Q_i\) 且 \(\lvert Q_i\rvert\le P_i^{g_i+\vartheta}\)。对一个误差槽位赋值 \(g_i=0\)。 方程 [\[old-eq:5.13e\]](#old-eq:5.13e) 把 \(I\) 中的所有误差槽位与分子一起界住； 其证明同时对不同的严格分歧标号使用方程 [\[old-eq:5.13d\]](#old-eq:5.13d) 中的 实际导子亏量。它不是对每个槽位单独的分子配额。由于 \(\mathcal H_{\eta,u}\ll_\epsilon U^\epsilon\)，在选取预备幂之后， 将这些估计相乘得到 \[\begin{split}
 \left|L^S(w,\chi_\bullet(u))
       \mathfrak H_{\eta,u,Z}^{(I)}(s,w,z)\right|
 \ll{}&U^{\delta/2+O(e)+\epsilon}(1+T_1)^{A_1}\\
 &\cdot
 Z^{\ell(17/50-1/2)+q\ell+O(e+\vartheta+\epsilon)}.
 \end{split}\] 这里 \(A_1<\infty\) 是目标与槽位系统的一个固定高度阶，且 \(\sum_i\ell_i g_i=q\ell\)，包括对误差所赋的零。没有使用误差槽位的下界。

乘以假定的基数即证明方程 [\[eq:stage-central-bound\]](#eq:stage-central-bound) 在 \(g=q\ell\) 下成立，只要取 \(\varepsilon_c\) 为 \(e+\vartheta+\epsilon\) 的一个固定的 足够大的倍数。该倍数只依赖于固定槽位系统与有界实范围。共有 \(2^K\) 个误差子集。振幅向量的数目固定，见证二进选择只贡献 \(1+\log Z\) 的一个固定幂。因此所需的逐点重数界成立。这些集合只在 引理 [\[lem:bin-contour-accounting\]](#lem:bin-contour-accounting) 用 \(\mathfrak H\) 移动了原始动态分箱和 之后才形成。它们不用于延拓，也不单独积分。

以 \(\sigma_0=7/8\) 与 \(g=q\ell\) 应用 引理 [\[lem:bin-contour-accounting\]](#lem:bin-contour-accounting)。它在 方程 [\[eq:stage-high-exponent\]](#eq:stage-high-exponent) 中的指数为 \[a-\frac78+h\left(\frac{17}{50}-\frac16\right)-a l_y-\frac{\ell}{2}
       +q\ell+d\left(R+\frac\delta2-\frac{17}{50}\right).\] 因为 \(-(1-a)\ell-(\delta/2-q)\ell=-\ell/2+q\ell\)， 这就是方程 [\[eq:common-high-exponent\]](#eq:common-high-exponent) 的第一行。 代入几何关系与 \(a=(1+\delta)/2\) 即得第二行。 特别地 \(q\ell=q/6\) 是一个以 \(Z\) 为底的指数，而非 \(dq/6\)。 在选取剩余的预备幂之后，方程 [\[eq:stage-central-contribution\]](#eq:stage-central-contribution) 中的 显式误差在有界 \(d\)-范围上为 \(O(e+\vartheta+\epsilon)\)。 其上确界正是陈述中的那个。引理 [\[lem:bin-contour-accounting\]](#lem:bin-contour-accounting) 还给出 所述的外部尾部，其尺度次数在 \(N\) 之前固定。

底部分箱 \(a=51/100\) 有 \(\delta_0=1/50\)，且不需要零见证。理想计数 \(R=1\) 连同 \(q\le\delta_0/2\) 给出 \[\label{eq:floor-bound}
 E(h)\le C_0+\frac34\delta_0=-\frac7{1200}<0.\] 其频率斜率 \(R+\delta_0/2-17/50\) 为正，因此这界住每个 \(d\le h\)。 略高于 \(h\) 的小扩展将在下面加以控制。

#### 小行范数与大行范数

置 \(d_{\min}=1/100\)。引理 [\[lem:compensated-absolute-local-bounds\]](#lem:compensated-absolute-local-bounds) 界住完整选取元组的正和，其中每个 \(G_p\) 在取绝对值之前被保留。 在小行线 \[\Re s=\beta_*+e,\qquad \Re w=1/2,\qquad \Re z=17/50\] 上，方程 [\[eq:absolute-local-tuple-bound\]](#eq:absolute-local-tuple-bound) 给出 \[|\mathfrak H_{\eta,u,Z}(s,w,z)|
 \ll_\epsilon U^\epsilon\prod_iP_i^{17/50}
 =U^\epsilon Z^{17\ell/50},\] 在所有虚部上一致。这就是方程 [\[eq:small-correction-bound\]](#eq:small-correction-bound)， 其高度次数为零。它在个别局部因子的零点处仍然成立。 引理 [\[lem:outer-row-tails\]](#lem:outer-row-tails) 的数据已在上面验证过，因此它适用于 这些二进对中的每个物理行 \(u\ne1\)。其分类包含非平凡的单位分子， 并允许主分母；这里不使用零点探测器见证或选取的矩。

相对指数中不依赖于 \(d\) 的部分是 \[\label{eq:small-frequency-margin}
 h\left(\frac{17}{50}-\frac16\right)-\frac{l_y}{2}
 =-\frac{79}{800}.\] 方程 [\[eq:small-row-bound\]](#eq:small-row-bound) 中的行指数为 \(63/50<2\)。因此，方程 [\[eq:small-row-sum\]](#eq:small-row-sum) 中相对于 \(C(\beta_*)\) 度量的 小二进和，其指数至多为 \[-\frac{79}{800}+2d_{\min}+O(e+\epsilon)
 =-\frac{63}{800}+O(e+\epsilon).\] 在可调的实损失取得足够小之后，它是负的。记 \(m_{\rm small}:=63/800\) 表示这个固定的无误差节省。

对大的行，固定 \(z_\infty>2\)。在 \((\Re s,\Re w,\Re z)=(2,2,z_\infty)\) 上，同一个 方程 [\[eq:absolute-local-tuple-bound\]](#eq:absolute-local-tuple-bound) 给出 \[|\mathfrak H_{\eta,u,Z}(s,w,z)|
 \ll_\epsilon U^\epsilon Z^{\ell z_\infty}\] 对每个物理行与所有虚部成立。这验证了 方程 [\[eq:large-correction-bound\]](#eq:large-correction-bound)。因此，引理 [\[lem:outer-row-tails\]](#lem:outer-row-tails) 在 \(B_0=l_x/2+1+l_y=53/32\) 下给出 \[|\mathscr R_\eta(U;Z)|
 \ll Z^{B_0+hz_\infty+\epsilon}U^{1+\epsilon-z_\infty},\] 并且，在选取 \(0<\epsilon<z_\infty-1\) 之后，对每个固定的 \(\zeta>0\)， \[\sum_{U>Z^{h+\zeta}}|\mathscr R_\eta(U;Z)|
 \ll
 Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon}.\] 这里 \(\mathscr R_\eta\) 是引理 [\[lem:outer-row-tails\]](#lem:outer-row-tails) 对 当前物理表达式的行贡献。固定的足够大的 \(z_\infty\) 使最后的指数达到所需的负值。它在 \(\zeta\) 之后、目标之前选取。这些引用使用无商元组界 （见节 [5](#sec:local-compensation)），而不是中心的主/误差分解。

#### 端点不等式

接下来我们界 \(E(h)\)，首先不考虑可调损失或高度因子。 它们将按量化的选择次序恢复。回顾 \[\kappa=\frac34+2\Delta,\qquad \alpha=\frac56.\] 在活动上端点 \(\delta=\alpha\) 处，在 命题 [\[prop:detector-witness\]](#prop:detector-witness) 中取 \(t=3/2\)。于是 \(r\ge1-O(\epsilon)\)。在 \(r=1\) 的两侧应用 方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count) 中的无槽位放大估计。 对 \(r\ge1\)，其指数为 \[1-\alpha+(\alpha-\delta)r=1-\delta.\] 对所述 \(O(\epsilon)\) 邻域内的 \(r<1\)，同一估计使用 \(e(r)=1\)， 故其指数为 \(1-\delta r\le1-\delta+O(\epsilon)\)。固定的放大余量 独立于该邻域。因此不需要选取素数，理想行指数为 \(R=1-\delta\)。在方程 [\[eq:common-high-exponent\]](#eq:common-high-exponent) 中使用 \(q\le\delta/2\) 给出 \[E(h)\le C_0+\left(\frac34-h\right)\delta+O(\epsilon)
       =-\frac1{48}-\frac{\delta}{16}+O(\epsilon)<0.
 \label{eq:large-delta-endpoint}\]

现在假设 \(1/50<\delta<\alpha\)。置 \(x=q/\delta\in[0,1/2]\)， 并使用命题 [\[prop:detector-counts\]](#prop:detector-counts) 中的 \(D_x,P_x,R_{\rm short},L\)。参数 \(\kappa\) 保持动态值 \(3/4+2\Delta\)，而不是上界 \(5/6\)。因此该命题中所用的实际普通容量为 \[z_P(m)=\frac{1-2m}{6\kappa}
       =\frac{1-2m}{9/2+12\Delta},\] 如方程 [\[eq:plain-zero-loss-capacity\]](#eq:plain-zero-loss-capacity) 中那样。方程 [\[eq:capacity-comparison\]](#eq:capacity-comparison) 中的比较针对这一确切容量，除所要求的小损失外，至多把行指数提高 \(\Delta/4\)。定义 \[\mathcal J=(\alpha-\delta)D_x+\delta P_x,\qquad
 t=1+\frac{\delta P_x}{2\mathcal J},\qquad
 R_*=L(t).
 \label{eq:target-cutoff}\] 分母为正。事实上 \[\frac{37}{18}\le D_x\le3,\qquad
 \frac79\le P_x\le2,\qquad
 D_x-P_x=1+x-\frac{8x^2}{9}>0,\] 从而 \[\frac{35}{54}\le\mathcal J\le\frac52.\] 因为 \(0<\delta<\alpha\)，有 \(\mathcal J>\delta P_x>0\)，故 \(1<t<3/2\)。 此外， \[D_x\{R_{\rm short}(t)-L(t)\}
 =\delta P_x(3/2-t)-(\alpha-\delta)D_x(t-1)
 =\frac{\delta P_x}{2}-\mathcal J(t-1)=0.\] 于是 \(R_*=R_{\rm short}(t)=L(t)\)，且这个 \(t\) 平衡了两个计数。 这些公式还具有所述的闭端点值：在 \(\delta=\alpha\) 处，有 \(\mathcal J=\alpha P_x\)、\(t=3/2\) 与 \(R_*=R_{\rm short}(3/2)=L(3/2)=1-\delta\)。相应的交叉 有 \(r_*(3/2)=1\)，故其逆容量为零。前面的 等式论证在该边界处使用方程 [\[eq:no-slot-inverse-count\]](#eq:no-slot-inverse-count)，而不是 带有消失余量的带标记估计。

<span id="lem:balanced-endpoint" label="lem:balanced-endpoint">\[lem:balanced-endpoint\]</span> 对 \(0\le\delta\le5/6\) 与 \(0\le x\le1/2\)，由 方程 [\[eq:target-cutoff\]](#eq:target-cutoff) 定义 \(\mathcal J,t,R_*\)，其中 \(\mathcal J>0\)，并令 \(E_*\) 为取 \(q=x\delta\) 与 \(R=R_*\) 的 \(E(h)\)。则 \[-E_*\ge\frac{49}{440640}>\frac1{10000}.\] 特别地，该界在范围 \(1/50<\delta\le5/6\) 上一致，包括闭端点。

置 \(y=1/2-x\in[0,1/2]\) 与 \(v=51+41y\)。为验证该 计算，记 \[p_y=7+18y+8y^2,\qquad
 j_y=185+170y+(-138+12y+96y^2)\delta.\] 则 \[D_x=\frac{37+34y}{18},\qquad
 P_x=\frac{p_y}{9},\qquad
 \mathcal J=\frac{j_y}{108}.\] 由 \(R_*=1-\delta+(\alpha-\delta)\delta P_x/(2\mathcal J)\) 与方程 [\[eq:common-high-exponent\]](#eq:common-high-exponent)， \[-E_*=
 \frac{1+(3+8y)\delta}{48}
 -\frac{13}{32}\,
   \frac{(5/6-\delta)\delta P_x}{\mathcal J}.\] 展开相乘得到显式的二次式 \[\begin{split}
 10368\mathcal J(-E_*)
 &=2j_y[1+(3+8y)\delta]
     -468(5/6-\delta)\delta p_y\\
 &=10(37+34y)
   -8(237+377y+26y^2)\delta\\
 &\hspace{12mm}
   +48(51+131y+94y^2+32y^3)\delta^2.
 \end{split}\] 乘以 \(v\) 并配方得到 \[\begin{aligned}
 10368v\mathcal J(-E_*)
 ={}&(3+5y)\bigl\{(4v\delta-79)^2+49\bigr\}\\
 &+4y\bigl\{
 4v\delta[(1+3y)(15+32y)\delta+9-13y]
       +265+3485y\bigr\}.
 \end{aligned}
 \label{eq:balanced-endpoint-certificate}\] 这个恒等式也可以通过系数来验证：将其右端展开为 \(\delta\) 的多项式，分别给出 \[\begin{split}
 &10v(37+34y),\\
 &-8v(237+377y+26y^2),\\
 &48v(51+131y+94y^2+32y^3),
 \end{split}\] 它们分别是前一个展示式中的常数、一次与二次系数乘以 \(v\)。

方程 [\[eq:balanced-endpoint-certificate\]](#eq:balanced-endpoint-certificate) 右端的每一项都非负： \(y,\delta\ge0\) 且 \(9-13y\ge5/2\)。 第一行至少为 \(49(3+5y)\)，而 \(v=51+41y\le17(3+5y)\)。因此 \[-E_*\ge\frac{49}{176256\mathcal J}
       \ge\frac{49}{440640}>\frac1{10000},\] 其中用到 \(\mathcal J\le5/2\)。

\(D_x\) 与 \(\mathcal J\) 的下界界住了交叉与截断在紧参数范围上的所有导数。 饱和损失是一致的，因为 \(\delta\ge1/50\)， 且逆选择具有命题 [\[prop:detector-counts\]](#prop:detector-counts) 中所证明的显式供给与宽度余量。 在零容量处，其未加权界与 \(1-\delta\) 之差至多为 所选容量减量的一个常数倍。由于 \(R_*\ge1-\delta\)，这些情形遵循相同的比较。 因此，一旦所有探测器、分箱与取整误差各自所要求的损失至多为 \(\epsilon\)，它们合计为 \(O(\epsilon)\)，且其常数不依赖于目标。 令 \(E_{\rm actual}(h)\) 表示在代入观察到的行界 \(R\le R_*+\Delta/4+\epsilon_{\rm row}\) 之后，相对于 \(C(7/8)\) 的尺度指数。目前显式高度因子仍在此外。 方程 [\[eq:common-high-exponent\]](#eq:common-high-exponent) 中 \(R\) 的系数 为 \(d\)，故在 \(d=h\) 处容量替换贡献 \(h\Delta/4\)。记 \(\epsilon_{\rm total}\) 为 \(h\epsilon_{\rm row}\) 与所有其他可调实损失之和；前述 一致性使其具有不依赖于目标的系数、且可任意小。该证书给出 实际所需的比较： \[\begin{split}
 E_{\rm actual}(h)-\Delta
 &\le-\frac{49}{440640}-\left(1-\frac h4\right)\Delta
       +\epsilon_{\rm total}\\
 &=-\frac{49}{440640}-\frac{51}{64}\Delta
       +\epsilon_{\rm total}.
 \end{split}
 \label{eq:adaptive-endpoint}\] 减去 \(\Delta=C(\beta_*)-C(7/8)\) 是本质的： 该证书并不是断言对每个 \(\Delta\) 都有 \(E_{\rm actual}(h)<0\)。 当高度因子在下面被转换为预留的指数配额时，该配额被加到 \(\epsilon_{\rm total}\) 上。

#### 频率范围

对 \(1/2\le d\le h\)，可用长度为 \[\frac{\ell}{d}\ge\frac8{39}>\frac15>\frac7{37}.\] 从以 \(Z\) 为底换到以 \(U\) 为底，把槽位长度从 \(\ell_i\) 变为 \(\ell_i/d\le2\ell_i\)，故按这个因子二选取的 一个网格在整个区间上满足矩的要求。若 \[0<\zeta<5\ell-h=\frac1{48},\] 则对 \(h<d\le h+\zeta\)，供给仍大于 \(1/5\)，其高于 \(7/37\) 的余量为 \(2/185\)。

对 \(1/50<\delta<\alpha\)，使用理想行上指数 \(R=R_*+\Delta/4\)。对 \(\delta=\alpha\)，使用 \(R=1-\delta\)。两者都至少为 \(1-\delta\)，故 \[R+\delta/2-\frac{17}{50}
 \ge\frac{33}{50}-\frac{\delta}{2}\ge\frac4{25}>0.\] 底部分箱也有正的斜率。因此 \(d=h\) 界住 \(d\le h\) 的所有这些指数。扩展到 \(h+\zeta\) 的代价至多为 \(2\zeta\)：事实上 \[R_*\le1-\delta+\frac{\alpha-\delta}{2}\le\frac{17}{12},
 \qquad
 R_*+\Delta/4\le\frac{139}{96},\] 且 \(139/96+1/2-17/50<2\)。在 \(\delta=\alpha\) 与底部分箱情形处的斜率都小于二。

对 \(d_{\min}\le d\le1/2\) 与 \(\delta\le\alpha\)，取 \(t=1\) 且不使用选取的素数。命题 [\[prop:detector-counts\]](#prop:detector-counts) 给出底部分箱之外的理想指数 \(1-2\delta/3\)。 使用略大的公共指数 \[R=\frac{76}{75}-\frac23\delta.\] 在 \(\delta=1/50\) 处它等于一，因此它也涵盖底部分箱。 其斜率在此范围上为 \(101/150-\delta/6>0\)。 在方程 [\[eq:common-high-exponent\]](#eq:common-high-exponent) 中使用 \(q\le\delta/2\) 得到 \[E(d)\le E(1/2)+O(\epsilon)
 \le-\frac{529}{2400}+\frac{25}{96}\delta+O(\epsilon)
 \le-\frac{49}{14400}+O(\epsilon)<0.
 \label{eq:adaptive-intermediate}\] 中间的表达式由代入 \(d=1/2\)、\(R=76/75-2\delta/3\) 与 \(q=\delta/2\) 得出； 最后一个不等式用到 \(\delta\le5/6\)。 在 \(\delta=\alpha\) 处，方程 [\[eq:large-delta-endpoint\]](#eq:large-delta-endpoint) 中所用的计数 及其正斜率已经控制每个 \(d\le h\)。 连同节 [9.3](#sec:tails)，这些情形覆盖每个 物理行范数。只有 \(d\ge1/2\) 在行矩中使用选取的物理素因子； 在每个范围中，每个物理槽位都保留在高阶修正中。

为与 \(C(\beta_*)\) 比较，从每个理想指数中减去 \(C(\beta_*)-C(7/8)=\Delta\)。 在自适应范围中，这正是方程 [\[eq:adaptive-endpoint\]](#eq:adaptive-endpoint) 中的比较； 其唯一的正容量配额是 \(h\Delta/4\)。其他端点范围在减去 \(\Delta\) 之前具有非正的理想指数。 因此它们都保留不依赖于目标的主高阶余量 \[m_{\rm hi}:=\left(1-\frac h4\right)\Delta
             =\frac{51}{64}\Delta.\] 低指数具有余量 \(m_{\rm lo}:=\Delta\)。 主围道与逼近余量已在节 [9.1](#sec:principal-signal) 中建立； 现在我们一起选取所有损失。

#### 选择次序与结论

最后，我们把不依赖于目标的实选择与依赖于目标的高度及外部检验次数分离。 数值选择仍是本应用的一部分；最终高度选取由 引理 [\[lem:late-height-closure\]](#lem:late-height-closure) 提供。

<span id="prop:parameter-order" label="prop:parameter-order">\[prop:parameter-order\]</span> 在方程 [\[eq:part-II-bootstrap\]](#eq:part-II-bootstrap) 的矛盾之下，存在数 \[0<\omega<\Delta,\qquad \sigma>0\] 以及固定的几何、矩损失、容量减量、槽系统、振幅宽度、分箱宽度 \(e>0\) 和扩张 \(0<\zeta<1/48\)， 所有这些都在目标特征之前选定，并具有下述性质。 对每个本原有限阶目标 \(\eta\)，随后可以选取其固定的算术数据、一个正的高度指数 \(\tau_\eta\)、 一个有限的外部尾阶 \(N_\eta\) 以及一个下阈值 \(Z_{0,\eta}\)，使得对 \(Z\ge Z_{0,\eta}\)， \[|J_{\mathrm{II},\eta}(Z)|\ll_\eta Z^{C(7/8)+\omega},\qquad
 |J_{\mathrm{II},\eta}(Z)-f_{\mathrm{II},\eta}(Z)|
 \ll_\eta Z^{C(\beta_*)-\sigma}.\] 指数 \(\omega,\sigma\) 不依赖于 \(\eta\)。 截断 \(T_1=Z^{\tau_\eta}\) 只出现在估计中，而不出现在这两个函数中的任何一个里。

理想的余量是 \[m_{\rm lo}=\Delta,\qquad m_{\rm hi}=\frac{51}{64}\Delta,\qquad
 m_{\rm high}:=\min\{m_{\rm hi},m_{\rm small}\}>0.\] 主围道余量是方程 [\[old-eq:5.14\]](#old-eq:5.14) 中的 \(m_w,m_z\)。 为 \(m_{\rm lo},m_{\rm high},m_w,m_z\) 中的每一个保留一半。 在紧实参数区间上，乘以所有所需的探测器、矩、容量与舍入损失的系数 都独立于目标而有界。 事实上，\(\delta\ge1/50\)、\(D_x\ge37/18\) 且 \(\mathcal J\ge35/54\)； 二进长度有界，并且命题 [\[prop:detector-counts\]](#prop:detector-counts) 给出了固定的逆宽度与供给余量。 等式 \(\delta=\alpha\) 使用了上面的单独无槽界。 选取矩损失与容量减量，使得它们在高度指数中的总代价小于 \(m_{\rm high}/8\)。

设 \(\eta_{\rm mesh}>0\) 为引理 [\[lem:plain\]](#lem:plain) 对这些损失与有界实区间所提供的网格。 它在 \([3/4,1]\) 上的一致断言特别适用于此处所用的紧闭包 \(\kappa\in[3/4,5/6]\)， 并且该网格不依赖于槽的数目。 只有最终的半范数与高度阶可能依赖于一个固定的槽计数。 设 \(b_{\rm round}>0\) 足够小，使得低于 \(b_{\rm round}\) 的平方尖峰舍入损失 在指数基的有界变化之后代价小于 \(m_{\rm high}/8\)。 选取一个固定的偶整数 \(K\)，使得 \[\frac{2\ell}{K}<
 \min\left\{\eta_{\rm mesh},b_{\rm round},\frac1{185}\right\},
 \qquad \ell_i=\frac{\ell}{K}\quad(1\le i\le K).\] 这些正长度之和为 \(\ell\)，且独立于目标与 \(Z\)。令 \(P_i=P=Z^{\ell/K}\)。 对 \(1\le i\le K\)，令 \[I_i=\left(1+\frac{2i-1}{2K+1},\,1+\frac{2i}{2K+1}\right)\subset(1,2)\] 并选取一个非负、非零的 \(W_i\in C_c^\infty(I_i)\)。 这些区间具有正的间隙。 因此，在施加射线、排除集或行掩码之前，它们的底层素窗口对每个 \(Z\) 都是不相交的。 方程 [\[eq:compensated-probe-definition\]](#eq:compensated-probe-definition) 使每个窗口在每个被加项中保持其原始尺度。

对每个选定的行区间，\(U=Z^d\) 满足 \(d\ge1/2\)，故 \[w_i=\frac{\ell_i}{d}\le\frac{2\ell}{K}<\eta_{\rm mesh},
 \qquad
 \delta\max_iw_i\le\frac{2\ell}{K}<b_{\rm round}.\] 第二个不等式使用了 \(\delta\le5/6<1\)。总可用长度仍为 \(\ell/d\)。 对 \(d\le h\)，它至少为 \(8/39\)，超出 \(7/37\) 达 \(23/1443\)。 对 \(h<d\le h+\zeta\) 且 \(\zeta<1/48\)，它超过 \(1/5\)， 其超出 \(7/37\) 的部分为 \(2/185\)。 因此每个选定的逆容量以及较小的普通容量都得到供给。 额外的界 \(2\ell/K<1/185\) 低于后一间隙的一半。 零容量的邻域（包括等式的端点）使用无槽矩。 实际的环带比将名义长度改变 \(O_K(1/\log U)\)， 这被足够大阈值处的固定严格余量所吸收。

内部的中心放大器也与这些窗口保持分离。 用 \(\sigma_{\rm width}\) 表示引理 [\[lem:plain\]](#lem:plain) 证明中记为 \(\sigma\) 的宽度减量。 该证明使用池指数 \(\ell_*=\sigma_{\rm width}/3\) 以及低于 \(\sigma_{\rm width}/6\) 的网格。 在基 \(U\) 处，每个活跃的物理槽的范数至多为 \(2U^{\eta_{\rm mesh}}\)， 而池从 \(U^{\ell_*}/2\) 开始。 它们固定的指数间隙使这些集合对所有充分大的 \(U\) 都不相交，且在选定的 \(d\)-区间上一致。 带标记的逆矩没有网格条件。

方程 [\[eq:principal-scalar\]](#eq:principal-scalar) 中的正规化因子对这一实际选取非零。 令 \(c_i=\int_0^\infty W_i(y)y^{-5/6}\,dy>0\)。 已在节 [9.1](#sec:principal-signal) 中证明的渐近式特殊化为 \[S_i(Z)\sim\frac{P^{1/6}c_i}{|T|\log P}>0,\qquad
 A_T(Z)\sim
 \left(\frac{K}{|T|\ell}\right)^K
       \left(\prod_i c_i\right)(\log Z)^{-K}>0.\] 符号使用了偶数的 \(K\)。 任何后来的固定排除集只影响公共下阈值，因为其素数最终会离开所有这些窗口。选取 \[\kappa_P=\frac7{16}\frac{\ell}{K}=\frac7{96K},
 \qquad 0<\kappa_P<\frac78\min_i\ell_i=\frac7{48K},
 \qquad m_P:=\kappa_P.\] 因此主逼近有一个在目标之前选定的正余量。 子集的数目、窄窗口的半范数以及它们的有限高度阶可能依赖于这个固定的 \(K\)。

选取振幅宽度、剩余的幂损失以及 \(e\)，使得它们在高度中的总代价小于 \(m_{\rm high}/8\)， 并且使得 \[(1+h)e+\epsilon_{\rm pr}<m_w/4,\qquad
 e+\epsilon_{\rm pr}<m_z/4,\qquad
 e+\epsilon_{\rm pr}<m_P/4.\] 这里 \(\epsilon_{\rm pr}>0\) 包含了主余项估计中所选取的小幂次。 还要求 \(e<10^{-3}\) 以及引理 [\[lem:detector-dyads\]](#lem:detector-dyads) 中的界 \(e_0\)。 槽长度已经固定，因此振幅细分中所需的小幂次可以依据它们的正下界来选取。 所有这些选择只依赖于 \(\Delta\) 与目标前的槽系统。

选取 \[0<\zeta<\min\{1/48,m_{\rm high}/16\}.\] 于是频率扩张的代价至多为 \(2\zeta<m_{\rm high}/8\)。 现在在节 [9.3](#sec:tails) 中选取绝对直线 \(z_\infty>2\) 足够靠右， 使得其大行和相对于 \(C(\beta_*)\) 具有大于 \(m_{\rm high}\) 的节省。 它的指数只依赖于这些实选择，因此 \(z_\infty\) 也先于目标。 选取方程 [\[eq:shared-principal-nonvanishing\]](#eq:shared-principal-nonvanishing) 所需的目标前截断。 在目标固定之后，命题 [\[prop:probe-errors\]](#prop:probe-errors) 所要求的任何额外固定排除素数 都可以添加到 \(S\) 中：同一个正乘积尾控制函数保持共享的压缩， 且 \(T\) 与槽窗口都不改变。

为清晰起见，非主实比较在引理 [\[lem:high-bin\]](#lem:high-bin) 中的所有逐点对上都一致。 设 \(\epsilon_{\rm real}(d)\ge0\) 汇集相关区间所分配的实、网格与矩损失。 端点不等式、中间不等式以及正的斜率给出 \[\label{eq:saving-criterion}
 E(d)+\epsilon_{\rm real}(d)
 \le(\beta_*-7/8)-\varepsilon_{\rm hi},
 \qquad \varepsilon_{\rm hi}>0,\] 对每个出现的 \((R,q)\) 以及每个适中的 \(d\) 成立，同时仍保留 \(m_{\rm high}\) 的一个固定比例。 因此同一不等式对 \(E_{\max,Z}(d)\) 成立，且在 \(Z\) 上一致。 小界与大界各自具有其所陈述的节省。 将次幂正规化因子估计应用一次于非主与外行的贡献， 并使用低于 \(m_{\rm high}/8\) 的幂吸收剩余的有限二进重数。 引理 [\[lem:principal-residue-interface\]](#lem:principal-residue-interface) 已经包含了它自己的正规化因子余量 \(\epsilon_{\rm pr}\)。上面的四个高度实分配代价小于 \(m_{\rm high}/2\)； 这最后一个余量留下超过 \(3m_{\rm high}/8\)。 主不等式为 \(m_w,m_z,m_P\) 中的每一个留下超过 \(3/4\)。因此可以在目标之前固定 \[m=\frac14\min\{m_{\rm high},m_w,m_z,m_P\}>0\] 作为一个在保留高度因子之前的公共剩余高度节省。 对于低估计，以目标前损失 \(\Delta/2\) 应用方程 [\[eq:part-II-normalized-low\]](#eq:part-II-normalized-low)， 并令 \(\omega=\Delta/2\)。 设 \(\epsilon_{\rm ht}>0\) 为已随这些实损失选定的有限多个探测器高度余量中的最小值。

现在固定一个本原目标 \(\eta\)。 选取其容许的固定算术数据以及最终的排除集 \(S\)，包括其导子、公共截断以及刚才描述的进一步固定排除。 物理表达式、\(H_\eta\)、\(c_S\) 以及信号都使用这同一份数据。 群 \(T\) 与槽系统保持独立于目标。 为这份数据固定前面结果所供给的所有内部矩、半范数与 Sobolev 阶。 它们在变动模数、公共掩码与冻结标号上的一致性给出一个有限的 \(A_\eta\)， 它控制所有保留高度因子的乘积，包括二进、素数、分子反射与行计数高度因子。 它独立于任何后来的外部测试阶。 全高度修正界以及共享解析引理中的直接全局或绝对界 同样为所有被丢弃的物理片段给出一个有限的尺度次数 \(B_\eta\)，独立于后来的阶 \(N\)。 将这些片段正规化并对它们的有限多个类型求和，只会增大这个固定的 \(B_\eta\)。

我们使用在节 [8.2](#sec:selection) 末尾验证的高度上界。 设 \(A_{{\rm ht},\eta}\le A_\eta\) 控制有限多个探测器高度阶，必要时增大 \(A_\eta\)，并令 \[\tau_{0,\eta}:=
       \frac{d_{\min}\epsilon_{\rm ht}}{20(1+A_{{\rm ht},\eta})}>0.\] 这个数在目标的保留阶之后、但在 \(N\) 与 \(Z\) 之前固定。若 \(0<\tau\le\min\{d_{\min}/100,\tau_{0,\eta}\}\) 且 \(T_1=Z^\tau\)， 则对 \(U\ge Z^{d_{\min}}\) 与充分大的 \(Z\)， \[T_1\le U^{1/100},\qquad
 (1+T_1)^{A_{{\rm ht},\eta}}
 \le2^{A_{{\rm ht},\eta}}Z^{d_{\min}\epsilon_{\rm ht}/20}
 \le U^{\epsilon_{\rm ht}/10}.\] 由 \(\epsilon_{\rm ht}\) 的定义，这在整个适中区间上证明了引理 [\[lem:detector-dyads\]](#lem:detector-dyads) 中的 每个字面条件 \((1+T_1)^{A_{\mathcal A}}\le U^{\epsilon/10}\)。 第一个界还使探测器的粗略误差 \(U^{-189/100+o(1)}T_1^2\le U^{-187/100+o(1)}\) 趋于零。 每个带缓冲的适中区间都满足 \(d\le h+\zeta<1\)；小行与绝对大行不使用带缓冲的截断。

固定的有限外部坐标列表（包括物理的 \(\Im z\) 坐标）使用方程 [\[eq:stage-height-allocation\]](#eq:stage-height-allocation) 中的单一分配。 它的矩阵由槽系统与有限保留估计固定，且独立于外部导数阶。 对每个这样的 \(\tau\)，二进、见证与素数估计可以如它们各自陈述所允许的那样， 在 \(\tau\) 之后选取其辅助外部阶，使得它们完整的逐点界成立。 在吸收它们被丢弃的部分时选取一个严格的幂间隙； 由此产生的外部半范数常数随后被依赖于 \(\tau\) 的下阈值所吸收。 对任何所要求的剩余阶 \(N\)，这些辅助阶可以进一步增大； 这只改变外部半范数常数与下阈值，而不改变 \(A_\eta\)、\(B_\eta\) 或 \(\tau_{0,\eta}\)。不再对经过外部微分的剖面重新应用内部矩。

因此，结合引理 [\[lem:high-bin\]](#lem:high-bin)、所有行区间以及主余项估计， 对每个固定的 \(N\) 与这个上界区间中充分大的 \(Z\)，得到 \[|J_{\mathrm{II},\eta}(Z)-f_{\mathrm{II},\eta}(Z)|
 \ll_{\eta,N}
 Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}
       +Z^{B_\eta}T_1^{-N}.\] 下阈值允许依赖于 \(\tau,N,\eta\)。 这就是方程 [\[eq:late-height-hypothesis\]](#eq:late-height-hypothesis)。 其低假设是取 \(\omega=\Delta/2\) 的方程 [\[eq:part-II-normalized-low\]](#eq:part-II-normalized-low)， 且这两个函数不包含 \(T_1\)。 以 \(\sigma_0=7/8\)、\(C=C_{\mathrm{II}}\)、这个 \(m\) 以及已验证的上界 \(\tau_{0,\eta}\) 应用 引理 [\[lem:late-height-closure\]](#lem:late-height-closure)。它选取 \(\tau_\eta\)，然后是一个公共的控制外部阶 \(N_\eta\)， 最后是阈值。 它给出所断言的高度估计，其中 \(\sigma=m/2>0\)。 \(\omega\) 与 \(\sigma\) 都在目标之前固定。

命题 [\[prop:parameter-order\]](#prop:parameter-order) 与 方程 [\[eq:shared-principal-nonvanishing\]](#eq:shared-principal-nonvanishing) 验证了命题 [\[lem:continuation-criterion\]](#lem:continuation-criterion) 的假设， 其中 \(\sigma_0=7/8\)、\(J_\eta=J_{\mathrm{II},\eta}\) 且 \(f_\eta=f_{\mathrm{II},\eta}\)。这与 \(\beta_*>7/8\) 矛盾； 因此 \(\beta_*\le7/8\)。取 \(\sigma_0=7/8\) 的命题 [\[prop:hecke-dirichlet-transfer\]](#prop:hecke-dirichlet-transfer) 把本原 Hecke 结论推广到所有有限阶 Hecke 与 Dirichlet \(L\) 函数（允许主极点）， 并证明了定理 [\[thm:main\]](#thm:main)。

<span>99</span>

S. Baier and A. Bansal, *The large sieve with power moduli for \(\mathbb Z[i]\)*, International Journal of Number Theory **14** (2018), no. 10, 2737–2756. [doi:10.1142/S1793042118501658](https://doi.org/10.1142/S1793042118501658); [arXiv:1802.08964](https://arxiv.org/abs/1802.08964).

V. Bhargava, G. Ivanyos, R. Mittal, and N. Saxena, *Irreducibility and deterministic \(r\)-th root finding over finite fields*, Proceedings of the 2017 ACM International Symposium on Symbolic and Algebraic Computation (ISSAC 2017), ACM, 2017, 37–44. [doi:10.1145/3087604.3087620](https://doi.org/10.1145/3087604.3087620); [author manuscript](https://www.cse.iitk.ac.in/users/nitin/papers/irred-and-rth-root.pdf).

K. Billington, M. Cheng, J. Schettler, and A. I. Suriajaya, *The average number of Goldbach representations and zero-free regions of the Riemann zeta-function*, International Journal of Number Theory **21** (2025), no. 2, 289–316. [doi:10.1142/S1793042125500150](https://doi.org/10.1142/S1793042125500150); [arXiv:2306.09102](https://arxiv.org/abs/2306.09102).

V. Blomer, L. Goldmakher, and B. Louvel, *\(L\)-functions with \(n\)-th-order twists*, International Mathematics Research Notices **2014** (2014), no. 7, 1925–1955. [doi:10.1093/imrn/rns257](https://doi.org/10.1093/imrn/rns257); [arXiv:1112.1650](https://arxiv.org/abs/1112.1650).

Clay Mathematics Institute, *Riemann Hypothesis*, Millennium Prize Problems, <https://www.claymath.org/millennium/riemann-hypothesis/>.

C. David, A. de Faveri, A. Dunn, and J. Stucky, *Non-vanishing for cubic Hecke \(L\)-functions*, preprint, arXiv:2410.03048v2 (2026). [arXiv:2410.03048](https://arxiv.org/abs/2410.03048).

P. G. L. Dirichlet, *Beweis des Satzes, daß jede unbegrenzte arithmetische Progression, deren erstes Glied und Differenz ganze Zahlen ohne gemeinschaftlichen Factor sind, unendlich viele Primzahlen enthält*, Abhandlungen der Königlichen Preussischen Akademie der Wissenschaften zu Berlin (1837), 45–81. English translation by R. Stephan, [arXiv:0808.1408](https://arxiv.org/abs/0808.1408).

A. Dunn and M. Radziwiłł, *Bias in cubic Gauss sums: Patterson’s conjecture*, Annals of Mathematics **200** (2024), no. 3, 967–1057. [doi:10.4007/annals.2024.200.3.3](https://doi.org/10.4007/annals.2024.200.3.3); [arXiv:2109.07463](https://arxiv.org/abs/2109.07463).

J. B. Friedlander and D. A. Goldston, *Sums of three or more primes*, Transactions of the American Mathematical Society **349** (1997), no. 1, 287–310. [doi:10.1090/S0002-9947-97-01652-8](https://doi.org/10.1090/S0002-9947-97-01652-8).

S. D. Galbraith, *Mathematics of Public Key Cryptography*, Cambridge University Press, 2012. [doi:10.1017/CBO9781139012843](https://doi.org/10.1017/CBO9781139012843). Section and algorithm references use the author’s extended and corrected version 2.0, [Chapter 2](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch2.pdf).

P. Gao and L. Zhao, *Moments of quadratic Hecke \(L\)-functions of imaginary quadratic number fields*, Journal of Number Theory **209** (2020), 359–377. [doi:10.1016/j.jnt.2019.09.002](https://doi.org/10.1016/j.jnt.2019.09.002); [arXiv:1707.00091](https://arxiv.org/abs/1707.00091).

P. Gao and L. Zhao, *Moments and one level density of sextic Hecke \(L\)-functions*, Functiones et Approximatio Commentarii Mathematici **70** (2024), no. 1, 7–28. [doi:10.7169/facm/2057](https://doi.org/10.7169/facm/2057); [arXiv:2201.01885](https://arxiv.org/abs/2201.01885).

L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, Mathematical Proceedings of the Cambridge Philosophical Society **154** (2013), no. 2, 193–212. [doi:10.1017/S0305004112000370](https://doi.org/10.1017/S0305004112000370); [arXiv:1112.1642](https://arxiv.org/abs/1112.1642).

L. Guth and J. Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics **203** (2026), no. 2, 623–675. [doi:10.4007/annals.2026.203.2.6](https://doi.org/10.4007/annals.2026.203.2.6); [arXiv:2405.20552](https://arxiv.org/abs/2405.20552).

J. Hadamard, *Sur la distribution des zéros de la fonction \(\zeta(s)\) et ses conséquences arithmétiques*, Bulletin de la Société Mathématique de France **24** (1896), 199–220. [doi:10.24033/bsmf.545](https://doi.org/10.24033/bsmf.545).

D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica **72** (1995), no. 3, 235–275. [doi:10.4064/aa-72-3-235-275](https://doi.org/10.4064/aa-72-3-235-275).

D. R. Heath-Brown, *Kummer’s conjecture for cubic Gauss sums*, Israel Journal of Mathematics **120**, part A (2000), 97–124. [doi:10.1007/s11856-000-1273-y](https://doi.org/10.1007/s11856-000-1273-y).

E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen. Erste Mitteilung*, Mathematische Zeitschrift **1** (1918), 357–376; *Zweite Mitteilung*, Mathematische Zeitschrift **6** (1920), 11–51. [doi:10.1007/BF01465095](https://doi.org/10.1007/BF01465095) (first paper).

M. N. Huxley, *The large sieve inequality for algebraic number fields*, Mathematika **15** (1968), no. 2, 178–187. [doi:10.1112/S0025579300002540](https://doi.org/10.1112/S0025579300002540).

T. Kubota, *On automorphic functions and the reciprocity law in a number field*, Lectures in Mathematics, Department of Mathematics, Kyoto University, no. 2, Kinokuniya Book-Store, Tokyo, 1969. <http://hdl.handle.net/2433/84907>.

J. Maynard and K. Pratt, *Half-isolated zeros and zero-density estimates*, International Mathematics Research Notices **2024** (2024), no. 19, 12978–13014. [doi:10.1093/imrn/rnae191](https://doi.org/10.1093/imrn/rnae191); [arXiv:2206.11729](https://arxiv.org/abs/2206.11729).

J. S. Milne, *Class Field Theory*, course notes, version 4.03, 6 August 2020. <https://www.jmilne.org/math/CourseNotes/CFT.pdf>.

OpenAI, *An unconditional first moment for cubic Gauss sums*, OpenAI Math Release preprint [OAI:An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf), 2026.

S. J. Patterson, *A cubic analogue of the theta series*, Journal für die reine und angewandte Mathematik **296** (1977), 125–161. [doi:10.1515/crll.1977.296.125](https://doi.org/10.1515/crll.1977.296.125).

B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, Monatsberichte der Königlichen Preussischen Akademie der Wissenschaften zu Berlin (1859), 671–680. Manuscript, transcription, and translation at <https://www.claymath.org/library/historical/riemann/r.html>.

T. Tao, *The Elliott–Halberstam conjecture implies the Vinogradov least quadratic nonresidue conjecture*, Algebra & Number Theory **9** (2015), no. 4, 1005–1034. [doi:10.2140/ant.2015.9.1005](https://doi.org/10.2140/ant.2015.9.1005); [publisher PDF](https://msp.org/ant/2015/9-4/ant-v9-n4-p09-p.pdf).

J. Thorner and A. Zaman, *A unified and improved Chebotarev density theorem*, Algebra & Number Theory **13** (2019), no. 5, 1039–1068. [doi:10.2140/ant.2019.13.1039](https://doi.org/10.2140/ant.2019.13.1039); [arXiv:1803.02823](https://arxiv.org/abs/1803.02823).

C.-J. de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers. Première partie: La fonction \(\zeta(s)\) de Riemann et les nombres premiers en général*, Annales de la Société scientifique de Bruxelles **20**, deuxième partie (1896), 183–256. Reprinted in *Recherches analytiques sur la théorie des nombres premiers*, Hayez, Brussels, 1897, <https://books.google.com/books?id=7e0GAAAAYAAJ>.
