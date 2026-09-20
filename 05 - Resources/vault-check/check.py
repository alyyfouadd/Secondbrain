#!/usr/bin/env python3
"""Fail loudly when the vault still states something it has retired.

Run it before any render and before any commit:
    python3 "05 - Resources/vault-check/check.py"

Exit 0 = clean. Exit 1 = a retired claim is stated live somewhere.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdftext

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))

# History is allowed to mention a retired claim. These files ARE the history.
SKIP_PARTS = (".git", "01 - Daily Notes", "vault-check")
SKIP_NAMES = ("Decisions.md", "Vault Brief.md", "retired.tsv")

# PDFs the client sent US. A retired claim inside the signed scope is what the
# contract says, not drift in our work, and editing it is not an option.
SOURCE_PDFS = ("TSA - Alex Foods Service Scope V2.pdf",)

import markers, structure
MARKERS = markers.HISTORY

def load_rules(path):
    rules = []
    for ln in open(path, encoding="utf-8"):
        if not ln.strip() or ln.startswith("#"):
            continue
        parts = ln.rstrip("\n").split("\t")
        if len(parts) >= 3:
            rules.append(tuple(p.strip() for p in parts[:3]))
    return rules

def _all_pdfs(vault):
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if not any(s in os.path.join(root, d) for s in SKIP_PARTS)]
        if any(s in root for s in SKIP_PARTS):
            continue
        for fn in files:
            if fn.lower().endswith(".pdf") and fn not in SOURCE_PDFS:
                yield os.path.join(root, fn)

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

    # ---------------------------------------------------------------- PDFs
    # The deliverable that actually reaches the client is the PDF, and that is
    # exactly where the BeBo reversal survived: every .md and .py could be
    # clean while page 11 of the shipped book said the opposite.
    #
    # This check is line-based for the same reason every other one is: a line
    # is the unit that can carry a history marker. A PDF is a bag of positioned
    # glyphs, so pdftext rebuilds lines from the text-matrix before the same
    # MARKERS apply. Matching the whole document as one string would only ever
    # be able to pass everything or fail everything, and an audit-trail page
    # would fail the build forever.
    pdf_hits = []
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not any(s in os.path.join(root, d) for s in SKIP_PARTS)]
        if any(s in root for s in SKIP_PARTS):
            continue
        for fn in files:
            if not fn.lower().endswith(".pdf") or fn in SOURCE_PDFS:
                continue
            fp = os.path.join(root, fn)
            try:
                doc = pdftext.pages(fp)
            except Exception as e:
                pdf_hits.append((os.path.relpath(fp, VAULT), 0, "(unreadable)",
                                 f"{type(e).__name__}: {e}", "pdftext.py"))
                continue
            muted = False
            for pageno, plines in doc:
                for line in plines:
                    forms = pdftext.variants(line)
                    low = " ".join(forms).lower()
                    if "retired-ok:start" in low:
                        muted = True; continue
                    if "retired-ok:end" in low:
                        muted = False; continue
                    if muted or any(m in low for m in MARKERS):
                        continue
                    for pat, now, where in rules:
                        if any(pat in f for f in forms):
                            pdf_hits.append((os.path.relpath(fp, VAULT), pageno,
                                             pat, now, where))

    # The structural half: links that resolve, valid frontmatter, indexes that
    # exist, files that are really there. Same marker vocabulary, same
    # line-based rule - see structure.py.
    struct = structure.run()

    if not hits and not pdf_hits and not struct:
        print(f"vault-check: clean. {len(rules)} retired claims, none stated live.")
        print(f"             notes, code and {sum(1 for _ in _all_pdfs(VAULT))} shipped PDFs all checked line by line.")
        print( "             structure clean: links, frontmatter, indexes, orphans.")
        return 0

    print(f"vault-check: FAILED. {len(hits) + len(pdf_hits)} live statement(s) of a retired claim"
          f"{f', {len(struct)} structural finding(s)' if struct else ''}.\n")
    if pdf_hits:
        print("  IN A SHIPPED PDF - this is the copy that reaches the client:\n")
        for fp, pg, pat, now, where in pdf_hits:
            print(f"  {fp}  page {pg}")
            print(f"     says     : {pat}")
            print(f"     but now  : {now}")
            print(f"     decided  : {where}")
            print(f"     fix      : correct the source, then re-render. Editing the PDF is not a fix.\n")
    for fp, i, pat, now, where in hits:
        print(f"  {fp}:{i}")
        print(f"     says     : {pat}")
        print(f"     but now  : {now}")
        print(f"     decided  : {where}\n")
    if struct:
        structure.report(struct)
        print()
    print("Fix each one, mark the line as history (SUPERSEDED / withdrawn / was wrong),")
    print("or wrap a whole audit-trail region in <!-- retired-ok:start --> ... <!-- retired-ok:end -->.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
