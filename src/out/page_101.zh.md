对于空槽位列表，$za = u = 0$。选取 $\eta > 0$，然后取 $Z$ 足够大，使得两个已显示的常数误差至多为 $\eta$ 且 $e_\lambda \ge -\eta$；后者由 $\log Z \ge 4\log q_\lambda /\eta$ 推出。在一个保留的二元组上，方程 (14.14) 与 $v + 3\ell_b + e_\lambda \le T_d + \tau_{\mathrm{ref}}$ 给出
$$E_{\mathrm{ref}} \le O/2 + \max\{H,\ T_d - S_0 - B_0\} + 53\eta + \tau_{\mathrm{ref}}.$$
对于第一个分支，在使用 $e_\lambda$ 的下界之后丢弃非正项；对于第二个分支，使用 $v \le T_d - 3\ell_b - e_\lambda + \tau_{\mathrm{ref}}$。该最大值关于每个自变量递增。因此我们可以对其第一个自变量使用方程 (5.35)，对其第二个自变量使用方程 (14.17)，然后对对数多个实际的 $H$-二元组求和。取 $\eta$、$\tau_{\mathrm{ref}}$ 以及局部小幂损失相对于 $\epsilon$ 足够小，即证明
$$\sideset{}{'}\sum_{0<q_k \ll Z^M} |T_1(Z^{N_*};\ k)|^2 \ll Z^{O/2 + \max\{M-O,\ 2M-O+Q+V-N_*\}+\epsilon}. \tag{14.18}$$
求和号上的撇号将强大部分限制在其 $O$-二元组上。一个有界对偶范围包含在第一项中；空范围可忽略不计。未使用任何等式 $H = M - O$。

15 补偿低估计

我们现在界定方程 (12.5) 中定义的有限补偿探针。其精确的低分离有两个因子。我们首先通过对标记槽位求和后直接应用引理 14.3 来界定完备行。然后我们证明第 6 节中加性多项式的定量 Gram 界。Cauchy–Schwarz 将结合这些估计给出指数 $3/16$。

15.1 标记完备行

对于一个固定的重标子集 $J$，带有标记子集 $J^c$，置
$$\hat{d} = \sum_{i \in J} \ell_i, \quad X' = X/q_{p_J} \asymp XZ^{-d}, \quad Y' = Y/q_{p_J} \asymp YZ^{-d},$$
$$M' = M - 2d, \quad \ell' = \ell - d, \quad 0 \le d \le \ell = 1/6. \tag{15.1}$$
对于槽位素数的无平方乘积 $D$，定义标记完备级数
$$T_D(s_0, \psi) = \sum_{\substack{c\ \mathrm{sf} \\ n}} \gamma_2(c)\alpha(cn^3)\psi(cn^3)\mathbf{1}_{D \mid cn^3}\, q_c^{-s_0} q_n^{-3s_0+1/2}.$$
理想 $c$、$n$ 是与 $S$ 互素的原始理想，由其主生成元表示，其中 $c$ 无平方；它们可以共享素数。所有特征幂保持其原始的零延拓。对于空乘积 $D = 1$，这就是完备的 $T(s_0, \psi)$。对于这个固定的 $J$，令
$$B^J_{m,\sigma}(Z) = \sum_{\substack{p_i \in P_i(Z),\ i \in J \\ \emptyset \ne P_i \subseteq J}} \prod_{i \in J} \eta(p_i) W_i(q_{p_i}/P_i) \sum_{\theta \in \widehat{T}} a_\theta \frac{1}{2\pi i} \int_{(4)} (Z q_{p_J} c)^t \Phi(t) \cdot T_{p_{J^c}}(t + 1/2,\ \nu_\sigma \theta \chi_\bullet(m))\, dt.$$
因此 $B^J$ 恰好是方程 (12.5) 的 $J$ 被加项在标记槽位求和后的完备行因子。固定元组 $p_J$ 仅在其低分离中影响 $X'$、$Y'$。

引理 15.1（补偿完备行范数）。对于每个 $\epsilon > 0$、每个固定的重标子集 $J$、以及每个 $\sigma \in T$，其中 $Q = q_{b_*} X' Y' \asymp Z^{M'}$，
$$\sum_{0<q_m \ll Q} |B^J_{m,\sigma}(Z)|^2 \ll Z^{M' + ((d-1/6)/4)_+ + \epsilon} = Z^{M' + \epsilon}. \tag{15.2}$$
该界关于固定的重标元组是一致的，且没有依赖于幸存槽位网格的损失。

101
