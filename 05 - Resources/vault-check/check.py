#!/usr/bin/env python3
"""vault-check — the whole-vault doctor.

    python3 "05 - Resources/vault-check/check.py"          # everything
    python3 "05 - Resources/vault-check/check.py" --quiet   # failures only

Exit 0 = clean. Exit 1 = at least one FAIL.

Every check here exists because that exact class of mistake actually shipped.
When a new class is found, it becomes a check rather than a resolution to be
more careful.
"""
import os, re, sys, json, collections

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
QUIET = "--quiet" in sys.argv

SKIP_DIRS  = (".git", ".obsidian", ".claude", "vault-check", "fonts", "tsafonts")
LOG_DIR    = "01 - Daily Notes"
HISTORY_FILES = ("Decisions.md", "Vault Brief.md")
MARKERS = ("superseded", "withdrawn", "was wrong", "corrected", "audit trail",
           "retired", "no longer", "kept because", "not sendable", "as a fact",
           "rewritten anyway", "unfrozen", "contested", "was:", "originally",
           "reversed", "replaced", "stale", "retired-ok", "on hold")

VALID = {"status": {"active","completed","parked","idea","archived"},
         "project": {"tsa","personal","meta"},
         "type": {"index","reference","guide","plan","log"}}

FAILS, WARNS = [], []
def fail(check, where, msg): FAILS.append((check, where, msg))
def warn(check, where, msg): WARNS.append((check, where, msg))

# ---------- gather ----------
def walk(exts):
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and ".git" not in d]
        if any(s in root for s in SKIP_DIRS): continue
        for fn in sorted(files):
            if fn.endswith(exts):
                yield os.path.join(root, fn)

def rel(p): return os.path.relpath(p, VAULT)
def read(p):
    try: return open(p, encoding="utf-8").read()
    except Exception: return ""

MD  = [p for p in walk((".md",))]
PY_ = [p for p in walk((".py",))]
ALL_FILES = {rel(os.path.join(r, f))
             for r, d, fs in os.walk(VAULT) if ".git" not in r for f in fs}
NOTE_NAMES = {os.path.splitext(os.path.basename(p))[0] for p in MD}

# ---------- 1 · conflict markers ----------
for p in MD + PY_:
    for i, l in enumerate(read(p).splitlines(), 1):
        if re.match(r"^(<{7,8}[^<]|>{7,8}[^>]|={7,8}$)", l):
            fail("conflict-markers", f"{rel(p)}:{i}", "unresolved merge marker")

# ---------- 2 · frontmatter ----------
for p in MD:
    r = rel(p)
    if os.path.basename(p) in ("CLAUDE.md",) or "/README.md" in "/"+r: pass
    s = read(p)
    if not s.startswith("---"):
        if os.path.basename(p) != "CLAUDE.md":
            fail("frontmatter", r, "no YAML frontmatter")
        continue
    fm = s.split("---", 2)[1]
    for k, allowed in VALID.items():
        m = re.search(rf"^{k}:\s*(\S+)", fm, re.M)
        if not m: fail("frontmatter", r, f"missing `{k}`")
        elif m.group(1) not in allowed:
            fail("frontmatter", r, f"{k}: `{m.group(1)}` is not one of {sorted(allowed)}")

# ---------- 3 · every note folder has an index ----------
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS and ".git" not in d]
    if any(s in root for s in SKIP_DIRS) or root == VAULT: continue
    r = rel(root)
    if re.match(r"^01 - Daily Notes/\d\d - ", r): continue          # month folders share one index
    mds = [f for f in files if f.endswith(".md") and f != "README.md"]
    if not mds:
        continue   # pure asset folders are covered by their parent's README
    name = os.path.basename(root).split(" - ")[-1]
    if (f"{name}.md" in files) or ("README.md" in files) or (f"{os.path.basename(root)}.md" in files):
        continue
    # a client folder's index is the client note, which is named after the folder
    fail("folder-index", r, "no `<Folder>.md` index and no `README.md`")

# ---------- 4 · wikilinks resolve ----------
for p in MD:
    s = re.sub(r"`[^`]*`", "", read(p))
    s = re.sub(r"```.*?```", "", s, flags=re.S)
    for t in set(re.findall(r"\[\[([^\]|#]+)", s)):
        t = t.strip()
        if t and t not in NOTE_NAMES:
            fail("wikilink", rel(p), f"[[{t}]] resolves to nothing")

