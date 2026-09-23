---
status: active
project: meta
type: plan
---
# Vault Rebuild Plan

How to stand this vault up **the right way** — same system, same information, organised so it stops drifting. Written 20 September 2026 off a full read of every note, recorded in [[Vault Brief]].

> **STATUS: APPROVED AND MOSTLY EXECUTED, 20 September 2026.** Aly approved the route; steps 0 to 4 and 7 are done in the same session.
>
> | Step | State |
> |---|---|
> | 0 · Merge the four refs | **DONE.** All three branches merged into one trunk, conflicts resolved by combining rather than picking |
> | 1 · Freeze and verify | **DONE.** No conflict markers, every wikilink resolves, every file from every ref accounted for |
> | 2 · Build the target structure | **DONE.** `Clients/Alex Foods/` and `Jobs/` exist, both indexed and on the hub line |
> | 3 · Move the files | **DONE.** Client work relocated; the generators' relative paths verified after the move |
> | 4 · Extract the registers | **DONE.** [[Delivery Register]] and [[Decisions]] built |
> | 5 · Rewrite the notes to §4's conventions | **NOT DONE — this is the remaining work.** Roughly forty notes, and rushing it is worse than leaving it |
> | 6 · Rebuild Active Priorities as a thin queue | **NOT DONE.** Waits on step 5 |
> | 7 · Write the conventions into the boot config | **DONE.** Rules 14 to 17 in `CLAUDE.md` |
> | 8 · Verify | **DONE for what shipped**; step 5's verification comes with step 5 |
>
> **What is left is the careful part, and it is deliberately not rushed.** §7's cost note still applies: forty notes rewritten badly is worse than forty notes left honest and untidy, against a Foundation due 9 October.

---

## 1. The diagnosis, because the folders are not the problem

**The structure of this vault is already right.** Six numbered folders, one same-named index per folder, every index one hop from the root, boot config split from the operating manual, one copy of the marketing playbook with a pointer skill at it, daily notes append-only. That is the jaredrhod system implemented properly and **none of it should be thrown away.**

What actually went wrong is four things, and not one of them is a folder:

### 1.1 A fact lives in six notes instead of one

Measured on `main` today:

- **Vector logo status** is stated in **6 notes.** It was closed on 18 September. Six notes still call it a blocker.
- **POLEKA's product category** is stated in **6 notes.** A branch says all six are wrong.
- **Deliverable 2's shipped filename** is stated in **3 notes**, two of which name a PDF that has been deleted.

One decision therefore needs six edits. Five get made, one rots, and the vault now disagrees with itself. **Every drift item in [[Vault Brief]] §5 is this one cause wearing different clothes.**

### 1.2 Notes carry their own argument history inline

Read [[Alex Foods Brands]] or [[Colour System]] §2 cold and you meet *"Superseded 18 Sep"*, *"Retired 18 September"*, *"the rule the umbrella model retires"*, and blockquotes correcting the paragraph above them. [[Brand Voice Guide]] §2 was literally stating the old model in its body and correcting itself underneath until Session 27 caught it.

**The reasoning is genuinely valuable and should be kept.** The mistake is keeping it *in the body*, where a future session reads the wrong model first and the correction second. A governance document the client may read should never contain an argument with itself.

### 1.3 Status lives in prose, spread across eight notes

"Drafted." "Shipped, pending approval." "Spec, execution pending client access." All true, all written in sentences, in different notes, in different words. **Nowhere can you read the state of eight deliverables in one glance** — which is exactly why [[Vault Brief]] had to be written to find out that four of them have no content at all.

### 1.4 The vault splits across git refs

Four live versions as of today. This one is a workflow problem rather than an organisation problem, but it multiplies all three above: a fix landed on one ref is drift on the other three.

---

## 2. The route: rebuild in place, not in a new repo

**Recommendation: do this as a deliberate reorganisation pass on `main`, in this repo. Do not start a new one.**

