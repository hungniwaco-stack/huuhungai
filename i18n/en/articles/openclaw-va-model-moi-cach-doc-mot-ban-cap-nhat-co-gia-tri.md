---
title: OpenClaw and new models: how to read an update that is worth it
desc: When a new model appears: check whether OpenClaw supports it, test safely with the model command, read fallbacks and context, and update with a backup.
min: 7
---
QUICK: An update or a new model is only worth it if it works well on your tasks. Check whether OpenClaw lists the model (`openclaw models list`), try it as a separate choice (`/model`) before changing the default, check the context and tool calling, then update the version with a backup. Do not change the default model just because of a news headline.
## How to read news about a new model
Each time a new model appears, ask three questions:
1. **What does it change for my work?** (accuracy, speed, price, context, tool-calling ability).
2. **Who says so?** Figures published by the vendor itself need re-measuring.
3. **What does switching cost?** Including token price, testing time and the risk of breaking the current workflow.
For rumors about unreleased models, see [Rumors about new AI models: how should you read leaked information?](tin-don-mo-hinh-gpt-moi-nen-doc-thong-tin-ro-ri-nhu-the-nao.html).
## Step 1: does OpenClaw support the model yet
Models in OpenClaw are written as `provider/model`. Check with:
```
openclaw models list
openclaw models list --provider openai
openclaw models set provider/model
```
If the model is not yet in the official provider's list, you can declare it manually through `models.providers` (see [OpenClaw and Kimi](openclaw-va-kimi-dung-agent-stack-voi-mo-hinh-mo.html) for an example). The provider documentation also has a practical note: if your API organization does not yet have access to a new version, explicitly set the version you do have (the documentation uses OpenAI as the example, and says signing in again keeps an explicitly set primary model).
## Step 2: try it as a separate choice, do not change the default right away
In a chat session, `/model` selects the model as a user override. According to the failover documentation, if this choice fails OpenClaw reports an error instead of switching to a fallback, which means you see the problem immediately. `/status` shows which model is in use; `/new` or `/reset` clears automatic pins. Only when the trial goes well should you change `agents.defaults.model.primary`.
## Step 3: check context, tools and cost
- **Context and tool calling:** a model that answers short questions can still break an agent turn. Try one real task that uses tools. For local models, `openclaw infer model run --local` and `--gateway` help separate where the error lies.
- **Set the right limits:** for a manually declared model, set `contextWindow` and `maxTokens` to the real limits. If left blank, the documentation says the defaults may not match (for example a default `maxTokens` of 32768 and a fallback context of 200000).
- **Cost:** record the price in `cost` if you want to track it; remember the different price tiers between fast and standard modes at some providers.
## Step 4: set up a sensible fallback
Set `agents.defaults.model.fallbacks` so that when the new model is rate-limited or fails, the agent switches to a stable model. Remember that fallbacks only apply when the model is the default, not when you choose it manually. For the switching conditions and cooldown time, see [DeepSeek, OpenClaw and Ollama Cloud](deepseek-openclaw-va-ollama-cloud-ket-noi-mo-hinh-voi-agent.html).
## Step 5: update the OpenClaw version safely
According to the update documentation:
- Take a verified backup before a major update; the automatic config copy is not a full backup of the state.
- Use `openclaw update`; the channels are `latest`, beta and an extended stable channel. `main` is not a release.
- An older version cannot read a database with a newer schema, so restoring must come with the right backup and the right version.
- After the update: `openclaw doctor`, `openclaw gateway status --deep`, `openclaw channels status --probe`.
In addition, run `openclaw security audit` because defaults can change, see [An OpenClaw learning path](lo-trinh-hoc-openclaw-cach-theo-kip-cong-cu-ai-agent-moi.html).
## Decision checklist
- Change the default when: the new model wins on 3 of your real tasks on accuracy or cost, calls tools reliably and you have a fallback.
- Keep things as they are when: the benefit lies only in the news headline, or you have not been able to measure it.
- Always keep a path back to the old model (record the configuration before changing).
