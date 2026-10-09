这个剖面之外的标量恰好是 $\prod_{a=1}^{2} Z^{(\kappa_a + 9\eta/2)/2}$。特别地，该剖面
包含每个实根一次，即使实际的列范数不同亦然。其变换由环境九维盒子上的
方程 (17.19) 定义，在任何实际的 $f$、$h$ 或外理想被求和之前。$b_a$、$f$、$J$、$E$、$q_0$ 的范数
仅出现在方程 (C) 之后的外系数、特征、掩码或各个截断中；它们不需要额外的耦合剖面坐标。

    为在 $t'$ 处展示算术提取，令 $y = hf^2 E$ 并令

$$B_{1,a}(t'; y) = \mu(t')\nu_a(t')\rho(t')\overline{\chi_{t'}(y)}\chi_{t'}(CJ)^4 \chi_{t'}(d_k) 1_{(t', \text{rad}\,q_0)=1}.$$

令 $\varepsilon_1 = 1$ 且 $\varepsilon_2 = -1$。对于固定的第一傅里叶模式 $t$，其余多项式恰好为
$$\begin{aligned} P_a(y) &= \sum_{x\ \text{sf}} \mu(x)\nu_a(x)\rho(x)\overline{\chi_x(y)}\chi_x(CJ)^4 \chi_x(d_k) 1_{(x, \text{rad}\,q_0 t')=1} \\ &\quad \times d I_a(x)\,\omega_{x,a}\,(q_x/Z^{s_a})(q_x/Z^{s_a})^{\varepsilon_a i t x_a}. \end{aligned} \tag{17.30}$$

乘法性用于无平方因子互素因子，然后通过所展示的零延拓；在任何零点处不除以特征。
来自互gcd反演的那一个额外 $\mu(t')$ 是外的。
将方程 (17.16) 应用于有序列表 $(b_a, A_a, C, t'; x)$。整除 $x$ 的幸存素数已经与 $b_a, A_a, C, t'$ 互素：
$B$ 的每个素数都在 $J\,\text{rad}\,q_0$ 中，且所展示的四次幂和穿孔提供了这些零点。因此 $d I_a$ 具有
原始的个体系数和列表，而指派的素数身份与优先掩码保持在外。
    以下是第一分离分量的完整结构。设 $\Omega_\sigma$ 由
$b_1, b_2, A_1, A_2, C, d_k, t', f, h$ 以及指派的槽素数组成，受其重构关系
和个体支撑约束。特别地 $A_a \mid B$，$(C,B)=1$，且 $d_k \mid CB/R_1$，而
$R_1, E, J, q_0$ 是导出的，不是自由指标。设 $A_{1,\sigma}$ 为指派的原始
系数与优先掩码之积，在第二侧取共轭，并设 $\psi^{\text{out}}_{1,\sigma}$ 为
所有保留的外二元截断之积。设 $e_\sigma$ 为在前述无商CRT提取中获得的
旧重数 $w(f)$、两个原始 $\beta$ 因子、其立方掩码（包括 $(b_a, f)=1$）、
提取的零掩码，以及在旧外理想处的有限高斯、单位、互反与第一射线因子之积，
排除所展示的 $\mu(d_k)$ 和 $B_{1,a}$。它独立于 $x_1, x_2$；其定义由该乘积给出，
而非通过除以方程 (17.30)。记
$O_1 = \{A_1, A_2, C, d, R, t, h\}$，置
$$w_{1,\sigma}(\omega; t) = e_\sigma(\omega)\mu(d_k)\mu(t')B_{1,1}(t'; y)\overline{B_{1,2}(t'; y)}B_1(h)A_{1,\sigma}(\omega)\psi^{\text{out}}_{1,\sigma}(\omega) \prod_{\alpha \in O_1} y_\alpha^{i t_\alpha}.$$

对于掩码的、主部还原的形式第一分量，傅里叶反演给出精确恒等式
$$T_{1,\sigma} = (2\pi)^{-9} \int_{\mathbb{R}^9} \hat{H}_{1,\sigma}(t) \sum_{\omega \in \Omega_\sigma} w_{1,\sigma}(\omega; t) \times Z^{(\kappa_1+9\eta/2)/2} P_1(y) \overline{Z^{(\kappa_2+9\eta/2)/2} P_2(y)}\, dt. \tag{17.31}$$

展开这两个多项式恢复了两个列模式；七个外模式恢复了方程 (17.29) 的其他坐标。其较大的
截断在保留支撑上为 1，而新截断在旧窗口非零处为 1。这逐项验证了该恒等式。
原始 $\beta$ 因子和每个外掩码仍在完整和中。

第一正优函数。对于任何有限或绝对收敛的加权和，我们使用

$$\left| \sum_\omega w_\omega U_1(\omega)\overline{U_2(\omega)} \right| \le \left( \prod_{i=1}^{2} \sum_\omega |w_\omega| |U_i(\omega)|^2 \right)^{1/2}. \tag{D}$$

                                                         130
