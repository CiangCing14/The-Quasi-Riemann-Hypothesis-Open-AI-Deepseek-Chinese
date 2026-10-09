#!/usr/bin/env python3
"""Assemble translated pages -> single HTML with rendered math -> (Chrome prints to PDF)."""
import os, re, glob, html, hashlib, base64, json, sys, subprocess

ROOT = '/home/a/Downloads/25'
OUTD = os.path.join(ROOT, 'out')
BUILD = os.path.join(ROOT, 'build')
MATHD = os.path.join(BUILD, 'math')
os.makedirs(MATHD, exist_ok=True)

import warnings
warnings.filterwarnings('ignore')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DPI = 200
BASE_PT = 10.5

GREEK = {'alpha':'α','beta':'β','gamma':'γ','delta':'δ','epsilon':'ε','varepsilon':'ε','zeta':'ζ',
 'eta':'η','theta':'θ','vartheta':'ϑ','iota':'ι','kappa':'κ','lambda':'λ','mu':'μ','nu':'ν','xi':'ξ',
 'pi':'π','varpi':'ϖ','rho':'ρ','varrho':'ϱ','sigma':'σ','varsigma':'ς','tau':'τ','upsilon':'υ',
 'phi':'φ','varphi':'φ','chi':'χ','psi':'ψ','omega':'ω','Gamma':'Γ','Delta':'Δ','Theta':'Θ',
 'Lambda':'Λ','Xi':'Ξ','Pi':'Π','Sigma':'Σ','Upsilon':'Υ','Phi':'Φ','Psi':'Ψ','Omega':'Ω'}
SYM = {'mid':'∣','nmid':'∤','equiv':'≡','mapsto':'↦','to':'→','times':'×','cdot':'·','le':'≤','leq':'≤',
 'ge':'≥','geq':'≥','ne':'≠','neq':'≠','in':'∈','notin':'∉','subset':'⊂','subseteq':'⊆','cup':'∪',
 'cap':'∩','infty':'∞','partial':'∂','nabla':'∇','pm':'±','mp':'∓','approx':'≈','sim':'∼','simeq':'≃',
 'ldots':'…','dots':'…','cdots':'⋯','forall':'∀','exists':'∃','wedge':'∧','vee':'∨','neg':'¬',
 'prod':'∏','sum':'∑','int':'∫','oint':'∮','sqrt':'√','langle':'⟨','rangle':'⟩','ll':'≪','gg':'≫',
 'asymp':'≍','propto':'∝','perp':'⊥','parallel':'∥','circ':'∘','ast':'∗','star':'⋆','oplus':'⊕',
 'otimes':'⊗','emptyset':'∅','angle':'∠','triangle':'△','prime':'′','colon':':','quad':' ',
 'qquad':'  ','ell':'ℓ','hbar':'ℏ','Re':'ℜ','Im':'ℑ','Vert':'‖','vert':'|','Longrightarrow':'⟹',
 'longrightarrow':'⟶','leftarrow':'←','setminus':'\\','varnothing':'∅','lesssim':'≲','gtrsim':'≳'}
U2L = {v: '\\' + k for k, v in GREEK.items()}
U2L.update({'−':'-','×':'\\times ','·':'\\cdot ','≡':'\\equiv ','≤':'\\le ','≥':'\\ge ','→':'\\to ',
            '↦':'\\mapsto ','∈':'\\in ','∞':'\\infty ','∑':'\\sum ','∏':'\\prod ','∫':'\\int ',
            '√':'\\surd ','ℜ':'\\Re ','μ':'\\mu ','𝒪':'O','‖':'\\Vert '})
COMPLEX = re.compile(r'\\(frac|sum|prod|int|oint|sqrt|begin|binom|overline|underline|substack|cfrac|dfrac|tfrac|stackrel|overset|underset|matrix|array|cases|operatorname\*?)\b')
ENV_RE = re.compile(r'\\begin\{(matrix|pmatrix|bmatrix|vmatrix|smallmatrix|cases|array|aligned|align|gathered|gather|split)\}(\{[^{}]*\})?(.*?)\\end\{\1\}', re.S)
BAD_OPS = re.compile(r'\\(limsup|liminf|argmin|argmax|sup|inf|gcd|lcm|deg|dim|ker|hom|rank|tr|sgn|vol|ord|Pr)\b')
KNOWN_OPS = {'max','min','lim','log','ln','exp','det','sin','cos','tan','cot','sec','csc','sinh',
             'cosh','tanh','arcsin','arccos','arctan','prod','sum','int','sqrt','frac','binom'}

