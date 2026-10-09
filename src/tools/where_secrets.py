#!/usr/bin/env python3
"""Show WHERE in config.yaml each credential sits (key path + masked value only)."""
import yaml

CFG = '/home/a/.hermes/config.yaml'
SECRETISH = ('key', 'token', 'secret', 'password', 'passwd', 'credential', 'authorization')


def walk(node, path=''):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk(v, '%s.%s' % (path, k) if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, '%s[%d]' % (path, i))
    else:
        if isinstance(node, str) and len(node) >= 12 and any(s in path.lower() for s in SECRETISH):
            print('  %-46s %s…(%d chars)' % (path, node[:3], len(node)))


print('credential-bearing fields in %s (values masked):' % CFG)
walk(yaml.safe_load(open(CFG, encoding='utf-8')))
