---
status: active
project: tsa
type: reference
---
# Brand Book Spec — Alex Foods Brand Foundation

The design and production specification for the document the [[Alex Foods]] Brand Foundation ships inside. What the PDF is, how it is laid out, what goes on every page, and how it gets built from an iPad.

**This is the wrapper, not the contents.** The eight deliverables are written work sequenced in [[Foundation Roadmap]]. This note governs the artifact they arrive in — and the artifact matters, because 20,000 EGP that arrives as a Google Doc reads as notes, and the same words in a built document read as a system.

---

## 0. The deliverable carries TSA's brand — decided 18 September

**These are TSA documents about a client's brand, so [[TSA Brand System]] governs the page and the client's system is the subject.** Cover, section openers, footers, headings, labels and body copy are Precision Navy, Cold White, Signal Red, Barlow Condensed 800 and Inter. The client's colours and type appear only inside swatches and specimen blocks.

This replaces the earlier idea that the book should be set in the system it specifies. That is right for a brand book the client owns outright; it is wrong for a kit TSA hands over as the agency. **Aly's call, and it is the right one for a kit going out under TSA's name.**

**Cold White `#F0F2F5` is the document ground**, which is on-system rather than a compromise: TSA's own rules name it for "any document printed or sent to a client to sign."

> **The gap this exposed: TSA's brand system specifies no Arabic typeface.** Barlow Condensed and Inter are Latin only, and TSA is an Alexandria agency producing Arabic work. Every bilingual deliverable is currently off-system by necessity. Arabic here is set in IBM Plex Sans Arabic as an interim. **TSA's system needs an Arabic companion named and locked.** See [[TSA Brand System]].

## 1. The decision that governs every other one

**The book is neutral. The brands are loud. The book never joins in.**

Four consumer brands with four deliberately clashing palettes have to live inside one document as equals. The moment BeBo's green becomes the section-header colour on page 12, the document has taken a side, and AlRawy's section looks like a guest in someone else's book.

So the rule, and it is absolute:

> **Brand colour appears as an object, never as an atmosphere.**
> Swatches, specimen fields, navigation tabs and the artwork itself are objects. Page backgrounds, headers, rules, tinted panels and type colour are atmosphere, and those stay in the house neutrals.

The house shell is **Cold White ground and Precision Navy type, with Signal Red reserved for rules and eyebrows**, per [[TSA Brand System]]. It is the empty gallery the four brands hang in, and it is TSA's gallery.

## 2. The book obeys its own rules

The [[Colour and Type Kit]] sets rules — two weights maximum per layout, Arabic set first and English fitted to it, white type on a colour field carries a dark keyline. **If the book breaks those rules on its own pages, the rules are dead the day they ship.** Every page of this document is built under the system it specifies. That is not neatness; it is the only proof the system works that the client can actually see.

## 3. Format and production

| | |
|---|---|
| **Page size** | A4 portrait, 210 × 297 mm |
| **Length** | 60–70 pages *(a consequence of eight deliverables across four brands, not a target)* |
| **Live area** | 170 mm wide — 20 mm side margins, 22 mm top, 26 mm foot |
| **Grid** | 6 columns, 6 mm gutters, 23.3 mm columns. Splits at 2 / 3 / 6 cover every layout in the book. |
| **Direction** | RTL document, Arabic-primary |
| **Target file size** | Under 15 MB, so it sends on WhatsApp and email without a link |
| **Delivered as** | `Alex Foods — Brand Foundation v1.0.pdf` |

**Portrait, not landscape, and this was a real decision.** Landscape looks more like an agency deck and reads better on a laptop. But this client opens things on a phone, and a landscape A4 on a phone is a pinch-and-rotate job. It also gets printed in an Alexandria office on A4 with no scaling. A brand book is a reference document people look things up in, not a pitch — portrait is the one that actually gets read. Picked the one that gets read.

### How it gets built — the working method

**HTML and CSS, rendered to PDF. Not InDesign, not Canva.**

- InDesign does not exist on an iPad, so it was never an option.
- Canva would mean hand-assembling 60+ pages, and every revision round is a manual re-assembly. On a document with one included revision round and four brands to keep consistent, that is the wrong rail.
- HTML means the master is text: diffable, versionable, and a revision is an edit and a re-render rather than a redesign. It is also the rail the TSA invoice template already runs on, so it is one method, not two.

