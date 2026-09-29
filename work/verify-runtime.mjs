import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const articlesSource = readFileSync(join(root, "articles.js"), "utf8");
const appSource = readFileSync(join(root, "app.js"), "utf8");

const windowStub = {};
new Function("window", articlesSource)(windowStub);

const articles = windowStub.HHA_ARTICLES;
const seoArticles = articles.filter((article) => article.category === "AI SEO");
const claudeArticles = articles.filter((article) => {
  const haystack = [article.title, article.excerpt, article.category, article.tags.join(" ")].join(" ").toLowerCase();
  return haystack.includes("claude");
});
const firstSeoRelated = articles.filter((article) => article.slug !== seoArticles[0].slug && article.category === seoArticles[0].category).slice(0, 3);

function assert(condition, message) {
  if (!condition) {
    console.error(`FAIL: ${message}`);
    process.exitCode = 1;
  }
}

assert(articles.length === 82, "runtime has 82 articles");
assert(seoArticles.length >= 8, "AI SEO filter has enough articles");
assert(claudeArticles.length >= 5, "Claude search finds articles");
assert(firstSeoRelated.length === 3, "related articles can render for SEO article");
assert(appSource.includes("location.hash"), "app uses hash routing");
assert(appSource.includes("article.body.split"), "app renders article body blocks");

if (!process.exitCode) {
  console.log(JSON.stringify({
    articles: articles.length,
    seoArticles: seoArticles.length,
    claudeArticles: claudeArticles.length,
    firstSeoSlug: seoArticles[0].slug,
    relatedForFirstSeo: firstSeoRelated.length
  }, null, 2));
}
