"""Mini-markdown renderer shared by the article pipeline.
Syntax: QUICK: line, '## ' h2, paragraphs, '- ' / '1. ' lists, ``` fenced code, `code`, **bold**, [text](url), '> VERIFY:' notes (collected, not rendered)."""
import html, os, re

def inline(t, problems=None, slug="", link_root=None):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1) + "</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = "".join(seg if seg.startswith("<code>") else re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<em>\1</em>", seg)
                for seg in re.split(r"(<code>.*?</code>)", t))

    def link(m):
        href = m.group(2)
        if link_root and not href.startswith(("http://", "https://", "/", "#")):
            if not os.path.exists(os.path.join(link_root, href)) and problems is not None:
                problems.append(f"{slug}: broken internal link {href}")
        return f'<a href="{href}">{m.group(1)}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, t)

def render(lines, slug, problems=None, link_root=None, quick_label="Trả lời nhanh:"):
    out, notes, i, list_kind, quick = [], [], 0, None, None

    def close_list():
        nonlocal list_kind
        if list_kind:
            out.append(f"</{list_kind}>"); list_kind = None

    while i < len(lines):
        l = lines[i]
        if l.startswith("```"):
            close_list(); i += 1; buf = []
            while not lines[i].startswith("```"): buf.append(lines[i]); i += 1
            out.append("<pre><code>" + html.escape("\n".join(buf), quote=False) + "</code></pre>")
        elif l.startswith("QUICK: "):
            quick = inline(l[7:], problems, slug, link_root)
        elif l.startswith("## "):
            close_list(); out.append('<h2 id="x">' + inline(l[3:], problems, slug, link_root) + "</h2>")
        elif l.startswith("> VERIFY: "):
            notes.append(l[10:])
        elif re.match(r"- ", l):
            if list_kind != "ul": close_list(); out.append("<ul>"); list_kind = "ul"
            out.append("<li>" + inline(l[2:], problems, slug, link_root) + "</li>")
        elif re.match(r"\d+\. ", l):
            if list_kind != "ol": close_list(); out.append("<ol>"); list_kind = "ol"
            out.append("<li>" + inline(re.sub(r"^\d+\. ", "", l), problems, slug, link_root) + "</li>")
        elif l.strip() == "":
            close_list()
        else:
            close_list(); out.append("<p>" + inline(l, problems, slug, link_root) + "</p>")
        i += 1
    close_list()
    n = 0
    def fix(m):
        nonlocal n; n += 1
        return f'<h2 id="{slug}-{n}">'
    body = re.sub(r'<h2 id="[^"]*">', fix, "\n".join(out))
    assert quick, f"{slug}: missing QUICK"
    body = f'<div itemprop="articleBody"><div class="quick-answer"><strong>{quick_label}</strong> {quick}</div>\n' + body + "</div>"
    return body, notes
