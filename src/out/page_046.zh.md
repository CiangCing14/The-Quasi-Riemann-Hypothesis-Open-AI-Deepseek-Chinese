固定非负、非零函数 $W_0, W_1 \in C_c^\infty(0, \infty)$，并令 $\Phi(t) = e^t$。定义

$$
I_\eta(X, Y, Z) = \frac{1}{Y} \sum_s \frac{W_1(q_s/Y)\chi_s(b^*)}{\tau \xi(s) \sqrt{q_{b^*} q_s X}} \cdot \sum_{m \in \mathcal{O}} \xi(m) q_s^{-1/2} g_{\chi_s}(s, -m) W_0\!\left(\frac{q_m}{q_{b^*} q_s X}\right) \frac{1}{2\pi i} \int_{(4)} Z^t \Phi(t) T_{m,s,\eta}(t) \, dt. \tag{6.1}
$$

此定义中的掩码去除了 $S$ 处的非单位。方程 (6.1) 中的所有求和沿所示直线绝对收敛；$m$ 与 $s$ 的求和为有限和，因为权重是环形的。

修正项的固定有限傅里叶展开为

$$
\overline{G(A)} = \sum_{\theta \in \widehat{T}} a_\theta \theta(A), \qquad a_\theta = \frac{1}{|T|} \sum_{v \in T} \overline{G(v)} \overline{\theta(v)}.
$$

Parseval 与 Cauchy–Schwarz 给出 $\sum_\theta |a_\theta| \leq |T|^{1/2}$。对于射线类 $\sigma \in T$，选取一个代表元 $s_\sigma$，并令

$$
\nu_\sigma(a) = \eta(a) \Xi(a)^{-1} R(a, s_\sigma) \quad ((a, S) = 1),
$$

$$
B_{m,\sigma}(Z) = \sum_{\theta \in \widehat{T}} a_\theta \frac{1}{2\pi i} \int_{(4)} Z^t \Phi(t) T(t + 1/2, \nu_\sigma \theta \chi_\bullet(m)) \, dt.
$$

将 $\nu_\sigma$ 在远离与 $S$ 互素的主元素之外延拓为零，且不在那里求值 $\Xi(a)^{-1}$。此处的函数 $T$ 是方程 (5.1) 中的完备乘积，带其原始的零掩码。由于对 $s \in \sigma$ 有 $R(A, s) = R(A, s_\sigma)$，修正行的所示 Mellin 积分在整个该类上等于 $B_{m,\sigma}(Z)$。

对于 $m \neq 0$，中心 Mellin 恒等式 (5.31) 给出直接的专门化

$$
B_{m,\sigma}(Z) = \sum_{\theta \in \widehat{T}} a_\theta \mathrm{CVG}(Z; m, \nu_\sigma \theta).
$$

特征 $\nu_\sigma \theta$ 构成一个固定的有限族，其导子与定义模的支集都包含于 $S$ 中。它们不必通过 $T$ 分解。它们原始的零延拓正是完备行矩中的那些，因此该估计直接适用于这个行和族。行 Hilbert 空间中的三角不等式仅耗费固定因子 $\sum_\theta |a_\theta|$。该估计所用的行扇区转换保留了共享好素数处的零点，包括当行赋值被六整除时。

记 $Q = q_{b^*} X Y$。选取 $(0, \infty)$ 上的一个光滑紧支函数 $\Omega$，使其在 $W_1(q_s/Y) W_0(q_m/(q_{b^*} q_s X))$ 的支集上可能出现的每个 $q_m/Q$ 值处都等于 1。对于 $v \in \mathbb{R}$，令

$$
A_{m,\sigma,v}(Y) = \frac{1}{Y} \sum_{s \in \sigma} \frac{W_1(q_s/Y) \chi_s(b^*)}{\tau \xi(s)} (q_s/Y)^{-1/2+iv} q_s^{-1/2} g_{\chi_s}(s, -m).
$$

我们对 $W_0$ 的 Mellin 约定为 $\widehat{W}_0(iv) = \int_0^\infty W_0(r) r^{iv} \, dr/r$。由于 $q_m/(q_{b^*} q_s X) = (q_m/Q)/(q_s/Y)$，Mellin 反演给出精确恒等式

$$
I_\eta(X, Y, Z) = \frac{Q^{-1/2}}{2\pi} \sum_{\sigma \in T} \int_{\mathbb{R}} \widehat{W}_0(iv) \sum_{m \neq 0} \Omega(q_m/Q) \xi(m) (q_m/Q)^{-iv} A_{m,\sigma,v}(Y) B_{m,\sigma}(Z) \, dv. \tag{6.2}
$$

被略去的 $m = 0$ 项由 $W_0$ 的环形支集而消失。因子 $(q_m/Q)^{-iv}$ 的绝对值为 1。在 $A$ 中，算术系数是固定的，且与 $m, v$ 无关地有界；对 $v$ 的全部依赖出现在环形变量的一个范数幂中。

Gaussian $V_G$ 的 Mellin 变换为 $e^t$，并直接满足反射假设。因此引理 5.8 无需对该测试作环形分解即可适用。
