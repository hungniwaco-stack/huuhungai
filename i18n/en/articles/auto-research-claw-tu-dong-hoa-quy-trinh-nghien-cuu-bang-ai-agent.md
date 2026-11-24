---
title: Auto Research Claw: automating the research workflow with an AI agent
desc: AutoResearchClaw (aiming-lab) turns a topic into a draft paper through 23 stages: install, configuration, human-approval modes, outputs and the limits to know.
min: 8
---
QUICK: AutoResearchClaw (repo `aiming-lab/AutoResearchClaw`, MIT license) is an automated research workflow: from a topic to a draft paper, experiment code, references and charts across 23 stages. It runs fully automatically or with a reviewer at checkpoints. The README states neither cost nor run time, and the results should be treated only as drafts that need verification.
## What this tool is
According to the README, AutoResearchClaw is an automated workflow that turns a research topic into a draft paper, LaTeX, BibTeX, experiment code and charts. It is compatible with OpenClaw (you give OpenClaw the repo address and ask it to research a topic), and also runs standalone from the command line or through an ACP-compatible agent. It is a project outside OpenClaw; there are many forks and copies with the same README, so use the original `aiming-lab` repo.
## Requirements
- Python 3.11 or later.
- A language model API key, or an ACP-compatible agent CLI that handles its own authentication (such as `claude`, `codex`, `gemini`).
- The `researchclaw setup` command checks Docker and LaTeX. Experiments can run on GPU, MPS or CPU, detected automatically.
## Install and run (per the README)
```
git clone https://github.com/aiming-lab/AutoResearchClaw.git
cd AutoResearchClaw
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
researchclaw setup
researchclaw init
export OPENAI_API_KEY="sk-..."
researchclaw run --config config.arc.yaml --topic "Your research idea" --auto-approve
```
The `config.arc.yaml` configuration file is created by `researchclaw init` and at minimum contains `llm.base_url`, `llm.api_key_env`, `llm.primary_model`, `llm.fallback_models` and `experiment.mode`. There are four experiment modes: `simulated`, `sandbox`, `docker`, `ssh_remote`, and the publication targets `neurips_2025`, `iclr_2026` or `icml_2026`. There is an option `cost_budget_usd` with warnings at 50%, 80% and 100% (set 0 for no limit) and a time limit per experiment (default 300 seconds).
## The 23-stage, 8-phase workflow
- **A. Scoping:** decompose the topic.
- **B. Literature:** search, collect, screen and extract knowledge from OpenAlex, Semantic Scholar and arXiv.
- **C. Synthesis:** synthesize and generate hypotheses.
- **D. Design:** design experiments, generate code, plan resources.
- **E. Execution:** run experiments and refine iteratively.
- **F. Analysis:** analyze results and decide PROCEED, REFINE or PIVOT.
- **G. Writing:** outline, draft, peer review, revision.
- **H. Finalization:** quality gate, archiving, publishing, citation verification.
Stages 5, 9 and 20 are approval gates: the pipeline pauses and waits unless `--auto-approve` is used; if rejected it rolls back.
## Human-in-the-loop modes
The README lists `full-auto`, `gate-only` (pauses at stages 5, 9, 20), `checkpoint` (pauses at the boundary of each phase), `co-pilot` (deep collaboration at key stages), `step-by-step` (pauses after every stage), `express` (the three most important gates) and `custom` (a per-stage policy). The page says "6 modes" but the table lists seven. This intervention system is off by default, and there are commands `attach`, `status`, `approve`, `reject` and `guide`. For serious work, use an approval mode instead of `--auto-approve`.
## Outputs
The folder `artifacts/rc-<time>-<id>/deliverables/` contains the draft (`paper_draft.md`, `paper.tex`), `references.bib`, `verification_report.json` (citation verification), experiment code and results, charts, `reviews.md` (multi-agent peer review) and the lessons from each run.
## Safeguards the project describes
Citation verification through arXiv, CrossRef and DataCite with model-scored relevance, removing references that cannot be verified; an anti-fabrication mechanism that cleans up unverified numbers; a warning flag for unsupported citations; experiments run in a sandbox with syntax-checked code; optional masking of sensitive logs. The README has no limitations section and says the project is looking for people to test it.
## Using it responsibly
- This is a **drafting** tool. Every conclusion, figure and citation must be read and rechecked by a person with expertise before you submit or publish.
- State the use of an automated tool as required by wherever you submit.
- Set `cost_budget_usd` before running because the README does not state costs; run experiments in Docker or a sandbox.
- Start with an approval mode and a small topic.
To use it with OpenClaw, install and set up OpenClaw first following [Installing the OpenClaw Desktop App: how to start with a clean-interface AI agent](cai-openclaw-desktop-app-cach-bat-dau-voi-ai-agent-giao-dien-sach.html), and keep tool permissions narrow following [OpenClaw skills and tools: building agent capability under control](tu-xay-openclaw-lop-skills-va-tools-quyet-dinh-nang-luc-agent.html).
