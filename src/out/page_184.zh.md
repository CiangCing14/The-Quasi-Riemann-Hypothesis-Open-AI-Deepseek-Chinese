无选定素数的逆见证。当没有选定任何逆槽时，改用引理 17.6 的六次幂放大。它适用于这些物理行，因为它们的理想赋值至多为五，且其原始零扩张保持不变。经过当前细分后，$U, t, D, D^*$ 是公共的，而逆基剖面为

$$W_{\mathrm{base}}(y) = W_1(y) V_{\leq}(Dy/D^*).$$

其固定对数半范数一致有界：第二个因子的导数支撑在其缩放自变量位于一个固定紧区间之处。其余逐行参数为位于固定紧区间内的 $\sigma$，以及纯扭转 $-( \gamma - \nu )$，其绝对值至多为 $(3I + 1)T_1$。因此引理 17.6 的逐行断言在该高度范围内适用。将其因子 $(1 + (3I + 1)T_1)^A$ 替换为 $(3I + 2)^A (1 + T_1)^A$ 只改变一个固定常数。

为清晰起见，即使 $r$ 随 $U$ 趋近于一，这一使用也是一致的。若 $0 \leq r \leq R_0$，则具有预备损失 $\epsilon_0$ 的方程 (17.88) 的指数为

$$\max\left\{1, \frac{1 + 5(1 + c)r}{6}\right\} + (1 + r)\epsilon_0 \leq e(r) + \frac{5cR_0}{6} + (1 + R_0)\epsilon_0, \quad e(r) = \max\left\{1, \frac{1 + 5r}{6}\right\}.$$

对于所要求的损失 $\epsilon_m > 0$，例如取 $c = 3\epsilon_m/(10 \max\{R_0, 1\})$ 和 $\epsilon_0 = \epsilon_m/(4(1 + R_0))$。这些在 $U$ 之前固定，且两个额外项至多为 $\epsilon_m/2$。因此除以逆见证尖峰给出

$$\#B \ll U^{e(r) - \delta r + \epsilon} (1 + T_1)^{AA},$$

$$e(r) - \delta r = \begin{cases} 1 - \delta r, & 0 \leq r \leq 1, \\ 1 - \alpha + (\alpha - \delta)r, & r \geq 1. \end{cases} \qquad (19.3)$$

特别地，这不是以收缩余量 $1 - r$ 对严格标记矩的应用。

无需选定素数的情况。我们首先处理那些见证已经给出所需计数而无需选定素数的情况。对于 $r \geq 1$，方程 (19.3) 使用有效矩指数 $(1 + 5r)/6 = 1 - \alpha + \alpha r$。除以逆尖峰给出 $1 - \alpha + (\alpha - \delta)r$。由于 $\delta \leq \alpha$ 且 $r \leq t + O(\epsilon)$，这至多为

$$L(t) = 1 - \alpha + (\alpha - \delta)t = 1 - \delta + (\alpha - \delta)(t - 1) \qquad (19.4)$$

至多相差 $O(\epsilon)$。这包括 $r = 1$，此时方程 (19.3) 中的两个分支一致。若 $m \geq 1/2$，引理 18.1 的零槽情形给出计数指数 $1 - 2\delta m \leq 1 - \delta$。由于 $R_{\mathrm{short}}(t) \geq 1 - \delta$，这也满足所述界。因此对于剩余论证，我们可以假设

$$r < 1, \quad m < 1/2.$$

此时两个容量 $z_M(r)$ 和 $z_P(m)$ 均为正；当其中任何一个对于固定减量而言过小时，我们将在下文使用其未加权估计。

比较正容量。对于逆容量 $z_M(r)$，所得的理想指数为下文的 $A_I(r)$。为了先比较普通指数，将 $z_P(m)$ 替换为其在 $\Delta = 0$ 处的值，即 $2(1 - 2m)/9$。由于实际的 $m$ 至少为 $t - r - O(\epsilon)$，所得的理想比较指数为

$$A_I(r) = 1 - \delta\{x + (1 - x)r\},$$

$$S_t(r) = 1 - \delta\left\{\frac{4x}{9} + \left(2 - \frac{8x}{9}\right)(t - r)\right\}. \qquad (19.5)$$
