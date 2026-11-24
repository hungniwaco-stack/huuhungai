---
title: Open Design and Claude Design for agencies: how to choose an AI design tool
desc: Open Design is an open-source design space using agents already on your machine: install, export, privacy and how to choose against cloud AI design services.
min: 7
---
QUICK: Open Design (repo `nexu-io/open-design`, Apache-2.0 license) is a design space for AI agents that prefers to run locally and uses the agent CLIs you have already installed instead of bundling a model. I have no data comparing its quality with Claude Design, so this article compares by criteria for choosing a tool: where it runs, data, model cost, export formats and maturity.
## What Open Design is
According to the README, Open Design is a design space for AI agents: you start with a brief, use a coding agent or OpenDesign Cloud to build a prototype in your design system, teammates review and the agent refines within the same project. There are skills, design templates, design systems and plugins that users can view and edit. The license is Apache-2.0, with some bundled skills and templates keeping their own licenses (such as MIT).
Many repos on GitHub are forks with the same description; the original repo per search results is `nexu-io/open-design`. The star counts and skill counts in introductory articles do not match each other, so look at the original repo.
## Installation and platforms
- **Desktop app:** macOS (Apple Silicon and Intel) and Windows (x64), downloaded from open-design.ai or GitHub Releases. **Linux has no prebuilt version yet**, and the README says to run from source for now.
- **Install into the agent you already use:**
```
od mcp install <agent>
```
With `<agent>` being one of the agents the README lists (such as `claude`, `codex`, `cursor`, `copilot`, `openclaw`, `hermes`, `kimi`, `opencode`...). There is an equivalent command through `curl ... | sh` from open-design.ai; read the script before running it.
- **Docker:**
```
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
```
then open `http://127.0.0.1:7456`.
- **From source:** needs Node `~24` and pnpm `10.33.x`.
## How it uses agents
The desktop app automatically detects agent CLIs on `PATH`; the README says about 26 CLIs are supported. When running with an agent that has file permissions, the agent combines the chosen skill or template with your `DESIGN.md` file, writes project files and Open Design previews them. In bring-your-own-key (BYOK) mode with no file tools, the agent returns one complete `<artifact>` block. BYOK supports OpenAI, Anthropic, Azure OpenAI, Gemini, Ollama, LM Studio, vLLM and any OpenAI-compatible endpoint. There is also "OpenDesign Cloud", the official model service integrated in the app.
## Output and handoff
Prototypes are HTML pages shown in a sandboxed iframe; slide decks export to HTML, PDF, PPTX, ZIP or Markdown; images go through `gpt-image-2`, ImageRouter or a custom API; motion video (HyperFrames) exports MP4. The README says the HTML and CSS can be passed on to Cursor, Codex or Claude Code.
## Privacy and security
- The README calls the product "local-first": the project runs locally or in a system you deploy yourself. Requests to cloud models and OpenDesign Cloud are sent to the respective service.
- Product analytics and session recording only with your consent; filtered safety and reliability telemetry is always on.
- The background process by default listens only on `127.0.0.1`; there is SSRF blocking for internal address ranges unless you open it with `OD_ALLOWED_INTERNAL_HOSTS`.
## Limits the README states itself
No prebuilt Linux version yet; automatic MCP configuration for Claude Desktop is only on macOS and Windows; fine-grained editing through comment mode is only "partial"; AI-proposed tuning panels are "not yet implemented"; still planned: a plugin SDK, converting from Figma and Pencil to code. On macOS, the `/usr/bin/od` command can shadow Open Design's `od` command.
## About Claude Design
I could not read Claude Design's official documentation so I do not describe its features or price; some articles say it is a cloud service tied to an Anthropic model, but that is secondary. Read Anthropic's official page before comparing.
## How to choose for an agency
1. **Where the data sits:** do clients allow design assets to leave the machine? Local is an advantage.
2. **Model cost:** Open Design uses agents and keys you already have; cloud services charge by plan. Calculate by real volume.
3. **Export formats:** do they meet your handoff needs (HTML, PDF, PPTX)?
4. **Maturity:** the README still has many "not done" items; try it on a small project.
5. **Controlling agent permissions:** the agent writes real files; run in a separate folder and review changes, see the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html).
Run the same brief on both tools and compare the output, time and cost, following the framework in [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