| | Rebuild in place | Brand-new repo |
|---|---|---|
| The actual work — rewriting notes to the new conventions | **Identical.** This is 90% of the job either way | Identical |
| Git history — the only complete record of how each decision was reached | **Kept** | **Lost** |
| The three branches of unmerged work | Merged in as step 0 | Have to be merged somewhere first anyway, then copied across |
| iPad plumbing — Working Copy clone, Obsidian folder sync, git identity, default branch | **Untouched** | **All of it again** |
| Cost | Free | Free |

**There is no upside to a new repo and three real downsides.** Moving a note inside the repo does not break `[[links]]` — Obsidian resolves by name, not path — so every reorganisation move below is safe, which is precisely what makes the in-place route cheap.

**The one case where a fresh repo is right:** if you want a clean, empty **template** vault to reuse on a second business or hand to a client. That is a different goal and a separate job — build it *after* this one, by stripping the finished vault down to its skeleton.

> **Step 0 is not optional: merge the three branches into `main` first.** Reorganising `main` today means carefully re-homing a vault that is missing the client's 19 September answers, the vector seal, the giveaway programme and the month-1 plan — and then doing the whole job again when those land. **Merge first, reorganise once.**

---

## 3. The target shape

```
00 - Inbox/
01 - Daily Notes/
    09 - September 2026/
02 - TSA/
    TSA.md                        <- agency index
    TSA Money.md
    TSA Brand/                    <- the agency's own identity (unchanged)
    Clients/
        Clients.md
        Alex Foods/
            Alex Foods.md         <- contract + doubles as this folder's index
            Discovery Brief.md    <- everything the CLIENT has told us
            Delivery Register.md  <- every deliverable, one row, one status
            Decisions.md          <- every decision, dated, with its reason
            Brand/                <- the brand system notes
            assets/               <- packshots, logos, mockups  (README.md)
            build/                <- the generators              (README.md)
    Jobs/
        Jobs.md                   <- one note per recurring job
03 - Personal/
04 - Archive/
05 - Resources/
    Marketing/
Active Priorities.md
VAULT-INDEX.md
CLAUDE.md
```

**What changed, and why each one earns its place:**

- **`Clients/<Client>/`** — client work stops sitting flat in `02 - TSA/`. The client note doubles as the folder index, because a client has exactly one master note and splitting "map of this folder" from "what they bought" makes two thin notes where one full one belongs.
- **`Discovery Brief.md`** — one note owning everything the client has actually said, tagged `[CONFIRMED]` / `[OBSERVED]` / `[ASSUMED]` / `[MISSING]` / `[CONFLICT]`. Nothing ships off a `[CONFLICT]`. *(This already exists on a branch and is the single best thing in the unmerged work.)*
- **`Delivery Register.md`** — one row per deliverable: number, name, status, what it is blocked on, where the artifact is. **Replaces status-in-prose across eight notes.** Reading the state of the contract becomes one glance instead of an afternoon.
- **`Decisions.md`** — dated, one row each: what was decided, by whom, on what evidence, what it overturned. **This is the piece the vault has never had**, and it is the fix for §1.2: the reasoning comes out of the body of ten reference notes and lands in one place that is built to hold it. It is also clause 4 armour — the rejection rule leans on the approved guide matching what the client actually said, and right now that trail is scattered across two daily logs and a dozen blockquotes.
- **`assets/` and `build/`** — artwork and generators are not notes. They take a `README.md` and stay out of the graph.
- **`Jobs/`** — already planned in [[Resources]], still empty. It gets built after Alex Foods month 1 has actually run, so the runbook describes what happened rather than what was imagined.

**What does NOT change:** the numbered folders, the index-per-folder rule, the root-index hub line, the `CLAUDE.md` / [[VAULT-INDEX]] split, the marketing folder and its pointer skill, [[Active Priorities]] as the single queue, daily notes append-only in month subfolders. All of it works. Leave it alone.

---

## 4. The four conventions that actually stop the drift

