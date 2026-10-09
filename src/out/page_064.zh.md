如果截断低于 1，同样的界仍然成立。取 $A$ 充分大，就得到任意负幂次的误差。

在剩余的求和中，写 $a = a_0 s$，其中 $a_0$ 是好的，$s$ 的支集在 $S$ 上，并对每个固定的 $s$ 选取一个生成元 $s_0$。方程 (9.3) 和 (9.4) 给出分离的因子
$$\Psi_{b,c}^{(j)}(a_0 s) = F_b(a_0)^j F_c(a_0)^j \chi_b(s_0)^j \chi_c(s_0)^j.$$
所有 $\chi_b(s_0)$ 的模均为 1。将 $a_0$ 分成壳层 $a_0 \in I_H$，其中 $H \ll ZN^2/(M q_s)$，并在 $\Re w = \delta$ 上对 $W$ 插入 Mellin 反演。除一个依赖于 $M, q_{a_0}, q_s$ 的有界因子外，两个系数序列为
$$A_b = \lambda_b \gamma_j(b) \chi_b(s_0)^j q_b^{-1/2+\delta+it}, \quad B_b = \lambda_b \gamma_{-j}(b) \chi_b(s_0)^j q_b^{-1/2+\delta+it}.$$
它们在 $a_0$ 求和过程中是固定的，且绝对值 $\ll N^{-1/2+\delta} |\lambda_b|$。用 Möbius 反演检测 $(b,c)=1$，并在 $a_0$ 上应用 Cauchy 得
$$\sum_{a_0 \in I_H} \sum_{\substack{b,c \in A_N \\ (b,c)=1}} A_b B_c F_b(a_0)^j F_c(a_0)^j$$
$$\leq E_j(H,N) \left(\sum_d \sum_{d|b} |A_b|^2\right)^{1/2} \left(\sum_d \sum_{d|b} |B_b|^2\right)^{1/2} \ll N^{-1+3\delta} E_j(H,N).$$
这里除数界吸收了关于 $d$ 的求和。对整个第一个多项式取共轭用同样的 $E_j$ 范数。$H < 1$ 的因子只有单位赋值理想，且满足 $E_j(H,N) \ll N$。$s$ 和二元壳层只有固定幂次个 $\log(2+ZN^2)$ 种选择，因为 $S$ 是固定的且非零的 $Q_j$ 有下界 $M$。方程 (9.5) 对 $t$ 变量积分。选择 $\delta$ 关于 $\varepsilon$ 充分小即证明方程 (9.7)，包括其 $M$ 项上允许的整体损失。

现在我们将这一配对估计应用于 $E_j$。按 $t$ 划分其内和，插入 $W$，并展开平方。将两个无平方因子指标写为 $db, dc$，其中 $d$ 是它们的 gcd，$(b,c)=1$，且 $(d,bc)=1$。它们的剩余类一致，因为 $t$ 是乘性的。指标乘性和方程 (9.3) 在每个好的 $a$ 上给出
$$F_{db}(a)^j F_{dc}(a)^j = 1_{(a,d)=1} \Psi_{b,c}^{(j)}(a).$$
令 $s_S = \prod_{p \in S} p$。对 $(a, s_S d) = 1$ 的 Möbius 反演写为 $a = ra$，其中 $r | s_S d$。对每个固定的 $r$ 选取一个生成元 $r_0$。$\Psi$ 在 $r$ 处的值分离为 $\chi_b(r_0)^j \chi_c(r_0)^j$，因此公共剩余序列为
$$\lambda'_b = \lambda_{db} 1_{(b,d)=1} \chi_b(r_0)^j, \quad |\lambda'_b| \leq |\lambda_{db}|.$$
它支撑在 $A_{N/qd}$ 的一个类上。以长度 $M/qr$ 和 $N/qd$ 应用方程 (9.7)。求和系数质量至多为
$$\sum_d \sum_{r|s_S d} \sum_b |\lambda_{db}|^2 \leq d^{O(s_S)} \sum_m d^{O(m)^2} |\lambda_m|^2 \ll_{S,\delta} (2+N)^\delta \|\lambda\|_2^2.$$
记 $\Delta_r = qr$，$\Delta_d = qd$，我们有 $1 \leq \Delta_d \leq 2N$ 和 $1 \leq \Delta_r \leq q_{s_S} \Delta_d$。我们得到递推界面
$$E_j(M,N) \ll_{S,\varepsilon} (2+MN)^\varepsilon \max_{\substack{1 \leq \Delta_d \leq 2N \\ 1 \leq \Delta_r \leq q_{s_S} \Delta_d}} \left\{ \frac{M}{\Delta_r} \right.$$
$$\left. + \frac{M \Delta_d}{N \Delta_r} \max_{\substack{1 \leq H \\ H \ll_{S,\varepsilon} (2+MN)^\varepsilon N^2 \Delta_r^2 / (M \Delta_d)}} E_j(H, N/\Delta_d) \right\}. \quad (9.8)$$

64
