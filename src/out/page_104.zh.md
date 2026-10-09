最后一个不等式对 $y \le Td$ 和 $y \ge Td$ 分别成立。这里平方后的核节省量是这样得到的：先从公共 Fourier 密度中提取 $\min\{1, Z^{(y-Td)/4}\}$，然后再对行范数取平方。相对于 $M'$，在剩余的 $+za$ 之前的节省量恰好为
$$
\begin{aligned}
O/2 + \Delta_H + S_0 + B_0 + T_d/4
&= \frac{2M' + 2za - 1 - \ell' + 2\Delta_H - \theta_N}{4} \\
&\quad + \frac{2A_0 - N_0 + B_0 + 4S_0}{4}.
\end{aligned} \tag{15.3}
$$
第二个分子非负。由于 $za \le \ell'$，该分支中的能量至多为
$$
\begin{aligned}
& M' + \frac{1 + 3\ell' - 2M' - 2\Delta_H + \theta_N}{4} + O(\epsilon_0 + \kappa_G + \epsilon_Z) \\
&= M' + \frac{d - 1/6 - 2\Delta_H + \theta_N}{4} + O(\epsilon_0 + \kappa_G + \epsilon_Z).
\end{aligned}
$$
在利用 $O \ge -\epsilon_Z$ 并吸收 $\theta_N$ 之后，两个上界为
$$
M' - \Delta_H + O(\epsilon_0 + \kappa_G + \epsilon_Z),
$$
$$
M' + \frac{d - 1/6 - 2\Delta_H}{4} + O(\epsilon_0 + \kappa_G + \epsilon_Z).
$$
它们关于 $\Delta_H$ 非增。由于 $\Delta_H \ge -\epsilon_Z$，它们的形式上 $\Delta_H = 0$ 的取值将每个实际的二元组控制到 $O(\epsilon_Z)$ 以内，无论端点二元组是否出现。因此它们的最大值至多为 $M' + ((d-1/6)/4)_+ + O(\epsilon_0 + \kappa_G + \epsilon_Z)$。当 $d = 1/6$ 时，有 $\ell' = za = 0$，且截断的单位区间落在第一个分支中；有界的负单位二元组只改变 $\epsilon_Z$。在规定的 $\epsilon$ 容差内选取 $\epsilon_0$ 和 $\kappa_G$，然后提高固定数据下阈值，使 $\epsilon_Z$ 也落在其中。对对数多个行二元组和对偶二元组求和即证得该引理。

15.2 加性 Gram 界

接下来我们估计范围 $Y'^2/Q \ge 1$ 中的加性因子。引理 13.3 的完全相关保留了决定其相消及其例外频率的碰撞零点。

命题 15.2（定量加性 Gram 界）。固定算术数据 $S, T, b^*, \xi$，环形权 $W_1$，以及一个射线类 $\sigma \in \mathcal{T}$。设 $Q, Y' \ge 1$ 处于 $Z$ 中的固定多项式范围内，并假设
$$
P_a = Y'^2/Q \ge 1.
$$
对于实高度 $\nu$，按第 6 节的定义置 $A_m = A_{m,\sigma,\nu}(Y')$。对每个固定的行球 $q_m \ll Q$ 和每个 $\epsilon > 0$，有
$$
\sum_{q_m \ll Q} |A_m|^2 \ll (1 + |\nu|) J_{\mathrm{Gr}} Q^{1/6} \left(1 + P_a + \frac{P_a^2}{Y'}\right) Z^{\epsilon}. \tag{15.4}
$$
这里 $J_{\mathrm{Gr}}$ 是一个固定的半范数阶，与变动尺度和 $\nu$ 无关。对射线系数 $1_{s \in \sigma}\chi_s(b^*)/\xi(s)$ 的任意固定有限线性组合，同样的断言成立。不断言任意依赖于行的算术系数。

证明。用一个固定的非负径向 Schwartz 函数对行球作控制。置 $r_s = q_s/Y'$，并在与 $S$ 互素的原始元素上置 $c_\sigma(s) = 1_{s \in \sigma}\chi_s(b^*)/(\tau \xi(s))$，在计算逆特征之前于其他处用零延拓。该多项式的精确环形改写为
$$
A_m = Y'^{-3/2} \sum_s c_\sigma(s) W_1(r_s) r_s^{-1+i\nu} g_{\chi_s}(s, -m).
$$
于是展开后的平方具有公共归一化因子 $Y'^{-3}$，且联合环形剖面包含因子 $W_1(r_{s_1}) r_{s_1}^{-1+i\nu} W_1(r_{s_2}) r_{s_2}^{-1-i\nu}$。记 $s_1 = Cn_1$，$s_2 = Cn_2$，其中 $(n_1, n_2) = 1$。

104
