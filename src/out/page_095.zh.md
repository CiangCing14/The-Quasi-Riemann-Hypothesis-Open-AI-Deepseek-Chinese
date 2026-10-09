对每一行，这样的除数个数至多为 $d_O(k)$。逐行的除数 Cauchy 不等式，随后对各行取正和，因此代价是一个允许的因子 $(KN BL)^\epsilon$。在固定的 $D$-分块中，写 $P = DP'$ 和 $k = Dk'$。无平方因子性给出固定限制 $(D, P') = (D, k') = 1$。定义
$$a_D(P') = a(DP')\mathbf{1}_{(D,P')=1},$$
$$\beta_D(n, b) = \beta(n, b)\chi_D(nb)^3 \chi_D(n)^{-2} \mathbf{1}_{(D,b)=1}.$$
所有这些因子都保留其零点，且 $|\beta_D| \le 1$。分解 $q_P^{-1/2} = q_D^{-1/2} q_{P'}^{-1/2}$ 给出
$$H \ll (KN BL)^\epsilon \sum_D \frac{1}{q_D} \sum_{k'} \sum_{n,b} \beta_D(n, b)\chi_{k'}(nb)^3 \left| \sum_{P'} \frac{a_D(P')}{\sqrt{q_{P'}}} \chi_{P'}(n)^{-2} \mathbf{1}_{(P',b)=1} \right|^2. \quad (14.8)$$
这里 $q_{k'} \ll K/q_D$，$q_{P'} \asymp L/q_D$，并且所有继承的固定限制都被保留。外层的 $D$ 是分裂所允许的无平方因子好除数，所以 $q_D \ll \min(K, L)$。特别地，在单个 $D$-分块内部没有重新引入 $(P', k')$ 掩码。其相消属于已经被逐行 Cauchy 不等式所界定的完整 Möbius 和。

对于固定的 $D$，$\beta_D(n, b)$ 与内层 $P'$-和之积是一个独立于 $k'$ 的任意复系数。以行长 $K/q_D$ 应用公式 (5.27)。使用其记号
$$b = gt^2, \quad c = (n, g), \quad n = cm, \quad g = ch, \quad q_c \asymp C, \quad q_g \asymp G, \quad q_t \asymp T,$$
于是 $B \asymp GT^2$，并写 $c = rc'$ 为其完整的 $c$-掩码除数。理想 $c, m, h$ 两两互素且无平方因子；$g$ 与 $t$ 之间不施加互素性。所引用的化简已经包含了自然的 $k'$-$t$ 限制以及 $k'$-$c$ 掩码的完整 Möbius 展开。它并未在剩余的行与 $c'$ 之间重新引入掩码。

对于一个 $C, G, T$ 块，其正输出代入公式 (14.8) 后至多为
$$(KN BL)^\epsilon \sum_D \frac{1}{q_D} \sum_{q_t \asymp T} \sum_{\substack{r \text{ sf}, (r,S)=1 \\ q_r \ll \min(K/q_D, C)}} \left( \frac{K}{q_D q_r} + \frac{NG}{C^2} \sum_{q_r} \sum_{c', m, h} |\beta_D(rc'm, rc'ht^2)|^2 \right)$$
$$\cdot \left| \sum_{P'} \frac{a_{D,r}(P')}{\sqrt{q_{P'}}} \chi_{P'}(c'm)^{-2} \mathbf{1}_{(P',ht)=1} \right|^2, \quad (14.9)$$
其中正的 $c', m, h$-和保持原始支撑，并且
$$a_{D,r}(P') = a_D(P')\chi_{P'}(r)^{-2}.$$
这里使用的分解，包括所有零点，为
$$\chi_{P'}(rc'm)^{-2} \mathbf{1}_{(P', rc'ht^2)=1} = \chi_{P'}(r)^{-2} \chi_{P'}(c'm)^{-2} \mathbf{1}_{(P', ht)=1}.$$
特征已经提供了在 $r, c', m$ 处缺失的零点。因此 $r$-因子仅依赖于元组，包括当 $(P', r) \neq 1$ 时的零点。固定的 $D$-相位保留在 $\beta_D$ 内部直到这个正界。二次化简已经在筛选 $m, h$ 的好乘积之前分离出它们有限的多个无平方因子 $S$-部分；公式 (14.9) 中的 $m, h$ 是原始理想。

我们现在可以丢弃 $|\beta_D|^2 \le 1$。对于固定的 $h, t, D, r$，$P'$-系数独立于 $j = c'm$，并且理想计数给出
$$\sum_{P'} \frac{|a_{D,r}(P')|^2 \mathbf{1}_{(P', ht)=1}}{q_{P'}} \ll_\epsilon (KN BL)^\epsilon.$$
