#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, sys, os
ROOT = '/home/a/Downloads/25'

def load(p):
    return open(os.path.join(ROOT, p), encoding='utf-8').read()

def save(p, t):
    open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(t)

# ---------------- PAGE 140 ----------------
p140 = 'out/page_140.zh.md'
t = load(p140)

R140 = [
 ('DKslot ', r'$D_{K_{\text{slot}}}$'),
 ('依赖于 f。', r'依赖于 $f$。'),
 ('后，B2 ', r'后，$B_2$ '),
 ('Qa = Qa,γ,ζ (knew , fnew )', r'$Q_a = Q_{a,\gamma,\zeta}(k_{\text{new}}, f_{\text{new}})$'),
 ('Z cσ /2 ，', r'$Z^{c_\sigma/2}$，'),
 ('∥νσ ∥', r'$\|\nu_\sigma\|$'),
 ('γ ∈ Γσ 使用', r'$\gamma \in \Gamma_\sigma$ 使用'),
 ('Hc = 2r − 2B − M + 4ℓ + 2V + δ − j', r'$H_c = 2r - 2B - M + 4\ell + 2V + \delta - j$'),
 ('r + 3ℓ + V = N + V 。', r'$r + 3\ell + V = N + V$。'),
 ('Ea,γ ≪ C(t, ζ)Z Fch +ϵchild ，', r'$E_{a,\gamma} \ll C(t,\zeta)Z^{F_{\text{ch}}+\epsilon_{\text{child}}}$，'),
 ('J、C、d2 、v ′ 留在', r"$J$、$C$、$d_2$、$v'$ 留在"),
 ('Z Fch +ϵchild 界定', r'$Z^{F_{\text{ch}}+\epsilon_{\text{child}}}$ 界定'),
 ('δN 都出现', r'$\delta_N$ 都出现'),
 ('Z M +π ，', r'$Z^{M+\pi}$，'),
 ('Z F +26η+τ +π ；', r'$Z^{F+26\eta+\tau+\pi}$；'),
]

missing = [a for a, b in R140 if a not in t]
if missing:
    print('140 MISSING:')
    for m in missing:
        print('   ', repr(m))
    sys.exit(1)
for a, b in R140:
    t = t.replace(a, b)

L = t.split('\n')
NEW_eq1763 = r'$$H_{a,\gamma} = \sum_{\substack{f\, s_f \\ q_f/Z^{V_c} \in I_f}} D_{K_{\text{slot}}}(f) \sum_{\substack{k \in \mathcal{O} \\ 0 < q_k \le Z^{M_{\text{ch}}}}} |Q_{a,\gamma,\zeta}(k, f)|^2 = Z^{F_{\text{ch}}} E_{a,\gamma}. \tag{17.63}$$'
NEW_big    = r'$$\sum_{\xi \in \Xi_\sigma} V_\sigma Q_1 Q_2 \le \left( \prod_{a=1}^{2} \sum_{\xi \in \Xi_\sigma} |V_\sigma| |Q_a|^2 \right)^{1/2} \ll Z^{c_\sigma} \left( \prod_{a=1}^{2} \int_{\Gamma_\sigma} H_{a,\gamma} \, d\nu_\sigma(\gamma) \right)^{1/2}.$$'
NEW_eq1764 = r'$$\kappa_i + \lambda_c + C_c + 2F_c = F. \tag{17.64}$$'
NEW_vqsig  = r'$$\sum_{\xi \in \Xi_\sigma} V_\sigma Q_1 Q_2 \ll C(t,\zeta)Z^{c_\sigma+2F_{\text{ch}}+\epsilon_{\text{child}}}\|\nu_\sigma\|.$$'
NEW_eq1765 = r'$$\begin{aligned} \kappa_i + \lambda_c + C_c + 2F_{\text{ch}} + \left(\frac{9}{2} + 18 + \frac{11}{2}\right)\eta + \tau + \pi + \epsilon_{\text{child}} &= F + 28\eta + 2\delta_N + \tau + \pi + \epsilon_{\text{child}} \\ &\le F + 40\eta + \tau + \pi + \epsilon_{\text{child}}. \end{aligned} \tag{17.65}$$'

new = [
 L[0],            # 1 prose
 NEW_eq1763,      # was lines 2-5
 L[5],            # 6 blank
 L[6],            # 7 prose
 NEW_big,         # was lines 8-16
 L[16], L[17],    # 17,18 blank
 L[18],           # 19 prose
 L[19],           # 20 blank
 L[20],           # 21 prose
 L[21],           # 22 blank
 NEW_eq1764,      # 23 (17.64)
 L[23],           # 24 blank
 L[24],           # 25 prose
 L[25],           # 26 prose
 NEW_vqsig,       # was 27-29
 L[29],           # 30 blank
 L[30],           # 31 prose
 L[31],           # 32 prose
 L[32],           # 33 blank
 NEW_eq1765,      # was 34-37 (17.65)
 L[37],           # 38 blank
 L[38],           # 39 prose
 L[39],           # 40 blank
 L[40],           # 41 page num
 L[41],           # 42 ''
]
save(p140, '\n'.join(new))
print('140 written:', len(new), 'lines')