_cache = {}
stats = {'display': 0, 'inline_img': 0, 'inline_html': 0, 'fail': 0}
_fails = []


def _png(latex, fontsize, key_extra=''):
    key = hashlib.sha1((latex + '|%.2f' % fontsize + key_extra).encode()).hexdigest()[:16]
    if key in _cache:
        return _cache[key]
    path = os.path.join(MATHD, key + '.png')
    try:
        fig = plt.figure(figsize=(0.01, 0.01))
        fig.text(0, 0, '$%s$' % latex, fontsize=fontsize, color='black')
        fig.savefig(path, dpi=DPI, transparent=True, bbox_inches='tight', pad_inches=0.01)
        plt.close(fig)
    except Exception:
        try:
            plt.close('all')
        except Exception:
            pass
        _cache[key] = None
        return None
    from PIL import Image
    with Image.open(path) as im:
        w, h = im.size
    _cache[key] = (path, w, h, DPI)
    return _cache[key]


# ---------------- MathJax: real LaTeX typesetting (offline, via node) ----------------
MJX_REQ = {}          # key -> (latex, display)
MJX_SVG = {}          # key -> svg markup, or {'error':...}
_MJX_CACHE = os.path.join(BUILD, 'math_svg_cache.json')
T_IN = '\x01MJX:%s\x01'
TOKEN_RE = re.compile('\x01MJX:([0-9a-f]+)\x01')


def mkey(latex, display):
    k = hashlib.sha1((('D' if display else 'I') + latex).encode()).hexdigest()[:14]
    if k not in MJX_REQ:
        MJX_REQ[k] = (latex, bool(display))
    return k


def mtok(latex, display):
    return T_IN % mkey(latex, display)


def render_mjx_batch():
    """Render every collected formula with MathJax in ONE node call (cached on disk)."""
    global MJX_SVG
    cache = {}
    if os.path.exists(_MJX_CACHE):
        try:
            cache = json.load(open(_MJX_CACHE, encoding='utf-8'))
        except Exception:
            cache = {}
    need = [k for k in MJX_REQ if k not in cache]
    if need:
        payload = [{'key': k, 'latex': MJX_REQ[k][0], 'display': MJX_REQ[k][1]} for k in need]
        with open('/tmp/mjx_in.json', 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False)
        r = subprocess.run(['node', os.path.join(ROOT, 'mjx', 'tex2svg.js'),
                            '/tmp/mjx_in.json', '/tmp/mjx_out.json'],
                           capture_output=True, text=True, cwd=os.path.join(ROOT, 'mjx'))
        print('mathjax:', (r.stderr or '').strip().splitlines()[-1][:160] if r.stderr else 'ok')
        cache.update(json.load(open('/tmp/mjx_out.json', encoding='utf-8')))
        json.dump(cache, open(_MJX_CACHE, 'w', encoding='utf-8'), ensure_ascii=False)
    MJX_SVG = cache
    bad = [k for k in MJX_REQ if not (cache.get(k) or {}).get('svg')]
    print('formulas: %d requested, %d typeset, %d fell back' % (len(MJX_REQ), len(MJX_REQ) - len(bad), len(bad)))
    return bad


def math_fallback(latex, display):
    """matplotlib image (then plain text) - only for formulas MathJax rejects."""
    if display:
        lines = [latex] if '\\begin{' in latex else [l.strip() for l in re.split(r'\\\\', latex) if l.strip()]
        out = []
        for l in lines:
            if _cjkin(l):
                for kind, s in split_cjk_math(l):
                    if kind == 't':
                        out.append('<span class="mtxt">%s</span>' % html.escape(s))
                    else:
                        r = _png(to_mathtext(s), 11.5)
                        if r:
                            p, w, h, dpi = r
                            out.append('<img src="%s" style="height:%.1fpt">' % (_datauri(p), h / dpi * 72.0))
                continue
            r = _png(to_mathtext(l), 11.5)
            if r:
                p, w, h, dpi = r
                hpt, wpt = h / dpi * 72.0, w / dpi * 72.0
                if wpt > 470:
                    hpt *= 470.0 / wpt
                out.append('<img src="%s" style="height:%.1fpt">' % (_datauri(p), hpt))
            else:
                out.append('<div class="mraw">%s</div>' % html.escape(latex_to_text(l)))
        return ''.join(out)
    if _cjkin(latex):
        out = []
        for kind, s in split_cjk_math(latex):
            if kind == 't':
                out.append('<span class="mtxt">%s</span>' % html.escape(s))
            else:
                r = _png(to_mathtext(s), 11)
                if r:
                    p, w, h, dpi = r
                    out.append('<img class="mi" src="%s" style="height:%.2fem">' % (_datauri(p), (h / dpi * 72.0) / BASE_PT))
        return ''.join(out)
    r = _png(to_mathtext(latex), 11)
    if r:
        p, w, h, dpi = r
        return '<img class="mi" src="%s" style="height:%.2fem">' % (_datauri(p), (h / dpi * 72.0) / BASE_PT)
    return '<span class="mraw">%s</span>' % html.escape(latex_to_text(latex))


