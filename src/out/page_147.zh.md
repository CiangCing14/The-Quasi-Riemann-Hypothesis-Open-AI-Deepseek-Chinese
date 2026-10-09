对于非空负中心窗口，$q_n \ge 1$ 且方程 (17.74) 给出 $\delta_{\text{init}} \le 3\eta$，而其上支撑端点给出 $Z\delta_{\text{init}} \le b$。若 $N_{c\,\text{init}} \ge 0$，则 $\delta_{\text{init}} = 0$，后一不等式由 $b \ge 1$ 推出。因此在每个保留的情形中都有 $1 \le Z\delta_{\text{init}} \le b$。截断 $\omega_{n,a}(Z\delta_{\text{init}}y)$ 支撑于 $[a/b, b]$ 中，且具有一致有界的 Euler 半范数。其重标度只依赖于固定的中心，而不依赖于当前的行或标号，并且其完整的裁剪族包含于 $ID$ 中。

在形式分解 $z_a = s n_a$ 上，完整的根与核论证恰好为
$$
\frac{Z^{-D'} Z^m}{q_d' q_s q_{n_1} q_{n_2}} \sqrt{\frac{Z^{\kappa_c^{\text{init}}} x_d^{-1} x_s (x_1 x_2)^{-1/2}}{q_s' q_{n_1} q_{n_2}}},\quad
\frac{Z^{m'} q_{h'}^2}{q_d' q_s q_{n_1} q_{n_2}} = A_{\text{ker,init}} \frac{x_h}{x_d x_s^2 x_1 x_2}, \tag{17.75}
$$
$$
A_{\text{ker,init}} = Z^{m+H-\theta-2(D'-B)}.
$$

对于第一个等式，使用 $N_{c\,\text{init}} = D' - B - v$ 以及 $\kappa_c^{\text{init}} = m - 2D' + B - \theta$。等价地，其根为 $x_d^{-1} x_C (x_{c1} x_{c2})^{-1/2}$，其中 $x_{ca} = x_C x_s x_a$。定义单一联合剖面
$$
H_{\text{init},\Sigma,\upsilon}(x) = Z^{-3\eta} \prod_{\alpha} \Omega_{\text{init},\alpha}(x_\alpha) x_d^{-1} x_s (x_1 x_2)^{-1/2}
\times W_0(x_C x_s x_1) W_0(x_C x_s x_2) K_{\text{init}}\!\left(A_{\text{ker,init}} \frac{x_h}{x_d x_s^2 x_1 x_2}\right). \tag{17.76}
$$
其外部标量恰好为 $Z^{\kappa_c^{\text{init}} + 3\eta}$。旧的 $c$-窗口被耦合，因此包含在此剖面中，所有归一化实逆根以及完整核也是如此。没有实根也被放入子测试中。

对于 $\xi = (\xi_C, \xi_d, \xi_s, \xi_h, \xi_1, \xi_2)$，令 $z_n = q_n / Z^{N_{\text{init}}}$，再次置 $\varepsilon_1 = 1$，$\varepsilon_2 = -1$，并定义
$$
W_{a\,\text{init}}(z) = \omega_{n,a}(Z^{\delta_{\text{init}}} z) z^{\varepsilon_a} i^{\xi_a}.
$$
若 $d_a'$ 是 $a$ 侧上存活的子集，则精确的未归一化子多项式为
$$
Q_{a,t,j,\xi}^{\text{init}}(k, f) = \sum_{n \in sf} A^*(n) \rho_{t,j}(n) \chi_n(k) \chi_n(f) 4 d_a'(n) W_{a\,\text{init}}(q_n / Z^{N_{\text{init}}}). \tag{17.77}
$$
其固定的有限特征、穿孔、乘积标记与测试均独立于 $k, f$。两侧可以有不同的测试和子集，但都具有相同的典范系数类。

令 $\Omega_\Sigma$ 由
$$
\omega = (C_{sf}, d' \mid C, s_{sf}, h' \ne 0;\ \text{已分配的槽位素数})
$$
组成，带有保留的个体支撑与槽位分支。它没有当前列指标。函数 $t, k, f$ 是上面定义的乘积；该集合可以在施加所示外部零掩码之前取定，零掩码将包含在权重中。令 $A_\Sigma^{\text{init}}(\omega)$ 为 $d_0$ 的所有已分配系数及其优先掩码在第二侧上取共轭后的乘积。完整的剩余外部权重为
$$
V_\Sigma^{\text{init}}(\omega; \xi) = \mu(d') \mu(s) G(\vartheta) \hat{B}_{\text{init}}(h') \mathbf{1}_{(C,j)=1} \mathbf{1}_{(s,C_j)=1} \mathbf{1}_{(s,h')=1} A_\Sigma^{\text{init}}(\omega)
\times \psi_C(x_C) \psi_{d'}(x_d) \psi_s(x_s) \psi_{h'}(x_h) \omega_f(q_f / Z^{V_c^{\text{init}}}) \tag{17.78}
$$
$$
\times x_C^{i\xi_C} x_d^{i\xi_d} x_s^{i\xi_s} x_h^{i\xi_h} Z^{i\delta_{\text{init}}(\xi_1 + \xi_2)}.
$$
截断 $\omega_f$ 在每个原始标号乘积上均为 1，因此在分离之前其插入是等式。每个 Möbius 因子和射线系数各有一份拷贝。特别地，$(s, h')$ 处的公共零点仍然存在。
