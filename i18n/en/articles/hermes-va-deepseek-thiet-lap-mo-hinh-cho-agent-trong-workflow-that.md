---
title: Hermes and DeepSeek: setting up a model for an agent in a real workflow
desc: Use DeepSeek as the model for Hermes Agent: declaring the provider, the API key, choosing a model, peak and off-peak pricing and data considerations.
min: 7
---
QUICK: Hermes Agent supports DeepSeek as its own provider (id `deepseek`, key in the `DEEPSEEK_API_KEY` variable). You get a key from the DeepSeek platform, run `hermes model` to choose it, then use it as normal. The most important thing to note is that model names and prices change over time, and your data is sent to the provider.
## How Hermes and DeepSeek fit together
Hermes is the orchestrating agent, and DeepSeek is the model that provides the "brain". According to Hermes's provider documentation, DeepSeek is in the list of providers reached directly through an API, with the provider id `deepseek`, the key set in `~/.hermes/.env` under the name `DEEPSEEK_API_KEY` and the OpenAI-compatible base address `https://api.deepseek.com/v1`. That page gives no example of an original DeepSeek model name; you choose in the wizard.
## Steps
1. **Create an API key** on the DeepSeek platform (`platform.deepseek.com`, API keys section). Keep it secret like a password.
2. **Run the provider picker** in a terminal, outside any chat session:
```
hermes model
```
Choose DeepSeek, enter the key when asked and choose a model. The `/model` command in a chat session only switches between providers you have already configured.
1. **Or set the key by command:**
```
hermes config set DEEPSEEK_API_KEY your-key
```
1. **Try one easy-to-verify question** and then hand over a task that uses tools to confirm the model calls tools correctly.
Another way, if you want to declare the endpoint yourself: use a custom endpoint with `provider: custom` and `base_url` pointing at an OpenAI-compatible address, as in [A free local AI agent with Hermes and Ollama: when to use it](ai-agent-local-mien-phi-voi-hermes-va-ollama-khi-nao-nen-dung.html).
## Model names and prices (read on 2026-11-15)
DeepSeek's API documentation currently lists two model names:
- `deepseek-flash` (version DeepSeek-V4.1-Flash-1017)
- `deepseek-v4-pro` (version DeepSeek-V4-Pro-0813)
The old name `deepseek-v4-flash` is still accepted but is redirected to Flash and billed at the Flash price. Both support tool calling and JSON output, with thinking and non-thinking modes. The pricing page lists a context length of 1M tokens (the page shows one shared figure for both columns, so it may not apply to both) and exceeds Hermes's minimum requirement of 64,000 tokens.
Prices per million tokens (the "$" symbol as the page shows it, with no currency code stated), off-peak and peak:
- **deepseek-flash:** cache-hit input 0.003 and 0.006; cache-miss input 0.15 and 0.3; output 0.6 and 1.2.
- **deepseek-v4-pro:** cache-hit input 0.022 and 0.044; cache-miss input 0.66 and 1.32; output 1.98 and 3.96.
Peak hours are 01:00 to 04:00 and 06:00 to 10:00 UTC from Monday to Friday, except Chinese holidays; outside those windows the off-peak price, half as much, applies.
## Things to weigh when choosing DeepSeek for an agent
- **Cost.** An agent calls the model many turns, so the cached input price matters. Hermes's stable prompt helps raise the cache-hit rate; changing the model or provider mid-session loses this advantage.
- **Data.** Using the API means conversation content, including files the agent reads, is sent to DeepSeek. Read their data policy and terms, and do not put in customer data or confidential information if you are not sure. If data must not leave the machine, look at the local option.
- **Tool reliability.** Each model is better or worse at calling tools. Test on your real tasks before using it for important work.
- **Fallback.** You can set DeepSeek as the main model and another provider as the fallback, or the reverse, with `fallback_providers` (see [Hermes AI Course: understanding multi-agent, profiles and fallback chains](hermes-ai-course-hieu-multi-agent-profile-va-fallback-chain.html)).
## Assigning models by role
Not every task needs the most expensive model. Hermes lets you set a separate model for subagents with `delegation.model` and `delegation.provider`, or pin a separate model to each profile. One common approach: a strong model for planning and review, a cheap model for repetitive steps such as summarizing and classifying. Measure the real cost after a week instead of guessing.
## A testing workflow before real use
1. Choose three real tasks, small enough.
2. Run them with DeepSeek and with the model you currently use.
3. Compare on accuracy, number of fixes, time and cost, using the framework in [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