def substitute_math(html_text):
    def rep(m):
        k = m.group(1)
        svg = (MJX_SVG.get(k) or {}).get('svg')
        if svg:
            return svg
        latex, display = MJX_REQ.get(k, ('', False))
        stats['fail'] += 1
        _fails.append(latex)
        return math_fallback(latex, display)
    return TOKEN_RE.sub(rep, html_text)


def repl_pmod(t):
    out, i = [], 0
    while True:
        j = t.find('\\pmod', i)
        if j < 0:
            out.append(t[i:])
            break
        out.append(t[i:j])
        k = j + 5
        while k < len(t) and t[k] == ' ':
            k += 1
        arg = ''
        if k < len(t) and t[k] == '{':
            depth, m = 0, k
            while m < len(t):
                if t[m] == '{':
                    depth += 1
                elif t[m] == '}':
                    depth -= 1
                    if depth == 0:
                        break
                m += 1
            arg, i = t[k + 1:m], m + 1
        else:
            m2 = re.match(r'[A-Za-z0-9]+', t[k:])
            arg = m2.group(0) if m2 else ''
            i = k + len(arg)
        out.append('\\ (\\mathrm{mod}\\ %s)' % arg)
    return ''.join(out)


def flatten_env(m):
    env = m.group(1)
    body = m.group(3) or ''
    if env in ('aligned', 'align', 'gathered', 'gather', 'split'):
        return body
    rows = [r.strip() for r in re.split(r'\\\\', body) if r.strip()]
    cells = [[c.strip() for c in r.split('&')] for r in rows]
    flat = ';\\ '.join(',\\ '.join(c for c in row if c) for row in cells if row)
    if env == 'pmatrix':
        return '\\left(' + flat + '\\right)'
    if env == 'bmatrix':
        return '\\left[' + flat + '\\right]'
    if env == 'vmatrix':
        return '\\left|' + flat + '\\right|'
    if env == 'cases':
        return '\\{ ' + flat + ' \\}'
    return flat


def to_mathtext(tex, aggressive=False):
    t = tex
    t = re.sub(r'\\tag\*?\{[^}]*\}', '', t)
    t = re.sub(r'\\qquad\s*\(\s*\d+\.\d+[a-z]?\s*\)', '', t)
    t = re.sub(r'\\begin\{(aligned|align|gathered|gather|split)\}', '', t)
    t = re.sub(r'\\end\{(aligned|align|gathered|gather|split)\}', '', t)
    t = ENV_RE.sub(flatten_env, t)
    t = re.sub(r'\\boxed\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\underbrace\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\overbrace\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\under(?:line|bar)\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\(?:bigg?l|bigg?r|Bigg?l|Bigg?r|bigg|Bigg|big|Big)\b', '', t)
    t = repl_pmod(t)
    t = re.sub(r'\\xrightarrow\{[^{}]*\}', r'\\to ', t)
    t = re.sub(r'\\xleftarrow\{[^{}]*\}', r'\\leftarrow ', t)
    t = re.sub(r'\\substack\{([^{}]*)\}', lambda m: m.group(1).replace('\\\\', ','), t)
    t = re.sub(r'\\text\{([^{}]*)\}', r'\\mathrm{\1}', t)
    t = re.sub(r'\\operatorname\*?\{([^{}]*)\}', r'\\mathrm{\1}', t)
    t = t.replace('\\bmod', '\\ \\mathrm{mod}\\ ')
    t = t.replace('\\tfrac', '\\frac').replace('\\dfrac', '\\frac').replace('\\cfrac', '\\frac')
    t = t.replace('\\lVert', '\\Vert').replace('\\rVert', '\\Vert')
    t = t.replace('\\lvert', '|').replace('\\rvert', '|')
    t = re.sub(r'\\le(?![A-Za-z])', '\\\\leq', t)
    t = re.sub(r'\\ge(?![A-Za-z])', '\\\\geq', t)
    t = re.sub(r'\\ne(?![A-Za-z])', '\\\\neq', t)
    t = t.replace('\\not=', '\\neq')
    t = re.sub(r'\\min(?![A-Za-z])', '\\\\min', t)
    t = BAD_OPS.sub(lambda m: '\\mathrm{%s}' % m.group(1), t)
    t = re.sub(r'\\(?:displaystyle|textstyle|scriptstyle|limits|nolimits|notag|nonumber|label|hspace|vspace)\b', '', t)
    t = re.sub(r'\\hspace\*?\{[^}]*\}', '', t)
    t = t.replace('&', '')
    if aggressive:
        t = re.sub(r'\\([A-Za-z]+)(?![A-Za-z])',
                   lambda m: m.group(0) if m.group(1) in KNOWN_OPS or m.group(1) in GREEK or m.group(1) in SYM else '', t)
        t = t.replace('\\{', '(').replace('\\}', ')')
    for u, l in U2L.items():
        t = t.replace(u, l)
    t = re.sub(r'\\;|\\,|\\!|\\ ', ' ', t)
    t = re.sub(r'\\(?:left|right)\s*([\\{}()\[\]|.])?', lambda m: (m.group(1) or ''), t)
    t = re.sub(r'\\math(?:rm|it|bf|cal|bb|frak|sf|tt)\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'[{}]', '', t) if aggressive else t
    return t


SUP = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹',
       '+':'⁺','-':'⁻','n':'ⁿ','i':'ⁱ'}
