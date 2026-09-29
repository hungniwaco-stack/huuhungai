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

  function categoryCode(category) {
    const codes = {
      "AI Agent": "AGENT",
      "AI SEO": "SEO",
      "Công cụ AI": "TOOL",
      "Mô hình AI": "MODEL",
      "Tự động hóa doanh nghiệp": "AUTO",
      "Năng suất": "FLOW",
      "Cộng đồng AI": "LEARN"
    };
    return codes[category] || "AI";
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
        <div class="card-topline">
          <span class="category">${escapeHtml(article.category)}</span>
          <span class="index-code">${categoryCode(article.category)}</span>
        </div>
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
      : `<p class="empty-state">Không tìm thấy bài viết phù hợp. Thử tìm “Claude”, “AI SEO”, “OpenClaw”, “Hermes” hoặc chọn lại chuyên mục Tất cả.</p>`;
    document.title = "Hữu Hùng AI | Blog AI Automation cho người Việt";
  }

  function relatedArticles(current) {
    return articles
      .filter((article) => article.slug !== current.slug && article.category === current.category)
      .slice(0, 3);
  }

  function headingId(text, index) {
    return `section-${index}-${text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/đ/g, "d").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")}`;
  }

  function renderBody(blocks) {
    let headingIndex = 0;
    return blocks.map((block) => {
      if (block.startsWith("## ")) {
        headingIndex += 1;
        const text = block.slice(3);
        return `<h2 id="${headingId(text, headingIndex)}">${escapeHtml(text)}</h2>`;
      }
      return `<p>${escapeHtml(block)}</p>`;
    }).join("");
  }

  function renderToc(blocks) {
    let headingIndex = 0;
    const links = blocks
      .filter((block) => block.startsWith("## "))
      .map((block) => {
        headingIndex += 1;
        const text = block.slice(3);
        return `<a href="#${headingId(text, headingIndex)}">${escapeHtml(text)}</a>`;
      })
      .join("");
    return `<aside class="toc"><strong>Mục lục</strong>${links}</aside>`;
  }

  function renderDetail(slug) {
    const article = articles.find((item) => item.slug === slug);
    if (!article) {
      setRoute("/");
      return;
    }

    const related = relatedArticles(article);
    const blocks = article.body.split("\n\n");
    listEl.hidden = true;
    detailEl.hidden = false;
    detailEl.innerHTML = `
      <div class="article-shell">
        <div class="article-main">
          <a class="back-link" href="#/">Quay lại blog</a>
          <header class="article-header">
            <span class="category">${escapeHtml(article.category)} / ${categoryCode(article.category)}</span>
            <h1>${escapeHtml(article.title)}</h1>
            <p>${escapeHtml(article.excerpt)}</p>
            <div class="meta">
              <span>${escapeHtml(article.date)}</span>
              <span>${escapeHtml(article.readTime)}</span>
            </div>
          </header>
          <div class="article-body">${renderBody(blocks)}</div>
          ${related.length ? `<section class="related">
            <h2>Bài liên quan</h2>
            <div class="related-grid">${related.map(articleCard).join("")}</div>
          </section>` : ""}
        </div>
        ${renderToc(blocks)}
      </div>
    `;
    document.title = `${article.title} | Hữu Hùng AI`;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function setRoute(path) {
    window.location.hash = path === "/" ? "#/" : `#${path}`;
  }

  function handleRoute() {
    const hash = window.location.hash || "#/";
    const articleMatch = hash.match(/^#\/article\/(.+)$/);
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
    detailEl.addEventListener("click", (event) => {
      const link = event.target.closest(".toc a");
      if (!link) return;
      event.preventDefault(); // ponytail: hash is owned by the router, so scroll manually
      document.getElementById(link.getAttribute("href").slice(1))?.scrollIntoView({ behavior: "smooth" });
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
