因此不需要选择任何素数，理想行指数为 $R = 1 - \delta$。在式 (20.4) 中取 $q \le \delta/2$，得到

$$E(h) \le C_0 + \left( \frac{3}{4} - h \right)\delta + O(\epsilon) = -\frac{1}{48} - \frac{\delta}{16} + O(\epsilon) < 0. \tag{20.7}$$

现在假设 $1/50 < \delta < \alpha$。令 $x = q/\delta \in [0, 1/2]$，并使用命题 19.2 中的 $D_x, P_x, R_{\text{short}}, L$。参数 $\kappa$ 保持动态值 $3/4 + 2\Delta$，而非上界 $5/6$。因此该命题中实际使用的普通容量为

$$z_P(m) = \frac{1 - 2m}{6\kappa} = \frac{1 - 2m}{9/2 + 12\Delta},$$

与式 (19.2) 一致。式 (19.6) 中的比较针对这一精确容量，至多将行指数提高 $\Delta/4$，除去所要求的小损失。定义

$$J = (\alpha - \delta)D_x + \delta P_x, \qquad t = 1 + \frac{\delta P_x}{2J}, \qquad R^* = L(t). \tag{20.8}$$

分母为正。事实上

$$\frac{37}{18} \le D_x \le 3, \qquad \frac{7}{9} \le P_x \le 2, \qquad D_x - P_x = 1 + x - \frac{8x^2}{9} > 0,$$

从而

$$\frac{35}{54} \le J \le \frac{5}{2}.$$

因为 $0 < \delta < \alpha$，有 $J > \delta P_x > 0$，故 $1 < t < 3/2$。此外，

$$D_x \{R_{\text{short}}(t) - L(t)\} = \delta P_x (3/2 - t) - (\alpha - \delta)D_x (t - 1) = \frac{\delta P_x}{2} - J(t - 1) = 0.$$

因此 $R^* = R_{\text{short}}(t) = L(t)$，且该 $t$ 平衡了两个计数。这些公式在端点处也具有所述的闭合值：当 $\delta = \alpha$ 时，$J = \alpha P_x$，$t = 3/2$，且 $R^* = R_{\text{short}}(3/2) = L(3/2) = 1 - \delta$。相应的交叉点有 $r^*(3/2) = 1$，故其逆容量为零。前述等式论证在该边界处使用了式 (19.3)，而非带有消失余量的标记估计。

引理 20.2（补偿端点证书）。对 $0 \le \delta \le 5/6$ 和 $0 \le x \le 1/2$，由式 (20.8) 定义 $J, t, R^*$，其中 $J > 0$，并令 $E^*$ 为取 $q = x\delta$ 和 $R = R^*$ 时的 $E(h)$。则

$$-E^* \ge \frac{49}{440640} > \frac{1}{10000}.$$

特别地，该界在范围 $1/50 < \delta \le 5/6$ 上一致成立，包括闭合端点。

证明。令 $y = 1/2 - x \in [0, 1/2]$ 且 $v = 51 + 41y$。为验证计算，写出

$$p_y = 7 + 18y + 8y^2, \qquad j_y = 185 + 170y + (-138 + 12y + 96y^2)\delta.$$

则

$$D_x = \frac{37 + 34y}{18}, \qquad P_x = \frac{p_y}{9}, \qquad J = \frac{j_y}{108}.$$

由 $R^* = 1 - \delta + (\alpha - \delta)\delta P_x / (2J)$ 和式 (20.4)，

$$-E^* = \frac{1 + (3 + 8y)\delta}{48} - \frac{13}{32} \cdot \frac{(5/6 - \delta)\delta P_x}{J}.$$
