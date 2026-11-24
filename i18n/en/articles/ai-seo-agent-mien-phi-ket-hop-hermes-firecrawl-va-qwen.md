---
title: A free AI SEO agent: combining Hermes, Firecrawl and Qwen
desc: Build an SEO-checking agent with Hermes Agent, Firecrawl and a locally run Qwen model: the workflow, the limits of the free tier and crawling notes.
min: 8
---
QUICK: Firecrawl turns web pages into clean Markdown for the agent to read, Hermes Agent orchestrates the work, and a locally run model handles the analysis. You can build an SEO-checking agent at almost no cost, but "free" has limits: Firecrawl's quota, the capability of the local model and your own time.
## The big picture
- **Firecrawl** fetches web content. According to its documentation, it offers operations such as web search, fetching one page's content (scrape), mapping a website's URLs (map) and crawling a whole site (crawl), returning Markdown or structured data.
- **Hermes Agent** is Nous Research's agent, which orchestrates steps, keeps memory and calls tools.
- **A local model** (for example a Qwen-family model run with Ollama) reads the data and writes conclusions.
The idea: the agent gets a list of a site's URLs, reads each page, checks the basic SEO elements, then writes a report.
## About the word "free"
- **Firecrawl:** the documentation says some page-fetch requests work without a key, and advises creating a free account for a higher quota. They also have a self-hosted (open-source) version, but I have not verified the license. Quotas and terms may change, so see the current pricing page.
- **Local model:** no per-use charge but it needs a capable machine. Hermes requires a model that can call tools and has a context of at least 64,000 tokens, see [A free local AI agent with Hermes and Ollama: when to use it](ai-agent-local-mien-phi-voi-hermes-va-ollama-khi-nao-nen-dung.html).
- **Time and quality:** a small model may miss errors, so you must check again.
## Connecting Firecrawl to Hermes through MCP
Hermes supports MCP (Model Context Protocol), which lets you add outside tools. Hermes's documentation explains adding a remote-type MCP server in the `config.yaml` file:
```
mcp_servers:
  firecrawl:
    url: "https://mcp.firecrawl.dev/v2/mcp"
```
The address above comes from the Firecrawl documentation, where they say this MCP server supports search, page fetching and file parsing. After configuring, check with:
```
hermes mcp test firecrawl
```
This command connects and lists the tools it finds. If an authentication key is needed, add it in the `headers` section as in the Hermes documentation's example. Use `tools.include` to allow only the tools you need, following their security recommendation.
## Suggested SEO checking workflow
1. **Map the site:** ask the agent to list the URLs of the website to check.
2. **Fetch each page** and extract the elements: title, meta description, headings, canonical tag, internal links, content length.
3. **Check against the rules** you set beforehand: one `h1` per page, no duplicate titles and descriptions, a canonical present.
4. **Gather the results** into an error table by priority.
5. **You review** and decide what to fix.
A sample prompt:
```
Use the map tool to list up to 30 URLs of the site example.com.
For each URL, fetch the page and check: exactly one h1, a title and meta description,
a canonical. Return a table with URL, errors found, priority. Do not change anything.
```
## Quality limits
- A page-fetch tool only sees the displayed content and does not replace Search Console data on indexing and impressions.
- A local model may miss things or judge wrongly. Verify important errors by hand.
- A technical check is only one part of SEO. It does not judge the real value of the content, see [Claude Code SEO Agent](claude-code-seo-agent-quy-trinh-xay-noi-dung-seo-bang-ai.html).
## Crawling notes
- Crawl only sites you own or have permission for.
- Respect `robots.txt` and the terms of use of the site being scanned.
- Limit the rate so you do not load someone else's server.
- Do not collect personal data without a lawful basis.