SUB = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉',
       '+':'₊','-':'₋','a':'ₐ','e':'ₑ','i':'ᵢ','j':'ⱼ','k':'ₖ','n':'ₙ','p':'ₚ','t':'ₜ','x':'ₓ'}


def latex_to_text(tex):
    """Readable plain-text fallback for math we cannot render."""
    t = tex
    t = re.sub(r'\\begin\{(matrix|pmatrix|bmatrix|vmatrix|smallmatrix|cases|array)\}(\{[^{}]*\})?', ' ( ', t)
    t = re.sub(r'\\end\{(matrix|pmatrix|bmatrix|vmatrix|smallmatrix|cases|array)\}', ' ) ', t)
    t = re.sub(r'\\begin\{[^}]*\}|\\end\{[^}]*\}', ' ', t)
    for _ in range(3):
        t = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1)/(\2)', t)
    t = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', t)
    t = re.sub(r'\\sqrt\s+(\w)', r'√\1', t)
    t = re.sub(r'\\(?:text|mathrm|mathbf|mathit|mathcal|mathbb|operatorname)\*?\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\tag\*?\{([^{}]*)\}', r'  (\1)', t)
    t = re.sub(r'\\qquad\s*\(\s*(\d+\.\d+[a-z]?)\s*\)', r'    (\1)', t)
    t = re.sub(r'\\(?:left|right)\s*', '', t)
    t = t.replace('&', ' ').replace('\\\\', ' ; ')
    t = re.sub(r'\\pmod\{?([^}$]+?)\}?(?![^{]*\})', r' (mod \1)', t)
    t = t.replace('\\bmod', ' mod ')
    for k, v in sorted(GREEK.items(), key=lambda kv: -len(kv[0])):
        t = t.replace('\\' + k, v)
    for k, v in sorted(SYM.items(), key=lambda kv: -len(kv[0])):
        t = re.sub(r'\\' + k + r'(?![A-Za-z])', lambda m, v=v: v, t)
    t = re.sub(r'\^(?:\{([^{}]*)\}|(\w))',
               lambda m: ''.join(SUP.get(c, c) if all(c in SUP for c in (m.group(1) or m.group(2))) else '^(' + (m.group(1) or m.group(2)) + ')'
                                 for c in [m.group(1) or m.group(2)])[0:400], t)
    t = re.sub(r'_(?:\{([^{}]*)\}|(\w))',
               lambda m: ''.join(SUB.get(c, c) if all(c in SUB for c in (m.group(1) or m.group(2))) else '_(' + (m.group(1) or m.group(2)) + ')'
                                 for c in [m.group(1) or m.group(2)])[0:400], t)
    t = re.sub(r'\\[A-Za-z]+', lambda m: KNOWN_OPS and '', t)
    t = t.replace('{', '').replace('}', '').replace('\\', '')
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def render_math(tex, fontsize):
    r = _png(to_mathtext(tex), fontsize)
    if r is None:
        r = _png(to_mathtext(tex, aggressive=True), fontsize, key_extra='|agg')
    return r


