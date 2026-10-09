设 $e_0 = v_p(c) \in \{0, 1\}$，$l = v_p(n)$，$t = e_0 + 3l$，$k = v_p(s)$，$m = v_p(a)$，于是 $v_p(H) = j' = j + 6m$。方程 (7.1) 在 $p$ 处的部分，在恢复其单位因子之前，为

$$C_p(t, k, j') = \sum_{\substack{d \bmod p^k \\ p^{j'} \equiv p^t d \pmod{p^k}}} \chi_p^k(d) g_{\chi_p^t}\left(p^t, \frac{p^{j'-t} d}{p^k}\right). \tag{7.7}$$

在模数为 1 时，此公式中的两个因子均表示 1。其完整求值为

$$C_p(t, k, j') = \begin{cases} 1, & t = k = 0, \\ 1_{j'=0}, & t = 0, k > 0, \\ g_{\chi_p^t}(p^t, p^{j'}), & t > 0, k = 0, \\ \omega_p^{-1} G_1 g_{\chi_p^{t-1}}(p^t, p^{j'-1}), & t > 0, k = 1, j' \geq 1, \\ 0, & \text{否则}. \end{cases} \tag{7.8}$$

对于 $t = 0$ 且 $k > 0$，同余式固定 $d = p^{j'}$ 模 $p^k$，其零延拓特征标非零当且仅当 $j' = 0$。对于第四行，同余式首先迫使 $j' \geq 1$。展开内层 Gauss 和，对 $d$ 模 $p$ 的求和为

$$\sum_{d \bmod p} \chi_p(d) e(-vd/p) = \omega_p^{-1} G_1 \chi_p(v)^{-1} \quad (p \nmid v),$$

这将 Gauss 特征标从 $\chi_p^t$ 变为 $\chi_p^{t-1}$。若 $t > 0$ 且 $k \geq 2$，允许的提升 $d = d_0 + p^{k-1} v$ 不改变 $\chi_p^k(d)$，但其 Gauss 相位为 $e(-yv/p)$，其中 Gauss 变量 $y$ 是一个单位。它们的和为零。这证明了方程 (7.8)，包括 Gauss 特征标为主特征标及零延拓的情形。

对于原始单位，记 $h_p = H/p^{j'}$，$s_p = s/p^k$，$A_p^\circ = A/p^t$。中国剩余定理及代换 $d = h_p (b^* A_p^\circ)^{-1} d'$ 给出额外的单位因子

$$U_p = \chi_p^{k-t}(h_p) \chi_p^t(s_p) \chi_p^{t-k}(A_p^\circ) \chi_p^{t-k}(b^*). \tag{7.9}$$

更明确地说，外层剩余特征标给出 $\chi_p^k(h_p) \chi_p^{-k}(b^* A_p^\circ)$，而中国剩余因子与 Gauss 变量的重新缩放给出 $\chi_p^t(b^* A_p^\circ) \chi_p^{-t}(h_p/s_p)$。它们的乘积即为方程 (7.9)。由于 $h_p = (u/p^j)(a/p^m)^6$，有 $\chi_p(h_p) = \rho$。

在 $b^*$ 的素因子处，有 $(H - b^* Ad)/s \equiv H/s \pmod{b^*}$。完整 Gauss 和中的局部因子为 $q_{b^*} \tau \xi(A) \xi(H/s)$。这里 $\xi(H/s) = \xi(u) \xi(s)$，因为 $\xi(a)^6 = 1$。这消去了方程 (7.4) 中所有显式出现的 $\xi$ 因子。方程 (7.9) 中最后几个因子的乘积消去了 $\chi_s(b^*) \chi_A(b^*)^{-1}$。这种消去是逐系数进行的。对于 $S$ 的任意固定扩张，同样的计算使用相同的射线群 $T$。

剩余配对相位的消去。设 $t_p = v_p(A)$，$k_p = v_p(s)$，在每对不同的素数处的互反律给出

$$R(A, s) \prod_p \chi_p^{-k_p}(s_p) \chi_p^{t_p}(A_p^\circ) = \prod_p R(p, p)^{t_p k_p}.$$

事实上，对于 $p \neq r$，两个方向的符号指数相反，其商为 $R(p, r)$；这消去了双特征标 $R(A, s)$ 中相应的配对。只剩下对角部分。

方程 (4.7) 给出 $\gamma_2(c) = \mu(c) \alpha(c) G(c) / \gamma_1(c)$。中国剩余公式

$$\gamma_1(c) = \prod_{p | c} \gamma_1(p) \prod_{p < r, \, p, r | c} \chi_p(r) \chi_r(p)$$
