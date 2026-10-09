$\ell_* = \sigma_{\mathrm{width}}/3$，网格小于 $\sigma_{\mathrm{width}}/6$。在基 $U$ 处，每个活跃物理槽的范数至多为 $2U\eta_{\mathrm{mesh}}$，而池从 $U\ell_*/2$ 开始。它们固定的指数差使得这些集合对所有充分大的 $U$ 都不相交，且在所选 $d$ 范围内一致。标记的逆矩没有网格条件。

方程 (20.1) 中的正规化因子对于这一实际选择非零。令 $c_i = \int_0^\infty W_i(y)y^{-5/6}\,dy > 0$。第 20.1 节中已证明的渐近式特化为
$$
S_i(Z) \sim \frac{P^{1/6}c_i}{|T|\log P} > 0, \qquad A_T(Z) \sim \frac{K}{|T|\ell}\left(\frac{K}{\log Z}\right)^K \prod_i c_i (\log Z)^{-K} > 0.
$$
符号使用偶数 $K$。任何后续固定的排除集只影响共同的下阈值，因为其素数最终会离开所有这些窗口。选取
$$
\kappa_P = \frac{7}{16}\frac{\ell}{K} = \frac{7}{96K}, \qquad 0 < \kappa_P < \frac{7}{8}\min_i \ell_i = \frac{7}{48K}, \qquad m_P := \kappa_P.
$$
因此主逼近具有一个在目标之前选定的正裕量。子集的数量、窄窗口的半范数及其有限高度阶数可以依赖于这个固定的 $K$。

选取振幅宽度、剩余的幂损失以及 $e$，使其总的高代价小于 $m_{\mathrm{high}}/8$，并且使得
$$
(1+h)e + \epsilon_{\mathrm{pr}} < m_w/4, \qquad e + \epsilon_{\mathrm{pr}} < m_z/4, \qquad e + \epsilon_{\mathrm{pr}} < m_P/4.
$$
这里 $\epsilon_{\mathrm{pr}} > 0$ 包含主余项估计中所选的小幂。还要求 $e < 10^{-3}$ 以及引理 8.2 中的界 $e_0$。槽长已经固定，因此振幅细分所需的小幂可以根据其正的最小值来选取。所有这些选择只依赖于 $\Delta$ 和目标前槽系统。

选取
$$
0 < \zeta < \min\{1/48,\ m_{\mathrm{high}}/16\}.
$$
频率延拓的代价于是至多为 $2\zeta < m_{\mathrm{high}}/8$。现在在第 20.3 节中选取绝对直线 $z_\infty > 2$ 足够靠右，使其大行和相对于 $C(\beta_*)$ 有大于 $m_{\mathrm{high}}$ 的节省。其指数只依赖于这些实选择，因此 $z_\infty$ 也先于目标。选取方程 (10.2) 所需的目标前截断。目标固定后命题 16.1 所要求的任何额外固定排除素数可以加入 $S$：相同的正乘积尾控制量保持共享的压缩，且 $T$ 和槽窗口都不改变。

为清晰起见，非主实比较在引理 20.1 中的所有逐点对上是一致的。令 $\epsilon_{\mathrm{real}}(d) \geq 0$ 收集相关范围内分配的实损失、网格损失和矩损失。端点不等式、中间不等式和正斜率给出
$$
E(d) + \epsilon_{\mathrm{real}}(d) \leq (\beta_* - 7/8) - \varepsilon_{\mathrm{hi}}, \qquad \varepsilon_{\mathrm{hi}} > 0, \tag{20.12}
$$
对每个出现的 $(R,q)$ 和每个适中的 $d$ 成立，同时仍保留 $m_{\mathrm{high}}$ 的一个固定分数。因此同一不等式对 $E_{\max,Z}(d)$ 一致地关于 $Z$ 成立。小界和大界具有所述的分开节省。将次幂正规化估计一次应用于非主和外行贡献，并使用低于 $m_{\mathrm{high}}/8$ 的幂吸收剩余的有限二进重数。引理 10.5 已包含其自身的正规化裕量 $\epsilon_{\mathrm{pr}}$。上述四个高实分配代价小于 $m_{\mathrm{high}}/2$；这最后的裕量留下超过 $3m_{\mathrm{high}}/8$。主不等式在 $m_w$、$m_z$、$m_P$ 的每一个中留下超过 $3/4$。因此可以在目标之前固定
$$
m = \frac{1}{4}\min\{m_{\mathrm{high}}, m_w, m_z, m_P\} > 0
$$
作为保留高度因子之前的共同剩余高节省。对于低估计，应用方程 (20.2) 并取目标前损失 $\Delta/2$，并令 $\omega = \Delta/2$。令 $\epsilon_{\mathrm{ht}} > 0$ 为已用这些实损失选定的有限多个探测器高度裕量的最小值。
