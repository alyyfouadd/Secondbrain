---
status: active
project: tsa
type: reference
---
# Brand Book Spec — Alex Foods Brand Foundation

The design and production specification for the document the [[Alex Foods]] Brand Foundation ships inside. What the PDF is, how it is laid out, what goes on every page, and how it gets built from an iPad.

**This is the wrapper, not the contents.** The eight deliverables are written work sequenced in [[Foundation Roadmap]]. This note governs the artifact they arrive in — and the artifact matters, because 20,000 EGP that arrives as a Google Doc reads as notes, and the same words in a built document read as a system.

---

## 1. The decision that governs every other one

**The book is neutral. The brands are loud. The book never joins in.**

Four consumer brands with four deliberately clashing palettes have to live inside one document as equals. The moment BeBo's green becomes the section-header colour on page 12, the document has taken a side, and AlRawy's section looks like a guest in someone else's book.

So the rule, and it is absolute:

> **Brand colour appears as an object, never as an atmosphere.**
> Swatches, specimen fields, navigation tabs and the artwork itself are objects. Page backgrounds, headers, rules, tinted panels and type colour are atmosphere, and those stay in the house neutrals.

The house shell is off-white paper, near-black ink, one grey for secondary text. Nothing else. It is the empty gallery the four brands hang in.

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

**The PDF is a build artifact and does not get committed.** The HTML is the master and belongs in the vault; a 15 MB render regenerated on every revision would bloat every clone on every device forever, exactly as the print-resolution mockups would have. Same decision, same reason.

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

## 6. Page architecture

The contents page **mirrors the signed Service Scope V2's own deliverable list, in the scope document's own wording**, mapped to page numbers. That is not presentation — it is clause 4 armour. A client rejecting a delivery has to state a written reason, and a delivery matching the agreed brief and the approved guide counts as delivered. A contents page that reads as the contract's checklist makes "this isn't what we bought" a much harder sentence to write.

| § | Section | Pages | Scope deliverable |
|---|---|---|---|
| 00 | Cover | 1 | — |
| 01 | How to use this book | 2 | — |
| 02 | Contents and deliverable map | 2 | — |
| 03 | Brand architecture | 4 | — *(the spine everything else hangs on)* |
| 04 | Colour system | 11 | 2 (part 1) |
| 05 | Type system | 7 | 2 (part 2) |
| 06 | Logo use | 5 | 2 (part 3) |
| 07 | Brand voice | 10 | 1 |
| 08 | Slogans and the giveaway song | 4 | 4 |
| 09 | Social pages setup | 5 | 3 |
| 10 | Animation and shooting recipe | 6 | 6 |
| 11 | Content calendar | 4 | 5 |
| 12 | Google Business Profile | 2 | 7 |
| 13 | Local SEO — Alexandria | 5 | 8 |
| 14 | Governance and version control | 2 | — |
| 15 | Sign-off | 1 | — |

### The pages that carry the weight

**00 — Cover.** Type only on off-white: the title in Arabic and English, the client, The Standard Agency, version, date, and the named approver it is prepared for. No logo collage — four logos on a cover reads as a supplier catalogue. One graphic move instead: a single horizontal band at the foot of the page split into the four brand primaries. Four brands, one system, said in one line without a word. It also survives the unresolved "Alex" question, because it needs no parent mark to work.

**03 — Brand architecture.** The three layers — parent seal, brand, flavour — drawn on an actual pack, with the rule that falls out of them: *the flavour colour owns the field, the brand colour owns the logo, and they never trade places.* This is the page that earns the 20,000. Everything downstream is application.

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

- **What "Alex" is.** Decides whether § 03 carries a house layer at all, and how every bio in § 09 and every sign-off reads. The book is structured so the house layer is one insertable section — build around it, drop it in when the answer lands.
- **Vector logo files.** § 06 cannot ship finished without them. It ships with the rules written and the artwork marked `PENDING CLIENT INPUT` rather than holding the whole book.

---

**Related:** [[Alex Foods]] · [[Foundation Roadmap]] · [[Colour and Type Kit]] · [[Alex Foods Brands]] · [[TSA]]
