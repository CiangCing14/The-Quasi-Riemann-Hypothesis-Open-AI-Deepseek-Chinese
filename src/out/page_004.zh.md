1 引言

设 $F = \mathbb{Q}(\sqrt{-3})$，$O$ 为其整数环，对非零整理想记 $N a = |O/a|$ 为其范数。模非零整理想 $f$ 的有限阶 Hecke 特征 $\eta$ 是模 $f$ 的射线类群的一个特征，并通过零延拓到与 $f$ 不互素的理想上。这与通常的有限阶 idelic 定义一致：复素位不贡献非平凡的有限阶连续特征 [22, Chapter VI, Section 1]。对 $\Re s > 1$，置
$$L_F(s, \eta) = \sum_{a \neq 0} \frac{\eta(a)}{(N a)^s} = \prod_{p} \left(1 - \eta(p)(N p)^{-s}\right)^{-1}.$$
同一记号也用来表示其亚纯延拓。对于模 $q$ 的 Dirichlet 特征 $\chi$，通过零延拓到非单位元上，我们同样记
$$L(s, \chi) = \sum_{n \geq 1} \frac{\chi(n)}{n^s} \qquad (\Re s > 1)$$
然后作亚纯延拓；模 1 的特征给出 Riemann zeta 函数 $\zeta(s)$。这里的问题是均匀排除：找一个常数 $\sigma_0 < 1$，不依赖于特征、其导子以及高度，使得这些函数在 $\Re s > \sigma_0$ 内没有零点。

仅对 $\zeta$ 而言，存在固定的 $\sigma_0 < 1$ 使得 $\zeta(s) \neq 0$ 于 $\Re s > \sigma_0$ 这一事实被称为拟 Riemann 假设（quasi-Riemann hypothesis）[3, Section 1]。它要求的是在每个高度都成立的一个间隙，而不仅仅是在 $\Re s = 1$ 上的非零性。对所有 Dirichlet 特征的相应均匀表述出现在 [9, p. 288, Equation (1.4) and the following paragraph]。

这些函数与素数分布之间的联系有着悠久的历史。Dirichlet 于 1837 年对每个既约算术级数中素数无穷性的证明引入了分离剩余类的特征 $L$-级数 [7]。Riemann 1859 年的论文将 $\zeta$ 的零点与素数分布联系起来，并提出了临界线猜想 [25]。Hadamard 与 de la Vallée Poussin 于 1896 年独立证明了 $\zeta$ 在 $\Re s = 1$ 上无零点，从而得到素数定理 [15, 28]。Hecke 随后发展了数域上的特征 zeta 函数及其解析理论 [18]。

Hecke $L$-函数的经典无零点区域随着导子或高度的增大而趋近直线 $\Re s = 1$，并且可能允许一个简单的实例外零点；对于阿贝尔扩张，其精确形式由 [27, Theorem 3.1] 给出。这样的区域不能给出固定半平面内的均匀排除。零点密度估计处理的是另一个问题：它们给出给定竖直线右侧零点数目的上界。例如，Guth 与 Maynard 的大值估计改进了 $\zeta$ 的零点密度上界 [14, Theorem 1.2]，但这些零点密度上界并不能排除每一个零点。

定理 1.1. $F = \mathbb{Q}(\sqrt{-3})$ 上的每个有限阶 Hecke $L$-函数在 $\Re s > 7/8$ 内没有零点。对每个 Dirichlet $L$-函数，包括 $\zeta(s)$，同样成立。主特征在 $s = 1$ 处的极点是被允许的。

特别地，定理 1.1 肯定地解决了拟 Riemann 假设：$\zeta$ 的非平凡零点（即其在 $0 < \Re s < 1$ 内的零点）实部的上确界至多为 $7/8$。边界 $\Re s = 7/8$ 不被包含，而 $(7/8, 1)$ 中的任何例外实零点都被排除。该定理并未建立 Riemann 假设或其推广版本，后者将非平凡零点置于 $\Re s = 1/2$ 上。Riemann 假设仍未解决 [5]。

Kubota 的 metaplectic 理论与 Patterson 的三次 theta 级数提供了自守框架 [20, 24]。我们使用 Dunn 与 Radziwiłł 所记录的无条件显式尖点展开 [8, Section 5 and Appendix A]；他们的 GRH 条件下素数渐近并非本文的输入。相应的一阶矩渐近在一份独立手稿中被无条件证明 [23, Theorem 1.1]；该结果在此也不被使用。命题 5.1 推导出这里所用的反射关系，同时保留了特征在非单位元上的取零限制。
