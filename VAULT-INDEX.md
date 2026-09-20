---
status: active
project: meta
type: index
---
# VAULT INDEX

Read this file at the start of every conversation to understand who I am, how I work, and how this vault is organized.

---

## Vault location

**This vault is the `alyyfouadd/Secondbrain` git repository, and the repo root is the vault root.** There is no separate folder — the whole repo is the vault, and the notes, the boot config and the Obsidian settings all travel together as one thing. This section is the single source of truth for where the vault lives; the boot config's path line points back here rather than repeating a path, because I work across devices and a hardcoded path would be wrong on most of them.

Where it physically sits depends on which device is reading it:

- **iPad (my main and only machine):** a git client holds the clone, and Obsidian opens that clone as a vault. See [[README]] for the exact setup.
- **Any AI session:** the working directory it was started in. If you're an AI other than Claude Code, point your filesystem connector at the repo clone and tell the AI "my vault is here." An AI can't read or maintain a vault it can't find.

The vault is private — the GitHub repo is set to private, which is what makes it safe for the financial and personal detail in here.

---

## Who I Am

I'm Aly, 20, in Egypt. I run **[[TSA]]** (The Standard Agency) — my fourth marketing agency, and the first one I'm building on AI direction, systems and structure instead of raw effort.

Before this I spent years as a video editor and did well at it. I know how that game is played, and I don't want to work as an editor any more. I'm a marketing director and strategist now, with AI doing the execution alongside me.

I sold my laptop, so right now I work entirely from [[Bassem]]'s iPad. That's not a temporary inconvenience to design around later — it's the machine, and everything built for me has to work on it.

## Key People

- **[[Bassem]]** — my partner. I'm working from their iPad, and I owe them 1,500 EGP. The only person with their own note.
- **Abdrabo** — I owe them 1,000 EGP.
- **Omar Elawady** — I owe them 1,000 EGP.
- **Torgo** — I owe them 500 EGP.
- **Fares Hammam** — I owe them 1,000 EGP.
- **Mahmoud** — graphic designer. Produces the 12 monthly graphics for [[Alex Foods]]. A supplier, not an employee, and one half of TSA's cost of delivery.
- **Mohamed** — works with [[Alex Foods]]. **The named approver under clause 3**, so his are the only notes that count on a delivery. Role and contact still needed for the signed page.
- **A CGI animator** — not yet found as of 19 September 2026. Would own the 2 animations and 6 animated stills every month. **Eight of twenty monthly deliverables rest on this role being filled.**

**People notes: Bassem only.** Everyone else lives as a line in this section and nothing more. Don't create a note for a person, and don't wikilink their name, unless I say so — a note per name I once mentioned is clutter, and unresolved links make the graph lie about what the vault actually holds. If one of them becomes someone the work genuinely revolves around, I'll ask for the note.

## TSA — The Standard Agency (02 - TSA)

The Standard Agency is my one business. We grow businesses on social media, and we find high-value businesses that need the right positioning in the market to grow faster — with AI doing the heavy lifting on execution.

**No packages.** Every client gets a dedicated price and a dedicated set of services, built for what that specific business needs. I can deliver all of them myself.

This is my fourth agency. The difference this time is that it runs on direction, systems and structure rather than on me out-working the problem — and that the system has to scale *in parallel* with the business, not get bolted on after it hurts.

- **Status:** Active — first client signed, work in progress.

## Vault Structure

```
00 - Inbox          <- Capture everything, sort later
01 - Daily Notes    <- Dated logs of what got done, one file per day, in month subfolders
02 - TSA            <- The Standard Agency: clients, offers, positioning, scaling
  TSA Brand/        <- the agency's OWN locked identity: colour, type, tagline, logo
  Clients/          <- one folder per client; the client note IS that folder's index
    Alex Foods/     <- contract note, signed scope PDF, the plan, the brief, the messages
      Alex Foods Brands/   <- the four brands, the whole Foundation build, and the assets
        design-system/     <- the generators that build the client's PDFs
        logos-vector/      <- the client's real Illustrator master seal
        logos-transparent/ <- the four range marks, cut out on transparency
        packshots/         <- product mockups keyed to transparency
03 - Personal       <- Life outside the agency: money, health, training, things I'm buying
04 - Archive        <- Completed projects and old notes
05 - Resources      <- Cross-project reference material, templates, Jobs
  Marketing/        <- jaredrhod's marketing playbook, read before any marketing work
```

