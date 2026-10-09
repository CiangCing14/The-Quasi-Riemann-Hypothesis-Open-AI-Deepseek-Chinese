$e(-zy)$。对于 $K > 0$，
$$
\sum_{k \in \mathcal{O}} \psi(k) \mathbf{1}(k, R) = \frac{1}{\Phi(qk/K)} \sum_{d \mid \operatorname{rad} R} \frac{K\gamma(\psi; m)}{\sqrt{qm}} \frac{\mu(d)\psi(d)}{qd} \sum_{h \in \mathcal{O}} \bar{\psi}(h) F_\Phi\!\left(\frac{Kqh}{qd\, qm}\right), \tag{17.8}
$$
其中 $\gamma(\psi; m) = qm^{-1/2} \sum_{x \bmod m} \psi(x) e(x/m)$。对于非主本原特征，$|\gamma(\psi; m)| = 1$，且 $h = 0$ 项为零。对于本原主特征，约定为 $m = 1$，$\gamma(1; 1) = 1$，$\psi(h) = 1$，包括在 $h = 0$ 处。

证明。将掩码展开为 $\sum_{d \mid \operatorname{rad} R,\, d \mid k} \mu(d)$，并写 $k = dk'$。尺度变为 $K/qd$，特征贡献 $\psi(d)$。模 $m$ 的剩余类上的 Poisson 求和具有前因子 $K/(qd\, qm)$。其有限变换为
$$
\sum_{x \bmod m} \psi(x) e(hx/m) = \sqrt{qm}\, \gamma(\psi; m) \bar{\psi}(h).
$$
对于单位 $h$，这由变量替换得到。对于非单位 $h$，由本原性知变换为零；对于 $m = 1$，适用所述的主特征约定。这证明了公式 (17.8)。对于非主本原特征，有限 Parseval 等式给出 $\sum_h \left|\sum_x \psi(x) e(hx/m)\right|^2 = qm \sum_x |\psi(x)|^2$。记 $\varphi(m) = |(\mathcal{O}/m)^\times|$，则有 $\varphi(m)$ 个单位 $h$，其绝对值均为 $\sqrt{qm}\,|\gamma(\psi; m)|$，且 $\sum_x |\psi(x)|^2 = \varphi(m)$。因此 $|\gamma(\psi; m)| = 1$。

固定的射线限制首先可以展开为有限多个特征。然后将每个特征替换为其本原诱导特征，被移除的局部零延拓保留在 $R$ 中；同一公式逐项适用。对于主模，非零频率的绝对和为 $O_\Phi(d_{\mathcal{O}}(\operatorname{rad} R))$。事实上，对于所有 $A > 0$，
$$
A \sum_{h \neq 0} |F_\Phi(Aqh)| \ll_\Phi 1.
$$
当 $A \leq 1$ 时由格点计数证明，当 $A \geq 1$ 时由 Schwartz 衰减证明。将此界与 $A = K/qd$ 一起对 $d$ 求和。在以下每次使用中，相关的非空行尺度均有 $K \geq 1$，因此这也是 $O(KZ^\epsilon)$。当在分离非主和时添加或移除主非零频率时，它们将携带与该和相同的外行掩码；其绝对贡献不超过此完整主界。

17.5 典范约化及其归纳

我们现在证明引理 17.2。反射能量处理短完成；剩余块经过两次 Poisson 变换以产生具有较短行的容许典范和。

引理 17.2 的证明。解析选择的顺序由第 17.3 节的推论 17.4 组织。其带指标的结论将分别用于每个正 Cauchy 侧和；下面的证明验证所需的公共系数测度、固定范数损失和有限深度。

在每个节点，每个联合 $(f, k)$ Hilbert 空间使用当前标签测度 $w(f)$，并且该因子在每个父 $f$-和中恰好保留一次，直到公式 (17.32) 移除旧标签。

在每个节点保持参数 $N, V, M$ 固定，并记

$$
F = N + V, \qquad Q = \log_Z qr\rho.
$$
