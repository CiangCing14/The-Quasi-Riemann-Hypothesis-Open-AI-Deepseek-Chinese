#!/usr/bin/env python3
"""Scan the deliverable tree for leaked credentials.

Never prints a secret: hits are reported as file + line + a masked fingerprint
(first 3 chars, length).  Usage: python3 tools/scan_secrets.py [roots...]
"""
import os
import re
import sys

ROOTS = sys.argv[1:] or ['/home/a/Downloads/25']
CONFIG = '/home/a/.hermes/config.yaml'
TEXT_EXT = {'.py', '.md', '.txt', '.sh', '.json', '.yaml', '.yml', '.js', '.html', '.htm',
            '.env', '.log', '.csv', '.ini', '.cfg', '.toml', '.bak', '.premath', ''}

KEYISH = re.compile(r'\b(sk-[A-Za-z0-9_\-]{12,}|[A-Za-z0-9_\-]{32,})\b')
ASSIGN = re.compile(r'(?i)(api[_-]?key|apikey|secret|token|password|passwd|credential|authorization)'
                    r'\s*[:=]\s*["\']?([^\s"\',]{8,})')


def mask(s):
    return '%s…(%d chars)' % (s[:3], len(s))


def config_secrets():
    out = []
    try:
        txt = open(CONFIG, encoding='utf-8').read()
    except OSError:
        return out
    for m in ASSIGN.finditer(txt):
        out.append(m.group(2))
    for m in KEYISH.finditer(txt):
        out.append(m.group(1))
    seen, uniq = set(), []
    for s in out:
        if s not in seen and len(s) >= 12:
            seen.add(s)
            uniq.append(s)
    return uniq


def main():
    secrets = config_secrets()
    print('credentials read from %s : %d candidate value(s) [values masked]' % (CONFIG, len(secrets)))
    for s in secrets:
        print('   fingerprint %s' % mask(s))

    print()
    print('--- literal occurrences in the deliverable tree ---')
    total = 0
    for root in ROOTS:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules')]
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                ext = os.path.splitext(fn)[1]
                if ext not in TEXT_EXT:
                    continue
                try:
                    data = open(p, encoding='utf-8', errors='ignore').read()
                except OSError:
                    continue
                hits = []
                for s in secrets:
                    n = data.count(s)
                    if n:
                        hits.append((mask(s), n))
                    elif len(s) >= 20:
                        pre = s[:12]
                        if pre in data:
                            hits.append((mask(s) + ' [%d-char prefix]' % len(pre), data.count(pre)))
                if hits:
                    total += 1
                    print('  %s' % p)
                    for h in hits:
                        print('        %s x%d' % h)
    print('files with a literal credential: %d' % total)

    print()
    print('--- generic key-shaped strings anywhere (masked) ---')
    for root in ROOTS:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules')]
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                if os.path.splitext(fn)[1] not in TEXT_EXT:
                    continue
                try:
                    data = open(p, encoding='utf-8', errors='ignore').read()
                except OSError:
                    continue
                for m in re.finditer(r'\bsk-[A-Za-z0-9_\-]{8,}', data):
                    print('  %s : %s' % (p, mask(m.group(0))))
    print('done')


main()
