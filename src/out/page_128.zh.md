保留自立方体起的四次方标签。唯一地写 $b_1 b_2 = q_2 s$，其中 $s$ 无平方因子，并定义
$$J_2 = \prod_{\substack{\pi_p =0\\ a_{1p}=a_{2p}=1}} p,\quad J = sJ_2,\quad q = J_2 q_0.$$
$J_2$ 的每个素数在 $b_1 b_2$ 中的赋值都是正偶数，故 $J_2 \mid q$。理想 $s, J_2$ 互素且无平方因子；因此 $J$ 无平方因子。设 $j \ge 0$ 为 $J$ 的中心，并令
$$\widehat{s} = \log_{\mathbb{Z}} \frac{q}{s},\quad \widehat{j_2} = \log_{\mathbb{Z}} \frac{q}{J_2},\quad \widehat{j} = \log_{\mathbb{Z}} \frac{q}{J} = \widehat{s} + \widehat{j_2},\quad \widehat{\ell}_{\mathrm{pair}} = (\widehat{b_1} + \widehat{b_2})/2.$$
理想等式 $b_1 b_2 = q_0^2 J_2^2 s$ 恰好给出
$$\widehat{c} := \log_{\mathbb{Z}} \frac{q}{q_0} = \widehat{\ell}_{\mathrm{pair}} - \widehat{s}/2 - \widehat{j_2} \ge 0,\quad 4\widehat{\ell}_{\mathrm{pair}} - 2\widehat{s} + \widehat{j_2} = 4\widehat{c} + 5\widehat{j_2} \ge 0. \tag{17.24}$$
上表现在证明精确的零延拓恒等式
$$\xi(n) = \chi_n(J)^4 \mathbf{1}_{(n,\mathrm{rad}\,q_0)=1}. \tag{17.25}$$
事实上，指数为四的素数恰好是 $sJ_2$ 的那些素数；$B$ 的每个其他素数都整除 $q_0$。同时属于 $J$ 与 $q_0$ 的素数只是重复了 $\chi_n(J)^4$ 已经提供的零。我们将在稍后的平均中固定 $q_0$ 但保留 $J$。模 $q_0$ 贡献一个 punctures，且不属于固定 ray group。对于固定的 $J, q_0$，$s, J_2$ 的选取、分解 $b_1 b_2 = q_0^2 J_2^2 s$ 以及理想 $A_i$ 仅有除子重数。
我们现在局部化真正的第一 Poisson 表达式，在延拓其互素支集或取绝对 Fourier 积分之前。局部表给出精确的实际范数恒等式
$$\widehat{b_1} - A + \widehat{b_2} - B + \widehat{E} = \widehat{s} - 2\widehat{j_2}.$$
对于 $y = hf^2 E$，蕴含 $Z^M q_h/(q_{\mathrm{dk}} q_{m1}) \le Z^\tau$ 与方程 (17.23) 给出
$$\widehat{y} \le \widehat{n_1} + \widehat{n_2} - 2\widehat{B} - M + \widehat{s} - 2\widehat{j_2} + \widehat{\delta} + 2\widehat{f} + \tau$$
$$\le \widehat{n_1} + \widehat{n_2} - 2\widehat{B} - M + 4\widehat{\ell}_{\mathrm{pair}} - \widehat{j} + \widehat{\delta} + 2\widehat{f} + \tau.$$
第二个不等式即方程 (17.24)。定义形式中心与外包外行尺度为
$$H_c = 2r - 2B - M + 4\ell + 2V + \delta - j,\quad H_{\mathrm{use}} = H_c + 12\eta + \tau. \tag{17.26}$$
相对于 $H_c$，最后那个实际上界具有误差
$$(\widehat{n_1} - r) + (\widehat{n_2} - r) - 2(\widehat{B} - B) + 2(\widehat{b_1} - \ell) + 2(\widehat{b_2} - \ell) - (\widehat{j} - j) + (\widehat{\delta} - \delta) + 2(\widehat{f} - V),$$
其在方程 (17.18) 下的正最大值是 $12\eta$。因此实际比值不等式蕴含对所有受支集的原始列对，$qy \le Z^{H_{\mathrm{use}}}$。
在原始表达式上仅插入外掩码
$$B_1(h) = \mathbf{1}_{0 < qhf^2 E \le Z^{H_{\mathrm{use}}}}.$$
对于每个受支集对，其补集包含于实际核尾部 $Z^M q_h/(q_{\mathrm{dk}} q_{m1}) > Z^\tau$；应用方程 (17.21) 舍弃该补集，原始计数与阶按下面固定。不插入比值不等式的指示函数。在 $B_1 = 1$ 内部保留完全光滑核，包括比值大于 $Z^\tau$ 的对。该掩码依赖于 $h, f, E$ 及固定扇区，但在所指出的提取之后不依赖于 $u_1, u_2$。若 $H_{\mathrm{use}} < 0$，其非零球为空，同样的尾部比较舍弃每个非零频率。任何主项非零

128
