我们现在恢复式 (9.17) 中 Wu 的逐行选择。这里检测器取 $t = 1$，故 $D_* = U$。在表示与二进对固定之后，其逆剖面具有形式
$$W_{\mathrm{dyad}}(x)V_{\le}(Dx/U)x^{-\sigma-i\omega},\quad \omega = \gamma - \nu_F,$$
其中 $W_{\mathrm{dyad}}$ 是固定的光滑二进截断函数，$\nu_F$ 是来自检测器的 Fourier 频率。因子 $V_{\le}(Dx/U)$ 对行和是公共的；变化参数为 $\sigma \in [51/100, 1]$ 与 $|\omega| \le (3i + 1)T_1$。对任一参数求导会插入一个 $\log x$ 的幂，它在固定圆环上有界。用单位方盒覆盖这两个参数范围。这样的方盒至多有 $1 + T_1$ 的固定幂次个。引理 4.5 中的参数 Sobolev 不等式将方盒上的上确界用剖面导数平方的积分之有限和来界定。在取这些积分之前先对各行求和。在每个固定参数值处，求导只改变固定的剖面系数，插入允许的对数权重或剖面导数。因此式 (9.21) 适用于每一个这样的积分。这就证明了
$$\sum_{u\in UV} |M_u(D; W_u)|^2 \ll_{A,\epsilon_1} (UD)^{\epsilon_1}(1 + T_1)^{A_A} V^{1/2}\left(\frac{U}{V} + D + \left(\frac{UD}{V}\right)^{2/3}\right). \tag{9.22}$$

导数阶数从而 $A_A$ 在选取 $\tau$ 之前就已固定。高度区间以及对附加频率的总容许量与共享检测器估计中的完全一致；Sobolev 这一步不分配新的频率容许量，也不改变围道。它不允许对每个 $k$ 单独选取一个系数。

还需将此矩与独立的计数式 (9.19) 结合起来。记
$$V = U^o,\quad D = U^r,\quad e_o(r) = \frac{o}{2} + \max\left\{1 - o,\ r,\ \frac{2(1 - o + r)}{3}\right\}.$$
这些是实际二进对的参数。非空二进对有 $0 \le o \le 1 + O_A(1/\log U)$；单位二进对有 $o = 0$。由于见证长度保持有界，式 (9.22) 中 $UD$ 的任意小幂次可写成 $U$ 的任意小幂次。将该式除以式 (9.17) 中的尖峰，并同时使用式 (9.19)，得到对该细分
$$\#U_V \ll U^{\min\{1-o/2,\,e_o(r)-\delta r\} + O(\epsilon_0) + \epsilon_1}(1 + T_1)^{A_A}, \tag{9.23}$$
必要时可减小用 $\epsilon_1$ 表示的筛损失。

我们首先在 $0 \le o \le 1$ 与 $1/2 \le r \le 1$ 上计算此表达式中的最大指数。置 $x = 1 - o$，$A = (1 + x)/2$。则
$$e_o(r) - \delta r = \max\left\{A - \delta r,\ \frac{1-x}{2} + (1-\delta)r,\ \frac{1}{2} + \frac{x}{6} + \left(\frac{2}{3} - \delta\right)r\right\}.$$
$A$ 与三个实数之最大者的最小值，等于 $A$ 与这些数各自之最小值中的最大者。第一个这样的最小值为 $A - \delta r \le 1 - \delta/2$。对固定的 $r$，第二个是 $x$ 的一个递增仿射函数与一个递减仿射函数的最小值。它们在 $x = (1-\delta)r \in [0, 1]$ 处相交，故其关于 $x$ 的最大值为
$$\frac{1 + (1-\delta)r}{2} \le 1 - \frac{\delta}{2}.$$
第三个最小值中的两个函数都随 $x$ 递增。因此其关于 $x$ 的最大值为
$$\min\left\{1,\ \frac{2}{3} + \left(\frac{2}{3} - \delta\right)r\right\}.$$
其中的仿射表达式在两端点处取值 $1 - \delta/2$ 与 $4/3 - \delta$。由此可得，且等号在其中一个端点处取到，
$$\max_{\substack{0\le o\le 1\\ 1/2\le r\le 1}} \min\{1 - o/2,\ e_o(r) - \delta r\} = \min\left\{1,\ \max\left\{1 - \frac{\delta}{2},\ \frac{4}{3} - \delta\right\}\right\}. \tag{9.24}$$