**The route:** the HTML source lives in the vault next to this note. It renders to PDF headlessly in a Claude Code session and comes back as a finished file. Aly never has to print anything. Fallback if a session is not available: open the HTML in Safari on the iPad, Share → Print → pinch the preview → Save to Files. Flag on the fallback — Safari can drop background fills on print, so `print-color-adjust: exact` goes on every coloured block and page 1 gets test-printed before anyone builds page 60.

**Correction, 18 Sep: the PDF does get committed.** The original call assumed a 15 MB render and treated it like the print-resolution mockups. **The real Design System render is 0.47 MB**, because a governance document carries swatches and type, not photographs. At that size the bloat argument does not hold, and Aly works from an iPad with no way to run a build, so a PDF he cannot open from the repo is a PDF he does not have. **Both go in: the source is the master, the PDF is the copy he can actually hand over.** If a future render ever carries photography and crosses a few MB, revisit it then.

## 4. Typography

**Document face: IBM Plex Sans Arabic + IBM Plex Sans.** Free, open-licensed, and genuinely drawn as one bilingual superfamily rather than a Latin face with Arabic bolted on — which is the difference between a document that looks designed and one that looks assembled. Codes and specifications are set in **IBM Plex Mono**, because HEX values in a proportional face do not align in a column and an `8` reads as a `B` at 8 pt.

*Verify the licence terms before shipping. Free-to-use is the strong expectation here, not a confirmed fact.*

**The book's face is not the brands' supporting face, and that distinction is deliberate.** The packs carry all the energy this system needs. The supporting type's job is order. Plex is the quiet member of the family, which is why the book is set in it and why it is the recommendation for the type system itself.

### Scale

| Role | Size / leading |
|---|---|
| Cover title | 72 pt |
| Section opener | 48 pt |
| Page heading | 28 pt |
| Sub-heading | 16 pt |
| Body | 10.5 pt / 15.75 pt |
| Caption and spec | 8.5 pt / 13 pt |
| Codes (mono) | 9 pt |

Two weights only across the whole book — Regular and SemiBold. That is the kit's own rule, applied to itself.

**No strict baseline grid.** Fighting CSS print for cross-column baseline alignment costs more than it returns on a reference document. Vertical rhythm comes from consistent block margins on a 5.5 mm step instead. Stated here so a future session does not try to "fix" it.

## 5. Bilingual handling

**Arabic leads, English follows, on every page.** Headings are Arabic with the English beneath at caption size. Explanatory text and rules run as parallel columns — Arabic right, English left — which works because rules are short imperative lines, not essays, so the columns stay in register.

**Sample copy is never translated.** The captions, slogans, reply templates and the giveaway song in the voice section *are the deliverable* — they are the actual Arabic that goes out. Translating Egyptian colloquial into English produces something nobody will ever post and quietly implies the English is the original. Sample copy stays in Arabic, with a one-line English gloss in the margin where a non-Arabic reader needs to follow the argument.

## 5b. DECIDED 19 September: one book, and what it swallows

**Aly's call, against `SWAG-Design-System.pdf` as the completeness bar: one document, not three.**

| Was | Now |
|---|---|
| `Design System v1.1.pdf`, 19pp, deliverable 2 | **Folded in as §04–06.** Stops being a client-facing document; `design-system/` and [[Colour System]] / [[Type System]] remain the internal source of the values. |
| `Brand and Social Kit v1.2.pdf`, 8pp, deliverable 3 | **Folded in as §07 and §11–14.** Its range pages and social spec survive as sections; its four page-4 defects die in the rewrite. |
| This book | **The only thing the client receives.** |

**Why this was the right call and not just a tidier one:** three documents stating the same hex value is the exact drift the vault's no-bloat rule exists to stop, and **a client handed three books has to be told which one wins.** The scope sells *one* Brand Foundation. It should arrive as one object.

> **One thing to confirm before it matters: nothing in the vault records the Design System PDF actually being sent to the client.** v1.0 was explicitly never sent, and [[Foundation Roadmap]] step 7 has the whole Foundation shipping in a single message around 9 October. **If it has not gone out, folding it in costs nothing.** If Aly has WhatsApped it to them at some point, they need one line saying it is now section 04 of the book rather than a separate document.

