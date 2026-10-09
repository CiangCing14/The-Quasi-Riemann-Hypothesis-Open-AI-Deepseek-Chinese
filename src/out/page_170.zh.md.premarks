多项式范数的。对每个固定的 $\Pi$，乘性将其值、掩码和范数幂在 $\Pi_{l_1 l_2}$ 上分解为 $\Pi$ 中的一个标量乘以结论中所述的三个因子。这证明了例外断言。

接下来我们记录两个剩余卷积的精确归一化。置
$$\alpha_1 = a_0 - c_2, \qquad \alpha_2 = a_0 - d_2, \qquad \frac{\alpha_1 + \alpha_2}{2} = a_0 - b_2.$$
在当前双变换阶段的入口处，设 $I_{\mathrm{in}}$ 为其活跃槽集合，$X_1, X_2$ 为其第一矩形的形式尺度。它们的精确约定为 $X_1 X_2 \prod_{i \in I_{\mathrm{in}}} P_i = Z^A$。对于侧 $j \in \{1, 2\}$，设 $F_j$ 为从该入口集合中被第一次和第二次真正的共同支撑提取所冻结的槽，设 $I_j$ 为在最终 $t$-分配之前仍活跃的槽，设 $Q_{\mathrm{plain},j}$ 为在这些步骤和放大器中提取的普通幂的精确范数之积。在祖先阶段被移除的槽不包含在 $F_j$ 中。设 $T_j$ 为其矩形中两个普通尺度的共同形式 pre-$t$ 乘积；对于非中心化输入，使用其一个形式普通乘积。在使用槽比值之前，丢弃一个冻结槽零剖面项，该项由其冻结数据恒为零，与行标和活跃标号无关。完全提取给出精确恒等式
$$Z^{A - \alpha_j} = Q_{\mathrm{plain},j} \prod_{i \in F_j} q_{p_i},$$
$$T_j \prod_{i \in I_j} P_i = \frac{Z^A}{Q_{\mathrm{plain},j} \prod_{i \in F_j} P_i} = Z^{\alpha_j + e_j},$$
$$e_j = \sum_{i \in F_j} \log_Z (q_{p_i} / P_i), \qquad |e_j| \leq \theta_N.$$

放大器对此计算只贡献精确的普通幂。每个较早的冻结槽只出现一次，即使它与某个普通槽共享其素因子。已经分离的逆根、核和固定归一化常数保持在 $e_j$ 之外。

对于侧 $j$，设 $d_{j,i}$ 为在普通 $i$ 中选择的最终 $t$-素数之积，设 $J_j \subseteq I_j$ 为新冻结的槽。置
$$a_{j,i} = \log_Z q_{d_{j,i}}, \qquad \widetilde{e}_j = a_{j,1} + a_{j,2} + \sum_{i \in J_j} z_i \geq 0, \qquad \omega_j = \sum_{i \in J_j} \log_Z (q_{p_i} / P_i).$$

相应的形式尺度在两个矩形中均除以 $q_{d_{j,i}}$。一个分配若在两个不同的 $t$-素数处选择同一个素数槽，或选择一个剖面值为零的新冻结槽，则由冻结数据恒为零，在这些比值界被使用之前即被丢弃。所有其他被提取的零保持到下文所述的非负估计或绝对估计为止。

使用下端点为除数的二进区间 $T \leq q_t < 2T$，$T \geq 1$，并置 $t_- := \log_Z T$。每个二进区间包含 $O(Z^{t_-})$ 个理想。侧 $j$ 上实际选定的乘积可被 $t$ 整除，故
$$\widetilde{e}_j + \omega_j = \log_Z \left( q_{d_{j,1} d_{j,2}} \prod_{i \in J_j} q_{p_i} \right) \geq \log_Z q_t \geq t_-, \tag{18.34}$$
$$|\omega_j| \leq \theta_N, \qquad |e_j + \omega_j| \leq \theta_N \qquad (j = 1, 2).$$

最后一个不等式利用了当前阶段入口槽的不相交子集 $F_j$ 和 $J_j$。它不包含祖先槽或固定的分离常数。

记 $T_j' = T_j / q_{d_{j,1} d_{j,2}}$，则后形式因子乘积和标称原始子尺度为
$$T_j' \prod_{i \in I_j \setminus J_j} P_i = Z^{\alpha_j + e_j - \widetilde{e}_j}, \qquad N_{\mathrm{post},j} = Z^{\alpha_j - \widetilde{e}_j}. \tag{18.35}$$
