"""Ping IndexNow (Bing, Yandex...) about changed URLs. The key is public by design (file /<key>.txt at the site root).
Usage: python tools/indexnow.py URL [URL...]   |   python tools/indexnow.py --since YYYY-MM-DD  (sitemap entries with lastmod >= date)
Run AFTER the deploy is live, because the search engine fetches the key file to verify ownership."""
import io, json, os, re, sys, urllib.request
KEY = "653a14e1af86f7862debdc2bf0dc45ec"
HOST = "huuhungai.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def urls_since(date):
    sm = io.open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return [u for u, d in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", sm) if d >= date]

def main():
    a = sys.argv[1:]
    urls = urls_since(a[1]) if a[:1] == ["--since"] else a
    assert urls and all(u.startswith("https://" + HOST + "/") for u in urls), "need https://%s/ URLs" % HOST
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": "https://%s/%s.txt" % (HOST, KEY), "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/IndexNow", body, {"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow", r.status, "urls:", len(urls))

if __name__ == "__main__":
    main()
