对每个固定的 $H \ge 0$，存在有限非负数 $\ell_e(H)$、$b_e(H)$、$c_e(H)$ 以及常数 $C_{e,H}$，使得

$$\int_{\mathbb{R}^{d_e}} |K_e(Z,w,t;\xi)| \langle \xi \rangle^H \, d\xi \le C_{e,H} \, p^{\ell_e(H)}(w)^{b_e(H)} \langle t \rangle^{c_e(H)}.$$

半范数指标可以向上取整为整数。所有这些常数和指标关于 $Z$ 及附加标签都是一致的；指数 $a_v$、$a_e$ 是固定的实数，与所要求的半范数阶和高度阶无关。

于是存在有限的 $J$、$B$、$H$ 和 $C$，使得在根 $v_0$ 处，

$$N_{v_0}(Z,w,t) \le C Z^E p^J(w)^B \langle t \rangle^H, \quad E = \max\left(a_v + \sum_{v_0 \to \cdots \to v} a_e\right),$$

其中求和遍历路径上的边 $e$。

指标 $J$、$B$、$H$ 可以沿至多 $D$ 个阶段反向选取。特别地，它们在施加任何限制 $|t| \le T_1 = Z^\tau$ 之前就已固定。

对于积分中有限个孩子的乘积，同样的结论成立。确切地说，一个边项可以具有如下形式

$$Z^{a_e} \int_{\mathbb{R}^{d_e}} |K_e| \prod_{r=1}^{r_e} N_{v_{e,r}}\left(Z, W_{e,r}, A_{e,r} t + B_{e,r} \xi\right)^{\theta_{e,r}} d\xi,$$

其中 $r_e \ge 1$ 是固定整数，$\theta_{e,r} \ge 0$ 是固定的，所有孩子具有更小的剩余深度，并且每个孩子剖面满足其自身版本的所述剖面界。联合系数测度满足相同的加权界。在此情形下，递归地定义范数指数为

$$E_v = \max\left(a_v, \max_e\left(a_e + \sum_{r=1}^{r_e} \theta_{e,r} E_{v_{e,r}}\right)\right).$$

结论以 $E = E_{v_0}$ 成立。这一形式包含了由 Cauchy–Schwarz 不等式产生的两个非负孩子估计的平方根。

证明。在终端顶点，断言即为所述的界。假设某个孩子已经被 $C Z^{E'} p^{J'}(W_e)^B \langle A_e t + B_e \xi \rangle^{H'}$ 所界住。由于线性映射是有界的，

$$\langle A_e t + B_e \xi \rangle^{H'} \ll_e \langle t \rangle^{H'} \langle \xi \rangle^{H'}.$$

孩子剖面界将幂 $B' c'_e(J')$ 加到这两个高度指数中的每一个上，并将其剖面因子替换为 $p^{m_e(J')}(w)^{B' b_e(J')}$。以 $H_e = H' + B' c'_e(J')$ 使用系数测度界。此边的贡献至多为

$$C_e Z^{a_e + E'} p^{\max\{m_e(J'), \ell_e(H_e)\}}(w)^{B' b_e(J') + b_e(H_e)} \langle t \rangle^{H_e + c_e(H_e)}.$$

上面出现的每个指标都是有限的。对有限多条出边取这些指标与终端指标的最大值，并在必要时增大剖面指数，因为 $p^j(w) \ge 1$。这就证明了父结点的界，其指数等于经过该顶点的最大路径指数。在无环图上做反向归纳法即完成证明。这些选择均不涉及外部截断或后加的导数阶。

对于乘积形式，插入每个孩子已经证明的界并将其提升到 $\theta_{e,r}$ 次幂。系数测度所必须积分的 $\langle \xi \rangle$ 的总幂次为

$$H_e = \sum_{r=1}^{r_e} \theta_{e,r} \left(H_r + B_r c'_{e,r}(J_r)\right).$$

父剖面的幂次与 $\langle t \rangle$ 的幂次是相应的有限和，随后在 $H_e$ 处使用一次系数测度界。$Z$ 的幂次按照 $E_v$ 的递推式相加。对有限多项取最大值，即由同样的反向归纳法证明此推广。
