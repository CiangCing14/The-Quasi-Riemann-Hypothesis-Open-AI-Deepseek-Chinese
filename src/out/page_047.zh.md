6.2    平衡低估计

对于平衡估计，已完成行的矩已经给出了 $B_{m,\sigma}(Z)$ 的均方界。剩下需要估计加性因子 $A_{m,\sigma,v}(Y)$。其 Gauss 展开给出 $\mathbb{C}/\mathcal{O}$ 中互不相同的既约分数；它们的分离性与系数质量给出了所需的均方界。平面加性大筛法是经典的；可比较 Huxley 的多变量与数域不等式 [19] 以及 [1, Section 3, Theorem 3] 中的 Poisson 证明。我们在此给出格点证明，以记录这里所用的归一化。

引理 6.1（平面加性大筛法）。设 $0 < \delta \le 1$，$Q \ge 1$，并设 $z_1, \ldots, z_J$ 是 $\mathbb{C}/\mathcal{O}$ 中满足

$$\inf_{n \in \mathcal{O}} |z_j - z_k - n| \ge \delta \qquad (j \ne k)$$

的有限点集。则对任意复数 $a_1, \ldots, a_J$，

$$\sum_{\substack{m \in \mathcal{O} \\ q_m \le Q}} \left| \sum_{j=1}^{J} a_j e(m z_j) \right|^2 \ll (Q + \delta^{-2}) \sum_{j=1}^{J} |a_j|^2.$$

其中隐含常数对于上述固定的格、加性特征与自对偶测度是绝对的。将行球中的 $Q$ 替换为它的固定倍数，只会改变该常数。

证明。当 $J = 0$ 时断言显然成立。由自对偶性，特征 $e(m z_j)$ 在 $\mathbb{C}/\mathcal{O}$ 上有良好定义。对于其余情形，在 $\mathbb{C}$ 中选取代表元。我们使用 Fourier 变换

$$\hat{F}(y) = \int_{\mathbb{C}} F(x) e(-xy) \, d\mu(x), \qquad \check{\phi}(x) = \int_{\mathbb{C}} \phi(y) e(xy) \, d\mu(y).$$

选取非负的 $\phi \in C_c^\infty(\mathbb{C})$，积分为一，支集在围绕原点的充分小的圆盘内。由于 $|e(xy) - 1| \le (4\pi/\sqrt{3})|x||y|$，其支集可取得使

$$|\check{\phi}(x) - 1| \le \frac{1}{2} \qquad (|x| \le 1).$$

于是 $F(x) = 4|\check{\phi}(x)|^2$ 是非负 Schwartz 函数，且 $F(x) \ge 1$ 在单位圆盘上成立。若 $\tilde{\phi}(y) = \phi(-y)$，则 Fourier 反演与乘积公式（卷积关于 $d\mu$ 取）给出

$$\hat{F} = 4\phi * \tilde{\phi}.$$

特别地，$\hat{F}$ 有界且支集在某个固定半径 $L$ 的圆盘内。这就是我们所需的带限优函数。

令 $R = \sqrt{Q}$。由 $F$ 的非负性首先得到

$$\left| \sum_{q_m \le Q} \sum_{j} a_j e(m z_j) \right|^2 \le \left( \sum_{m \in \mathcal{O}} F(m/R) \right) \left| \sum_{j} a_j e(m z_j) \right|^2.$$

右端所有和式绝对收敛。对任意 $z \in \mathbb{C}$，映射 $x \mapsto F(x/R) e(xz)$ 在 $y$ 处的 Fourier 变换为 $R^2 \hat{F}(R(y - z))$。因子 $R^2$ 是实二维伸缩的 Jacobian；不出现格体积因子，因为 $d\mu$ 在 $\mathcal{O}$ 上的余体积为一。因此 Poisson 求和将右端展开为

$$R^2 \sum_{j,k} a_j \overline{a_k} \sum_{n \in \mathcal{O}} \hat{F}\big(R(n - z_j + z_k)\big).$$
