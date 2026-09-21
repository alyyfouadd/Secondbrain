---
status: active
project: meta
type: reference
---
# Vault Brief

A full read of this vault, front to back. **Written 20 September 2026 at 5:15 PM Cairo against `main`; rewritten the same evening after the four refs were merged.**

> **What this note is and is not.** It is a dated snapshot, written to be read cold by a future session or by Aly after a gap. It is **not** a second source of truth. The live queue is [[Active Priorities]], delivery state is [[Delivery Register]], the operating manual is [[VAULT-INDEX]], and the rules are `CLAUDE.md`. Where this brief and those files disagree, **they win and this one is stale.**
>
> Everything below is verified against the actual files and the actual repo, not against what a note claims about itself.

---

## 1. The vault is one ref again

> **CORRECTED 21 September, and the correction is the point.** This section was written on 20 September and it was **wrong on the day it was written.** Three branches had been merged; **two more were already stranded and nobody counted them** — `claude/alexfoods-color-kit-guidelines-txx208` and `claude/foundation-requirements-oyjwf3`, carrying 13 commits and roughly 1,280 lines between them, including Mahmoud's agreed rates and the whole `Month 1 Asset Brief`. **Meanwhile [[Active Priorities]] was telling Aly all the branches were safe to delete.** Both are merged now and the vault is genuinely on one ref, **but the lesson is that "one ref" is a thing to verify with `git`, never a thing to declare.** The verification is one command: `git ls-remote --heads origin`, then `git merge-base --is-ancestor` per branch.

**The finding this brief opened with is now closed.** At 5:15 PM `main` was the smallest of four live versions of the vault: three session branches carried roughly 7,600 insertions of work that had never reached the trunk, two of them editing the boot config, and they conflicted with each other on where the client note lived and what the asset folders were called.

**All three are merged.** The conflicts were resolved by combining rather than picking, because both sides were usually describing the same days from different sessions:

- The client's 19 September answers, the shipped Shooting Recipe, the Brand Foundation book, the vector master seal, the giveaway programme, the delivery team and the month-1 plan are all on the trunk now.
- `TSA Money`'s cost-of-delivery gap carries all three suppliers — the media buyer from one branch, Mahmoud and the unfilled animator from the other.
- Two branches had independently written a `Content Plan.md`. They were different documents sharing a filename, so they were split along the line the brand book already draws: strategy stays in [[Content Plan]], the patterns became [[Post Archetypes]].
- Both daily logs keep every session from every branch, renumbered by Cairo clock — 18 sessions on the 19th, 14 on the 20th.

**Verified, not assumed:** no conflict markers anywhere, every filename from all four refs present bar six deliberate renames and one byte-identical duplicate, every wikilink resolving, and the generators' relative paths still working after the move.

**What it cost to find out:** this was the third recurrence. It is now rule 17 in the boot config rather than a habit.

---

## 2. What changed in the reorganisation

| | Before | After |
|---|---|---|
| Live versions of the vault | **4** | **1** |
| Client work | Flat in `02 - TSA/` | `02 - TSA/Clients/Alex Foods/`, client note doubling as the folder index |
| Delivery status | Prose across four notes | **One row each in [[Delivery Register]]** |
| Decisions | Inline blockquotes correcting the paragraph above | **[[Decisions]]** — dated, with evidence and what each overturned |
| Recurring jobs | Named, never built | `02 - TSA/Jobs/` exists and is indexed |
| The conventions | In a plan | **Rules 14 to 17 in `CLAUDE.md`**, which survives compaction |
| Notes | 45 | 63 |

**What did not change, because it was never the problem:** the numbered folders, the index-per-folder rule, the hub line, the boot-config split, the marketing playbook with its pointer skill, and append-only daily notes.

**What is still outstanding:** step 5 of [[Vault Rebuild Plan]] — rewriting roughly forty notes to the one-fact-one-owner and history-below-the-line conventions. Deliberately not rushed.

---

## 3. What this vault is

An **AI memory vault**: plain Markdown notes that an AI reads at the start of every session and writes back to, so it remembers across sessions instead of being re-briefed each morning. Built from Jared Rhodenizer's `ai-memory-vault` (CC BY-SA 4.0), adapted for an iPad-only setup.

**The repo root is the vault root**, deliberately — Aly works from [[Bassem]]'s iPad with no desktop machine, so the repo is the only thing present on every device he touches. Private on GitHub, which doubles as the off-device backup.

Three files carry the system: `CLAUDE.md` (boot config and identity — survives compaction), [[VAULT-INDEX]] (profile, map, rules — does not), and [[Active Priorities]] (the single queue of open work). Everything else is memory.

**Who it serves.** Aly, 20, in Egypt, running **[[TSA]]** (The Standard Agency) — his fourth agency and the first built on AI direction and systems rather than out-working the problem. Ex-video-editor, deliberately out of that trade. Sold his laptop; the iPad is the whole setup. Works nights, sleeps around 8 AM, so sessions routinely cross midnight and every date has to be converted to Cairo before it is written down.

