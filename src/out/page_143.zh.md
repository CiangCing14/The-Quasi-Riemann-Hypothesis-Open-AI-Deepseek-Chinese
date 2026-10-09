成立，所有零延拓均适用。符号 $\mu(P_0)$ 是存活槽位上各符号的乘积，并可并入它们的有界系数中。因此系数仍保持式 (14.1) 的形式。

对于这个固定指定的子集，由各名义槽中心定义 $G$：

$$G = \sum_{i \text{ assigned}} z_i, \quad z_0 = z - G, \quad D' = r + z - 2G.$$

于是 $G, z_0 \geq 0$，且 $z_0$ 恰为存活的名义容量。归一化满足

$$Z^{-(r+z)/2} = Z^{-G} Z^{-D'/2}.$$

实际的 $j$ 是指定素数的乘积，因此 $q_j / Z^G$ 落在一个固定的乘积区间内。理想计数至多给出 $CZ^G$ 种选择，此外还有为指定单独选取的除数损失。行 Hilbert 空间中的三角不等式利用 $Z^{-G}$ 来抵消这一计数。整个因子 $\psi_u(j)^2$ 是一个有界的行标量，包括其零点，并且在该空间中是一个压缩。剩余的列与 $j$ 互素，给出固定的穿刺 $1_{(c,j)=1}$。

以下是这一重叠归约背后的精确恒等式。设 $I_0$ 为存活子集，并令 $y_j = q_j / Z^G$，$y_c = q_c / Z^{D'}$，且对每个槽位 $y_i = q_{p_i} / Z^{z_i}$。在原支撑上，

$$\frac{q_n}{Z^r} = \frac{y_j y_c}{\prod_{i \in I_0} y_i}.$$

对于一个固定的指定元组，其对 $M_u(Z^r; W)Q_u$ 的贡献 $U_{u,j}$ 恰为

$$U_{u,j} = \mu(j) \prod_{i \in I \setminus I_0} a_i(p_i) W_i(y_i) \, Z^{-G} \psi_u(j)^2 Z^{-D'/2} \sum_{\substack{c \text{ sf} \\ (c,j)=1}} \mu(c) \psi_u(c)$$
$$\times \sum_{\substack{(p_i) \in \prod_{i \in I} P_i \\ P_0 \mid c}} \mu(P_0) \prod_{i \in I_0} a_i(p_i) W_i(y_i) W\left( \frac{y_j y_c}{\prod_{i \in I_0} y_i} \right). \tag{17.67}$$

确实，一个与 $j$ 互素的平方自由 $c$，连同满足 $P_0 \mid c$ 的存活元组，唯一地重构出 $n = j(c/P_0)$ 以及规定的重叠。$c$ 的平方自由性已经给出 $(c/P_0, P_0) = 1$，因此没有丢失任何进一步的条件。符号 $\mu(P_0)$ 是各个素数符号的乘积。这也表明，随后每个平方两侧的 $j$ 都是同一个固定理想：前面的三角不等式是在该平方之前取的。

恒等式 $c = nP/j^2$ 将 $y_c$ 置于一个固定的紧区间内。若 $D'$ 在一个有界的非空窗口内略微为负，这仍然有意义；$D'$ 尚不是一个典范参数。选取一个新的单独截断 $\omega_c$，使其在整个商支撑上等于 1。对于固定的 $j$，令 $\Omega_c$ 在 $\omega_c$ 的整个支撑上等于 1，并令 $\Omega_i$ 在每个存活的单独槽位支撑上等于 1。单个联合剖面

$$H_{\text{ov},j}(y_c, (y_i)_{i \in I_0}) = \Omega_c(y_c) \prod_{i \in I_0} \Omega_i(y_i) W\left( \frac{y_j y_c}{\prod_{i \in I_0} y_i} \right)$$

在这些独立坐标中是紧支撑的。当前的截断 $\omega_c$ 和各个因子 $W_i(y_i)$ 保持在其变换之外。因此，在维数 $1 + |I_0|$ 中的式 (17.19) 将式 (17.67) 精确地表示为同一个指定标量和 $Z^{-G} \psi_u(j)^2$，乘以

$$(2\pi)^{-1-|I_0|} \int_{\mathbb{R}^{1+|I_0|}} \widehat{H}_{\text{ov},j}(\upsilon) Z^{-D'/2} \sum_{c \text{ sf}} \mu(c) \psi_u(c) 1_{(c,j)=1} \, d\upsilon(c) \, \omega_c(y_c) y_c^{i\upsilon_c} d\upsilon,$$

其中 $d\upsilon$ 带有原来的存活列表和各个系数 $\mu(p) a_i(p) W_i(y_i) y_i^{i\upsilon_i}$。展开标记并反演联合变换，逐项证明了这一等式。没有测度
