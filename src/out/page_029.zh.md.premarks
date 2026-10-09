由 $e$ 给出的特征配对在 $O/(p)$ 上非退化。对 Gauss 和作变量替换，并利用非平凡乘性特征的正交性，得到

$$
C_{p,j}(h) =
\begin{cases}
q_p^{-1/2}\tau_{p,j}^{-}\,\chi_p(h)^{-j}, & j \neq 0,\ h \neq 0, \\
0, & j \neq 0,\ h = 0, \\
-q_p^{-1}, & j = 0,\ h \neq 0, \\
1 - q_p^{-1}, & j = 0,\ h = 0.
\end{cases}
\tag{5.11}
$$

这里及以下 $h = 0$ 均表示 $h \equiv 0 \pmod p$。$\chi_p$ 的每个非平凡幂在素数 $p$ 模下都是本原的，因此通常的有限域 Gauss 和恒等式给出 $|\tau_{p,m}^{\pm}| = 1$。

现在对 $O/(L)$ 以及每个 $O/(p)$ 作 Fourier 反演，得到

$$
\phi(x)\prod_p \chi_p(x)^{j_p} = \sum_h C(h)\, e\!\left(x\left(h_0/L + \sum_p h_p/p\right)\right), \quad C(h) = \hat{\phi}(h_0)\prod_p C_{p,j}(h_p).
$$

这里用到了每一个加法频率，包括非单位的 $h_0$ 和零局部频率。我们没有引用 [8, Lemma 5.2 and Corollary 5.1] 中的扭公式，因为其单位 Fourier 支撑假设对这些掩码未必成立。以该乘子作用于其无穷系数 $x = \lambda^3\mu \in O$ 的 theta 函数是如下有限和

$$
F(z, v) = \sum_h C(h)\bar{\theta}(z + z_h, v), \quad z_h = \lambda^2\left(h_0/L + \sum_p h_p/p\right).
\tag{5.12}
$$

对于孤立的无穷指数 $x = nb^3$，$\phi$ 的分段定义首先丢弃所有满足 $(nb, E) \neq 1$ 的项。这是对整个完备指数的一个掩码：$(nb^3, E) = 1$ 当且仅当 $n$ 与 $b$ 都是 $E$-单位。仅在这个剩余的区域内，我们才使用完全乘性，包括 $\chi_b(\lambda)^6 = 1$，来写出

$$
\phi(nb^3)\prod_p \chi_p(nb^3)^{j_p} = \chi_n(\lambda)^2\,\Psi(n)\Psi(b)^3 \qquad ((nb, E) = 1).
$$

当 $n, b$ 共享一个变动的素数时，此式仍然成立，因为相应的局部幂保持其零值，包括 $j_p = 0$ 的情形。对于被丢弃的项，完备系数直接定义为零；那里不计算 $\chi_n(\lambda)$ 的任何值。将保留区域上的 Equations (5.9) 与 (5.10) 结合，即可将直接 Mellin 级数与乘积 $T$ 等同起来。对偶系数函数 $d_H$ 在 Equation (5.2) 中保留完整的源支撑；它们上面没有放置 $S$-掩码。

固定 $h_0$，并恰好当 $h_p \neq 0$ 时称 $p$ 为活跃的。Equation (5.11) 迫使所有满足 $j_p \neq 0$ 的素数都是活跃的。对每个 $h_0 \bmod L$ 各选取一次代表元以及一个约化表达式 $\lambda^2 h_0/L = a_F/c_F$。将分子与分母同乘一个单位，若 $\lambda \mid c_F$ 则将分子规范化为 $1 \pmod 3$，否则将分母规范化为 $1 \pmod 3$。由于每个活跃素数都是主要的，这个单位仅依赖于 $h_0$。对于 $r = \prod_{p\ \text{active}} p$，Equation (5.12) 给出

$$
z_h = \frac{a}{c}, \quad c = c_F r, \quad a = a_F r + \lambda^2 c_F \sum_{p \mid r} (r/p)h_p.
\tag{5.13}
$$

在整除 $c_F$ 的素数处，分子同余于 $a_F r$ 且是一个单位。在 $p \mid r$ 处，它同余于 $\lambda^2 c_F (r/p)h_p$，同样是一个单位。因此这个分数是约化的，即使 $h_0$ 是模 $L$ 的非单位时也是如此。允许空乘积 $r = 1$。将任何提升替换为另一个，会使 $z_h$ 改变 $\lambda^2 O = 3O$ 中的一个元素，即 $\theta$ 的一个周期。

尖点矩阵及其乘子的选取。接下来的构造对刚才得到的每个约化尖点分数确定自守乘子与反射加法相位。令
