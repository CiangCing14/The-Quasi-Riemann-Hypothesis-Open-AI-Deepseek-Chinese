我们还需要在 $Z \downarrow 0$ 时进行控制。由式 (2.2)，$H_\eta$ 在 $\Re s > \sigma_0$ 上有界。倒数 Euler 乘积在 $\Re s \geq 2$ 上绝对且一致有界。在每个固定带状区域 $2 \leq \Re s \leq B$ 上，式 (2.3) 中的 Gaussian 为 $O_B(e^{-(\Im s)^2})$。因此矩形上的 Cauchy 定理可将围道移至任意固定的 $B > 2$，水平积分趋于零。故

$$|f_\eta(Z)| \ll_{\eta,B} Z^{B+c} \qquad (0 < Z \leq 1).$$

由于 $B$ 任意，该信号在零点处具有任意快的幂次衰减。

这一界与式 (2.6) 表明

$$F_\eta(s) := \int_0^\infty f_\eta(Z) Z^{-C(s)} \frac{dZ}{Z}$$

在 $\Re s > \beta_* - \epsilon_*$ 上局部一致收敛。在每个紧子集上，选取 $B$ 大于积分在零点附近出现的所有实部，并在无穷远处使用式 (2.6)。因此 $F_\eta$ 在该半平面上全纯。

我们在不跨越零点的前提下移动围道来识别这个 Mellin 变换。令

$$A_\eta(s) = e^{(s-5/6)^2} \frac{H_\eta(s)}{L_{SF}(s,\eta)} \qquad (\Re s > 1).$$

函数 $A_\eta(2+it)$ 关于 $t$ 连续且可积。令 $Z = e^u$，式 (2.3) 变为

$$e^{-(2+c)u} f_\eta(e^u) = \frac{1}{2\pi} \int_{\mathbb{R}} e^{itu} A_\eta(2+it) \, dt.$$

由两个端点估计，左端关于 $u$ 可积。因此普通 Fourier 反演给出对每个实数 $t$ 有 $F_\eta(2+it) = A_\eta(2+it)$。两端在 $\Re s > 1$ 上均全纯，故由恒等定理得

$$F_\eta(s) = e^{(s-5/6)^2} \frac{H_\eta(s)}{L_{SF}(s,\eta)} \qquad (\Re s > 1).$$

式 (2.2) 蕴含在 $\Re s > \sigma_0$ 上 $|H_\eta(s)| \geq 1/2$。因此

$$e^{-(s-5/6)^2} \frac{F_\eta(s)}{H_\eta(s)} \qquad (\Re s > \beta_* - \epsilon_*)$$

是 $1/L_{SF}(s,\eta)$ 的全纯延拓。数 $\epsilon_*$ 的选取与 $\eta$ 无关。由 $\beta_*$ 的定义，某个目标具有零点 $\rho$ 满足 $\Re\rho > \beta_* - \epsilon_*$。其倒数在 $\rho$ 处有极点，而被删去的因子在该处非零。这与延拓矛盾。

命题 2.1 中的高估计是相对于 $C(\beta_*)$ 而非 $C(\sigma_0)$ 度量的。当某一行的贡献达到低尺度但仍相对于假设的最右零点具有幂次节省时，这一区别至关重要。第一部分使用

$$\sigma_0 = \frac{11}{12}, \qquad C(s) = s - \frac{2}{3}, \qquad C(\sigma_0) = \frac{1}{4},$$

而第二部分使用

$$\sigma_0 = \frac{7}{8}, \qquad C(s) = s - \frac{11}{16}, \qquad C(\sigma_0) = \frac{3}{16}.$$

只有正的幂次余量必须在目标上一致。在两个应用中，固定特征常数、排除集以及充分大的下阈值都可以依赖于它。

9