# ---------------- inline latex -> html (simple constructs only) ----------------
def _tok_latex(s):
    out = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+|.)', s[i:])
            if not m:
                return None
            name = m.group(1)
            if name in GREEK:
                out.append(('txt', GREEK[name]))
            elif name in SYM:
                out.append(('txt', SYM[name]))
            elif name in ('mathrm', 'text', 'operatorname', 'mathcal', 'mathbb', 'mathbf', 'mathit'):
                m2 = re.match(r'\*?\{([^{}]*)\}', s[i + len(m.group(0)):])
                if not m2:
                    return None
                out.append(('txt', m2.group(1)))
                i += len(m.group(0)) + len(m2.group(0))
                continue
            elif name in (',', ';', '!', ' '):
                out.append(('txt', ' ' if name == ' ' else ''))
            else:
                return None
            i += len(m.group(0))
            continue
        if c in '{}':
            out.append(('txt', c))
            i += 1
            continue
        if c in '^_':
            j = i + 1
            if j < n and s[j] == '{':
                k = s.find('}', j)
                if k < 0:
                    return None
                arg, i = s[j + 1:k], k + 1
            elif j < n:
                arg, i = s[j], j + 1
            else:
                return None
            out.append(('sup' if c == '^' else 'sub', arg))
            continue
        if c.isalpha():
            out.append(('it', c))
            i += 1
            continue
        out.append(('txt', c))
        i += 1
    return out


GREEK_R = {v: k for k, v in GREEK.items()}


def tokens_to_html(tokens):
    parts = []
    for kind, val in tokens:
        if kind in ('sup', 'sub'):
            inner = _tok_latex(val)
            if inner is None:
                return None
            h = tokens_to_html(inner)
            if h is None:
                return None
            parts.append('<%s>%s</%s>' % (kind, h, kind))
        elif kind == 'it':
            parts.append('<i>%s</i>' % (GREEK_R.get(val, val)))
        else:
            parts.append(html.escape(val))
    return ''.join(parts)


def inline_html(tex):
    if COMPLEX.search(tex):
        return None
    t = re.sub(r'\\(?:left|right)\s*', '', tex)
    toks = _tok_latex(t)
    if toks is None:
        return None
    return tokens_to_html(toks)


def _datauri(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()


def _cjkin(s):
    return any('\u3400' <= c <= '\u9fff' or '\uff00' <= c <= '\uffef' for c in s)


CJK_RUN = re.compile(r'[\u3000-\u303f\u3400-\u9fff\uff00-\uffef]+')


def split_cjk_math(tex):
    """Split math containing Chinese text into renderable math / literal text parts."""
    segs, pos = [], 0
    for m in CJK_RUN.finditer(tex):
        before = tex[pos:m.start()]
        mm = re.search(r'\\(?:text|mathrm|mbox|textbf|operatorname)\*?\{([^{}]*)$', before)
        if mm:
            before = before[:mm.start()]
        segs.append(('m', before))
        segs.append(('t', m.group(0)))
        pos = m.end()
        if pos < len(tex) and tex[pos] == '}':
            pos += 1
    segs.append(('m', tex[pos:]))
    return [(k, s) for k, s in segs if s.strip()]


def _math_inline_img(seg, fontsize=11):
    r = render_math(seg, fontsize)
    if not r:
        return None
    path, w, h, dpi = r
    em = (h / dpi * 72.0) / BASE_PT
    return '<img class="mi" src="%s" style="height:%.2fem">' % (_datauri(path), em)


def inline_math(tex):
    if not _cjkin(tex):
        try:
            h = inline_html(tex)
        except Exception:
            h = None
        if h is not None and not re.search(r'[{}\\]', re.sub(r'<[^>]+>', '', h)):
            stats['inline_html'] += 1
            return '<span class="m">%s</span>' % h
    stats['inline_img'] += 1
    return mtok(tex, False)


def display_math(tex):
    tag = ''
    mt = re.search(r'\\tag\*?\{([^}]*)\}', tex)
    if mt:
        tag = mt.group(1)
    else:
        mt = re.search(r'\\qquad\s*\(\s*(\d+\.\d+[a-z]?)\s*\)', tex)
        if mt:
            tag = mt.group(1)
    tex = re.sub(r'\\tag\*?\{[^}]*\}', '', tex)
    tex = re.sub(r'\\qquad\s*\(\s*\d+\.\d+[a-z]?\s*\)', '', tex)
    lines = [l.strip() for l in re.split(r'\\\\', tex) if l.strip()]
    if not lines:
        return ''
    stats['display'] += 1
    tagh = '<span class="eqno">(%s)</span>' % html.escape(tag) if tag else ''
    return '<div class="eq">%s%s</div>' % (mtok(tex.strip(), True), tagh)


# ---------------- page -> html ----------------
DISPLAY_RE = re.compile(r'\$\$(.+?)\$\$|\\\[(.+?)\\\]', re.S)


def page_to_html(text, split=True, heads=True, toc=False, bib=False):
    items, pos = [], 0
    for m in DISPLAY_RE.finditer(text):
        seg = m.group(1) if m.group(1) is not None else m.group(2)
        items.append(('t', text[pos:m.start()]))
        items.append(('eq', seg))
        pos = m.end()
    items.append(('t', text[pos:]))
    out = []
    for kind, seg in items:
        if kind == 'eq':
            out.append(('eq', display_math(seg)))
        else:
            if split and toc:
                seg = toc_mark(seg)
            if split and bib:
                seg = ref_mark(seg)
            if heads:
                seg = mark_headings(seg)
            for b in page_blocks(seg):
                if split:
                    out.extend(('blk', h) for h in block_html(b))
                else:
                    out.append(('blk', '<p>%s</p>' % inline_pass(b.replace('\n', ' '))))
    return out


def page_blocks(text):
    text = re.sub(r'\n{3,}', '\n\n', text)
    keep = []
    for ln in text.split('\n'):
        s = ln.strip()
        if s and re.fullmatch(r'[.·…\s]+', s):
            continue           # TOC dot leaders
        if re.fullmatch(r'\d{1,3}', s):
            continue           # stray page number
        keep.append(ln)        # blank lines are paragraph separators - keep them
    text = '\n'.join(keep)
    return [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]


def inline_pass(text):
    out, i = [], 0
    for m in re.finditer(r'\$([^$]+?)\$', text):
        out.append(html.escape(text[i:m.start()]))
        out.append(inline_math(m.group(1)))
        i = m.end()
    out.append(html.escape(text[i:]))
    return ''.join(out)


E_DOTS = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(.+?)'
                    r'[ \u3000]*((?:[.．·][ \u3000]*){3,})[ \u3000]*(\d{1,3})?[ \u3000]*$')
