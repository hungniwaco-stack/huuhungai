# Huu Hung AI Automation Blog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static Vietnamese data-driven blog for **Hữu Hùng AI Automation** using the public article topics visible on AI Profit Boardroom's blog page.

**Architecture:** The site is a no-backend static app. `articles.js` owns structured article data, `app.js` owns routing/search/filter/rendering, `styles.css` owns the clean professional visual system, and `index.html` provides semantic containers. Verification uses lightweight Node/browser checks without external dependencies.

**Tech Stack:** HTML, CSS, vanilla JavaScript, browser `hashchange`, Node.js built-ins for local verification.

---

## File Structure

- Create `index.html`: semantic shell, metadata, header, hero, controls, list/detail containers, footer.
- Create `styles.css`: responsive light visual design, cards, filters, article typography, mobile behavior.
- Create `articles.js`: normalized public source snapshot and rewritten Vietnamese article records.
- Create `app.js`: article rendering, search, category filter, hash routing, related article selection.
- Create `work/verify-site.mjs`: static verification script for article data and required DOM anchors.
- Create `work/source-snapshot.md`: human-readable source snapshot notes and article count.
- Modify `docs/superpowers/specs/2026-07-05-huu-hung-ai-automation-blog-design.md`: only if implementation discovers a necessary clarification.

## Public Source Snapshot

The source page `https://aiprofitboardroom.com/blog/` was re-opened on 2026-07-05. The listing shows public article cards from April 16, 2026 through May 8, 2026, with link references 3 through 84, which equals 82 visible public articles. Use the public title, category, date, read time, and visible summary as source intent only.

Do not copy source article bodies. Do not reproduce private or unverifiable claims as facts for Hữu Hùng AI Automation.

---

### Task 1: Create Static Shell And Verification Baseline

**Files:**
- Create: `index.html`
- Create: `work/verify-site.mjs`

- [ ] **Step 1: Create the failing verification script**

Create `work/verify-site.mjs` with this content:

```js
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
```

- [ ] **Step 2: Run the verification to confirm it fails**

Run: `node work/verify-site.mjs`

Expected: `ENOENT` for `index.html` because the shell has not been created yet.

- [ ] **Step 3: Create `index.html`**

Create `index.html` with this content:

```html
<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hữu Hùng AI Automation | Blog AI Automation cho người Việt</title>
    <meta name="description" content="Hướng dẫn AI Automation thực chiến cho người Việt: AI Agent, SEO AI, workflow, công cụ AI và tự động hóa doanh nghiệp.">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="#/">Hữu Hùng AI Automation</a>
      <nav class="nav" aria-label="Điều hướng chính">
        <a href="#/">Blog</a>
        <a href="#topics">Chủ đề</a>
        <a href="#resources">Tài nguyên</a>
        <a href="#about">Giới thiệu</a>
      </nav>
    </header>

    <main id="app">
      <section class="hero" aria-labelledby="hero-title">
        <p class="eyebrow">Blog AI Automation</p>
        <h1 id="hero-title">Hướng dẫn AI Automation thực chiến cho người Việt</h1>
        <p class="hero-copy">Các bài viết về AI Agent, SEO AI, workflow, công cụ AI và tự động hóa vận hành được viết lại theo ngôn ngữ rõ ràng, thực tế, dễ áp dụng.</p>
        <div class="stats" aria-label="Thống kê nội dung công khai">
          <span><strong id="stat-count">0</strong> bài viết</span>
          <span><strong id="stat-categories">0</strong> nhóm chủ đề</span>
          <span>AI Agent, SEO AI, Workflow</span>
        </div>
      </section>

      <section class="toolbar" aria-label="Tìm kiếm và lọc bài viết">
        <label class="search-label" for="search-input">Tìm bài viết</label>
        <input id="search-input" type="search" placeholder="Tìm theo chủ đề, công cụ, workflow..." autocomplete="off">
        <div id="category-filters" class="filters" aria-label="Lọc theo chuyên mục"></div>
      </section>

      <section id="article-list" class="article-grid" aria-live="polite"></section>
      <article id="article-detail" class="article-detail" hidden></article>
    </main>

    <footer class="site-footer">
      <div>
        <strong>Hữu Hùng AI Automation</strong>
        <p>Tiếp tục học AI Automation cùng Hữu Hùng qua các bài viết thực chiến, dễ hiểu và phù hợp thị trường Việt Nam.</p>
      </div>
      <a class="footer-link" href="#/">Xem bài mới nhất</a>
    </footer>

    <script src="articles.js"></script>
    <script src="app.js"></script>
  </body>
</html>
```

