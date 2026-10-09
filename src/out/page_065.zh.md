最大值可以限制在非空范围上。这是 [4, Lemmas 3.2–3.3] 中 gcd 步骤与 Poisson 步骤的结合；这里用到的每个序列在其范数和中都是公共的，且 $S$ 保持固定。

初始界与幂界。行的包含关系给出 $D_j \le E_j$。Hilbert 空间对偶性与六次互反律，按有限 $t$-类拆分一个矩阵变量，给出

$$D_j(M, N) \ll_S D_j(N, M). \tag{9.9}$$

各相位取单位值，且两个方向上的非互素元素均为零。我们还有初始估计

$$D_j(M, N) \ll_S M^2 + N \qquad (M, N \ge 1). \tag{9.10}$$

事实上，对于无平方因子的行 $a$，有限 Fourier 反演在每个 $b$ 上（包括非单位元）给出

$$\chi_a(b)^j = \frac{1}{\sqrt{q_a}\,\gamma_{-j}(a)} \sum_{x \bmod a} \chi_a(x)^j e(xb/a).$$

Cauchy 代价至多 $\#(O/(a))^\times / q_a \le 1$。来自 $a \in A_M$ 的既约分数 $x/a$ 在模 $O$ 下互不相同，且彼此间隔至少 $1/(2M)$：$x/a - y/c - h$ 的非零分子绝对值至少为 1，而 $|ac| \le 2M$；模 $O$ 相等迫使主分母与剩余相同。Lemma 6.1 的对偶，在系数生成元位于球 $q_b \le 2N$ 内时，证明了 (9.10)。

我们需要下述近单调性，它也被用于 [13, Lemma 4.4 and Remark 5] 与 [4, Lemma 3.1] 的大筛递推：

$$D_j(M_1, N) \ll_S D_j(M_2, N) \quad \text{若 } M_2 \ge C M_1 \log(2 M_1 N), \quad M_1, M_2, N \ge 1. \tag{9.11}$$

下面给出直接验证。若范数为零则结论显然。否则为 $D_j(M_1, N)$ 选取一个最大化单位系数向量，并在 $3M_1/2$ 处拆分行壳；其中一部分至少承载其一半质量。令 $L = M_2/M_1$。对第一部分使用范数位于 $(L, 4L/3]$ 内的好素理想，对第二部分使用范数位于 $(2L/3, L]$ 内的。于是当 $p \nmid a$ 时 $ap \in A_{M_2}$。固定域的素理想定理提供 $P \gg_S L/\log L$ 个这样的素数。范数至多为 $2x$ 的理想至多包含其中 $d_x = \log(2x)/\log(2L/3)$ 个。对于 $S_a(v) = \sum_b v_b F_b(a)^j$ 且 $p \nmid a$，乘性给出

$$S_a(\lambda) = S_{ap}\bigl(\lambda_b F_b(p)^j\bigr)_b + S_a\bigl(\lambda_b \mathbf{1}_{p \mid b}\bigr)_b.$$

第一个系数在 $p \mid b$ 处为零，否则抵消 $p$ 处的因子。对所选的行与素数平方并求和，得到

$$\frac{P - d_{M_1}}{2} D_j(M_1, N) \le 2P D_j(M_2, N) + 2d_N D_j(M_1, N).$$

对于所述阈值，当 $C$ 充分大时，$d_{M_1} + 4d_N \le P/2$，从而证明了 (9.11)。

最后我们给出 [4, Lemmas 3.4–3.5] 的幂分解与递推。假设对 $j \in J$ 同时成立：对每个正损失

$$D_j(M, N) \ll_{S,\varepsilon} (MN)^\varepsilon \{M^\alpha + N + (MN)^{2/3}\}, \qquad \alpha > 4/3, \tag{9.12}$$

对 $M, N \ge 1$ 成立；单位壳直接满足相同的界。初始估计以 $\alpha = 2$ 给出此式。将一个好的求值理想唯一地写成

$$a = a_1 a_2^2 a_3^3 a_4^4 a_5^5 a_6^6,$$

65