E_PLAIN = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(\S.*?)'
                     r'[ \u3000]+(\d{1,3})[ \u3000]*$')
BARE_NUM = re.compile(r'^[ \u3000]*(\d{1,3})[ \u3000]*$')
EN_TOC_LINE = re.compile(r'^([ \u3000]*)(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(.+?)[ \u3000]*'
                         r'((?:\.\s*){3,})[ \u3000]*(\d{1,3})\s*$')


def match_entry(ln):
    """-> (num, title, page) for a table-of-contents line, else None."""
    m = E_DOTS.match(ln)
    if m:
        title, page = m.group(3).strip().rstrip(' .．·'), m.group(5)
        if len(re.findall(r'[\u4e00-\u9fff]', title)) < 2:
            return None
        return m.group(2), title, page
    m = E_PLAIN.match(ln)
    if m:
        title, page = m.group(3).strip(), m.group(4)
        if len(re.findall(r'[\u4e00-\u9fff]', title)) < 2 or re.search(r'[。，；：]', title):
            return None
        return m.group(2), title, page
    return None


REF_LINE = re.compile(r'^\s*\[\d+\]\s')


def is_bib_page(text):
    return sum(1 for ln in text.split('\n') if REF_LINE.match(ln)) >= 3


def ref_mark(text):
    """Give every bibliography entry its own block (own line in the HTML)."""
    out, n = [], 0
    for i, ln in enumerate(text.split('\n')):
        if REF_LINE.match(ln) and i > 0 and out and out[-1].strip():
            out.append('')
        out.append(ln)
    return '\n'.join(out)


def is_toc_page(text):
    lines = text.split('\n')
    return ('目录' in text) or sum(1 for ln in lines if match_entry(ln)) >= 4


def load_en_toc():
    """number -> original page, from the English TOC (fills entries whose page number wrapped)."""
    m = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'pages', 'page_*.txt')))[:4]:
        try:
            txt = open(f, encoding='utf-8').read()
        except Exception:
            continue
        for ln in txt.split('\n'):
            mm = EN_TOC_LINE.match(ln)
            if mm:
                m.setdefault(mm.group(2), mm.group(5))
    return m


EN_TOC = {}


def toc_mark(text):
    """Turn table-of-contents lines into @@TOC@@ markers, one per line."""
    lines = text.split('\n')
    out, i = [], 0
    while i < len(lines):
        ent = match_entry(lines[i])
        if ent:
            num, title, page = ent
            if not page:                       # number wrapped to the next line in the PDF
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and BARE_NUM.match(lines[j]):
                    page, i = BARE_NUM.match(lines[j]).strip(), j
            if not page:
                page = EN_TOC.get(num, '')
            lvl = 1 if '.' not in num else min(num.count('.') + 1, 3)
            out += ['', '@@TOC@@%d@@%s@@%s@@%s' % (lvl, num, title, page), '']
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return '\n'.join(out)


