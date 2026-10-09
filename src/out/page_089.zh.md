本小节中的所有字符均采用第 4 节所指定的零延拓，并令
$v_p(0) = +\infty$。

引理 13.2（素数幂 Fourier 和）。对 $P = q^p$ 及任意整数 $a \ge 1$，

$$
|G(p^a, k)| = P^{(a-1)/2} \mathbf{1}_{v_p(k)=a-1}, \quad 6 \nmid a,
$$

$$
G(p^a, k) = P^{a/2} \mathbf{1}_{p^a \mid k} - P^{a/2-1} \mathbf{1}_{p^{a-1} \mid k}, \quad 6 \mid a. \tag{13.5}
$$

证明。将模 $p^a$ 的一个剩余类写成 $x_0 + py$，其中 $x_0 \bmod p$，$y \bmod p^{a-1}$。对 $y$ 的求和除非 $p^{a-1} \mid k$ 否则为零，而在后一情形下等于 $P^{a-1}$。在后一情形中写 $k = p^{a-1} k_0$。剩余的归一化和为

$$
P^{a/2-1} \sum_{x_0 \bmod p} \chi_p(x_0)^a e(k_0 x_0/p).
$$

若 $6 \nmid a$，其内和当 $p \mid k_0$ 时为零，否则绝对值为 $\sqrt{P}$。若 $6 \mid a$，内和为单位元上的加性特征之和，即 $P \mathbf{1}_{p \mid k_0} - 1$。这正是陈述中的两种情形。

引理 13.3（完全相关与公因子）。对 $S$ 之外的本原模 $u, v$ 及 $j \in O$，令

$$
F(u, v; j) = \sum_{\substack{x \bmod u,\ y \bmod v \\ vx - uy \equiv j \pmod{uv}}} \chi_u(x) \chi_v(y). \tag{13.6}
$$

则

$$
F(u, v; j) = \frac{1}{\sqrt{q_u q_v}} \sum_{h \bmod uv} G(u, h) G(v, h) e(-jh/(uv)).
$$

在零频率处，除非 $u = v$，否则 $F(u, v; 0) = 0$，且 $F(u, u; 0) = \varphi(u)$，其中 $\varphi(u)$ 是模 $u$ 的单位元个数。

令 $C = (u, v)$ 并写 $u = Cn_1$，$v = Cn_2$，其中 $(n_1, n_2) = 1$。则除非 $C \mid j$，否则 $F(u, v; j) = 0$。对 $j = Ck$，

$$
F(Cn_1, Cn_2; Ck) = \chi_{n_1}(k) \chi_{n_2}(-k) R(n_1, n_2) L_C(n_1, n_2; k),
$$

$$
L_C(n_1, n_2; k) = \sum_{\substack{x, y \bmod C \\ n_2 x - n_1 y \equiv k \pmod{C}}} \chi_C(x) \chi_C(y) = \prod_{p^c \parallel C} L_{p^c}. \tag{13.7}
$$

对 $P = q^p$ 及 $p \nmid n_1 n_2$，局部因子为

$$
L_{p^c} = \begin{cases}
P - 1, & p \mid k, \\
P^{c-1} \chi_p(n_1/n_2) - 1, & p \nmid k,\ 6 \nmid c, \tag{13.8} \\
P - 2, & p \nmid k,\ 6 \mid c.
\end{cases}
$$

若 $p$ 恰好整除 $n_1, n_2$ 之一，则局部因子为 $P^{c-1}(P-1) \mathbf{1}_{6 \mid c} \mathbf{1}_{p \nmid k}$。在真正的剩余轨迹 $(n_1, n_2) = 1$ 上，$L_C$ 表示式 (13.7) 中的同余和。当 $L_C$ 用于所有剩余对时，它转而表示这些局部公式的人为乘积延拓，其中若 $p \mid (n_1, n_2)$ 则局部值定义为零。在真正的剩余轨迹之外，这并非原来的同余和。真正的函数与此人为延拓均满足 $|L_C| \le q_C$，且该延拓在每个剩余列中关于 $\operatorname{rad} C$ 周期。

证明。将两个 Gauss 和代入所示的 Fourier 变换得到

$$
\frac{1}{q_u q_v} \sum_{x \bmod u, y \bmod v} \chi_u(x) \chi_v(y) \sum_{h \bmod uv} e\left(h(vx - uy - j)/(uv)\right).
$$
