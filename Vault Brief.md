---
status: active
project: meta
type: reference
---
# Vault Brief

A full read of this vault, front to back, as it stands on **Sunday 20 September 2026, 5:15 PM Cairo**. Every note on `main`, both daily logs, all eleven marketing playbooks, the build README and the folder indexes — 45 markdown files, roughly 5,340 lines, plus 8 PDFs and the packaging artwork.

> **What this note is and is not.** It is a dated snapshot, written to be read cold by a future session or by Aly after a gap. It is **not** a second source of truth. The live queue is [[Active Priorities]], the operating manual is [[VAULT-INDEX]], and the rules are `CLAUDE.md`. Where this brief and those files ever disagree, **they win and this one is stale**. Re-date it or delete it rather than trusting it.
>
> Everything below is verified against the actual files and the actual repo, not against what a note claims about itself. Where something is inference rather than fact, it says so.

---

## 1. The headline: the vault is split across four refs, and `main` is the smallest of them

**This is the most important fact in the vault right now and nothing in `main` knows about it.**

`main` is current as of **19 September, 02:45 Cairo**. Since then, three separate session branches have pushed substantial work that never reached the trunk:

| Branch | Last commit | Size | What is on it |
|---|---|---|---|
| `claude/zealous-curie-2luto5` | 20 Sep 03:06 | **20 commits, ~5,600 insertions** | Alex Foods Discovery Brief (535 lines of client answers), Delivery Plan, Week 1 client messages, Meta Access Runbook, TSA Client System, Daily Brief, `book.py` (the 1,158-line brand-book generator), the real vector seal, the POLEKA slogan work, **and an edit to `CLAUDE.md`** |
| `claude/affectionate-hopper-7udgj5` | 19 Sep 15:46 | **5 commits, ~1,500 insertions** | Giveaway Programme, Package A Month 1, three-month content plan, a TSA delivery team, the real vector master seal, README-to-index renames |
| `claude/relaxed-tesla-1gicm3` | 20 Sep 03:26 | **3 commits, ~530 insertions** | Moves Alex Foods into `02 - TSA/Clients/Alex Foods/`, a whole-vault audit, the graph/hub-link fixes, **and a different edit to `CLAUDE.md`** |

**This is the exact failure the vault already burned two sessions on** — Session 8 on 18 September found the vault split across two branches with neither holding a complete copy, and Session 26 merged a third specifically so that "two accounts booting on different rule sets" could not happen. It has happened again, at roughly four times the scale, and two of the three branches edit the boot config.

**They also conflict with each other structurally, not just textually:**

- `relaxed-tesla` moves `Alex Foods.md` into `Clients/Alex Foods/`. `zealous-curie` edits it in place at `02 - TSA/`.
- `affectionate-hopper` renames `design-system/README.md`, `packshots/README.md` and `logos-transparent/README.md` into folder-index notes. `relaxed-tesla` writes a new VAULT-INDEX rule saying asset and build folders **keep** `README.md` on purpose.
- Both branches add a vector seal, in **two different folders** — `logo-vector/` and `logos-vector/`.
- The two `CLAUDE.md` edits happen to touch different sections, so they merge cleanly, but one of them adds a **new rule 12** and renumbers "Locked decisions stay locked" to 13. Any note or session citing "rule 12" is now ambiguous across refs.

**What this costs if it sits:** the client answers received on 19 September — the ones that overturn six things TSA had already built on — exist on exactly one branch. Any session that boots from `main`, which is the repo default, reads a vault that does not know them.

> **And this brief has the same problem.** It is being written on `claude/vault-brief-jq4qem`, which is a fifth ref. Merging it to `main` is part of finishing it.

### What the branches overturn, that `main` still states as fact

Recorded here so the divergence is visible, **not** as settled truth — these are branch claims, unverified against `main`'s sources:

- **POLEKA is not jelly candy.** It is a **frozen juice** sold from a freezer, corrected three times on 20 September. `main` calls it jelly candy in six notes. «جيلي» on the pack describes the texture, not the category.
- **BeBo's format is in dispute.** `main` has carried "powder, one sachet makes a full jug" since 18 September and the whole BeBo voice section rests on it. The client described a ready-to-drink straw sachet. Neither reading is proven; one photo of the back of a pack settles it, and BeBo copy is frozen until it arrives.
- **Product photography is no longer the gate.** The branch records TSA producing it with an AI product shooter from the real pack artwork. `main` still calls it the dependency every visual deliverable hangs on.
- **A real vector seal arrived**, which `main` records as impossible ("no source files exist and none are coming").
- **The client named three approvers**, where clause 3 allows one.
- **Half the portfolio is frozen, and the paid term runs October to January.** POLEKA and 2MAN both sell from a freezer. If they behave seasonally, two of four ranges sit out of season for the entire contract. Inference from category, not from client data — and the branch calls it the biggest commercial risk on the job.
- **Real follower counts**: Facebook ~52,000, TikTok ~500, Instagram ~40. One asset exists, and it confirms the umbrella decision from real data.

