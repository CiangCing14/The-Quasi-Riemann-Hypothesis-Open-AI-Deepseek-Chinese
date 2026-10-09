平均后仍为 $\frac{1}{|P|}\sum_{p\in P}$，因此对冻结的 $p$ 一致的界不会引入素因子计数。对每个误差集
$$\ell = 0,\quad g = J_+ + \sigma$$
并将其原始行直接放大为长度为 $K + g$ 的光滑球。误差不再被放大。三类范数均满足
$$0 \le w_o \le w \le 7\sigma/3. \tag{18.29}$$

零行仅在最终光滑球处加入。令 $Y_{\mathrm{col}} = e^{H_N}Z^{a_0} = Z^{a_0+\theta_N}$。非空的列壳层满足 $Y_{\mathrm{col}} \ge 1$，从而 $a_0 \ge -\theta_N$。由式 (13.5)，除非 $u$ 是六次幂，否则 $G(u,0) = 0$，且 $|G(u,0)| \le q_u^{1/2} \le Y_{\mathrm{col}}^{1/2}$。在此支撑集上有 $O(Y_{\mathrm{col}}^{1/6})$ 个六次幂。若 $s \mid u$，则 $q_s^6 \le q_u \le Y_{\mathrm{col}}$，故 $s_0 \le (a_0 + \theta_N)/6$。计入指定的除数有界卷积损失后，中心归一化后的平方贡献为
$$\ll Z^{-a_0} Y_{\mathrm{col}}^{1/6} Y_{\mathrm{col}}^{1/2} \Big)^2 Z^{\epsilon_1} = Z^{a_0/3 + 4\theta_N/3 + \epsilon_1} \le Z^{a_0 - s_0 + 2\theta_N + \epsilon_1}.$$

最后一个不等式由 $a_0 \ge -\theta_N$ 及 $s_0$ 的上述界得到。因此式 (18.25) 可用数值修正 $2\theta_N$（已包含在 $C_*\xi$ 阶段的容差中）来界定这一新增行。这里 $C_* \ge 1$ 表示一个阶段中聚集支撑误差的公共常数，其选取与槽数 $N$ 无关。以下估计将确立一个这样的选取可覆盖一个阶段中的所有运算。零永远不会乘以池中的素数。

18.6 第二次变换与更小宽度的乘积

在展开平方之前恢复所有活跃槽的和。令 $B(u)$ 表示前述某个 Gauss 多项式中完整分配的卷积系数，包括其固定掩码与 $s$-整除条件。当使用中心化时，它包含整个差。其模满足 $q_u/Z^{a_0} \in \exp([-H_N, H_N])$。令 $\Phi_2$ 为定义最终行球的非负光滑径向函数。除素数密度中的 $Z^{o(1)}$ 损失外，待界定的范数为
$$Z^{-\ell} \sum_h \Phi_2(q_h/Z^{K+g}) Z^{-a_0/2} \sum_u B(u)\tau_1(u) q_u^{it} G(u,h) \Bigg|^2.$$

引理 13.3 中的 Fourier 恒等式给出其精确展开
$$Z^{K+g-\ell-a_0} \sum_{u,v} \frac{B(u)B(v)\tau_1(u)\tau_1(v) q_u^{it} q_v^{-it}}{\sqrt{q_u q_v}} \sum_j F(u,v;j) \widehat{\Phi}_2\!\left(\frac{Z^{K+g} q_j}{q_u q_v}\right).$$

此处出现的核为
$$\widehat{\Phi}_2\!\left(\frac{Z^{K+g} q_j}{q_u q_v}\right). \tag{18.30}$$
上述显示的逆平方根与此核均作为完整 $u, v$ 的函数保留，直至下文将其整体乘积分离。特别地，该公式包含每个活跃素数及每个共享素数的重数。

在 $j = 0$ 时，引理 13.3 只剩 $u = v$，且 $F(u,u;0) = \varphi(u) \le q_u$。在非空壳层上，被 $s$ 整除的支撑模数个数至多为
$$C \frac{Y_{\mathrm{col}}}{q_s} = C Z^{a_0 - s_0 + \theta_N},$$
因为在该壳层上写 $u = sv$ 有 $Y_{\mathrm{col}}/q_s \ge 1$。除数有界系数使用其单独的 $\epsilon_1$ 份额。因此对角指数为 $K + g - \ell - s_0 + \theta_N$，包括当 $a_0 - s_0$ 为