**These matter more than the folders. The folders are an afternoon; these are the thing that keeps it true in November.**

### 4.1 One fact, one owner

Every fact has exactly **one** note that owns it. Every other note that needs it **links, and never restates it.**

The client note opens with an owners table — colour is owned by [[Colour System]], voice by [[Brand Voice Guide]], deliverable status by the Delivery Register, what the client said by the Discovery Brief — and the rule is absolute: **if you are about to type a fact into a note that does not own it, type a link instead.**

*Test it works:* changing one fact should require editing exactly one note. Today it takes six.

### 4.2 Current state on top, history below the line

A note's body describes **only what is true now.** Superseded models, retired rules and the reasoning that overturned them move to a `## How we got here` section at the foot of the note, or into `Decisions.md`.

**No blockquote in a body ever corrects the paragraph above it.** If a correction is needed, rewrite the paragraph and log the change at the bottom.

### 4.3 Status lives in a register row, never in prose

If a thing has a state — a deliverable, a client material, an open question, an invoice — it gets a row in a register and **no note describes its status in a sentence.** Notes describe *what a thing is*. Registers describe *where it has got to*.

### 4.4 One ref, always

Work on `main`. A session branch gets merged and deleted at the end of the session that created it, not "later." **A checkpoint is not saved until it is on the trunk** — the vault already says this and it has been broken three times, so it goes in the boot config as a numbered rule rather than a bullet in a habits list.

---

## 5. The order of work

Sequenced by dependency. Each step is safe to stop after.

0. **Merge the three branches into `main`** and resolve their structural conflicts deliberately — the `Alex Foods.md` move, the README-versus-index naming, the two vector-seal folders, the two `CLAUDE.md` edits. Delete the five dead branches. **Nothing below is safe on a vault that has four versions.**
1. **Freeze and verify.** One ref, clean tree, every wikilink resolving, a note of what exists before anything moves.
2. **Build the empty target structure** — folders and their index notes, the map in [[VAULT-INDEX]] and the one-hop hub line updated in the same pass.
3. **Move the files.** `git mv` keeps history, and moving does not break `[[links]]`. **Prefer moves and avoid renames** — a rename outside Obsidian breaks every link pointing at the note, and if one is genuinely needed, every `[[old name]]` gets fixed by hand in the same pass.
4. **Extract the three registers** — Delivery, Decisions, and the open-items table — out of the prose that currently holds them across eight notes.
5. **Rewrite the notes to §4's conventions**, one at a time: strip restated facts down to links, lift the inline history out of the bodies, delete the status sentences the registers now own. **This is the real work and it is most of the time budget.**
6. **Rebuild [[Active Priorities]]** as a thin queue pointing at the registers, instead of 82 lines that restate them.
7. **Write the conventions into `CLAUDE.md` and [[VAULT-INDEX]]**, so the next session inherits them instead of rediscovering them.
8. **Verify, and this is the step that gets skipped:** every wikilink resolves, every folder has an index, every index is on the hub line, no fact is stated in two notes, the graph shows the client note as the biggest node and the daily logs as leaves.

---

## 6. How to know it worked

Measurable, so it is not a matter of opinion in a month:

| Test | Today | After |
|---|---|---|
| Notes that must be edited to change one fact | **6** | **1** |
| Notes whose body describes a superseded model | **4+** | **0** |
| Places you must read to learn the state of 8 deliverables | **8** | **1** |
| Live versions of the vault | **4** | **1** |
| Drift items found by a full read | **9** | **0** |

---

## 7. The honest cost

**Steps 0 to 4 are a session's work.** Step 5 is not — it is a careful rewrite of roughly forty notes, and rushing it produces a tidy vault full of subtly wrong content, which is worse than the untidy one that is right.

**It costs nothing in money.** It costs a working session that does not ship a client deliverable, against a Foundation due 9 October with four deliverables carrying no content at all.

