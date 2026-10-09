这些项现在被恢复以统一公式，并带有相同的掩码。它们的绝对贡献已由先前估计的完整主恢复所界定。
    通过
$$1_{(u_1,u_2)=1} = \sum_{t' \mid (u_1,u_2)} \mu(t'), \qquad u_i = t' x_i, \qquad \hat t = \log_Z q_{t'}.$$

去除条件 $(u_1, u_2) = 1$。
设 t 为其固定的非负中心。此反演是在交叉相位已被上述固定射线函数替换之后进行的。这些函数、未改变的外层掩码 $B_1$、所有剩余的零延拓局部因子，以及光滑核中的形式乘积 $q_{u_1} q_{u_2} q_{R_1}$，也为非互素的 $u_1, u_2$ 定义了一个表达式。它与互素支集上的 Poisson 求和一致；所展示的除子恒等式随后恰好恢复该支集。对于新引入的非互素对，不宣称任何本原 Poisson 公式。无平方因子性保留了穿孔 $(x_i, t') = 1$。在 $t'$ 处指定的槽位是外系数，而其他槽位构成 $x_i$ 上的标记。
    从对所有 $f, E$ 共同的一个固定分割中插入 $q_h$ 的二进对，而不是为那些标签重新中心化的分割。掩码 $B_1$ 蕴含 $q_h \le q_{hf}^2 E \le Z^{H_{\text{use}}}$，因此在有界保留尺度范围内只有对数多个这样的二进对。将 $B_1$ 保持在每次 Fourier 反演之外。定义
$$s_i = r - A_i - B - t, \qquad \kappa_i = M - 2r - 2\ell - V - \delta + A_i + B - R/2.$$
在因式化表达式上的恒等式 $n_i = A_i C t' x_i$ 给出 $|\hat x_i - s_i| \le 4\eta$。完整的新鲜 $x_i$-支集包含在 $I_D$ 中，因此在分离后该相同界直接在该支集上成立，而不仅仅在原始乘积支集上。当前前因子中使用的重构形式乘积也包含在那里。

分离第一个变换后的乘积。我们记录应用 Cauchy 前的实际前因子。它恰好按两个列侧分裂为

$$Z^{-r-2\ell-V} Z^{M-\hat\delta-\hat L_1/2} = Z^{\hat\kappa_1/2} Z^{\hat\kappa_2/2}, \qquad \hat\kappa_i = M - r - 2\ell - V - \hat\delta - \hat n_i + \hat A_i + \hat B - \hat R/2.$$

方程 (17.18) 在每侧给出
$$\hat\kappa_i \le \kappa_i + \frac{9}{2}\eta. \tag{17.27}$$
五个误差权重为 $1, 1, 1, 1, 1/2$。我们现在在一个联合剖面中实现此归一化，包含所有实反根。固定第一个二进、射线和槽位模式 $\sigma$，并设 $h_1$ 为其裸 $h$ 二进对的中心。使用九个独立归一化坐标
$$y = (y_{A_1}, y_{A_2}, y_C, y_d, y_R, y_t, y_h, y_{x_1}, y_{x_2}) = \left( \frac{q_{A_1}}{Z_{A_1}}, \frac{q_{A_2}}{Z_{A_2}}, \frac{q_C}{Z_B}, \frac{q_{d_k}}{Z_\delta}, \frac{q_{R_1}}{Z_R}, \frac{q_{t'}}{Z_t}, \frac{q_h}{Z_{h_1}}, \frac{q_{x_1}}{Z_{s_1}}, \frac{q_{x_2}}{Z_{s_2}} \right).$$
在形式 $u_a = t' x_a$ 表达式上的精确全根与核参数为
$$\begin{aligned} \frac{Z^{-r-2\ell-V} Z^M}{q_{d_k} \sqrt{q_{R_1} q_{t'}} \sqrt{q_{x_1} q_{x_2}}} &= Z^{(\kappa_1+\kappa_2)/2} y_d^{-1} y_R^{-1/2} y_t^{-1} (y_{x_1} y_{x_2})^{-1/2}, \\ \frac{Z^M q_h}{q_{d_k} q_{R_1} q_{t'}^2 q_{x_1} q_{x_2}} &= A_{\text{ker},1} \frac{y_h}{y_d y_R y_t^2 y_{x_1} y_{x_2}}, \tag{17.28} \\ A_{\text{ker},1} &= Z^{M+h_1-\delta-R-2t-s_1-s_2}. \end{aligned}$$
选择新鲜截断 $\omega_{x,a}$，在旧 $W$-支集除以单个 $A_a, C, t'$ 支集上等于一，并将它们保留在列中。将每个当前外二进截断保留在反演之外。设 $\Omega_{1,\alpha}$ 为在这些保留截断的完整支集上等于一的更大截断。令 $K_1 = F\Phi$，定义单个紧剖面
$$H_{1,\sigma}(y) = Z^{-9\eta/2} \prod_\alpha \Omega_{1,\alpha}(y_\alpha) y_d^{-1} y_R^{-1/2} y_t^{-1} (y_{x_1} y_{x_2})^{-1/2} \times W(y_{A_1} y_C y_t y_{x_1}) W(y_{A_2} y_C y_t y_{x_2}) K_1 \left( A_{\text{ker},1} \frac{y_h}{y_d y_R y_t^2 y_{x_1} y_{x_2}} \right). \tag{17.29}$$

                                                           129
