import re

ROOT = '/home/a/Downloads/25'
pages = [7, 8, 22, 25, 31, 32, 40, 42, 56, 58, 77, 82, 123, 129, 130, 132, 133, 136,
         140, 154, 175, 187, 191, 193]
EQ = re.compile(r'\((\d{1,2}\.\d{1,3})\)')


def nums(path):
    t = open(path, encoding='utf-8').read()
    return sorted(set(EQ.findall(t)), key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1])))


bad = 0
for n in pages:
    en = nums('%s/pages/page_%03d.txt' % (ROOT, n))
    zh = nums('%s/out/page_%03d.zh.md' % (ROOT, n))
    missing = [x for x in en if x not in zh]
    extra = [x for x in zh if x not in en]
    if missing or extra:
        bad += 1
        print('page_%03d  EN=%s' % (n, ','.join(en)))
        print('           ZH=%s' % ','.join(zh))
        if missing:
            print('           !! equation numbers LOST: %s' % ', '.join(missing))
        if extra:
            print('           ++ numbers not in EN: %s' % ', '.join(extra))
print('---- %d/%d pages have equation-number discrepancies ----' % (bad, len(pages)))
