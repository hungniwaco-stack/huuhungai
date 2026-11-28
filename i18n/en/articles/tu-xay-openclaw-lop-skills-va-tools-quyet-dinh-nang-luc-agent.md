---
title: OpenClaw skills and tools: building agent capability under control
desc: Skills and tools decide an OpenClaw agent's capability: installing skills, SKILL.md structure, tool policy by profile, allow, deny and security warnings.
min: 8
---
QUICK: In OpenClaw, skills are folders with a `SKILL.md` that teach the agent to do one job, while tools are what the agent is allowed to call. You control agent capability with two things: choosing which skills to install, and setting the tool policy (`tools.profile`, `allow`, `deny`). Third-party skills are code you are letting the agent run, so treat them like software.
## How skills and tools differ
- **Tools** are the specific abilities the agent can call: reading and writing files, running commands, web search, memory, scheduled tasks...
- **Skills** are packages of instructions and resources (a folder) that the agent loads when needed to carry out a procedure, for example working with a service. A skill may require tools or command-line programs that are already installed.
Raising capability means adding the right skills and granting enough tools, but no more than needed.
## Managing skills from the command line
According to the `openclaw skills` documentation:
```
openclaw skills search "calendar"
openclaw skills install @owner/<slug>
openclaw skills install git:owner/repo
openclaw skills install ./path/to/skill --as custom-name
openclaw skills update --all
openclaw skills list
openclaw skills list --eligible
```
- By default it installs into the `skills/` folder of the workspace in use; `--global` installs into the shared skills folder; `--agent <id>` installs for a specific agent.
- Search, update and verification use ClawHub, OpenClaw's official skill registry. Publishing and maintenance use separate ClawHub tools.
- Installing from Git or a local folder needs a `SKILL.md` at the root, with a `description` in its front matter.
## The structure of a skill
A skill is a folder. A `SKILL.md` is required. The optional YAML header, for example using `name` and `description`; the name should match the folder name, made of lowercase letters, digits and hyphens, 1 to 64 characters long. A minimal skeleton per the documentation:
```
---
name: my-skill
description: Short summary of what this skill does.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - MY_API_KEY
      bins:
        - curl
    primaryEnv: MY_API_KEY
---
```
`requires.env` declares the environment variables that must be present, `requires.bins` the programs that must all be installed, and `requires.anyBins` that at least one of them is needed. Install methods can be declared (`brew`, `node`, `go`, `uv`). The documentation stresses that declarations must match what the code actually uses; a variable that is not declared but is referenced by the code may be flagged as a mismatch. Skills on ClawHub use the MIT-0 license, with a total bundle size of at most 50 MB.
To point to a file or script inside a skill, the documentation says to use `{baseDir}`: the agent resolves it to the skill's own folder, so you do not hard-code paths, for example `{baseDir}/scripts/run.sh`. Any ordinary files in the folder go along with the skill.
## Tool policy
The `tools` configuration decides what the agent can call, in order: the base profile, the provider-specific profile, then `allow` and `deny`.
- `tools.profile`: `minimal` (only session status and Gateway maintenance), `coding` (files, run, web, sessions, memory, cron, skills), `messaging` (messaging, conversations, subagents), `full` (no core filtering). Local onboarding sets `full` if you have not configured anything, so review it.
- **A global `deny` always wins**, even when the Docker sandbox is off. A group block beats even an explicit `allow`.
- `allow` and `alsoAllow` do not share one scope.
- It can be set differently by provider (`tools.byProvider`), by sender (`tools.toolsBySender`) and by agent (`agents.entries.*.tools`).
An example blocking all file writes (the documentation's JSON5 syntax):
```
{
  tools: { deny: ["write", "edit", "apply_patch"] },
}
```
## Important warnings from the documentation
- `write` and `apply_patch` are two separate tools: allowing `write` also turns on `apply_patch` for compatible models, but blocking `write` does not block `apply_patch`.
- When the sandbox is on, MCP and plugin tools must also be declared in `tools.sandbox.tools`, or they are filtered out even though the server has loaded; `openclaw doctor` detects this error.
- `toolsBySender` keys of the form `username:` or `name:` match properties that can be changed; prefer `id:` or `channel:`.
- `tools.codeMode.executor: "node"` is not security isolation; use `"quickjs"` for the hardened version.
## Staying safe with third-party skills
- Skills from a `skills-sh:` reference are currently **not scanned by ClawHub**, and this label persists through updates.
- If the install policy returns a warning result, OpenClaw shows the findings and asks you to type a confirmation; a non-interactive run stops, unless you add the flag that accepts warnings, but that flag approves every warning in the run.
- `--force` does not override a block result.
- Read `SKILL.md` and every script before installing. Limit a skill to the agent that needs it with `--agent`.
## Suggested workflow
1. Start with a narrow tool profile (`messaging` or `coding`) instead of `full`.
2. Add skills one at a time, checking with `openclaw skills list --eligible`.
3. Block explicitly what is not needed (for example the browser, file writes) with `deny`.
4. Run `openclaw doctor` and `openclaw security audit` after every big change, see [An OpenClaw learning path: how to keep up with new AI agent tools](lo-trinh-hoc-openclaw-cach-theo-kip-cong-cu-ai-agent-moi.html).
5. Periodically review installed skills and remove those not used.
