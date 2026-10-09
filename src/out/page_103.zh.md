分离损失全部至多为一个小的 $\epsilon_0 > 0$。在固定行部分求和之后，我们使用指数 $E_{\mathrm{ref}}$；它们的计数已包含在 $E_{\mathrm{ref}} + \epsilon_0$ 中，主指数为 $O/2$，不再重复计数。

这里 $f = 1$，且穿刺点为 $\rho = 1$，因此唯一移动的非槽位素数是该行的那些素数。在引理 14.3 中的有限单位与反射扇区分裂之后，冻结其范数长度为 $O$ 的强部分及其支撑在 $S$ 上的赋值一部分，并将其剩余的平方自由好乘积分裂为范数 $\asymp Z H$ 的实际二元组。设 $\epsilon_Z = O_{\mathrm{fixed}}(1/\log Z)$ 为非负且足够大，以包含此计算中所有固定的环状与固定导子对数偏移。则
$$H \leq M' - O + \epsilon_Z, \quad \Delta H = M' - O - H \geq -\epsilon_Z, \quad O \geq -\epsilon_Z.$$
实际的行与对偶环状截断保持在同一个联合剖面中，而其公共 Fourier 密度被分离出来。小核振幅在该齐次密度中、行范数平方之前被提取出来，只有在此之后才可以扩大正筛和，如式 (5.24) 那样。特别地，式 (14.14) 中的核节省使用这个 $H$；它不会在任何由正扩大添加的更短行上重新求值。

在那个能量估计的记号中，$A_0$ 中计数的每个移动非槽位素数都以至少二次的指数整除强行部分。因此，将其精确范数与强二元组以及任何固定导子贡献相比较，得到
$$2A_0 \leq O + \epsilon_Z, \quad N_0 \leq A_0, \quad z_a \leq \ell'.$$
在实际完成尺度上可用的对偶长度为
$$T_d = 2H + 2A_0 + 2z_a - 1 - \ell' - \theta_N - N_0 - 3B_0.$$
由于 $M' + \ell' - 1 = -3d$，直接相减给出
$$T_d - (H - 3d) = H - M' + 2A_0 + 2(z_a - \ell') - N_0 - 3B_0 - \theta_N \leq 2\epsilon_Z + |\theta_N|.$$
如同反射能量的证明中那样，低于某个固定负长度的对偶范围在正的 Mellin 平移之后可以忽略，而有界边界范围只付出任意小的幂次代价。这些二元组中的源对偶理想 $n, b$ 保持式 (5.2) 的支撑：它们可以共享素数，并且可以包含 $S$ 的允许素数；$n$ 与 $b$ 之间没有额外的 $S$-掩码或互素条件。在每个剩余的对偶二元组上，置 $y = v + 3\ell_b + e_\lambda$。保留性给出 $y \leq T_d + \epsilon_0$，而非零单位范围在增大其固定常数之后给出 $v, \ell_b, e_\lambda \geq -\epsilon_Z$。于是有
$$\max(H, v + \ell_b) = H + O(\epsilon_0 + \kappa_G + \epsilon_Z).$$
记 $\mathrm{shyb} = \min\{v, z_a, (v + z_a)/3\}$ 为式 (14.13) 中称为 $u$ 的量。若 $\mathrm{shyb} = z_a$，则 $-S_0 - B_0 + z_a - \mathrm{shyb} \leq 0$，核项非正，且
$$-\ell_b - \frac{2e_\lambda}{3} + \frac{5}{3} \leq \epsilon_Z.$$
这里单独的 $O$ 是强行对数长度。于是有
$$E_{\mathrm{ref}} \leq O/2 + H + O(\epsilon_0 + \kappa_G + \epsilon_Z) = M' - O/2 - \Delta H + O(\epsilon_0 + \kappa_G + \epsilon_Z).$$
否则 $\mathrm{shyb} \geq v/2 - O(\epsilon_Z)$，而有界单位范围蕴含
$$\mathrm{shyb} + \ell_b + \frac{2e_\lambda (T_d - y)_+}{3} + \frac{y (T_d - y)_+}{2} \geq \frac{y}{4} + \frac{(T_d - y)_+}{2} - O(\epsilon_Z) \geq \frac{T_d}{4} - O(\epsilon_Z).$$
