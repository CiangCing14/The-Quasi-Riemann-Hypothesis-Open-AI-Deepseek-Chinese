对于特征表示，其定义模支撑恰好由那些它被零延拓的素数组成，包括非本原表示中的任何冗余素数。一个固定特征包含其整个零延拓表示以及通过其呈现的有限射线群，这些都独立于 $Z$、当前行和平均化标签而固定。固定数据可以依赖于事先固定的目标。特别地，每个这样的特征在每个 $S$ 外的素数处模为一。我们也记 $S = S$。我们称 $S$ 外的素数为好素数，并称一个理想为好理想，如果它的所有素因子都在 $S$ 外。除非指定了不同的支撑，理想的求和排除 $S$ 并使用主生成元。我们用“sf”表示无平方因子，用 $\mu$ 表示理想 Möbius 函数。相比之下，元素行可以具有任意素数幂和单位因子。

对于 $z \in F$，定义
$$e(z) = \exp 2\pi i \operatorname{Tr}_{F/\mathbb{Q}} (z/\lambda).$$
它到 $\mathbb{C}$ 的延拓为 $e(z) = \exp(4\pi i \operatorname{Im} z/\sqrt{3})$。测度 $d\mu(z) = (2/\sqrt{3}) \, dx \, dy$ 使得 $\mathcal{O}$ 对于配对 $(z, y) \mapsto e(zy)$ 是自对偶的。事实上，写 $y = u + v\omega$，其中 $u, v$ 为实数，条件 $e(y) = e(\omega y) = 1$ 说明 $v, u - v \in \mathbb{Z}$，从而 $y \in \mathcal{O}$；且 $\mathcal{O}$ 关于 $d\mu$ 的余体积为一。圆盘中的格点计数，随后除以六个单位，给出无限制的理想计数
$$\#\{a : q_a \leq H\} = \frac{\pi H}{3\sqrt{3}} + O(\sqrt{H} + 1) \qquad (H \geq 0).$$
例如，误差项可通过用 $O(\sqrt{H} + 1)$ 个固定基本平行四边形覆盖圆盘边界得到。

若 $p \notin S$ 为素数，其剩余域有阶 $P = q_p \equiv 1 \pmod{6}$：六个单位根在该域中保持互异。定义六次符号 $\chi_p(a) = (a/p)_6$ 为满足
$$\chi_p(a) \equiv a^{(P-1)/6} \pmod{p} \ (p \nmid a), \qquad \chi_p(a) = 0 \ (p \mid a)$$
的唯一六次单位根。

对于 $S$ 外的主元 $c = \prod_{p \mid c} p^{v_p(c)}$，定义 $\chi_c(a) = \prod_{p \mid c} \chi_p(a)^{v_p(c)}$，并对每个 $a$ 置 $\chi_1(a) = 1$。对于每个整数 $j$，包括 $j = 0$ 和负 $j$，记号 $\chi_c(a)^j$ 在 $(a, c) = 1$ 时表示通常的幂，否则表示零。因此，被六整除的指数是函数 $\mathbf{1}_{(a,c)=1}$，而非常数函数一。平方 $\chi_c^2$ 是三次符号。对于无平方因子的 $c$，置
$$\gamma_j(c) = q_c^{-1/2} \sum_{v \bmod c} \chi_c(v)^j e(v/c), \qquad \gamma_j(1) = 1.$$

引理 4.1（固定分子给出射线特征）。固定 $0 \neq a \in \mathcal{O}$。在素理想 $\mathfrak{p} \nmid 6a$ 处，设 $(a/\mathfrak{p})_6$ 为满足 $a^{(q_{\mathfrak{p}} - 1)/6} \pmod{\mathfrak{p}}$ 的唯一六次单位根；在 $S$ 外的素数处，这就是 $\chi_{\mathfrak{p}}(a)$。扩张 $F(a^{1/6})/F$ 是有限阿贝尔扩张，且在整除 $6a$ 的素数外非分歧，并且
$$\frac{\operatorname{Frob}_{\mathfrak{p}}(a^{1/6})}{a^{1/6}} = (a/\mathfrak{p})_6,$$
其中 $\operatorname{Frob}_{\mathfrak{p}}$ 是算术 Frobenius。因此，此符号到与 $6a$ 互素的理想的乘法延拓是一个有限阶射线特征，其导子支撑在整除 $6a$ 的素数上。对其在这些素数处的导子指数未作任何断言。这一识别仅在与 $6a$ 互素的理想上成立；当一个好理想 $A$ 与 $a$ 相交时，它并不会抹去 $\chi_A(a)$ 的规定零点。

特别地，对每个 $\mathfrak{p} \in S$ 选取一个生成元 $\pi_{\mathfrak{p}}$。在 $S$ 外的主理想上，特征
$$A \mapsto \chi_A\left(u \prod_{\mathfrak{p} \in S} \pi_{\mathfrak{p}}^{v_{\mathfrak{p}}}\right), \qquad u \in \mathcal{O}^\times, \ v_{\mathfrak{p}} \geq 0,$$
属于一个有限族射线特征，它们具有支撑在 $S$ 上的公共模；此族由 $u$ 和剩余类 $v_{\mathfrak{p}} \pmod{6}$ 确定。
