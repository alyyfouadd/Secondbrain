---
status: active
project: personal
type: index
---
# Daily Notes

One note per day, logging what got done across every AI session that day. This is the append-only log — the one place in the vault where duplication across days is correct rather than sloppy.

## How it works
- Month subfolders, named `NN - Month YYYY` (e.g. `09 - September 2026`). This convention starts from the very first note, never once the folder fills up.
- Filename `YYYY-MM-DD.md`, frontmatter `status: active` · `project: personal` · `type: log`.
- Every note is created from [[Daily Note Template]] — never hand-rolled.
- If today's note exists already, a new session gets appended as `## Session N` with a line added to the Index block. Nothing gets overwritten.
- **Dates are Cairo time.** Aly works nights and sleeps around 8 AM, so sessions routinely cross midnight and the machine writing the note may be on UTC.

## Why an old daily note is not the truth
A daily note is a frozen snapshot of the moment it was written. Its "What's Still In Progress" section goes stale the second something closes. The live queue is [[Active Priorities]] — always check there for what's actually open, never here.

## Notes in this folder
- [[Daily Note Template]] — the shape every daily note is copied from.
- `09 - September 2026/` — 2026-09-18 onward. The vault's first day.
  - [[2026-09-18]] — 28 sessions. The vault built, Alex Foods scoped, the Foundation's first two deliverables written and shipped.
  - [[2026-09-19]] — the overnight continuation. Session 1 started at 11:05 PM on the 18th and is filed here because it crossed midnight.
  - [[2026-09-20]] — TSA restructured on the agency/client split; Alex Foods moved into `Clients/`; the vault audited end to end.

**Every daily note is wikilinked from this index, not just named.** Backticked filenames create no links, so the daily notes were graph orphans — floating islands nothing pointed at — which is the same defect the folder indexes had before the one-hop line was added to [[VAULT-INDEX]]. A month subfolder does not get its own index note; this list is the index for all of them.

---

**Up:** [[VAULT-INDEX]]
