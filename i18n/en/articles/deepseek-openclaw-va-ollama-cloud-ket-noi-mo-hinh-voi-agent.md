---
title: DeepSeek, OpenClaw and Ollama Cloud: connecting models to an agent
desc: Connect DeepSeek and Ollama Cloud to OpenClaw through the official provider plugins: provider ids, key variables, choosing a model, fallbacks and data notes.
min: 7
---
QUICK: The OpenClaw documentation has dedicated guides for DeepSeek (id `deepseek`, variable `DEEPSEEK_API_KEY`) and Ollama Cloud (id `ollama-cloud`, variable `OLLAMA_API_KEY`). For DeepSeek you install the official plugin and run onboarding; for Ollama Cloud run `openclaw onboard --auth-choice ollama-cloud`. Model names change over time, so check with `openclaw models list`.
## Two providers, two ways of using them
- **DeepSeek:** calls DeepSeek's API directly with your key. Data is sent to DeepSeek.
- **Ollama Cloud:** runs large models on Ollama's cloud infrastructure so you do not need a powerful graphics card. According to Ollama's documentation, you can call through the API (no Ollama install needed) or run cloud models from the app, the CLI and the local API; both ways need an Ollama account. The cloud model catalog is at `ollama.com/search?c=cloud`.
For how this differs from running a model on your own machine, see [Running local models for OpenClaw: runtimes, configuration and risks](deepseek-va-openclaw-thiet-lap-local-gateway-cho-agent.html).
## How OpenClaw connects providers
The "Official provider plugins" page lists dozens of bundled provider plugins (including DeepSeek, Moonshot, Ollama Cloud, OpenRouter, Together, Groq...). According to that page, official plugins do not need a `models.providers` entry: you enable the plugin, set authentication and choose a model. Use `models.providers` only for custom providers or narrow settings such as timeouts.
The page's table states:
- **DeepSeek:** id `deepseek`, auth variable `DEEPSEEK_API_KEY`, example model `deepseek/deepseek-v4-flash`.
- **Ollama Cloud:** id `ollama-cloud`, auth variable `OLLAMA_API_KEY`, example model `ollama-cloud/kimi-k2.6`.
The dedicated DeepSeek page gives the install command `openclaw plugins install @openclaw/deepseek-provider` and the onboarding command `openclaw onboard --auth-choice deepseek-api-key`, which sets `deepseek/deepseek-v4-pro` as the default. The Ollama Cloud page gives `openclaw onboard --auth-choice ollama-cloud`, with `ollama-cloud/minimax-m2.7` as the default model.
## Choosing and checking a model
OpenClaw's general commands for choosing a model:
```
openclaw models list
openclaw models list --provider deepseek
openclaw models set deepseek/<model-name>
```
Models are written as `provider/model`. Get the exact name from `openclaw models list`, because model names change over time. The catalog on OpenClaw's DeepSeek page (read on 2026-11-25) has `deepseek/deepseek-flash` and `deepseek/deepseek-v4-pro`, while `deepseek/deepseek-v4-flash` is a legacy alias of V4.1 Flash. The example on the official plugins page still uses this old alias, so do not copy it mechanically. The DeepSeek page also says `deepseek-chat` and `deepseek-reasoner` were retired on Jul 24, 2026.
In a chat session, `/model` selects the model as a mandatory user choice; if it fails, OpenClaw reports an error instead of switching to a fallback. `/status` shows the model in use and, if different, the fallback model and the reason.
## Fallback (failover)
Fallback configuration per the "Model failover" documentation:
- `agents.defaults.model.primary` is the default model and `agents.defaults.model.fallbacks` is the ordered fallback list.
- Each agent's model is strict unless that agent has its own `fallbacks`; use `fallbacks: []` to state strictness explicitly.
- It switches to the next model on authentication errors, rate limits, overload, timeouts, billing lockouts, `model_not_found` or context overflow that compaction cannot resolve.
- It does not switch on an intentional abort, the provider's final refusal, or local errors such as a session write conflict.
- Cooldown: 30 seconds on the first failure, 1 minute on the second, up to 5 minutes from the third; for permanent billing and authentication failures the API key is locked for the first 10 minutes.
A sensible example: DeepSeek as the main model, an Ollama Cloud model or another provider as the fallback, to avoid stopping when one side is limited. However each provider switch sends the same content to another party, so set a fallback only for providers you accept on data grounds.
## About data and cost
- Ollama says it only processes prompts and responses to answer requests and **does not use them to train models**, but the page I read does not state a retention period; read their privacy policy and Cloud FAQ. Cloud models do not yet support structured output, and capabilities differ between models; models may also be removed over their lifecycle.
- DeepSeek's price is per token, with peak and off-peak prices (see [Hermes and DeepSeek: setting up a model for an agent in a real workflow](hermes-va-deepseek-thiet-lap-mo-hinh-cho-agent-trong-workflow-that.html) for the price table read on 2026-11-15). Ollama Cloud has its own plans and balances, and I have not read the pricing page.
- An agent runs many steps so it burns tokens fast; set a limit on the provider account.
## Testing workflow
1. Set the key, run `openclaw models list --provider deepseek` to see the real model names.
2. Choose a model and message one small task that uses tools.
3. Check `/status`, run `openclaw doctor`.
4. Add a fallback after the main model runs well.
