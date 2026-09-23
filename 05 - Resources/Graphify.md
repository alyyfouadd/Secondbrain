---
status: active
project: meta
type: reference
source: github.com/Graphify-Labs/graphify
---
# Graphify

**What it is:** an open-source tool (Apache 2.0, free) that turns a folder into a knowledge graph — every note, the `[[wikilinks]]` between them, the generator code, PDFs and images — so a session can **query the graph instead of reading files one by one.** Installed 23 September 2026 at version 0.9.66.

**Who it is for:** mostly Jarvis. Obsidian already draws the link graph for Aly. What graphify adds is a graph an AI session can *ask* — "what connects the POLEKA line to the brand book?" — plus relationships it infers between notes that do not link to each other.

## How to use it

Type `/graphify .` in a Claude Code session on this repo. That:

1. installs the `graphifyy` Python package into the container if it is missing (cloud containers start fresh, so expect this on the first run of every session),
2. reads the code for free, locally, with no model,
3. reads the notes and PDFs with the session's own model — **costs tokens, not money; no API key is needed or asked for,**
4. writes `graphify-out/` at the repo root: `graph.html`, `GRAPH_REPORT.md`, `graph.json`.

After that, `/graphify query "<question>"`, `/graphify path "A" "B"` and `/graphify explain "X"` answer from the graph. `/graphify . --update` re-reads only what changed.

**To see the graph on the iPad:** ask Jarvis to publish `graph.html` as a private page and open the link.

## What was installed, and what was deliberately left out

**Installed:** the skill only, at `.claude/skills/graphify/` (`SKILL.md`, eight files in `references/`, a version stamp). It was produced by `graphify install --project` in a scratch folder and copied across, so nothing the installer writes outside that folder ever touched the vault.

**Left out, on purpose:**

- **The PreToolUse hooks** (`.claude/settings.json`). They run the `graphify` command before every Read, Grep, Glob and Bash call. A fresh cloud container does not have that command installed, so every file read would hit a failing hook.
- **The `.claude/CLAUDE.md` and root `CLAUDE.md` sections** that tell the assistant to consult the graph first. The boot config is the one file that decides how Jarvis works; a third-party tool does not write into it.
- **The post-commit hook** (`graphify hook install`). Same missing-command problem, and it rebuilds on code changes only, which is the smaller half of this vault.
- **The repository itself.** 25 MB of source, and `vault-check` walks every `.py` in the tree.

**`graphify-out/` is gitignored, and `vault-check` skips it in every check.** It rebuilds in minutes, goes stale the moment a note changes, and its report has no frontmatter — without the skip, the checker (which walks the disk, not git) failed on it as an orphan note.

## Traps

- **The PyPI package is `graphifyy`, double y.** Other `graphify*` packages on PyPI are not affiliated.
- **The skill's trigger is broad.** Its description claims *any* question about the project's content. Only once a `graphify-out/graph.json` exists does it start routing questions through the graph; in a fresh session there is none, so normal vault reads are unaffected.
- **It will print a Gemini-key tip.** Ignore it. Without a key the session does the reading itself, which is the intended setup here.

---

**Up:** [[Resources]] · [[VAULT-INDEX]]