### The hub rule: links point UP, logs never point out

Two rules keep this file the centre of the vault instead of an ornament, and the graph view is where you check them.

1. **Every folder index ends with an `**Up:**` line back to [[VAULT-INDEX]]**, plus its parent index where it has one. Without it the root index is a *source* — fifteen links out, none in — which draws as a spoke on the edge of the graph rather than a hub at the middle. A hub is inbound-heavy.
2. **Daily notes never use `[[wikilinks]]`.** They reference notes and files by name in backticks. A daily note's "Notes Touched" section names twenty files, so wikilinking them makes a frozen log the single most connected node in the vault — which is exactly the failure the one-hop line below was added to fix, reappearing from the other direction. **The fix for an orphaned daily note is an inbound link from [[Daily Notes]], never outbound links from the log.**

> **Measured 20 September:** `2026-09-18.md` carried **202 wikilinks — 30 outbound edges against 1 inbound** — and sat dead centre of the graph while [[VAULT-INDEX]] sat on the rim. Converted to backticks; the daily notes are now leaf nodes and [[Alex Foods]], the live client, is the largest node, which is what a working vault should look like.

**Every folder index, one hop from here:** [[Inbox]] · [[Daily Notes]] · [[TSA]] · [[Personal]] · [[Archive]] · [[Resources]] · [[Marketing]] (inside Resources) · [[TSA Brand]] (inside TSA) · [[Clients]] (inside TSA) · [[Alex Foods]] (inside Clients — the client note doubles as its folder index) · [[Alex Foods Brands]] (inside Alex Foods)

> **Asset and build folders are deliberately not on that line.** `design-system/`, `packshots/`, `logos-transparent/` and `logos-vector/` hold artwork, fonts and build scripts rather than notes, so each carries a **`README.md`** — documentation sitting beside code, not a node in the graph. They are described from [[Alex Foods Brands]], which is where a human would actually look them up. Giving `fonts/` an index note listing twenty-six `.woff2` files would be bloat under rule 5, not a map.

That line is not decoration. The map above is a code block, so it creates no links — without these, the only thing pointing at the folder indexes is whichever daily note happened to mention them, which makes a frozen log the hub of the vault instead of this file. This index is the hub. Every folder is one step away from it, and a new folder's index gets added to this line in the same pass that creates it.

## What's Active Right Now

All open work lives in one note: [[Active Priorities]]. Tag each item with its project where it isn't obvious. Check it at the start of every conversation; verify an item's real state before acting on it (a listed item may already be done).

## Background

I've been a video editor for years and I got good at it — good enough to know exactly how that game is played, which is why I'm out. TSA is my fourth agency. The first three taught me what I was missing, and it wasn't effort or skill: it was structure, upfront planning, and a system that holds the shape of the business so I'm not the only thing holding it. That's what this vault is. I sold my laptop to get here and I'm running the whole thing from an iPad.

## How I Think

- I take the second step first, then have to come back and redo the one I already made. I don't know why I do it. Structure is the fix, and that's the whole reason this vault exists — so put step one in front of me when you see it happening.
- I want the plan upfront. I need to know where I'm going before I move, and I want the system to scale alongside the business rather than lag behind it.
- I'd rather build the thing that holds than the thing that works today.

## Personal Interests

- Training is the next thing I'm building into my life: gym and MMA are both lined up to start, and I'm buying the kit for each before I begin.
- Coffee.
- Long term I want a racing bike.

## Daily Routine

- I sleep around 8 AM Egypt time. My working day runs through the night and across midnight, so "today" for me usually means a date that started the previous evening. Check the real Cairo date and time before writing either one down.

## What I Want

Right now, winning is one thing: getting past this money problem. Clearing what I owe, handling the mobile tax, and getting to stable ground.

Past that: scale TSA with real structure and upfront planning, so I always know where I'm going and can grow without the system breaking underneath me.

Long term: my own place, my own machine, and the freedom that comes with both. The full picture of what that costs is in [[Money]].

## My Preferences for Working with AI

