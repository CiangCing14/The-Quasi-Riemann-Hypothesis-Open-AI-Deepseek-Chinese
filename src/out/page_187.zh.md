几何与 Mellin 指数为
$$\begin{aligned} &h = \frac{13}{16}, \quad \ell = \frac{1}{6}, \quad l_x = \frac{17}{48}, \quad l_y = \frac{23}{48}, \quad h = 1 - l_x + \ell, \\ &C(s) = C_{II}(s) = s - \frac{11}{16}, \quad C(7/8) = \frac{3}{16}. \end{aligned}$$
这些是方程 (12.4) 与 (12.3) 中的值。用 $s$ 表示第 16 节中称为 $x$ 的局部变量；下面的振幅比 $x = q/\delta$ 是另一个不同的实数。
使用定义 10.1，其中

$I_\eta(Z) = I_{\eta,\text{modified}}(Z)$, $H_{\eta,u,Z}(s, w, z)$ 如方程 (16.3) 所定义。

在共用的解析引理中取 $\sigma_0 = 7/8$。第 16 节验证了这些数据的每一部分：方程 (16.7) 是方程 (12.5) 中独立定义的有限表达式所满足的绝对收敛的高恒等式，且完整修正项在两个所需的 Euler 区域中全纯，并满足方程 (10.4)。排除集、物理行掩码与校准均不变。特别地，在此完整修正项之外没有额外的 Euler 因子。其标量分母为 $\mathrm{LSF}(s, \eta_{\chi_\bullet}(u))$，其 Gaussian 为 $\Phi(s + z - 1)$。
在下面的估计中，$0 < e < 10^{-3}$ 是一个容许的探测器宽度。它的最终选取，连同其余实损失，将在结尾的选择次序中作出。

20.1    主正规化子
我们验证引理 10.5 的两个修正假设。首先，方程 (16.14) 给出

$$|H_{\eta,1,Z}(s, w, z)| \ll Z^{\ell \Re z}$$

在第二 Euler 区域的每个固定实盒上对所有虚部一致成立。特别地，它在方程 (10.17) 中的整个矩形上成立，高度次数为零。这是对完整元组修正项的界。
对于留数值，定义
$$S_i(Z) = \sum_{p \in \mathcal{P}_i(Z)} W_i(q_p/P_i) q_p^{-5/6}, \quad P_i = Z^{\ell_i}.$$

引理 13.1，包括其关于删除一个固定有限集的断言，给出
$$S_i(Z) \sim \frac{P_i^{1/6}}{|T| \log P_i} \int_0^\infty W_i(y) y^{-5/6}\, dy.$$

每个首项常数均为正。由于槽位数固定，对所有充分大的 $Z$，所有 $S_i(Z)$ 均为正，且有一个可依赖于固定数据的公共下阈值。令
$$A_T(Z) = (-1)^K Z^{-\ell/6} \prod_{i=1}^{K} S_i(Z). \tag{20.1}$$
利用 $\log P_i = \ell_i \log Z$ 以及 $\sum_i \ell_i = \ell$，我们得到

$$A_T(Z) \sim \frac{(-1)^K}{|T|^K (\log Z)^K} \prod_{i=1}^{K} \left( \frac{1}{\ell_i} \int_0^\infty W_i(y) y^{-5/6}\, dy \right).$$

因此 $A_T(Z) \neq 0$ 在该范围内，且

$$|A_T(Z)| \asymp_{T,K,(\ell_i,W_i)} (\log Z)^{-K}, \qquad |A_T(Z)|^{-1} \ll_\epsilon Z^\epsilon.$$

                                                    187
