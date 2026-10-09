第14.2节中的带标记反射将用到对活跃素数对的如下依赖关系。由于

$$\epsilon_p = -\lambda^{-5} (c/p)^{-2} \pmod{p},$$

存在一个绝对值为1的标量 $\xi_{p,j}$，它依赖于 $p, j$ 但不依赖于其他任何活跃素数，使得

$$\chi_p(\sigma_p)^{-2} \omega_{p,j} = \xi_{p,j} \chi_p(c/p)^{2j+2}. \tag{5.17}$$

对于 $j = 4$，这用到了 $2j + 2 \equiv -2 \pmod{6}$；对于其他指数，代入 $\epsilon_p$ 的表达式即可立即得到。因此，另一个活跃素数对 $p$ 处相位的贡献的指数恰为模六的 $2j + 2$。特别地，活跃指数 $j = 1$ 具有列耦合 $\chi_p(x)^{-3} = \chi_p(x)^3$。

Mellin 规范化与延拓。令

$$J(s) = \int_0^\infty \partial_{\bar{z}} F(z, v)\big|_{z=0} v^{2s-1} \, dv.$$

[8, Lemma 5.3] 中使用的 Bessel 恒等式为

$$\int_0^\infty K_{1/3}(y) y^{w-1} \, dy = 2^{w-2} \Gamma((w - 1/3)/2)\Gamma((w + 1/3)/2) \qquad (\Re w > 1/3).$$

在 $\Re s > 1$ 上系数和绝对收敛，因此我们可以逐项对其展开式求导和积分。由于 $\partial_{\bar{z}} \check{e}(\mu z) = 2\pi i \bar{\mu}\check{e}(\mu z)$，取 $w = 2s + 1$ 的恒等式给出

$$J(s) = \frac{i}{4} (2\pi)^{-2s} \Gamma(s + 1/3)\Gamma(s + 2/3) \sum_{0 \neq \mu \in \lambda^{-3}\mathcal{O}} d_I(\mu)\phi(\lambda^3 \mu) \prod_p \chi_p(\lambda^3 \mu)^{j_p} \bar{\alpha}(\mu)q_\mu^{-s}.$$

首先如上面那样用整指数掩码限制到 $(nb, E) = 1$，然后代入方程 (5.9) 和 (5.10)。利用 $q_{\lambda^{-3}} = 27^{-1}$ 和 $\bar{\alpha}(\lambda^{-3}) = -i$ 得到

$$J(s) = \frac{3^{5/2}}{4} \left(\frac{27}{(2\pi)^2}\right)^s \Gamma(s + 1/3)\Gamma(s + 2/3)T(s, \Psi). \tag{5.18}$$

对于一个平移项 $z_h = a/c$，使用上面构造的矩阵 $g = GH$。由 [8, Equation (5.1)]，$g^{-1}$ 在双曲空间上的坐标作用给出

$$g^{-1}(z + a/c, v) = \left( -\frac{\delta'}{c} - \frac{\bar{z}}{c^2(v^2 + |z|^2)}, \frac{v}{q_c(v^2 + |z|^2)} \right).$$

在 $z = 0$ 处，其第一个坐标关于 $\bar{z}$ 的导数为 $-(cv)^{-2}$；其共轭坐标和竖直坐标关于 $\bar{z}$ 的导数均为零。链式法则和 $\bar{\theta}(gw) = \bar{\kappa}(G)\bar{\theta}(Hw)$ 因此给出

$$\partial_{\bar{z}}\bar{\theta}(z + a/c, v)\big|_{z=0} = -\frac{\bar{\kappa}(G)}{c^2 v^2} \partial_z \bar{\theta}(H(z, 1/(q_c v)))\big|_{z=-\delta'/c}.$$

特别地，该导数从方程 (5.7) 中的每个尖点展开式中去掉了 $C_H(v)$。代入该展开式，然后在积分中作替换 $v \mapsto 1/(q_c v)$，对于 $\Re s < 0$ 得到贡献

$$-\frac{i}{4} (2\pi)^{2s-2} \bar{\alpha}(c)^2 q_c^{1-2s} \bar{\kappa}(G) \prod_{\pm} \Gamma(3/2 - s \pm 1/6) \times \sum_{\mu \neq 0} d_H(\mu)\alpha(\mu)\check{e}(-\delta' \mu/c)q_\mu^{-(1-s)}. \tag{5.19}$$

为直接验证该标量，在应用 Bessel 积分之前因子为 $-2\pi i c^{-2} q_c^{2-2s}$，剩余的积分为 $\int_0^\infty u^{2-2s} K_{1/3}(4\pi|\mu|u) \, du$。取 $w = 3-2s$ 的 Bessel 恒等式，连同 $c^{-2} = \bar{\alpha}(c)^2/q_c$，恰好给出该式。
