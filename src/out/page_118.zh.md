推论 17.4（带指标的有限传播）. 在引理 17.3 中，设 $\ell$ 表示顶点 $v$ 处的任意 admissible length 与外标签，并设 $\Phi_v(\ell)$ 为其期望的范数指数。假设在除以 $Z^{\Phi_v(\ell)}$ 之后，终端界具有该引理中的形式，且指数 $\delta_v$ 固定。一条边可以用依赖于 $Z$ 的族 $\Gamma_e$ 配以非负测度 $\nu_e$ 来指标化，并可以具有形式
$$
\int_{\Gamma_e}\int_{\mathbb{R}^{d_e}} Z^{a_e(\ell,\gamma)}|K_{e,\gamma}| \prod_{r=1}^{r_e} N_{v_{e,r}}\bigl(Z,\ell_{e,r},W_{e,r},A_{e,r}t+B_{e,r}\xi_{e,r}\bigr)^{\theta}\,d\xi\,d\nu_e(\gamma),
$$
其中子标签 $\ell_{e,r}$ 可以依赖于 $\ell,\gamma$。假设对那些标签一致地有
$$
a_e(\ell,\gamma)+\sum_r \theta_{e,r}\Phi_{v_{e,r}}(\ell_{e,r})-\Phi_v(\ell)\le \delta_e, \tag{17.4}
$$
其中 $\delta_e$ 固定，并且引理中的子剖面界成立。还假设对每个固定的 $H\ge 0$，
$$
\int_{\Gamma_e}\int_{\mathbb{R}^{d_e}} |K_{e,\gamma}|\langle \xi\rangle^H\,d\xi\,d\nu_e(\gamma)\le C_{e,H}Z^{\delta_e^{\mathrm{mass}}}p_{\ell_e(H)}(w)b_e(H)\langle t\rangle^{c_e(H)}, \tag{17.5}
$$
其中 $\delta_e^{\mathrm{mass}}$ 固定，且与 $H$ 无关。当这些量是通过分离一个 profile 而得到的平方 Hilbert 空间行范数时，此假设必须使用那些行所共有的系数测度。在有限多个深度中的每一个深度上只需有有限多种边类型；$\Gamma_e$ 的基数可以随 $Z$ 变化。

于是 $N_v/Z^{\Phi_v(\ell)}$ 具有引理 17.3 的结论，且对 $\ell$ 一致，终端指数为 $\delta_v$，边指数为 $\delta_e+\delta_e^{\mathrm{mass}}$。特别地，所有必需的半范数与高度阶数均为有限，并且与外部截断无关。

证明. 令 $\bar N_v=Z^{-\Phi_v(\ell)}N_v$。将其代入一条边，并由 (17.4) 式将其范数幂界定为 $Z^{\delta_e}$ 乘以归一化子项之积。代入它们的归纳界。如同引理 17.3 的乘积证明中那样，所需的系数矩为
$$
H_e=\sum_r \theta_{e,r}\bigl(H_r+B_r c'_{e,r}(J_r)\bigr),
$$
它是有限的，且与 $\gamma$ 无关。(17.5) 式在此阶数下贡献 $Z^{\delta_e^{\mathrm{mass}}}$，并且只贡献有限的 profile 阶数与高度阶数。因此，对有限多种边类型作反向归纳，恰好给出所述的归一化递推。在子项内部取平均的标签在整个论证过程中仍留在该子项内部；它不是 $\nu_e$ 的第二个积分变量。

我们明确说明本推论中离散标签如何归一化。在相关的加权 Cauchy 不等式之后，假设一个非负外测度满足 $\sum_{\gamma\in\Gamma} w_\gamma\le CZ^{c+\epsilon}$，其中 $c$ 与 $\epsilon$ 固定，且在高度阶数之前选定。对于块上共有的每个标签前因子 $Z^{a_{\mathrm{raw}}}$，令
$$
d\nu_\Gamma(\gamma)=Z^{-c}\sum_{\gamma\in\Gamma} w_\gamma \delta_\gamma,\qquad \nu_\Gamma(\Gamma)\le CZ^\epsilon.
$$
这里 $\delta_\gamma$ 表示单位点质量。对于使所示积分为有限的非负 $B_\gamma$，精确恒等式为
$$
Z^{a_{\mathrm{raw}}}\sum_{\gamma\in\Gamma} w_\gamma \int |K_\gamma(\xi)|B_\gamma(\xi)\,d\xi
=Z^{a_{\mathrm{raw}}+c}\int_\Gamma\int |K_\gamma(\xi)|B_\gamma(\xi)\,d\xi\,d\nu_\Gamma(\gamma). \tag{17.6}
$$
$K_\gamma$ 的一致加权矩现在给出 (17.5) 式，其中只剩残余的 $Z^\epsilon$ 质量。因此，一个已经包含计数 $c$ 的所示指数必须使用此归一化测度；