# ---------- 5 · backticked paths that do not exist ----------
PATHISH = re.compile(r"`([A-Za-z0-9 _\-./]+\.(?:md|py|css|pdf|png|jpg|svg|tsv|json|html))`")
for p in MD:
    base = os.path.dirname(rel(p))
    for m in set(PATHISH.findall(read(p))):
        if m.startswith(("http", "@")) or " " == m: continue
        cands = {m, os.path.normpath(os.path.join(base, m))}
        if any(c in ALL_FILES for c in cands): continue
        if any(os.path.basename(m) == os.path.basename(f) for f in ALL_FILES): continue
        warn("dead-path", rel(p), f"`{m}` is not a file in the vault")

# ---------- 6 · retired claims stated live ----------
rules = []
for ln in read(os.path.join(HERE, "retired.tsv")).splitlines():
    if ln.strip() and not ln.startswith("#"):
        parts = ln.split("\t")
        if len(parts) >= 3: rules.append(tuple(x.strip() for x in parts[:3]))
for p in MD + PY_:
    r = rel(p)
    if r.startswith(LOG_DIR) or os.path.basename(p) in HISTORY_FILES: continue
    muted = False
    for i, line in enumerate(read(p).splitlines(), 1):
        low = line.lower()
        if "retired-ok:start" in low: muted = True; continue
        if "retired-ok:end" in low:  muted = False; continue
        if muted or any(mk in low for mk in MARKERS): continue
        for pat, now, where in rules:
            if pat in line:
                fail("retired-claim", f"{r}:{i}", f"says “{pat}” — now: {now} ({where})")

# ---------- 7 · content duplicated between a note and a generator ----------
def arabic_runs(s):
    return {x.strip() for x in re.findall(r"[؀-ۿ][؀-ۿ ،؟.,!؟«»]{18,}", s)}
gen = {}
for p in PY_:
    for a in arabic_runs(read(p)): gen.setdefault(a, []).append(rel(p))
for p in MD:
    r = rel(p)
    if r.startswith(LOG_DIR) or os.path.basename(p) in HISTORY_FILES: continue
    for a in arabic_runs(read(p)):
        if a in gen:
            warn("duplicated-content", r,
                 f"same Arabic string also hard-coded in {', '.join(gen[a])} — “{a[:42]}…”")

# ---------- 8 · every PDF a note names actually exists ----------
pdfs = {os.path.basename(f) for f in ALL_FILES if f.endswith(".pdf")}
EXTERNAL = {l.strip() for l in read(os.path.join(HERE, "external.txt")).splitlines()
            if l.strip() and not l.startswith("#")}
for p in MD:
    r = rel(p)
    if r.startswith(LOG_DIR) or os.path.basename(p) in HISTORY_FILES: continue
    muted = False
    for i, line in enumerate(read(p).splitlines(), 1):
        low = line.lower()
        if "retired-ok:start" in low: muted = True; continue
        if "retired-ok:end" in low:  muted = False; continue
        if muted or any(mk in low for mk in MARKERS): continue
        for m in set(re.findall(r"`([^`]+\.pdf)`", line)):
            b = os.path.basename(m)
            if b in EXTERNAL or any(x in m for x in EXTERNAL): continue
            if b in pdfs: continue
            near = [f for f in pdfs if f.endswith(b) or b.endswith(f)]
            if near:
                warn("pdf-partial-name", f"{r}:{i}", f"names `{m}`; the file is `{near[0]}`")
                continue
            fail("missing-pdf", f"{r}:{i}", f"names `{m}`, which is not in the vault")

# ---------- 9 · notes nothing links to ----------
inbound = collections.Counter()
for p in MD:
    s = re.sub(r"`[^`]*`", "", read(p))
    for t in set(re.findall(r"\[\[([^\]|#]+)", s)):
        inbound[t.strip()] += 1
for p in MD:
    n = os.path.splitext(os.path.basename(p))[0]
    r = rel(p)
    if r.startswith(LOG_DIR) or os.path.basename(p) in ("README.md","CLAUDE.md","VAULT-INDEX.md"): continue
    if inbound[n] == 0:
        warn("orphan", r, "no note links to it")

# ---------- report ----------
def show(items, label):
    if not items: return
    print(f"\n{label} ({len(items)})")
    by = collections.defaultdict(list)
    for c, w, m in items: by[c].append((w, m))
    for c in sorted(by):
        print(f"\n  [{c}]")
        for w, m in by[c]: print(f"    {w}\n        {m}")

print(f"vault-check · {len(MD)} notes, {len(PY_)} generators, {len(rules)} retired claims")
show(FAILS, "FAIL")
if not QUIET: show(WARNS, "WARN — look, but not necessarily wrong")
print(f"\n{'CLEAN' if not FAILS else 'FAILED'} · {len(FAILS)} fail, {len(WARNS)} warn")
sys.exit(1 if FAILS else 0)
