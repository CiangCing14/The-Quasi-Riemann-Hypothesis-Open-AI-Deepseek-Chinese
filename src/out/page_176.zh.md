引理 18.3（带掩码的矩形消去）。设 $\vartheta$ 取遍一个固定的有限集合，其中的元素是导子素因子属于 $S$ 的有限阶射线特征。设 $R^*$ 无平方因子，且对某个固定的 $B^*$ 有 $q_{R^*} \le Z^{B^*}$，并设 $W_1, W_2$ 是固定圆环上的光滑剖面。对 $X > 0$ 和 $t \in \mathbb{R}$，定义
$$
L_i(X,t) := \sum_l \vartheta(l) \mathbf{1}_{(l,R^*)=1} q_l^{it} W_i(q_l/X).
$$
则
$$
L_i(X,t) = c_{\vartheta,R^*} X^{1+it} I_i(t) + O\left(Z^{\epsilon_1}(1+|t|)^J\right), \tag{18.45}
$$
$$
|L_i(X,t)| \ll X. \tag{18.46}
$$
这里 $J$ 固定，常数用到有限多个半范数，$c_{\vartheta,R^*}$ 与 $X,t$ 无关，而 $I_i(t)$ 是一个固定测度常数乘以 $\int_0^\infty W_i(y) y^{it} \, dy$。这两个估计对 $X > 0$、所述的掩码以及有限特征集都是一致的。

令 $D_b$ 如式 (18.17) 所定义，并置
$$
U_i = X_i / q_{b_i}, \quad V_i = Y_i / q_{b_i}, \quad T = U_1 U_2 = V_1 V_2.
$$
若对 $i = 1,2$ 及某个 $r \ge 0$ 有 $U_i, V_i \ge Z^r$，则
$$
T^{-1/2} \sum_{l_1,l_2} \vartheta(l_1)\vartheta(l_2) \mathbf{1}_{(l_1 l_2, R^*)=1} q_{l_1}^{it_1} l_2 D_b(l_1,l_2) \ll Z^{\epsilon_1} (1+|t|)^{2J} T^{1/2} Z^{-r}. \tag{18.47}
$$
若无非负的长度下界，同一表达式为 $O(T^{1/2})$。

证明。首先略去掩码。代表 $S$ 之外的理想、带有固定特征权 $\vartheta$ 的主生成元，是固定格中有限个带权剩余类。在该格上对
$$
f_{X,t}(z) = q_z^{it} W_i(q_z/X) = X^{it} f_t(z/\sqrt{X}), \quad f_t(z) = q_z^{it} W_i(q_z).
$$
应用 Poisson 求和。Fourier 变换为 $X^{1+it} \hat{f}_t(\sqrt{X}\xi)$。由于 $f_t$ 支在固定圆环上，对任意固定的 $J_0 > 2$，分部积分给出
$$
|\hat{f}_t(\xi)| \ll_{J_0} (1+|t|)^{J_0} (1+|\xi|)^{-J_0},
$$
其中用到 $W_i$ 的有限多个半范数。因此对 $X \ge 1$，固定对偶格上非零点的求和为
$$
\ll (1+|t|)^{J_0} \sqrt{X} \sum_{\xi \neq 0} (1+\sqrt{X}|\xi|)^{-J_0} \ll (1+|t|)^{J_0}
$$
必要时可增大 $J_0$。对 $0 < X < 1$，由固定圆环上的绝对计数，格和及其零频主项均为 $O(1)$。零频为 $c_\vartheta X^{1+it} I_i(t)$，其中 $c_\vartheta$ 是剩余类的固定加权平均。这证明了式 (18.45) 的无掩码版本。

现在用容斥插入掩码。首先从 $R^*$ 中删去属于 $S$ 的素数，因为每个求和理想已经避开它们。因此下面所用的所有除数都在 $S$ 之外。以 $L_i^0$ 记无掩码的和，由乘性得
$$
L_i(X,t) = \sum_{d|R^*} \mu(d)\vartheta(d) q_d^{it} L_i^0(X/q_d, t).
$$
主系数为
$$
c_{\vartheta,R^*} = c_\vartheta \sum_{d|R^*} \frac{\mu(d)\vartheta(d)}{q_d}.
$$

176
