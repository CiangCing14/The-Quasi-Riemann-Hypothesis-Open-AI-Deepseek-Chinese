直接地，$M_W(s) = e^s$，并且式 (4.11) 中的加权对数导数在每个紧实条带上一致有限。

证明。 这样的分拆可通过将非负紧支光滑函数（在 $[-1/2, 1/2]$ 上为正）的整数平移进行归一化而得到。设 $\operatorname{supp}\chi \subset [-C, C]$。$W_G(e^k x)$ 的每个对数导数都是 $k + \log x$ 的多项式乘以同一个高斯函数。因此乘积法则给出
$$p_j(w_k) \le C_j (1 + |k|)^j \exp\left(-\tfrac{1}{4}\left((|k| - C)_+\right)^2\right).$$
对任意固定的 $A$，乘以 $e^{A|k|}$ 后该式可和。第一个断言随之成立，分离范数则由引理 4.5 得到。在剖面的对数傅里叶变换中，对圆环进行重标度只插入单位相位 $e^{-ikt}$，因此不改变这些范数；周围多项式的任何实归一化仍然是显式的。在所指出的尾部上，乘以 $Z^B e^{A|k|}$ 后最后一个界取对数至多为 $-c\kappa^2 (\log Z)^2 + O(\log Z)$，其中 $c > 0$ 固定；对高斯尾部求和即得对每个 $M$ 所述的估计。最后，令 $u = \log y$ 并在其高斯积分中配方，得到 $M_W(s) = e^s$。同一个高斯界控制着 $L^1(\mathbb{R})$ 中的每个 $e^{\sigma u}(d/du)^j W_G(e^u)$，且对紧区间中的 $\sigma$ 一致成立。

我们记录伴随这种分离的两类核的显式有限阶连续性陈述。它们不对算术变换作任何断言；该变换必须提供所述的核及其可用的实直线。

引理 4.7（Fourier 与 Mellin 核的有限半范数）。 对于 $\mathbb{R}^d$ 上的 Schwartz 函数 $f$，令
$$s_j(f) = \sum_{|\alpha|,|\beta| \le j} \|x^\alpha \partial^\beta f(x)\|_{L^1(\mathbb{R}^d)}.$$
对每个 $A \ge 0$ 和多指标 $\beta$，普通 Fourier 变换满足
$$\sup_\xi (1 + |\xi|)^A |\partial^\beta \widehat{f}(\xi)| \ll_{A,\beta,d} s_{\lceil A \rceil + |\beta|}(f).$$
对于任何固定的非退化线性 Fourier 配对，同样的结论成立，常数有固定改变。对于写为 $\widehat{f}(\xi) = F(|\xi|^2)$ 的径向变换，任何给定的界
$$\sup_{r \ge 0} (1 + r)^A |(r\partial_r)^j F(r)|$$
因此由 $f$ 的有限多个 Schwartz 半范数控制。

对于 Mellin 断言，设 $m(s)$ 在固定的闭竖直条带上全纯，并假设在其上一致地有 $|m(\sigma + it)| \le C(1 + |t|)^h$，其中 $h \ge 0$ 固定。在该条带中的一条可用直线 $\Re s = \sigma$ 上定义
$$K_W(x) = \frac{1}{2\pi i} \int_{(\sigma)} M_W(-s) m(s) x^{-s}\, ds,$$
其中 $W$ 具有使积分绝对收敛所需的有限加权对数导数，且对数分部积分中的边界项消失。对每个整数 $j \ge 0$，
$$|(x\partial_x)^j K_W(x)| \ll x^{-\sigma} \int_{\mathbb{R}} |M_W(-\sigma - it)| (1 + |t|)^{h+j}\, dt.$$
右端的积分由有限多个积分 $\int y^{-\sigma} |(y\partial_y)^k W(y)|\, dy/y$ 界定，且对固定条带中的 $\sigma$ 一致成立。对于 $W(y) y^{i\omega}$，同样的界至多额外付出一个因子 $(1 + |\omega|)^{h+j}$。乘以固定的圆环截断后，这些结论也界定了 $y \mapsto K_W(Ry)$ 的每个固定对数半范数，并带有因子 $R^{-\sigma}$。
