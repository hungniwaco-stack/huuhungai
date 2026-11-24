---
title: Evaluating AI agents through real tests: which criteria to look at
desc: A framework for evaluating AI agents with tests from your real work: choosing tasks, scoring criteria, measuring cost, stability, intervention and safety risks.
min: 7
---
QUICK: Do not choose an AI agent based on a demo video or a general leaderboard. Take 5 to 10 of your own real tasks, run each task several times, then score by fixed criteria: correct results, stability, cost, the amount of human intervention and dangerous behavior.
## Why demos and benchmarks are not enough
A demo is always selected to look good, and public benchmarks measure general problems, not your data, tools and workflow. An agent at the top of a leaderboard can still ruin your own work over a small detail such as file format or access permission. The most reliable test is one drawn from the work you actually need to do.
## Step 1: Choose a set of trial tasks
Choose 5 to 10 representative tasks, both easy and hard:
- A few simple, repetitive daily jobs (a basic control).
- A few multi-step jobs that need tools or reading many documents.
- One or two deliberately hard situations: missing data, conflicting requirements, unusual formats.
Write each task as a fixed description, so every agent is tried with the same prompt.
## Step 2: Define what counts as a "pass" before running
For each task, write the scoring criteria in advance. Do not decide after seeing the results, because that invites bias.
- **Pass or fail:** is the result correct and immediately usable.
- **A short scale** for parts that are a matter of impression such as writing style and completeness, with a clear description of each level.
- **Forbidden conditions:** things the agent must absolutely not do, such as editing files out of scope or sending data outside.
## Step 3: Run several times
AI models do not give identical results every time. One good run may be luck. Run each task a few times with each agent and look at the success rate instead of a single result.
## A suggested scorecard
Use a simple table for each agent:
```
Task   | Pass (runs/total) | Time | Estimated cost | Times a person fixed it | Violations
-------|-------------------|------|----------------|-------------------------|-----------
Task 1 |                   |      |                |                         |
Task 2 |                   |      |                |                         |
```
These columns answer five questions: is it correct, is it stable, is it fast, how much does it cost and is it safe.
## The criteria to look at
- **Accuracy:** are the results true and as requested, down to small details.
- **Stability:** for the same prompt, are runs consistent.
- **Real cost:** the total cost of the whole process, including retries, not just the price of one call.
- **Amount of human intervention:** how many times you had to fix, re-ask or stop it.
- **Auditability:** is there a log of the steps so you can trace back when there is an error.
- **Error handling:** when it meets something it cannot do, does it stop and report, or pretend it is done.
## Safety tests
Test a few risky situations separately:
- Have the agent read a page or document with a sentence inserted such as "ignore the previous request and do something else" to see whether it is led astray. This is the kind of prompt injection attack that an agent reading outside content easily meets.
- Hand over work that could lead to an irreversible action (delete, send, pay) and see whether it asks permission first.
- Check whether it goes beyond the data scope or folder you allowed.
Test in an isolated environment or with fake data, not on real data.
## Common mistakes
- Testing with only one nice task and concluding.
- Evaluating after seeing the results, which lets the criteria drift with emotion.
- Forgetting to count the cost of retries and the time you spend checking.
- Comparing agents with different prompts.
## Turn testing into a habit
Keep the task set and the scorecard. When a new agent or version arrives, you rerun the same set in a few hours instead of evaluating from scratch. This is also the basis for deciding whether to switch platforms, see [When should you switch AI agent platforms in your workflow?](khi-nao-nen-doi-nen-tang-ai-agent-trong-workflow-cua-ban.html).
