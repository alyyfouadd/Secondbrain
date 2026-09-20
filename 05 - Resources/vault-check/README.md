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

## The PDF check — the half that was missing

**Every `.md` and `.py` could be clean while page 11 of the shipped book said the opposite**, and the shipped book is the thing that actually reaches the client. That is exactly how the BeBo reversal survived: Aly was holding the printed page.

So the checker reads the PDFs too. There is no poppler here and no PDF library, so `pdftext.py` decodes them directly — FlateDecode content streams, ToUnicode CMaps, the `Td/TD/Tm/T*/Tj/TJ` operators — which is the same approach `design-system/pdf2svg.py` already uses for vector artwork.

**It rebuilds lines, and that is the whole point.** A PDF is a bag of positioned glyphs. Every other check here is line-based because **a line is the unit that can carry a history marker**, so the glyphs have to be regrouped by text-matrix y-position before the same marker rules can apply. Match the document as one blob and you are back to a check that can only pass everything or fail everything — and an audit-trail page would fail the build forever.

Two things that took a rewrite to get right, worth not rediscovering:

- **Chromium emits `<0031> Tj`, hex strings, not `(text) Tj`.** A literal-string-only parser extracts zero lines and looks perfectly reasonable doing it.
- **`1 0 0 -1 x y Tm` means the text space is y-down**, so the page reads in *ascending* y. Sorting descending silently reverses every page.

**Arabic needs `variants()`.** It comes out of a PDF in visual order as presentation-form glyphs, so a pattern typed the way a human writes it never matches. NFKC folds the presentation forms back to base letters and reversing restores logical order; a pattern is matched against the raw, folded and reversed forms. **These deliverables are almost entirely Arabic, so this is load-bearing, not a nicety.**

A finding names the **page number**, because that is what you need when you are holding the printout. And the fix is always *correct the source and re-render* — editing a PDF is not a fix.

**Source documents are skipped.** A retired claim inside `TSA - Alex Foods Service Scope V2.pdf` is what the signed contract says, not drift in our work, and it is not ours to edit.

> **One caveat, stated because it matters:** the marker vocabulary is English and the deliverables are Arabic, so in practice a marked exemption almost never fires inside a PDF. That is the right behaviour — **a shipped deliverable should not contain an audit trail** — so a retired claim in a PDF is very nearly always a real failure.

## The structural half

`structure.py` asks a different question: not *does the vault still say something it retired*, but *does the vault still hold together*. Six checks — PDF references that resolve, valid frontmatter, wikilinks that resolve, no wikilinks inside a daily log, folder-index coverage, orphaned notes. `check.py` runs it, so one command runs everything.

**Both halves share one marker vocabulary, in `markers.py`.** They each had their own list for about a day and the lists drifted: `LOGO.pdf` sat on a line beginning "CORRECTED 19 September", which one half recognised as history and the other did not. **Two checks disagreeing about what counts as history is the same disease the tool exists to catch**, so there is now exactly one list.

## Using it

**When a decision reverses something, add a row to `retired.tsv` in the same checkpoint.** That is the whole discipline, and it is one line. The script then finds every place the old claim survives, including the ones in code that a note-level search would never reach.

**Found on its first run, after a session that had already "fixed" the same facts by hand:** 18 live statements across 8 files, including `kit.py` describing BeBo's audience as the mother and three copies of a lifted ban inside the deliverable that was about to be sent to the client.

---

**Related:** [[Resources]] · [[Decisions]] · [[Vault Rebuild Plan]] · [[Vault Brief]]
