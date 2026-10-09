#!/usr/bin/env python3
"""Byte-level credential sweep: reads EVERY file (binary included) and looks for
each configured secret, plus its 12-char prefix, plus auth-header shapes.
Reports only file paths and masked fingerprints - never a secret value.
"""
import os
import re
import sys

CONFIG = '/home/a/.hermes/config.yaml'
ROOTS = sys.argv[1:] or ['/home/a/Downloads/25']
ASSIGN = re.compile(r'(?i)(api[_-]?key|apikey|secret|token|password|passwd|credential)'
                    r'\s*[:=]\s*["\']?([^\s"\',]{12,})')


def mask(s):
    return '%s…(%d)' % (s[:3].decode('utf-8', 'replace'), len(s))


def secrets():
    txt = open(CONFIG, encoding='utf-8').read()
    vals = [m.group(2).encode() for m in ASSIGN.finditer(txt)]
    return [v for v in dict.fromkeys(vals) if len(v) >= 12]


def main():
    secs = secrets()
    print('%d candidate credential(s) loaded [masked]' % len(secs))
    hits = 0
    scanned = 0
    for root in ROOTS:
        if not os.path.exists(root):
            continue
        if os.path.isfile(root):
            files = [root]
        else:
            files = []
            for dp, dn, fn in os.walk(root):
                dn[:] = [d for d in dn if d not in ('.git',)]
                files += [os.path.join(dp, f) for f in fn]
        for p in files:
            scanned += 1
            try:
                if os.path.getsize(p) > 20 * 1024 * 1024:
                    continue
                data = open(p, 'rb').read()
            except OSError:
                continue
            found = []
            for s in secs:
                if s in data:
                    found.append(mask(s) + ' FULL')
                elif s[:12] in data:
                    found.append(mask(s) + ' prefix')
            for pat in (b'Bearer ', b'Authorization'):
                if pat in data:
                    found.append(pat.decode() + ' header string')
            if found:
                hits += 1
                print('HIT %s  ->  %s' % (p, ', '.join(sorted(set(found)))))
    print('scanned %d files, %d with a hit' % (scanned, hits))


main()