- **Plain language, no jargon, and be direct.** Don't hedge or over-qualify. Be honest and upfront, always.
- **Don't settle for half-finished work.** Do it right the first time. "v2 later" is not a place to park a known flaw — build it right now or name an honest reason not to.
- **Be a partner, not a yes-man.** Argue your position when you think I'm wrong. When I push back, don't just cave — half the time I'm testing your reasoning. Make your case, show the tradeoffs, then let me decide. Only change your answer if my argument actually changes your mind.
- **Take it straight.** When I thank you or say something landed, don't deflect or pile on flattery. Just keep building.
- **When I ask "why do you need that?", it's a spec-check, not confusion.** Treat it as a flag that your plan might be off. Re-examine it, then either fix it or explain with examples.
- **Recommend for my actual setup, not a generic beginner.** I'm on an iPad. No laptop, no desktop, no terminal of my own. Weight what I actually have. Never hand me a fix that needs a machine I don't own.
- **Give me the plan before the work.** Sequencing is the thing I'm buying from you. If you catch me jumping to step two, stop me and put step one in front of me.
- **I move fast — don't sandbag timelines.** My bottleneck is planning, not doing. Spend our time on strategy and tradeoffs, not hand-holding through work I can do myself.
- **Pull me back from rabbit holes.** When a tangent shows up, decide if it serves the current goal. If not, flag it ("that's a tangent from X — pursue or park?"). Be the closer.
- **Offer to draft my copy; don't wait to be asked.** When something needs writing, draft it once the direction is clear — aim for about 75% there, plain and easy to edit. I lead on what to say.
- **Don't push me toward shipping.** After a round of edits, show me what changed and stop. No "ready to ship?" I'll say when I'm ready.
- **Restating isn't approving.** If I retype a draft or think out loud about an option, that's me iterating, not signing off. Don't save it as final until I clearly say "lock it" or "ship it." When unsure, ask.
- **Money is tight right now, and that's context, not a mood.** When a recommendation costs money, say what it costs and what the cheaper or free version gives up. Never quietly assume I'll spend.
- **Hand me big structured data as a file, not a chat paste.** Tell me the columns you need (never secrets) and I'll send a file.
- **Most of my guidance is guidelines, not laws.** When I hand you a rule of thumb, it's a reference point, not legislation. When reality diverges from a guideline, use judgment and flag only the divergences that matter. Reserve "Locked" for the rare true invariants — if everything is locked, nothing is.
- **I drive the trust-and-access ramp.** Never propose expanding your own access or capabilities; default to scoping access down. When I decide we're ready for more, we'll add it with safeguards. More access comes from me, not from you.

---

## How My Memory Works (for the AI)

This vault is your memory. It is external and effectively unlimited. Do not try to hold all of it at once. Hold only what the current task needs, and trust that everything else is one search away. To find something, start at this index, follow the folder indexes and wikilinks, or search. Knowing a note exists is as good as holding it, because you can retrieve it in one step. This is what lets you operate across everything here without drowning.

---

## Vault Rules for AI

These rules apply to any AI that reads or writes to this vault.

### Frontmatter and Wikilinks

Every note MUST have YAML frontmatter. When you create a note, include it. When you edit an existing note that's missing or has incomplete frontmatter, fix it as part of that write. Don't stop to add frontmatter to files you're only reading. Code files are the exception — no frontmatter or wikilinks in code. `CLAUDE.md` is also an exception: it is Claude Code configuration that happens to sit at the vault root, not a note.

Never ask Aly what the frontmatter values should be. Infer them.

### Note format

Simple, legible, readable. No random emojis. Checkboxes are real Markdown checkboxes (`- [ ]` / `- [x]`), never emoji stand-ins. **Append before you create:** default to adding to an existing note rather than spinning up a new one — fewer, fuller notes beat many thin ones. Create a new note only when nothing existing is a logical home.

```yaml
---
status: active
project: tsa
type: plan
---
```

When creating or editing a note, add `wikilinks`:

**Always link:** anyone in Key People · named businesses, products, and platforms · any note this one directly references, extends, or depends on.
**Never link:** generic words just because a note shares the name · the same target twice in one note · the note's own title.

### How to Determine Each Field

**status** — Default `active`. For existing notes infer from content: in progress / has unchecked items -> `active`; all done -> `completed`; a future "maybe" -> `idea`; was active but gone quiet -> `parked`; in the Archive folder -> `archived`.

**project** — What the note *serves* (folder is the default, but content wins). Mapping:
- `02 - TSA/*` -> `tsa`
- `03 - Personal/*` -> `personal`
- `01 - Daily Notes/*` -> **`tsa` by default**, because that is what the days are actually spent on. A day genuinely dominated by personal work takes `personal`. *(This used to read `personal` unconditionally, which contradicted the "content wins" line above it and mis-filed a log that is almost entirely agency work.)*
- `04 - Archive/*` -> infer from content / original project
- `05 - Resources/*` -> `meta`
- `00 - Inbox/*` -> infer from content, else `personal`
- Root-level files -> `meta`

