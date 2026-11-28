---
title: Gemma Chat: build an offline app with a local model
desc: Ways to run Gemma models on your own machine to make an offline chat app: ready-made tools, calling the model from code, hardware limits and privacy.
min: 7
---
QUICK: Gemma is Google's family of open models, which can run on a personal computer or a phone. To build an offline chat app, you run the model with a local tool such as Ollama and call it from your own interface. Downloading the model needs the internet; after that the app runs without a network.
## What Gemma is
According to Google's official page, Gemma is a family of lightweight open models developed by Google DeepMind and other Google teams, built from the same research and technology as Gemini. According to the Gemma 4 page and model card (read on Nov 28, 2026), this generation comes in 5 sizes: E2B, E4B, 12B, 26B A4B and 31B. All sizes accept text and images; audio is only on E2B, E4B and 12B. The models were pre-trained on more than 140 languages, and the context window is 128K tokens on the small models and 256K on the medium ones. The model can run on your own machine, a mobile device or a hosting service.
## Ready-made ways to chat with Gemma offline
- **Ollama:** runs the model on your machine and opens a local address for other apps to call. This is the most common way to integrate it into your own app.
- **Prebuilt chat apps:** there are open-source apps that run Gemma locally. For example, the `ammaarreshi/gemma-chat` repo (MIT license) describes an Electron app for Macs with Apple Silicon chips that runs Gemma 4 through Apple's MLX framework, supports Ollama and works offline after the first model download. Its README calls it a proof of concept; I have not tried it.
- **Phones:** Google has an on-device model test app (Google AI Edge Gallery) for running Gemma offline on a phone.
- **Other tools** such as LM Studio and Jan can also run models locally with a graphical interface.
## Building your own offline chat app
The simple architecture has two parts: a **local model server** and your own **interface**.
1. Install Ollama and download a Gemma model:
```
ollama pull gemma4:31b
```
The names and sizes of available models change, so check the Ollama library. Large models need a lot of memory, see the limits section below. When checked on Nov 28, 2026, the Ollama library listed `gemma4:31b` at about 20 GB, with smaller versions too (`e2b`, `e4b`, `12b`). On a weaker machine, change the model name in both commands to a smaller one.
1. Call the model from code through the OpenAI-compatible address that Ollama opens:
```
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gemma4:31b", "messages": [{"role": "user", "content": "Hello"}]}'
```
1. Write an interface (a web page or desktop app) that sends messages to this address and shows the answer.
2. Store conversations on the machine (a file or local database) if you want to keep history.
Because everything runs on the machine, your app works without a network, as long as the model has been downloaded beforehand.
## Hardware limits
The larger the model, the more RAM or graphics card memory it needs. Nous Research's guide to running agents locally gives a reference of about 8 GB of RAM for a 3-billion-parameter model and 32 GB or more for models of 27 billion parameters and up. Choose the version that fits your machine, and remember to test carefully on the devices your users will really use.
## What to test before release
- **Vietnamese quality:** try many realistic questions, because quality depends on the model and size.
- **Speed on weak machines:** is the wait acceptable.
- **Privacy:** content does not leave the machine during local inference, but review whether the app has any other feature that sends data out.
- **License:** Gemma 4 is released under Apache 2.0 (stated on the model card). Older Gemma generations use the separate Gemma Terms of Use, so check the license of the exact version you use before building a commercial product.
## When this approach fits
- An app that handles sensitive data which needs to stay on the machine.
- Environments with no or limited internet.
- You want to avoid per-call costs.
When you need the highest quality or many simultaneous users, see [Ollama and Hermes: when does a local AI agent beat the cloud?](ollama-va-hermes-khi-nao-local-ai-agent-tot-hon-cloud.html).
