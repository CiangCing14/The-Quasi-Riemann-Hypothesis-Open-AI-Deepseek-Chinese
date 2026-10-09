命题 8.3（两个饱和见证元）。设 $u$ 有一个箱子 $(i, a)$，其中 $a > 51/100$，并假设引理 8.2 的损失与高度假设成立。对每个 $t \in [1, 3/2]$，以及每个给定的 $\epsilon > 0$，在缩减其预备损失之后，存在 $\psi \in X_u$、一个如引理 8.1 中的零点 $\rho = \sigma + i\gamma$、二进长度 $D = U^r$、$N = U^m$，以及两个多项式 $M_r$、$S_m$，它们对应于公共行特征 $\psi$，使得

$$r \leq t + O(1/\log U), \quad r + m \geq t - O(1/\log U), \quad |M_r S_m|_2 \gg_{A,\epsilon} U^{\delta(r+m)-\epsilon}. \tag{8.3}$$

它们的长度与各自的值也满足

$$t - \tfrac{1}{2} - O(\epsilon) \leq r \leq t + O(1/\log U), \quad 0 \leq m \leq \tfrac{1}{2} + O(\epsilon),$$
$$|M_r|_2 \gg_{A,\epsilon} U^{\delta r-\epsilon}, \quad |S_m|_2 \gg_{A,\epsilon} U^{\delta m-\epsilon}. \tag{8.4}$$

$O(\epsilon)$ 项中的常数在所陈述的参数范围内是绝对的。两个多项式具有相同的扭曲高度 $\gamma - \nu$，其中 $|\nu| \leq cT_1$，$c > 0$ 为在累积频率容许范围内选定的固定常数。它们的非扭曲剖面构成一个一致光滑的环状族。对每一行，两个见证元都使用一个表示 $\psi_{u,\vartheta,\varsigma}$，其由固定有限集 $\Theta \times \{-1, 1\}$ 中的一个标签 $(\vartheta, \varsigma)$ 选定。表示本身随 $u$ 变化。二进对同样可以对每一行从 $O((\log U)^2)$ 种可能性中分别选取。

证明。截断逆与 Gamma 积分构造是经典零点检测器的一种形式；比较 [21, 附录 C] 与 [14, 第 13.1 节]。此处所需的带缓冲的依赖行的矩形以及同时下界将在下面建立。选取由箱子提供的零点 $\rho$ 并置

$$D_* = U^t, \quad Y_* = U^{20}.$$

设 $V_\leq$ 为一个固定的光滑函数，在 $[0, 1]$ 上等于一，在 $[2, \infty)$ 上等于零。定义

$$C_\psi(s) = \sum_l \mu(l)\psi(l)V_\leq(q_l/D_*)q_l^{-s}, \quad J = \frac{1}{2\pi i}\int_{(2)} Y_*^z \Gamma(z)L_{\mathrm{orig}}(\rho + z, \psi)C_\psi(\rho + z)\, dz.$$

行特征非主，故 $L_{\mathrm{orig}}$ 为整函数。将直线移至 $\Re z = -1/4$ 仅穿过 $\Gamma(z)$ 在零处的极点，其留数因 $L_{\mathrm{orig}}(\rho, \psi) = 0$ 而消失。式 (4.14) 中的全局带状界，连同被删除的 Euler 因子，将新直线界为

$$U^{-5} U^2 D_*^{1-\sigma+1/4+o(1)} T_1^2.$$

确实 $\Re(\rho - 1/4) \geq 26/100 > 0$，故被删除的乘积具有任意小的 $U$ 幂次；刻意较弱的 $U^2$ 包含了本原导子界。有限多项式利用理想计数由所示 $D_*$ 的幂次界定。最后，附加高度中的固定多项式对 $\Gamma(-1/4 + iv)$ 可积，因为 $(1 + |\gamma + v|)^2 \leq (1 + |\gamma|)^2(1 + |v|)^2$。对 $1 \leq t \leq 3/2$ 一致地有

$$-3 + t(5/4 - \sigma) \leq -3 + \frac{3}{2}\cdot\frac{5}{4} - \frac{51}{100} = -\frac{189}{100}.$$

因此 $J = o(1)$。此 Gamma 积分仅使用全局上界，不消耗任何倒数高度容许量。

在原始直线上，绝对收敛性与指数的 Mellin 公式给出

$$J = \sum_{l,k} \mu(l)\psi(lk)V_\leq(q_l/D_*)(q_l q_k)^{-\rho} e^{-q_l q_k/Y_*}.$$

对 $1 < q_n \leq D_*$，$\psi(n)q_n^{-\rho}$ 的系数为 $\sum_{l \mid n} \mu(l) = 0$。对 $n = 1$ 它等于一。当 $qn > D_*$ 时，$V_\leq(2q_n/D_*) = 0$。因此插入 $1 - V_\leq(2q_l q_k/D_*)$ 恰好移除单位贡献 $e^{-1/Y_*} = 1 + o(1)$。由此产生的尾部绝对值为 $1 + o(1)$。将其乘以

59
