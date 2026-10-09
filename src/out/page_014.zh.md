我们得到 $J(H_2, H_2) \equiv P^{-2} \equiv -1 \pmod 3$。由 $p$ 的整除性以及范数相等可知，存在单位 $u$ 使得 $J(H_2, H_2) = up$。由于 $p$ 是主元且六个单位模 $3$ 的剩余类互不相同，该同余式迫使 $u = -1$。最后，
$$\tau_2^3 = J(H_2, H_2)\tau_2\tau_4 = -pP^2.$$
将两个 Gauss 恒等式除以 $P$ 的相应幂次即证得引理。

剩余相因子是二次的。下面对它的求值即使对非平方自由或非主元的奇元素也成立。

引理 4.3（二次四项公式）。对非零奇元素 $c \in \mathcal{O}$，定义
$$\Gamma(c) = |c|^{-1} \sum_{x \bmod c} e(x^2/c).$$
则
$$\Gamma(c) = \frac{1}{2} \sum_{y \bmod 2\mathcal{O}} e(-cy^2/4). \tag{4.3}$$
对 $c = a + b\omega$，右端为 $(1 + i^{-b} + i^a + i^{b-a})/2$。特别地，$\Gamma$ 仅依赖于 $c \bmod 4\mathcal{O}$，且对每个奇元素 $v$ 有 $\Gamma(cv^2) = \Gamma(c)$。模 $4$ 的单位群的平方子群为 $\{1, \omega, \omega^2\}$，平方类代表元为 $1, -1, \lambda, -\lambda$。函数 $\Gamma$ 在这些单位上永不为零，且 $r(a, b) = \Gamma(ab)/(\Gamma(a)\Gamma(b))$ 满足

$$\begin{array}{c|cccc}
c & 1 & -1 & \lambda & -\lambda \\
\hline
\Gamma(c) & 1 & 1 & i & -i
\end{array} \tag{4.4}$$

$$r((-1)^e \lambda^f, (-1)^g \lambda^h) = (-1)^{eh + fg + fh}, \quad e, f, g, h \in \{0, 1\}.$$

因此 $|\Gamma(c)| = 1$，且 $r$ 是平方类群上的对称 $\{\pm 1\}$-值双特征。

证明。使用核为 $e(-zy)$、测度为 $d\mu$ 的 Fourier 变换。对 $\varepsilon > 0$，在 $\mathcal{O}$ 上对 $f_\varepsilon(z) = e(z^2/c)e^{-\pi\varepsilon|z|^2}$ 应用 Poisson 求和。直接的 Gaussian 积分给出，其中 $r_\varepsilon = 1 + 3q_c\varepsilon^2/16$，
$$\hat{f}_\varepsilon(y) = \frac{|c|}{2\sqrt{r_\varepsilon}} e^{-\pi\varepsilon q_c|y|^2/(4r_\varepsilon)} e\left(-cy^2/(4r_\varepsilon)\right).$$
为验证归一化，将 $z$ 旋转 $c$ 的辐角的一半。所得实二元 Gaussian 的二次矩阵为
$$\begin{pmatrix} \varepsilon & -4i/(\sqrt{3}|c|) \\ -4i/(\sqrt{3}|c|) & \varepsilon \end{pmatrix}, \quad \det = \frac{16r_\varepsilon}{3q_c}.$$
其特征值为共轭复数且实部为正。行列式的正平方根、$d\mu$ 中的因子 $2/\sqrt{3}$ 以及配方法给出了上述公式。

令 $I_\varepsilon = \int_{\mathbb{C}} e^{-\pi\varepsilon|z|^2} d\mu(z) = 2/(\sqrt{3}\varepsilon)$。对固定的理想 $(b)$、固定的类 $v \bmod b$ 及 $a > 0$，在 $b\mathcal{O}$ 上的 Gaussian Poisson 求和给出
$$\frac{1}{I_\varepsilon} \sum_{z \in v + b\mathcal{O}} e^{-\pi a\varepsilon|z|^2} \longrightarrow \frac{1}{a q_b} \quad (\varepsilon \downarrow 0).$$
零对偶向量给出极限，每个非零对偶向量都指数小。相因子 $e(z^2/c)$ 模 $c$ 周期。因此 Poisson 恒等式左端的归一化极限趋于 $\Gamma(c)/|c|$。

在右端可以用 $1$ 代替 $r_\varepsilon$。对固定 $c$，来自相因子的总误差至多为
$$C c \varepsilon^2 \sum_{y \in \mathcal{O}} |y|^2 e^{-C_c \varepsilon|y|^2} = O_c(1),$$
