"""Minimal DeepSeek API helper (thinking mode DISABLED, per user instruction)."""
import json, os, time, urllib.request, urllib.error, yaml

CFG = '/home/a/.hermes/config.yaml'
BASE = 'https://api.deepseek.com/chat/completions'
MODEL = 'deepseek-v4-flash'

_key = None
def key():
    global _key
    if _key:
        return _key
    env = os.environ.get('DEEPSEEK_API_KEY')
    if env:
        _key = env.strip()
        return _key
    cfg = yaml.safe_load(open(CFG))
    pools = cfg.get('providers') or cfg.get('custom_providers') or []
    for p in pools:
        if 'api.deepseek.com' in str(p.get('base_url', '')):
            _key = (p.get('api_key') or p.get('name')).strip()
            break
    if not _key:
        raise SystemExit('no deepseek key in config')
    return _key


def call(messages, max_tokens=16000, temperature=None, retries=4, timeout=600):
    body = {
        'model': MODEL,
        'messages': messages,
        'max_tokens': max_tokens,
        'stream': False,
        'thinking': {'type': 'disabled'},   # <-- thinking mode OFF
    }
    if temperature is not None:
        body['temperature'] = temperature
    data = json.dumps(body, ensure_ascii=False).encode()
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                BASE, data=data,
                headers={'Content-Type': 'application/json',
                         'Authorization': 'Bearer ' + key()})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.loads(r.read())
            msg = d['choices'][0]['message']
            return msg.get('content') or '', d.get('usage', {})
        except Exception as e:
            last = e
            body_err = ''
            if isinstance(e, urllib.error.HTTPError):
                try:
                    body_err = e.read().decode()[:300]
                except Exception:
                    pass
            time.sleep(1.5 * (attempt + 1))
            print(f'  retry {attempt+1}: {type(e).__name__} {e} {body_err}', flush=True)
    raise RuntimeError(f'api failed: {last}')


if __name__ == '__main__':
    txt, u = call([{'role': 'user', 'content': 'Reply with exactly: OK'}], max_tokens=2000)
    print(repr(txt), u)