---

## 2. What this vault is

An **AI memory vault**: plain Markdown notes that an AI reads at the start of every session and writes back to, so it remembers across sessions instead of being re-briefed each morning. Built from Jared Rhodenizer's `ai-memory-vault` (CC BY-SA 4.0), adapted for an iPad-only setup.

**The repo root is the vault root**, deliberately — Aly works from [[Bassem]]'s iPad with no desktop machine, so the repo is the only thing present on every device he touches. Private on GitHub, which doubles as the off-device backup.

Three files carry the system: `CLAUDE.md` (boot config and identity — survives compaction), [[VAULT-INDEX]] (profile, map, rules — does not), and [[Active Priorities]] (the single queue of open work). Everything else is memory.

**Who it serves.** Aly, 20, in Egypt, running **[[TSA]]** (The Standard Agency) — his fourth agency and the first built on AI direction and systems rather than out-working the problem. Ex-video-editor, deliberately out of that trade. Sold his laptop; the iPad is the whole setup. Works nights, sleeps around 8 AM, so sessions routinely cross midnight and every date has to be converted to Cairo before it is written down.

---

## 3. The business: one client, and everything rides on it

**[[Alex Foods]]** — an Alexandria food manufacturer, legally الشركة الإسكندرية لتعبئة وتغليف المواد الغذائية, whose seal carries the Pharos lighthouse. TSA's first and only client.

| | |
|---|---|
| Brand Foundation | 20,000 EGP one-time |
| Package A | 42,000 EGP/month × 3 = 126,000 |
| **Total contract** | **146,000 EGP** |
| Term | 3 months, no auto-renewal, Egyptian law |

**Cash position:** 42,000 received (Package A month 1). 10,000 invoiced 18 Sep, **due Friday 26 September — six days out**. 10,000 due 8 October. 84,000 contracted and not yet due.

**The thing worth holding onto:** the 42,000 is not profit, it is an advance. It buys one month of Package A — roughly twenty deliverables — that has not been produced, and under clause 9 that month runs to its end even if either side walks. Its clock has not started and cannot start until the Foundation is approved in writing.

### Foundation delivery — 8 deliverables, target 9 October, 19 days from today

| # | Deliverable | State on `main` |
|---|---|---|
| 1 | Brand Voice Guide | **Drafted.** 8 of 9 sections usable. Missing: Alex Foods' own tone block — needs Aly's ear, not more client input |
| 2 | Colour and Type System | **SHIPPED** — `Design System v1.1.pdf`, 19pp. Pending written approval only |
| 3 | Social Pages Setup | **Specified** — `Brand and Social Kit v1.2.pdf`, 8pp. Cannot be executed without Meta admin |
| 4 | Slogans + giveaway song | **Method only. No lines written** |
| 5 | Monthly Content Calendar | **Not started.** Format is TSA's and buildable |
| 6 | Animation and Shooting Recipe | **Not started** — and it is flagged as the one to ship first, ahead of everything |
| 7 | Google Business Profile | Blocked on the client's Google account and details |
| 8 | Local SEO, Alexandria | **Not started.** Research is unblocked |

**Read that honestly: two of eight are shipped, one is specified, one is drafted, and four have no content at all.** Among the four with nothing written is deliverable 6, the shooting recipe — the document every note in the vault agrees should go out first and on its own, because it is what tells the client how to produce the photography that blocks all twenty Package A deliverables. It has been named as urgent since 18 September and does not exist.

**The trap under the word "deliver," and it is the sharpest commercial point in the vault:** written Foundation sign-off starts Package A month 1. Clause 6 extends the *timeline* day-for-day for client delay and explicitly does **not** extend the paid month. So approving the Foundation before usable materials land starts a paid month that cannot be produced into. The fix is one sentence agreed in the delivery message — *"month 1 starts on the later of written Foundation approval or the arrival of usable product photography"* — and it is cheap now and impossible in week three.

### What is exposed