**type** — What KIND of document it is (not its topic):
- `index` — a folder index / map-of-content note (or this root index)
- `reference` — a static document meant to be looked up later (specs, knowledge bases, templates, voice guides)
- `guide` — step-by-step how-to, runbook, or build instructions
- `plan` — a strategy, phased build, or multi-step project plan (Active Priorities is a plan)
- `log` — a dated session capture or working note (daily notes are logs)

### Valid Field Values

**status:** `active` | `completed` | `parked` | `idea` | `archived`
**project:** `tsa` | `personal` | `meta`
**type:** `index` | `reference` | `guide` | `plan` | `log`

### Folder Indexes (keep them in sync)

**Every folder here has an index, with no exceptions and no "once it fills up."** The index is named after the folder with its number prefix stripped — `03 - Personal/Personal.md`, `01 - Daily Notes/Daily Notes.md` — carries frontmatter `type: index`, and lists each note in the folder with a one-line description.

**One sanctioned double-duty: a client folder.** `02 - TSA/Clients/<Client>/<Client>.md` is both the client note and that folder's index — the name lines up by design. A client has exactly one master note, and splitting "the map of this folder" away from "what they bought" makes two thin notes where one full one belongs. It carries `type: index` and opens with a "What's in this folder" block before the deal. This is the only place a note wears two hats; don't generalise it. The index is a contract: when you create, rename, move, or materially change a note, update its folder's index in the same pass. A stale index makes a future session decide from a wrong map.

**When a new folder is created:** create its `<Folder Name>.md` index at the same time, add an entry to the parent folder's index if it has one, and update the **Vault Structure** map in this file in the same pass. A folder the map doesn't show is a folder no future session will look in.

*(One local adaptation, because this vault is a git repo: git does not track empty folders. So every folder here gets its index note from day one, even the ones that are still empty, or the folder would vanish on the next device that syncs the repo.)*

**The one carve-out: asset and build folders take a `README.md`, or nothing.** A folder holding artwork, packshots, fonts or build scripts is not a note folder, and giving `fonts/` an index note listing twenty-six `.woff2` files would be bloat under rule 5 rather than a map. The line is what a human would actually look something up in:

- **A folder of notes gets `<Folder Name>.md`**, `type: index`, wikilinked from its parent and from the one-hop line above. No exceptions, and this is the rule that matters.
- **A folder of assets or build files gets a `README.md`** when there is something a future session genuinely needs — provenance, limits, a build command, a trap worth not rediscovering. `logos-transparent/`, `packshots/` and `design-system/` each earn one. It is named `README.md` on purpose: it is documentation sitting beside code and artwork, not a note in the graph, and it is described from the nearest real index rather than wikilinked.
- **A folder of raw material gets nothing.** `fonts/`, `tsafonts/`, `packshots/single/` and `client-legacy-creative/` hold files their parent already explains. A note per folder here would be a note nobody opens twice.
- **Month subfolders under `01 - Daily Notes/` get no index either.** [[Daily Notes]] lists every daily note directly, wikilinked, which keeps one map instead of one per month.

**Stated because the rule as written said "no exceptions" and eight folders were quietly breaking it.** A rule everybody has to silently ignore is worse than a rule with a written boundary — the first time a session obeys it literally, the vault gains eight index notes nobody wanted.

### Renaming and moving notes

- **Moving** a note to another folder is safe — wikilinks resolve by note name, so a folder change doesn't break `[[links]]`. Update both folders' indexes in the same pass.
> **A real example of why this rule exists, 19 September 2026.** Four asset folders each carried an index called `README.md`, and the root vault-setup doc is also `README.md`. **Three `[[README]]` wikilinks all meant the root one, and Obsidian had five files to choose from.** The link resolved to whichever it felt like. The four asset indexes were renamed to match their folders — `design-system.md`, `packshots.md`, `logos-transparent.md`, `logo-vector.md` — which was safe only because nothing wikilinked them; they were referenced by path in prose, and every one of those references was updated in the same pass. **`README.md` at the root keeps its name and `[[README]]` now resolves to exactly one file.**

- **Renaming** a note (changing its name) breaks the `[[links]]` pointing to it unless the rename is done **inside the Obsidian app**, whose "auto-update internal links" setting repairs them automatically (already switched on in `.obsidian/app.json`). A shell `mv`, or any rename outside the app, does not. So do renames in the app; if the AI must rename a file directly, it then has to find and fix every `[[old name]]` reference by hand.

