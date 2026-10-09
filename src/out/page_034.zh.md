零线。因此，核围线的移动不需要对条件收敛的 Dirichlet 级数逐项移动。
    对于方程 (5.5)，令 $f_Y (v) = \chi(e^v )V^\sharp (Y e^v )$。它支撑在一个固定的紧区间上。对其 Fourier 变换分部积分 $J + 2$ 次，并使用 $|u| \leq 1$ 时的平凡界，得到
                             $$\int_{\mathbb{R}} (1 + |u|)^J |\hat{f}_Y (u)|\, du \ll_J \sum_{j=0}^{J+2} \|f_Y^{(j)}\|_{L^1 (\mathbb{R})}.$$

Leibniz 法则和方程 (5.4) 将每个范数用方程 (5.5) 的右端控制，因为 $e^v$ 保持在 $(0, \infty)$ 的一个固定紧子区间内。最后，对于 $|u| \geq 1$，$B + 2$ 次分部积分给出
$$|\hat{V}(\eta + iu)| \leq |\eta + iu|^{-B-2} \int_0^\infty |(x\partial_x )^{B+2} V(x)| x^\eta \frac{dx}{x}.$$
对于 $|u| \leq 1$，使用相应的未求导积分。在 $-A \leq \eta \leq 1/4$ 上，$x^\eta \leq 1 + x^{-A} + x^{1/4}$，由此证明方程 (5.6)。恒等式 $x\widehat{{}^{iu_0} V}(\eta + iu) = \hat{V}(\eta + i(u + u_0))$ 和 $1 + |u| \leq (1 + |u + u_0|)(1 + |u_0|)$ 给出所断言的范数扭变界。特别地，Gaussian 测试函数 $V(x) = (2\sqrt{\pi})^{-1} \exp(-(\log x)^2 /4)$，其 Mellin 变换为 $e^{t^2}$，直接满足本命题的假设。

5.2  元素行与固定扇区
    为了将反射应用于特征 $A \mapsto \chi_A (m)$，我们将固定的补充相位与行的好素因子分离开来。这种分离在每个共享的好素数处保留了零点。

引理 5.2（非零行的固定射线扇区）。设 $\Psi_{\text{base}}$ 取遍一个固定的有限族有限射线特征，其导子支撑在 $S$ 上，并在与 $S$ 互素的素元素之外零延拓。使用引理 4.1 中 $l \in S$ 的固定生成元 $\pi_l$。对于 $0 \neq m \in \mathcal{O}$，唯一地写
$$m = u m_S m_{\text{good}}, \quad m_S = \prod_{l \in S} \pi_l^{v_l (m)}, \quad m_{\text{good}} = \prod_{p \notin S} p^{v_p (m)},$$
其中好素生成元是素的，$u$ 是单位。在每个与 $S$ 互素的素元素 $A$ 上，有
$$\chi_A (m) = \chi_A (u m_S )R(A, m_{\text{good}}) \prod_{p | m_{\text{good}}} \chi_p (A)^{v_p (m)}. \qquad (5.20)$$
右端所有幂保持其零值，包括当 $v_p (m) \equiv 0 \pmod{6}$ 时。固定 $u$、估值 $v_l (m)$ 模六，以及 $m_{\text{good}}$ 在 $R$ 所通过因式分解的固定射线群中的类。在这样的扇区中定义
$$\Psi_0^{[m]} (A) = \begin{cases} \Psi_{\text{base}} (A)\chi_A (u m_S )R(A, m_{\text{good}}), & A \equiv 1 \pmod{3},\ (A, S) = 1, \\ 0, & \text{否则}. \end{cases} \qquad (5.21)$$
非零分支是一个固定的有限族有限射线特征的成员，其导子支撑在 $S$ 上。因此，命题 5.1 中的单个 $E, L$ 对所有这样的扇区都适用。局部素数集包含每个 $p | m_{\text{good}}$，指数为 $v_p (m)$ 模六，即使该指数为零。没有移动的好素数被吸收进 $L$。

证明。若 $(A, m_{\text{good}}) = 1$，乘性以及引理 4.4 中的对称互反因子给出方程 (5.20)。若一个好素数被共享，两端均为零：左端是 $\chi_A (m)$ 的零延拓，而右端的局部因子即使对可被六整除的指数也为零。这证明了在所陈述的整个区域上的恒等式。
