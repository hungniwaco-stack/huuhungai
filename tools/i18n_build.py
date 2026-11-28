"""Build the English version of huuhungai.com under /en/ and wire hreflang between languages.

Inputs (all in git):
  i18n/en/articles/<slug>.md      English article (front matter: title, desc, min; QUICK; ## headings; same mini-markdown as the Vietnamese drafts)
  i18n/en/privacy.md              English privacy page body (front matter: title, desc)
  news-data/<date>.json           optional "en": {"summary": str, "items": [{"title","body"}, ...]} (same order as the Vietnamese items)
Outputs: en/index.html, en/articles/*.html, en/news/*.html, en/privacy.html, hreflang links on the Vietnamese pages, /en/ URLs in sitemap.xml.
Run:  python tools/i18n_build.py          (idempotent; run after tools/news_build.py)
      python tools/i18n_build.py --check  (validate the English sources only, write nothing)
"""
import glob, html, io, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
from mdrender import render, inline
import add_sources
import related
SOURCES = add_sources.load()

SITE = "https://huuhungai.com"
BRAND = "Hữu Hùng AI"
esc = lambda t: html.escape(t, quote=True)

CAT = {"AI Agent": "AI Agents", "Cộng đồng AI": "AI Communities", "Năng suất với AI": "Productivity with AI", "Tin tức AI": "AI News",
       "Kinh doanh với AI": "AI for Business", "Lập trình với AI": "AI Coding", "Khóa học AI": "AI Courses", "Mô hình AI": "AI Models",
       "SEO bằng AI": "AI SEO", "Công cụ AI": "AI Tools", "Công cụ thiết kế AI": "AI Design Tools"}
TOPIC = {"All Posts": "All articles", "AI Agents": "AI Agents", "AI Courses": "AI Courses", "AI Communities": "AI Communities", "AI Tools": "AI Tools",
         "AI SEO": "AI SEO", "AI Coding": "AI Coding", "Productivity": "Productivity with AI", "AI Design Tools": "AI Design Tools",
         "AI Models": "AI Models", "AI Business": "AI for Business", "AI News": "AI News"}

HEADER = ('<header class="site"><div class="wrap nav"><a class="brand" href="/en/">' + BRAND + '</a><nav><a href="/en/#topics">Topics</a>'
          '<a href="/en/news/">AI News</a><a href="/en/#automation-index">All articles</a></nav></div></header>')
FOOT = ('<footer class="site-foot"><a href="/en/privacy.html">Privacy and cookies</a> · <a href="/en/news/">AI News</a> · © ' + BRAND + '</footer>')
OG_ALT = "Hữu Hùng AI: practical AI Automation"


def norm(t):
    t = t.lower().replace("đ", "d")
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", t).strip()


def rd(p):
    return io.open(p, encoding="utf-8", newline="").read()


