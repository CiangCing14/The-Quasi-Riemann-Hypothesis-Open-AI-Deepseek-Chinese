因为该和为 $O_c(\varepsilon^{-2})$。振幅误差为 $O_c(\varepsilon)$，阻尼误差同理，由相同的格点估计得到。三者均为 $o(I_\varepsilon)$。相位 $e(-cy^2/4)$ 在模 $2\mathcal{O}$ 下是周期的。在前面的高斯平均中取 $b=2$ 和 $a=qc/4$；其四个类中每一个的归一化均值为 $1/qc$。因此归一化后的右端趋于 $(2|c|)^{-1}\sum_{y \bmod 2} e(-cy^2/4)$，这就证明了式 (4.3)。

代表元 $0, 1, \omega, \omega^2$ 模 $2$ 给出了所述的四项表达式。乘以奇数 $v$ 置换这些类，因此同一公式给出 $\Gamma(cv^2) = \Gamma(c)$。模 $4$ 的单位群阶为 $12$。一个提升模 $4$ 的平方仅依赖于它模 $2$ 的类，其三个可能的平方为 $1, \omega, \omega^2$。陈述中的四个代表元模该子群互不相同；又 $\lambda^2 = -3 \equiv 1 \pmod 4$。将四项表达式作用于它们即得所述表格。将 $\Gamma(ab)/(\Gamma(a)\Gamma(b))$ 作用于两个生成元 $-1, \lambda$ 即得所显示的指数，从而证明了最后的论断。

引理 4.4（六次互反律与固定高斯相位）。对于 $S$ 外互素的主元 $a, b$，
$$\chi_b(a) = R(a, b)\chi_a(b), \quad R(a, b) = r(a, b).$$
在 $S$ 外的所有主元对上，包括非互素对，用式 (4.4) 的双特征 $r$ 定义 $R$。在 $S$ 外的每个主指数上定义
$$G(c) = \overline{\chi_c(4)}\Gamma(c).$$
它的模为 $1$，且通过一个支撑在 $2, 3$ 上的固定射线群分解。对于所有这样的 $v, w$，
$$G(vw) = G(v)G(w)R(v, w), \qquad G(1) = 1. \qquad (4.5)$$
此外 $G(v^2) = \chi_v(4)$，且在好素数处
$$G(p^3) = \gamma_3(p), \qquad R(p, p) = \gamma_3(p)^2 = \chi_p(-1). \qquad (4.6)$$
在 $S$ 外的每个主元 $n$ 上，有 $\chi_n(-1) = R(n, n)$。对角线映射 $t \mapsto R(t, t)$ 是固定射线群的一个特征。在式 (4.4) 的平方类记号中，它是 $r(-1, n)$，其中 $-1$ 表示其模 $4$ 的剩余平方类，而非单位理想 $(-1)$ 的理想射线类。对于无平方因子 $c$，完整的高斯恒等式为
$$\gamma_2(c)^3 = \mu(c)\alpha(c), \quad \gamma_1(c)\gamma_2(c) = \mu(c)\alpha(c)G(c), \quad G(c) = \overline{\chi_c(4)}\gamma_3(c), \quad |G(c)| = 1. \qquad (4.7)$$
$G$ 在非无平方因子指数上的所有出现均指刚刚定义的有限射线函数，而非非无平方因子的高斯和。

证明。在好素数处，对剩余域中的平方根计数给出
$$\sum_{x \bmod p} e(x^2/p) = \sum_{y \bmod p} (1 + \chi_p(y)^3)e(y/p) = \sum_{y \bmod p} \chi_p(y)^3 e(y/p).$$
不含特征的加性求和为零。因此 $\Gamma(p) = \gamma_3(p)$，且对于单位 $u$，将 $x^2/p$ 替换为 $ux^2/p$ 会使该和乘以 $\chi_p(u)^3$。对于无平方因子 $c$，将剩余表示为 $\sum_{p|c} (c/p)x_p$，则在两个和中均有
$$\Gamma(c) = \prod_{p|c} \chi_p(c/p)^3 \Gamma(p), \qquad \gamma_3(c) = \prod_{p|c} \chi_p(c/p)^3 \gamma_3(p).$$
平方中的交叉项在加性特征下为整数。因此对于无平方因子 $c$ 有 $\Gamma(c) = \gamma_3(c)$。特别地，对于不同的好素数 $p, q$，
$$\frac{\Gamma(pq)}{\Gamma(p)\Gamma(q)} = \chi_p(q)^3 \chi_q(p)^3.$$
