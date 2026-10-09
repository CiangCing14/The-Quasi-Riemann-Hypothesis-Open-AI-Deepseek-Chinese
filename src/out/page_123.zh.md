记 $\hat h = \log_Z q_h$。完成是在实际尺度 $N_* = N - 3\hat h$ 上进行的。其固定支撑集在施加了下面指定的固定环形阈值后给出
$\hat h \le \ell_1 + \eta < d + \eta$。在引理 14.3 中，保留实际的剩余行二元组，并选取相同的阈值，使得

$$H \le M - O + \eta, \qquad T_d - S_0 - B_0 \le 2M - O + Q + V - N_* + 2z_a + \eta. \tag{17.11}$$

这些是方程 (5.35) 和 (14.17)，而不是针对扩大行范围的估计。代入 $N_* = N - 3\hat h$ 以及方程 (17.9) 中的第一个不等式，得到

$$T_d - S_0 - B_0 \le M - O + 2z_a - z_0 - c_{\text{node}} + 5d + 4\eta. \tag{17.12}$$

事实上，额外的项为 $2V + 3\hat h + \eta < 5d + 4\eta$。

同样选取阈值以保证 $e_\lambda \ge -\eta$，并如引理 14.3 中那样丢弃整个反射尾二元组。于是每个保留的二元组满足 $v + 3\ell_b + e_\lambda \le T_d + \tau_{\text{ref}}$。方程 (14.14) 的行分支在去掉其非正项后满足

$$E_{\text{ref}} \le M + z_a + \frac{5}{3}\eta \le F - c_{\text{node}} + \frac{5}{3}\eta.$$

对于 $u = z_a$ 的列分支，保留的对偶界首先给出 $E_{\text{ref}} \le O/2 + (T_d - S_0 - B_0) + 5\eta/3 + \tau_{\text{ref}}$。方程 (17.12) 和第一个不变量随后给出

$$E_{\text{ref}} \le F - 2c_{\text{node}} + 5d + \frac{17}{3}\eta + \tau_{\text{ref}}. \tag{17.13}$$

若 $u \ne z_a$，其定义蕴含 $u \ge v/2$。此时保留的对偶界首先给出

$$E_{\text{ref}} \le O/2 + (T_d - S_0 - B_0)/2 + z_a + \frac{7}{6}\eta + \frac{1}{2}\tau_{\text{ref}}.$$

利用方程 (17.12)、$z_a \le z_0$，以及第二个不变量，得到

$$E_{\text{ref}} \le F - M/4 - 3c_{\text{node}}/4 + (5/2)d + \frac{19}{6}\eta + \frac{1}{2}\tau_{\text{ref}}. \tag{17.14}$$

使用带有聚合局部损失 $\pi_{\text{ref}}$ 的反射估计，包括其自由选取的指数、标签除数界，以及有限多个对数和。若

$$c_{\text{node}} \ge c_*/2, \qquad d \le c_*/200, \qquad \eta, \tau_{\text{ref}}, \pi_{\text{ref}} \le c_*/1000,$$

则加上 $\pi_{\text{ref}}$ 之后，三个界都严格小于 $F$。在最后一个界中 $M \ge 0$。对于 $z_0 = 0$，只出现 $u = z_a = 0$。反射估计是对每个固定的 $f$ 分别应用的；加权质量界 $\sum_f w(f) \ll Z^{V + \pi_{\text{ref}}}$ 表明，对 $f$ 求其平方界之和至多花费这一数量，这已包含在聚合损失中，并抵消了外部的 $Z^{-V}$。因此没有移动的四次方标签进入混合范数，且这些终端项满足典范估计。

剩余项及其标记。在每次因式分解时，首先将一个槽位分配给被提取的因子，若其素数整除该因子，否则将其保留在剩余列上。完成的恒等式为

$$1_{p \mid n b^3} = 1_{p \mid b} + 1_{p \nmid b} 1_{p \mid n}. \tag{17.15}$$

更一般地，对于提取因子的有序列表 $D_1, \ldots, D_h$，精确的优先恒等式为
$$1_{p \mid D_1 \cdots D_h n} = \sum_{j=1}^{h} 1_{p \mid D_j} \prod_{a < j} 1_{p \nmid D_a} + 1_{p \mid n} \prod_{a \le h} 1_{p \nmid D_a}. \tag{17.16}$$

即使提取的因子共享素数，它依然成立。将其应用于每个槽位和每个平方的副本，就对每个素数元组给出一个不相交划分；一个槽位的两个副本具有

                                                          123
