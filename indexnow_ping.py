"""Push all canonical URLs to IndexNow (Bing/Yandex/Seznam/Naver) in one POST.

IndexNow needs:
  1. A key file hosted at https://luzentucuerpo.com/<KEY>.txt containing exactly
     the key (deployed with the site — see site/<KEY>.txt).
  2. A POST to https://api.indexnow.org/indexnow with the host + key + urlList.

Run AFTER the key file is live on the domain:
    python3 indexnow_ping.py
"""
from __future__ import annotations
import json
import urllib.request

KEY = "b95ba6055d330203b26848096f2d15c0"
HOST = "luzentucuerpo.com"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URLS = [
    f"https://{HOST}/",
    f"https://{HOST}/ghk/",
    f"https://{HOST}/resultados/",
    f"https://{HOST}/estudios/",
    f"https://{HOST}/en/",
    f"https://{HOST}/en/ghk/",
    f"https://{HOST}/en/results/",
    f"https://{HOST}/en/studies/",
]


def main():
    # 0. Sanity: the key file must be reachable, or IndexNow rejects the batch.
    # Send a browser UA — Cloudflare 403s the default python-urllib agent.
    _UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    try:
        _kreq = urllib.request.Request(KEY_LOCATION, headers={"User-Agent": _UA})
        served = urllib.request.urlopen(_kreq, timeout=15).read().decode().strip()
        if served != KEY:
            raise SystemExit(f"[abort] {KEY_LOCATION} serves {served!r}, expected {KEY!r}")
        print(f"[ok] key file live at {KEY_LOCATION}")
    except Exception as e:
        raise SystemExit(f"[abort] key file not reachable at {KEY_LOCATION}: {e}")

    body = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": URLS,
    }).encode()

    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            code = r.status
            print(f"[indexnow] HTTP {code} — {len(URLS)} URLs submitted")
    except urllib.error.HTTPError as e:
        code = e.code
        print(f"[indexnow] HTTP {code} — {e.read().decode()[:200]}")
    # 200 or 202 = accepted; 422 = key/url mismatch; 403 = key invalid.
    print("  200/202 = aceptado · 403 = llave inválida · 422 = URL/clave no coinciden")


if __name__ == "__main__":
    main()
