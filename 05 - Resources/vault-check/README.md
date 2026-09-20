---
status: active
project: meta
type: guide
---
# vault-check — the guard that makes a correction stick

**Run it before any render and before any commit:**

```
python3 "05 - Resources/vault-check/check.py"
```

Exit 0 is clean. Exit 1 prints every place the vault still states something it has retired, what is true instead, and where that was decided.

## The problem it exists to solve

**Aly, 20 September: *"how do I make sure that anything I say is updated everywhere in the vault."***

He asked it while holding a page of the shipped brand book that described BeBo as a powder you make into a jug, in copy written to a mother. **Both facts had been reversed that same day** and the correction had reached the voice guide and stopped there.

**The reason it stopped is that the content is duplicated.** `Brand Voice Guide.md` holds the BeBo captions. `book.py` holds its own copy. `kit.py` holds a third. Correcting the note changes one of three, and **nothing in the vault knew the other two existed.**

> **This is why a fresh vault would not have fixed it.** A new vault starts with the same duplication on day one: the generators still carry their own strings. **The disease is not the folder structure, it is that a fact lives in more than one place and nothing checks.** Rules 14 to 17 in the boot config state the discipline. This script is what happens when the discipline is not enough, which on a document this size it never is.

## How it works

`retired.tsv` holds one row per retired claim, tab separated:

```
pattern	what is true now	where the decision is recorded
```

`check.py` walks every `.md` and `.py` in the vault and fails on any **live** statement of a pattern.

**History is allowed and is not a failure.** A line is skipped when it carries a marker — *superseded, withdrawn, was wrong, corrected, audit trail, no longer, reversed, retired-ok* — and whole regions can be exempted:

```
<!-- retired-ok:start -->
   ... the audit trail of how a decision was reached ...
<!-- retired-ok:end -->
```

**Always skipped:** `01 - Daily Notes/` (an append-only log records what was believed at the time), `Decisions.md` and `Vault Brief.md` (both are records of supersession by design).

## Using it

**When a decision reverses something, add a row to `retired.tsv` in the same checkpoint.** That is the whole discipline, and it is one line. The script then finds every place the old claim survives, including the ones in code that a note-level search would never reach.

**Found on its first run, after a session that had already "fixed" the same facts by hand:** 18 live statements across 8 files, including `kit.py` describing BeBo's audience as the mother and three copies of a lifted ban inside the deliverable that was about to be sent to the client.

---

**Related:** [[Resources]] · [[Decisions]] · [[Vault Rebuild Plan]] · [[Vault Brief]]
