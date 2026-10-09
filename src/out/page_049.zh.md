这个整除性模 $s$，并利用 $d$ 模 $s$ 的逆，给出 $s \mid s'$。对称的论证给出 $s' \mid s$。$S$ 之外一个理想的主生成元是唯一的，故 $s = s'$；原来的同余式随后给出 $d = d' \pmod{s}$。同一结论也包含单位模的情形。改变剩余类代表元只会将其分数平移一个 $O$ 中的元素。

    设 $0 < r_- < r_+$ 固定，且 $\operatorname{supp} W_1 \subset [r_-, r_+]$。对于两个不同的有贡献分数以及每个 $n \in O$，Eisenstein 整数 $ds' - d's - nss'$ 非零。因此
    $$\left| \frac{d}{s} - \frac{d'}{s'} - n \right| = \frac{|ds' - d's - nss'|}{|ss'|} \ge \frac{1}{|ss'|} \ge \frac{1}{r_+ Y}.$$
    最后一个不等式利用了 $q_s, q_{s'} \le r_+ Y$。于是这些分数在 $\mathbb{C}/O$ 中是 $\delta_Y$-分离的，其中 $\delta_Y = \min(1, r_+^{-1})/Y \le 1$。

    将展开后的多项式写作 $\sum_{s,d} a_{s,d} e(-md/s)$，只保留单位剩余类，其系数平方质量恰好为
    $$\sum_{s,d} |a_{s,d}|^2 = Y^{-3} \sum_s |c_\sigma(s) W_1(r_s)|^2 r_s^{-2} \varphi_O(s),$$
    $$\varphi_O(s) := \#(O/sO)^\times, \qquad \varphi_O(1) := 1.$$
    此表达式中不依赖于 $v$。由于 $\varphi_O(s) \le q_s \le r_+ Y$，在支集上 $r_s \ge r_-$，且满足 $q_s \le r_+ Y$ 的理想有 $O(Y)$ 个，故该质量为 $O(Y^{-1})$。将引理 6.1 应用于具有分离度 $\delta_Y$ 的点 $-d/s$，即证得第一个界。最后 $q_{b^*} \ge 1$，所以 $Q = q_{b^*} Y^2$ 蕴含 $Q + Y^2 \le 2Q$，从而证得第二个界。

    加性范数现在恰好具有与未标记的完备行范数配对所需的尺度。以下命题对原始探针实施该配对。

命题 6.3（平衡下界估计）。固定用于定义 $I_\eta$ 的算术数据与光滑权。对每个 $\epsilon > 0$，当 $Z \to \infty$ 时，
    $$I_\eta(Z^{1/2}, Z^{1/2}, Z) \ll_{A,\epsilon} Z^{1/4+\epsilon}.$$
    该指数与目标特征无关；隐含常数与下阈值可能依赖于其固定的算术数据。

证明。令 $X = Y = Z^{1/2}$ 且 $Q = q_{b^*} XY = q_{b^*} Z$。式 (6.2) 中的函数 $\Omega$ 有界，且支集在 $(0, \infty)$ 的一个固定紧子区间内。因此该恒等式中的所有行都落在 $0 < q_m \le C_\Omega Q$ 中，其中 $C_\Omega$ 为固定常数。

    取引理 5.8 的特化 $M = N = 1$，随后用定义 $B_{m,\sigma}$ 的有限射线分解，对每个 $\epsilon_1 > 0$ 给出
    $$\sum_{0 < q_m \le C_\Omega Q} |B_{m,\sigma}(Z)|^2 \ll_{A,\epsilon_1} Z^{1+\epsilon_1}.$$
    事实上，$q_{b^*}$ 固定，故行球是 $M = 1$ 球的固定倍数。完备尺度为 $Z$，即该引理中的 $N = 1$。该引理直接适用于定义 $B$ 的完备积分中的 Gaussian 剖面；对射线特征所作的固定有限 Fourier 和，由行 Hilbert 空间中的三角不等式只耗费一个固定因子。特别地，此应用保留了原始的行使零掩码。

    对式 (6.2) 中的行和施用 Cauchy–Schwarz。因子 $(q_m/Q)^{-iv}$ 的绝对值为一，$|\xi(m)| \le 1$（含其零延拓），且 $\Omega$ 有界。引理 6.2 关于 $v$ 一致，而 $B$ 与 $v$ 无关。由于 $W_0$ 光滑且为环状，$\int_{\mathbb{R}} |\widehat{W}_0(iv)| \, dv < \infty$。因此对 $\sigma \in T$ 的有限和给出
    $$|I_\eta(X, Y, Z)| \ll_{A,\epsilon_1} Q^{-1/2} \left( \frac{Q}{Y} \right)^{1/2} Z^{1/2+\epsilon_1/2} = Z^{1/4+\epsilon_1/2}.$$
    取 $\epsilon_1 = 2\epsilon$ 即证得命题。

49
