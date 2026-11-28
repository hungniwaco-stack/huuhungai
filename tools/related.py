"""Three related links under each article, written into the static HTML.
Run: python tools/related.py   (writes the Vietnamese pages, idempotent; i18n_build uses pick() and section() for English)."""
import collections, glob, html, io, math, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = re.compile(r'<nav class="related".*?</nav>', re.S)
HEAD = {"vi": "Bài liên quan", "en": "Related articles"}


# Vietnamese filler words that appear in slugs and say nothing about the topic
STOP = set("ai va voi cho cua la nen khi nao de dung cach bai hoc ve trong bang mot nhung the gi o tu co duoc can "
           "lam sao truoc sau vi tren qua theo moi phan dau nhu hay chon doc viec thuc te nhin vao tung buoc nhanh bat tao xay".split())
# product names: sharing one is the strongest signal
NAMES = set("openclaw hermes claude chatgpt deepseek ollama kimi manus gemma google remotion telegram obsidian seo".split())


def pick(cats, n=3):
    """cats: {slug: category}. Shared topic words in the slug count (rarer counts more, product names triple);
    same category is a smaller bonus. Deterministic. ponytail: slug words only; add tags if picks feel off."""
    words = {s: set(s.split("-")) - STOP for s in cats}
    df = collections.Counter(w for ws in words.values() for w in ws)
    weight = {w: math.log(len(cats) / c) * (3 if w in NAMES else 1) for w, c in df.items()}
    return {s: sorted((o for o in cats if o != s),
                      key=lambda o: (-(sum(weight[w] for w in sorted(words[s] & words[o])) + (2 if cats[o] == cats[s] else 0)), o))[:n]
            for s in cats}


def section(items, lang):
    """items: [(href, title, note)] with title and note as plain text."""
    lis = "".join('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>' % (h, html.escape(t, quote=False), html.escape(x, quote=False)) for h, t, x in items)
    return '<nav class="related" aria-label="%s"><h2>%s</h2><ul>%s</ul></nav>' % (HEAD[lang], HEAD[lang], lis)


def main():
    pages, meta = {}, {}
    for p in sorted(glob.glob(os.path.join(ROOT, "articles", "*.html"))):
        slug = os.path.basename(p)[:-5]
        s = io.open(p, encoding="utf-8", newline="").read()
        if '<div itemprop="articleBody">' not in s:
            continue
        cat = html.unescape(re.search(r'<p class="code">(.*?)</p>', s).group(1)).split(" / ")[-1]
        title = html.unescape(re.search(r'<h1 itemprop="headline">(.*?)</h1>', s, re.S).group(1))
        pages[slug] = (p, s)
        meta[slug] = (title, "%s · %s phút đọc" % (cat, re.search(r"(\d+) phút đọc", s).group(1)), cat)
    rel = pick({k: v[2] for k, v in meta.items()})
    n = 0
    for slug, (p, s) in pages.items():
        t = BLOCK.sub("", s)
        assert t.count("</article></main>") == 1, slug
        t = t.replace("</article></main>", "</article>" + section([(o + ".html", meta[o][0], meta[o][1]) for o in rel[slug]], "vi") + "</main>")
        if t != s:
            io.open(p, "w", encoding="utf-8", newline="").write(t); n += 1
    print("articles:", len(pages), "| pages changed:", n)


if __name__ == "__main__":
    main()
