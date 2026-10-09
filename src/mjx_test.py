import json, subprocess, sys
tests = [
    r'\begin{pmatrix} \varepsilon & -4i/(\sqrt{3}|c|) \\ -4i/(\sqrt{3}|c|) & \varepsilon \end{pmatrix}, \quad \det = \frac{16r_\varepsilon}{3q_c}.',
    r'6\pi^{-s}\Gamma(s)L(s,\psi)=\int_0^\infty\left(\Theta_\phi(v)-\phi(0)\right)v^{s-1}\,dv,\qquad \Theta_\phi(v)=\sum_{a\in\mathcal{O}}\phi(a)e^{-\pi v q_a}.',
    r'Q_{C,G,T}(\beta) \ll_\epsilon (KNB)^\epsilon T^\epsilon \sum_{q_t \asymp T} \sum_{\substack{r\ \mathrm{sf},\ (r,S)=1 \\ q_r \ll \min(K,C)}} \left( \frac{K}{q_r} + \frac{NG}{C^2} \right) \frac{C}{q_r}',
    r'\begin{cases} \chi_x(\lambda)^2 \Psi_0(x), & x \equiv 1 \pmod{3},\ (x, E) = 1, \\ 0, & \text{other cases}, \end{cases}',
    r'\beta^* = \sup \left( \{1/2\} \cup \left\{ \Re\rho : \begin{array}{l} 1/2 \le \Re\rho \le 1,\ L_F(\rho, \eta) = 0 \end{array} \right\} \right)',
    r'\theta(gw) = \kappa(g)\theta(w) \quad (g \in \Gamma_2), \qquad \kappa\begin{pmatrix} a & b \\ c & \delta\' \end{pmatrix} = \left( \frac{c}{a} \right)_3',
    r'p \nmid n_1 n_2, \qquad \prod_{p \mid P}\left(1 - \frac{\chi_p(n_1)\chi_p(n_2)}{p}\right)',
    r'\sum_{x \bmod p} e(x^2/p) = \sum_{y \bmod p} \chi_p(y)^3 e(y/p). \tag{4.5}',
    r'\frac{D_R\'}{D_R}(s) \le \sum_{p \mid R} \frac{\log q_p}{q_p^{\sigma_0} - 1} \ll_{\sigma_0} \log(2q_R).',
    r'|L(\sigma+it,\psi)|\ll Q^{3/5}(3+|t|)^2,\qquad -1/10\le\sigma\le 11/10.\qquad(4.14)',
]
inp = [{'key': 'k%02d' % i, 'latex': t, 'display': True} for i, t in enumerate(tests)]
open('/tmp/mjx_in.json', 'w').write(json.dumps(inp))
r = subprocess.run(['node', '/home/a/Downloads/25/mjx/tex2svg.js', '/tmp/mjx_in.json', '/tmp/mjx_out.json'],
                   capture_output=True, text=True, cwd='/home/a/Downloads/25/mjx')
print('stderr:', r.stderr.strip()[:400])
d = json.load(open('/tmp/mjx_out.json'))
for k in sorted(d):
    v = d[k]
    print('%-5s %s' % (k, ('ERROR ' + v['error'][:80]) if 'error' in v else 'ok  svg %d bytes  %s' % (len(v['svg']), (v['svg'][:95]).replace('\n', ' '))))