# ---------------- PAGE 154 ----------------
p154 = 'out/page_154.zh.md'
t = load(p154)

R154 = [
 ('集合与 ϵ，且对 κ ∈ [3/4, 1] 一致', r'集合与 $\epsilon$，且对 $\kappa \in [3/4, 1]$ 一致'),
 ('与 Z 无关的算术数据 A 和', r'与 $Z$ 无关的算术数据 $A$ 和'),
 ('对 7/8 界的应用取 κ = 2β∗ − 1，', r'对 $7/8$ 界的应用取 $\kappa = 2\beta_* - 1$，'),
 ('由 11/12 界提供的值 5/6，', r'由 $11/12$ 界提供的值 $5/6$，'),
 ('此后 z = 0 表示', r'此后 $z = 0$ 表示'),
 ('有效宽度 M = m + q 进行的', r'有效宽度 $M = m + q$ 进行的'),
 ('范围 A ≤ 5M/6。', r'范围 $A \le 5M/6$。'),
 ('落在 Θ 中的', r'落在 $\Theta$ 中的'),
 ('超出量 A−5M/6。', r'超出量 $A - 5M/6$。'),
 ('以及 S 中的固定素数', r'以及 $S$ 中的固定素数'),
 ('无平方理想 R 中', r'无平方理想 $R$ 中'),
 ('满足 qR ≤ Z B ，且', r'满足 $q_R \le Z^B$，且'),
 ('变动因子 χn (k) 之间的', r'变动因子 $\chi_n(k)$ 之间的'),
 ('设 ψk0 为', r'设 $\psi_k^0$ 为'),
 ('并设 Tk (X) 表示其在尺度 X 处', r'并设 $T_k(X)$ 表示其在尺度 $X$ 处'),
 ('用 Sk,R (X) 表示', r'用 $S_{k,R}(X)$ 表示'),
 ('插入 d|(n,R) µ(d) 并写 n = dl 得到', r'插入 $\sum_{d \mid (n,R)}\mu(d)$ 并写 $n = dl$ 得到'),
 ('商 l 在 d 的素数处', r'商 $l$ 在 $d$ 的素数处'),
 ('构成 J ⊆ I，而普通除子为 d1 , d2 ，则', r'构成 $J \subseteq I$，而普通除子为 $d_1, d_2$，则'),
 ('若 z ′ > 0，则', r"若 $z' > 0$，则"),
 ('若 z ′ = 0，则', r"若 $z' = 0$，则"),
 ('且 Rz ⊆ R0 。', r'且 $R_z \subseteq R_0$。'),
]

missing = [a for a, b in R154 if a not in t]
if missing:
    print('154 MISSING:')
    for m in missing:
        print('   ', repr(m))
    sys.exit(1)
for a, b in R154:
    t = t.replace(a, b)

L = t.split('\n')
NEW_eq184 = r'$$S_{k,R}(X) = \sum_{d \mid R} \mu(d)\psi_k^0(d)q_d^{-1/2}T_k(X/q_d), \tag{18.4}$$'
NEW_eq185 = r'$$Q_{k,i,R} = Q_{k,i}^0 - P_i^{-1/2}\sum_{\substack{p \mid R \\ p\ \text{prime}}}\psi_k^0(p)\nu_i(p)W_i^{\text{slot}}(q_p/P_i), \qquad P_i = Z^{z_i}. \tag{18.5}$$'
NEW_coeff = r'$$q_{d_1 d_2}^{-1/2}\prod_{i \in J}P_i^{-1/2}.$$'
NEW_lengths = r"$$A' = A - \log_Z q_{d_1 d_2} - \sum_{i \in J}z_i, \qquad z' = z - \sum_{i \in J}z_i.$$"

new = [
 L[0],          # 1
 L[1],          # 2
 L[2],          # 3
 L[3],          # 4 blank
 L[4],          # 5 heading
 L[5],          # 6
 L[6],          # 7
 NEW_eq184,     # was 8-11 (18.4)
 NEW_eq185,     # was 12-18 (18.5) + stray P dropped
 L[18],         # 19
 L[19],         # 20
 NEW_coeff,     # was 21-24
 L[24],         # 25 blank
 L[25],         # 26
 NEW_lengths,   # was 27-29
 L[29],         # 30 blank
 L[30],         # 31
 L[31],         # 32 blank
 L[32],         # 33 page num
 L[33],         # 34 ''
]
save(p154, '\n'.join(new))
print('154 written:', len(new), 'lines')