### Checkpoint Persistence

Whenever something changes that a future session would need to know, persist it without being asked: update the relevant note, today's daily note, and (only for a new always-on rule) CLAUDE.md. Then scan the touched folder's index and any cross-referenced notes for drift and fix it in the same pass. The vault is the memory — keeping it current is not busywork, it's maintaining the system itself.

**And because this vault is a git repo: a checkpoint isn't saved until it's committed.** A written file only changes the copy on the device it was written on. Commit it, and push it, or the next device syncs a vault that never heard about the change.

### Archiving

When Aly says something is done or asks to archive a note: (1) set its frontmatter `status: archived` and save; (2) move it to the Archive folder, same filename; (3) confirm what was archived and where. Always confirm before archiving. Never archive on your own initiative.

### Daily Notes

Daily notes capture what happened across all of Aly's work sessions for a day. They live in `01 - Daily Notes/`, in month subfolders named `NN - Month YYYY` (`01 - Daily Notes/09 - September 2026/`) from the very first note, never once the folder fills up -- a convention that starts later means two sessions reading two files disagree about where today's note goes. Filename `YYYY-MM-DD.md`. Frontmatter `status: active`, `project: personal`, `type: log`.

Start the body with a human-readable date heading (`# Friday, September 18, 2026`). Then, right after it, an **`## Index`** block: one bold-topic line per session/entry with a one-sentence outcome. The index makes a day with many entries scannable instead of a wall of prose. Then the entry body follows `01 - Daily Notes/Daily Note Template.md` — create every daily note FROM that template (What Got Done · What's Still In Progress · Decisions Made · Notes Touched · Profile Updates); never hand-roll one.

If today's note already exists from an earlier session, append a new session section (`## Session 2`, `## Evening Session`) and add a line to the Index block — don't overwrite. Timestamp each entry with Aly's local time (Africa/Cairo), never UTC.

**Aly works nights and sleeps around 8 AM,** so a session that starts in the evening routinely runs past midnight into the next calendar date. The rule is the plain one: the note's date is the real Cairo calendar date at the moment you write it. Don't back-date a 2 AM session to the previous day just because it feels like the same stretch of work — if a session spans midnight, it earns a second entry in the new day's note.

#### Trigger 1: Wrap-Up Signal
Never ask Aly if he's done working. When he signals it ("I'm done," "calling it," "goodnight"), offer to create or update today's daily note. Always check the actual current date and time first — conversations can stay open overnight.

#### Trigger 2: Review Yesterday's Note at Start of Conversation
At the start of every conversation, after reading this index, check yesterday's daily note (or the most recent weekday if today is Monday).
- **If it doesn't exist:** create it from whatever context you have (chat history, session context), and say it's reconstructed and may be incomplete. Zero context for that day -> assume a day off and skip it. Don't create empty daily notes.
- **If it exists:** read it; if you have context it's missing, append a session section; otherwise leave it alone.

This is universal — every AI that reads this vault does it. Aly uses multiple AIs across multiple sessions, no single one sees everything, so each contributes what it knows and the daily note fills in over time. Don't make a production of it. Briefly say what you did and move on.

### Living Profile

This file is a living document. Update the profile sections as you learn new things about Aly through conversation. Updates happen silently and are logged in the daily note under "Profile Updates."

**You can update:** Key People · How I Think · Health · Personal Interests · Beliefs · Daily Routine.
**You must NOT update:** Who I Am (basic bio — only Aly changes it) · the project sections · What's Active Right Now (lives in Active Priorities) · My Preferences for Working with AI · Vault Rules for AI.
**Vault Structure is a special case:** never rewrite it on your own initiative, but when a folder is actually created, renamed, or removed, updating the map is part of that change — do it in the same pass.

Judgment: a passing mention is not a personality trait. Check for duplicates/contradictions; if new info contradicts an entry, update that entry rather than adding a second. Match existing tone. Never remove an entry unless explicitly contradicted. Fewer, higher-quality updates.

Log every profile update in the daily note's "Profile Updates" section (e.g. "**Personal Interests:** added woodworking").

**Two sections are deliberately missing and should be added the moment Aly gives the material:** *Health* (nothing shared yet beyond training plans) and *Beliefs* (not discussed). Don't invent either one; ask, or wait until it comes up naturally.