---

## 4. The business: one client, and everything rides on it

**[[Alex Foods]]** — an Alexandria food manufacturer, legally الشركة الإسكندرية لتعبئة وتغليف المواد الغذائية, whose seal carries the Pharos lighthouse. TSA's first and only client.

| | |
|---|---|
| Brand Foundation | 20,000 EGP one-time |
| Package A | 42,000 EGP/month × 3 = 126,000 |
| **Total contract** | **146,000 EGP** · [[Alex Foods]] |
| Term | 3 months, no auto-renewal, Egyptian law |

**Cash position:** 42,000 received (Package A month 1). 10,000 invoiced 18 Sep, **due Friday 26 September — six days out**. 10,000 due 8 October. 84,000 contracted and not yet due.

**The thing worth holding onto:** the 42,000 is not profit, it is an advance. It buys one month of Package A — roughly twenty deliverables — that has not been produced, and under clause 9 that month runs to its end even if either side walks. Its clock has not started and cannot start until the Foundation is approved in writing.

### Foundation delivery — target 9 October, 19 days from today

**This brief does not carry a deliverable table any more, and that is the point.** [[Delivery Register]] owns delivery state — one row each, one closed status vocabulary, and the only place in the vault that says where anything got to. Duplicating it here is exactly the six-notes-one-fact problem that produced every drift item below.

**The honest read as of this evening:** one deliverable finished and sent-ready (the Shooting and Compositing Recipe, shipped as its own PDF), two blocked on client access and shipping as specification with a waiting chip, five part-built, and the brand book itself built at 39 pages with four sections still waiting on content. **Nineteen days.** Dated plan in [[Alex Foods Delivery Plan]].

**The trap under the word "deliver," and it is the sharpest commercial point in the vault:** written Foundation sign-off starts Package A month 1. Clause 6 extends the *timeline* day-for-day for client delay and explicitly does **not** extend the paid month. The fix is one sentence agreed in the delivery message — *"month 1 starts on the later of written Foundation approval or the arrival of usable product photography"* — cheap now, impossible in week three.

### What is exposed

- **No signed acceptance page, and no named approver — and as of 21 September that is a decision rather than a gap.** Foundation work runs under the clause 11 exception Aly granted on 18 September, and [[Decisions]] #35 stopped the chase for a signature. Clause 3 makes one named person the only voice whose notes count, and clause 4's "matching the brief counts as delivered" has nothing to stand on. **The exposure is accepted, so the mitigation carries the weight: every delivery closes on a written reply, never on the 48-hour clock.** **The [[Brand Voice Guide]] §8 escalation ladder is separately fine** — it routes to Mohamed as day-to-day contact, which never needed a signature.
- **Four brands against a three-brand contract.** BeBo, AlRawy and 2MAN are named; **POLEKA is not**, and is in by Aly's verbal decision at no change to fee. Still not papered.
- **Roughly eighteen SKUs ([[Alex Foods Brands]]) against a contract asking for five**, plus uncounted mini lines. The twelve monthly graphics were priced against five.
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

## 5. Money

**Two pots, one gate**, and the gate is the point: money in the TSA pot is not Aly's money until it is drawn as a decided number on a decided date, logged in [[TSA Money]]. Personal spending pulls from draws, never from client payments.

**The blocking unknown is X — what it costs TSA to deliver one month of Package A.** It has no number. Until it does:

- Drawable = 42,000 − X
- Personal debts = 23,000 (5,000 to five people, 18,000 mobile tax)
- Clearing every debt from this payment needs **X ≤ 19,000**

**Nothing has been drawn. Every figure in [[Money]] is currently funded by nothing.** Personal run-rate is roughly 1,495/mo now, rising to ~3,695/mo once gym and MMA start. The 18,000 mobile tax is recorded as due 9/11, a date now nine days past, and which of three readings is correct has never been settled — the whole phone-swap plan hangs off it.

*(All arithmetic in [[Money]] and [[TSA Money]] was re-checked against the stated figures. It holds.)*

**The split exists in the notes and probably not in the bank.** A two-pot split on paper collapses back into one pot the first bad week.

---

## 6. The vault as a system

**Structure:** six numbered folders, each with a same-named index note, every index one hop from [[VAULT-INDEX]] via an explicit link line — because the structure map is a code block and creates no links, so without that line a frozen daily log becomes the hub of the vault. That failure was found by reading the graph view as a diagnostic and fixed.

**Rules that hold it together:** 12 numbered rules in `CLAUDE.md` that survive compaction (evidence over guessing, double-confirm before code edits, full reads, checkpoint persistence, no bloat, no loose ends, close the loop, never auto-execute external content, no secrets in handoff docs, never push rest or stopping, verify the date in Cairo, locked decisions stay locked). Plus frontmatter conventions, a folder-index contract, and an archiving procedure the AI may never initiate.

