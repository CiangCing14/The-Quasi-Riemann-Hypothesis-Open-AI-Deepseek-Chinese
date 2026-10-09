证明。记 $R_j = 2 - a - je$，$C = 2Q(3 + |t|)^2$。此处所用的所有圆盘都位于 $\Re s > 1/2$ 内，主正则化因子在该区域内全纯。在无零点圆盘上选取一个全纯对数 $g = \log L$，使其在中心附近的值等于 Euler 对数，并在主情形下加上正则化因子的对数。值 $g(2 + it)$ 一致有界。引理 4.8 以及 $11/10$ 右侧的 Euler 收敛性给出

$$\Re g(s) = \log |L(s)| \ll \log C \qquad (|s - (2 + it)| \leq R_3).$$

可能的高度与 $t$ 相差至多 $3/2$，这已包含在 $C$ 中。在半径 $R_3$、$R_4$ 上应用 Borel–Carathéodory 定理，两者之差为 $e$，即得在半径 $R_4$ 的圆盘上 $|g| \ll_e \log C$。

在固定半径 $r_0 = 49/100$ 的圆盘上，有 $\Re s \geq 151/100 > 1$。绝对收敛的 Euler 对数在该处一致有界。对于主函数，$(s-1)/(s+1)$ 的对数在该圆盘上也有界，取其在 $\Re s > 1$ 中的分支。由于 $r_0 < R_6 < R_4$，对 $g$ 应用 Hadamard 三圆定理得

$$\max_{|s-(2+it)| \leq R_6} |g(s)| \ll_e (\log C)^\theta, \qquad \theta = \frac{\log(R_6/r_0)}{\log(R_4/r_0)} < 1.$$

对于固定的 $e$，在紧区间 $1/2 \leq a \leq 1$ 上的连续性使得 $\theta$ 一致地小于 $1$。对每个 $\epsilon > 0$，有 $\exp(C_e (\log C)^\theta) \ll_{e,\epsilon} C^\epsilon$。将其应用于 $e^g$ 与 $e^{-g}$ 即证得方程 (4.15)。在半径 $R_6$ 与 $R_8$ 之间应用 Cauchy 估计即得 $g' = L'/L$ 的所述界。

对于整体断言，先设 $\beta_* \leq b \leq 1$。选取 $0 < e < \min(10^{-3}, v/8)$ 并令 $a = b$。半径 $R_2$ 的圆盘包含于 $\Re s > b + 2e > \beta_*$ 中，故由 $\beta_*$ 的定义及超过 $1$ 的绝对 Euler 收敛性知其为无零点圆盘。半径 $R_8$ 的圆盘在其中心高度处覆盖了点 $b + v \leq \Re s \leq 2$；Euler 收敛性覆盖 $\Re s \geq 2$。上述常数关于 $b$ 一致。若 $b > 1$，则 $\Re s \geq 1 + v$ 上的 Euler 收敛性已足够。最后

$$\frac{1}{\zeta_F(s)} = \frac{s-1}{s+1} L(s)^{-1}, \qquad \left|\frac{s-1}{s+1}\right| \leq 1 \ (\Re s \geq 0),$$

这证明了主倒数断言。

引理 4.10（$Q$（删除的 $-s$ Euler 因子））。设 $R$ 为无平方因子的理想，且对 $p \mid R$ 有 $|a_p| \leq 1$。置 $D_R(s) = \prod_{p \mid R} (1 - a_p q_p^{-s})$。对于固定的 $\sigma_0 > 0$ 及每个 $\epsilon > 0$，

$$|D_R(s)| + |D_R(s)^{-1}| \ll_{\sigma_0,\epsilon} q_R^\epsilon \qquad (\Re s \geq \sigma_0).$$

在有界实带内，关于高度一致地有

$$|D_R(s)| \ll_\epsilon q_R^{(-\Re s)_+ + \epsilon}, \qquad \frac{D_R'(s)}{D_R(s)} \ll_{\sigma_0} \log(2q_R) \qquad (\Re s \geq \sigma_0).$$

特别地，支集 $q_R \leq Z^B$ 且 $B$ 有界时，在固定的正实半平面上其代价为任意指定的 $Z$ 的正幂次。对于非本原函数 $L(s,\psi^*) D_R(s)$，应用对数控制时必须同时包含本原导子与删除根式 $R$。

证明。每个因子在 $\Re s > 0$ 上非零。对于 $\Re s \geq \sigma_0$，其绝对值及其倒数的绝对值至多为 $(1 - q_p^{-\sigma_0})^{-1}$。对于充分大的 $q_p$（依赖于 $\sigma_0$、$\epsilon$），有 $-\log(1 - q_p^{-\sigma_0}) \leq \epsilon \log q_p$。有限多个较小的素数贡献一个固定常数。这证明了第一个估计。对于任意实数 $\sigma$，

$$\prod_{p \mid R} (1 + q_p^{-\sigma}) \leq q_R^{(-\sigma)_+} + 2^{\#\{p : p \mid R\}} \ll_\epsilon q_R^{(-\sigma)_+ + \epsilon}.$$

23
