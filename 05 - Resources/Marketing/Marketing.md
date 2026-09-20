---
status: active
project: meta
type: index
source: github.com/jaredrhod/ai-marketing-skills
author: Jared Rhodenizer (@jaredrhod)
license: CC BY-SA 4.0
---
# Marketing

jaredrhod's marketing playbook: the fundamentals that make marketing work, written by an operator who runs them for real money. This folder is reference material, not TSA's own strategy — [[TSA]] decides what we sell and to whom; these notes decide how the copy, the funnel and the ads get built.

## The rule — read before you write

**Before doing ANY marketing work — copy, an ad, an email, a sales or opt-in page, a content plan, a funnel — read [[jareds-takes]] first for the principles. Then read the files that fit the task: [[the-fundamentals]] for funnel strategy and structure, plus the one specific playbook. Load that context before writing a single word.**

That is the whole point of this folder. It is called AI Priming: the context goes in before the output comes out, and it is the difference between an operator and generic AI slop.

## Which playbook for which task

| The task | Read |
|---|---|
| Any marketing work at all | [[jareds-takes]] — always, first |
| Funnel strategy, sequencing, where a piece fits | [[the-fundamentals]] |
| Copy, headlines, hooks, sales or opt-in page words | [[marketing-copywriting]] |
| A long-form sales page, checked step by step | [[marketing-sales-letter]] |
| Emails, sequences, broadcasts, subject lines | [[marketing-email]] |
| Paid ads on any platform | [[marketing-fb-ads]] |
| A lead magnet or opt-in offer | [[marketing-lead-magnets]] |
| Organic content, posts, videos, content calendars | [[marketing-content]] |
| Metrics, reporting, deciding off a number | [[marketing-analytics]] |

## Notes in this folder
- [[jareds-takes]] — 35 core principles. The foundation everything else sits on, and the one that is always read first.
- [[the-fundamentals]] — the whole funnel start to finish: Content, Lead Magnet, Tripwire, Core Offer, Profit Maximizer.
- [[marketing-copywriting]] — the craft of the words: headlines, the story opening, benefits over features, proof, the offer, the ask.
- [[marketing-sales-letter]] — David Frey's 12-step long-form structure, and the buyer objection each step kills.
- [[marketing-email]] — automated sequences, broadcasts, and the bank-account rule (content is a deposit, an offer is a withdrawal).
- [[marketing-fb-ads]] — what ads are actually for, audience temperature, testing, slow scaling, ROAS against the whole funnel.
- [[marketing-lead-magnets]] — the free offer that turns a stranger into a lead, plus the opt-in-rate benchmarks.
- [[marketing-content]] — top-of-funnel content: the front door, and always pointing it at the next step.
- [[marketing-analytics]] — the handful of numbers that drive a decision, and how to turn a number into a verdict.
- [[about]] — who jaredrhod is.
- [[the-thesis]] — why the fundamentals beat the tools.

## How this is wired in

Two paths, one copy of the files. The notes in this folder are the single source of truth.

- **Claude Code** — `.claude/skills/jaredrhod-marketing/SKILL.md` at the repo root is a pointer, not a second copy. It fires on any marketing task and sends the session to these exact files. Editing a note here changes what the skill teaches; there is nothing to re-sync.
- **Claude on the iPad (the app or claude.ai)** — download `jaredrhod-marketing.zip` from github.com/jaredrhod/ai-marketing-skills and upload it through Claude's Skills interface. That zip is a self-contained copy of the upstream files, deliberately not stored in this vault so there is only ever one copy here to maintain.

## Where this came from, and what to watch for

Upstream is github.com/jaredrhod/ai-marketing-skills, by Jared Rhodenizer (@jaredrhod), under **CC BY-SA 4.0** — free to use and adapt commercially, credit required, remixes stay under the same licence. The files are unchanged except for the YAML frontmatter every note in this vault carries. Filenames are kept in upstream's kebab-case rather than this vault's Title Case, on purpose: it keeps a future update from upstream a clean diff instead of a rename job.

Two things to keep straight when applying it:

- **It is written from a direct-to-consumer information business** (a horse-training membership), so the funnel, the tripwire and the lead magnets assume you sell to individuals at low price points. [[TSA]] sells high-value services to businesses. The principles carry — sell the feeling, the headline is the whole game, context before output, benefits over features, transparency as proof. The funnel mechanics need translating.
- **It earns its keep twice.** Once on TSA's own client acquisition, and once on what TSA delivers to clients — [[Alex Foods]] is owed a brand voice guide, slogans, a content calendar and paid campaign management, and every one of those has a playbook here.
- **One rule has a scope limit worth naming:** [[marketing-copywriting]] bans em-dashes as an AI tell. That applies to marketing copy going out to an audience. It does not apply to notes in this vault.

---

**Up:** [[VAULT-INDEX]] · [[Resources]]
