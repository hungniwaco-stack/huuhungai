---
title: Sonnet for business: which workflow should get an AI model first?
desc: Which workflow to put Claude Sonnet on first in a business: criteria for choosing work, choosing between Sonnet, Haiku and Opus, and measuring results.
min: 7
---
QUICK: Start with a workflow that repeats often, has low risk, is easy to check and has data ready. According to Anthropic, Sonnet is the model that balances speed and intelligence, Haiku suits high-volume work that needs fast replies, and Opus suits long, complex work. Choose the model per task and measure with your own tests.
## How the Claude models differ
According to Anthropic's model overview page, the current model line includes Fable, Opus, Sonnet and Haiku, positioned as follows:
- **Sonnet:** "the best combination of speed and intelligence", with fast latency.
- **Haiku:** for high-volume tasks that need fast replies such as classification, extraction and routing, with the fastest latency.
- **Opus:** for agentic coding and long-running knowledge work.
- **Fable:** for demanding reasoning and long-running agentic work.
The current models all support text and image input, many languages and tool use, with a 1 million token context window. Prices and model names change, so see Anthropic's official pricing and model pages instead of relying on this article.
## Criteria for the first workflow
A good workflow to start with usually has:
- **Frequent repetition:** enough volume to see the effect.
- **Low risk:** one mistake does not cause big consequences, and a person reviews the result.
- **Easy-to-check results:** you can quickly tell right from wrong.
- **Available, clean data:** no months of preparation.
- **Measurable value:** how much time saved or how many errors reduced.
Avoid starting with work that has large legal or financial consequences, or work where nobody can check the result.
## Examples of workflows suited to try first
- **Summarizing** documents, meeting minutes and long emails.
- **Classifying and routing** customer requests by topic and urgency.
- **Drafting** replies, product descriptions or reports for a person to review.
- **Extracting** structured information from text (invoices, contracts, forms), with a checking step.
- **Supporting internal lookup** over the company's documents.
Each of these has a person in the loop reviewing results in the early phase.
## Choosing a model per task
You do not need to use one model for everything:
- Simple, high-volume work: try a smaller, faster model first.
- Work that needs a balance of quality and speed: Sonnet is usually a reasonable starting point.
- Hard, multi-step work or work that needs deep reasoning: try a stronger model for those tasks only.
Start from the balanced model, measure results, then try stepping down for simple work to save money or stepping up for hard work.
## How to deploy safely
1. **Define what counts as passing** before running, see [Evaluating AI agents through real tests: which criteria to look at](danh-gia-ai-agent-qua-bai-test-thuc-te-nhin-vao-tieu-chi-nao.html).
2. **Run a trial with a small group** using real data, with a person reviewing every result.
3. **Measure:** accuracy, time saved, rework rate, cost.
4. **Expand gradually** when the numbers are good, keeping the review step for the high-risk parts.
5. **Review periodically** because models and needs both change.
## Data and security
Before putting company data into any AI service, decide which kinds of data are allowed, read the provider's data policy and limit access to exactly what is needed. Do not put in customers' personal data without a lawful basis; see also the notes in [AI Lead Generation Agent: automating the sales pipeline](ai-lead-generation-agent-tu-dong-hoa-pipeline-ban-hang.html).
## Common mistakes
- Choosing a task that is too big or too vague to start with.
- Having no measurement criteria, so not knowing whether it works.
- Removing the reviewer too early.
- Choosing a model by reputation instead of your own tests.