def toc_row(marker):
    parts = marker.split('@@')
    lvl, num, title, page = parts[2], parts[3], parts[4], parts[5]
    return ('<div class="toc lvl%s"><span class="tn">%s</span>'
            '<span class="tt">%s</span><span class="lead"></span>'
            '<span class="tp">%s</span></div>' % (lvl, html.escape(num), inline_pass(title), html.escape(page)))


def is_heading(block):
    lines = [l for l in block.split('\n') if l.strip()]
    if len(lines) != 1:
        return None
    s = lines[0].strip()
    if len(s) > 70 or '。' in s:
        return None
    m = re.match(r'^(\d+(?:\.\d+)*)\s+\S', s)
    if m:
        return 'h%d' % (m.group(1).count('.') + 1)
    if re.match(r'^(?:[IVX]+|附录\s*[A-Z0-9]|第\s*\d+\s*[章部])[\s、.]', s):
        return 'h1'
    return None


TOC = []
TOC_NUMS = set()
HEAD_LINE = re.compile(r'^(\d+(?:\.\d+)*|[IVX]+)[ \u3000]+(\S.{0,32})$')


def is_head_line(line):
    """A standalone section-title line (Chinese title, no sentence punctuation)."""
    s = line.strip()
    m = HEAD_LINE.match(s)
    if not m:
        return None
    num, title = m.group(1), m.group(2)
    if re.search(r'[。，；：！？]', title) or title.endswith('的'):
        return None
    if len(re.findall(r'[\u4e00-\u9fff]', title)) < 2:
        return None          # maths fragments like "2 X X" / "4 (2π)2"
    if re.search(r'[$\\{}^_=<>|]', title):
        return None
    return num


def mark_headings(text):
    out = []
    for ln in text.split('\n'):
        if is_head_line(ln):
            out += ['', ln.strip(), '']
        else:
            out.append(ln)
    return '\n'.join(out)


def load_toc():
    """Titles from the translated table of contents: [(num, 'num title'), ...]."""
    out = []
    for p in sorted(glob.glob(os.path.join(OUTD, 'page_*.zh.md')))[:6]:
        txt = open(p, encoding='utf-8').read()
        if '目录' not in txt:
            continue
        for ln in txt.split('\n'):
            m = re.match(r'^\s*(\d+(?:\.\d+)*|[IVX]+)\s+(.{2,45}?)\s*(?:[.．·\s]{3,}\s*)?(\d{1,3})\s*$', ln)
            if m:
                num, title = m.group(1), m.group(2).strip(' .·')
                if title and not re.fullmatch(r'[.\s]*', title):
                    out.append((num, num + ' ' + title))
    return out


TOC = []


def split_title(block):
    """If the block starts with a known section title, split it off."""
    for num, full in TOC:
        if block == full:
            return full, ''
        if block.startswith(full):
            rest = block[len(full):]
            if rest[:1] in (' ', '\u3000') or '\u4e00' <= rest[:1] <= '\u9fff' or rest[:1] in '（(':
                return full, rest.strip()
    return None, block


def heading_level(num):
    return num.count('.') + 1


def block_html(block):
    out = []
    if block.lstrip().startswith('@@TOC@@'):
        rows = [l.strip() for l in block.split('\n') if l.strip()]
        if all(r.startswith('@@TOC@@') for r in rows):
            return [toc_row(r) for r in rows]
    num = is_head_line(block) if '\n' not in block else None
    if num:
        lvl = min(num.count('.') + 1, 3)
        return ['<h%d>%s</h%d>' % (lvl, inline_pass(block.strip()), lvl)]
    title, rest = split_title(block)
    if title:
        num = title.split(' ', 1)[0]
        lvl = min(heading_level(num), 3)
        out.append('<h%d>%s</h%d>' % (lvl, inline_pass(title), lvl))
        block = rest
    if not block:
        return out
    out.append('<p>%s</p>' % inline_pass(block.replace('\n', ' ')))
    return out


