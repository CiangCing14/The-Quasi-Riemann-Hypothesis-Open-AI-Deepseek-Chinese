9     六次筛法的行计数

零检测器为底仓（floor bin）之上的每一行提供了一个大的逆多项式。我们现在把这个下界转化为物理行数的计数。我们首先在原始约定（primary convention）下证明所需的平方自由六次大筛法，使用 Blomer、Goldmakher 和 Louvel [4, 第3节] 的范数递归方法。然后我们固定物理行中素值至少为二的部分，并对它的平方自由因子应用筛法。固定部分的大小也给出了行数的独立上界；两个界中较好的一个给出所需的指数。

9.1   原始约定下的六次大筛法

我们继续使用固定的有限素理想集合 $S$，它包含 6 以上的素数和所有固定导子素数。下一个引理中的所有理想指标都与 $S$ 互素，并用它们的原始生成元表示。特别地，“平方自由”指的是 $\mathcal{O} = \mathbb{Z}[\omega]$ 的理想，而不是它们的有理范数。

引理 9.1（六次大筛法）。设 $K, D \geq 1$，设 $\varsigma \in \{-1, 1\}$，并设 $(c_n)$ 是任意以 $S$ 之外的平方自由理想为指标的复数序列。该序列独立于行 $k$ 固定。对每个 $\epsilon > 0$，

$$
\sum_{qk \leq K} \sum_{\substack{\mathfrak{n}\ \text{sf} \\ q\mathfrak{n} \leq D}} \left| \sum_{\mathfrak{n}\ \text{sf}} c_{\mathfrak{n}} \chi_{\mathfrak{n}}(k)^{\varsigma} \right|^2 \ll_{S,\epsilon} (KD)^{\epsilon} \left( K + D + (KD)^{2/3} \right) \sum_{\substack{\mathfrak{n}\ \text{sf} \\ q\mathfrak{n} \leq D}} |c_{\mathfrak{n}}|^2. \tag{9.1}
$$

此公式中的每个符号在非单位元上取原来的零值。允许对行集合作固定限制。允许对系数支集作固定限制，方法是用零延拓该系数序列。这样的限制可以依赖于在行求和之前固定的对象，但系数在其他方面不得依赖于 $k$。

证明。我们遵循 Blomer、Goldmakher 和 Louvel [4, 第3节] 的高阶大筛法递归，对当前的原始规范化给出局部验证。在有限傅里叶计算中，各个剩余特征作用于元素；它们的单位平凡商是我们应用 Poisson 求和法的理想上的特征。

对于好的理想 $\mathfrak{a}, \mathfrak{b}$，用它们的原始生成元表示，令

$$
F_{\mathfrak{b}}(\mathfrak{a}) = \chi_{\mathfrak{a}}(\mathfrak{b}), \qquad J = \{1, 2, 4\}.
$$

这使用了原来的零延拓符号，当 $\mathfrak{a}$ 非平方自由时也是如此。它对 $\mathfrak{a}$ 和 $\mathfrak{b}$ 都是乘性的。在下面的每个幂中，包括六的倍数，非单位元仍然取值为零。对 $M > 0$ 令

$$
I_M = \{\mathfrak{a}\ \text{好的} : M < q_{\mathfrak{a}} \leq 2M\}, \qquad A_M = \{\mathfrak{a} \in I_M : \mathfrak{a}\ \text{平方自由}\}.
$$

对于支集在 $A_N$ 上的序列，记 $\|\lambda\|_2^2 = \sum_{\mathfrak{b} \in A_N} |\lambda_{\mathfrak{b}}|^2$，并定义

$$
D_j(M, N) = \sup_{\|\lambda\|_2 = 1} \sum_{\mathfrak{a} \in A_M} \left| \sum_{\mathfrak{b} \in A_N} \lambda_{\mathfrak{b}} F_{\mathfrak{b}}(\mathfrak{a})^j \right|^2,
$$

$$
E_j(M, N) = \sup_{\|\lambda\|_2 = 1} \sum_{\mathfrak{a} \in I_M} \left| \sum_{\mathfrak{b} \in A_N} \lambda_{\mathfrak{b}} F_{\mathfrak{b}}(\mathfrak{a})^j \right|^2.
$$
