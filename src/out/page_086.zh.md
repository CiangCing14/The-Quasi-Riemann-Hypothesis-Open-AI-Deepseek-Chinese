第 8 节中的精确 bin 上界适用，因为 $\beta_{*}> 7/8 > 51/100$。对每个保留下来的非主行及其 bin $(i, a)$，它给出
$$a \le \beta_{*}, \qquad \delta = 2a - 1 \le \kappa \le \frac{5}{6}. \tag{12.2}$$
事实上，定义 $M_i(u)$ 的有限集由下取整 $51/100$ 以及实际零点的实部组成，全都至多为 $\beta_{*}$。这里只用到上确界的定义，而非其可达性。边界情形 $\delta = 5/6$ 仍属于论证的一部分。

对于命题 2.1 的第二次应用，在第二部分中始终记
$$C(s) = C_{II}(s) := s - \frac{11}{16}, \qquad C(7/8) = \frac{3}{16}. \tag{12.3}$$
我们的任务是从下面的有限表达式构造一个归一化探针 $J_{II,\eta}$。它不同于平衡探针 $J_{I,\eta}$。其低端目标是 $|J_{II,\eta}(Z)| \ll_\eta Z^{3/16+\omega}$，其中共同的 $0 < \omega < \Delta$；其高端必须满足式 (2.5) 中以此 $C$ 表示的信号估计。非零标量归一化将在主项求值之后指定。

对每个本原目标 $\eta$，使用第 6 节中数据 $T, S, b_*, \xi, \tau, \Xi, W_0, W_1$ 的一个容许固定实例。$P_0$ 的允许选择将在下面的参数顺序中作出。这些数据可以不同于第一部分所用的数据，但在本次应用中它们与 $Z$ 无关，并且在物理探针及其高端表示中相同。

我们首先在原始探针上定义双项修正，然后再移动任何围道。随后的低端和高端估计将涉及这同一个有限表达式。

使用固定的几何构型
$$b = \frac{1}{8}, \qquad h = \frac{13}{16}, \qquad \ell = \frac{1}{6},$$
$$l_x = 1 + \ell - h = \frac{17}{48}, \qquad l_y = l_x + b = \frac{23}{48}, \tag{12.4}$$
$$X = Z^{l_x}, \qquad Y = Z^{l_y}, \qquad M = l_x + l_y = \frac{5}{6}, \qquad M + \ell = 1.$$
固定总长度为 $\ell$ 的正槽长 $\ell_1, \ldots, \ell_K$，并令 $P_i = Z^{\ell_i}$。每个物理槽具有非负、非零的光滑环形权重 $W_i(q_p/P_i)$。其允许的素数集为
$$\mathcal{P}_i(Z) = \{p \text{ 为素数} : p \notin S,\ p \in 1_T,\ q_p/P_i \in \operatorname{supp} W_i\}.$$
在施加射线和 $S$ 限制之前，要求不同槽的基础窗口集 $\{p \text{ 为素数} : q_p/P_i \in \operatorname{supp} W_i\}$ 互不相交。特别地，集合 $\mathcal{P}_i(Z)$ 互不相交，且 $\prod_i \mathcal{P}_i(Z)$ 中的每个元组都由互不相同的素数组成。槽的数量和长度将在后面选择，但它们与 $Z$ 无关地固定。下面关于槽 $i$ 的对 $p \in 1_T$ 的求和始终保留这同一个排除条件和环形支集。

对于槽素数的无平方乘积 $D$，令 $I_{\eta;D}(X, Y, Z)$ 表示式 (6.1) 中在其完整行内插入指示函数 $1_{D \mid c_{n_3}}$ 后的结果。因此 $I_{\eta;1} = I_\eta$。对于元组 $(p_1, \ldots, p_K) \in \prod_i \mathcal{P}_i(Z)$ 和 $J \subseteq \{1, \ldots, K\}$，记 $p_J = \prod_{i \in J} p_i$，其中 $p_\emptyset = 1$。子集 $J$ 索引重标度槽，$J^c$ 索引标记槽；此子集记号不同于归一化探针 $J_{II,\eta}$。由下面的有限恒等式定义修正探针
$$I_{\eta,\text{modified}}(Z) = \sum_{(p_i) \in \prod_i \mathcal{P}_i(Z)} \prod_{i=1}^K W_i(q_{p_i}/P_i) \sum_{J \subseteq \{1, \ldots, K\}} (-1)^{|J|} q_{p_J}^{-3/2} \eta(p_{J^c}) \cdot I_{\eta; p_{J^c}}(X/q_{p_J}, Y/q_{p_J}, Z q_{p_J^c}). \tag{12.5}$$
等价地，在每个素数 $p$ 处，该运算为标记项 $\eta(p) I_{\eta;p}(X, Y, Z q_p)$ 减去重标度项 $q_p^{-3/2} I_\eta(X/q_p, Y/q_p, Z)$。公式 (12.5) 指定了它们的复合：每个槽

86
