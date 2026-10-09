引理 10.4（一个保留积分及其指数）。假设定义 10.1 的数据成立。固定
$\sigma_0 \in [7/8, 1)$ 且 $\beta_* > \sigma_0$，并令 $z_0 = 17/50$。设 $0 < d_{\min} < d_{\max} < \infty$，$U = Z^d$ 其中
$d_{\min} \leq d \leq d_{\max}$，并设 $B$ 为物理行 $u$ 的有限集合，满足 $q_u \asymp U$，位于引理 8.1 的一个保留
箱 $(i, a)$ 中。$q_u \asymp U$ 中的比较常数固定。令 $\delta = 2a - 1$，取
$0 < e < 10^{-3}$ 如该引理中所述，并令 $T_1 = Z^\tau > 2$ 其中 $0 < \tau \leq d_{\min}/100$。实的取值范围
和 $e$  independent 于目标选取。
    箱 $B$ 在任何 Mellin 变量移动之前固定。在方程 (10.11) 的保留中心围道上，假设存在分解
$$H_{\eta,u,Z}(s, w, z) = \sum_{\lambda \in \Lambda} H^{(\lambda)}_{\eta,u,Z}(s, w, z),$$

其中 $\Lambda$ 有限、非空且在 $Z$ 之前固定。此等式仅在保留围道上要求成立；被加项不必在围道之外全纯。对于每个 $\lambda$ 和每个保留的
$(s, w, z)$，假设 $B$ 被划分为至多 $C(1 + \log Z)^D$ 个集合 $B_{\lambda,\nu}(s, w, z)$，其中 $C, D$ 固定。
对于每个保留点处的每个集合，设 $R, g$ 为固定有界范围内的实数。假设对于固定的 $\varepsilon_c \geq 0$ 和有限的 $A_\eta \geq 0$，

$$\sum_{u \in B_{\lambda,\nu}(s,w,z)} L^S(w, \chi_\bullet(u)) H^{(\lambda)}_{\eta,u,Z}(s,w,z) \ll_\eta U^{R+\delta/2+\varepsilon_c} Z^{\ell(z_0-1/2)+g+\varepsilon_c} (1+T_1)^{A_\eta}. \tag{10.13}$$

该界在保留点、行集合和移动标号上一致。数 $\varepsilon_c$ 以及 $R, g$ 的有界范围在目标之前固定；$R, g$ 可以依赖于 $d, a$、逐点集合和全局数 $\beta_*$，但不以其他方式依赖于 $\eta$。设 $P_Z$ 为此分解中在任何保留点出现的所有对 $(R, g)$ 的集合。
      此处“保留”具有以下精确的高度含义。列出所有进入缓冲 L-值、倒数或对数导数（在验证方程 (10.13) 时）的外部坐标 $v_1, \ldots, v_m$，并包含所有三个原始 Mellin 高度，当它们不作为参数出现时系数为零。经过纯扭平移后，每个这样的参数的虚部为 $\gamma_j + \sum_{k=1}^{m} a_{jk} v_k$，其中有限矩阵 $(a_{jk})$ 固定且 $|\gamma_j| \leq (3i + 1)T_1$。限制

$$|v_k| \le c_k T_1, \qquad c_k = \frac{1}{2m(1+\max_j |a_{jk}|)}. \tag{10.14}$$

系数为零的坐标可以用同样的规则限制。于是每个添加的高度总计至多 $T_1/2$。固定的有界扩大通过提高 $Z$ 的下阈值来包含。如果使用额外的 Mellin 积分来建立方程 (10.13)，则该不等式在其完整左侧经这些积分后要求成立。任何被丢弃的部分必须留在其全局或绝对线上，由引理 10.2 或引理 4.5 界定，并在假设断言之前包含在所示界中。允许量 $T_1/2$ 在后续估计中不再更新。
    与一对 $(R, g)$ 相关的公共理想指数为

$$E_{\sigma_0}(d; R, g) = a - \sigma_0 + h(z_0 - 1/6) - a l_y - \ell/2 + g + d(R + \delta/2 - z_0). \tag{10.15}$$

如果 $B$ 为空，其贡献为零。否则令

$$E^{\max}_{\sigma_0,Z}(d) = \sup_{(R,g) \in P_Z} E_{\sigma_0}(d; R, g).$$

对于每个 $\varepsilon_d, \varepsilon_p > 0$，$B$ 在中心围道上的总贡献，对于充分大的 $Z$，为
$$\ll_\eta Z^{C(\sigma_0) + E^{\max}_{\sigma_0,Z}(d) + (16-6l_y)e} \cdot Z^{(1+d)\varepsilon_c + d\varepsilon_d + \varepsilon_p} (1+T_1)^{A_\eta}. \tag{10.16}$$

                                                            77
