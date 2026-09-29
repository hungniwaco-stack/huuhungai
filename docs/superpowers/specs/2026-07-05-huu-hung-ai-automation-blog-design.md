# Huu Hung AI Automation Blog Design

Date: 2026-07-05

## Goal

Build a Vietnamese personal-brand blog named **Huu Hung AI Automation** based on the public article topics and blog structure visible on `https://aiprofitboardroom.com/blog/`.

The website should establish authority first, not sell aggressively. It should feel clean, professional, trustworthy, and easy for Vietnamese readers to understand.

## Source Boundary

Use only public information from the source blog:

- Public article titles
- Public article categories
- Public summaries/descriptions
- Public dates and reading-time signals where visible
- Public blog structure and content grouping patterns

Do not use or invent internal metrics such as traffic, revenue, conversion rates, private community data, or backend analytics.

The articles must not be copied or translated verbatim. They should be rewritten as original Vietnamese content using the same topic intent and public-facing theme.

## Scope

The first version is a content-first blog that can later expand into services, courses, resources, or community pages.

Included:

- Blog homepage
- Category filters
- Search
- Article cards
- Article detail pages
- Related articles
- Light credibility/continuation CTA
- Responsive desktop and mobile layout

Excluded for the first version:

- Payment
- Login
- CMS admin panel
- Newsletter backend
- Real analytics dashboard
- Strong sales landing page

## Brand

Brand name: **Huu Hung AI Automation**

Vietnamese display name: **Hữu Hùng AI Automation**

Positioning:

> Hướng dẫn AI Automation thực chiến cho người Việt.

Tone:

- Expert but not academic
- Practical but not exaggerated
- Clear Vietnamese with correct AI/business terminology
- Suitable for Vietnamese founders, marketers, operators, consultants, and learners

Terminology:

- Keep common technical terms where useful: AI agent, workflow, automation, MCP, local model, lead generation, SEO AI.
- Explain difficult terms briefly in context.

## Visual Direction

Selected direction: **Clean, expert, trustworthy**.

Design traits:

- Light background
- High readability
- Calm professional color palette
- Simple header
- Spacious article layout
- Compact article cards
- No aggressive sales styling
- No oversized marketing landing-page hero

Header navigation:

- Blog
- Chủ đề
- Tài nguyên
- Giới thiệu

## Information Architecture

### Blog Homepage

The homepage should include:

- Brand header
- Hero section with clear positioning
- Public content stats such as:
  - number of visible articles imported from the source list
  - number of topic groups
  - representative topic names
- Search input
- Category filter chips
- Article grid/list
- Light CTA at the end

### Article Detail Page

Each article should include:

- Vietnamese title
- Category
- Publication date
- Reading time
- Short intro
- Main body, approximately 1,000-1,500 Vietnamese words
- Practical Vietnamese-market framing
- Conclusion
- Related articles
- Back-to-blog navigation

### Categories

Initial categories:

- AI Agent
- AI SEO
- Công cụ AI
- Mô hình AI
- Tự động hóa doanh nghiệp
- Năng suất
- Cộng đồng AI

Article categories may be normalized from source categories to these Vietnamese categories.

## Content Model

Use a data-driven static website.

Each article record should contain:

- `slug`
- `title`
- `sourceTitle`
- `category`
- `date`
- `readTime`
- `excerpt`
- `tags`
- `body`

The `sourceTitle` is for internal traceability and should not be emphasized in the UI.

## Technical Design

Use a static, data-driven implementation:

- `index.html`: shared shell for blog listing and article view
- `styles.css`: responsive clean visual system
- `articles.js`: article data
- `app.js`: rendering, filtering, searching, article routing

Routing can use URL hash or query parameters so the site works without a backend.

The site should run as static files. A local dev server may be used for preview and verification if needed.

## User Experience

Required interactions:

- Users can search article titles, excerpts, tags, and categories.
- Users can filter by category.
- Users can click an article card to open the article detail.
- Users can return to the blog list.
- Related articles should be shown on detail pages.
- Mobile layout must remain readable and not overflow.

## CTA Strategy

The CTA should be light and authority-building:

- "Xem bài mới nhất"
- "Theo dõi cập nhật"
- "Tiếp tục học AI Automation cùng Hữu Hùng"

No hard-selling CTA in the first version.

## Content Generation Rules

For each public article from the source blog:

1. Preserve the topic intent.
2. Rewrite the title in Vietnamese for local readers.
3. Write a new Vietnamese excerpt.
4. Assign a normalized Vietnamese category.
5. Write an original Vietnamese article body.
6. Avoid unsupported claims.
7. Avoid copying source wording.
8. Keep the writing practical and easy to understand.

If the full source article content is not fetched, article bodies should be written from the public title, category, and summary only, with no claim that the source article was fully translated.

## Verification

Before completion:

- Open the website locally.
- Confirm the article list renders.
- Confirm search works.
- Confirm category filters work.
- Confirm article detail pages open.
- Confirm Vietnamese text displays correctly.
- Check desktop and mobile widths.
- Confirm no broken layout or overlapping text.

## Risks And Mitigations

Risk: Copying too closely from the source site.
Mitigation: Use public topics as inspiration and write original Vietnamese content.

Risk: Very large amount of article content.
Mitigation: Use a consistent article template, then prioritize deeper polishing for core AI SEO and AI Agent articles.

Risk: Static data file becomes large.
Mitigation: Keep data structured and separate from rendering logic.

Risk: Source article count may change.
Mitigation: Treat the imported list as a snapshot from the public page at build time.

## Approval Status

Approved by user during brainstorming:

- Brand: Hữu Hùng AI Automation
- Content approach: rewrite public topics into original Vietnamese articles
- CTA strategy: authority-first, no strong sales
- Scope: blog first, expandable later
- Article scope: all public articles visible on the source blog
- Detail pages: yes
- Article length: 1,000-1,500 Vietnamese words each
- Technical approach: data-driven static blog
- Visual style: clean, expert, trustworthy
