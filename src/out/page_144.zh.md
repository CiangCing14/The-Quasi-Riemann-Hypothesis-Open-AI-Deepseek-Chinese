为实际存活的元组选取。该测度可能依赖于已经固定的 $j$，但
式 (17.20) 对其在固定乘积区间内的 $y_j$ 是一致的。对于这一个测度，在整个行 Hilbert 空间中使用了 Minkowski 不等式。在最终阈值被选定之前，将 $\omega_c$ 的完全支撑、其更大的截断、存活槽位的支撑以及 $j$-乘积区间包含进有限集合 ID 中。采用与规范证明相同的 $\eta$ 约定，我们于是有
$$|\hat{b}_c - D'| \le \eta, \qquad |\hat{b}_j - G| \le \eta$$
在实际于下文使用的完全支撑上成立，其中 $\hat{b}_c = \log_Z q_c$。对于符号 $\varepsilon_\chi = 1$，对整个剩余多项式取共轭，包括其有限特征、标记和测试；其行范数不变。对于另一个符号，保持其不变。因此只需估计一个具有精确形式的多项式
$$R_0(u) = Z^{-D'/2} \sum_{c \in \mathrm{sf}} \mu(c)\nu_0(c)\mathbf{1}_{(c,j)=1}\overline{\chi_c(u)}d_0(c)W_0(q_c/Z^{D'}). \tag{17.68}$$
这里 $\nu_0$ 是一个固定的有限射线特征，$d_0$ 是帽 $z_0$ 与那些个体系数或其共轭的乘积标记，而 $W_0$ 是 $\omega_c(y)y^{i\upsilon_c}$ 或其共轭。所有这些都与行无关。

用尺度为 $Z^m$ 的固定非负径向 Schwartz 函数 $\Phi_{\mathrm{init}}$ 控制原始行球，并展开其平方。设 $C$ 为两列的 gcd，记 $c_i = Cz_i$，其中 $z_1, z_2$ 无平方因子且互素。令 $\hat{b}_{c_i} = \log_Z q_{c_i}$，于是前述支撑界对每个 $i = 1, 2$ 成立。设 $B \ge 0$ 为 $C$ 的中心，并记 $\hat{B} = \log_Z q_C$。行特征具有本原模 $z_1 z_2$ 和剩余零掩码 $C$。应用引理 17.5，其中 $d' \mid C$。设 $\theta \ge 0$ 为其中心，$\hat{\theta} = \log_Z q_{d'}$。令
$$P_1 = B - \theta \ge -2\eta,$$
其中不等式由 $\hat{\theta} \le \hat{B}$ 和两个 $\eta$-比值界得出。实际导子长度为
$$\hat{L}_{\mathrm{init}} = \hat{b}_{c_1} + \hat{b}_{c_2} - 2\hat{B}, \qquad |\hat{L}_{\mathrm{init}} - 2(D' - B)| \le 4\eta.$$
对于正容差 $\tau_{\mathrm{init}}$，蕴含关系 $Z^m q_{h'}/(q_{d'} q_{z_1 z_2}) \le Z^{\tau_{\mathrm{init}}}$ 给出
$$d' h' \le 2D' - m - 2P_1 + 6\eta + \tau_{\mathrm{init}}.$$
定义固定的形式行尺度与包围行尺度
$$\mathcal{M}_{\mathrm{init}} = 2D' - m - 2P_1, \qquad M_{\mathrm{init}} = \mathcal{M}_{\mathrm{init}} + 6\eta + \tau_{\mathrm{init}}. \tag{17.69}$$
$6\eta$ 中的 $4\eta$ 来自导子，$2\eta$ 来自新行界中 $d'$ 的两个副本。

将原始主贡献分离出来，用于下面的直接计数。在真正的非主互素 Poisson 表达式上，在任何非互素扩张或 Fourier 绝对化之前，只保留外掩码
$$B_{\mathrm{init}}(h') = \mathbf{1}_{0 < q_{d'} h' \le Z^{M_{\mathrm{init}}}}.$$
对于每个受支撑对，其补集都包含在上面的实际比值尾部中。式 (17.21) 按下面指定的独立初始原始计数和阶数，恰好丢弃该补集。保留掩码内的完整光滑核，不使用依赖于列的比值选择器。掩码依赖于 $d'$、$h'$、固定的重叠与扇区，但不依赖于剩余列。若 $M_{\mathrm{init}} < 0$，其非零球为空，同一尾部比较丢弃每个非零频率；否则保留的行参数非负。

实际归一化与 Poisson 前因子按两侧分解为
$$Z^{-D'} Z^{m - \hat{\theta} - \hat{L}_{\mathrm{init}}/2} = Z^{\hat{\kappa}_{b_1}^{\mathrm{init}}/2} Z^{\hat{\kappa}_{b_2}^{\mathrm{init}}/2}, \qquad \hat{\kappa}_{b_i}^{\mathrm{init}} = m - D' - \hat{\theta} - \hat{b}_{c_i} + \hat{B}.$$

144
