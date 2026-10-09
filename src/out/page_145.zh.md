因此，实际的旁指标满足

$$
\kappa_i^{\mathrm{init}} \le \kappa_c^{\mathrm{init}} + 3\eta, \qquad \kappa_c^{\mathrm{init}} = m - 2D' + P_1. \tag{17.70}
$$

所有归一化的实逆根都将保留在下面单个联合剖面中，而不再出现在最终的子检验里。主列具有直接的对角界 $O(Z^{m+\epsilon})$，对于有界的非空负 $D'$-窗口也是如此。任何恢复到形式公式中的主非零频率都带有相同的 $B_{\mathrm{init}}$ 掩码，并且由引理 17.5 中的完整主恢复所界定，因为 $Z^m \ge 1$。

插入来自对所有 $d'$ 共同的一个划分的 $q_{h'}$ 的频率二元组，而不是一个标签重定心的划分。外掩码蕴含 $q_{h'} \le Z M_{\mathrm{init}}$，因此在有界保留范围内只有对数多个二元组。设 $H$ 为这样一个裸频率二元组的中心，并设 $\psi_C, \psi_{d'}, \psi_{h'}$ 为当前 $C, d', h'$ 二元组上保留的各个截断函数，在其归一化范数处取值。

方程 (17.68) 中的定向现已固定。第二个典范 Poisson 变换中的计算将 $\mu(z)\gamma^{-1}(z)$ 替换为 $\bar{\alpha}(z)\gamma^2(z)\chi_z(-1)G(z)$。在第二侧，共轭内的因子具有射线因子 $G(z)$；连同 CRT 交叉相位，相对射线因子为 $G([z_2][z_1]^{-1})$。用上面固定的群公式将其展开，并在一个固定的射线被加项中令

$$
\nu_* = \nu_0\vartheta, \quad A_*(z) = \bar{\alpha}(z)\gamma^2(z)\nu_*(z), \quad K_{\mathrm{init}} = F\Phi_{\mathrm{init}}.
$$

对于一个固定重叠、这些二元组和射线被加项的预备模式 $\Sigma_0$，并在先前模式保持固定的情况下，带掩码的主恢复非零分量恰好为

$$
\begin{aligned}
T_{\Sigma_0}^{\mathrm{init}} = & \sum_{\substack{C\ \mathrm{sf},\ d'\mid C \\ h'\ne 0}} \psi_C\psi_{d'}\psi_{h'}\,\mu(d')G(\vartheta)\widehat{B}_{\mathrm{init}}(h')\,\mathbf{1}_{(C,j)=1} \\
& \times \sum_{\substack{z_1,z_2\ \mathrm{sf} \\ (z_1 z_2, Cj)=1}} \mathbf{1}_{(z_1,z_2)=1} A_*(z_1)A_*(z_2)\chi_{z_1}(d')\chi_{z_1}(h')\chi_{z_2}(d')\chi_{z_2}(h') \\
& \times d_0(Cz_1)d_0(Cz_2)W_0(q_C q_{z_1}/Z^{D})W_0(q_C q_{z_2}/Z^{D'}) \\
& \times \frac{Z^{-D}Z^m}{\sqrt{q_{d'}q_{z_1}q_{z_2}}} K_{\mathrm{init}}\!\left(\frac{Z^m q_{h'}}{q_{d'}q_{z_1}q_{z_2}}\right).
\end{aligned} \tag{17.71}
$$

事实上，对于 $S$ 外的无平方因子 $C$ 有 $|\mu(C)\nu_0(C)|^2 = 1$，公共行因子恰好为 $\mathbf{1}_{(u,C)=1}$，其 Poisson 展开贡献出单个 $\mu(d')$。显示的两个分子因子分别是本原特征 $\chi_{z_1}\chi_{z_2}$ 及其 Fourier 变换的因子。有限射线和通过 $G(1)=1$ 恢复主对。该恢复的代价以及在此等式之前移除的原始补集已在上文分别界定。

通过显示的各个 $A_*$ 因子、特征、形式乘积范数、完整核以及不变的外球，在一切与 $Cj$ 互素的各自无平方因子 $z_1, z_2$ 上定义方程 (17.71) 中的被加项。它在互素区域上一致。在任何逐因子界之前插入完整恒等式

$$
\mathbf{1}_{(z_1,z_2)=1} = \sum_{s\mid(z_1,z_2)} \mu(s), \qquad z_a = s n_a,
$$

设 $v \ge 0$ 为一个无平方因子 $s$-二元组的中心，$\hat{v} = \log_Z q_s$，并设 $\psi_s$ 为其保留的各个截断函数。各 $n_a$ 无平方因子且与 $s$ 互素，但不必两两互素。这一形式延拓不将 Poisson 求和应用于非互素的导子。对于无平方因子且互素的 $s, n$，CRT 与保零恒等式 $\chi_n(d') = \chi_n(d')\chi_n(d')^4$ 恰好给出

$$
\begin{aligned}
A_*(sn)\chi_{sn}(d')\chi_{sn}(h') = & A_*(s)\chi_s(d')\chi_s(h') \\
& \times A_*(n)\chi_n(d'h')\chi_n(d's)^4.
\end{aligned} \tag{17.72}
$$
