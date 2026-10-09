设 $A_0$ 为 $k_{\mathrm{res}}$ 之外所有活跃非槽位素数的对数范数，

设 $S_0$ 为其中小 Ramanujan 项与活跃零掩码项的对数范数，

设 $N_0$ 为分配给无平方对偶理想的 $j=4$ 整除项的对数范数，

设 $B_0$ 为分配给立方理想但不分配给无平方理想的 $j=4$ 整除项的对数范数。

此处对数范数是指所示乘积的范数的 $\log ZP$。分配使用了 $1_{p\mid nb^3}=1_{p\mid n}+1_{p\nmid n}1_{p\mid b}$。令 $z_a=i$ 活跃 $z_i$ 为其名义槽位长度之和。活跃素数的乘积的范数除以 $Z^{z_a}$ 落在一个固定的紧区间内，包括零名义长度或空列表的情形。在提取出强制的无平方素数与立方素数之后，将剩余的对偶理想限制为

$$q_n\asymp Z^v,\qquad q_b\asymp Z^{\ell_b},\qquad q^\lambda h_\lambda=Z^{e_\lambda}.$$

选择理想中心 $v,\ell_b$ 非负。这些是源对偶理想：它们保留方程 (5.2) 所允许的 $S$ 中的每一个素数；它们上面不放置额外的 $S$-掩码。只施加所显示的 $\lambda$-赋值支撑条件。单位和整数 $h_\lambda\ge -4$ 在此二元组中固定。对于这些选择，记 $U_{v,\ell_b,e_\lambda}(k_{\mathrm{res}})$ 为方程 (14.3) 的右端，以乘积形式元组系数求和，带有指定的局部选择与对偶限制，以及实际因子 $\chi_{\mathrm{row}}(q_{k_{\mathrm{res}}}/Z^H)$。在此定义中活跃槽位元组仍被求和。此定义分别对每个固定的强性且受支撑的行部分，以及通过固定剩余行乘积与活跃槽位乘积模完全反射模 $M_{\mathrm{ref}}^2$ 的各个类而得到的每个扇区作出。

引理 14.3（反射能量）。保留上述反射块数据。设 $Z\ge 2$，并假设它们的对数长度在固定的有界集合中取值。在方程 (14.2) 的完备和中，固定的特征、穿刺与槽位系数独立于 $k,f$，槽位支撑互不相交，且槽位系数如方程 (14.1) 中那样为乘积。冻结 $k_{\mathrm{pow}},k_{\mathrm{sup}}$ 之后的固定行限制必须独立于活跃槽位与对偶变量，除了显式的零掩码 $1_{(P,k_{\mathrm{res}})=1}$ 之外。固定一个小量 $\tau_{\mathrm{ref}}>0$，令 $X=Z^{N_*}$。定义 $T_d$，并称一个二元组被以下公式保留：

$$T_d=2H+2A_0+2z_a-N_*-N_0-3B_0,\tag{14.11}$$
$$v+3\ell_b+e_\lambda\le T_d+\tau_{\mathrm{ref}}\qquad\text{对于保留的二元组}.$$

满足
$$v+3\ell_b+e_\lambda>T_d+\tau_{\mathrm{ref}}$$
的项，在充分远的核围道平移以及仅依赖于固定支撑区间与 $\tau_{\mathrm{ref}}$ 的 $Z$ 阈值之下，具有任意小的总大小，且代价为固定的多项式高度。每个保留的二元组对每个活跃元组具有系数指数

$$-v/2-\ell_b-e_\lambda/3-(S_0+B_0+z_a)/2.\tag{14.12}$$

定义
$$u=\min\{v,z_a,(v+z_a)/3\},\tag{14.13}$$
以及
$$\begin{aligned}E_{\mathrm{ref}}={}&O/2+\max(H,v+\ell_b)-S_0-B_0+z_a-u-\ell_b-2e_\lambda/3\\&-\tfrac12(T_d-v-3\ell_b-e_\lambda)_+.\end{aligned}\tag{14.14}$$

对每个 $\epsilon>0$，固定 $k_{\mathrm{pow}},k_{\mathrm{sup}}$ 的贡献满足
$$\sum_{k_{\mathrm{res}}\ \mathrm{sf}}|U_{v,\ell_b,e_\lambda}(k_{\mathrm{res}})|^2\ll Z^{E_{\mathrm{ref}}-O/2+\epsilon}.$$
