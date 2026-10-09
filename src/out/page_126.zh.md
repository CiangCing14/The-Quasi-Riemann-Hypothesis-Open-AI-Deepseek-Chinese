因此，分离半范数对每个标量 $A > 0$ 都是一致的，不含 $Z$ 的导数阶幂次。归一化实幂在固定盒上具有有界的 Euler 导数，而继承的范数扭曲只有固定的多项式高度代价。在这样的剖面内部，不设置依赖于列的核比值的尖锐截断。对于 Poisson 步骤中的径向 Fourier 核，这些就是引理 4.7 和公式 (17.7) 中的归一化核界。

我们将使用的原始尾估计是，对于 $Y \ge 1$ 和 $A > 1$，

$$\sum_{h \neq 0:\, aq_h > Y} |K(aq_h)| \ll_A (1 + a^{-1}) Y^{1-A} \qquad (a > 0). \qquad (17.21)$$

事实上，壳层 $2^j Y < aq_h \le 2^{j+1} Y$ 包含 $O(1 + 2^j Y / a)$ 个格点，且核在该处为 $O_A((2^j Y)^{-A})$。对这两个几何级数求和即证得该式；同样的论证适用于固定格 $\lambda^{-4}O$。证明只用到 $x \ge 1$ 时的大自变量界 $|K(x)| \ll_A x^{-A}$，因此它也适用于此类尾上的反射核。在下文中，实际比值不等式仅用于说明扇区固定的外行球的补集包含在每个受支持的原始列对的该尾中。该补集在非互素延拓之前和 Fourier 绝对化之前被移除。完整光滑核保留在球内，其非光滑掩码在相关加权 Cauchy 不等式之前一直置于 Fourier 反演之外。尾阶和粗略的原始计数在最后固定。

第一次 Poisson 变换。展开公式 (A) 中的平方。令

$$B = \operatorname{rad}(b_1 b_2), \qquad n_i = A_i C u_i \quad (i = 1, 2),$$

其中 $A_i = (n_i, B)$，而 $C$ 是 $n_1/A_1$ 与 $n_2/A_2$ 的最大公约数。于是 $A_i \mid B$，而 $u_1, u_2$ 无平方因子、彼此互素且与 $CB$ 互素。设 $\underline{A}_i$、$\underline{B}$ 分别为 $A_i$、$C$ 的固定中心，并记 $\widehat{\underline{A}_i} = \log_Z q_{A_i}$、$\widehat{\underline{B}} = \log_Z q_C$。对于 $p \mid B$，定义

$$a_{ip} = 1_{p \mid A_i}, \qquad \pi_p = v_p(b_1 b_2) \bmod 2, \qquad t_p = a_{1p} - a_{2p} + 3\pi_p \bmod 6,$$

并令 $R_1 = \prod_{t_p \neq 0} p$。其中心为 $\underline{R}$，且 $\widehat{\underline{R}} = \log_Z q_{R_1}$。行特征及其剩余的零掩码恰好为

$$\psi_1 = \chi_{u_1} \bar{\chi}_{u_2} \prod_{t_p \neq 0} \chi_p, \qquad m_1 = u_1 u_2 R_1, \qquad R_{\mathrm{mask}} = CB/R_1. \qquad (17.22)$$

事实上，在 $u_1$、$u_2$ 处的指数为 $1, -1$；公共的非 $B$ 因子 $C$ 的指数为零但保留其掩码；而在 $p \mid B$ 处的指数为 $t_p$。每个非零局部幂都是非主特征且在模 $p$ 下本原，且支集互不相交。因此除非 $m_1 = 1$，$\psi_1$ 是本原的。每个原始列掩码以及两个因子 $\beta(b_1, f)\beta(b_2, f)$ 都保留在表达式中。

对 $K = Z^M$ 应用引理 17.5，并记其除子为 $d_k \mid CB/R_1$，中心为 $\underline{\delta}$，$\widehat{\underline{\delta}} = \log_Z q_{d_k}$。在这个真正的互素表达式上，实际导子长度为

$$\widehat{L}_1 = \widehat{n}_1 + \widehat{n}_2 - \widehat{A}_1 - \widehat{A}_2 - 2\widehat{B} + \widehat{R}. \qquad (17.23)$$

实际的核自变量为 $Z^M q_h / (q_{d_k} q_{m_1})$，而 Poisson 前因子的指数为 $M - \widehat{\underline{\delta}} - \widehat{L}_1 / 2$。我们尚未对该核进行截断或 Fourier 分离。

若 $m_1 = 1$，则 $u_1 = u_2 = 1$ 且对每个 $p \mid B$ 有 $t_p = 0$。后一条件迫使 $\pi_p = 0$ 且 $a_{1p} = a_{2p}$。因此 $n_1 = n_2$ 且 $b_1 b_2$ 为平方数。即使计入所有 $O(Z^{2\ell+\epsilon})$ 对 $b_1, b_2$、所有 $O(Z^{r+\epsilon})$ 个相等列、所有 $O(Z^{V+\epsilon})$ 个标签以及 $O(Z^M)$ 行，公式 (A) 中的归一化给出 $O(Z^{M+\epsilon})$。若 $r < 0$ 但其固定环形列窗口非空，则 $Z^{-r}$ 由其固定上端点所界，因此其理想计数仍为 $O(Z^r)$，常数固定。标记和保留的掩码不会将该界增大超过一个小幂次。当非零主
