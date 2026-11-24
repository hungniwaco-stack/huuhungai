---
title: Google Simula and mechanism design: understanding synthetic data for AI
desc: Google Research's Simula creates synthetic data by designing the whole dataset: the steps, published results, limits and what AI practitioners should take away.
min: 7
---
QUICK: Simula is a framework published by Google Research for creating synthetic data in a "reasoning first" way: use a reasoning model to build a taxonomy of the domain, generate many scenarios from it, raise the difficulty of a portion, then use two critic models to check quality. The authors themselves say there is no universal recipe, and that data quality relates to results in a very context-specific way.
## The problem Simula solves
According to Google Research's blog post, specialized AI needs data that is rare, expensive to make by hand, or privacy-sensitive. Existing ways of creating synthetic data usually rely on hand-written prompts, evolutionary algorithms or seed data, which limits scalability, explainability and controllability. They also usually work one sample at a time instead of designing a whole dataset. The paper is "Reasoning-Driven Synthetic Data Generation and Evaluation" (Davidson et al.), accepted at TMLR 2026, with the first version submitted on Mar 31, 2026 (arXiv:2603.29791).
## What "mechanism design" means here
The authors' view is to treat data generation as **design at the level of the whole dataset**: you specify the desired properties (broad coverage, local diversity, difficulty, quality) and control them separately, instead of hoping each random sample adds up to a good dataset. This is the post's way of putting it; the blog post does not go deep into mechanism design theory in the economics sense, and some secondary articles exaggerate this aspect.
## The method, four steps
1. **Global diversification:** a reasoning model builds a hierarchical taxonomy of the target domain with a "propose then refine" loop, with a critic model merging and filtering subcategories. This taxonomy is the scaffold for sampling, covering the long tail too.
2. **Local diversification:** "meta-prompts" are created from the taxonomy nodes, and many different variants are generated from each scenario to avoid mode collapse.
3. **Complexification:** a configurable share of the meta-prompts is refined to be more complex or harder.
4. **Quality checking:** a "dual critic" loop independently assesses whether the answer is correct, helping reduce sycophancy and ensure label quality.
This approach **needs no human seed data** and, according to the authors, will get better as the reasoning ability of the base model improves.
## Published results
According to the blog post: the teacher is Gemini 2.5 Flash and the student is Gemma-3 4B, on five datasets: CTI-MCQ and CTI-RCM (cybersecurity), LEXam (legal reasoning), GSM8k (grade-school math) and Global MMLU (multilingual knowledge). Datasets reached up to 512,000 points per domain.
- The full system consistently beat simpler baseline methods.
- High complexity gave a 10% accuracy gain on GSM8k but reduced performance on LEXam, where the teacher model is weaker.
- Simula reached lower loss with fewer samples, but the page gives no specific numbers.
- Two new metrics: Taxonomic Coverage and Calibrated Complexity Scoring, used in batch comparisons by a language model to assign Elo-style scores.
## Where it is used
The blog post says Simula has supported the Gemma family of models (ShieldGemma, FunctionGemma, MedGemma), is the main synthetic data foundation for Gemini's safety classifiers, call scam detection on Android and spam filtering in Google Messages, along with applied research on enterprise security and teaching AI to read maps. This is Google's own description, not an independent assessment.
## Limits the authors state
- There is no "silver bullet" or fixed recipe; the relationship between data quality and downstream task performance is "very specific".
- Data must be tailored to the abilities of the model that uses it, as the LEXam results show.
- The evaluation uses a distillation setup for repeatability; the authors say the lessons extend beyond it, but the page does not test that.
## What AI practitioners should take away
- **Design the dataset, do not just generate samples.** Write down which situations you need to cover, how difficulty is distributed, and measure that.
- **Do not raise difficulty blindly:** high difficulty can hurt if the data-creating model is weak in that domain.
- **Have an independent critic** to check labels instead of trusting one model.
- **Verify on the final task**, because good on the data does not mean good for your model.
- Synthetic data helps when data is scarce or sensitive, but does not replace evaluation with real data. For private data, you also need to weigh the risk of information leaking through the data-generating model.
A practical view on when to use small models and your own data, see [Where open source AI is winning: lessons for small businesses](open-source-ai-dang-thang-o-dau-bai-hoc-cho-doanh-nghiep-nho.html).
