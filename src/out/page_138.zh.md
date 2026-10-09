其外的标量恰为 $Z^{\lambda_c+18\eta+\tau}$。完整的 qd2 分母与两个归一化实列根都在此剖面中，且最终检验不再追加此类根。

对于 $\zeta = (\zeta_g, \zeta_d, \zeta_v, \zeta_k, \zeta_1, \zeta_2)$，令 $z_n = q_n / Z N_{ch}$，并定义
$$W'_a(z) = \omega_{n,a}(Z^{\delta_N} z) z^{\varepsilon_a} i^{\zeta_a}, \qquad \nu'_a = \nu i^{\vartheta}, \qquad d'_a = d I_{a'}.$$
于是两个新 Cauchy 侧上的多项式恰为
$$Q_{a,\gamma,\zeta}(k_{new}, f_{new}) = \sum_{n \in sf} \bar{\alpha}(n) \gamma_2(n) \nu'_a(n) \rho'(n) \chi_n(k_{new}) \times \chi_n(f_{new})^4 d'_a(n) W'_a(q_n / Z N_{ch}). \tag{17.55}$$

在 $q_0$、$t'$、$g'/d^2$ 及有限射线扇区固定之后，$\nu'_a$ 与 $\rho'$ 独立于 $J$、$C$、$d_2$、$v'$ 及新行。关于 $n$ 的唯一新特征是显式展示的行因子与四次幂因子；所有涉及旧 $b_i$、$A_i$ 的其他相位都已置于方程 (17.25) 或旧行 $e_h$ 中。分离出的环形权重 $W'_a$ 也独立于新行与标签。完整的剩余外权重为
$$\begin{aligned}
V_\sigma(\xi; \zeta) = {} & w_{o+} \mu(d_2) \mu(v') G(\vartheta) |B_o(g')|^2 |D_o(v'; d_2, k'')|^2 \mathbf{1}_{(v', g' C_J) = 1} B_2(k'') \\
& \times A_{2,\sigma}(\xi) \psi_g(y_g) \psi_{d_2}(y_d) \psi_v(y_v) \psi_{k''}(y_k) \omega_f(q_{f_{new}} / Z V_c) \\
& \times y_g^{i \zeta_g} y_d^{i \zeta_d} y_v^{i \zeta_v} y_k^{i \zeta_k} Z^{i \delta_N (\zeta_1 + \zeta_2)}.
\end{aligned} \tag{17.56}$$
所有旧的纯算术与优先权掩码都保留在 $O_\sigma$ 中，并带有其非负旧系数权重 $w_{o+}$。所展示的两个公共量保持所有其他公共系数为零，包括依赖于 $k''$ 的那个。有一个 $\mu(d_2)$、一个 $\mu(v')$ 和一个射线系数。标签截断作为原始乘积支集上的等式插入，并保持在外层。

设 $T_{\sigma,i}$ 为通过上述完整 Möbius 与槽展开从方程 (17.41) 得到的固定 $v'$-二元组、射线与槽被加项。子项所需的精确恒等式为
$$T_{\sigma,i} = Z^{\lambda_c + 18\eta + \tau} (2\pi)^{-6} \int_{\mathbb{R}^6} \hat{H}_{2,\sigma,t}(\zeta) \times \sum_{\xi \in \Xi_\sigma} V_\sigma(\xi; \zeta) Q_{1,\gamma,\zeta}(k_{new}, f_{new}) Q_{2,\gamma,\zeta}(k_{new}, f_{new}) \, d\zeta. \tag{17.57}$$

为验证它，展开两个 $Q$。由于 $y_a = Z^{\delta_N} z_{n_a}$，它们的模态连同方程 (17.56) 的最后一个因子恰为 $y_1^{i \zeta_1} y_2^{i \zeta_2}$。另外四个模态是外层的。方程 (17.19) 恢复了完整剖面，其较大的截断在保留的支集上为一。新列截断在旧 $W_i$ 因子非零处为一，且 $\omega_f = 1$ 在每个原始标签乘积上成立。因此标量与剖面恢复了完整根、完整核与旧窗口。方程 (17.42)、(17.43) 与 (17.16) 逐项恢复了算术因子。固定盒求和是有限的，方程 (17.20) 为积分提供了依据。完整新窗口中的额外组合在此复 Fourier 恒等式中通过旧窗口在 Cauchy 之前相互抵消；只有在之后它们才被独立地保留在一个正和中。

方程 (17.57) 中的密度依赖于固定的扇区、$Z$、固定检验与 $t$，而不依赖于实际的 $\gamma$、$k_{new}$、$f_{new}$。耦合核使用裸 $k''$ 坐标，而非导出的行；后者仅出现在特征与 $B_2$ 中。导出的标签仅出现在特征及其外截断中。诸如 $g' = d_2 r_g$ 的关系限制求值点，而不限制变换。对每个固定的 $B_{ht}$、$J_{ht} \ge 0$，方程 (17.20) 中的 Euler 计算给出某个固定 $b$，使得
$$\int_{\mathbb{R}^9} \int_{\mathbb{R}^6} |\hat{H}_{1,\sigma}(t)| |\hat{H}_{2,\sigma,t}(\zeta)| (1 + |t|)^{B_{ht}} (1 + |\zeta|)^{J_{ht}} \, d\zeta \, dt \ll p_b(W)^2. \tag{17.58}$$
事实上，内层加权积分是 $t$ 的多项式，因为 $W_i$ 是一个固定截断乘以一个单位范数模态；在该多项式阶数加上 $B_{ht}$ 上应用第一个变换的界即可。常数对每个实际理想与每个正核标量都是一致的，且不含 $Z$ 的高度阶幂。

138