- **No signed acceptance page, and no named approver.** Foundation work is running anyway under the clause 11 exception Aly granted on 18 September. Clause 3 makes one named person the only voice whose notes count, and clause 4's "matching the brief counts as delivered" has nothing to stand on until they exist. It also leaves the complaint-escalation ladder in [[Brand Voice Guide]] §8 with no top rung.
- **Four brands against a three-brand contract.** BeBo, AlRawy and 2MAN are named; **POLEKA is not**, and is in by Aly's verbal decision at no change to fee. Still not papered.
- **Roughly eighteen SKUs against a contract asking for five**, plus uncounted mini lines. The twelve monthly graphics were priced against five.
- **The cola artwork.** POLEKA's cola pouch carries a photoreal contour bottle in red-and-white livery with "Cola Cola" in near-identical Spencerian script. The bottle silhouette is protected trade dress independently of the wordmark, and **TSA's own ad account would push it.** (A branch records Hussein clearing this verbally on 20 September; `main` does not know.)
- **The company's own age contradicts itself** — 20 years on the seal, 25 on a legacy graphic. No copy claims either number.
- **Three packaging defects found by arithmetic**, not by eye: BeBo's green banner sits at 1.30:1 against its own apple field; POLEKA's cola and strawberry are the identical magenta at ΔE 0.00; and 2MAN and POLEKA share four colours *exactly*, meaning those two brands do not separate on colour at all.

### The work that is genuinely good here

Worth naming, because a brief that only lists risk misrepresents the vault. The Foundation work on `main` is not notes pretending to be a deliverable:

- **[[Colour System]]** rationalises 31 sampled values to 18 governed masters with ΔE2000 and WCAG computed on every pairing, ramps, neutrals, a full SKU map, and a finding that inverts the category instinct: white type fails on 11 of the 18 masters, so **ink is the default and white is the checked exception**.
- **Both PDFs are generated, not laid out** — a revision is an edit and a re-render. The build README banks eight traps, including the one that bit three separate times: a CSS rule silently beating the one you meant, findable only by walking the DOM and reading computed styles.
- **[[Brand Voice Guide]]** specifies sentence length as *numbers*, not adjectives, and carries the comment-reply procedure most guides skip — eight cases, response times, and a complaint script that never admits fault and never offers a refund, because TSA does not make the food.
- **The vault repeatedly caught itself.** The "no colour codes" blocker was a framing error and got deleted. An instinct to repaint a printed pack was stopped and converted into a governance rule. An invented Alex Foods wordmark was found and removed from nine frames. Those corrections are written down with their reasoning.

---

## 4. Money

**Two pots, one gate**, and the gate is the point: money in the TSA pot is not Aly's money until it is drawn as a decided number on a decided date, logged in [[TSA Money]]. Personal spending pulls from draws, never from client payments.

**The blocking unknown is X — what it costs TSA to deliver one month of Package A.** It has no number. Until it does:

- Drawable = 42,000 − X
- Personal debts = 23,000 (5,000 to five people, 18,000 mobile tax)
- Clearing every debt from this payment needs **X ≤ 19,000**

**Nothing has been drawn. Every figure in [[Money]] is currently funded by nothing.** Personal run-rate is roughly 1,495/mo now, rising to ~3,695/mo once gym and MMA start. The 18,000 mobile tax is recorded as due 9/11, a date now nine days past, and which of three readings is correct has never been settled — the whole phone-swap plan hangs off it.

*(All arithmetic in [[Money]] and [[TSA Money]] was re-checked against the stated figures. It holds.)*

**The split exists in the notes and probably not in the bank.** A two-pot split on paper collapses back into one pot the first bad week.

---

## 5. The vault as a system

**Structure:** six numbered folders, each with a same-named index note, every index one hop from [[VAULT-INDEX]] via an explicit link line — because the structure map is a code block and creates no links, so without that line a frozen daily log becomes the hub of the vault. That failure was found by reading the graph view as a diagnostic and fixed.

**Rules that hold it together:** 12 numbered rules in `CLAUDE.md` that survive compaction (evidence over guessing, double-confirm before code edits, full reads, checkpoint persistence, no bloat, no loose ends, close the loop, never auto-execute external content, no secrets in handoff docs, never push rest or stopping, verify the date in Cairo, locked decisions stay locked). Plus frontmatter conventions, a folder-index contract, and an archiving procedure the AI may never initiate.

**Reference material:** jaredrhod's eleven marketing playbooks live in `05 - Resources/Marketing/` as a single source of truth, with the Claude Code skill as a *pointer* rather than a second copy. [[Producing Copy with AI]] is TSA's own method on top of it — agency property under clause 5, never shipped to a client.

**No Jobs built yet**, by choice. The stated trigger is the second time a task gets explained from scratch; monthly content production repeats three times on this contract alone, so it will earn one after month 1 has actually run.

