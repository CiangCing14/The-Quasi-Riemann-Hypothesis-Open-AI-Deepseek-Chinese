设 $T_\Sigma^{\mathrm{init}}$ 为由式 (17.71) 经完整的 Möbius 展开与优先展开所得到的固定 $s$-二元组与槽位被加项。其精确分离恒等式为

$$T_\Sigma^{\mathrm{init}} = Z^{\kappa_{\mathrm{init}} + 3\eta} c^{-6} (2\pi)^{-6} \int_{\mathbb{R}^6} \hat{H}^{\mathrm{init}, \Sigma, \upsilon}(\xi) \times \sum_{\omega \in \Omega_\Sigma} V_\Sigma^{\mathrm{init}}(\omega; \xi) Q_{1,t,j,\xi}^{\mathrm{init}}(k, f) \overline{Q_{2,t,j,\xi}^{\mathrm{init}}(k, f)} \, d\xi. \tag{17.79}$$

事实上 $x_a = Z \delta_{\mathrm{init}} z n_a$。两个列模式，连同式 (17.78) 的最后一个因子，恰好是 $x_{i\xi_1} x_{i\xi_2}$，另外四个模式是外部的。Fourier 反演恢复完整剖面；其较大的截断在保留支集上为一，而新的列截断在旧 $W_0$ 窗口非零处为一。式 (17.75) 恢复完整的前因子与核。式 (17.72) 与优先展开逐项恢复每一个算术因子项。完整新窗口中的额外组合在此复恒等式中通过旧窗口在 Cauchy 之前相互抵消。

式 (17.79) 中的变换是在任何实际的 $C, d', s, h'$，从而在任何 $t, k, f$ 被求值之前，从固定的环境剖面中选取的。它依赖于 $\Sigma$、$Z$、固定的测试函数以及先前的模式 $\upsilon$，并且可能依赖于已经冻结的 $j$，但不依赖于任何当前的外部理想、重索引行或标号。裸的 $h'$ 范数是一个坐标；导出的行与标号只出现在外部掩码或所显示的字符中。关系 $C = td'$ 只限制求值点。由式 (17.20)，对每个固定的 $J$ 存在固定的 $L, b_0$ 使得

$$\int_{\mathbb{R}^6} |\hat{H}^{\mathrm{init}, \Sigma, \upsilon}(\xi)| (1 + |\xi|)^J \, d\xi \ll (1 + |\upsilon|)^L, \quad \int_{\mathbb{R}^{1+|I_0|}} |\hat{H}^{\mathrm{ov}, j}(\upsilon)| (1 + |\upsilon|)^L \, d\upsilon \ll p_{b_0}(W).$$

第一个界使用了固定的归一化根以及完整核对于每个正的 $A_{\mathrm{ker}, \mathrm{init}}$ 的一致 Euler 界；$W_0$ 只具有多项式 $\upsilon$ 依赖性。第二个界在固定的 $j$-乘积区间上一致成立。必要时取更大的 $L$ 也能控制先前的行空间 Minkowski 不等式。任何导数阶都不引入 $Z$ 的幂次。

式 (17.79) 现在将分量表示为具有标准形状的多项式，其中有一个在当前外部理想被求值之前就已选定的公共 Fourier 密度。剩下的工作是界定正纤维与源测度、从源见证验证子可达性，并在引理 17.1 中恢复归一化。

在固定一个 $t$ 用于子项之前，先在整个 $\Omega_\Sigma$ 上，包括所有商 $t$，应用式 (D)。只有在此之后才取绝对权重。保留的 $(s, C) = 1$ 与 $d' \mid C$ 使 $f = d' s$ 无平方因子，而权重的所有其他因子都被一个固定常数界定。于是

$$|V_\Sigma^{\mathrm{init}}(\omega; \xi)| \ll B_{\mathrm{init}}(h') \mu^2(f).$$

对固定的 $t, f, k$，恒等式

$$d' \mid f, \quad s = f/d', \quad C = td', \quad h' = k/d' \quad \text{若此商为元素}$$

表明重构在槽位之前至多有 $d_O(f)$ 种选择。这里 $K_{\mathrm{slot}}$ 仍表示原始槽位数目的固定界。至多 $2K_{\mathrm{slot}}$ 个被分配的剩余素数整除 $tf$。它们的选择至多耗费 $[d_O(t) d_O(f)]^{2K_{\mathrm{slot}}}$。先前的重叠素数已经被冻结并在重叠三角形中计数。因此，纤维即使其实际大小依赖于 $k$，也被界定为

$$D_{\mathrm{init}}(f) C_{\mathrm{init}}(t), \quad D_{\mathrm{init}}(f) = d_O(f)^{1 + 2K_{\mathrm{slot}}}, \quad C_{\mathrm{init}}(t) = d_O(t)^{2K_{\mathrm{slot}}}. \tag{17.80}$$

不存在独立的 $d', s$ 计数，也不存在第二个频率计数。

设 $\Omega_\Sigma^{\mathrm{src}}$ 为刚刚使用的结构外部集合，在独立的正行或标号添加之前，并忽略单位 Fourier 相位，定义不同源商的集合

$$T_\Sigma = \{t = C/d' : \omega \in \Omega_\Sigma^{\mathrm{src}}\}.$$
