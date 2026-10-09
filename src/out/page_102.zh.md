证明。令 $A = cn^3$，并对 $i \in J$ 令 $\varrho_i = qp_i / P_i$。由于 $qA = qc\, qn^3$，即使 $c$ 与 $n$ 有公共素因子也成立，且 $qp_J c = Z \prod_{i \in J} \varrho_i$，对定义 $B$ 的所示积分作 Mellin 反演，得到物理光滑因子
$$
V\!\left(\frac{qA}{Z qp_J c}\right) = W_G\!\left(Q \prod_{i \in J} \varrho_i\right), \qquad r = 1 + \frac{\ell'}{Z}.
$$
这里 $V = W_G$ 是引理 4.6 中的 Gauss 函数。空乘积取为 1。

对该引理中的 $r$ 使用固定平移分解 $\chi$。在环带 $r = e^k x$ 上，保留单个联合剖面
$$
w_{k,J}(x, \varrho) = \chi(\log x)\, W_G\!\left(Q \frac{e^k x}{\prod_{i \in J} \varrho_i}\right) \prod_{i \in J} W_i(\varrho_i).
$$
在此支集上，$x$ 及所有 $\varrho_i$ 的对数都落在固定的紧集中。因此 Gauss 函数自变量的对数为 $k + O_{\mathrm{fixed}}(1)$。引理 4.6 中的导数估计，配合此有界平移与固定槽窗，给出：对任意固定的 $\kappa_G > 0$，$A_{\mathrm{cnt}}, B_{\mathrm{cnt}}, C_{\mathrm{ann}} \ge 0$，$D_{\mathrm{tail}} > 0$，以及固定的半范数阶 $j$，
$$
\sum_{k \in \mathbb{Z}} e^{A_{\mathrm{cnt}} |k|} p_j(w_{k,J}) < \infty,
$$
$$
Z^{B_{\mathrm{cnt}}}\!\! \sum_{|k| > \kappa_G \log Z - C_{\mathrm{ann}}}\!\! e^{A_{\mathrm{cnt}} |k|} p_j(w_{k,J}) \ll Z^{-D_{\mathrm{tail}}}.
$$
这些常数可以依赖于固定的槽系统，但不依赖于其移动的素标签。在环带 $\log r = k + O(1)$ 上，由初等的行、槽与理想计数，行 $\ell^2$ 范数的一个绝对上界至多为 $Z^{B_{\mathrm{cnt}}} e^{A_{\mathrm{cnt}} |k|} p_j(w_{k,J})$，其中指数固定。取 $C_{\mathrm{ann}}$ 大于 $\chi$ 的固定对数半径，并只丢弃满足 $|k| > \kappa_G \log Z + C_{\mathrm{ann}}$ 的整个环带。对其范数界求和再平方，得到小于 $Z^{-1}$ 的任意给定幂。每个满足 $|\log_Z r| \le \kappa_G$ 的环带都被保留。

对每个剩余环带，保留固定的单个环带截断函数，使其在 $w_{k,J}$ 的支集上等于 1，并对整个剖面应用引理 4.5。其对数 Fourier 反演使用一个对每一行及每个存活槽组都相同的系数密度。归一化的槽比在分离之前始终是联合剖面的变量；它们并不为分别选取的密度提供指标。对固定的 Fourier 变量，所得的每个槽系数是原算术系数 $\eta(p_i)$ 与单个环带截断及范数幂的乘积。它保持有界，且与行及所有其他槽无关。补全后的因子是长度为
$$
N_* = 1 + \ell' + \theta_N, \qquad \theta_N = \frac{k}{\log Z}, \qquad |\theta_N| \le \kappa_G + O_{\mathrm{fixed}}(1/\log Z)
$$
的环带测试。这些保留下来的长度落在固定的有界范围内。由所示 Gauss 估计，加权 Fourier 范数之和可和；小环带权重保留在这一齐次的单剖面 Fourier 范数中，而不在非齐次的槽组半范数中。Minkowski 不等式使分离后的行范数穿过此公共密度。当测试尺度重中心化时，现有的 $q_c^{-1/2} q_n^{-1}$ 归一化保持不变，因此不引入额外的 $e^k$ 幂。在最终的 $\epsilon$ 容许范围内选取 $\kappa_G$。对每个固定的 $\theta$，引理 5.2 给出 $\nu_{\sigma\theta\chi_\bullet}(m)$ 在保留全部原始零掩码下的行扇区归约。它涵盖所有非零元素行，包括与 $S$ 相交的那些；此行的范数中不使用因子 $\xi(m)$。行球仅通过 $Q = q b_* X' Y'$ 依赖于固定的重标度槽组 $p_J$，而与存活的标记槽及对偶变量无关。物理槽集保持互不相交，其分离后的系数为乘积形式。因此对 $\theta$ 作有限三角求和并应用引理 14.3，在实际的 $N_*$ 处给出方程 (14.14) 中的指数，其中取保留参数 $\tau_{\mathrm{ref}}$ 以及独立给定的输出与

102
