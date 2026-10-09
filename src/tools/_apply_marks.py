#!/usr/bin/env python3
import sys
BASE='/home/a/Downloads/25/out/'
edits = {
 15: [
   (r'$$G(c) = \chi_c(4)\Gamma(c).$$', r'$$G(c) = \overline{\chi_c(4)}\Gamma(c).$$'),
   (r'G(c) = \chi_c(4)\gamma_3(c),', r'G(c) = \overline{\chi_c(4)}\gamma_3(c),'),
 ],
 46: [
   (r'G(A) = \sum_{\theta \in \widehat{T}} a_\theta \theta(A)',
    r'\overline{G(A)} = \sum_{\theta \in \widehat{T}} a_\theta \theta(A)'),
   (r'\sum_{v \in T} G(v) \overline{\theta(v)}.',
    r'\sum_{v \in T} \overline{G(v)} \overline{\theta(v)}.'),
 ],
 123: [
   (r'$h \le \ell_1 + \eta < d + \eta$', r'$\hat h \le \ell_1 + \eta < d + \eta$'),
 ],
 144: [
   (r'\mathbf{1}_{(c,j)=1}\chi_c(u)d_0(c)', r'\mathbf{1}_{(c,j)=1}\overline{\chi_c(u)}d_0(c)'),
   (r'Z^{m - \theta - \hat{L}_{\mathrm{init}}/2}', r'Z^{m - \hat{\theta} - \hat{L}_{\mathrm{init}}/2}'),
   (r'= Z^{\kappa_{b_1}^{\mathrm{init}}/2} Z^{\kappa_{b_2}^{\mathrm{init}}/2}',
    r'= Z^{\hat{\kappa}_{b_1}^{\mathrm{init}}/2} Z^{\hat{\kappa}_{b_2}^{\mathrm{init}}/2}'),
 ],
 149: [
   (r'$$\sum_{\omega \in \Omega_\Sigma} V_{\Sigma_{\text{init}}} Q_1 Q_2 \ll',
    r'$$\left|\sum_{\omega \in \Omega_\Sigma} V_{\Sigma_{\text{init}}} Q_1 \overline{Q_2}\right| \ll'),
   (r'\|\nu_{\Sigma_{\text{init}}}\|', r'\lVert\nu_{\Sigma_{\text{init}}}\rVert'),
 ],
}
for p,es in edits.items():
    path=BASE+'page_%03d.zh.md'%p
    t=open(path,encoding='utf-8').read()
    for old,new in es:
        n=t.count(old)
        if n==0:
            print('!! page %03d NOT FOUND: %r'%(p,old[:60])); continue
        t=t.replace(old,new)
        print('page %03d  replaced %d x  %r'%(p,n,old[:50]))
    open(path,'w',encoding='utf-8').write(t)
print('done')
