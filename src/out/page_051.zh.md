令 $x = t + 1 - z$，在两个权重的 Mellin 反演之后。对于非零且不含六次方因子的 $u$，且 $(u, S) = 1$，定义
$$F_{\eta,u}(x, w, z) = \sum_{\substack{c \text{ sf} \\ n,s,a}} K_\eta(c, n, s, a; u)\, q_c^{-1/2-x} q_n^{-1-3x} q_s^{-w} q_a^{-6z}, \tag{7.3}$$
其中 $A = cn^3$，而保留全部归一化因子的系数为
$$K_\eta(c, n, s, a; u) = \frac{F(s, A, ua^6)\chi_s(b^*)}{\sqrt{q_{b^*}}\, \tau\, \xi(s)\xi(u)}\, \gamma_2(c)\alpha(A)G(A)\eta(A)\Xi(A)^{-1}R(A, s). \tag{7.4}$$

为方便起见，定义公共的 Mellin 权重
$$W(X, Y, Z; x, w, z) = X^{1/2-z} Z^{x+z-1} Y^{w-1} \Phi(x + z - 1) M(z) W_{c_1}(w).$$

例如，直线 $\Re x = 3$、$\Re w = 3$、$\Re z = 2$ 对应于原本的直线 $\Re t = 4$，并且落在绝对收敛区域内。完整的高阶恒等式为
$$I_\eta(X, Y, Z) = \frac{1}{(2\pi i)^3} \int_{(3)} \int_{(3)} \int_{(2)} W(X, Y, Z; x, w, z) \cdot \sum_u q_u^{-z} \xi(u) F_{\eta,u}(x, w, z)\, dz\, dw\, dx. \tag{7.5}$$

人们可以用初等界 $|F(s, A, H)| \le q_s q_{b^*} A$ 以及环形权重来证明这些直线上的所有交换都是合理的。特别地，方程 (6.2) 与 (7.5) 是对同一探针成立的恒等式，而不是针对分别选取的测试表达式所作的估计。

7.2 标量 Euler 恒等式

接下来我们计算方程 (7.4) 中的系数。我们的目标是证明高阶级数是目标 $\eta$ 的标量 Euler 乘积。该计算还单独记录了在给定素数处完备指标 $A$ 具有正赋值的那些项。我们保留每一个射线相位，直到它被消去或被赋予某个局部因子。

固定一个非零且不含六次方因子的行 $u$，且 $(u, S) = 1$，并取素数 $p \notin S$。置
$$Q = q_p, \quad j = v_p(u) \in \{0, \ldots, 5\}, \quad \rho = \chi_p(u/p^j), \quad \omega_p = \chi_p(-1),$$
$$a_p = \alpha(p)^3 \eta(p)^3, \quad b_p = \alpha(p)^2 \eta(p)^2 \chi_p(4), \quad b_p^3 = a_p^2, \tag{7.6}$$
$$V = Q^{-6z}, \quad R = a_p^2 Q^{4-6x-6z}, \quad W_{\text{loc}} = \rho Q^{-w}.$$

值 $\rho$、$a_p$、$b_p$ 的绝对值为一，而 $\omega_p \in \{1, -1\}$。对 $p$ 不施加任何射线类限制。

有限标量及其单位因子。记 $G_r = g_{\chi_p^r}(p, 1)$，其中 $G_0 = -1$，并对 $1 \le r \le 5$ 记 $\gamma_r = Q^{-1/2} G_r$。对于 $t \ge 1$ 和 $j' \ge 0$，对一个模 $p$ 的剩余类的提升求和给出
$$g_{\chi_p^r}(p^t, p^{j'}) = \begin{cases} Q^{t-1} G_r\, \mathbf{1}_{j' = t-1}, & 6 \nmid r, \\ Q^t \mathbf{1}_{j' \ge t} - Q^{t-1} \mathbf{1}_{j' \ge t-1}, & 6 \mid r. \end{cases}$$

第二行是主特征经零延拓后的 Ramanujan 和。正交性还给出 $G_1 G_{-1} = \omega_p Q$。