### The two production facts this creates

1. **The book roughly doubles, from 71 pages to about 105.** Nine genuinely new sections. **The template is proven** — the Design System exercised every page type — so this is content work, not layout work. **But it is still content work against a 9 October target and a 20,000 EGP deliverable, and that should be said plainly rather than absorbed quietly.**
2. **The 15 MB WhatsApp limit in §3 will not survive this, and that is a real problem rather than a detail.** The 8-page kit alone rendered at **10.2 MB**, because pack artwork is heavy. A 105-page book carrying range lineups, packshots and do-not pages will land far outside anything WhatsApp will carry. **The delivery route has to be solved before the book is finished, not after:** a compressed screen export alongside the full-resolution master, or a link. **Do not discover this at the moment of delivery.**

## 5c. BUILT 19 September — `Alex Foods - Brand Foundation v1.0.pdf`

**34 pages, 25 sections, bilingual throughout with Arabic leading, 8.0 MB.** Generated from `design-system/book.py`, which is now **the single source for every section's content** — `render(ids)` renders any subset, so an early standalone ship of one section is a call rather than a second script.

**What is DEFINED and complete: 17 sections.** Cover, how to use, contents, architecture, colour, type, logo and seal, the four ranges, voice, captions, canvas and grid, pack in field, flashes and characters, motion, shooting and compositing, compliance, the system in numbers, governance, sign-off.

**What carries a waiting chip: 5 sections.** §10 slogans *(needs a native ear, not a machine's guess)*, §14 social setup and §19 GBP *(both `SPEC · EXECUTION PENDING CLIENT ACCESS` — written in full, blocked on Meta admin and a Google account)*, §17 calendar *(needs seasonality)*, §18 patterns *(depends on §11, §13, §15 and POLEKA's unchosen extended colours)*, §20 local SEO.

> **The waiting sections are printed, not omitted, and each one states what it waits on and who from.** A book that quietly leaves a bought deliverable out is worse than one that says where it stands. This is the status-chip system in §6 doing the job it was specified for.

**Two things the build settled:**

1. **The 15 MB delivery problem did not materialise, and the earlier worry was wrong about why.** The book renders at **8.0 MB**, comfortably inside WhatsApp. The 10.2 MB on an 8-page kit came from full-bleed pack lineups on nearly every page; a governance book is mostly type, and only the range pages carry heavy artwork.
2. **`field.py` and `recipe.py` were deleted.** Their content is §12 and §16 of `book.py`. Keeping standalone generators would have put the same governance text in two files.

> **One deviation from §6 that needs Aly's word rather than a silent override.** This spec says the cover is **type only on off-white**. The built cover is **navy with the seal**, on the reasoning that the umbrella decision made the master own the seal and the presence, and a navy cover states the hierarchy before page 3 explains it. **The four-brand band at the foot is exactly as specified.** It is a one-line change back to Paper if the original call stands.

## 6. Page architecture

The contents page **mirrors the signed Service Scope V2's own deliverable list, in the scope document's own wording**, mapped to page numbers. That is not presentation — it is clause 4 armour. A client rejecting a delivery has to state a written reason, and a delivery matching the agreed brief and the approved guide counts as delivered. A contents page that reads as the contract's checklist makes "this isn't what we bought" a much harder sentence to write.

**Revised 19 September for the one-book decision.** Nine sections are new, marked **NEW**; they carry the depth the SWAG reference sets as the bar — states and configurable options rather than examples, and computed values rather than asserted ones. **The deliverable column is unchanged and still mirrors the signed scope**, because that mapping is the clause 4 armour and nothing about added depth is allowed to disturb it.

