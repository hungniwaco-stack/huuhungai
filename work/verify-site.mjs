import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = dirname(dirname(fileURLToPath(import.meta.url)));

function read(path) {
  return readFileSync(join(root, path), "utf8");
}

function assert(condition, message) {
  if (!condition) {
    console.error(`FAIL: ${message}`);
    process.exitCode = 1;
  }
}

const html = read("index.html");

assert(html.includes('id="app"'), "index.html must include #app root");
assert(html.includes('id="article-list"'), "index.html must include #article-list");
assert(html.includes('id="article-detail"'), "index.html must include #article-detail");
assert(html.includes('id="search-input"'), "index.html must include #search-input");
assert(html.includes('id="category-filters"'), "index.html must include #category-filters");
assert(html.includes("Hữu Hùng AI Automation"), "brand name must render with Vietnamese accents");
assert(html.includes("styles.css"), "index.html must load styles.css");
assert(html.includes("articles.js"), "index.html must load articles.js");
assert(html.includes("app.js"), "index.html must load app.js");

if (!process.exitCode) {
  console.log("PASS: static shell anchors are present");
}

const articlesSource = read("articles.js");

assert(articlesSource.includes("window.HHA_ARTICLES"), "articles.js must expose window.HHA_ARTICLES");
assert(!articlesSource.includes("Julian Goldie ·"), "articles.js must not copy source byline strings");
assert(!articlesSource.includes("$300K/month"), "articles.js must not reuse unverifiable revenue claims");
assert(!articlesSource.includes("2,200+ members"), "articles.js must not reuse private/community claim copy");
assert(!articlesSource.includes("700+ daily clicks"), "articles.js must not reuse traffic claim copy");
assert(!articlesSource.includes("106K GitHub stars"), "articles.js must not reuse GitHub-star claim copy");
assert(!articlesSource.includes("92.2% retrieval accuracy"), "articles.js must not reuse accuracy claim copy");

const fn = new Function("window", `${articlesSource}; return window.HHA_ARTICLES;`);
const articles = fn({});

assert(Array.isArray(articles), "window.HHA_ARTICLES must be an array");
assert(articles.length === 82, "article count must match the 82 visible public source cards");

const requiredFields = ["slug", "title", "sourceTitle", "category", "date", "readTime", "excerpt", "tags", "body"];
const slugs = new Set();
for (const article of articles) {
  for (const field of requiredFields) {
    assert(Boolean(article[field]), `article ${article.slug || article.sourceTitle} missing ${field}`);
  }
  assert(!slugs.has(article.slug), `duplicate slug ${article.slug}`);
  slugs.add(article.slug);
  assert(article.title !== article.sourceTitle, `title must be rewritten for ${article.sourceTitle}`);
  assert(article.excerpt.length >= 80, `excerpt too short for ${article.slug}`);
  assert(article.body.length >= 3500, `body too short for ${article.slug}`);
}

if (!process.exitCode) {
  console.log("PASS: article data is complete");
}

const appSource = read("app.js");
for (const name of ["renderFilters", "renderList", "renderDetail", "getFilteredArticles", "setRoute"]) {
  assert(appSource.includes(`function ${name}`), `app.js must define ${name}`);
}
assert(appSource.includes("hashchange"), "app.js must listen for hashchange routing");

const css = read("styles.css");
for (const selector of [".site-header", ".hero", ".article-grid", ".article-card", ".article-detail", "@media"]) {
  assert(css.includes(selector), `styles.css must include ${selector}`);
}
assert(!css.includes("linear-gradient(135deg, #6"), "avoid dominant purple-blue gradient palette");

if (!process.exitCode) {
  console.log("PASS: app and styles are present");
}
