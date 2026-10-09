展开相乘得到显式二次式

$$\begin{aligned} 10368J(-E^*) &= 2j_y[1 + (3 + 8y)\delta] - 468(5/6 - \delta)\delta p_y \\ &= 10(37 + 34y) - 8(237 + 377y + 26y^2)\delta \\ &\qquad + 48(51 + 131y + 94y^2 + 32y^3)\delta^2. \end{aligned}$$

乘以 $v$ 并配方得到

$$10368vJ(-E^*) = (3 + 5y)\left((4v\delta - 79)^2 + 49 + 4y\left(4v\delta[(1 + 3y)(15 + 32y)\delta + 9 - 13y] + 265 + 3485y\right)\right). \tag{20.9}$$

该恒等式也可通过系数验证：将其右边展开为 $\delta$ 的多项式，分别得到

$$\begin{aligned} &10v(37 + 34y), \\ &- 8v(237 + 377y + 26y^2), \\ &48v(51 + 131y + 94y^2 + 32y^3), \end{aligned}$$

它们分别是前式中常数项、一次项和二次项系数乘以 $v$。
方程 (20.9) 右边的每一项都非负：$y, \delta \ge 0$ 且 $9 - 13y \ge 5/2$。第一行至少为 $49(3 + 5y)$，而 $v = 51 + 41y \le 17(3 + 5y)$。因此
$$-E^* \ge \frac{49}{176256J} \ge \frac{49}{440640} > \frac{1}{10000},$$
其中用到 $J \le 5/2$。

$D_x$ 和 $J$ 的下界给出了交叉点与截断在紧参数范围内的所有导数的界。饱和损失是一致的，因为 $\delta \ge 1/50$，而逆选择具有命题 19.2 中证明的显式供给与宽度裕量。在零容量处，其未加权界与 $1 - \delta$ 的差至多为所选容量减量乘以一个常数。由于 $R^* \ge 1 - \delta$，这些情形服从相同的比较。因此，一旦各个请求损失至多为 $\epsilon$，所有检测器、分箱和舍入误差的总和就是 $O(\epsilon)$，其常数与目标无关。设 $E_{\text{actual}}(h)$ 表示在插入观测行界 $R \le R^* + \Delta/4 + \epsilon_{\text{row}}$ 之后相对于 $C(7/8)$ 的尺度指数。目前显式高度因子仍留在此指数之外。方程 (20.4) 中 $R$ 的系数为 $d$，因此在 $d = h$ 处，容量替换贡献 $h\Delta/4$。用 $\epsilon_{\text{total}}$ 表示 $h\epsilon_{\text{row}}$ 与所有其他可调实损失之和；前述一致性使其在与目标无关的系数下任意小。证书给出了实际所需的比较：
$$\begin{aligned} E_{\text{actual}}(h) - \Delta &\le -\frac{49}{440640} - \left(1 - \frac{h}{4}\right)\Delta + \epsilon_{\text{total}} \\ &= -\frac{49}{440640} - \frac{51}{64}\Delta + \epsilon_{\text{total}}. \end{aligned} \tag{20.10}$$
减去 $\Delta = C(\beta_{*}) - C(7/8)$ 是本质性的：该证书并不声称对每个 $\Delta$ 都有 $E_{\text{actual}}(h) < 0$。当高度因子在下面被转换为预留的指数裕量时，该裕量被加到 $\epsilon_{\text{total}}$ 上。

20.5 频率范围
对于 $1/2 \le d \le h$，可用长度为

$$\frac{\ell}{d} \ge \frac{8}{39} > \frac{1}{5} > \frac{7}{37}.$$

                                                193
