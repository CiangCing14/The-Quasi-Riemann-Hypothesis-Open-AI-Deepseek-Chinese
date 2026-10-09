正典范子节点。对于固定的 Fourier 模，定义正子节点和
$$H_{a,\gamma} = \sum_{\substack{f\, s_f \\ q_f/Z^{V_c} \in I_f}} D_{K_{\text{slot}}}(f) \sum_{\substack{k \in \mathcal{O} \\ 0 < q_k \le Z^{M_{\text{ch}}}}} |Q_{a,\gamma,\zeta}(k, f)|^2 = Z^{F_{\text{ch}}} E_{a,\gamma}. \tag{17.63}$$

该等式是式 (17.3) 在同一行球、标号权重 $D_{K_{\text{slot}}}$、以及式 (17.55) 和 (17.44) 中的检验与穿刺下的归一化；若此处使用更大的固定行球，则该等式改为所需上界方向的不等式。权重仅依赖于 $f$。重新编号后，$B_2$ 恰好就是所显示的行球。只有如今为正的外行和与标号求和被放大到其完整的固定窗口。列使用其完整的固定新鲜窗口，但它们的穿刺、标记和检验未被删除或改变。刚刚证明的实际纤维支配给出
$$\sum_{\xi \in \Xi_\sigma} V_\sigma Q_1 Q_2 \le \left( \prod_{a=1}^{2} \sum_{\xi \in \Xi_\sigma} |V_\sigma| |Q_a|^2 \right)^{1/2} \ll Z^{c_\sigma} \left( \prod_{a=1}^{2} \int_{\Gamma_\sigma} H_{a,\gamma} \, d\nu_\sigma(\gamma) \right)^{1/2}.$$


这里 $Q_a = Q_{a,\gamma,\zeta}(k_{\text{new}}, f_{\text{new}})$。两个平方根各提供 $Z^{c_\sigma/2}$，因此有一个固定计数因子。一致子节点界提供一份总质量 $\|\nu_\sigma\|$，而非其平方。子节点界将仅对 $\gamma \in \Gamma_\sigma$ 使用，利用式 (17.51) 中已验证的假设。

能量指数。形式中心满足精确恒等式

$$\kappa_i + \lambda_c + C_c + 2F_c = F. \tag{17.64}$$

这通过代入它们的定义以及 $H_c = 2r - 2B - M + 4\ell + 2V + \delta - j$ 得到；所有提取出的长度相消，结果为 $r + 3\ell + V = N + V$。
    我们现在仅对 $\gamma \in \Gamma_\sigma$ 使用子节点估计，因为前文的余量和行递减已对该情形得证。若它在该处一致地给出 $E_{a,\gamma} \ll C(t,\zeta)Z^{F_{\text{ch}}+\epsilon_{\text{child}}}$，并带有其固定的多项式高度依赖，则式 (17.63) 和上述最终的加权 Cauchy 界给出
$$\sum_{\xi \in \Xi_\sigma} V_\sigma Q_1 Q_2 \ll C(t,\zeta)Z^{c_\sigma+2F_{\text{ch}}+\epsilon_{\text{child}}}\|\nu_\sigma\|.$$

归一化质量即式 (17.62) 中的那个；见证重数已包含在其纤维权重中。公共 Fourier 密度随后利用式 (17.58) 积分一次。它不属于离散测度的一部分，也不对任何行或标号重新选取。因此真正的外计数及其归一化质量各出现一次。平均后的 $J$、$C$、$d_2$、$v'$ 留在正子节点和内部，不被重复计数。
    若一个子节点被 $Z^{F_{\text{ch}}+\epsilon_{\text{child}}}$ 界定，则第一个前因子误差、第二个前因子误差、固定计数以及恢复的归一化在每个正的第二次 Cauchy 侧给出

$$\begin{aligned} \kappa_i + \lambda_c + C_c + 2F_{\text{ch}} + \left(\frac{9}{2} + 18 + \frac{11}{2}\right)\eta + \tau + \pi + \epsilon_{\text{child}} &= F + 28\eta + 2\delta_N + \tau + \pi + \epsilon_{\text{child}} \\ &\le F + 40\eta + \tau + \pi + \epsilon_{\text{child}}. \end{aligned} \tag{17.65}$$

两份 $\delta_N$ 都出现：一份恢复子节点列归一化，另一份出现在其所断言的指数中。两个加权 Cauchy 不等式各取其正侧的几何平均，因此不会使这一损失加倍。第一个主界为 $Z^{M+\pi}$，上述第二个主界至多为 $Z^{F+26\eta+\tau+\pi}$；二者都符合同一容许量。

                                                     140
