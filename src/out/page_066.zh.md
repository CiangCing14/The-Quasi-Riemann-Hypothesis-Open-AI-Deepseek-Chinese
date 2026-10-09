其中 $a_1, \ldots, a_5$ 两两互素且无平方因子，$a_6$ 任意。取 $a_i \in X_i$ 并令 $X = \prod_i X_i$；这里 $X_i \geq 1/2$ 且 $\prod_i X_i \asymp M$。选取 $\ell \in \{1, 2\}$ 使得 $X_\ell = \max(X_1, X_2)$。当其余因子固定后，系数
$$
\lambda'_b = \lambda_b \prod_{i \neq \ell} F_b(a_i)_{ij}
$$
的绝对值至多为 $|\lambda_b|$，而剩余的核恰好是 $D_{j_\ell \bmod 6}(X_\ell, N)$ 的核。将其固定的正行限制放大即得此范数界。这包括了六次幂因子的零点。集合 $J$ 在映射 $j \mapsto j_\ell \bmod 6$ 下封闭。对固定的理想计数，并在正和中忽略它们的互素性，得到
$$
E_j(M, N) \ll_{S,\varepsilon} (MN)^\varepsilon \max_X \min\left\{ M^{1/3}, (M/X_\ell)^{2/3} D_{j_\ell \bmod 6}(X_\ell, N) \right\}. \tag{9.13}
$$
为验证该因子，固定选择的数目为 $O(X/X_\ell)$。对 $\ell = 1$，它至多是一个常数乘以 $(M/X_1)^{1/2} \ll (M/X_1)^{2/3}$ 与 $(M X_2/X_1)^{1/3} \leq M^{1/3}$ 两者；对 $\ell = 2$，它至多是一个常数乘以 $(M X_1^2/X_2^2)^{1/3} \leq M^{1/3} \ll (M/X_2)^{2/3}$。盒子的数目是 $\log(2 + M)$ 的固定幂次。

将式 (9.12) 代入式 (9.13) 得
$$
E_j(M, N) \ll_{S,\varepsilon} (MN)^\varepsilon (M^\alpha + M^{1/3} N).
$$
简化前的三项分别被 $M^\alpha$、$M^{1/3} N$ 和 $(MN)^{2/3}$ 控制；最后一项根据 $N \leq M$ 或 $N \geq M$ 被前两项之一控制。将此估计用于式 (9.8)。所有辅助的非空尺度都被 $2 + MN$ 的固定幂次控制：这里 $N/\Delta_d \geq 1/2$ 且 $H(N/\Delta_d) \ll_{S,\varepsilon} (2+MN)^{3+\varepsilon}$。单位列壳层直接满足同样的估计。因此可以选取更小的预备损失以给出任意指定的最终损失。两个尺度因子为
$$
\Delta_r^{\alpha-1} \Delta_d^{1-2\alpha} \ll_S \Delta_d^{-\alpha} \leq 1, \qquad (\Delta_r \Delta_d)^{-2/3} \leq 1.
$$
从而，对 $M, N \geq 1$，
$$
D_j(M, N) \leq E_j(M, N) \ll_{S,\varepsilon} (MN)^\varepsilon \{ M + N^{2\alpha-1} M^{1-\alpha} + (MN)^{2/3} \}. \tag{9.14}
$$
令 $h = 2 - 3/(3\alpha - 1) = (2\alpha - 5/3)/(\alpha - 1/3)$，$\beta = 2 - 2/(3\alpha - 1)$。若 $M \geq N^h$，则式 (9.14) 中的中间项至多为 $(MN)^{2/3}$。若 $M < N^h$，则以 $N^h \log(2MN)$ 的固定倍数代替 $M$ 应用式 (9.11)。式 (9.14) 在那里给出 $(MN)^\varepsilon N^\beta$，因为 $2(h + 1)/3 = \beta$ 且 $h < \beta$。因此在两种情形下
$$
D_j(M, N) \ll_{S,\varepsilon} (MN)^\varepsilon \{ M + N^\beta + (MN)^{2/3} \}.
$$
对称性给出将 $\alpha$ 换为 $\beta$ 的式 (9.12)，且对每个 $j \in J$ 同时成立。从 $2$ 出发，映射 $\alpha \mapsto 2 - 2/(3\alpha - 1)$ 递减至 $4/3$。对指定的损失，取有限多次迭代直到剩余的指数差小于该损失的固定分数，并将其吸收进 $(MN)^\varepsilon$。结合该界及其对称形式，当 $M \leq N$ 时利用 $M^{4/3} \leq (MN)^{2/3}$，当 $N \leq M$ 时利用类似的不等式，即证得
$$
D_j(M, N) \ll_{S,\varepsilon} (MN)^\varepsilon \{ M + N + (MN)^{2/3} \} \qquad (j \in J). \tag{9.15}
$$
对两个范数球作二进分割，并在列壳层上使用 Cauchy 不等式，将式 (9.15) 转化为球矩阵（其元素为 $F_b(a) = \chi_a(b)$）的同样界。对数因子被更小的预备损失吸收，而单位壳层直接被控制。$\varsigma = 1$ 时式 (9.1) 中的矩阵是此矩阵在长度 $(D, K)$ 处的转置。复矩阵与其转置具有相同的算子范数，这由伴随恒等式继以整向量共轭得到。该界在两个长度上对称，因此恰好给出 $K + D + (KD)^{2/3}$。对整个内和取共轭给出 $\varsigma = -1$，零点不变。最后，固定的行限制去掉非负项，固定的系数限制通过零延拓施加。这证明了引理的全部断言。