| § | Section | Pages | Scope deliverable |
|---|---|---|---|
| 00 | Cover | 1 | — |
| 01 | How to use this book | 2 | — |
| 02 | Contents and deliverable map | 2 | — |
| 03 | Brand architecture | 4 | — *(the spine everything else hangs on)* |
| 04 | Colour system | 11 | 2 (part 1) |
| 05 | Type system | 7 | 2 (part 2) |
| 06 | Logo and seal use | 5 | 2 (part 3) |
| 07 | **The ranges** — one spread each: BeBo, AlRawy, 2MAN *(both packs)*, POLEKA | 6 | — · **NEW**, from kit v1.2 |
| 08 | Brand voice | 10 | 1 |
| 09 | **The caption system** — structure, length per range, Arabic-first, emoji, hashtags | 3 | 1 · **NEW** |
| 10 | Slogans and the giveaway song | 4 | 4 |
| 11 | **Canvas, grid and export specs** — post sizes, safe areas per platform, live area | 4 | 3 · **NEW** |
| 12 | **The pack-in-field system** — how a cut-out pack sits on its flavour field | **4, BUILT** | 3 · **NEW** |
| 13 | **Flashes, badges and the character library** | 4 | 3 · **NEW** |
| 14 | Social pages setup | 5 | 3 |
| 15 | **Motion** — what moves, duration, easing, stills versus animations | 4 | 6 · **NEW** |
| 16 | Shooting and compositing recipe | **7, built** | 6 |
| 17 | Content calendar | 4 | 5 |
| 18 | **Post archetypes and pattern inventory** | 6 | 5 · **NEW** |
| 19 | Google Business Profile | 2 | 7 |
| 20 | Local SEO — Alexandria | 5 | 8 |
| 21 | **Compliance — contrast audit and the never list** | 3 | — · **NEW** |
| 22 | **The system in numbers · rebuilding from this book** | 2 | — · **NEW** |
| 23 | Governance and version control | 2 | — |
| 24 | Sign-off | 1 | — |

**About 105 pages.** Sections 04, 05, 06, 07 and 14 already exist as built content in the Design System and the kit, so **the writing is the nine NEW sections plus the deliverables that were always outstanding.**

### The three new sections that carry the most weight

**12 — The pack-in-field system.** **This is Alex Foods' signature device and the book has never specified it.** A cut-out pack on its own flavour field is what every graphic, every still and every animation is built from. SWAG devotes a whole section to its sticker-shadow because that one device is the brand; this is the equivalent. Specify the field, the pack's position and scale, the margin, what happens when a pack is portrait versus landscape, and **what a pack may never sit on.**

**18 — Post archetypes and pattern inventory.** **The section that makes the book buildable rather than admirable.** SWAG's pattern inventory lists all nineteen page patterns with exactly what is configurable in each. Here: every post pattern, per pillar — product, character, moment, trade — with what changes and what never does. **Without it the book describes a style. With it, somebody can make Tuesday's post without asking.**

**22 — The system in numbers, and rebuilding from this book.** SWAG's closing move, and it is worth stealing outright: the system counted (named colours, type sizes, post formats, patterns, ranges, SKUs), then the short paragraph naming **the few things everything else is assembled from**. It is how a reader knows they have understood the system rather than read it.

### The section that changed job
**16 — Shooting and compositing recipe** *(was "Animation and shooting recipe")*. **With product photography now produced by TSA with an AI product shooter, there is no client shoot to write specs for.** It becomes the production recipe: scene prompts, the compositing rules, and the lighting and angle constants that keep eighteen SKUs looking like one brand. **The rule it exists to enforce: AI makes the scene, the client's real artwork gets placed into it, and nothing about a pack is ever generated.** See [[Alex Foods]].

### The pages that carry the weight

**00 — Cover.** Type only on off-white: the title in Arabic and English, the client, The Standard Agency, version, date, and the named approver it is prepared for. No logo collage — four logos on a cover reads as a supplier catalogue. One graphic move instead: a single horizontal band at the foot of the page split into the four brand primaries. Four brands, one system, said in one line without a word. The band survives the architecture change intact: under the umbrella model it reads as the four ranges of one company, which is exactly what it now is. **What changed is the title block** — Alex Foods is set above the four rather than listed alongside them, so the cover states the hierarchy before page 3 explains it.

**03 — Brand architecture.** **Rebuilt 18 September on the umbrella model.** Alex Foods is the **master brand** and BeBo, AlRawy, 2MAN and POLEKA are **ranges beneath it** — not four independents that happen to share a factory. The page is drawn as a hierarchy, master on top and the three lower layers beneath it, rather than four equal boxes: *master, range, flavour, extended*, laid over an actual pack. The rule that falls out of it: *the flavour colour owns the field, the range colour owns the logo, and the master owns the seal and takes neither.*