- [ ] **Step 4: Run verification**

Run: `node work/verify-site.mjs`

Expected: `PASS: static shell anchors are present`

---

### Task 2: Create Article Data Model And Content Verification

**Files:**
- Create: `articles.js`
- Modify: `work/verify-site.mjs`
- Create: `work/source-snapshot.md`

- [ ] **Step 1: Extend verification before creating data**

Modify `work/verify-site.mjs` by appending this code after the HTML assertions:

```js
const articlesSource = read("articles.js");

assert(articlesSource.includes("window.HHA_ARTICLES"), "articles.js must expose window.HHA_ARTICLES");
assert(!articlesSource.includes("Julian Goldie ·"), "articles.js must not copy source byline strings");
assert(!articlesSource.includes("$300K/month"), "articles.js must not reuse unverifiable revenue claims");
assert(!articlesSource.includes("2,200+ members"), "articles.js must not reuse private/community claim copy");

const sandbox = { window: {} };
const fn = new Function("window", `${articlesSource}; return window.HHA_ARTICLES;`);
const articles = fn(sandbox.window);

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
```

- [ ] **Step 2: Run verification to confirm it fails**

Run: `node work/verify-site.mjs`

Expected: `ENOENT` for `articles.js`.

- [ ] **Step 3: Create `work/source-snapshot.md`**

Create `work/source-snapshot.md` with:

```markdown
# Source Snapshot

Source: https://aiprofitboardroom.com/blog/
Snapshot date: 2026-07-05

Use only public listing data:

- Category
- Title
- Visible summary
- Author/date/read-time line

The listing has 82 public article cards, represented by web references 3 through 84 on the opened page.

Rules:

- Use source titles only as topic intent.
- Rewrite all public titles into Vietnamese.
- Write original Vietnamese excerpts and article bodies.
- Avoid unsupported source claims such as private revenue, private member counts, or unverified performance numbers.
```

- [ ] **Step 4: Create `articles.js` with the data shape**

Create `articles.js` with an immediately invoked function and 82 article records:

