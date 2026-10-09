# SPEC — repair un-typeset mathematics in the translated page files

## What this is
`/home/a/Downloads/25` holds a 200-page English paper (`paper.pdf`) that was translated page by page
into Chinese.  For each page there are two files:

* `pages/page_NNN.txt` — English text extracted with `pdftotext -layout`.  LAYOUT ONLY: it loses
  sub/superscript positioning and shreds fractions, products, integrals and big delimiters across
  several lines.  Use it for MEANING (and `paper.pdf` itself), never as the source of symbol structure.
* `out/page_NNN.zh.md` — the Chinese translation.  On some pages the translator copied the
  mathematics straight out of that layout text, so the formulas are plain text with unicode
  sub/superscripts.  That is the defect you are fixing.

**Your job:** rewrite `out/page_NNN.zh.md` so that every piece of mathematics is inside LaTeX math mode
(`$...$` inline, `$$...$$` display).  Nothing else may change.

## Hard rules
1. **The Chinese prose must come out byte-identical**: same characters, same punctuation, same word
   order, same paragraph breaks, same blank lines, same trailing bare page-number line.  No rewording,
   no “improving”, no added or deleted sentences, no explanatory additions.
2. Only *wrap* (or restore) mathematics.  You may re-join fragments of one display equation that the
   layout split over several lines, and you may drop the layout's column padding inside math.
3. Use only `$...$` / `$$...$$`.  No `\[...\]`, no `\begin{equation}`, no `\label`.
   `\frac`, `\sqrt`, `\prod`, `\sum`, `\int`, `\left(...\right)`, `\begin{aligned}`, `\tag{...}` are fine.
4. Equation numbers go back into the math as `\tag{17.27}` — once per equation, never duplicated.
5. Chinese punctuation (`、，。：；`) stays OUTSIDE math: `相异分配 $\pi_{\text{count,init}}$、$\pi_{\text{fib,init}}$。`
6. The layout extraction garbles big delimiters into control characters `\u0010 \u0011 \u0012 \u0013`
   (and `\u0010...\u0011` for parentheses, `\u0012...\u0013` for braces).  Rebuild them as
   `\left( ... \right)` etc. inside the display math.
7. Do not touch any file other than the `out/page_NNN.zh.md` pages assigned to you, plus your own
   backups.  Never run `build_html.py`, `make_md.py`, npm or chrome — the parent agent rebuilds once at the end.

## Authoritative source of truth for symbol structure
The PDF's own glyph coordinates:

    cd /home/a/Downloads/25
    python3 tools/bbox_dump.py NNN            # whole page
    python3 tools/bbox_dump.py NNN 300 420    # optional y-range (pt)

Output A — visual lines: tokens sharing a baseline are joined; a token that is smaller and *raised*
is marked `^`, *lowered* is marked `v`, odd height `~` (rules, braces, sqrt bars, big operators).
Use these marks to decide sub- vs superscript for every single symbol.
Output B — raw tokens `x0-x1  y0-y1  token`: essential for fractions (numerator above, denominator
below), for `\prod`/`\sum`/`\int` limits (a token above/below the operator), and for roots.
Decide EVERY sub/superscript, fraction and limit from this geometry.  Do not guess.

## Back up before editing
    cd /home/a/Downloads/25
    cp -n out/page_NNN.zh.md out/page_NNN.zh.md.premath

## House style — copy it from the pages that are already correct
`out/page_139.zh.md`, `out/page_149.zh.md`, `out/page_150.zh.md`, `out/page_151.zh.md` are the
reference.  Highlights:

* multi-letter sub/superscripts live in `\text{}`:
  `$\pi_{\text{init}}$`, `$\pi_{\text{count,init}}$`, `$\tau_{\text{init}}$`, `$s_{\text{slot}}$`,
  `$B_{\text{crude,init}}$`, `$F_{\text{init}}$`, `$K_{\text{slot}}$`, `$M_{\text{init}}$`
* `\max`/`\min` are operators: `$r_{\max}$`, `$z_{\max}$`, `$m_{\max}$`, `$D_{\max}$`, `$M_{\max}$`,
  `$N_{\max}$`, `$V_{\max}$`, `$d_{\min}$`
* divisor count: `$d_{\mathcal{O}}(c)$`; big-O: `$O(Z^{-T_{\text{init}}})$`; real part: `$\Re s$`
* relations/operators: `$\le$`, `$\ge$`, `$\ll$`, `$\asymp$`, `$\in$`, `$\mid$`, `$\sim$`, `$\#T_\Sigma$`
* greek: `$\eta$`, `$\epsilon$`, `$\delta_{\text{init}}$`, `$\epsilon_c$`, `$\kappa$`, `$\tau$`, `$\pi$`, `$\sigma$`
* accents: `$\bar c$`, `$\bar\alpha(z)$`
* an inline run is `$a = Z^{m}/(q_{d'} q_{z_1 z_2})$` — no spaces just inside the delimiters, no
  full-width characters inside math.
* a display equation occupies its own line(s):

      $$\kappa^{\text{init}}_{c} + P_1 + 2F^{\text{init}}_{c} = m$$

      $$a^{-1} \le q_{d'} q_{z_1 z_2} \le q_{c_1} q_{c_2}/q_C \le C_Z^{2D_{\max}}. \tag{17.27}$$

## Which lines need work (typical defects)
* a line that looks like a formula but has no `$` — e.g. `si = r − Ai − B − t,   κi = M − 2r − 2ℓ − V − δ + Ai + B − R/2.`
* a shredded display equation, e.g. `Z M qh  yh  (17.28)` together with a `1` / `2πi` / `X` / `Z` fragment
  on neighbouring lines: fold them into ONE `$$...$$`.
* identifiers such as `rmax`, `sslot`, `Huse`, `Aker,1`, `Bcrude,init`, `qd′`, `CZ` inside Chinese prose:
  wrap just the symbols: ``掩码 $B_1$ 蕴含 $q_h \le q_{hf}^2 E \le Z^{H_{\text{use}}}$，``

## Self-check — mandatory, must report PASS
    cd /home/a/Downloads/25
    python3 tools/check_page.py NNN [NNN ...]

It verifies (a) the CJK character sequence is identical to the pre-edit snapshot
(`.out_snapshot/page_NNN.zh.md`), (b) `$` balance per line, (c) no un-typeset math left,
(d) no empty math delimiters.  Fix everything it reports as `!` (warnings `?` are advisory but
should normally be resolved too).  Do not report success until it prints PASS for all your pages,
unless a hard failure is genuinely unfixable — then quote it.

## Report back (exact format)
* `pages_fixed`: the page numbers you rewrote
* `display_restored`: how many `$$...$$` display equations you recovered
* `inline_wrapped`: roughly how many inline runs you wrapped
* `uncertain`: any formula whose structure you could not pin down from the geometry — quote the raw
  token line and say what you assumed (this list is what the parent agent re-checks)
* `check`: the last line printed by `check_page.py` for your pages