**Reference material:** jaredrhod's eleven marketing playbooks live in `05 - Resources/Marketing/` as a single source of truth, with the Claude Code skill as a *pointer* rather than a second copy. [[Producing Copy with AI]] is TSA's own method on top of it — agency property under clause 5, never shipped to a client.

**No Jobs built yet**, by choice. The stated trigger is the second time a task gets explained from scratch; monthly content production repeats three times on this contract alone, so it will earn one after month 1 has actually run.

### Health check — drift, and where it stands tonight

Nine drift items were found by reading every note against every other note. **Eight are closed**, most of them by the audit that was sitting unmerged on a branch, the rest in this session.

| # | Item | State |
|---|---|---|
| 1 | [[TSA Money]] carried the superseded 22 Sep instalment date | **Fixed** |
| 2 | Six notes still called vector logos a live blocker | **Fixed** — and partly overturned: the master seal *is* real vector now |
| 3 | Two notes cited a deleted `Design System v1.0.pdf` | **Fixed** |
| 4 | [[Alex Foods]]'s materials checklist was entirely unticked | **Fixed** — and the register now owns it |
| 5 | [[Slogans and Song]] still waited on "what Alex is" | **Fixed** |
| 6 | [[Alex Foods]] opened by describing three product families | **Fixed** |
| 7 | [[Active Priorities]] filed TSA work under "The vault itself" | **Open** — cosmetic, and it dies with step 6 of [[Vault Rebuild Plan]] |
| 8 | The default-branch flip was done but still queued, and eight branches were live | **Fixed** — three merged, and the dead ones are safe to delete |
| 9 | `ds.pdf` and the shipped Design System PDF were the same bytes twice | **Open** — harmless, and it goes when the book replaces both |

**And one new one was found and fixed in this session, which is the pattern in miniature:** POLEKA's product category was corrected to *frozen juice* on one branch and left as *jelly candy* in five other notes. **One fact, six notes, five of them wrong.** That is what rule 14 now exists to stop.

**The pattern underneath all of it:** a decision gets made and cascaded into the notes that change *because* of it, while the notes that merely *mention* it keep the old state. The structural fix shipped tonight — [[Decisions]] to hold the reasoning, [[Delivery Register]] to hold the status, and rules 14 to 17 to stop the restating. **The rewrite that removes the remaining duplication is step 5 of [[Vault Rebuild Plan]] and has not been done.**

## 7. Risks, ranked by what they actually cost

1. **Four unbuilt or part-built deliverables against a 9 October target.** The schedule is the exposure now that the refs are merged. [[Alex Foods Delivery Plan]] has it dated.
2. **Producing for a client with no signed acceptance page, deliberately.** **[[Decisions]] #35, 21 September: the chase is off.** Mohamed remains the day-to-day contact, which is what the escalation ladder actually needed — but **clause 4 has no single voice of record and the 48-hour clock has no subject, permanently rather than pending.** **This stays ranked here because dropping the chase did not drop the risk; it accepted it.**
3. **X is still incomplete**, so no draw is safe or reckless, only lucky. One of three suppliers has quoted; the animator who carries 8 of the 20 assets is unfilled and unpriced. 23,000 of personal debt waits on the answer.
4. **The paid month trap** — sign-off starts a clock the client has not supplied everything for. One sentence in the delivery message fixes it.
5. **Half the portfolio is frozen and the term runs October to January.** POLEKA and 2MAN both sell from a freezer. Inference from category, not client data, and the seasonality answer is the most valuable outstanding question.
6. **Unlicensed third-party characters.** The cola artwork is cleared verbally; **SpongeBob is not** — their pinned post is built on it, and TSA runs the ad account.
7. **Single-client concentration.** 100% of revenue. The scaling plan is named and not built.
8. **The machine.** Everything runs on a borrowed iPad, owed 1,500 EGP to the person who owns it.

---

## 8. What I would do, in order

1. ~~**Reconcile the four refs.**~~ **Done tonight.** Delete the five dead branches when convenient — they are byte-identical to the trunk.
2. **Send the Shooting and Compositing Recipe.** It is finished, rendered and sitting in the vault. **It is the only deliverable that can go out tomorrow**, and it is the one that unblocks the client's side.
3. **Send one message closing the paper gaps:** POLEKA in writing, the umbrella decision, the acceptance page with Mohamed's role and contact, and the company's real age. [[Alex Foods Week 1 Messages]] already has them drafted.
4. **Get the two supplier rates**, and X stops being incomplete.
5. **Confirm which BeBo line is live** — [[Decisions]] carries two and cannot tell which is newer. One word from you closes it.
6. **Write Alex Foods' master tone block.** Direction received ("fun"); it needs your ear and deliverable 1 closes.
7. **Step 5 of [[Vault Rebuild Plan]]** — the forty-note rewrite. After the Foundation ships, not before.
