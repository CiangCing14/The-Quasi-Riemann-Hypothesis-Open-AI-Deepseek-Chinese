变换后测试的界。对 $A \ge 0$ 与整数 $B \ge 0$，令

$$M_{A,B}(V) = \sup_{-A \le \eta \le 1/4} \int_{\mathbb{R}} (1+|u|)^B |\widehat{V}(\eta + iu)| \, du.$$

对每个整数 $j \ge 0$，

$$|(x\partial_x)^j V^\sharp(x)| \ll_{A,j} \min\{x^{1/4}, (1+x)^{-A}\} M_{A,\lceil 4A \rceil + j + 2}(V). \tag{5.4}$$

若固定 $\chi \in C_c^\infty(0,\infty)$，$Y > 0$，且 $J \ge 0$ 为整数，则

$$\int_{\mathbb{R}} (1+|u|)^J \int_0^\infty \chi(y) V^\sharp(Yy) y^{-iu} \frac{dy}{y} \, du \ll_{A,J,\chi} \min\{Y^{1/4}, (1+Y)^{-A}\} M_{A,\lceil 4A \rceil + J + 4}(V). \tag{5.5}$$

这些都是有限的光滑半范数。更确切地说，

$$M_{A,B}(V) \ll_{A,B} \int_0^\infty (1 + x^{-A} + x^{1/4}) \left( |V(x)| + |(x\partial_x)^{B+2} V(x)| \right) \frac{dx}{x}. \tag{5.6}$$

将 $V(x)$ 替换为 $x^{iu_0} V(x)$ 至多使 $M_{A,B}$ 乘以 $(1+|u_0|)^B$。

证明。我们首先通过有限多个平移后的 theta 值来表达特征掩码。然后变换它们的有理尖点，并计算所得的自守乘子与局部 Fourier 因子；最后的 Mellin 比较给出反射恒等式及其变换后测试的界。

固定的 theta 输入。令 $\Gamma = SL_2(\mathcal{O})$，$\Gamma_1(3) = \{g \in \Gamma : g \equiv I \pmod 3\}$，$\Gamma_2 = \langle SL_2(\mathbb{Z}), \Gamma_1(3) \rangle$。[8, 方程 (5.4), (5.7), (5.9), 以及 (5.12)–(5.17)] 的无条件公式给出 $H_3 = \mathbb{C} \times \mathbb{R}_{>0}$ 上的光滑三次 theta 函数 $\theta$，满足

$$\theta(gw) = \kappa(g)\theta(w) \quad (g \in \Gamma_2), \qquad \kappa\begin{pmatrix} a & b \\ c & \delta' \end{pmatrix} = \left( \frac{c}{a} \right)_3 \quad \begin{pmatrix} a & b \\ c & \delta' \end{pmatrix} \in \Gamma_1(3), \; c \neq 0.$$

这里 $\kappa$ 在 $SL_2(\mathbb{Z})$ 上取值为一，并且在 $\Gamma_1(3)$ 中下左元素为零的元素上也取值为一。下标 $3$ 表示通常的三次剩余符号；对好的素数 $p \notin S$，有 $(x/p)_3 = \chi_p(x)^2$。这些自守性与系数公式不依赖于关于 $L$-函数零点的任何假设。

令

$$L(t) = \begin{pmatrix} 1 & 0 \\ t & 1 \end{pmatrix}, \qquad (t_0, t_1, t_2) = (0, \omega^2, \omega), \qquad \widehat{\Theta}(w) = \theta(L(t_b)w).$$

若 $v \in \mathbb{Z} + 3\mathcal{O}$，则 $L(v)$ 是 $SL_2(\mathbb{Z})$ 中一个元素与 $\Gamma_1(3)$ 中一个下平移的乘积，其乘子为一。对上传也有类似的断言。因此

$$\theta(L(\lambda)w) = \Theta_1(w), \qquad \theta(L(-\lambda)w) = \Theta_2(w),$$

因为 $\lambda - \omega^2 = 2 + 3\omega$ 且 $-\lambda - \omega = -1 - 3\omega$。若 $u_0 = s + t\omega$ 且 $0 \le s, t < 3$，$E = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$，

则

$$\begin{pmatrix} u_0 & -1 \\ 1 & 0 \end{pmatrix} = E L(-u_0), \qquad -u_0 - \frac{t}{t} \in \mathbb{Z} + 3\mathcal{O},$$

从而 $\theta\left(\begin{pmatrix} u_0 & -1 \\ 1 & 0 \end{pmatrix} w\right) = \Theta_t(w)$。这些是下文所需的仅有的尖点代表元。

对其中任何一个，通过下式定义 $d_H$：

$$\bar{\theta}(H(z,v)) = C_H(v) + \sum_{\mu \neq 0} d_H(\mu) v K_{1/3}(4\pi|\mu|v) \check{e}(\mu z). \tag{5.7}$$

这里 $C_H(v)$ 与 $z$ 无关。三个函数 $\Theta_0, \Theta_1, \Theta_2$ 分别是 [8] 中的 $F_1, F_{19}, F_{10}$。其附录 A 第 1、19、10 行用其方程 (5.7)、(5.13) 和 (5.14) 中的 $\tau, \tau_1, \tau_2$ 表达了它们的系数。在其记号中，共轭展开使用 $d_j(-\mu)$，如其
