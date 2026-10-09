引理 5.5（完备化指标的二次归约）。设 $K, N, B \ge 1$。设 $I$ 为任意一组无平方因子的本原好理想 $k$，满足 $q_k \ll K$。设 $n$ 遍历无平方因子本原理想且 $q_n \asymp N$，设 $b$ 遍历本原理想且 $q_b \asymp B$。理想 $n, b$ 可以含有 $S$ 中除 $\lambda$ 以外的素数。设 $\beta(n, b)$ 为与 $k$ 无关的任意复系数。允许对 $I$ 的固定限制以及对 $(n, b)$-支集的固定限制。
将 $b = gt^2$ 唯一地写出，其中 $g$ 无平方因子，并令 $c = (n, g)$，$n = cm$，$g = ch$。于是 $c, m, h$ 两两互素且无平方因子。固定一组二进范围

$$q_c \asymp C, \qquad q_g \asymp G, \qquad q_t \asymp T, \qquad B \asymp GT^2,$$

其中所有比较常数均固定。设 $Q_{C,G,T}(\beta)$ 为对 $k \in I$ 求和，取限制于这组范围的 $(n, b)$-和的绝对值的平方，其被加项为 $\beta(n, b)\chi_k(nb)^3$。对于无平方因子的好理想 $r$ 和固定的 $t$，设 $D_r(t)$ 为三元组 $(c', m, h)$ 的集合，使得

$$c = rc', \qquad n = rc'm, \qquad b = rc'ht^2$$

属于原始支集并属于这些范围，且满足所述 $c, m, h$ 的无平方因子性与两两互素性。则

$$Q_{C,G,T}(\beta) \ll_\epsilon (KNB)^\epsilon T^\epsilon \sum_{q_t \asymp T} \sum_{\substack{r\ \mathrm{sf},\ (r,S)=1 \\ q_r \ll \min(K,C)}} \left( \frac{K}{q_r} + \frac{NG}{C^2} \right) \frac{C}{q_r} \sum_{(c',m,h) \in D_r(t)} |\beta(rc'm, rc'ht^2)|^2. \tag{5.27}$$

空的商范围贡献为零；所有有界范围，包括单位理想，都通过固定的比较常数包含在内。允许固定的射线扇区和有界的行标量。特别地，若 $|\beta(n, b)| \le 1$，则

$$\sum_{k \in I} \left| \sum_{n,b} \beta(n, b)\chi_k(nb)^3 \right|^2 \ll_\epsilon (KNB)^\epsilon (K + NB)NB. \tag{5.28}$$

常数可以依赖于固定的支集比较和 $S$，但对系数和允许的支集限制是一致成立的。
证明。分解式 $b = gt^2$ 允许 $g$ 与 $t$ 共享素数。由于 $nb = c^2 mht^2$，零约定给出精确恒等式

$$\chi_k(nb)^3 = \chi_k(mh)^3 \mathbf{1}_{(k,ct)=1}. \tag{5.29}$$

确实，在所显示的二次特征下，一个平方具有六次幂；它在单位上取值为一，在碰撞处取值为零。因此当 $n$ 或 $g$ 与 $t$ 共享素数时该恒等式同样成立。
对于所选范围，$t$ 有 $O(T)$ 种可能。Hilbert 空间 Cauchy 不等式给出

$$\left| \sum_{q_t \asymp T} F_t \right|^2 \ll T \sum_{q_t \asymp T} \|F_t\|_2^2.$$

在正和式中固定 $t$。条件 $(k, t) = 1$ 现在是一个固定的行限制。对于剩余的条件使用完全恒等式

$$\mathbf{1}_{(k,c)=1} = \sum_{r | (k,c)} \mu(r).$$

对于每个 $k$，可能的 $r$ 的数量至多为 $d^{O}(k)$。逐行 Cauchy 不等式后对 $k$ 求和耗费 $(KNB)^\epsilon$，并给出关于固定的无平方因子好 $r$ 的正和。写 $k = rk'$ 并
