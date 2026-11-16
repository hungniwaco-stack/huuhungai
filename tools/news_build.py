"""Build the daily AI news category from news-data/*.json.

Input  news-data/YYYY-MM-DD.json:
  {"date": "2026-11-15", "summary": "1-2 cau mo dau (<=160 ky tu)",
   "items": [{"title": "...", "body": "2-3 cau tu viet", "source_name": "...", "source_url": "https://..."}]}
Output tin-tuc/<date>.html, tin-tuc/index.html, homepage block, sitemap.xml.
Run from anywhere: python tools/news_build.py   (idempotent)
"""
import glob, html, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://huuhungai.com"
os.chdir(ROOT)
esc = lambda t: html.escape(t, quote=True)
dmy = lambda d: f"{d[8:10]}/{d[5:7]}/{d[:4]}"


def load(paths=None):
    days = []
    for p in sorted(paths or glob.glob("news-data/*.json"), reverse=True):
        d = json.load(io.open(p, encoding="utf-8"))
        date = d["date"]
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", date) and os.path.basename(p) == date + ".json", p
        assert 3 <= len(d["items"]) <= 10, f"{date}: need 3-10 items"
        assert 20 <= len(d["summary"]) <= 160 and not re.search(r'["&<>]', d["summary"]), f"{date}: summary"
        for it in d["items"]:
            assert it["source_url"].startswith("https://") and it["source_name"], f"{date}: source missing"
            assert len(it["title"]) <= 120 and 40 <= len(it["body"]) <= 600, f"{date}: {it['title'][:30]}"
        days.append(d)
    return days