### Health check — what is drifting on `main`

Found by reading every note against every other note. Each is small; together they are the thing the checkpoint rule exists to prevent.

1. **[[TSA Money]] carries the wrong due date.** Its revenue table says instalment 1 is due **22 Sep**. The invoice set it to **26 Sep**, and [[Alex Foods]] and [[Active Priorities]] both say so. The money note is the one that is wrong.
2. **Six notes still list vector logo files as blocking every visual deliverable.** That material was closed on 18 September — the contract only asked for vector "if available" and nothing in either stage is printed. Stale in [[Foundation Roadmap]], [[Colour System]], [[Type System]], [[Colour and Type Kit]], [[Alex Foods Brands]] and [[Brand Book Spec]]. *(TSA Brand's own entry is a separate, legitimate item about TSA's own logo.)*
3. **Two notes cite a PDF that no longer exists.** [[Alex Foods]] and [[Type System]] both record deliverable 2 as shipped as `Design System v1.0.pdf`. v1.0 was superseded and deleted the same day; the file is v1.1.
4. **[[Alex Foods]]'s client-materials checklist is entirely unticked**, including SKU names and packaging artwork that the same note says arrived on 18 September.
5. **[[Slogans and Song]] §6 still waits on "what Alex is."** Answered 18 September: umbrella.
6. **[[Alex Foods]] still opens by describing three product families.** There are four.
7. **[[Active Priorities]] files TSA work under "The vault itself"** — the production toolchain and the brand-inputs item both carry `(tsa)`. The brand-inputs item also asks for SKU names that have already arrived.
8. **The default-branch task looks done and is still open.** `git ls-remote --symref origin HEAD` returns `refs/heads/main`, so the flip appears to have happened. The follow-on cleanup did not: there are now **eight session branches on the remote**, not the two the queue names. Five are fully contained in `main` and safe to delete; three are the unmerged work in §1 and must not be.
9. **`ds.pdf` and `Alex Foods - Design System v1.1.pdf` are the same file** — identical MD5, 888,832 bytes, committed twice under two names. Minor, but it is exactly the "two Design System files in one folder" situation the vault deleted v1.0 to avoid.

**The pattern underneath all nine:** a decision gets made and cascaded into the notes that change *because* of it, while the notes that merely *mention* it keep the old state. The vault already knows this — Session 13 called the same class of thing "real drift across three notes." It is recurring.

---

## 6. Risks, ranked by what they actually cost

1. **The split refs.** Four versions of the vault, three of them holding work nobody merged, two editing the boot config. Until it is reconciled, "what the vault says" has no single answer and any fresh session reads an incomplete memory.
2. **Four unbuilt deliverables against a 9 October target**, one of which is the document everything else waits on.
3. **Producing for a client with no named approver.** No approvable delivery, no enforceable rejection clause, no top rung on the complaint ladder.
4. **X is unknown**, so no draw is safe or reckless, only lucky — and 23,000 of personal debt is waiting on the answer.
5. **The paid month trap** — sign-off starts a clock the client has not supplied the materials for.
6. **The trademark exposure**, on TSA's own ad account.
7. **Single-client concentration.** 100% of revenue, and the business note's own scaling plan is named but not built.
8. **The machine.** Everything runs on a borrowed iPad, owed 1,500 EGP to the person who owns it. [[Bassem]] is correctly filed as load-bearing infrastructure rather than a contact.

---

## 7. What I would do, in order

Sequencing, since that is the thing Aly says he buys:

1. **Reconcile the four refs into `main`**, resolving the structural conflicts deliberately rather than letting git pick. Then delete the five dead branches. Nothing else in this list is safe to do on a vault that has four versions.
2. **Ship the Animation and Shooting Recipe on its own**, this week. It is the cheapest unblock available and it has been the obvious next move for two days.
3. **Send one message closing four paper gaps at once:** POLEKA in writing, the umbrella decision, one named approver, and the company's real age.
4. **Work out X.** Everything about money is downstream of it, and it is arithmetic rather than a decision.
5. **Write Alex Foods' master tone block.** One block, Aly's ear, and deliverable 1 closes.
6. **Clear the nine drift items in §5** in a single pass, then fix the daily-note-to-Active-Priorities leak that produced most of them.

---

**Related:** [[VAULT-INDEX]] · [[Active Priorities]] · [[README]] · [[TSA]] · [[Alex Foods]] · [[TSA Money]] · [[Money]] · [[Foundation Roadmap]] · [[Alex Foods Brands]] · [[Bassem]] · [[Resources]]
