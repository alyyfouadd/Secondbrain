#!/usr/bin/env python3
"""
structure.py - the structural half of vault-check.

check.py asks "does the vault still SAY something it retired?"
This asks "does the vault still HOLD TOGETHER?" - links that resolve,
frontmatter that is valid, indexes that exist, files that are really there.
check.py imports and runs it, so `python3 check.py` runs both.

EVERY CHECK IS LINE-BASED AND MARKER-AWARE.

That is the whole design, and it is not a detail. This vault deliberately
keeps its own history in place: a note says "v1.0 was superseded and
removed" and that sentence is correct, permanent, and refers to a file
that no longer exists. A whole-file check has to choose between failing
that note forever or exempting it forever, and exempting a whole file
hides the real drift sitting three lines below.

So a finding is raised against a LINE, and a line is exempt when it
carries a marker saying what it is:

  HISTORY  - this was true and is recorded on purpose
  PLANNED  - this does not exist yet and is supposed to not exist yet

Anything else that points at something missing is real drift.
"""
import os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

import markers

PLANNED = re.compile(r"""
    \bdelivered\ as\b       # the spec naming a file it will produce
  | \bwill\ (?:ship|be|carry)\b
  | \bships?\ as\b
  | \bnot\ yet\b
  | \bto\ be\ built\b
  | \bpending\b
  | \btarget\b
  | \bonce\ .{0,40}\ exists\b
""", re.X | re.I)

VALID = {'status': {'active','completed','parked','idea','archived'},
         'project': {'tsa','personal','meta'},
         'type':    {'index','reference','guide','plan','log'}}

# folders that hold assets or build files, not notes - see VAULT-INDEX
ASSET_FOLDERS = {'fonts','tsafonts','single','client-legacy-creative',
                 'packshots','design-system','logos-transparent','logos-vector'}

findings = []
def flag(check, path, line_no, msg):
    findings.append((check, os.path.relpath(path, ROOT), line_no, msg))

def marked(line):
    """Is this line exempt, and why? Same vocabulary as check.py - see markers.py."""
    if markers.is_history(line): return 'history'
    if markers.is_planned(line): return 'planned'
    return None

def strip_code(line):
    """Obsidian does not link inside code spans, so neither do we."""
    return re.sub(r'`[^`]*`', '', line)