def wr(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def sub1(pat, repl, s, flags=0):
    s2, n = re.subn(pat, lambda m: repl, s, count=1, flags=flags)
    assert n == 1, "pattern not found: " + pat
    return s2


def sub0(pat, repl, s, flags=0):
    return re.sub(pat, lambda m: repl, s, count=1, flags=flags)


# ---------------------------------------------------------------- english sources
def read_md(path):
    raw = rd(path).replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    meta = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
    return meta, m.group(2).strip("\n").split("\n")


def vi_facts(slug):
    s = rd(f"articles/{slug}.html")
    s = add_sources.BLOCK.sub("", s)
    a = s.index('<div itemprop="articleBody">'); b = s.index("</div></article>")
    body = s[a:b]
    return {"html": s,
            "date": re.search(r'datetime="(\d{4}-\d{2}-\d{2})"', s).group(1),
            "cat": re.search(r'<p class="code">(.*?)</p>', s).group(1),
            "h2": body.count("<h2"), "pre": body.count("<pre>"), "li": body.count("<li>"),
            "links": sorted(set(re.findall(r'<a href="([^"#/][^"]*\.html)"', body)))}


def load_articles():
    out, problems = {}, []
    for p in sorted(glob.glob("i18n/en/articles/*.md")):
        slug = os.path.basename(p)[:-3]
        if not os.path.exists(f"articles/{slug}.html"):
            problems.append(f"{slug}: no Vietnamese article"); continue
        meta, lines = read_md(p)
        v = vi_facts(slug)
        body, _ = render(lines, slug, problems, "articles", quick_label="Quick answer:")
        e = {"h2": body.count("<h2"), "pre": body.count("<pre>"), "li": body.count("<li>"),
             "links": sorted(set(re.findall(r'<a href="([^"#/][^"]*\.html)"', body)))}
        for k in ("h2", "pre", "li"):
            if e[k] != v[k]: problems.append(f"{slug}: {k} count {e[k]} differs from Vietnamese {v[k]}")
        if e["links"] != v["links"]: problems.append(f"{slug}: internal links differ")
        t, d = meta.get("title", ""), meta.get("desc", "")
        if not t or len(t) > 110: problems.append(f"{slug}: title missing or over 110 chars ({len(t)})")
        if not d or len(d) > 160 or re.search(r'["&<>]', d): problems.append(f"{slug}: desc missing, over 160 chars or has quotes/&/<> ({len(d)})")
        if re.search(r"[ạảãàáâậầấẩẫăắằặẳẵẹẻẽèéêệềếểễịỉĩìíọỏõòóôộồốổỗơợờớởỡụủũùúưựừứửữỵỷỹỳýđ]", body + t + d, re.I):
            problems.append(f"{slug}: Vietnamese characters left in the English text")
        out[slug] = {"title": t, "desc": d, "min": meta.get("min", "6"), "body": body, "date": v["date"], "cat": v["cat"], "vi": v["html"]}
    return out, problems


# ---------------------------------------------------------------- common head helpers
def hreflang(vi_url, en_url):
    return ('<link rel="alternate" hreflang="vi" href="%s"><link rel="alternate" hreflang="en" href="%s"><link rel="alternate" hreflang="x-default" href="%s">'
            % (vi_url, en_url, vi_url))


def en_head(vi_html, url, title, desc, vi_url, ld_extra=None):
    """Turn a Vietnamese page head into the English one (title, description, social tags, JSON-LD, hreflang)."""
    head = vi_html.split("</head>")[0].replace('<html lang="vi">', '<html lang="en">', 1)
    full = esc(title if BRAND in title else title + " | " + BRAND)
    head = sub1(r"<title>.*?</title>", "<title>" + full + "</title>", head, re.S)
    head = sub1(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + esc(desc) + '">', head)
    head = sub1(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="' + url + '">' + hreflang(vi_url, url), head)
    head = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", head)  # drop copied vi alternates, re-added after canonical
    head = head.replace('<link rel="canonical" href="' + url + '">', '<link rel="canonical" href="' + url + '">' + hreflang(vi_url, url) if hreflang(vi_url, url) not in head else '<link rel="canonical" href="' + url + '">', 1)
    head = sub0(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="' + full + '">', head)
    head = sub0(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="' + esc(desc) + '">', head)
    head = sub0(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="' + url + '">', head)
    head = sub0(r'<meta property="og:locale" content="[^"]*">', '<meta property="og:locale" content="en_US">', head)
    head = sub0(r'<meta property="og:image:alt" content="[^"]*">', '<meta property="og:image:alt" content="' + esc(OG_ALT) + '">', head)
    head = sub0(r'<meta name="twitter:title" content="[^"]*">', '<meta name="twitter:title" content="' + full + '">', head)
    head = sub0(r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="' + esc(desc) + '">', head)
    return head


def set_ld(head, **fields):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
    ld = json.loads(m.group(1))
    ld.update(fields)
    ld.pop("keywords", None)
    return head.replace(m.group(0), '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", 1)


# ---------------------------------------------------------------- articles
def article_page(slug, a, have=(), rel=""):
    # links to articles not translated yet fall back to the Vietnamese page
    a = dict(a, body=re.sub(r'href="([^"/#:]+)\.html"', lambda m: m.group(0) if m.group(1) in have else 'href="/articles/%s.html"' % m.group(1), a["body"]))
    url = f"{SITE}/en/articles/{slug}.html"; vi_url = f"{SITE}/articles/{slug}.html"
    head = en_head(a["vi"], url, a["title"], a["desc"], vi_url)
    head = set_ld(head, headline=a["title"], description=a["desc"], mainEntityOfPage=url, inLanguage="en", **({"dateModified": SOURCES[slug]["checked"]} if slug in SOURCES else {}),
                  articleSection=CAT.get(a["cat"].split(" / ")[-1], a["cat"].split(" / ")[-1]))
    code = a["cat"].split(" / ")[0] + " / " + CAT.get(a["cat"].split(" / ")[-1], a["cat"].split(" / ")[-1])
    return (head + "</head><body>" + HEADER + '<main class="reader"><article class="article" itemscope itemtype="https://schema.org/Article"><header>'
            '<a class="back" href="/en/#automation-index">Back to all articles</a><p class="code">' + esc(code) + '</p>'
            '<h1 itemprop="headline">' + esc(a["title"]) + '</h1><p class="excerpt" itemprop="description">' + esc(a["desc"]) + '</p>'
            '<p class="meta">By <span itemprop="author">Hữu Hùng</span> · Published: <time itemprop="datePublished" datetime="' + a["date"] + '">' + a["date"] +
            "</time> · " + a["min"] + " min read</p></header>" + a["body"] + (add_sources.section(SOURCES[slug], "en") if slug in SOURCES else "") + "</article>" + rel + "</main>" + FOOT + "</body></html>")


# ---------------------------------------------------------------- homepage
START_EN = ["New to AI agents", "Coding with AI", "Doing SEO with AI", "Choosing a tool"]  # same order as the Vietnamese "start" list


def home_page(arts):
    vi = rd("index.html")
    cards = re.findall(r'<a class="card article-card" href="articles/([^"]+)\.html" data-topic="([^"]*)" data-search="[^"]*"><span class="code">([^<]*)</span><h2>.*?</h2><p>.*?</p><small>(.*?) · (\d{4}-\d{2}-\d{2}) · (\d+) phút đọc</small></a>', vi, re.S)
    cards = [c for c in cards if c[0] in arts]
    start = re.findall(r'<li><a href="articles/([^"]+)\.html"><span>', re.search(r'<div class="start" id="start">.*?</ul></div>', vi, re.S).group(0))
    assert len(start) == len(START_EN), "start list changed: update START_EN"
    url = SITE + "/en/"
    title = BRAND + ": practical AI Automation"
    desc = "Hữu Hùng AI shares practical AI Automation, AI agents, AI SEO and workflow automation guides."
    head = en_head(vi, url, title, desc, SITE + "/")
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', "", head, flags=re.S)
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": BRAND + " - Automation Index", "inLanguage": "en",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/en/articles/{c[0]}.html", "name": arts[c[0]]["title"]} for i, c in enumerate(cards)]}
    head += '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>"
    counts = {}
    for c in cards: counts[c[1]] = counts.get(c[1], 0) + 1
    n = len(cards)
    chips = ['<a class="topic-chip active" href="#automation-index" data-filter="All Posts" title="All articles: %d in the %s library"><span>All articles</span><em>%d</em></a>' % (n, BRAND, n)]
    order = re.findall(r'data-filter="([^"]*)"', vi)
    for t in order:
        if t in ("All Posts", "AI News") or t not in counts: continue
        chips.append('<a class="topic-chip" href="#automation-index" data-filter="%s" title="%s: %d article%s in the %s library"><span>%s</span><em>%d</em></a>'
                     % (t, TOPIC[t], counts[t], "" if counts[t] == 1 else "s", BRAND, TOPIC[t], counts[t]))
    card_html = []
    for slug, topic, code, cat, date, mins in cards:
        a = arts[slug]; ccat = CAT.get(cat, cat)
        search = norm(a["title"] + " " + a["desc"] + " " + ccat + " " + TOPIC.get(topic, topic))
        card_html.append('<a class="card article-card" href="/en/articles/%s.html" data-topic="%s" data-search="%s"><span class="code">%s</span><h2>%s</h2><p>%s</p><small>%s · %s · %s min read</small></a>'
                         % (slug, topic, esc(search), code, esc(a["title"]), esc(a["desc"]), esc(ccat), date, mins))
    start_html = "".join('<li><a href="/en/articles/%s.html"><span>%s</span><strong>%s</strong></a></li>' % (s, label, esc(arts[s]["title"])) for s, label in zip(start, START_EN))
    body = ('<body id="top" class="home">' + HEADER + '<main><section class="wrap hero"><h1>Practical AI Automation</h1>'
            '<p>Guides and analysis on AI agents, coding with AI, AI SEO and work automation.</p></section>'
            '<section class="wrap" id="automation-index"><div class="toolbar"><input class="searchbox" id="article-search" type="search" placeholder="Search articles on AI agents, SEO, tools, workflows..." aria-label="Search articles">'
            '<button class="clear-btn" id="clear-search" type="button">Clear filter</button></div>'
            '<div class="topic-browser" id="topics"><div class="topic-chips">' + " ".join(chips) + '</div></div>'
            '<div class="start" id="start"><h2>Where to start</h2><ul>' + start_html + '</ul></div>'
            '<h2 class="list-title">Articles, newest first</h2><p class="result-line" id="result-status" aria-live="polite"></p>'
            '<div class="empty" id="empty-state">No matching articles. Try a broader keyword such as AI agents, AI SEO or AI tools.</div>'
            '<div class="cluster">' + " ".join(card_html) + '</div><button class="more-btn" id="show-more" type="button" hidden>Show more articles</button></section>'
            + en_news_block() +
            '<section class="wrap about" id="about"><h2>About the content</h2>'
            '<p>Many articles, especially those about specific tools, list their sources at the end with the date they were cross-checked. Some articles about methods do not have that section.</p>'
            '<p>AI products change quickly. Open the original sources and check again before following along, especially for install commands, pricing, access permissions and legal rules.</p></section></main>'
            '<script src="/assets/home.js" defer></script>' + FOOT + "</body></html>")
    return head + "</head>" + body


# ---------------------------------------------------------------- news
def en_days():
    days = []
    for p in sorted(glob.glob("news-data/*.json"), reverse=True):
        d = json.load(io.open(p, encoding="utf-8"))
        e = d.get("en")
        if not e: continue
        assert len(e["items"]) == len(d["items"]), f"{d['date']}: English items count differs"
        assert 20 <= len(e["summary"]) <= 160 and not re.search(r'["&<>]', e["summary"]), f"{d['date']}: English summary"
        items = [{"title": t["title"], "body": t["body"], "source_name": s["source_name"], "source_url": s["source_url"]} for t, s in zip(e["items"], d["items"])]
        days.append({"date": d["date"], "summary": e["summary"], "items": items})
    return days


def en_news_block():
    days = en_days()
    if not days: return ""
    d = days[0]
    cards = "".join('<a class="card" href="/en/news/%s.html"><span class="code">AI NEWS</span><h2>%s</h2><small>%s</small></a>' % (d["date"], esc(i["title"]), d["date"]) for i in d["items"][:3])
    return ('<section class="wrap" id="tin-ai"><div class="section-heading"><h2>Latest AI news</h2><p>Issue of %s. <a href="/en/news/" style="text-decoration:underline">View all issues</a></p></div>'
            '<div class="cluster compact">%s</div></section>' % (d["date"], cards))


def news_pages():
    days = en_days()
    if not days: return {}
    vi_idx = rd("tin-tuc/index.html")
    pages = {}
    for d in days:
        date = d["date"]; vi_url = f"{SITE}/tin-tuc/{date}.html"; url = f"{SITE}/en/news/{date}.html"
        title = f"AI news for {date}: {d['items'][0]['title']}"
        head = en_head(rd(f"tin-tuc/{date}.html"), url, title, d["summary"], vi_url)
        head = set_ld(head, headline=title, description=d["summary"], mainEntityOfPage=url, inLanguage="en")
        parts = ['<article class="article"><header><a class="back" href="/en/news/">All issues</a><p class="code">AI NEWS / DAILY</p><h1>AI news for ' + date + '</h1>'
                 '<p class="excerpt">' + esc(d["summary"]) + '</p><p class="meta">Edited by Hữu Hùng · <time datetime="' + date + '">' + date + '</time> · ' + str(len(d["items"])) + ' items</p></header><div>']
        for it in d["items"]:
            parts.append('<section class="news-item"><h2>' + esc(it["title"]) + '</h2><p>' + esc(it["body"]) + '</p><p class="news-src">Source: <a rel="noopener" href="' + esc(it["source_url"]) + '">' + esc(it["source_name"]) + "</a></p></section>")
        parts.append('<p class="news-src">This issue is summarised in our own words from the sources cited. Open the original source for the full text before relying on any item.</p></div></article>')
        pages[f"en/news/{date}.html"] = head + "</head><body>" + HEADER + '<main class="reader">' + "".join(parts) + "</main>" + FOOT + "</body></html>"
    lis = "".join('<li><a href="/en/news/%s.html">AI news for %s</a><br><span class="news-src">%s</span></li>' % (d["date"], d["date"], esc(" · ".join(i["title"] for i in d["items"][:3]))) for d in days)
    url = SITE + "/en/news/"
    desc = "A short daily briefing on AI models, tools and the AI market, each item linked to its original source so you can verify it."
    head = en_head(vi_idx, url, "Daily AI news", desc, SITE + "/tin-tuc/")
    head = set_ld(head, headline="Daily AI news", description=desc, mainEntityOfPage=url, inLanguage="en")
    pages["en/news/index.html"] = (head + "</head><body>" + HEADER + '<main class="reader"><article class="article"><header><a class="back" href="/en/">Home</a><p class="code">AI NEWS / DAILY</p><h1>Daily AI news</h1>'
                                   '<p class="excerpt">A short daily briefing on AI models, tools and the AI market, with a source link for every item.</p></header><ul class="news-list">' + lis + "</ul></article></main>" + FOOT + "</body></html>")
    return pages


# ---------------------------------------------------------------- privacy
def privacy_page():
    p = "i18n/en/privacy.md"
    if not os.path.exists(p): return None
    meta, lines = read_md(p)
    vi = rd("quyen-rieng-tu.html")
    url = SITE + "/en/privacy.html"
    head = en_head(vi, url, meta["title"], meta["desc"], SITE + "/quyen-rieng-tu.html")
    head = set_ld(head, headline=meta["title"], description=meta["desc"], mainEntityOfPage=url, inLanguage="en")
    body, _ = render(lines, "privacy")
    body = "<div>" + re.sub(r'^<div itemprop="articleBody"><div class="quick-answer">.*?</div>\n', "", body, flags=re.S)
    return (head + "</head><body>" + HEADER + '<main class="reader"><article class="article"><header><a class="back" href="/en/">Home</a><p class="code">PRIVACY</p><h1>' + esc(meta["title"]) +
            '</h1><p class="excerpt">' + esc(meta["desc"]) + '</p><p class="meta">Updated: ' + meta.get("updated", "2026-11-24") + "</p></header>" + body + "</article></main>" + FOOT + "</body></html>")


# ---------------------------------------------------------------- hreflang on the Vietnamese side + sitemap
def add_hreflang(pairs):
    for vi_path, en_path in pairs:
        s = rd(vi_path)
        vi_url = SITE + ("/" + vi_path if vi_path != "index.html" else "/")
        en_url = SITE + "/" + en_path.replace("index.html", "")
        t = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", s)
        t = sub1(r'(<link rel="canonical" href="[^"]*">)', "", t) if False else t
        m = re.search(r'<link rel="canonical" href="[^"]*">', t)
        assert m, vi_path
        t = t.replace(m.group(0), m.group(0) + hreflang(vi_url, en_url), 1)
        if t != s: wr(vi_path, t)


def update_sitemap(en_paths):
    sm = rd("sitemap.xml")
    sm = re.sub(r"  <url>\s*<loc>" + re.escape(SITE) + r"/en/[^<]*</loc>.*?</url>\n", "", sm, flags=re.S)
    add = ""
    for p in en_paths:
        loc = SITE + "/" + p.replace("index.html", "")
        add += "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n" % (loc, TODAY)
    sm = sm.replace("</urlset>", add + "</urlset>")
    wr("sitemap.xml", sm)


TODAY = os.environ.get("I18N_DATE", "2026-11-24")


def main():
    arts, problems = load_articles()
    if problems:
        print("PROBLEMS:"); [print("  " + p) for p in problems]; sys.exit(1)
    if "--check" in sys.argv:
        print("English sources OK:", len(arts), "articles"); return
    files, pairs = {}, []
    cats = {s: CAT.get(a["cat"].split(" / ")[-1], a["cat"].split(" / ")[-1]) for s, a in arts.items()}
    rel = related.pick(cats)
    for slug, a in arts.items():
        block = related.section([(o + ".html", arts[o]["title"], "%s · %s min read" % (cats[o], arts[o]["min"])) for o in rel[slug]], "en")
        files[f"en/articles/{slug}.html"] = article_page(slug, a, arts, block); pairs.append((f"articles/{slug}.html", f"en/articles/{slug}.html"))
    if arts:
        files["en/index.html"] = home_page(arts); pairs.append(("index.html", "en/index.html"))
    for k, v in news_pages().items():
        files[k] = v
        pairs.append(("tin-tuc/index.html" if k.endswith("index.html") else "tin-tuc/" + os.path.basename(k), k))
    pp = privacy_page()
    if pp: files["en/privacy.html"] = pp; pairs.append(("quyen-rieng-tu.html", "en/privacy.html"))
    # remove stale English pages whose source disappeared
    for f in glob.glob("en/**/*.html", recursive=True):
        if f.replace("\\", "/") not in files: os.remove(f)
    for k, v in files.items(): wr(k, v)
    add_hreflang(pairs)
    update_sitemap(sorted(files))
    print("built:", len(arts), "articles |", len(files), "English pages | hreflang pairs:", len(pairs))


if __name__ == "__main__":
    main()
