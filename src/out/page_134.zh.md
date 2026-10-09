范数。对于这个预备模式 $\sigma_0$，方程 (17.33) 中被掩蔽的主恢复非零分量恰好为
$$
\begin{aligned}
T_{2,\sigma_0,i} = & \sum_{\substack{o\in O_\sigma,\ g'\ \mathrm{sf}\\ d_2\mid g',\ k''\neq 0}} w_{o+}\psi_g\psi_{d_2}\psi_{k''}\mu(d_2)B_2(k'')|B_o(g')|^2 \\
& \times \sum_{\substack{z_1,z_2\ \mathrm{sf}\\ (z_1z_2,g')=1}} \mathbf{1}_{(z_1,z_2)=1}L_{o,d_2,k''}(z_1)L_{o,d_2,k''}(z_2)G([z_2][z_1]^{-1}) \\
& \times dI_i(g'z_1)dI_i(g'z_2)W_i(q_{g'}q_{z_1}/Z^{s_i})W_i(q_{g'}q_{z_2}/Z^{s_i}) \\
& \times \frac{K}{\sqrt{q_{d_2}q_{z_1}q_{z_2}}}K^2\left(\frac{Kq_{k''}}{q_{d_2}q_{z_1}q_{z_2}}\right).
\end{aligned}
\tag{17.41}
$$
这里括号表示固定有限射线群中的类。确实，$c_i(g'z)$ 的算术部分分解为 $B_o(g')$ 及其在 $(g',z)=1$ 上的剩余 $\mu(z)$ 系数。公共行因子是 $g'$ 处的掩码，其 Poisson 展开给出单个除数 $d_2$，而上面的信号计算给出所显示的两个 $L$ 因子和射线商。恢复的主对 $z_1=z_2=1$ 由 $G(1)=1$ 吻合。其单独代价，以及在此公式之前移除的原始补余，均已界定。因此这是对正优函数指定分量的等式，而非对原带符号块的等式。

对所有逐个可容许的无平方因子 $z_1,z_2$，用其所显示的免商 $L$ 因子、固定射线商、形式乘积范数、完整核以及不变的 $B_2$ 来定义方程 (17.41) 的被加项。它在互素对上与真正公式一致。在任何逐因子估计之前，插入恒等式
$$
\mathbf{1}_{(z_1,z_2)=1} = \sum_{v'\mid (z_1,z_2)} \mu(v'), \qquad z_a = v'n_a,
$$
设 $v\geq 0$ 为无平方因子 $v'$-二进组的中心，$\hat{v}=\log_Z q_{v'}$。$n_a$ 是无平方因子的，且 $(v',n_a)=1$；它们不必两两互素。在此延拓上不使用本原 Poisson 公式。对无平方因子 $v'$，置
$$
D_o(v';d_2,k'') = a_0(v')\nu_i(v')\rho(v')\mathbf{1}_{(v',r_0)=1}\chi_{v'}(H_o)^4\chi_{v'}(d_0)\chi_{v'}(d_2)\chi_{v'}(k'').
$$
在无平方因子互素的 $v',n$ 上，精确提取为
$$
\begin{aligned}
L_{o,d_2,k''}(v'n) = & \ D_o(v';d_2,k'')a_0(n)\nu_i(n)\rho(n)\mathbf{1}_{(n,r_0)=1} \\
& \times \chi_n(H_o)^4\chi_n(d_0)\chi_n(d_2)\chi_n(k'')\chi_n(v')^4.
\end{aligned}
\tag{17.42}
$$
这利用了 $a_0(v'n)=a_0(v')a_0(n)\chi_n(v')^4$。在重叠处，右端通过 $\chi_n(v')^4$ 定义延拓为零，而不必计算非无平方因子的 Gauss 和。这两个公共因子给出 $|D_o(v';d_2,k'')|^2$，包括零 $(v',k'')=1$ 及其固定穿孔、$d_0$ 和标签零点。它们通过 Cauchy 留在外权重中。旧的 gcd 也留下 $\mathbf{1}_{(v',g')=1}$。由于 $D_o$ 在 $(v',CJ)>1$ 上为零，我们等价地保留显式外因子 $\mathbf{1}_{(v',g'CJ)=1}$，它重复了该标签零点。

置 $r_g=g'/d_2$，$k_{\mathrm{new}}=d_kd_2k''$，$f_{\mathrm{new}}=JCd_2v'$。$n$ 上所有变动因子满足完整的零延拓恒等式
$$
\chi_n(d_k)\chi_n(k'')\chi_n(d_2)\chi_n(CJ)^4\chi_n(v')^4 = \chi_n(k_{\mathrm{new}})\chi_n(f_{\mathrm{new}})^4.
\tag{17.43}
$$
它利用了 $\chi_n(d_2)=\chi_n(d_2)\chi_n(d_2)^4$，对非单位元也成立。与 $g'=d_2r_g$ 的剩余 gcd 分裂为 $d_2$ 处的重复零和 $r_g$ 处的固定穿孔。$q_0,t'$ 处的旧穿孔保留。若 $C_{\mathrm{ray}}$ 表示 $G$ 通过其分解的固定群，置
$$
\hat{G}(\vartheta) = |C_{\mathrm{ray}}|^{-1}\sum_{c\in C_{\mathrm{ray}}} G(c)\vartheta(c).
$$

134
