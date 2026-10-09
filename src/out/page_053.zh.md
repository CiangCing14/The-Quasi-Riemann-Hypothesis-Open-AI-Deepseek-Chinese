去掉剩余配对乘积的无平方因子部分。若 $e_p = v_p(c)$，$l_p = v_p(n)$，则其在配对 $p < r$ 处的指数为 $t_p t_r - e_p e_r = 3(e_p l_r + e_r l_p + 3 l_p l_r)$。$\chi_p(r)\chi_r(p)$ 的立方是 $R(p, r)$，其平方为 1。因此，在此除法之后所剩的配对乘积为
$$\prod_{p<r} R(p, r)^{e_p l_r + e_r l_p + l_p l_r} = R(c, n)G(n_3) \prod_p G(p_3)^{l_p} R(p, p)^{-e_p l_p - l_p(l_p-1)/2}.$$
该等式通过对 $n_3$ 的素因子展开二次加细方程 (4.5) 得到。同一加细给出 $G(c)R(c, n)G(n_3) = G(cn_3)$，它被插入的 $G(cn_3)$ 所抵消。最后，方程 (4.6) 给出 $G(p_3) = \gamma_3(p)$ 和 $R(p, p) = \omega_p$。这些恒等式解释了所有配对相位，且对 $p$ 的射线类没有限制。

因此，方程 (7.4) 中的系数已分解为素因子。在绝对收敛下，其在 $p$ 处的因子是级数
$$P_p = \sum_{\substack{e_0 = 0, 1 \\ l, k, m \ge 0}} (-1)^{e_0} \gamma_1^{-e_0} \eta(p)^{e_0} (a_p \gamma_3)^l \rho^{k-t} \omega_p^{t k - e_0 l - l(l-1)/2} C_p(t, k, j + 6m) \cdot Q^{-(x+1/2)e_0 - (1+3x)l - wk - 6zm}, \quad t = e_0 + 3l. \tag{7.10}$$
设 $P_p^*$ 为限制在 $t > 0$（等价地，完备化指数 $A$ 具正赋值）上的同一和。

引理 7.1（完备局部恒等式）。对每个非零六次无幂 $u$，$(u, S) = 1$，以及每个素点 $p \notin S$，刚定义的因子为
$$P_p^* = \frac{1}{1-R} \left[ R(1 - Q^{-1}) - \eta(p)(Q - 1)Q^{-x-w} V \mathbf{1}_{j \le 1} \right] + J_j, \tag{7.11}$$
$$P_p = \frac{1}{1-V} + \mathbf{1}_{j=0} \frac{W_{\mathrm{loc}}}{1 - W_{\mathrm{loc}}} + P_p^*,$$
其中 $J_j$ 的六个值为

j   J_j
0   $-\eta(p)\rho^{-1}Q^{-x} + W_{\mathrm{loc}} R$
1   $\eta(p)Q^{-x-w}$
2   $a_p \rho^{-3} Q^{3/2-3x}$
3   $-\eta(p)b_p \rho^{-2} Q^{2-3x-w} + b_p^2 \rho^{-4} Q^{2-4x}$
4   $-\eta(p)a_p \rho^{-3} Q^{5/2-4x-w}$
5   $-a_p^2 Q^{3-6x}$.

令 $W = \chi_p(u)Q^{-w}$，$D = \eta(p)\chi_p(u)Q^{-x}$，在 $p \mid u$ 处取原零延拓，并定义
$$H_p = P_p \frac{(1 - V)(1 - W)}{1 - D}, \quad H_{\eta, u} = \prod_{p \notin S} H_p. \tag{7.12}$$
则方程 (7.3) 中的级数具有标量分解
$$F_{\eta, u}(x, w, z) = \frac{\zeta_F^S(6z) L_S(w, \chi_\bullet(u))}{L_S(x, \eta \chi_\bullet(u))} H_{\eta, u}(x, w, z). \tag{7.13}$$
记 $x_r = \Re x$，$w_r = \Re w$，$z_r = \Re z$。对每个固定的 $\epsilon_0 > 0$，修正乘积在下列每个区域中每一点的邻域上正规收敛，因而在那里定义了一个全纯函数：

$$x_r \ge 51/100, \quad z_r \ge 17/50, \quad w_r \ge -1/100, \quad x_r + w_r \ge 1 + \epsilon_0; \tag{7.14}$$
$$x_r \ge 7/8, \quad z_r \ge 33/200, \quad w_r \ge 19/20. \tag{7.15}$$

53
