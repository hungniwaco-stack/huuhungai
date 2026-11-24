---
title: OpenClaw and Kimi: configuring Moonshot, Kimi Coding and Ollama Cloud
desc: Use Kimi with OpenClaw through Moonshot AI and Kimi Coding: key variables, sample config, the China endpoint, Ollama Cloud and notes on cost and data.
min: 7
---
QUICK: OpenClaw supports Kimi in two ways: **Moonshot AI** (`MOONSHOT_API_KEY`, model `moonshot/kimi-k2.6`) and **Kimi Coding** (`KIMI_API_KEY`, model `kimi/kimi-for-coding`). Both have a ready-made onboarding command. You can also call Kimi through Ollama Cloud. The prices in the documentation's sample config are only example values, so do not use them to plan a budget.
## "Open models" and what needs to be said clearly
This article is about connecting Kimi to OpenClaw. Many articles lump models such as Kimi together as "open models", but whether a model's weights are published is a question for each individual release. When you use the Moonshot API, you use their cloud service, not weights running on your own machine. For running a model locally, see [Running local models for OpenClaw: runtimes, configuration and risks](deepseek-va-openclaw-thiet-lap-local-gateway-cho-agent.html).
## Route 1: Moonshot AI (Kimi through the Moonshot API)
Sample config from the "Provider examples" documentation (JSON5):
```
{
  env: { vars: { MOONSHOT_API_KEY: "sk-..." } },
  agents: {
    defaults: {
      model: { primary: "moonshot/kimi-k2.6" },
      models: { "moonshot/kimi-k2.6": { alias: "Kimi K2.6" } },
    },
  },
  models: {
    mode: "merge",
    providers: {
      moonshot: {
        baseUrl: "https://api.moonshot.ai/v1",
        apiKey: "${MOONSHOT_API_KEY}",
        api: "openai-completions",
        models: [
          { id: "kimi-k2.6", name: "Kimi K2.6", reasoning: false, input: ["text", "image"],
            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },
            contextWindow: 262144, maxTokens: 262144 },
        ],
      },
    },
  },
}
```
- The key variable is `MOONSHOT_API_KEY`, and the model reference is `moonshot/kimi-k2.6`.
- China endpoint: change `baseUrl` to `https://api.moonshot.cn/v1`, or run `openclaw onboard --auth-choice moonshot-api-key-cn`.
- The `cost` and `contextWindow` numbers in the block above are part of the config example. Check the real prices and limits on Moonshot's page before relying on them.
## Route 2: Kimi Coding
```
{
  env: { vars: { KIMI_API_KEY: "sk-..." } },
  agents: {
    defaults: {
      model: { primary: "kimi/kimi-for-coding" },
      models: { "kimi/kimi-for-coding": { alias: "Kimi Code" } },
    },
  },
}
```
This is a built-in provider that is Anthropic-compatible. The onboarding shortcut is `openclaw onboard --auth-choice kimi-code-api-key`.
## Route 3: Kimi through Ollama Cloud
In the provider plugin table, Ollama Cloud (id `ollama-cloud`, variable `OLLAMA_API_KEY`) has an example model `ollama-cloud/kimi-k2.6`. For details see [DeepSeek, OpenClaw and Ollama Cloud: connecting models to an agent](deepseek-openclaw-va-ollama-cloud-ket-noi-mo-hinh-voi-agent.html), including the notes on Ollama's data handling.
## Which route to choose
- You need a direct integration with Moonshot and want to manage costs on a Moonshot account: route 1.
- Mainly for coding and you want a prebuilt provider: route 2.
- You already use Ollama and want a single account: route 3.
Try the same real task on the models you are considering and compare accuracy, speed and cost, instead of trusting a generic comparison table. For a scoring framework, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
## Fallbacks and tool permissions
Set fallbacks with `agents.defaults.model.fallbacks`; if you pick a model manually with `/model`, an error is reported instead of switching to a fallback. Outside models may resist prompt injection less well than top-tier models, so keep tool permissions narrow and read the [security lessons](openclaw-update-bai-hoc-ve-tich-hop-message-cron-va-bao-mat.html).
## A note on data
Using an API means conversation content, including files the agent reads, is sent to the provider. Read Moonshot's data policy (and Ollama's if you use route 3) and choose the endpoint that matches your region. Do not put in customer data or secrets until you are sure.
