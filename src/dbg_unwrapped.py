import glob, re

UNI = r'[πκτηδϵεζσλμνωΩ∈≤≥≪≫−√·×∑∏∫ΞΘΦΨΓΛΣΥ∅⁎⊥⌈⌉]'
SYM = r'[=≤≥≪≫∈]'
EQN = re.compile(r'\((\d{1,2}\.\d{1,3})\)\s*$')


def unwrapped(path):
    """Lines that are plainly a formula but were never wrapped in math mode."""
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.S)
    t = re.sub(r'\$[^$\n]*\$', ' ', t)
    hits = []
    for i, ln in enumerate(t.split('\n'), 1):
        s = ln.strip()
        if not s:
            continue
        n = len(re.findall(UNI, s))
        if (n >= 3 and re.search(SYM, s)) or EQN.search(s) or (n >= 6):
            hits.append((i, n, s[:100]))
    return hits


target = 'out/page_150.zh.md'
h = unwrapped(target)
print('== %s : %d unwrapped-math lines' % (target, len(h)))
for i, n, s in h:
    print('   L%-4d n=%d  %s' % (i, n, s))

print()
tot = 0
pages = []
for p in sorted(glob.glob('out/page_*.zh.md')):
    hh = unwrapped(p)
    if hh:
        pages.append((p, len(hh)))
        tot += len(hh)
print('== document-wide: %d pages, %d lines with un-wrapped math ==' % (len(pages), tot))
for p, c in pages:
    print('   %s  %d' % (p, c))
print()
# balance check on the repaired page
lines = open(target, encoding='utf-8').read().split('\n')
odd = [i + 1 for i, l in enumerate(lines) if len(re.findall(r'(?<!\$)\$(?!\$)', l)) % 2]
print('page_150: lines with odd $ count:', odd)
print('page_150: $$ fences:', len([l for l in lines if l.strip() == '$$']))
