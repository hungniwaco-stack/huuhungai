"""Publish one approved daily news issue end to end.
Usage: python tools/news_publish.py YYYY-MM-DD [--dry-run]
  1. moves news-drafts/<date>.json to news-data/ (if it is still a draft) and validates it
  2. runs tools/news_build.py
  3. git add (specific paths only), commit, push
  4. waits for the Vercel deploy (gh status), checks the live pages return 200
  5. pings IndexNow for the home page, /tin-tuc/ and the new day page
--dry-run stops after step 2 (no git, no network)."""
import os, re, shutil, subprocess, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
REPO = "hungniwaco-stack/huuhungai"
SITE = "https://huuhungai.com"


def run(*cmd, check=True):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode:
        sys.exit(f"FAILED: {' '.join(cmd)}\n{r.stdout}{r.stderr}")
    return r.stdout.strip()


def http(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "news-publish"}), timeout=20).status
    except Exception as e:
        return getattr(e, "code", 0)


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    dry = "--dry-run" in sys.argv
    assert len(a) == 1 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", a[0]), "usage: news_publish.py YYYY-MM-DD [--dry-run]"
    date = a[0]
    draft, final = f"news-drafts/{date}.json", f"news-data/{date}.json"
    if os.path.exists(draft):
        run(sys.executable, "tools/news_build.py", "--check", draft)
        os.makedirs("news-data", exist_ok=True)
        shutil.move(draft, final)
    assert os.path.exists(final), f"no draft or data for {date}"
    print(run(sys.executable, "tools/news_build.py"))
    if dry:
        print("dry-run: stopped before git"); return

    run("git", "add", "news-data", "tin-tuc", "index.html", "sitemap.xml")
    if run("git", "diff", "--cached", "--name-only"):
        run("git", "-c", "core.safecrlf=false", "commit", "-q", "-m",
            f"Publish daily AI news {date}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>")
        run("git", "push", "-q", "origin", "main")
        for _ in range(24):  # up to about 2 minutes
            time.sleep(5)
            st = run("gh", "api", f"repos/{REPO}/commits/main/status", "--jq", ".state")
            if st != "pending":
                break
        assert st == "success", f"deploy state: {st}"
    else:
        print("nothing new to commit, checking live pages anyway")

    urls = [f"{SITE}/", f"{SITE}/tin-tuc/", f"{SITE}/tin-tuc/{date}.html"]
    for u in urls:
        code = http(u)
        assert code == 200, f"{u} -> {code}"
    print("live OK:", ", ".join(u.replace(SITE, "") for u in urls))
    print(run(sys.executable, "tools/indexnow.py", *urls))


if __name__ == "__main__":
    main()
