在下面的乘积中，不强制两个变量互素：

$$D(s,\Psi)=\sum_{\substack{n\equiv 1\,(3)\\ (n,E)=1}}^{sf}\gamma_2(n)\bar{\alpha}(n)\Psi(n)q_n^{-s},\qquad L_0(s,\Psi)=\sum_{\substack{b\equiv 1\,(3)\\ (b,E)=1}}\bar{\alpha}(b)^3\Psi(b)^3 q_b^{-3s+1/2},\qquad T(s,\Psi)=L_0(s,\Psi)D(s,\Psi).$$

两个级数及其乘积在 $\Re s > 1$ 时绝对收敛。
   设 $X > 0$。假设 $V \in C^\infty(0, \infty)$，且对每个 $C > 0$ 和每个整数 $j \geq 0$，当 $x \to 0$ 时 $(x\partial_x)^j V(x)$ 为 $O_{C,j}(x^C)$，当 $x \to \infty$ 时为 $O_{C,j}(x^{-C})$。定义

$$\hat{V}(t)=\int_0^\infty V(x)x^t\,\frac{dx}{x}.$$

待变换的光滑化表达式是完全和

$$\frac{1}{2\pi i}\int_{(a)}\hat{V}(s-1/2)X^{s-1/2}T(s,\Psi)\,ds=\sum_{\substack{n\ \text{sf},\,b\\ n,b\equiv 1\,(3)\\ (nb,E)=1}}\frac{\gamma_2(n)\alpha(nb^3)\Psi(nb^3)}{\sqrt{q_n q_b}}\,V\!\left(\frac{q_n q_b}{X}\right),\qquad a > 1.$$

此等式由绝对收敛和 Mellin 反演得到。特征作用于整个指标 $nb^3$，其零值予以保留；$n$ 与 $b$ 可以共享素因子。
   反射检验函数定义为

$$K=\frac{(2\pi)^4}{27},\qquad R(t)=\prod_{\pm}\frac{\Gamma(1+t\pm 1/6)}{\Gamma(1-t\pm 1/6)},\qquad V^{\sharp}(x)=\frac{1}{2\pi i}\int_{(\sigma)}\hat{V}(-t)R(t)(Kx)^{-t}\,dt\qquad(\sigma\ge 0).$$

定义 $V^\sharp$ 的积分绝对收敛，且与 $\sigma \geq 0$ 无关。
   乘积 $T$ 具有整函数延拓。在每条固定的竖直带内它具有多项式增长，其中的常数可依赖于 $L$、$\Psi_0$、$P$、$(j_p)$ 以及该带。存在唯一一组固定的尖点系数函数三元组，从 $\lambda^{-4}\mathfrak{O} \setminus \{0\}$ 到 $\mathbb{C}$，由证明中的 theta 展开构造。对于算术数据、尺度和检验剖面的所有选择，都使用同一个三元组。对于上述每个固定的算术选择，存在一个有限项族，按 (1) 中的方式编号，与 $X$、$V$ 以及围道参数 $a > 1$ 无关。在每一项中，$d$ 取自这个三元组，$\vartheta$ 是 $\mathfrak{O}$ 的加法特征模一个仅依赖于 $L$ 的固定模数；它们的扇形依赖关系恰好是 (3) 中所述，其余数据具有性质 (1)–(3)。对于这些项以及每个 $a > 1$，恒等式为

$$\frac{1}{2\pi i}\int_{(a)}\hat{V}(s-1/2)X^{s-1/2}T(s,\Psi)\,ds=\sum_{\text{terms}}\zeta\sum_{0\neq\mu\in\lambda^{-4}\mathfrak{O}}\frac{d(\mu)\alpha(\mu)\vartheta(\lambda^4\mu)}{\sqrt{q_\mu}}\prod_{p\ \text{active}}B_p(\lambda^4\mu)\,V^{\sharp}\!\left(\frac{q_\mu X}{q_c^2}\right). \tag{5.1}$$

每个内和都绝对收敛。这些项具有以下确切性质。
