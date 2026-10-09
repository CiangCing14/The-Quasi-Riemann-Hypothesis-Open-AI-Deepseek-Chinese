关于 $f$。对每个 $\delta > 0$，它一致地蕴含 $w(f) \ll_{C,\delta} q_f^{\delta}$。事实上，对于范数充分大的素理想 $\mathfrak{p}$，对每个整数 $e \geq 0$ 有 $(e+1)C \leq q_{\mathfrak{p}}^{\delta e}$，这是因为当 $e \geq 1$ 时 $e+1 \leq 2^e$。对于其余有限多个素理想，$\sup_{e\geq 0} (e+1)C q_{\mathfrak{p}}^{-\delta e} < \infty$；将这些界沿 $f$ 的素因子分解相乘即证得断言。

4.2 高斯和与有限互反相位
我们首先计算素高斯和。这也确定了后续所有公式中三次符号的定向。

引理 4.2（素高斯恒等式）。设 $\mathfrak{p}$ 是 $S$ 之外某个素理想的首一生成元，并令 $H = \chi_{\mathfrak{p}}$，$P = q_{\mathfrak{p}}$。则

$$\gamma_2(\mathfrak{p})^3 = -\alpha(\mathfrak{p}), \qquad \gamma_1(\mathfrak{p})\gamma_2(\mathfrak{p}) = H(4)\gamma_3(\mathfrak{p})\gamma_2(\mathfrak{p})^3.$$

对于 $j \not\equiv 0 \pmod 6$，有 $|\gamma_j(\mathfrak{p})| = 1$。

证明。令 $k = \mathcal{O}/(\mathfrak{p})$，并令 $\psi(x) = e(x/\mathfrak{p})$ 为其非平凡加法特征。对于 $k^\times$ 的乘法特征 $A$，将其零延拓后，令

$$\tau(A) = \sum_{x\in k} A(x)\psi(x), \qquad J(A,B) = \sum_{x\in k} A(x)B(1-x).$$

若 $A$ 非主特征，变量代换 $x = ty$ 给出

$$|\tau(A)|^2 = \sum_{t\in k^\times} A(t) \sum_{y\in k^\times} \psi((t-1)y) = P.$$

内层和对 $t = 1$ 为 $P - 1$，否则为 $-1$，且 $\sum_{t\in k^\times} A(t) = 0$。共轭还给出 $\tau(A)\overline{\tau(A)} = A(-1)P$。当 $AB$ 非主特征时，按 $x + y$ 对乘积 $\tau(A)\tau(B)$ 分组可得

$$\tau(A)\tau(B) = J(A,B)\tau(AB).$$

$x + y = 0$ 的组消失，因为 $AB$ 非主特征；对于非零和，除以 $x + y$ 即得所展示的 Jacobi 因子。特别地，若 $A, B, AB$ 均非主特征，则 $|J(A,B)| = \sqrt{P}$。

方程 $4x(1-x) = y$ 的解的个数为 $1 + H^3(1-y)$。将 $H(y)$ 乘以此恒等式并求和，利用 $\sum_y H(y) = 0$ 得 $J(H,H) = H(4)\overline{J(H,H)}$。记 $\tau_j = \tau(H^j)$。高斯–Jacobi 恒等式与 $\tau_2\tau_4 = P$ 现在给出

$$\frac{\tau_1\tau_3}{\tau_4} = H(4)\frac{\tau_2}{\tau_2^1}, \qquad \tau_1\tau_2 = H(4)\frac{\tau_3\tau_2^3}{P}.$$

这里 $H^2(-1) = 1$，因为 $-1$ 是立方。

尚需确定三次 Jacobi 和，包括其单位。令 $m = (P-1)/3$。$H^2$ 的定义在 $k$ 中给出

$$J(H^2,H^2) \equiv \sum_{x\in k} x^m(1-x)^m = 0 \pmod{\mathfrak{p}}.$$

事实上该多项式次数为 $2m < P - 1$，而每个次数小于 $P - 1$ 的单项式在 $k$ 上的和为零（常数情形即 $P = 0$ 于 $k$ 中）。Jacobi 和属于 $\mathcal{O}$ 且绝对值为 $\sqrt{P}$。

对于 $x \neq 0, 1$，选取 $j_x \in \{0,1,2\}$ 使得 $H^2(x(1-x)) = \omega^{j_x}$。这些 $x$ 上 $x$ 与 $1 - x$ 的乘积均为 $-1$，故 $\prod_{x\neq 0,1} x(1-x) = 1$。因此 $\sum_{x\neq 0,1} j_x \equiv 0 \pmod 3$。由于

$$\omega^j \equiv 1 + j(\omega - 1) \pmod{(\omega - 1)^2}, \qquad ((\omega - 1)^2) = (3),$$

13