```js
(function () {
  const categories = {
    community: "Cộng đồng AI",
    productivity: "Năng suất",
    design: "Công cụ AI",
    models: "Mô hình AI",
    agents: "AI Agent",
    tools: "Công cụ AI",
    education: "Cộng đồng AI",
    seo: "AI SEO",
    business: "Tự động hóa doanh nghiệp",
    automation: "Tự động hóa doanh nghiệp",
    news: "Mô hình AI"
  };

  function article(sourceTitle, title, category, date, readTime, excerpt, tags, sections) {
    return {
      slug: title
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase()
        .replace(/đ/g, "d")
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-|-$/g, ""),
      sourceTitle,
      title,
      category,
      date,
      readTime,
      excerpt,
      tags,
      body: sections.join("\n\n")
    };
  }

  const standardSections = (topic, angle, useCase) => [
    `## Vì sao chủ đề này đáng quan tâm\n\n${topic} đang trở thành một phần quan trọng trong cách doanh nghiệp nhỏ, đội marketing và người làm vận hành tiếp cận AI Automation. Điểm cần hiểu không phải là chạy theo tên công cụ mới, mà là biết công cụ đó giải quyết khâu nào trong quy trình làm việc: nghiên cứu, viết nội dung, chăm sóc khách hàng, tạo lead, phân tích dữ liệu hay phối hợp đội nhóm.`,
    `## Cách nhìn đúng cho người Việt\n\nVới thị trường Việt Nam, ${angle} cần được đặt trong bối cảnh nguồn lực hạn chế, đội ngũ nhỏ và yêu cầu triển khai nhanh. Một workflow tốt phải dễ giải thích cho người không chuyên, có bước kiểm tra đầu ra, có người chịu trách nhiệm phê duyệt, và không phụ thuộc hoàn toàn vào một mô hình AI duy nhất.`,
    `## Quy trình triển khai gợi ý\n\nBắt đầu bằng việc xác định đầu vào, đầu ra và tiêu chuẩn chất lượng. Sau đó chia quy trình thành các bước nhỏ: thu thập dữ liệu, xử lý bằng AI, kiểm tra kết quả, lưu lại tri thức, và đo hiệu quả theo tuần. Nếu dùng AI agent, hãy giới hạn quyền truy cập lúc đầu, ghi log thao tác và luôn có điểm dừng để con người kiểm soát.`,
    `## Ứng dụng thực tế\n\n${useCase} Ví dụ, một đội nội dung có thể dùng AI để gom ý tưởng, phân loại từ khóa, tạo dàn ý, viết bản nháp và chuẩn hóa bài trước khi đăng. Một đội bán hàng có thể dùng automation để lọc danh sách khách hàng tiềm năng, cá nhân hóa email và nhắc lịch follow-up. Giá trị thật nằm ở việc giảm thao tác lặp lại, không phải thay thế toàn bộ con người.`,
    `## Lưu ý khi áp dụng\n\nKhông nên triển khai automation chỉ vì công cụ đang được nhắc nhiều. Hãy kiểm tra chi phí API, quyền riêng tư dữ liệu, khả năng bảo trì và mức độ phù hợp với quy trình hiện tại. Với các tác vụ ảnh hưởng đến khách hàng, tài chính hoặc pháp lý, AI nên đóng vai trò hỗ trợ và con người vẫn là người phê duyệt cuối cùng.`,
    `## Kết luận\n\n${topic} hữu ích nhất khi được biến thành một quy trình rõ ràng, có kiểm tra và có mục tiêu kinh doanh cụ thể. Nếu bạn mới bắt đầu, hãy chọn một tác vụ nhỏ, đo thời gian tiết kiệm được, rồi mới mở rộng sang hệ thống lớn hơn.`
  ];

  window.HHA_CATEGORIES = Object.values(categories).filter((value, index, list) => list.indexOf(value) === index);
  window.HHA_ARTICLES = [
    article("AI Money Lab Vs AI Profit Boardroom (Free Vs Paid 2026)", "So sánh cộng đồng AI miễn phí và trả phí: nên bắt đầu từ đâu?", categories.community, "2026-05-08", "7 phút đọc", "Phân tích cách chọn cộng đồng AI phù hợp với mục tiêu học automation, xây hệ thống và phát triển năng lực cá nhân.", ["cộng đồng AI", "học AI", "automation"], standardSections("Cộng đồng AI", "việc chọn môi trường học và thực hành", "Người mới có thể bắt đầu từ cộng đồng miễn phí để hiểu thuật ngữ, sau đó chọn nhóm chuyên sâu khi cần lộ trình và phản hồi.")),
    article("OMI Obsidian For Entrepreneurs (Productivity Stack 2026)", "OMI và Obsidian cho doanh nhân: xây hệ thống ghi nhớ công việc bằng AI", categories.productivity, "2026-05-08", "6 phút đọc", "Cách kết hợp ghi chú, ghi âm và AI để lưu lại cuộc họp, ý tưởng và quyết định quan trọng.", ["Obsidian", "năng suất", "ghi chú AI"], standardSections("Bộ công cụ OMI và Obsidian", "việc xây second brain cho doanh nhân", "Nhà sáng lập có thể lưu biên bản họp, tóm tắt quyết định và chuyển chúng thành danh sách việc cần làm.")),
    article("Open Design Vs Claude Design For Agencies (Which Wins 2026)", "Open Design và Claude Design cho agency: chọn công cụ thiết kế AI thế nào?", categories.design, "2026-05-08", "6 phút đọc", "Góc nhìn thực tế cho agency khi dùng AI để tạo concept, bản nháp giao diện và tài liệu trình bày cho khách hàng.", ["thiết kế AI", "agency", "workflow"], standardSections("Công cụ thiết kế AI cho agency", "việc chuẩn hóa quy trình sáng tạo", "Agency có thể dùng AI để tạo nhiều phương án ban đầu, sau đó designer tinh chỉnh theo brand guideline.")),
    article("OpenClaw Roadmap Course (Stay 6 Months Ahead)", "Lộ trình học OpenClaw: cách theo kịp công cụ AI Agent mới", categories.community, "2026-05-08", "7 phút đọc", "Một cách tiếp cận có hệ thống để học AI Agent mà không bị loạn giữa quá nhiều bản cập nhật.", ["OpenClaw", "AI Agent", "học AI"], standardSections("Lộ trình học OpenClaw", "việc học công cụ agent theo thứ tự", "Người học nên đi từ khái niệm agent, quyền truy cập, bộ nhớ, tác vụ mẫu rồi mới đến workflow phức tạp.")),
    article("Sonnet 4.8 For Business (Real Use Cases & ROI 2026)", "Sonnet cho doanh nghiệp: dùng mô hình AI vào quy trình nào trước?", categories.models, "2026-05-08", "6 phút đọc", "Cách đánh giá một mô hình AI mới theo tác vụ kinh doanh thay vì chỉ nhìn benchmark.", ["mô hình AI", "doanh nghiệp", "ROI"], standardSections("Mô hình AI Sonnet cho doanh nghiệp", "việc gắn mô hình AI với hiệu quả vận hành", "Doanh nghiệp nên thử ở viết nội dung, phân tích tài liệu, chăm sóc khách hàng nội bộ và hỗ trợ báo cáo.")),
    article("I Switched From OpenClaw To Accomplish — Here's Why", "Khi nào nên đổi nền tảng AI Agent trong workflow của bạn?", categories.agents, "2026-05-06", "6 phút đọc", "Những tiêu chí thực tế để quyết định giữ hay thay một nền tảng agent: độ ổn định, tốc độ, chi phí và khả năng kiểm soát.", ["AI Agent", "workflow", "nền tảng"], standardSections("Việc chuyển đổi nền tảng AI Agent", "việc đánh giá công cụ theo vận hành thực tế", "Một nhóm nhỏ nên thử song song hai công cụ trên cùng tác vụ trước khi chuyển toàn bộ workflow.")),
    article("Why Agent Zero Beats OpenClaw In Real Tests", "Đánh giá AI Agent qua bài test thực tế: nhìn vào tiêu chí nào?", categories.agents, "2026-05-06", "6 phút đọc", "Cách so sánh AI Agent bằng tác vụ thật thay vì chỉ đọc lời giới thiệu sản phẩm.", ["Agent Zero", "OpenClaw", "đánh giá agent"], standardSections("So sánh AI Agent bằng bài test thực tế", "việc đo độ tự chủ và độ tin cậy", "Có thể giao cùng một nhiệm vụ nghiên cứu, tạo báo cáo và thao tác trình duyệt cho hai agent rồi so kết quả.")),
    article("What's In The AI Profit Boardroom Vault (1,000+ Tools)", "Một kho công cụ AI nên được tổ chức như thế nào để dễ dùng?", categories.community, "2026-05-06", "5 phút đọc", "Cách nhìn về thư viện automation, agent và template để người dùng tìm đúng công cụ thay vì bị ngợp.", ["kho công cụ", "automation", "template"], standardSections("Kho công cụ AI", "việc tổ chức tài nguyên theo mục tiêu sử dụng", "Một thư viện tốt nên chia theo marketing, sales, vận hành, nội dung, nghiên cứu và chăm sóc khách hàng.")),
    article("Claude Operon Vs Chat, Code, Co-work: What's Different", "Các chế độ làm việc của Claude: chat, code và cộng tác khác nhau ra sao?", categories.tools, "2026-05-06", "6 phút đọc", "Giải thích cách chọn chế độ làm việc AI phù hợp khi trò chuyện, viết code hoặc phối hợp trên tác vụ phức tạp.", ["Claude", "AI tools", "workflow"], standardSections("Các chế độ làm việc trong Claude", "việc chọn đúng giao diện cho đúng nhiệm vụ", "Người làm nội dung dùng chat, developer dùng code, còn quản lý dự án cần chế độ cộng tác và theo dõi ngữ cảnh.")),
    article("Build Anything With Hermes (106K GitHub Stars)", "Hermes AI Agent: dùng framework agent để tự động hóa công việc", categories.agents, "2026-05-06", "6 phút đọc", "Tổng quan cách một framework AI Agent hỗ trợ xây workflow, chạy tác vụ và kết nối công cụ.", ["Hermes", "AI Agent", "framework"], standardSections("Hermes AI Agent", "việc dùng framework để chuẩn hóa agent", "Developer có thể dùng framework để tạo agent nghiên cứu, agent viết nội dung và agent kiểm tra kết quả.")),
    article("Hermes Kanban Setup: Build Websites With AI", "Thiết lập Kanban cho Hermes: quản lý quy trình xây website bằng AI", categories.agents, "2026-05-06", "6 phút đọc", "Cách kết hợp AI Agent với bảng Kanban để chia nhỏ nhiệm vụ và kiểm soát tiến độ.", ["Hermes", "Kanban", "xây website"], standardSections("Hermes Kanban", "việc quản lý tác vụ AI bằng bảng việc", "Một dự án website có thể chia thành nghiên cứu, nội dung, giao diện, kiểm thử và bàn giao.")),
    article("Build A Hermes Second Brain In 30 Minutes (Free)", "Xây second brain với Hermes, ghi chú và AI Automation", categories.agents, "2026-05-06", "7 phút đọc", "Cách tổ chức tri thức cá nhân để AI Agent có thể hỗ trợ nhớ, tìm và tái sử dụng thông tin.", ["second brain", "Hermes", "Obsidian"], standardSections("Second brain với Hermes", "việc lưu tri thức để agent dùng lại", "Người làm tư vấn có thể lưu case study, câu hỏi khách hàng và mẫu đề xuất để tái sử dụng.")),
  ];
})();
```

Then append the remaining 70 source-card topics from the opened page using the same `article(...)` pattern. Keep the count exactly 82. Use rewritten Vietnamese titles and original Vietnamese sections for each record.

- [ ] **Step 5: Run verification**

Run: `node work/verify-site.mjs`

Expected: `PASS: static shell anchors are present` and no `FAIL:` lines.

---

### Task 3: Implement Rendering And Routing

**Files:**
- Create: `app.js`
- Modify: `work/verify-site.mjs`

- [ ] **Step 1: Extend verification for app functions**

Append to `work/verify-site.mjs`:

```js
const appSource = read("app.js");
for (const name of ["renderFilters", "renderList", "renderDetail", "getFilteredArticles", "setRoute"]) {
  assert(appSource.includes(`function ${name}`), `app.js must define ${name}`);
}
assert(appSource.includes("hashchange"), "app.js must listen for hashchange routing");
```

- [ ] **Step 2: Run verification to confirm it fails**

Run: `node work/verify-site.mjs`

Expected: `ENOENT` for `app.js`.

- [ ] **Step 3: Create `app.js`**

Create `app.js`:

```js
(function () {
  const articles = window.HHA_ARTICLES || [];
  const listEl = document.getElementById("article-list");
  const detailEl = document.getElementById("article-detail");
  const searchInput = document.getElementById("search-input");
  const filtersEl = document.getElementById("category-filters");
  const statCount = document.getElementById("stat-count");
  const statCategories = document.getElementById("stat-categories");

  let activeCategory = "Tất cả";

  function uniqueCategories() {
    return ["Tất cả", ...Array.from(new Set(articles.map((article) => article.category)))];
  }

  function escapeHtml(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function renderFilters() {
    filtersEl.innerHTML = uniqueCategories()
      .map((category) => `<button class="filter-chip${category === activeCategory ? " active" : ""}" type="button" data-category="${escapeHtml(category)}">${escapeHtml(category)}</button>`)
      .join("");
  }

  function getFilteredArticles() {
    const query = searchInput.value.trim().toLowerCase();
    return articles.filter((article) => {
      const matchesCategory = activeCategory === "Tất cả" || article.category === activeCategory;
      const haystack = [article.title, article.excerpt, article.category, article.tags.join(" ")].join(" ").toLowerCase();
      return matchesCategory && (!query || haystack.includes(query));
    });
  }

  function articleCard(article) {
    return `
      <a class="article-card" href="#/article/${article.slug}">
        <span class="category">${escapeHtml(article.category)}</span>
        <h2>${escapeHtml(article.title)}</h2>
        <p>${escapeHtml(article.excerpt)}</p>
        <div class="meta">
          <span>${escapeHtml(article.date)}</span>
          <span>${escapeHtml(article.readTime)}</span>
        </div>
      </a>
    `;
  }

  function renderList() {
    const filtered = getFilteredArticles();
    detailEl.hidden = true;
    listEl.hidden = false;
    listEl.innerHTML = filtered.length
      ? filtered.map(articleCard).join("")
      : `<p class="empty-state">Không tìm thấy bài viết phù hợp. Hãy thử từ khóa khác.</p>`;
    document.title = "Hữu Hùng AI Automation | Blog AI Automation cho người Việt";
  }

  function relatedArticles(current) {
    return articles
      .filter((article) => article.slug !== current.slug && article.category === current.category)
      .slice(0, 3);
  }

  function renderDetail(slug) {
    const article = articles.find((item) => item.slug === slug);
    if (!article) {
      setRoute("/");
      return;
    }
    listEl.hidden = true;
    detailEl.hidden = false;
    const related = relatedArticles(article);
    detailEl.innerHTML = `
      <a class="back-link" href="#/">← Quay lại blog</a>
      <header class="article-header">
        <span class="category">${escapeHtml(article.category)}</span>
        <h1>${escapeHtml(article.title)}</h1>
        <p>${escapeHtml(article.excerpt)}</p>
        <div class="meta">
          <span>${escapeHtml(article.date)}</span>
          <span>${escapeHtml(article.readTime)}</span>
        </div>
      </header>
      <div class="article-body">${article.body.split("\\n\\n").map(renderParagraphBlock).join("")}</div>
      <section class="related">
        <h2>Bài liên quan</h2>
        <div class="related-grid">${related.map(articleCard).join("")}</div>
      </section>
    `;
    document.title = `${article.title} | Hữu Hùng AI Automation`;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function renderParagraphBlock(block) {
    if (block.startsWith("## ")) {
      return `<h2>${escapeHtml(block.slice(3))}</h2>`;
    }
    return `<p>${escapeHtml(block)}</p>`;
  }

  function setRoute(path) {
    window.location.hash = path === "/" ? "#/" : `#${path}`;
  }

  function handleRoute() {
    const hash = window.location.hash || "#/";
    const articleMatch = hash.match(/^#\\/article\\/(.+)$/);
    if (articleMatch) {
      renderDetail(articleMatch[1]);
    } else {
      renderList();
    }
  }

  function bindEvents() {
    searchInput.addEventListener("input", renderList);
    filtersEl.addEventListener("click", (event) => {
      const button = event.target.closest("[data-category]");
      if (!button) return;
      activeCategory = button.dataset.category;
      renderFilters();
      renderList();
    });
    window.addEventListener("hashchange", handleRoute);
  }

  function init() {
    statCount.textContent = articles.length;
    statCategories.textContent = uniqueCategories().length - 1;
    renderFilters();
    bindEvents();
    handleRoute();
  }

  init();
})();
```

- [ ] **Step 4: Run verification**

Run: `node work/verify-site.mjs`

Expected: no `FAIL:` lines.

---

### Task 4: Build The Visual System

**Files:**
- Create: `styles.css`
- Modify: `work/verify-site.mjs`

- [ ] **Step 1: Extend verification for CSS**

Append to `work/verify-site.mjs`:

```js
const css = read("styles.css");
for (const selector of [".site-header", ".hero", ".article-grid", ".article-card", ".article-detail", "@media"]) {
  assert(css.includes(selector), `styles.css must include ${selector}`);
}
assert(!css.includes("linear-gradient(135deg, #6"), "avoid dominant purple-blue gradient palette");
```

- [ ] **Step 2: Run verification to confirm it fails**

Run: `node work/verify-site.mjs`

Expected: `ENOENT` for `styles.css`.

- [ ] **Step 3: Create `styles.css`**

Create a clean professional stylesheet. Required rules:

```css
:root {
  --bg: #f7f8fb;
  --surface: #ffffff;
  --ink: #182033;
  --muted: #5b6472;
  --line: #e3e7ef;
  --accent: #1769aa;
  --accent-soft: #eaf4fb;
  --success: #0f7a5f;
  --radius: 8px;
  --shadow: 0 12px 30px rgba(24, 32, 51, 0.08);
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.6;
}

a {
  color: inherit;
  text-decoration: none;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 18px clamp(18px, 4vw, 56px);
  background: rgba(255, 255, 255, 0.92);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(16px);
}

.brand {
  font-weight: 800;
  letter-spacing: 0;
}

.nav {
  display: flex;
  gap: 18px;
  color: var(--muted);
  font-size: 0.95rem;
}

main {
  width: min(1180px, calc(100% - 32px));
  margin: 0 auto;
}

.hero {
  padding: 72px 0 38px;
}

.eyebrow,
.category {
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0;
  text-transform: uppercase;
}

.hero h1 {
  max-width: 780px;
  margin: 10px 0 16px;
  font-size: clamp(2.2rem, 6vw, 4.8rem);
  line-height: 1.02;
  letter-spacing: 0;
}

.hero-copy {
  max-width: 720px;
  color: var(--muted);
  font-size: 1.1rem;
}

.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 28px;
}

.stats span,
.filter-chip {
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
  padding: 10px 12px;
}

.toolbar {
  display: grid;
  gap: 14px;
  padding: 22px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.search-label {
  font-weight: 700;
}

#search-input {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 14px 16px;
  font: inherit;
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-chip {
  cursor: pointer;
  font: inherit;
  color: var(--muted);
}

.filter-chip.active {
  background: var(--accent-soft);
  border-color: var(--accent);
  color: var(--accent);
}

.article-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  padding: 28px 0 56px;
}

.article-card {
  display: flex;
  min-height: 260px;
  flex-direction: column;
  gap: 12px;
  padding: 22px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: 0 8px 24px rgba(24, 32, 51, 0.05);
}

.article-card h2 {
  margin: 0;
  font-size: 1.12rem;
  line-height: 1.35;
}

.article-card p {
  margin: 0;
  color: var(--muted);
}

.meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: auto;
  color: var(--muted);
  font-size: 0.9rem;
}

.article-detail {
  max-width: 840px;
  margin: 32px auto 72px;
  padding: clamp(22px, 4vw, 48px);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}

.back-link {
  color: var(--accent);
  font-weight: 700;
}

.article-header h1 {
  font-size: clamp(2rem, 5vw, 3.8rem);
  line-height: 1.08;
  letter-spacing: 0;
}

.article-body h2 {
  margin-top: 34px;
  font-size: 1.45rem;
}

.article-body p {
  color: #293244;
  font-size: 1.05rem;
}

.related {
  margin-top: 44px;
  border-top: 1px solid var(--line);
  padding-top: 28px;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.site-footer {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  padding: 34px clamp(18px, 4vw, 56px);
  background: var(--ink);
  color: #ffffff;
}

.site-footer p {
  max-width: 620px;
  color: #cbd5e1;
}

.footer-link {
  align-self: center;
  border: 1px solid rgba(255, 255, 255, 0.24);
  border-radius: var(--radius);
  padding: 10px 14px;
}

.empty-state {
  grid-column: 1 / -1;
  padding: 32px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
}

@media (max-width: 900px) {
  .article-grid,
  .related-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 680px) {
  .site-header,
  .site-footer {
    align-items: flex-start;
    flex-direction: column;
  }

  .nav {
    flex-wrap: wrap;
  }

  .article-grid,
  .related-grid {
    grid-template-columns: 1fr;
  }

  .hero {
    padding-top: 42px;
  }
}
```

- [ ] **Step 4: Run verification**

Run: `node work/verify-site.mjs`

Expected: no `FAIL:` lines.

---

### Task 5: Complete All 82 Vietnamese Article Records

**Files:**
- Modify: `articles.js`
- Modify: `work/source-snapshot.md`

- [ ] **Step 1: Add remaining source titles to `work/source-snapshot.md`**

Append the source title inventory from the public listing. It must include all records from `AI Money Lab Vs AI Profit Boardroom...` through `OpenClaw AI SEO: My Exact System for 700+ Daily Clicks`.

- [ ] **Step 2: Expand `articles.js` from 12 records to 82 records**

For each remaining source card, add one `article(...)` record using:

```js
article(
  "SOURCE TITLE EXACTLY AS PUBLIC LISTING",
  "Rewritten Vietnamese title for Hữu Hùng AI Automation",
  categories.agents,
  "2026-MM-DD",
  "N phút đọc",
  "Vietnamese excerpt of at least 80 characters that explains the practical value.",
  ["tag 1", "tag 2", "tag 3"],
  standardSections("Vietnamese topic phrase", "Vietnamese angle phrase", "Vietnamese practical use-case sentence")
)
```

Use `categories.agents`, `categories.seo`, `categories.tools`, `categories.models`, `categories.business`, `categories.automation`, `categories.productivity`, `categories.community`, or `categories.education` according to the public category and Vietnamese normalization rules.

- [ ] **Step 3: Remove unverifiable private claims from Vietnamese rewrites**

Search `articles.js` and ensure it does not include these strings:

```text
$300K/month
2,200+ members
2,800 members
700+ daily clicks
tripled my organic traffic
106K GitHub stars
4,600 GitHub stars
92.2% retrieval accuracy
```

If a source title includes a public number, rewrite the Vietnamese title to focus on the concept rather than repeating the number unless the number is independently public and necessary.

- [ ] **Step 4: Run verification**

Run: `node work/verify-site.mjs`

Expected: no `FAIL:` lines and article count assertion passes with 82 records.

---

### Task 6: Manual Browser Verification

**Files:**
- No code changes expected unless bugs are found.

- [ ] **Step 1: Start a local static server**

Run from project root:

```powershell
python -m http.server 4173
```

Expected: server starts at `http://localhost:4173/`.

- [ ] **Step 2: Open desktop viewport**

Open `http://localhost:4173/`.

Expected:

- Brand renders as `Hữu Hùng AI Automation`.
- Hero is visible without overlap.
- Article count says `82 bài viết`.
- Category count matches rendered categories.
- Article cards appear in a 3-column desktop grid.

- [ ] **Step 3: Test search**

Type `Claude` into the search box.

Expected:

- List narrows to Claude-related records.
- Clearing the search restores all records for the active category.

- [ ] **Step 4: Test category filtering**

Click `AI SEO`.

Expected:

- Filter chip becomes active.
- Only AI SEO articles remain.

- [ ] **Step 5: Test article detail routing**

Click the first visible article.

Expected:

- URL changes to `#/article/<slug>`.
- Article detail appears.
- Back link returns to the blog list.
- Related articles render.

- [ ] **Step 6: Test mobile width**

Resize browser to approximately 390px wide.

Expected:

- Header stacks cleanly.
- Cards are one column.
- Long Vietnamese words do not overflow.
- Article text remains readable.

---

### Task 7: Final Packaging

**Files:**
- Copy/Create user-facing deliverable under `outputs/huu-hung-ai-automation-blog/`

- [ ] **Step 1: Create output folder**

Create:

```text
outputs/huu-hung-ai-automation-blog/
```

- [ ] **Step 2: Copy final site files**

Copy:

```text
index.html
styles.css
articles.js
app.js
```

to:

```text
outputs/huu-hung-ai-automation-blog/
```

- [ ] **Step 3: Run verification against root files**

Run:

```powershell
node work/verify-site.mjs
```

Expected: no `FAIL:` lines.

- [ ] **Step 4: Report final paths**

Final response should link:

```text
outputs/huu-hung-ai-automation-blog/index.html
```

and mention whether the local server is still running.

---

## Self-Review

Spec coverage:

- Brand and Vietnamese positioning: Task 1 and Task 4.
- Public-source-only boundary: Task 2 and Task 5.
- 82 visible public articles: Task 2 and Task 5.
- Data-driven static website: Task 2 and Task 3.
- Search and category filters: Task 3 and Task 6.
- Article detail pages: Task 3 and Task 6.
- Clean professional design: Task 4 and Task 6.
- No strong sales CTA: Task 1 and Task 4.
- Verification: Task 1 through Task 7.

Placeholder scan:

- No `TBD`.
- No `TODO`.
- No unspecified "add appropriate" steps.
- Task 5 intentionally describes the repeatable per-article record pattern because the implementation must expand all 82 records using the public source snapshot.

Type consistency:

- Article fields match the design spec: `slug`, `title`, `sourceTitle`, `category`, `date`, `readTime`, `excerpt`, `tags`, `body`.
- Rendering functions in `app.js` consume the same fields verified in `work/verify-site.mjs`.
