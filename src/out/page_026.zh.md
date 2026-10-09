1. 一个项由 $h_0 \bmod L$ 和活跃素数的子集确定。每个满足 $j_p \neq 0$ 的 $Q_p$ 都是活跃的，而 $j_p = 0$ 的素数既可以是活跃的也可以是非活跃的。记 $r = \prod_{p \text{ active}} p$。则 $c = c_F r$，其中 $c_F$ 是 $\lambda_2 h_0 / L$ 的既约分母，带有一个正规化单位。于是 $c_F$ 取遍一个固定的有限集，且其素因子整除 $L$。共有 $O_L(2^{|P|})$ 个项，或在将下一个展示式中的每个 Ramanujan 因子拆分为其两个被加项后为 $O_L(4^{|P|})$ 个项。

2. 局部列因子为
$$
B_p(x) = \begin{cases}
\chi_p(x)^{-j_p-2}, & j_p \neq 0, 4, \\
q_p^{-1/2}(-1 + q_p \mathbf{1}_{p \mid x}), & j_p = 4, \\
q_p^{-1/2} \chi_p(x)^{-2}, & j_p = 0 \text{ 且 } p \text{ 活跃}.
\end{cases}
$$
函数 $d$ 是三个固定尖点系数函数之一。以 $u$ 记一个 Eisenstein 单位，其支集与大小满足
$$
\operatorname{supp} d \subset \{u\lambda_k n b^3 : k \geq -4,\ n, b \equiv 1 \pmod 3,\ n \text{ 无平方因子}\},\quad |d(\mu)| \leq 27\, 3^{k/6} |b|. \tag{5.2}
$$
该界指的是支集中指标所示的表示。它允许 $n$ 和 $b$ 有公共素因子，并且除在 $\lambda$ 处所显示的限制外，对 $L$ 的素数不施加任何排除。特征 $\vartheta$ 是 $O$ 的某个商的一个加法特征，其模数固定且仅依赖于 $L$。

3. 标量 $\zeta$ 与 $\mu$ 无关，且满足 $|\zeta| \leq 1/81$。它关于变动素数的依赖可以精确给出。对于 $m \not\equiv 0 \pmod 6$，令
$$
\tau_{p,m}^{\pm} = q_p^{-1/2} \sum_{y \bmod p} \chi_p(y)^m e(\pm y/p), \quad |\tau_{p,m}^{\pm}| = 1.
$$
对每个活跃的 $p$，用模 $p$ 的单位定义
$$
\sigma_p = \lambda_2 c/p, \quad \epsilon_p = -\left((\lambda_3 c/p)\sigma_p\right)^{-1},
$$
并令
$$
\omega_{p,j} = \begin{cases}
\tau_{p,j}^{-} \tau_{p,j+2}^{+} \chi_p(\epsilon_p)^{-j-2}, & j \neq 0, 4, \\
\tau_{p,4}^{-}, & j = 4, \\
-\tau_{p,2}^{+} \chi_p(\epsilon_p)^{-2}, & j = 0.
\end{cases}
$$
$\tau$ 的指标按模六读取。令 $M = \lambda_{12} L^4$，则存在一个绝对值为一的数 $\kappa_F$，仅依赖于 $h_0$ 与 $r$ 模 $M^2$ 的类，使得
$$
\zeta = -\frac{i}{81} \bar{\alpha}(c)^2 \phi(\hat{h}_0) \bar{\kappa}_F \prod_{p \text{ inactive}} (1 - q_p^{-1}) \prod_{p \text{ active}} \chi_p(\sigma_p)^{-2} \omega_{p,j_p}. \tag{5.3}
$$
在 $h_0$ 与 $r$ 模 $M^2$ 的有限多个类中的每一个里，$d$ 和 $\vartheta$ 都固定。因此这些是该扇区内的公共列因子。除所显示的尺度 $q_c^2$ 之外，$B_p$ 之外的所有其他变动素数依赖都包含在标量 $\zeta$ 中，而 $\zeta$ 可以依赖于整个活跃集。
这些分支约定对所有具有相同 $L$ 和 $\Psi_0$ 的局部素数集是同时的。特别地，若将一个好素数 $p$ 以指数零加入局部集并宣布其为非活跃，则所得分支具有相同的 $c_F, c, d, \vartheta, \kappa_F$，在每个其他活跃素数处有相同的数据，并且与 $p$ 不出现时的分支有相同的核。其标量乘以 $1 - q_p^{-1}$。这种相容性包含每个 $h_0$，而不仅是模 $L$ 的单位类。
