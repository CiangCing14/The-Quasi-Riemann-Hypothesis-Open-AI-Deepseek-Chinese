包含高行族中所用目标与固定射线扭结，并且 $\Theta$ 中成员的每个导子素数都属于 $S$。对于六次方自由元 $u$，定义有限的表现集合
$$X_u = \{\psi_{u,\nu,\varsigma}(n) = \nu(n)\chi_n(u)^\varsigma : \nu \in \Theta,\ \varsigma \in \{-1,1\}\}$$。

在非单位处，$\chi_n(u)^{-1}$ 的值如同该符号的其他幂一样为零。$\Theta$ 的群性质表明 $X_u$ 在共轭下封闭。它包含分子特征 $\chi_\bullet(u)$、分母特征 $\eta\chi_\bullet(u)$，以及将六次符号的任一方向乘以 $\Theta$ 中元素所得的每个零延拓表现。

设 $\psi^*$ 为诱导表现 $\psi \in X_u$ 的本原特征，并设 $Q_\psi$ 为其导子范数。互反性与固定导子素数给出
$$Q_\psi \ll_A q_u, \qquad L_{\text{orig}}(s,\psi) = L(s,\psi^*) \prod_{p \in E_u} (1 - \psi^*(p) q_p^{-s}), \qquad E_u \subset S \cup \{p : p \mid u\}$$。

被删去乘积的根式具有范数 $O_S(q_u)$。这些恒等式保留了原有的零延拓；特别地，它们不会把依赖于行的掩码替换为独立选取的掩码。

若在素数 $p \notin S$ 处 $v_p(u) = j \in \{1, \ldots, 5\}$，则 $\chi_\bullet(u)$ 在 $p$ 处单位上的局部特征具有阶 $6/\gcd(6,j) > 1$。$\Theta$ 中的特征在该处非分歧，因此无法抵消这个局部特征。 consequently，$X_u$ 中的表现只有在 $u$ 支撑于 $S$ 上时才能诱导主特征。这样的六次方自由行只有有限多个，其中包括单位因子。就当前检测器而言，将它们移除；每次应用都必须单独估计这些有界的物理行。

固定 $0 < d_{\min} < d_{\max} < \infty$，并记 $U = Z^d$，其中 $d_{\min} \le d \le d_{\max}$。当前二元组中的行满足 $q_u \asymp U$，比较常数固定。令
$$0 < \tau \le d_{\min}/100, \qquad T_1 = Z^\tau > 2, \qquad 0 < e < 10^{-3}, \qquad I = \lceil 1/e \rceil + 2$$。

$\tau$ 的值将在固定高度阶已知后选取。目前它固定且独立于 $Z$。特别地，$T_1 \le U^{1/100}$。

引理 8.1（带缓冲的无零点箱）。对每个保留的行 $u$，存在指标 $i \in \{1, \ldots, I-1\}$ 与格点
$$a \in (51/100 + eZ_{\ge 0}) \cap [51/100, 1]$$
具有以下性质。对 $j = 1, \ldots, I$，令
$$M_j(u) = \max\{ \{51/100\} \cup \{\Re\rho : \psi \in X_u,\ L(\rho, \psi^*) = 0,\ \Re\rho \ge 51/100,\ |\Im\rho| \le 3jT_1\}\}$$。
则
$$a \le M_i(u) < a + e, \qquad M_{i+1}(u) < a + 2e$$。
若 $a > 51/100$，则某个 $\psi \in X_u$ 具有零点 $\rho = \sigma + i\gamma$，满足
$$a \le \sigma < a + e, \qquad |\gamma| \le 3iT_1$$。

对每个 $\epsilon_1 > 0$、每个 $\psi \in X_u$ 以及充分大的 $Z$，关于保留的行一致地有
$$|L_{\text{orig}}(s,\psi)| + |L_{\text{orig}}(s,\psi)^{-1}| \ll_{A,e,\epsilon_1} U^{\epsilon_1} \qquad (\Re s \ge a + 6e,\ |\Im s| \le (3i+2)T_1)$$。

在同一高度范围内的反射线上，
$$|L_{\text{orig}}(1 - a - 6e + it, \psi)| \ll_{A,e,\epsilon_1} U^{a-1/2+12e+\epsilon_1} (3 + T_1)^C,$$
其中 $C$ 只依赖于固定的实带状区域与域。可能的配对 $(i,a)$ 有 $O_e(1)$ 个，独立于行及其导子。
