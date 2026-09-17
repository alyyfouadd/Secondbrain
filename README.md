---
status: active
project: meta
type: guide
---
# Secondbrain

This repository is an **AI memory vault**. It is not a codebase — it's a set of plain Markdown notes that an AI reads at the start of every conversation and writes back to as we work, so it remembers across sessions instead of being re-explained to every morning.

Built from [ai-memory-vault](https://github.com/jaredrhod/ai-memory-vault) by Jared Rhodenizer (CC BY-SA 4.0), adapted for an iPad-only setup.

## The two files that matter

| File | What it is |
|---|---|
| `CLAUDE.md` | The boot config. Claude Code loads it automatically every session. Holds the agent's identity, the vault's location, and the rules that can't lapse. Configuration, not a note. |
| `VAULT-INDEX.md` | The operating manual. Profile, the map of the vault, and the full rules any AI follows when reading or writing here. Read at the start of every conversation. |

Everything else is memory.

```
00 - Inbox/          Capture everything, sort later
01 - Daily Notes/    One file per day, in month subfolders
02 - TSA/            The Standard Agency
03 - Personal/       Money, health, training
04 - Archive/        Finished work
05 - Resources/      Reference material, templates, Jobs
Active Priorities.md The single queue of open work
```

---

## Setting this up on the iPad

The vault is the repo, so the iPad needs two things: a git client to hold the clone and sync it, and Obsidian to read and edit it. Both are one-time.

**1. Install Obsidian.** Free on the App Store. Don't open a vault yet — there's nothing to open until step 3.

**2. Install a git client.** Obsidian on iOS cannot do git by itself. [Working Copy](https://workingcopy.app) is the standard choice and the free tier clones and pulls; pushing your own commits requires the paid unlock, which matters here because this vault is written to constantly.

In Working Copy: **+ → Clone repository →** `https://github.com/alyyfouadd/Secondbrain.git`, and sign in to GitHub when asked. The repo is **private**, so this step needs real credentials — a GitHub account with access, not an anonymous clone.

**3. Point Obsidian at the clone.** In Working Copy, open the repository's settings and use **Setup Folder Sync** (or share the repo folder to the Files app), then in Obsidian choose **Open folder as vault** and pick the `Secondbrain` folder. Obsidian now reads the repo directly, and `.obsidian/app.json` in this repo means it opens already configured.

**4. Commit and push after a working session.** This is the part that's easy to forget and the part that actually protects the memory: a note you wrote on the iPad only exists on the iPad until it's committed and pushed. Do it in Working Copy at the end of a session. An uncommitted note is an unsaved note.

### What's deliberately not tracked

`.obsidian/workspace*.json` is in `.gitignore`. Those files record which panes happen to be open on one device and rewrite themselves constantly — tracking them means a merge conflict on every sync in exchange for nothing. The rest of `.obsidian/` **is** tracked, so the vault's real settings travel with it.

### Connecting other AIs

- **Claude Code:** reads `CLAUDE.md` automatically. Nothing to do.
- **Claude.ai or Desktop:** add to User Preferences — *"At the start of every new conversation, read VAULT-INDEX.md from the root of my Obsidian vault."*
- **Any other AI with access to these files:** tell it to start by reading `VAULT-INDEX.md`. The rules are plain English; any capable model follows them.

### Backup

The vault lives on GitHub, privately, which is already a real off-device backup — it covers the case the original build guide warns about, where a vault sits on one machine and a dead machine takes the memory with it. The thing that breaks it is uncommitted work, which is why step 4 exists.