> **So the real question is not how, it is when.** Doing this before the Foundation ships buys a clean vault and spends days the contract needs. Doing it after month 1 ships buys the opposite. **Step 0 alone — merging the four refs — is the exception: that is urgent regardless, because every day it waits, more work lands on the wrong ref.**

---

## 8. Step 5, measured — 24 September 2026

**"Roughly forty notes" was an estimate and it was never checked. Measured against the vault: it is twenty-nine notes, not forty**, and the work inside them is very unevenly spread. Four notes carry a third of it. **That changes step 5 from a week-shaped blob into something that can be done in pieces**, which is the only reason it is written down here rather than left as a line in [[Active Priorities]].

### What was counted

- **Inline history** — a blockquote in a note's *body* carrying correction language (superseded, retired, was wrong, used to read, reverted, withdrawn, corrected). Rule 15 puts these in a `## How we got here` foot section or in [[Decisions]]. **54 of them across the vault.**
- **Status in prose** — a sentence describing what state a thing is in, outside the register that owns it. Rule 16 puts these in a register row. **93 lines matched**, and this number is the soft one: the pattern also catches contract language (*"counts as delivered"*) and specs (*"delivered ready to publish"*), which are not violations. **Spot-checked two notes: roughly half the matches are genuine.** Treat 93 as the search list, not the defect count.

Daily notes, [[Decisions]], [[Delivery Register]] and the `Marketing/` playbook are excluded by design — a log is history by construction, the registers *own* history and status, and the playbook is third-party.

### The worklist, heaviest first

| Note | Inline history | Prose status | Has `How we got here` |
|---|---|---|---|
| [[Brand Voice Guide]] | 12 | 1 | — |
| [[Brand and Social Kit]] | 8 | 3 | — |
| [[Slogans and Song]] | 8 | 2 | — |
| [[Alex Foods Brands]] | 7 | 7 | — |
| [[Alex Foods]] | 0 | 13 | — |
| [[Foundation Roadmap]] | 2 | 11 | — |
| [[Alex Foods Week 1 Messages]] | 3 | 3 | — |
| [[Package A Month 1]] | 0 | 7 | — |
| [[Alex Foods Discovery Brief]] | 1 | 4 | — |
| [[Brand Book Spec]] | 1 | 4 | — |
| [[Giveaway Programme]] | 1 | 4 | — |
| [[Colour System]] · [[Content Plan]] · [[Type System]] · [[El Ghaly Motors Pitch]] · [[Month 1 Asset Brief]] | 1–2 each | 0–2 each | — |
| Eleven more with a single hit each | 0–1 | 1–2 | — |

**Only three notes in the whole vault already comply**: [[Local SEO — Alexandria]], [[Alex Foods Marketing Plan]] and [[Active Priorities]] have a `## How we got here` section. Every other note keeps its argument in its body.

### The two highest-value fixes, and they are not the heaviest notes

1. **[[Alex Foods]] and [[Foundation Roadmap]] each carry a complete deliverable-by-deliverable status list.** That is three copies of the same eight statuses — theirs plus [[Delivery Register]], the note built to own them. **It has already drifted once:** row 7 of the register still read *"unblocking 21 Sep"* on 24 September, three days stale, because the 23 September pass corrected row 3 and missed the identical phrase one row down. Stripping both lists to a link at the register is the single change that removes the most future drift, and neither note loses anything a reader needs.
2. **[[Brand Voice Guide]] is the worst single note at twelve inline corrections** — and it is a **client-facing** governance document. A guide that argues with itself in front of the client is the failure §1.2 describes, sitting in the one place it costs most.

### What this does not change

**The gate still holds: after the Foundation ships, not before.** §7's cost argument is unaffected by knowing the number — twenty-nine notes rewritten badly is still worse than twenty-nine left honest and untidy. What the measurement buys is the ability to take the top two rows in an hour instead of booking a week, and **fix 1 above is worth doing on its own the moment the Foundation is out**, because it is the one that keeps re-breaking.
