"""Source links under each article, from data/sources.json:  {slug: {"checked": "YYYY-MM-DD", "sources": [{"title", "url"}]}}
Run: python tools/add_sources.py   (writes the Vietnamese pages, idempotent; run tools/i18n_build.py afterwards for English)."""
import html, io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = re.compile(r'<section class="sources">.*?</section>', re.S)
TEXT = {"vi": ("Nguồn tham khảo", "Mở lại và đối chiếu ngày {d}. Trang nguồn có thể thay đổi sau ngày này, hãy kiểm tra lại trước khi làm theo."),
        "en": ("Sources", "Reopened and cross-checked on {d}. Source pages can change after that date, so check them again before following along.")}


def load():
    p = os.path.join(ROOT, "data", "sources.json")
    return json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {}


def section(entry, lang):
    head, note = TEXT[lang]
    d = entry["checked"]
    shown = f"{d[8:10]}/{d[5:7]}/{d[:4]}" if lang == "vi" else d
    items = []
    for s in entry["sources"]:
        assert s["url"].startswith("https://") and s["title"], s
        items.append('<li><a href="%s" rel="noopener">%s</a><span>%s</span></li>'
                     % (html.escape(s["url"], quote=True), html.escape(s["title"], quote=False),
                        html.escape(re.sub(r"^https://(www\.)?", "", s["url"]), quote=False)))
    return '<section class="sources"><h2>%s</h2><p>%s</p><ul>%s</ul></section>' % (head, note.format(d=shown), "".join(items))


def main():
    n = 0
    for slug, entry in load().items():
        p = os.path.join(ROOT, "articles", slug + ".html")
        s = io.open(p, encoding="utf-8", newline="").read()
        t = BLOCK.sub("", s)
        assert t.count("</div></article>") == 1, slug
        t = t.replace("</div></article>", "</div>" + section(entry, "vi") + "</article>")
        t = re.sub(r'("dateModified":\s*")\d{4}-\d{2}-\d{2}(")', lambda m: m.group(1) + entry["checked"] + m.group(2), t, count=1)
        if t != s:
            io.open(p, "w", encoding="utf-8", newline="").write(t); n += 1
    print("source blocks:", len(load()), "| pages changed:", n)


if __name__ == "__main__":
    main()
