第二 Cauchy 不等式与外层计数。对第二个变换后的和式应用公式 (D)，在每个固定的 Fourier 模式上，取 $U_a = Z^{(\lambda_c + 18\eta + \tau)/2} Q_{a,\gamma,\zeta}$ 作用于完备集 $\Xi_\sigma$ 上。特别地，$B_2$、$|B_o|^2$、$|D_o|^2$ 以及 $\mathbf{1}_{(v', g' CJ) = 1}$ 仍在其权重中。它们保持上述已证的 $f_{\text{new}}$ 的无平方因子性。权重中所有其他因子都被一个固定常数所界定，包括有界的原始指派槽系数数目、固定的射线系数、各个截断以及单位模式。因此，仅在 Cauchy 之后，绝对权重满足

$$|V_\sigma(\xi; \zeta)| \ll B_2(k'')\mu^2(f_{\text{new}}).$$

这一步使得新的平均理想能够保持在无平方因子类中。

我们首先记录支配一个纤维所需的精确重构。

$$d_k \mid C B / R_1 \implies d_k \mid f_{\text{new}} \operatorname{rad} q_0. \tag{17.59}$$

为证明这一点，$B/R_1$ 的一个素数有 $t_p = 0$。局部表显示它具有偶宇称且 $a_{ip}$ 相等。若两者均为 1 则它属于 $J_2$，若两者均为 0 则它属于 $\operatorname{rad} q_0$。$C$ 的素数已经在 $f_{\text{new}}$ 中。这就证明了该蕴含关系。因此，在指定 $f_{\text{new}}$、$q_0$ 之后 $d_k$ 也具有除子重数。一旦这些因子固定，$k''$ 就由元素 $k_{\text{new}} = d_k d_2 k''$ 唯一确定。

设 $K_{\text{slot}}$ 界定原始槽数。在固定 $\gamma = (q_0, t', r_g)$、无平方因子 $f = f_{\text{new}}$ 以及元素 $k = k_{\text{new}}$ 时，权重非零的 $\xi \in \Xi_\sigma$ 的数目至多为一个固定常数乘以 $D_{K_{\text{slot}}}(f) C_{K_{\text{slot}}}(\gamma)$，其中

$$D_{K_{\text{slot}}}(f) = d_{\mathcal{O}}(f)^{9 + 4K_{\text{slot}}}, \tag{17.60}$$

$$C_{K_{\text{slot}}}(\gamma) = d_{\mathcal{O}}(q_0)^{5 + 2K_{\text{slot}}} d_{\mathcal{O}}(t')^{2K_{\text{slot}}} d_{\mathcal{O}}(r_g)^{2K_{\text{slot}}},$$

这里及以下 $d_{\mathcal{O}}$ 表示理想除子计数。为完备起见，将 $f$ 有序分配为 $J$、$C$、$d_2$、$v'$ 的代价为 $4^{\omega(f)} = d_{\mathcal{O}}(f)^2$，而拆分 $J = s J_2$ 的代价至多为 $d_{\mathcal{O}}(f)$。满足 $b_1 b_2 = q_0^2 J_2^2 s$ 的 $b_1, b_2$ 的选择代价至多为 $d_{\mathcal{O}}(q_0)^2 d_{\mathcal{O}}(f)^3$；两个选择 $A_a \mid \operatorname{rad}(b_1 b_2)$ 的代价至多为 $d_{\mathcal{O}}(q_0)^2 d_{\mathcal{O}}(f)^2$。这些估计使用了 $d_{\mathcal{O}}(IJ) \leq d_{\mathcal{O}}(I) d_{\mathcal{O}}(J)$ 和 $d_{\mathcal{O}}(I^2) \leq d_{\mathcal{O}}(I)^2$。方程 (17.59) 为 $d_k$ 带来的选择代价至多为 $d_{\mathcal{O}}(q_0) d_{\mathcal{O}}(f)$。然后 $g' = d_2 r_g$ 固定，且若 $k'' = k/(d_k d_2)$ 为整元素则它是唯一的。至多 $2K_{\text{slot}}$ 个旧指派素数整除 $q_0 f t'$，因此它们的选择代价至多为 $[d_{\mathcal{O}}(q_0) d_{\mathcal{O}}(f) d_{\mathcal{O}}(t')]^{2K_{\text{slot}}}$。至多 $2K_{\text{slot}}$ 个新指派素数整除 $f r_g$，代价至多为 $[d_{\mathcal{O}}(f) d_{\mathcal{O}}(r_g)]^{2K_{\text{slot}}}$。第一侧其余存活的槽在选择第一个正侧时消失；被选中的存活槽在其新的平方中出现两次，恰如这里所计。因此，即使其实际大小依赖于 $k$，所展示的乘积仍支配该纤维。这里没有对旧 $f, h$ 的计数，没有对 $J$、$C$、$d_2$、$v'$ 的独立计数，也没有第二次频率计数。

方程 (17.34) 及同样的源见证将 $\Gamma_\sigma$ 置于三个范数球的乘积之内

$$q q_0 \leq Z^{\ell + R/2 - j + 5\eta/2}, \quad q t' \leq Z^{t + \eta}, \quad q r_g \leq Z^{g - \theta + 2\eta}.$$

我们使用这些球仅仅是为了界定不同三元组的数目，而非作为子估计的替换区域。理想计数给出

$$\#\Gamma_\sigma \leq C_Z C_c + 11\eta/2 + \pi_{\text{count}}, \quad C_c = \ell + R/2 - j + t + g - \theta. \tag{17.61}$$

这里 $\pi_{\text{count}}$ 是单独选定的聚合 $\pi$ 的一部分。在非空扇区中，这三个球的每个上指数均非负，因为它界定了某个存在理想的范数；因此理想计数中的常数项不添加边界幂。特别地，$J$ 在此处不被计数。三个理想的范围都是有界的，因此可调除子界一致地给出 $C_{K_{\text{slot}}}(\gamma) \ll Z^{\pi_{\text{fib}}}$ 在包含球上。置 $c_\sigma = C_c + 11\eta/2$，并引入真正与行和标号无关的测度

$$d\nu_\sigma(\gamma) = Z^{-c_\sigma} \sum_{\gamma \in \Gamma_\sigma} C_{K_{\text{slot}}}(\gamma) \delta_\gamma, \quad \|\nu_\sigma\| \ll Z^{\pi_{\text{count}} + \pi_{\text{fib}}}. \tag{17.62}$$

139
