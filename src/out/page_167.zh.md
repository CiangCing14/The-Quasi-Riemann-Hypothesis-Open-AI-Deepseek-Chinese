若该素数不整除 $j/G_c$，则称分割频率 $j/G_c$ 为单位（unit）；若整除，则称为非单位（nonunit）。设 $t_2$ 为这些单位素数的总根长度。设 $V_{\mathrm{id}}$ 为这些非单位素数的乘积，并令 $V = \log_Z q V_{\mathrm{id}}$。

方程 (13.8) 给出如下绝对局部界：

    公共重数与分割频率的绝对关联界
    $i = i,\ 6 \nmid i,\ \text{单位}$                    $P^{i-1}$
    $i = i,\ 6 \nmid i,\ \text{非单位}$                  $P^i$
    $i = i,\ 6 \mid i,\ \text{两者皆可}$                 $P^i$
    $i > j_0,\ 6 \mid j_0,\ \text{单位}$                 $P^{j_0}$

凡不在最后一行中的不等情形均为零。固定所指明的单位/非单位划分，并记 $j = G_c V_{\mathrm{id}} h'$。分块标量
$$\text{1part}(h') \frac{F(D_2, E_2; G_c V_{\mathrm{id}} h')}{Z^{g_2 - t_2}}$$
定义为在该划分之外为零，且按此定义其模处处至多为 1。我们并不对其他行上的未分块关联断言该单位界。凡被旧掩码强制为零的冻结分配，在此绝对界使用之前仍被丢弃。

完备支撑恒等式在每个完整剩余列上留下行因子 $\chi_n(G_c V_{\mathrm{id}} h')$。为计数其固定的移动支撑，令 $v = G_c V_{\mathrm{id}}$，$e_p = v_p(v) \bmod 6$。这些好理想的典范主生成元的乘积仍是主的，因此精确的全输入恒等式为
$$\chi_n(v) = \prod_{\substack{p \mid v \\ e_p \neq 0}} \chi_n(p)^{e_p} \prod_{\substack{p \mid v \\ e_p = 0}} 1_{(n,p)=1},$$
其中原行的任何单位都保留在 $h'$ 中。此恒等式中的所有素数都已刺穿每个剩余因子，因为它们位于真正提取出的支撑中。活跃的 $e_p \neq 0$ 素数包含于由 $t_2$ 计数的单位集和由 $V$ 计数的非单位集中。相等的六可整除素数与不等的最小六可整除素数都有 $e_p = 0$，在此固定因子中仅由公共刺穿表示。非单位素数也可以有 $e_p = 0$，此时将其计入 $V$ 只会放大该界。这里只分解出 $\chi_n(v)$：自然行因子 $\chi_n(h')$（连同其所有零点）以及所有固定射线互反相位都保留下来。它不会将与变化行之间的抵消重新归类为额外的刺穿。因此，完整的新移动支撑长度至多为 $q_e + w_o + t_2 + V$。

定义名义行宽与总宽为
$$m' = 2a_0 - K - g - g_2 - V, \qquad q' = q_e + w_o + t_2 + V, \tag{18.32}$$
$$M' = m' + q' = M + J - g - g_2 + t_2 \leq M - \sigma.$$
这里 $g_2 \geq t_2$，而 $g$ 的定义给出 $g - J \geq \sigma$。这些恒等式通过代入 $a_0 = A - c - w$ 以及方程 (18.22) 之前 $K_0$ 的定义得到。令
$$0 \leq \delta_{\mathrm{fr},2} := \frac{\xi \log(C_d C_{\mathrm{sec}})}{2} + \frac{\log Z}{\log Z} < \xi.$$
此处的扇区常数是第二变换的常数。所保留的行权重精确拉回为 $\Omega_{\mathrm{ret}}(q_{G_c V_{\mathrm{id}}} q_{h'})$。在其支撑上，
$$q_{h'} \leq \frac{C_d T_{\mathrm{sec}} Z^{\xi/2}}{q_{G_c V_{\mathrm{id}}}} \leq \frac{C_d C_{\mathrm{sec}} Z^{2a_0 - K - g + \xi/2}}{q_{G_c V_{\mathrm{id}}}} = Z^{m' + \delta_{\mathrm{fr},2}}.$$
因此它位于那个共同的包围行球内。在一个非空保留范围上，定义所宣称的非负行长度 $m'_{\mathrm{act}} = \max\{0, m' + \delta_{\mathrm{fr},2}\}$ 以及 $M'_{\mathrm{act}} = m'_{\mathrm{act}} + q'$。非空性蕴含

167