def walk_lines(path):
    """Yield (line_no, raw_line) skipping fenced code blocks."""
    fenced = False
    with open(path, encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            if line.lstrip().startswith('```'):
                fenced = not fenced
                continue
            if not fenced:
                yield i, line.rstrip('\n')

# ---------------------------------------------------------------- gather
notes, assets = {}, set()
for r, ds, fs in os.walk(ROOT):
    if '.git' in r.split(os.sep) or 'vault-check' in r.split(os.sep) or 'graphify-out' in r.split(os.sep): continue
    for f in fs:
        p = os.path.join(r, f)
        if f.endswith('.md') and '.claude' not in r.split(os.sep) and 'vault-check' not in r.split(os.sep):
            notes.setdefault(os.path.splitext(f)[0], []).append(p)
        assets.add(f)

def run():
    findings.clear()
    # ---------------------------------------------------- 1. PDF references
    # A note may name a PDF that is gone (history) or not built yet (planned).
    # Everything else must exist on disk.
    for name, paths in notes.items():
        for p in paths:
            # A daily note is an append-only record of what was true on its
            # date. "Shipped v1.0.pdf" was true on 18 Sep and stays true as a
            # sentence about that day. The filename IS the marker, so the whole
            # class is exempt from this check rather than needing a word added
            # to every line. Logs stay in every other check.
            if '01 - Daily Notes' in p and re.search(r'\d{4}-\d{2}-\d{2}\.md$', p):
                continue
            for n, line in walk_lines(p):
                # Only a BACKTICKED name is a reference. Verified against all 46
                # notes: every genuine PDF reference in this vault is in a code
                # span, and prose that merely quotes a filename ("shipped
                # v1.0.pdf") is an example, not a pointer. Matching bare prose
                # made this check flag its own documentation.
                for ref in re.findall(r'`([^`\n]*?\.pdf)`', line):
                    ref = ref.strip()
                    if '<' in ref or '>' in ref:      # <client contract>.pdf template
                        continue
                    base = os.path.basename(ref)
                    # A note often cites a file by a shortened name, e.g.
                    # `Design System v1.1.pdf` for the real
                    # `Alex Foods - Design System v1.1.pdf`. Suffix-match so a
                    # correct citation is not reported as a missing file.
                    if base in assets or any(a.endswith(base) for a in assets):
                        continue
                    why = marked(line)
                    if why:
                        continue
                    flag('pdf', p, n, f'`{base}` is referenced but does not exist, '
                                      f'and the line carries no history or planned marker')

    # ------------------------------------------------- 2. frontmatter
    for name, paths in notes.items():
        for p in paths:
            if os.path.basename(p) == 'CLAUDE.md': continue
            head = open(p, encoding='utf-8').read()
            m = re.match(r'^---\n(.*?)\n---\n', head, re.S)
            if not m:
                flag('frontmatter', p, 1, 'no YAML frontmatter'); continue
            fm = dict(re.findall(r'^(\w+):\s*(.+)$', m.group(1), re.M))
            for k, allowed in VALID.items():
                if k not in fm:
                    flag('frontmatter', p, 1, f"missing '{k}'")
                elif fm[k] not in allowed:
                    flag('frontmatter', p, 1, f"{k}: {fm[k]!r} is not one of {sorted(allowed)}")

    # ------------------------------------------------- 3. wikilinks resolve
    inbound = collections.Counter()
    for name, paths in notes.items():
        for p in paths:
            for n, line in walk_lines(p):
                for t in re.findall(r'\[\[([^\]\|#]+)', strip_code(line)):
                    t = t.strip()
                    if t in notes:
                        if t != name: inbound[t] += 1
                    elif not marked(line):
                        flag('wikilink', p, n, f'[[{t}]] resolves to nothing')

    # ------------------------------------------------- 4. a log never wikilinks
    for name, paths in notes.items():
        for p in paths:
            if '01 - Daily Notes' not in p or 'Daily Notes.md' in p or 'Template' in p:
                continue
            for n, line in walk_lines(p):
                if re.search(r'\[\[', strip_code(line)):
                    flag('dailylog', p, n,
                         'daily notes reference in backticks, never [[wikilinks]] - '
                         'it makes a frozen log the hub of the graph')

    # ------------------------------------------------- 5. folder indexes
    for r, ds, fs in os.walk(ROOT):
        parts = r.split(os.sep)
        if ('.git' in parts or '.claude' in parts or '.obsidian' in parts
                or 'vault-check' in parts or 'graphify-out' in parts
                or '__pycache__' in parts or r == ROOT):
            continue
        b = os.path.basename(r)
        if b in ASSET_FOLDERS or re.match(r'^\d\d - \w+ \d{4}$', b):
            continue
        want = re.sub(r'^\d+\s*-\s*', '', b) + '.md'
        if want not in fs:
            flag('index', os.path.join(r, want), 0,
                 f'note folder has no index note (expected {want})')

    # ------------------------------------------------- 6. orphans
    for name, paths in notes.items():
        if name in ('CLAUDE', 'README', 'VAULT-INDEX'): continue
        if inbound[name] == 0:
            flag('orphan', paths[0], 0, 'nothing in the vault links to this note')

    return list(findings)

def report(found):
    by = collections.defaultdict(list)
    for c, p, n, m in found: by[c].append((p, n, m))
    for c in sorted(by):
        print(f'\n  structure/{c}  ({len(by[c])})')
        for p, n, m in sorted(by[c]):
            print(f'    {p}:{n}  {m}')

if __name__ == '__main__':
    f = run()
    report(f)
    print(f"\nstructure: {len(f) or 'clean'}")
    sys.exit(1 if f else 0)