def main():
    global TOC, TOC_NUMS, EN_TOC
    pages = sorted(glob.glob(os.path.join(OUTD, 'page_*.zh.md')))
    if not pages:
        sys.exit('no translated pages yet')
    TOC = load_toc()
    TOC_NUMS = set(num for num, _ in TOC)
    EN_TOC = load_en_toc()
    TOC = sorted(TOC, key=lambda t: -len(t[1]))
    print('toc titles: %d | en-toc pages: %d' % (len(TOC), len(EN_TOC)))
    body = []
    for p in pages:
        n = int(os.path.basename(p)[5:8])
        text = open(p, encoding='utf-8').read().strip()
        if not text:
            continue
        text = text.replace('**', '')
        text = re.sub(r'^#{1,6}\s*', '', text, flags=re.M)
        toc_page = is_toc_page(text)
        bib_page = is_bib_page(text)
        for kind, htmlb in page_to_html(text, split=True, heads=not toc_page,
                                        toc=toc_page, bib=bib_page):
            if kind == 'blk' and re.match(r'^<h1>', htmlb) and n > 1:
                htmlb = '<div class="chapter"></div>' + htmlb
            body.append(htmlb)

    css = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm; }
html { font-family: 'Noto Serif CJK SC','Noto Serif',serif; }
body { font-size: %(pt)spt; line-height: 1.65; text-align: justify; color:#111; margin:0; }
h1,h2,h3 { font-weight: 700; line-height: 1.3; page-break-after: avoid; }
h1 { font-size: 1.55em; margin: 18pt 0 10pt; }
h2 { font-size: 1.25em; margin: 15pt 0 8pt; }
h3 { font-size: 1.1em; margin: 12pt 0 6pt; }
p { margin: 0 0 7pt; }
.eq { text-align:center; margin: 9pt 0; position: relative; page-break-inside: avoid; }
.eq img { vertical-align: middle; }
.eq svg { max-width: 96%%; height: auto; vertical-align: middle; }
svg text { font-family: 'Noto Serif CJK SC', 'DejaVu Serif', serif; }
.eqno { position: absolute; right: 0; top: 50%%; transform: translateY(-50%%); font-size: 0.85em; color:#333; }
.chapter { page-break-before: always; }
.m { font-style: normal; }
.m i { font-style: italic; }
.mi { vertical-align: -0.30em; }
.mraw { font-family: 'DejaVu Sans Mono', monospace; font-size: 0.9em; color:#222; text-align:left; padding-left: 12pt; }
.mtxt { font-family: 'Noto Serif CJK SC', serif; font-size: 0.97em; padding: 0 1pt; }
.toc { display: flex; align-items: baseline; margin: 0 0 2.5pt; font-size: 0.97em; page-break-inside: avoid; }
.toc .tn { flex: 0 0 auto; min-width: 3.2em; }
.toc .tt { flex: 0 1 auto; white-space: nowrap; }
.toc .lead { flex: 1 1 auto; border-bottom: 1px dotted #999; margin: 0 3pt; position: relative; top: -0.25em; min-width: 1.5em; }
.toc .tp { flex: 0 0 auto; text-align: right; min-width: 2.2em; }
.toc.lvl2 { padding-left: 1.8em; }
.toc.lvl3 { padding-left: 3.6em; }
.cover { text-align:center; padding-top: 55mm; page-break-after: always; }
.cover h1 { font-size: 2.0em; margin-bottom: 6mm; }
.cover .sub { font-size: 1.15em; color:#333; margin-bottom: 20mm; }
.cover .meta { font-size: 1em; color:#444; line-height: 1.9; }
.cover .note { margin-top: 40mm; font-size: 0.85em; color:#666; line-height: 1.7; text-align:left; }
""" % {'pt': BASE_PT}

    head = ['<h1>准黎曼假设：无零点半平面 Re(s) &gt; 7/8</h1>',
            '<div class="sub">利用立方 theta 反射与特征矩的两阶段证明</div>',
            '<div class="meta">原作者：OpenAI<br>2026 年 9 月 30 日<br>英文原文 199 页 · 简体中文机器翻译</div>',
            '<div class="note">本译本由 DeepSeek-V4.1-Flash 逐页机器翻译，公式依据 PDF 提取文本重排，'
            '保留原文公式编号。译文仅供参考，细节请以英文原文为准。</div>']

    doc = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
           '<title>准黎曼假设（中文译本）</title><style>%s</style></head><body>'
           '<div class="cover">%s</div>%s</body></html>' % (css, ''.join(head), '\n'.join(body)))
    render_mjx_batch()
    doc = substitute_math(doc)
    outp = os.path.join(BUILD, 'paper-zh-cn.html')
    with open(outp, 'w', encoding='utf-8') as f:
        f.write(doc)
    with open(os.path.join(BUILD, 'fails.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(_fails))
    print(json.dumps({'html': outp, 'bytes': len(doc), 'math': stats}, ensure_ascii=False))


if __name__ == '__main__':
    main()
