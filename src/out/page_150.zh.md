这里把相异的冻结商计算一次，其见证重数已包含在纤维权重中。形式恒等式

$$\kappa^{\text{init}}_{c} + P_1 + 2F^{\text{init}}_{c} = m$$

在恢复子规范化并应用损失为 $\epsilon_c$ 的典范界之后，给出单侧指数

$$m + 3\eta + 2\eta + 2\delta_{\text{init}} + \pi_{\text{init}} + \epsilon_c \le m + 11\eta + \pi_{\text{init}} + \epsilon_c. \tag{17.86}$$

这里 $\pi_{\text{init}}$ 是合计的自由选择的局部除子、二进和分离损失，包括指定重叠除子损失和相异分配 $\pi_{\text{count,init}}$、$\pi_{\text{fib,init}}$。这些是一个合计量的各部分，不是重复的容许量。两个裁剪副本来自恢复的规范化和子指数。没有 $\tau_{\text{init}}$ 能量因子：行放大发生在典范子内部，并已在其边缘检验中计入。初始加权 Cauchy 取几何平均，重叠三角形已被 $Z^{-G}$ 抵消。

我们明确给出参数和尾阶。设 $r_{\max}$、$z_{\max}$、$m_{\max}$ 界定标记范围，设 $s_{\text{slot}}$ 界定槽数，并令 $D_{\max} = r_{\max} + z_{\max}$。置 $\bar c = \min(c_1, c_2)$ 并选择典范边缘 $c_{*} = \bar c/2$。对于 $\eta, \tau_{\text{init}} \le 1/100$，该应用有效的先验起始界为

$$M_{\max} = 2D_{\max} + 1, \qquad N_{\max} = V_{\max} = D_{\max} + 1.$$

确实，$P_1 \ge -2\eta$ 给出 $M_{\text{init}} \le 2D_{\max} + 10\eta + \tau_{\text{init}}$，而 $F_{\text{init}} \le D_{\max} + 5\eta$ 界定两个非负子参数。按方程 (17.66) 进行选择，取 $\epsilon_c = \epsilon/2$，并额外施加

$$\eta, \tau_{\text{init}} \le \bar c/100, \qquad \eta \le \epsilon/88, \qquad \pi_{\text{init}} \le \epsilon/8.$$

在施加这两组界之后，可以取 $\tau_{\text{init}} = \tau$。方程 (17.85) 随即给出两个边缘至少为 $3\bar c/4 > c_{*}$，因此引理 17.2 适用。方程 (17.86) 至多为其 $\epsilon_c = \epsilon/2$ 损失增加 $\epsilon/4$。

在这些有界初始范围固定之后，选择实现目标 $\pi_{\text{init}}$ 的辅助输入指数，然后再选择初始尾阶和 Fourier 高度阶。

对于单独的初始原始尾，被支撑的列满足 $q_{c_i} \le C_Z^{D_{\max}}$，而 $D' \in [-z_{\max}, D_{\max}]$。在真正的初始展开上置 $a = Z^{m}/(q_{d'} q_{z_1 z_2})$。由于 $m \ge 0$、$d' \mid C$ 且 $c_i = C z_i$，

$$a^{-1} \le q_{d'} q_{z_1 z_2} \le q_{c_1} q_{c_2}/q_C \le C_Z^{2D_{\max}}.$$

显式的粗略指数

$$B_{\text{crude,init}} = 10\{1 + m_{\max} + (s_{\text{slot}} + 1)(D_{\max} + 1)\}$$

即使没有抵消也界定所有原始非频率因子。为验证这一点，规范化至多耗费 $z_{\max}$，两个列计数耗费 $2D_{\max}$，$d'$-除子计数至多耗费 $D_{\max}$，而 $1 + a^{-1}$ 至多耗费 $2D_{\max}$。两个剩余标记至多耗费 $2s_{\text{slot}} D_{\max}$，利用 $d_{\mathcal{O}}(c)^{s_{\text{slot}}} \le q_c^{s_{\text{slot}}}$。即使计算重叠对及其指定系数而不计其抵消权重，也至多耗费 $2z_{\max} + 2s_{\text{slot}} z_{\max}$。Poisson 前因子至多耗费 $m_{\max}$。总和至多为 $m_{\max} + (8 + 4s_{\text{slot}})D_{\max} < B_{\text{crude,init}}$。

选择 $T_{\text{init}} > 1 + B_{\text{crude,init}}$，然后

$$A_{\text{init}} > 1 + (B_{\text{crude,init}} + T_{\text{init}})/\tau_{\text{init}}.$$

方程 (17.21) 使原始 $B_{\text{init}} = 0$ 补集为 $O(Z^{-T_{\text{init}}})$，具有固定的半范数和多项式高度因子。这个阶是在标记范围和 $\tau_{\text{init}}$ 之后选择的，但在初始 Fourier 高度阶之前，且在最终 $Z$ 阈值之前。如果 $\tau_{\text{init}} = \tau$，取以下的最大值
