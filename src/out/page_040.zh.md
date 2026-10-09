选定一项。设 $N_F$ 为指派给无平方因子理想 $n_0$ 的素数的乘积，并设 $B_F$ 为指派给 $b_0$ 但不指派给 $n_0$ 的素数的乘积。记 $n_0 = N_F n$，$b_0 = B_F b$。在第一次指派中，只提取 $n_0$ 中的出现，即使 $b_0$ 含有该素数；在第二次指派中，从 $b_0$ 中恰好提取一次出现。所有剩余的源限制都保留在 $n, b$ 上。设 $F_{\mathrm{sm}}$ 为小的 $j_p = 4$ 被加项与活跃的 $j_p = 0$ 素数的乘积，并令
$$A_0 = \log_Z q_{\mathrm{Fact}}, \quad S_0 = \log_Z q_{F_{\mathrm{sm}}}, \quad N_0 = \log_Z q_{N_F}, \quad B_0 = \log_Z q_{B_F}.$$
空乘积的对数范数为零。
  固定一个单位 $u$、一个整数 $k \ge -4$，以及对偶范围
$$\mu = u\lambda^k N_F n (B_F b)^3, \quad q_n \asymp Z^v, \quad q_b \asymp Z^{\ell_b}, \quad q_{\lambda_k} = Z^{e_\lambda}.$$
其中 $v, \ell_b \ge 0$。无平方因子的 $n$ 与本原的 $b$ 保留方程 (5.2) 的完整源支撑，包括 $S$ 的允许素数以及共享素数。设 $H \ge 0$，并在一个固定的紧致对数箱上选取一个公共的光滑剖面 $W_1(y_R, y_n, y_b)$，其中
$$y_R = q_R/Z^H, \quad y_n = q_n/Z^v, \quad y_b = q_b/Z^{\ell_b}.$$
为这三个范围选取固定的光滑环形截断 $\chi_{\mathrm{row}}, \chi_n, \chi_b$，并令
$$W_0(y) = \chi_{\mathrm{row}}(y_R)\chi_n(y_n)\chi_b(y_b)W_1(y).$$
其支撑集与所涉及的半范数在整个块上一致固定。用 $U_{v,\ell_b,e_\lambda}(R)$ 表示方程 (5.1) 右端中指定的项，限制于此对偶表示并乘以 $W_0(y_R, y_n, y_b)$。原始行集 $I_H$ 由满足 $\chi_{\mathrm{row}}(q_R/Z^H) \ne 0$ 的允许的 $R$ 组成。此定义对上述每一个固定选择分别作出。
    此定义中的冻结素数在不同调用之间可以变化；它们不被加入固定的算术模数 $L$。该定义仅在取当前关于 $R$ 的范数之前固定它们。
引理 5.7（无标记反射块）。对于一个无标记反射块，令
$$T_0 = 2H + 2A_0 - N - N_0 - 3B_0, \qquad \nu_0 = \frac{v}{2} + \ell_b + \frac{e_\lambda}{3} + \frac{S_0 + B_0}{2}.$$
设所有这些对数长度在一个固定有界集上取值。令
$$Y = \frac{q_{\lambda_k} N_F B_F^3 X Z^v Z^{3\ell_b}}{q_{c_F}^2 \mathrm{Fact}\, Z^{2H}}, \quad W(y) = y_n^{-1/2} y_b^{-1} W_0(y), \quad F_Y(y) = W(y) V^\sharp(Y y_n y_b^3 y_R^{-2}).$$

存在函数 $\rho(R)$ 与 $\beta(n, b)$，其绝对值至多为 1，使得 $\beta$ 与 $R$ 无关，并且
$$U_{v,\ell_b,e_\lambda}(R) = Z^{-\nu_0} \rho(R)\, \frac{1}{3} \sum_{n,b} \beta(n, b) \chi_R(nb)^3 F_Y(y_R, y_n, y_b). \tag{5.32}$$

该求和保留定义中所有固定的对偶限制。这里唯一同时依赖于 $R$ 与对偶变量的算术因子是所展示的零延拓二次符号。此外，
$$\frac{q_\mu X}{q_c^2} = Y y_n y_b^3 y_R^{-2}, \quad c = c_F \mathrm{Fact}\, R. \tag{5.33}$$
这是原始支撑集上的一个精确恒等式，包括当 $N_F$ 与 $b$ 共享素数时。
    对每个 $\epsilon > 0$ 以及每个固定的 $A \ge 0$，
$$\begin{aligned} \sum_{R \in I_H} |U_{v,\ell_b,e_\lambda}(R)|^2 &\ll_{\epsilon,A} Z^{E_0+\epsilon} p_5(W)^2 M_{A,\lceil 4A \rceil+7}(V)^2, \tag{5.34}\\ E_0 &= \max(H, v + \ell_b) - S_0 - B_0 - \ell_b - \frac{2e_\lambda}{3} - \frac{1}{2}(T_0 - v - 3\ell_b - e_\lambda)_+. \end{aligned}$$

                                                         40
