---
title: Where open source AI is winning: lessons for small businesses
desc: Open source and open models in AI: the OSI definition, how it differs from open weights, and how a small business chooses between self-hosting and a service.
min: 7
---
QUICK: Not every model called "open" is open source in the strict sense. The Open Source Initiative's definition requires sharing information about the training data, the source code and the parameters. For a small business, the practical questions are what the license allows, the cost of self-hosting versus using a service, and who is responsible for operations.
## "Open" has many meanings
The term "open source" is often used loosely in AI. There are at least two different concepts:
- **Open source by the OSI definition:** the Open Source Initiative has an "Open Source AI Definition" that lists four freedoms: to use the system for any purpose, to study how it works, to modify it and to share it. To make those possible, it requires sharing the preferred form for making modifications, including sufficiently detailed information about the data used for training, the complete source code used to train and run the system, and the model's parameters such as weights.
- **Open weights models:** these share the parameters so you can download and run them, but may not publish the data or training code, and usually come with their own license with usage conditions.
Under the OSI definition, weights are the learned parameters, and publishing them alone is not the whole preferred form for making modifications. So a model can be downloadable and usable but not open source in this sense.
## Why this matters to a small business
The difference lies in **what you are allowed to do**. Read each model's license to find out:
- Whether commercial use is allowed, and whether there are limits (for example on scale or field).
- Whether you may modify, further train and redistribute it.
- Whether it requires attribution or has other terms.
Do not rely on a model calling itself "open". Read the actual license.
## Where genuinely open models help
- **Data control:** running on your own infrastructure means content does not have to be sent out, which suits sensitive data.
- **No dependence on one provider:** you can change the model or where it runs, see [When should you switch AI agent platforms in your workflow?](khi-nao-nen-doi-nen-tang-ai-agent-trong-workflow-cua-ban.html).
- **Customization:** adjust the model for your narrow needs if the license allows.
- **Predictable cost at a steady high load,** because you do not pay per use.
- **Learning and experimenting:** you can try it free on your machine, see [Installing DeepSeek with Ollama: running AI models on a budget](cai-deepseek-voi-ollama-chay-mo-hinh-ai-theo-huong-tiet-kiem.html).
## The price you pay
- **Operations:** you handle installation, updates, security and incident handling.
- **Hardware:** a strong model needs a strong machine.
- **Quality:** a model you can run may be weaker than top services on complex work.
- **Responsibility:** you are responsible for safety, moderating output and compliance.
- **No official support** as with a commercial service.
## Self-host or use a service: how to choose
```
Sensitive data that must not leave your infrastructure?   -> Consider self-hosting
Small load, need high quality, few people to operate it?  -> Use a service
Large steady load, people with operations skills?         -> Self-hosting may be cheaper
Not sure?                                                 -> Try both on a few real tasks
```
Compare using your own tests, following the framework in [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html), with real costs including operating time.
## Advice for small businesses
1. Start by identifying which data is sensitive.
2. Read the license before choosing a model.
3. Try on your own machine or a cheap service before investing in infrastructure.
4. Calculate total cost of ownership, not just the model download fee.
5. Keep the ability to switch providers.
