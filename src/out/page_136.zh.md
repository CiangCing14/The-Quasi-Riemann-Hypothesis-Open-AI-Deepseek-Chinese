多项式为零，该分量被省略。若 $N_c < 0$ 且存在子列，则其范数至少为 1，且式 (17.45) 给出 $-6\eta \le N_c < 0$。对于保留的非空子式，定义

$$N_{\text{ch}} = \max(0, N_c), \quad \delta N = N_{\text{ch}} - N_c \in [0, 6\eta], \quad F_{\text{ch}} = N_{\text{ch}} + V_c = F_c + \delta N. \tag{17.46}$$

这是检验的有界变化，而非 $Z^{\eta}$ 宽度的支集扩大。使用上面选定的固定包围支集区间 $[a, b]$。若 $N_c < 0$，非空性给出 $Z^{\delta N} \le b$；若 $N_c \ge 0$，则 $\delta N = 0$，同样的界由 $b \ge 1$ 得到。因此两种情形下均有 $1 \le Z^{\delta N} \le b$。新的环形截断 $\omega_{n,a}(Z^{\delta N} y)$ 的支集在 $[a/b, b]$ 中，且 Euler 半范数一致有界。其尺度仅依赖于固定的扇区中心，而不依赖于当前的行或标号。这些裁剪支集的全体并集包含于 $I_D$ 中。

    固定 $\sigma_0$ 的一个加细 $\sigma$，由其 $v'$-二元组、第二条射线被加项和槽分支确定。设 $\Xi_\sigma$ 由

$\xi = (o, g'\,sf, d_2 \mid g', v'\,sf, k'' \neq 0;$ 新指派的槽素数 $)$

组成，带有保留的各个支集和槽分支。它既不包含旧的 $f, h$，也不包含当前列指标 $n_1, n_2$。定义 $R_1, E, J, q_0$ 的恒等式继承自 $o$，而 $\gamma, k_{\text{new}}, f_{\text{new}}$ 是 $\xi$ 的显式函数。该集合可在施加 $B_2$ 和 $(v', g'\,CJ) = 1$ 之前取定，在带符号外权重中保留这些掩码。设 $A_{2,\sigma}(\xi)$ 为所有新指派的原始槽系数及其优先掩码在第二侧的共轭之积。

    设 $X^{\text{src}}_\sigma$ 为该变换分量的结构外集合，在添加任何独立子行或标号之前。它保留 $o \in O_\sigma$，特别地保留精确重构 $b_1 b_2 = q_0^2 J_{22} s$、导出的 $J = sJ_2$、$q_0$，以及完全固定的 $b_1, b_2, t'$ 二元组支集；它还保留固定的 $g', d_2$ 支集、$d_2 \mid g'$，及其它外算术与槽条件。零权元组可被保留，单位 Fourier 相位在定义此结构集时被忽略。定义互异三元组之集（不计见证重数）为

$$\Gamma_\sigma = \{(q_0, t', r_g = g'/d_2) : \xi \in X^{\text{src}}_\sigma\}. \tag{17.47}$$

此投影在所有可能的当前行和标号上取一次，在固定任何 $k_{\text{new}}, f_{\text{new}}$ 或 Fourier 模式之前。每个非零变换项都映到其中。每个成员都有源见证，给出 $\hat{c} \le \ell + \eta$、$\hat{t} \le t + \eta$，且 $\log_Z q_{r_g} \le g - \theta + 2\eta$。其中第一个界将用于子穿刺；用于计数的包含范数球并不蕴含它。上述非空行与子列门控保持独立于该结构投影。

    令

$$D_c = \ell + A_i + t + g - \theta + V.$$

由于 $r = N - 3\ell$ 是与固定父式绑定的精确定义，代入式 (17.45) 和 (17.37) 给出精确的形式恒等式

$$\begin{aligned} F_c &= F - D_c - 2\ell + j, \qquad M_c = M - 2D_c - 2\ell + j, \\ F_c - M_c &= F - M + D_c, \\ 4F_c - 3M_c &= 4F - 3M + 2(A_i + t + g - \theta + V) + j. \end{aligned} \tag{17.48}$$

这些恒等式涉及与式 (17.9) 相同的固定 $F = N + V$，而非实际父范数。

    对于每个 $\gamma \in \Gamma_\sigma$，任选一个源见证。其实际整除性 $d_2 \mid g'$ 和式 (17.24) 给出

$$\hat{\theta} \le \hat{g}, \quad \hat{j} \le 2\hat{\ell}_{\text{pair}}, \quad \hat{c} \le \hat{\ell}_{\text{pair}}.$$

因此这里所需的唯一实际到中心的等式为

$$g - \theta \ge -2\eta, \qquad j \le 2\ell + 3\eta, \qquad \hat{c} \le \ell + \eta. \tag{17.49}$$

                                                    136
