对于固定的一对保留下来的矩形，隐去它们的矩形指标。于是式 (18.34) 将成对除数计数与这些系数界定为
$$
t^- - \frac{r_{\mathrm{clip},1} + r_{\mathrm{clip},2}}{2} + \frac{e_1 + \pi_{0,1} + e_2 + \pi_{0,2}}{2} \le \frac{(e_1 + \omega_1) + \pi_1 + (e_2 + \omega_2) + \pi_2}{2} \le 2\theta_N. \tag{18.37}
$$

每侧至多有两个矩形，因此至多有四对这样的组合；它们的三角形因子是固定的。对有符号差没有使用公共的裁剪约化。

在 $c_2$ 一侧，在最后一次互素提取之前，名义总长度为 $A' = \alpha_1 = A - c - w - c_2$。对于正槽参数，
$$
\begin{aligned}
(A' - M') - (A - M) &= g + w - d - c_2 - (K_0 - K) - w_o + g_2 - t_2 \\
&\le 6(w + \ell) + \delta_{\mathrm{fr},1}. \tag{18.38}
\end{aligned}
$$

为证明该不等式，首先使用 $g_2 - t_2 \le c_2$。在放大后的主范数中，$w = w_o = 0$ 且
$$
g = J_+ + 2\sigma \le d + (K_0 - K) + 6\ell + \delta_{\mathrm{fr},1}.
$$
对于误差项，$g \le d + (K_0 - K) + \sigma + \delta_{\mathrm{fr},1}$，故超出量至多为 $w - w_o + \sigma + \delta_{\mathrm{fr},1}$。这些不等式用到 $d + K_0 - K \ge -\delta_{\mathrm{fr},1}$ 以及正部的 1-Lipschitz 性质。式 (18.28) 中的三种选择，连同 $\ell_p \ge \sigma/6$，给出 $w - w_o + \sigma \le 6w$。这就证明了式 (18.38)。

对每个保留下来的裁剪矩形，若无槽存活，就在所声明的宽度 $M'_{\mathrm{act}}$ 处应用完备的无限制零槽断言。若有槽存活，则先应用式 (18.4)–(18.6) 中的代数掩码删除。它把这个标准裁剪乘积表示为自然乘积，并且只会减小其非负仿射表达式。对每个实际乘积，在两次频率包围、$t$-分配以及掩码删除之后，设 $A_{\mathrm{act}}, z_{\mathrm{act}}$ 为其所声明的总长度与槽长度，并令
$$
F_{\mathrm{act}} = \left(A_{\mathrm{act}} - M'_{\mathrm{act}} + (6\kappa - 1)z_{\mathrm{act}}\right)_+.
$$
其父项满足式 (18.3)。在此掩码删除之前，设 $z' \le z$ 为该裁剪矩形存活槽的长度。式 (18.38) 与 (18.36)，连同 $M'_{\mathrm{act}} \ge M'$，给出
$$
\begin{aligned}
A_{\mathrm{clip},j,\varrho} - M'_{\mathrm{act}} + (6\kappa - 1)z' &\le \alpha_j - M' + (6\kappa - 1)z + e_j + \pi_{j,\varrho} - r_{e_j} - (M'_{\mathrm{act}} - M') \\
&\le 6(w + \ell) + \delta_{\mathrm{fr},1} + e_j + \pi_{j,\varrho}.
\end{aligned}
$$
在另一侧交换 $c_2, d_2$ 后同样的计算成立。因此取正部再删除固定掩码，得到
$$
F_{\mathrm{act}} \le 6(w + \ell) + \delta_{\mathrm{fr},1} + (e_j + \pi_{j,\varrho})_+ \le 6(w + \ell) + \delta_{\mathrm{fr},1} + 2\theta_N.
$$
这里 $z_{\mathrm{act}} \le z' \le z$。所有列出的账目都使用固定的聚合长度列表
$$
A, z, c, d, p, R, E, s_0, K, w, w_o, g, \ell, c_2, d_2, p_2, g_2, t_2, V.
$$
它们的仿射系数与正部 Lipschitz 常数都是数值常数，与 $N$ 无关。因此，一旦施加了聚合阈值，所显示的频率界、原始归一化界与矩形裁剪界都包含在 $C_* \xi$ 中，其中 $C_* \ge 1$ 是固定的且与 $N$ 无关。这一固定误差界的存在性，在比较长度之前只用到单个 $\theta_N = H_N / \log Z$，而不是 $N$ 个彼此独立的 $\xi$ 副本。我们在下文放大 $C_*$，以覆盖一个阶段中固定数目的运算。

若 $F_{\mathrm{act}} > 0$，则从该乘积中移除整槽，直到剩余乘积满足式 (18.3) 或不再有槽剩余。这里的移除是指对整个选定的素多项式应用逐点界式 (18.12)；没有任何素标号被冻结。被移除的槽