def head_style():
    s = io.open("articles/cai-hermes-agent-don-gian-huong-dan-cho-nguoi-khong-chuyen-ky-thuat.html", encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    return css + ".news-item{border-top:1px solid #d9dde3;padding-top:6px;margin-top:22px}.news-src{font-size:.92rem;color:#5f6368}.news-src a{color:#1769aa;text-decoration:underline}.news-list{list-style:none;padding:0}.news-list li{border-top:1px solid #d9dde3;padding:14px 0}.news-list a{color:#1769aa;font-weight:700}"


BOOT = ('<script>try{var d=document.documentElement,t=localStorage.getItem("hh-theme");if(!t)t=matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";'
        'd.dataset.theme=t;var z=localStorage.getItem("hh-size");if(z)d.dataset.size=z}catch(e){document.documentElement.dataset.theme="dark"}</script>')
GTM = '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("consent","default",{analytics_storage:"denied",ad_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",wait_for_update:500});try{if(localStorage.getItem("hh-consent")==="granted")gtag("consent","update",{analytics_storage:"granted"})}catch(e){}gtag("js",new Date());</script><script async src="https://www.googletagmanager.com/gtm.js?id=GTM-TQP6WHPC"></script>'
OGIMG = '<meta property="og:image" content="https://huuhungai.com/assets/og-default.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Hữu Hùng AI: AI Automation thực chiến cho người Việt"><meta name="twitter:image" content="https://huuhungai.com/assets/og-default.png">'
FOOT = '<footer class="site-foot"><a href="/quyen-rieng-tu.html">Quyền riêng tư và cookie</a> · <a href="/tin-tuc/">Tin AI</a> · © Hữu Hùng AI</footer>'
ASSETS = '<link rel="stylesheet" href="/assets/display.css"><script src="/assets/display.js" defer></script>'
HEADER = ('<header class="site"><div class="wrap nav"><a class="brand" href="/">Hữu Hùng AI</a><nav><a href="/#topics">Chủ đề</a>'
          '<a href="/tin-tuc/">Tin AI</a></nav></div></header>')


def page(title, desc, url, body, date, css, kind="Article"):
    ld = {"@context": "https://schema.org", "@type": kind, "headline": title, "description": desc, "datePublished": date, "dateModified": date,
          "author": {"@type": "Person", "name": "Hữu Hùng"}, "publisher": {"@type": "Organization", "name": "Hữu Hùng AI"}, "mainEntityOfPage": url}
    return ('<!doctype html><html lang="vi"><head>' + GTM + '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{esc(title)} | Hữu Hùng AI</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="article"><meta property="og:site_name" content="Hữu Hùng AI"><meta property="og:locale" content="vi_VN">'
            f'<meta property="og:title" content="{esc(title)} | Hữu Hùng AI"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">' + OGIMG + '<meta name="twitter:card" content="summary_large_image"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
            f'{BOOT}<style>{css}</style><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>{ASSETS}</head>'
            f'<body>{HEADER}<main class="reader">{body}</main>' + FOOT + '</body></html>')


def day_page(d, css):
    date, items = d["date"], d["items"]
    title = f"Tin AI ngày {dmy(date)}: {items[0]['title']}"
    url = f"{SITE}/tin-tuc/{date}.html"
    parts = [f'<article class="article"><header><a class="back" href="/tin-tuc/">Tất cả bản tin</a><p class="code">TIN AI / HÀNG NGÀY</p>'
             f'<h1>Tin AI ngày {dmy(date)}</h1><p class="excerpt">{esc(d["summary"])}</p>'
             f'<p class="meta">Biên tập: Hữu Hùng · <time datetime="{date}">{date}</time> · {len(items)} tin</p></header><div>']
    for it in items:
        parts.append(f'<section class="news-item"><h2>{esc(it["title"])}</h2><p>{esc(it["body"])}</p>'
                     f'<p class="news-src">Nguồn: <a rel="noopener" href="{esc(it["source_url"])}">{esc(it["source_name"])}</a></p></section>')
    parts.append('<p class="news-src">Bản tin tóm tắt bằng lời của chúng tôi từ các nguồn đã dẫn. Hãy mở nguồn gốc để xem đầy đủ trước khi dựa vào thông tin.</p></div></article>')
    return title, url, page(title, d["summary"], url, "".join(parts), date, css)


def archive(days, css):
    lis = "".join(
        f'<li><a href="/tin-tuc/{d["date"]}.html">Tin AI ngày {dmy(d["date"])}</a><br><span class="news-src">'
        + esc(" · ".join(i["title"] for i in d["items"][:3])) + "</span></li>" for d in days)
    body = (f'<article class="article"><header><a class="back" href="/">Trang chủ</a><p class="code">TIN AI / HÀNG NGÀY</p><h1>Tin tức AI hàng ngày</h1>'
            f'<p class="excerpt">Bản tin ngắn mỗi ngày về mô hình, công cụ và thị trường AI, kèm nguồn gốc để bạn kiểm chứng.</p></header>'
            f'<ul class="news-list">{lis}</ul></article>')
    return page("Tin tức AI hàng ngày", "Bản tin ngắn mỗi ngày về mô hình, công cụ và thị trường AI, mỗi tin kèm nguồn gốc để bạn tự kiểm chứng.",
                f"{SITE}/tin-tuc/", body, days[0]["date"], css, "CollectionPage")


def home_block(days):
    d = days[0]
    cards = "".join(f'<a class="card" href="/tin-tuc/{d["date"]}.html"><span class="code">TIN AI</span><h2>{esc(i["title"])}</h2><small>{dmy(d["date"])}</small></a>'
                    for i in d["items"][:3])
    return ('<!--news-start--><section class="wrap" id="tin-ai"><div class="section-heading"><h2>Tin AI mới nhất</h2>'
            f'<p>Bản tin ngày {dmy(d["date"])}. <a href="/tin-tuc/" style="text-decoration:underline">Xem tất cả bản tin</a></p></div>'
            f'<div class="cluster compact">{cards}</div></section><!--news-end-->')


def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--check":  # validate drafts only, write nothing
        load(sys.argv[2:]); print("draft OK"); return
    days = load()
    if not days: sys.exit("no news-data")
    css = head_style()
    urls = {f"{SITE}/tin-tuc/": days[0]["date"]}
    for d in days:
        title, url, s = day_page(d, css)
        write(f"tin-tuc/{d['date']}.html", s); urls[url] = d["date"]
    write("tin-tuc/index.html", archive(days, css))
    # homepage
    h = io.open("index.html", encoding="utf-8", newline="").read()
    blk = home_block(days)
    if "<!--news-start-->" in h:
        h = re.sub(r"<!--news-start-->.*?<!--news-end-->", lambda m: blk, h, flags=re.S)
    else:
        anchor = '<section class="wrap" id="automation-index"'
        assert anchor in h; h = h.replace(anchor, blk + anchor, 1)
    if 'href="tin-tuc/"' not in h:
        h = h.replace('<nav><a href="#topics">Chủ đề</a>', '<nav><a href="#topics">Chủ đề</a><a href="tin-tuc/">Tin AI</a>', 1)
    write("index.html", h)
    # sitemap
    sm = io.open("sitemap.xml", encoding="utf-8", newline="").read()
    for url, date in urls.items():
        entry = (f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{date}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.6</priority>\n  </url>\n")
        pat = re.compile(r"  <url>\s*<loc>" + re.escape(url) + r"</loc>.*?</url>\n", re.S)
        sm = pat.sub(lambda m: entry, sm) if pat.search(sm) else sm.replace("</urlset>", entry + "</urlset>")
    write("sitemap.xml", sm)
    print("built days:", [d["date"] for d in days], "| pages:", len(urls))


if __name__ == "__main__":
    main()
