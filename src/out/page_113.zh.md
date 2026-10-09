它还给出了共享留数估计所需的绝对主校正。确实，这里
$Gp = Hp Bp = O(1)$，而未选取乘积由第二区域版本的方程 (16.5) 有一个有界的正控制函数。因此，对每个环形槽进行理想计数，在第二欧拉区域的每个固定实盒上，并对所有虚部一致地有
$$
|H_{\eta,1,Z}(x,w,z)| \le \sum_{\substack{(p_i)\in \prod_i P_i(Z)}} \frac{|W_i(q_{p_i}/P_i)| q_{p_i}^{z_{\mathrm{ir}}-1} |G_{p_i}|}{Q} \prod_{\substack{p\in S \\ p\in\{p_1,\dots,p_K\}}} |H_p| \ll \prod_i P_i^{z_{\mathrm{ir}}} = Z^{\ell z_{\mathrm{ir}}}.
\tag{16.14}
$$
这里仅使用单独的主行下界来获得局部近似；它并不断言一般 $H_p$ 的非消失性。

16.3 剩余围道的绝对界

共享解析估计所用的每条围道上并不都能使用动态分解。下面的界则在取绝对值之前保留每个选取的因子 $G_p$。

引理 16.2（绝对局部元组界）。设 $Z \ge 2$，并设 $u$ 是一个非零六次无幂行，满足 $(u,S)=1$ 且 $q_u \asymp U \ge 1$，其中比较常数固定。保留第 12 节中固定的物理槽系统。以下界对所有虚部和单位相位一致成立。

1. 在
$$
x_r = \beta_{*}+ e, \qquad w_r = 1/2, \qquad z_r = 17/50, \qquad 0 < e \le 10^{-3}
$$
上，对于选取的素数 $p \nmid u$ 有 $G_p = O(1)$，对于选取的素数 $p \mid u$ 有 $G_p \ll Q^{1/2}$。

2. 对每个固定的 $z_\infty > 2$，在
$$
x_r = w_r = 2, \qquad z_r = z_\infty
$$
上，对每个选取的素数有 $G_p = O_{z_\infty}(1)$。

在任一种情形下，对完整选取元组的正和满足
$$
\sum_{\substack{(p_i)\in \prod_i P_i(Z)}} \frac{|W_i(q_{p_i}/P_i)| q_{p_i}^{z_{\mathrm{ir}}-1} |G_{p_i}|}{Q} \prod_{\substack{p\in S \\ p\in\{p_1,\dots,p_K\}}} |H_p| \ll_\epsilon U^\epsilon \prod_i P_i^{z_{\mathrm{ir}}}.
\tag{16.15}
$$
其中的常数可以依赖于固定数据、$e$，以及在第二种情形下的 $z_\infty$，但不依赖于 $Z$、$u$ 或虚部。这些估计在 $P_p$ 或 $H_p$ 的零点处仍然有效。

证明。两组直线都位于第一欧拉区域，$\epsilon_0 = 3/8$。其逐素数缺陷估计给出 $H_p = O(1)$，而方程 (16.5) 将所有未选取因子的正乘积界为 $O_\epsilon(U^\epsilon)$。

先考虑 $x_r = \beta_{*}+ e$、$w_r = 1/2$、$z_r = 17/50$。对选取的 $p \nmid u$，方程 (16.8) 给出
$$
|G_p + \chi_p(u) H_p| \ll Q^{-x_r} + Q^{-6z_r} + Q^{4-5x_r-6z_r} + Q^{1-w_r-6z_r}.
$$
这四个指数分别至多为 $-7/8-e$、$-51/25$、$-483/200-5e$、$-77/50$。因此，在 $u$ 之外有 $G_p = O(1)$，无需除以 $H_p$。

对选取的 $p \mid u$，有 $W = D = 0$ 且 $E_p = P_p^*$。方程 (16.2) 变为
$$
G_p = \eta(p) Q^x (1-V) E_p - Q^{-w} H_p.
$$
