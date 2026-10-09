选取一个非负的 $W \in C_c^\infty((0, \infty))$，满足在 $[1, 2]$ 上 $W \geq 1$。对于算术预备中的 Fourier 变换与自对偶测度，令 $w(z) = W(|z|^2)$，并定义 $\widehat{W}$ 为

$$\widehat{w}(y) = W(|y|^2).$$

该变换是径向的，在零点光滑，且速降。因此

$$W(x) \ll_A (1 + x)^{-A}, \quad \int_{\mathbb{R}} |\mathcal{M}W(\sigma + it)| \, dt < \infty \quad (\sigma > 0). \tag{9.5}$$

这里 $\mathcal{M}$ 表示 Mellin 变换。第二个断言由 Mellin 积分中的分部积分得到；所有对数导数在零点有界，在无穷远处速降。对 Fourier 变换作伸缩，对应于 $z \mapsto W(|z|^2/M)$ 得到 $\mathcal{M}W(M|y|^2)$。

对于 $bc \neq 1$，本原原始特征的有限 Fourier 反演为

$$\sum_{v \bmod bc} \Theta_{b,c}^{(j)}(v) e(vy/(bc)) = \Theta_{b,c}^{(j)}(y) \sqrt{q_{bc}} \, \Gamma_{b,c}^{(j)}.$$

对于非单位元 $y$，左端为零，因为一个非平凡局部特征与平凡加性特征求和相消。对于所述的 $e$ 与 $d\mu$，基 $(1, \omega)$ 上的迹配对矩阵为 $\begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$，行列式为 $-1$，而 $O$ 的 $d\mu$-余体积为 $1$。因此 $bcO$ 的对偶为 $(bc)^{-1}O$，而 $bcO$ 的余体积为 $q_{bc}$。陪集 Poisson 求和，随后除以每个理想的六个生成元，因此给出

$$\sum_{a \neq 0} W(q_a/M) \Psi_{b,c}^{(j)}(a) = \frac{\mathcal{M}\Gamma_{b,c}^{(j)}}{\sqrt{q_{bc}}} \sum_{a \neq 0} W(M q_a/q_{bc}) \Psi_{b,c}^{(j)}(a). \tag{9.6}$$

这里两个求和均遍历所有非零整理想。除以六用到了 $\Theta_{b,c}^{(j)}$ 的单位平凡性与权重的径向性。零频率项消失，因为该特征非平凡。

平方范数的 Poisson 变换。对于支撑在 $AN$ 中一个 $t$-类上的 $\lambda$，令

$$Q_j(M, N; \lambda) = \sum_{\substack{b, c \in A_N \\ (b,c) = 1}} \lambda_b \lambda_c \sum_{a \neq 0} W(q_a/M) \Psi_{b,c}^{(j)}(a).$$

我们断言，对每个 $\varepsilon > 0$，

$$|Q_j(M, N; \lambda)| \ll_{S,\varepsilon} (2 + MN)^\varepsilon \|\lambda\|_2^2 \left( M + \frac{M}{N} \max_{\substack{1 \leq H \\ H \ll_{S,\varepsilon} (2+MN)^\varepsilon N^2/M}} E_j(H, N) \right). \tag{9.7}$$

最大值遍历二进壳层，若为空则为零。若 $N \leq 1$，则只可能出现单位好理想，环状理想计数证明了 $M$ 项。此外当 $M$ 低于某个固定正常数时 $Q_j = 0$，因为 $W$ 有固定的上支撑端点，且非零理想的范数至少为一。

假设 $N > 1$ 并规范化 $\|\lambda\|_2 = 1$。则 $Q_j$ 中的每一对均非平凡，且 $q_{bc} \asymp N^2$。应用式 (9.6) 并对对偶理想取三角不等式。对于小的 $\delta > 0$，令 $Z = (2 + MN)^\delta$。Cauchy 给出 $(\sum_b |\lambda_b|)^2 \ll N^2$。由式 (9.5)，$q_a > ZN^2/M$ 的部分，对任意 $A > 1$，至多为

$$M \sum_{q_a > ZN^2/M} (M q_a/N^2)^{-A} \ll N^2 Z^{1-A}.$$
