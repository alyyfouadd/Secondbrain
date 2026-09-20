# -*- coding: utf-8 -*-
"""The one marker vocabulary, shared by every check.

A "marker" is a word on a line that says the line is RECORDING something
rather than ASSERTING it. History is allowed everywhere in this vault --
that is the point of keeping an audit trail -- so a line that carries a
marker is never a failure.

This lives in one file because check.py and structure.py each had their own
list and they drifted apart within a day: `LOGO.pdf` sat on a line beginning
"CORRECTED 19 September", which check.py recognised and structure.py did not.
Two checks disagreeing about what counts as history is the same disease the
whole tool exists to catch.
"""

# A line carrying one of these is history, not a live claim.
HISTORY = (
    "superseded", "withdrawn", "was wrong", "corrected", "audit trail",
    "retired", "no longer", "kept because", "not sendable", "as a fact",
    "rewritten anyway", "unfrozen", "contested", "was:", "originally",
    "reversed", "replaced", "stale", "retired-ok", "on hold",
    "removed", "deleted", "never committed", "not in the vault", "not in this vault",
    "not in this repo", "used to read", "used to say", "used to sit",
    "former", "git history retains", "folded in", "supersedes",
)

# A line carrying one of these names something that does not exist YET and
# is not supposed to. Only the file-existence checks use this.
PLANNED = (
    "delivered as", "will ship", "will be", "ships as", "not yet",
    "to be built", "pending", "target", "external reference",
)

def is_history(text):
    low = text.lower()
    return any(m in low for m in HISTORY)

def is_planned(text):
    low = text.lower()
    return any(m in low for m in PLANNED)
