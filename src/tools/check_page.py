#!/usr/bin/env python3
"""Verify a repaired translated page.

usage: python3 tools/check_page.py 129 [130 ...]

Checks, per page:
  a) CJK character sequence identical to the pre-edit snapshot (.out_snapshot/)
  b) dollar-sign balance per line, and an even number of $$ fences
  c) no un-typeset math left as plain text (heuristic: formula-looking lines,
     and identifiers such as rmax/sslot/tau_init outside math mode)
  d) no empty math delimiters
Exit status is non-zero if any page fails.
"""
import os
import re
import sys

ROOT = '/home/a/Downloads/25'
SNAP = os.path.join(ROOT, '.out_snapshot')

UNI = r'[πκτηδϵεζσλμνωΩ∈≤≥≪≫−√·×∑∏∫ΞΘΦΨΓΛΣΥ⌈⌉⊥∂′]'
EQN = re.compile(r'\(\d{1,2}\.\d{1,3}\)\s*$')
IDENT = re.compile(r'(?:[a-zA-Zα-ωΑ-Ω]\s?(?:max|min|init|crude|slot|ref|sup|pow|new|step|old|fib|count|cost|extra|mask|raw|use|tot)\b'
                   r'|κi|κb|si\b|bi\b|Ai\b|Bi\b|zi\b|ci\b|σ0|β∗|∆0|θp|ℓb|ϵp)')
CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\u3000-\u303f\uff01-\uff60]')


def strip_math(t):
    t = re.sub(r'\$\$.*?\$\$', ' \u0000 ', t, flags=re.S)
    t = re.sub(r'\$[^$\n]*\$', ' \u0001 ', t)
    return t


def cjk_seq(t):
    return ''.join(CJK.findall(strip_math(t)))


def check(page):
    name = 'page_%03d.zh.md' % page
    new_p = os.path.join(ROOT, 'out', name)
    old_p = os.path.join(SNAP, name)
    if not os.path.exists(new_p):
        return False, ['missing file %s' % new_p]
    if not os.path.exists(old_p):
        return False, ['no snapshot for %s (cannot verify text preservation)' % name]
    new = open(new_p, encoding='utf-8').read()
    old = open(old_p, encoding='utf-8').read()
    errs = []
    warns = []

    if cjk_seq(new) != cjk_seq(old):
        a, b = cjk_seq(old), cjk_seq(new)
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        errs.append('CJK text changed! first difference at %d: old ...%s  new ...%s'
                    % (i, a[max(0, i - 25):i + 25], b[max(0, i - 25):i + 25]))

    for i, ln in enumerate(new.split('\n'), 1):
        if len(re.findall(r'(?<!\$)\$(?!\$)', ln)) % 2:
            errs.append('line %d: odd number of $ : %s' % (i, ln.strip()[:90]))
    if len(re.findall(r'\$\$', new)) % 2:
        errs.append('odd number of $$ fences overall')
    # precise emptiness test: tokenise math regions ($$...$$ preferred over $...$)
    for m in re.finditer(r'\$\$(?P<d>.+?)\$\$|\$(?P<i>[^$]*)\$', new, flags=re.S):
        kind = 'display' if m.group('d') is not None else 'inline'
        if not (m.group('d') or m.group('i') or '').strip():
            errs.append('empty %s math region at offset %d' % (kind, m.start()))

    plain = strip_math(new)
    for i, ln in enumerate(plain.split('\n'), 1):
        s = ln.strip()
        if not s:
            continue
        n = len(re.findall(UNI, s))
        if (n >= 3 and re.search(r'[=≤≥≪∈]', s)) or EQN.search(s):
            errs.append('line %d still un-typeset math (n=%d): %s' % (i, n, s[:90]))
        for m in IDENT.finditer(s):
            if len(CJK.findall(s)) >= 10 and n < 2:
                warns.append('line %d maybe-inline math left plain: %r' % (i, m.group(0)))
            else:
                errs.append('line %d identifier %r left in plain text: %s' % (i, m.group(0), s[:80]))
    return (not errs), errs + ['(warn) ' + w for w in warns]


def main():
    pages = [int(a) for a in sys.argv[1:]]
    if not pages:
        print('usage: check_page.py <page> [page ...]')
        return 2
    bad = 0
    for p in pages:
        ok, msgs = check(p)
        hard = [m for m in msgs if not m.startswith('(warn)')]
        warn = [m for m in msgs if m.startswith('(warn)')]
        print('%s page_%03d  %s' % ('PASS' if ok else 'FAIL', p,
                                    ('%d warnings' % len(warn)) if warn else 'clean'))
        for m in hard:
            print('      ! %s' % m)
        for m in warn:
            print('      ? %s' % m)
        if not ok:
            bad += 1
    print('---- %d/%d pages pass ----' % (len(pages) - bad, len(pages)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
