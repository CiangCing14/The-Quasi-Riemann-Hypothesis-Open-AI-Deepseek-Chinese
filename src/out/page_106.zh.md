实际残差范数落在 $N$ 的固定倍数中；名义值 $N$ 允许小于 1。固定任意 $A > 2$ 与 $B > 2$。对每个固定的 $C, d, k$，两列所对应的唯一联合环形剖面 $W_R$ 具有有限多个齐次单剖面半范数，其在下文中所用到的界为 $O_{B,J_{\mathrm{Gr}}}((1 + |\nu|)^{J_{\mathrm{Gr}}} R^{-B})$，其中 $J_{\mathrm{Gr}}$ 在这些导数阶数以及 $A, B$ 选定之后固定。这由对第一个 Fourier 核求导得到，其 Schwartz 衰减吸收由此产生的每一个 $R$ 的幂；范数幂的导数只付出 $1 + |\nu|$ 的固定幂。这个因子 $R^{-B}$ 保留在单剖面 Fourier 估计中，并在下文的线性格和中出现一次；不使用任何小的非齐次多元组半范数。

设 $a_{C,d,k}$ 为该周期算术系数。对非例外频率，其归一化完全 Fourier 变换（对两个剩余变量取归一化 $Q^{-2}$）的绝对值至多为 $q_C$，并在 $(0,0)$ 处为零。由于 $\mathcal{O}$ 的每个理想都是主理想，周期格具有线性尺度 $Q^{1/2}$。因此四维格 Poisson 求和给出，对此 $A$，

$$\sum_{m \in \mathcal{O}^2} a_{C,d,k}(m) W_R(m/\sqrt{N}) \ll (1 + |\nu|)^{J_{\mathrm{Gr}}} R^{-B} q_C N^2 \min\{1, (Q/N)^A\}. \tag{15.5}$$

对 $N \geq Q$，零频率为零，而其他对偶向量具有线性尺度 $(N/Q)^{1/2}$。阶为 $2A > 4$ 的 Fourier 衰减将其和界为 $(Q/N)^A$。对 $N < Q$，使用两个环形区域中的点数估计。非空的次单位环形区域其 $N$ 有固定的正常数下界，因此它仍包含 $O(N)$ 个格点；低于该常数时它是空的。这就证明了式 (15.5)，且无需对 $a_{C,d,k}$ 作任何本原性或张量积假设。

令 $K_R = R^{P_a}/C_0$。固定的壳层比较常数给出 $q_k^{-1} \leq C_{\mathrm{sh}} K_R$，其中 $C_{\mathrm{sh}} > 0$ 固定。因此当 $K_R < C_{\mathrm{sh}}^{-1}$ 时非零频率范围为空。在非空范围上，初等格点计数给出

$$\#\{k : 0 < q_k \leq C_{\mathrm{sh}} K_R\} \ll_{\mathrm{fixed}} K_R + \sqrt{K_R} + 1 \ll_{\mathrm{fixed}} K_R.$$

因此在这些二进块上有 $O(C_0 D_0 K_R)$ 个 $C, d, k$ 的选择。将式 (15.5) 乘以该计数以及公共前因子，至多得到

$$(1 + |\nu|)^{J_{\mathrm{Gr}}} R^{-B} \frac{Q}{Y'} \frac{R^{P_a}}{C_0 D_0} \min\left\{1, \left(\frac{R^{P_a} C_0 D_0}{Y'}\right)^A\right\}.$$

对 $\Lambda = Y'/(R^{P_a})$，所需的正式二进和为

$$\sum_{i,j \geq 0} 2^{-i-j} \min\{1, (2^{i+j}/\Lambda)^A\} = \sum_{n \geq 0} (n+1) 2^{-n} \min\{1, (2^n/\Lambda)^A\} \ll_A \frac{1 + \log(2 + \Lambda)}{\Lambda}.$$

对 $\Lambda \geq 1$，在 $2^n \asymp \Lambda$ 处将两个几何尾部拆开；对 $\Lambda < 1$，左端有界而所显示的右端大于某个正常数。因此，在选取固定的 $B > 2$ 并对 $R$ 求和之后，非例外频率的贡献为

$$\ll (1 + |\nu|)^{J_{\mathrm{Gr}}} \frac{Q}{Y'} \frac{P_a^2}{Y'} Z^\epsilon.$$

剩下要计数的是例外的非零频率。它们满足 $(k) = a_6^6 e$，其中 $e$ 无六次幂因子，且支集在 $C$ 的素因子与固定支集上。至多有 $6^{\omega(C) + O_S(1)} \ll_\epsilon q_C^\epsilon$ 个可能的 $e$。对其中每个，壳层界 $q_k \leq C_{\mathrm{sh}} K_R$ 只允许 $q_a \leq (C_{\mathrm{sh}} K_R / q_e)^{1/6}$。若该范围非空，其上界至少为 1，理想计数给出 $O_{\mathrm{fixed}}(K_R^{1/6})$ 个选择；若 $q_e > C_{\mathrm{sh}} K_R$ 则为空。单位因子只付出一个固定因子。因此有 $O_\epsilon(K_R^{1/6} q_C^\epsilon)$ 个这样的元素 $k$，其中包括 $K_R$ 的有界次单位范围。

使用 $K_R = R^{P_a}/C_0$、$|L_C| \leq q_C$ 以及平凡的两列点数估计。在乘以 $Q/Y'^3$ 之前，这些二进块上的贡献为

$$\ll (1 + |\nu|)^{J_{\mathrm{Gr}}} R^{-B} Z^\epsilon Y'^2 (R^{P_a})^{1/6} C_0^{-1/6} D_0^{-1}.$$

106
