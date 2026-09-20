#!/usr/bin/env python3
"""Fail loudly when the vault still states something it has retired.

Run it before any render and before any commit:
    python3 "05 - Resources/vault-check/check.py"

Exit 0 = clean. Exit 1 = a retired claim is stated live somewhere.
"""
import os, re, sys

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))

# History is allowed to mention a retired claim. These files ARE the history.
SKIP_PARTS = (".git", "01 - Daily Notes", "vault-check")
SKIP_NAMES = ("Decisions.md", "Vault Brief.md", "retired.tsv")

# A line that carries one of these is recording history, not asserting the claim.
MARKERS = ("superseded", "withdrawn", "was wrong", "corrected", "audit trail",
           "retired", "no longer", "kept because", "not sendable", "as a fact",
           "rewritten anyway", "unfrozen", "contested", "was:", "originally",
           "reversed", "replaced", "stale", "retired-ok", "on hold")

def load_rules(path):
    rules = []
    for ln in open(path, encoding="utf-8"):
        if not ln.strip() or ln.startswith("#"):
            continue
        parts = ln.rstrip("\n").split("\t")
        if len(parts) >= 3:
            rules.append(tuple(p.strip() for p in parts[:3]))
    return rules

def main():
    rules = load_rules(os.path.join(HERE, "retired.tsv"))
    hits = []
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not any(s in os.path.join(root, d) for s in SKIP_PARTS)]
        if any(s in root for s in SKIP_PARTS):
            continue
        for fn in files:
            if not fn.endswith((".md", ".py")) or fn in SKIP_NAMES:
                continue
            fp = os.path.join(root, fn)
            try:
                lines = open(fp, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            muted = False
            for i, line in enumerate(lines, 1):
                low = line.lower()
                # block-level exemption for a region that IS the audit trail
                if "retired-ok:start" in low:
                    muted = True; continue
                if "retired-ok:end" in low:
                    muted = False; continue
                if muted or any(m in low for m in MARKERS):
                    continue
                for pat, now, where in rules:
                    if pat in line:
                        hits.append((os.path.relpath(fp, VAULT), i, pat, now, where))

    if not hits:
        print(f"vault-check: clean. {len(rules)} retired claims, none stated live.")
        return 0

    print(f"vault-check: FAILED. {len(hits)} live statement(s) of a retired claim.\n")
    for fp, i, pat, now, where in hits:
        print(f"  {fp}:{i}")
        print(f"     says     : {pat}")
        print(f"     but now  : {now}")
        print(f"     decided  : {where}\n")
    print("Fix each one, mark the line as history (SUPERSEDED / withdrawn / was wrong),")
    print("or wrap a whole audit-trail region in <!-- retired-ok:start --> ... <!-- retired-ok:end -->.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