**And the seal is a rollout, not a tier.** Its absence from BeBo and POLEKA is a print run that has not caught up. Printed packs stay as they are; new print carries it on every range. The page says so, because a designer reading "frozen where it sits" would refuse a seal the client is actively rolling out.

**This is the page that earns the 20,000**, and the umbrella call is what makes that true — it is a strategic decision about how the company goes to market, not a diagram. Everything downstream is application: § 09 builds **one** Alex Foods presence rather than four brand pages, and the calendar rotates the ranges inside it.

**04 — Colour system.** One spread explaining the system and the neutral house layer, then one page per brand for fixed brand colours with HEX, RGB and CMYK (conversions flagged as conversions, not press-accurate), then the flavour matrices, the neutrals, and a full **contrast table**: every text-on-field pairing with a verdict — *white / white + keyline / navy only*. That table is not decoration on a system where half the fields are pale yellow and lime.

**07 — Brand voice.** House voice, then one page per brand: register, words in and out, sentence length, emoji policy. Then the page most guides skip and this scope explicitly asks for — **the comment-reply policy**, written as actual reply templates for praise, complaint, price question, availability question and troll. A policy that says "reply warmly within 24 hours" is not usable by the person actually replying. Five templates are.

**10 — Animation and shooting recipe.** Camera angle, lens, lighting diagram, background, product framing, the shot list per SKU type, what makes a photo unusable, and a phone-shot fallback spec. **This section ships early and separately, as its own short PDF, before the book is finished** — it is the document that tells the client how to shoot the product photos TSA is still waiting on. Holding it inside the book keeps the client blocked on the thing that blocks the client.

**15 — Sign-off.** Name, role, contact, date, signature — and it does double duty. This is the page that gets the Foundation approved *and* the page that finally puts a named approver on file, which clause 3 has been missing since day one. One page closes two gaps.

### Rules that apply to every page

- **Status chip, top right of every section opener:** `DEFINED` · `SPEC — EXECUTION PENDING CLIENT ACCESS` · `PENDING CLIENT INPUT`. Two deliverables genuinely cannot be executed without Meta admin and a Google account. Saying so on the page is honest, it pre-empts "you didn't finish it," and it puts the delay where it belongs.
- **Every "never" is shown, not described.** Each system section ends with a do-not page: the wrong thing rendered at full size with a rule through it. A non-designer forgets a written prohibition and remembers a picture of the mistake.
- **Footer on every page:** `Alex Foods × TSA · Brand Foundation v1.0 · 09.10.2026 · p.NN`. A page found loose on a desk in six months has to identify itself and its version.
- **Page numbers are real and quotable.** This is a governance document — someone has to be able to say "page 34" on a phone call.
- **No stock photography, anywhere.** The book shows the brands' own artwork only. A stock lifestyle shot in a brand book is a promise about a photo library that does not exist.
- **Export specs live at the back**, not scattered: feed 1080 × 1350, story 1080 × 1920, profile 320 × 320 with the safe circle marked, cover per platform, GBP photo 1200 × 900 minimum. So the next designer does not have to ask.

## 7. What this spec is still waiting on

- ~~What "Alex" is.~~ **Answered 18 September: Alex Foods is the MASTER BRAND**, and the four are ranges beneath it. § 03 carries a master layer — **still no house palette**, but now by architectural choice rather than because a parent does not repaint what it endorses: the master owns the seal and the presence, the ranges keep the four clashing palettes that separate them on a shelf. **§ 09 builds one Alex Foods presence, not four brand pages**, and the earlier bio rule is withdrawn — **every bio names Alex Foods**, sealed pack or not, because the seal is mid-rollout rather than a tier. See [[Brand Voice Guide]] §2.
- **Alex Navy `#0A0378` has no ramp and no contrast row.** Sampled after the 18 masters were computed. Not a blocker for the book — the seal is placed as supplied — but § 04 carries the gap honestly rather than quietly. See [[Colour System]] §11.
- **Vector logo files.** § 06 cannot ship finished without them. It ships with the rules written and the artwork marked `PENDING CLIENT INPUT` rather than holding the whole book.

---

**Related:** [[Alex Foods]] · [[Foundation Roadmap]] · [[Colour and Type Kit]] · [[Alex Foods Brands]] · [[TSA]]
