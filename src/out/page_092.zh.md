对于一个由系数有界的互不相交素数列表构成的子集族 $I' \subset I$，定义其标记为
$$d_{I'}(A) = \sum_{(p_i) \in \prod_{i \in I'} P_i} \prod_{i \in I'} a_i(p_i) \mathbb{1}_{p_i \mid A}. \tag{14.1}$$
当 $I'$ 不言自明时，我们在记号中省略它。由于这些列表互不相交，一个元组具有无平方因子的乘积。对每个固定的 $\epsilon > 0$，整除 $A$ 的元组个数为 $O_\epsilon(q_A^\epsilon)$。方程 (14.1) 中的系数是各个素数函数的乘积；当某些槽位被分配给一个提取出的因子时，我们将用到这一性质，而不仅仅是逐点的除数界。

对于一个光滑环带 $W$，令 $V^*(y) = y^{1/2} W(y)$，并定义完备标记和
$$T_d(X; k) = \sum_{\substack{n \\ \mathfrak{b} \text{ sf}}} \frac{\bar{\alpha}(n)\gamma_2(n)\Psi_k(n) \, \bar{\alpha}(\mathfrak{b})^3 \Psi_k(\mathfrak{b})^3}{\sqrt{q_n q_{\mathfrak{b}}}} d(n\mathfrak{b}^3) V^*(q_n q_{\mathfrak{b}^3}/X). \tag{14.2}$$
两个主理想都避开 $S$；它们可能共享素数。标记属于整个指标 $n\mathfrak{b}^3$。当 $d = 1$ 时，这就是方程 (5.1) 左端的 Mellin 完备化。当只使用完备估计时，该方程中的高斯 Mellin 测试函数也是允许的。

对于反射公式，我们使用引理 5.2，且仅对非零行使用。如该引理中那样写 $k = u k_S k_{\text{good}}$。在固定单位、模六的 $S$-赋值以及好行的射线类之后，其字面扇区特征为
$$\Psi_0^{[k]}(A) = \begin{cases} \nu(A)\chi_A(u k_S) R(A, k_{\text{good}}), & A \equiv 1 \pmod{3},\ (A, S) = 1, \\ 0, & \text{否则}. \end{cases}$$
零分支在两个特征之前被求值。该引理在好素数变化之前提供了一个有限族，从而提供了一个素支撑为 $S$ 的公共 $L$。记 $M_{\text{ref}} = \lambda^{12} L^4$；完整的反射扇区模为 $M_{\text{ref}}^2 = \lambda^{24} L^8$。$k$、$f$、$r$ 的所有好素数都留在局部素数集中，其指数按模六合并，且每个零点都保留。$f$ 处的四次方没有额外的互反符号，因为 $R(A, f)^4 = 1$。穿孔是其好素数处局部零次幂的乘积。因此，局部表示在所声明的素支撑上恰好给出 $\Psi_k(n)\Psi_k(\mathfrak{b})^3$，包括在共享的好素数处；没有变动的好素数进入 $L$。

14.2 全指标标记反射

下一个推论将乘积形式的标记添加到第一部分中的精确反射中。其分支数据很重要：一个不活跃的标记素数不出现在导子中，因此标记变换不能通过将一个固定导子的对偶和乘以独立的局部因子来得到。

推论 14.1（带全指标标记的完备反射）。固定命题 5.1 的一次调用，其基局部素数集为 $P_0$，幂为 $j_p$，固定乘子为 $\phi$，测试函数为 $V$。对这次调用令 $M_{\text{ref}} = \lambda^{12} L^4$。设 $Q$ 是一个由与 $P_0$ 不相交的 $Q$ 个不同好素数组成的有限集。在直接完备系数和中，插入因子 $\prod_{q \in Q} \mathbb{1}_{q \mid n\mathfrak{b}^3}$；将此和记为 $T_Q(X; \Psi, V)$。它与方程 (14.2) 具有相同的正规化，其中 $\Psi_k$、$V^*$ 替换为 $\Psi$、$V$。主无平方因子理想与立方理想可以共享素数。

存在一个精确的有限展开
$$T_Q(X; \Psi, V) = \sum_B \zeta_Q \sum_{0 \neq \mu \in \lambda^{-4}\mathcal{O}} \frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4 \mu)}{\sqrt{q_\mu}} \prod_{p \in A_0} B_p(\lambda^4 \mu) \cdot \prod_{q \in A_Q} q^{-1/2} \chi_q(\lambda^4 \mu)^{-2} V^\sharp\left(\frac{q_\mu X}{q c^2}\right). \tag{14.3}$$
