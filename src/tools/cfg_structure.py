#!/usr/bin/env python3
"""Safe structural dump of config.yaml: key paths + masked leaf values."""
import yaml

CFG = '/home/a/.hermes/config.yaml'
d = yaml.safe_load(open(CFG, encoding='utf-8'))


def fmt(v):
    if isinstance(v, str):
        if len(v) >= 12:
            return '"%s…" (%d chars)' % (v[:3], len(v))
        return repr(v)
    return repr(v)


def walk(node, path=''):
    if isinstance(node, dict):
        for k, v in node.items():
            walk(v, '%s.%s' % (path, k) if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, '%s[%d]' % (path, i))
    else:
        print('%-52s %s' % (path, fmt(node)))


walk(d)
