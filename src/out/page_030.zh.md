$M = \lambda^{12} L^4$。对每个活跃的 $p$，中国剩余定理允许将所选的非零类 $h_p \bmod p$ 提升为满足 $h_p \equiv 0 \pmod{M^2}$。将 $r$ 限制在模 $M^2$ 的一个类中。方程 (5.13) 表明 $a$ 随后模 $M c_F$ 固定；事实上其变动项可被 $M^2 c_F$ 整除，而 $a_F r$ 模 $M^2$ 固定，且由于 $c_F$ 整除 $L$ 至多相差一个单位，$M^2$ 可被 $M c_F$ 整除。它还表明若 $\lambda \mid c$ 则 $a \equiv 1 \pmod 3$，否则 $c \equiv 1 \pmod 3$。

通过以下相容的局部同余式选取 $\delta'$：

$$\delta' \equiv a^{-1} \pmod{M c_F} \quad \text{在整除 } c_F \text{ 的每个素数处},$$
$$\delta' \equiv 0 \pmod{M} \quad \text{在整除 } M \text{ 但不整除 } c_F \text{ 的每个素数处},$$
$$\delta' \equiv a^{-1} \pmod{p} \quad (p \mid r).$$

第一行指的是 $M c_F$ 的相应素数幂部分。所有逆元都存在，因为 $a/c$ 是约化的。令 $b = (a\delta' - 1)/c$ 及 $g = \frac{ac}{b}\delta'$。则 $g \in \Gamma$，且将 $a\delta' - 1$ 除以 $c$ 给出

$$b \equiv 0 \pmod{M} \text{ 在 } c_F \text{ 的素数处}, \qquad b \equiv -c^{-1} \pmod{M} \text{ 在 } M \text{ 的其他素数处}.$$

因而 $a, b, c, \delta'$ 在整除 $L$ 的每个素数的所需幂次处具有固定的剩余类，与类 $h_p$ 无关。当在剩余符号计算中出现零元时，可先将 $z_h$ 平移 $\lambda^2 M^2 \mathcal{O}$，然后对 $\delta'$ 加上合同余模数的倍数。这些改动保持所有已列出的同余式，并避开使某元为零的有限多个值。它们不改变平移后的 theta 函数。

分三种情形，由 $v_\lambda(c)$ 区分。若 $3 \mid c$，令 $H = I$。则 $G = g \in \Gamma_1(3)$，对主元 $a$ 与 $r$ 的主素数的三次互反律给出
$$\kappa(G) = \left(\frac{c_F}{a}\right)_3 \left(\frac{a}{r}\right)_3. \tag{5.14}$$
若 $v_\lambda(c) = 1$，取唯一的 $u_0 \in \{\lambda, -\lambda\}$ 使得 $u_0 \equiv c \pmod 3$，并令 $H = L(u_0)$；这是仅有的两种可能，因为 $\mathcal{O}/(\lambda) \simeq \mathbb{F}_3$。上述同余式表明 $G = gH^{-1} \in \Gamma_1(3)$。记 $A = a - u_0 b$。$A$ 与 $a$ 均为主元，且互素：$(a, b) = 1$ 且 $(a, u_0) = 1$。行列式方程给出

$$a(c - u_0 \delta') = cA - u_0, \qquad bc \equiv -1 \pmod a.$$

由此，对 $a, A$ 应用三次互反律得
$$\kappa(G) = \left(\frac{-u_0}{A}\right)_3 \left(\frac{a}{A}\right)_3^{-1}$$
$$= \left(\frac{-u_0}{A}\right)_3 \left(\frac{c/u_0}{a}\right)_3 = \left(\frac{-u_0}{A}\right)_3 \left(\frac{c_F/u_0}{a}\right)_3 \left(\frac{a}{r}\right)_3.$$

对于第二个等号，将 $A$ 模 $a$ 归约并使用 $(A/a)_3 = (-u_0 b/a)_3 = (u_0/a)_3 (c/a)_3^{-1}$；$-1$ 的三次符号为 1。最后设 $(\lambda, c) = 1$。选取 $u_0 = s + t\omega \equiv a \pmod 3$，其中 $0 \leq s, t < 3$，并令 $H = \begin{pmatrix} u_0 & -1 \\ 1 & 0 \end{pmatrix}$。此处 $c \equiv 1$，$\delta' \equiv 0$，$b \equiv -1 \pmod 3$，故
$$G = gH^{-1} = \begin{pmatrix} -b & a + bu_0 \\ -\delta' & c + \delta' u_0 \end{pmatrix} \in \Gamma_1(3).$$

$-b$ 与 $c$ 均为主元。此外 $-bc = 1 - a\delta' \equiv 1 \pmod 9$。将 $\delta' = u\lambda^k \delta_0$ 分解，其中 $\delta_0$ 为主元。补充律给出 $(u\lambda^k/(1 - a\delta'))_3 = 1$；三次互反律给出 $(\delta_0/(1 - a\delta'))_3 = 1$，因为互反后分子为 $1 \pmod{\delta_0}$。因此
$$\left(\frac{\delta'}{-bc}\right)_3 = 1, \qquad \kappa(G) = \left(\frac{\delta'}{-b}\right)_3 = \left(\frac{\delta'}{c}\right)_3^{-1} \left(\frac{a}{c}\right)_3 = \left(\frac{a}{c}\right)_3 = \left(\frac{a}{c_F}\right)_3 \left(\frac{a}{r}\right)_3.$$

最后一个逆元使用了 $a\delta' \equiv 1 \pmod c$。
