固定有限阿贝尔射线群上的每个函数都有其特征的有限傅里叶展开。例如，若 $\phi : T \to \mathbb{C}$，则
$$\phi(v) = \sum_{\theta \in \widehat{T}} a_\theta \theta(v), \qquad a_\theta = \frac{1}{|T|} \sum_{u \in T} \phi(u) \overline{\theta(u)}.$$

Parseval 和 Cauchy–Schwarz 给出 $\sum_\theta |a_\theta|$ 被 $|T|^{1/2} \max_T |\phi|$ 控制。将同样的陈述应用于 $T \times T$，可将 $R(a, b)$ 分解为特征之积的有限和。这些展开在非互素的 primary 对处仍然有效，因为那里的 $R$ 是固定射线双特征，而不是符号商。例如，对于好的素数 $p$ 以及 $S$ 之外的每个 primary $n$，

$$\chi_n(p) \chi_p(n) = R(p, n) 1_{(n, p) = 1}.$$

在互素对上这就是六次互反律，而在其余对上两边都为零。因此，移动局部特征的抵消既可能留下互素性指示函数，也可能留下固定射线相位；二者都不可丢弃。

4.3 光滑范数剖面
以下约定使特征多项式估计中的光滑依赖性成为定量的。它们将固定测试函数的导数与谱高度的幂次区分开来。当傅里叶尾部只在高度范围选定之后才被移除时，这一区分是必要的。

对于 $(0, \infty)^d$ 上具有固定紧集 $\Omega \subset \mathbb{R}^d$ 中对数支撑的剖面 $w$，令
$$w_{\log}(u) = w(e^{u_1}, \ldots, e^{u_d}), \qquad p_j(w) = \sum_{|\alpha| \leq j} \sup_{u \in \mathbb{R}^d} |\partial^\alpha w_{\log}(u)|.$$

我们始终约定 $w_{\log}$ 光滑且支撑在 $\Omega$ 中。定义
$$\widehat{w}(t) = \int_{\mathbb{R}^d} w_{\log}(u) e^{-i t \cdot u} \, du, \qquad \|w\|_{J, \mathrm{sep}} = \int_{\mathbb{R}^d} |\widehat{w}(t)| (1 + |t|)^J \, dt.$$

对于固定的有限元组 $w = (w_1, \ldots, w_r)$，其分量可能具有不同的固定维数，我们使用 $p_j(w) = 1 + \sum_{i=1}^r p_j(w_i)$。

引理 4.5（光滑演算）。对整数 $J \geq 0$，

$$\|w\|_{J, \mathrm{sep}} \ll_{J, d, \Omega} p_{J + d + 2}(w).$$

对数傅里叶反演可分离任意固定的范数单项式。更确切地说，若 $x_j = c_j \prod_{\ell=1}^r y_\ell^{a_{j\ell}}$，其中 $c_j, y_\ell > 0$ 且 $a_{j\ell}$ 为固定实数指数，则
$$w(x_1, \ldots, x_d) = \frac{1}{(2\pi)^d} \int_{\mathbb{R}^d} \widehat{w}(t) \prod_j c_j^{i t_j} \prod_\ell y_\ell^{i \sum_j a_{j\ell} t_j} \, dt.$$

若该公式中的系数测度为一组行所共有，则 Minkowski 不等式将任何分离的行 $\ell^2$ 界通过积分传递，只要分离界的高度增长至多为 $(1 + |t|)^J$，即可使用 $\|w\|_{J, \mathrm{sep}}$。

对于单位盒 $I \subset \mathbb{R}^d$ 以及 $I + [-1, 1]^d$ 上的光滑标量函数 $F$，
$$\sup_I |F|^2 \ll_d \sum_{\alpha \in \{0, 1\}^d} \int_{I + [-1, 1]^d} |\partial^\alpha F|^2. \qquad (4.9)$$

因此，在相应的导数界之下，多项式范围内逐行选择尺度所付出的代价是 $\log Z$ 的幂次，而逐行选择绝对值至多为 $T_1$ 的范数扭转高度所付出的代价是 $1 + T_1$ 的固定幂次。
