前两个不等式并非以零误差断言。特别地，第三个不等式对每个固定三元组成立，因为它有来源见证，尽管它不必在整个包含计数球上都成立。方程 (17.44) 中的新根式具有实际对数范数 $Q_{\text{new}} = Q_\gamma$，满足

$$
\begin{aligned}
Q_{\text{new}} &\le Q + bt + gb - \theta b \frac{c+b}{} \\
&\le Q + \ell + t + g - \theta + 4\eta \le Q + D_c + 4\eta.
\end{aligned}
\tag{17.50}
$$

当它的因子与旧穿刺共享素数时，这也成立，因为取根式只会减小范数。最后一个不等式使用了 $A_i, V \ge 0$。

在方程 (17.48) 中使用 $F_{\text{ch}} = F_c + \delta_N$，$M_{\text{ch}} = M_c + \eta$，以及 $2(A_i + t + g - \theta + V) + j \ge -4\eta$。两个子边缘满足

$$
\begin{aligned}
F_{\text{ch}} - M_{\text{ch}} - Q_{\text{new}} - z_0 &\ge c_{\text{node}} + \delta_N - 5\eta \ge c_{\text{node}} - 5\eta, \\
4F_{\text{ch}} - 3M_{\text{ch}} - 6z_0 &\ge c_{\text{node}} + 4\delta_N - 7\eta \ge c_{\text{node}} - 7\eta.
\end{aligned}
\tag{17.51}
$$

名义上限 $z_0$ 保持不变，因为幸存标记是一个子集合。此外 $D_c \ge \ell + V - 2\eta$ 且 $2\ell - j \ge -3\eta$，因此

$$
M - M_{\text{ch}} = 2D_c + 2\ell - j - \eta \ge 2(\ell + V) - 8\eta \ge 2d - 8\eta.
\tag{17.52}
$$

对于 $\eta \le d/16$，这至少为 $3d/2$，从而至少为 $d$。同样的恒等式给出 $F_c \le F - \ell - V + 5\eta$，所以 $F_{\text{ch}} \le F + 11\eta$。由于其两个被加数非负，这通过有限深度界定了子 $N_{\text{ch}}, V_c$。

算术构造由此产生了具有更小行长度的容许子范围。我们接下来用它们的规范多项式表示变换后的和。所需的傅里叶密度对所有三元组 $\gamma$、行和标签都是共同的；只有在得到该恒等式之后，我们才会应用 Cauchy 并控制重构重数。

第二个变换和的一个共同密度。在求和任何实际外理想之前，使用六个独立坐标

$$
(y_g, y_d, y_v, y_k, y_1, y_2) = \left( \frac{q'_g}{Z_g}, \frac{q_{d^2}}{Z_\theta}, \frac{q_v}{Z_v}, \frac{q'_k}{Z_{h^2}}, \frac{q_{n_1}}{Z_{N_c}}, \frac{q_{n_2}}{Z_{N_c}} \right).
$$

使用已经选好的新截断 $\omega_{n,a}$，$\omega_f$。保留四个当前二进截断以及反转外侧的 $\omega_f$，以及两列中的 $\omega_{n,a}$。令 $\Omega_{2,\alpha}$ 为更大的截断，在相应的四个二进截断和两个列截断的完整支集上等于一。这些完整支集、$I_f$ 以及其上的形式乘积 $g' v' n$ 是已经包含在 $I_D$ 中的窗口。

确切的第二根和核参数为

$$
\begin{aligned}
\frac{K}{\sqrt{q_{d^2} q'_v q_{n_1} q_{n_2}}} &= Z^{\lambda_c + 12\eta + \tau} y_d^{-1} y_v^{-1} (y_1 y_2)^{-1/2}, \\
\frac{K q''_k}{q_{d^2} q'_v q_{n_1} q_{n_2}} &= A_{\text{ker},2} \frac{y_k}{y_d y_v^2 y_1 y_2}, \\
A_{\text{ker},2} &= Z^{H_{\text{use}} + h^2 - \theta - 2v - 2N_c}.
\end{aligned}
\tag{17.53}
$$

确实 $N_c = s_i - g - v$ 且 $\lambda_c = H_c - \theta - (s_i - g)$。定义一个环境剖面

$$
H_{2,\sigma,t}(y) = Z^{-6\eta} \prod_\alpha \Omega_{2,\alpha}(y_\alpha) y_d^{-1} y_v^{-1} (y_1 y_2)^{-1/2}
\times W_i(y_g y_v y_1) W_i(y_g y_v y_2) K_2 \left( A_{\text{ker},2} \frac{y_k}{y_d y_v^2 y_1 y_2} \right).
\tag{17.54}
$$
