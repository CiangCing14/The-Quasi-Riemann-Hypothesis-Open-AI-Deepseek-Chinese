第二次 Poisson 变换。固定由第一次 Cauchy 不等式得到的两个正和之一。它的多项式具有形式
$$P_i(y) = \sum_{x} c_i(x)\chi_x(y).$$

系数 $c_i(x)$ 由方程 (C) 的其余因子组成，其中 $u_i = t'x$，穿刺点在 $t'$，并带有分离的权重。它与 $y$ 无关。特别地，$x$ 是无平方因子的，且

$c_i(x) = 0$ 除非 $(x, CJ) = 1$, $(x, \mathrm{rad}\, q_0 t') = 1$.

穿刺点 $\rho$ 以及 $\chi_x(d_k)$ 的零点也被保留。$y$-和使用了在尺度 $Z^{H_{\text{use}}}$ 处的固定形状光滑正球。

在其展开平方中令

$$g' = (x_1, x_2), \qquad x_j = g' z_j, \qquad \hat g = \log_Z q_{g'}.$$

设 $g \ge 0$ 为其固定中心。则 $z_1, z_2$ 无平方因子且互素，并且每个都与 $g'$ 互素。引理 17.5 的行数据为

$$K = Z^{H_{\text{use}}}, \qquad \psi_2 = \bar\chi_{z_1}\chi_{z_2}, \qquad m_2 = z_1 z_2, \qquad R_{\text{mask}} = g'. \tag{17.36}$$

公因子 $\bar\chi_{g'}(y)\chi_{g'}(y)$ 正是这个掩码。该特征在远离 $m_2 = 1$ 处是本原的，因为它的两个非零局部幂具有不相交的支集。对于 $d_2 \mid g'$，设 $\theta \ge 0$ 为其中心并记 $\hat\theta = \log_Z q_{d_2}$。实际导子长度为

$$\hat L_2 = \hat x_1 + \hat x_2 - 2\hat g, \qquad |\hat L_2 - 2(s_i - g)| \le 10\eta.$$

最后一个不等式使用了每个副本的完整新 $x$-支集界 $|\hat x_a - s_i| \le 4\eta$ 以及 $|\hat g - g| \le \eta$.

对于 $k_{\text{new}} = d_k d_2 k''$，蕴含关系 $Z^{H_{\text{use}}} q_{k''}/(q_{d_2} q_{m_2}) \le Z^{\tau}$ 给出

$$k_{\text{new}} \le 2(s_i - g) - H_{\text{use}} + \delta + 2\theta + 13\eta + \tau = M_c + \eta,$$

其中

$$M_c = 2(s_i - g) - H_c + \delta + 2\theta = M - 4\ell - 2A_i - 2t - 2g + 2\theta - 2V + j, \qquad M_{\text{ch}} = M_c + \eta. \tag{17.37}$$

其中的 $13\eta$ 由来自导子的 $10\eta$、来自 $d_k$ 的 $1\eta$ 以及来自 $d_2$ 的 $2\eta$ 组成。减去 $H_{\text{use}} = H_c + 12\eta + \tau$ 恰好抵消了在这次第二次 Poisson 比较中所用的同一容差 $\tau$。因此不需要单独的行裁剪或未记录的边界误差。

将原始主贡献分离出来用于下面的直接计数。在任何非互素扩展或 Fourier 绝对化之前，在真正的非主第二次 Poisson 表达式上只保留外掩码

$$B_2(k'') = 1_{0 < q_{d_k d_2 k''} \le Z^{M_{\text{ch}}}}.$$

对于每个被支撑的配对，其余集包含在刚才所考虑的实际比值尾中，因此方程 (17.21) 以如下确定的阶将其舍弃。在掩码内部保留完整的光滑核。该掩码依赖于 $d_k$、$d_2$、$k''$ 以及固定扇形，而不依赖于剩余量 $z_1$、$z_2$。若 $M_{\text{ch}} < 0$，则非零球为空，同一尾比较舍弃每个非零频率。在保留的非空通道中 $M_{\text{ch}} \ge 0$。

实际的第二前因子具有精确的侧分裂

$$Z^{H_{\text{use}} - \hat\theta - \hat L_2/2} = Z^{\hat\lambda_1/2} Z^{\hat\lambda_2/2}, \qquad \hat\lambda_a = H_{\text{use}} - \hat\theta - \hat x_a + \hat g.$$



                                                      132
