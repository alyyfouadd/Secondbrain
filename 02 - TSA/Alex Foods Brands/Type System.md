---
status: active
project: tsa
type: reference
---
# Type System — Alex Foods

**Brand Foundation deliverable 2 of 8, part 2** for [[Alex Foods]]. The faces, the weights, the scales for print and for social, and the bilingual rules that stop an Arabic layout breaking. Pairs with [[Colour System]] to make deliverable 2 complete.

> **Shipped as a PDF, 18 Sep 2026.** Both halves of deliverable 2 are published as `Alex Foods - Design System v1.0.pdf`, 19 pages, A4. Source and build instructions in `design-system/`. **Deliverable 2 is complete and Phase 1 of [[Foundation Roadmap]] is closed.**

---

## 1. The rule that governs everything else

**No brand name in this system is ever set in a font.**

| Brand | The wordmark is | Consequence |
|---|---|---|
| **BeBo** | Heavy rounded italic sans, customised | Close to typeset. Still artwork. |
| **AlRawy** | Rounded sans with a script quality, plus flowing Arabic | Artwork. |
| **2MAN** | Custom illustrated 3D lettering, dripping ice | **Cannot be retyped. Ever.** |
| **POLEKA** | Custom illustrated 3D gel lettering | **Cannot be retyped. Ever.** |

All four are placed as supplied vector artwork. Anyone who rebuilds a logo because the file was missing has produced something unusable, and it will be spotted.

> **Revised again 19 Sep: the master seal is real vector.** `logo-vector/alex-seal.svg`, converted 1:1 from the client's Illustrator PDF. The rule is unchanged and the mark is still never rebuilt — what changed is that "as supplied" now means an actual path set for the master, so it holds at any size including print. **The four range wordmarks are still raster.**

> **Revised 18 Sep.** No source files exist. All four marks are now available cut out on transparency in `logos-transparent/`, which is sufficient for every deliverable in this contract, since none of them are printed. **The rule above is unchanged and is what matters: the wordmark is placed as supplied and never rebuilt.** Whether "as supplied" means a vector path or a transparent PNG only starts to matter at print or at large scale, and neither is in scope.

## 2. The faces

**TSA selects the type; the client approves the choice, not the process** (clause 1). Selected:

| Role | Face | Weights | Cost |
|---|---|---|---|
| **Arabic and Latin text** | **IBM Plex Sans Arabic** | 400, 600, 700 | Free |
| **Latin, where set alone** | **IBM Plex Sans** | 400, 600, 700 | Free |
| **Codes and specifications** | **IBM Plex Mono** | 400, 600 | Free |

**Why this family.** It is drawn as one bilingual superfamily rather than a Latin face with Arabic bolted on, which is the difference between a system that looks designed and one that looks assembled. Plex Sans Arabic carries a complete Latin set of the same design, so there is no visible seam where a line switches script. And the mono sibling matters more than it sounds: **HEX values in a proportional face do not align in a column, and an `8` reads as a `B` at 9pt.**

**The honest tradeoff.** Plex runs cool and slightly technical. On BeBo and POLEKA it will not supply warmth, and it is not supposed to: **the packs carry all the personality this system needs, and the type's job is order.** Warmth comes from colour, character and copy. If the client rejects it on that basis, the fallback is **Cairo** (also free, also open-licensed, warmer and more geometric), and the scales below transfer unchanged.

*Licence: IBM Plex is published under the SIL Open Font License. **Confirm the current terms before the book ships** — the expectation is strong but it was not verified from source in this session.*

## 3. Weights

**400 Regular · 600 SemiBold · 700 Bold.**

> **Two weights maximum in any single layout.** One for the headline, one for everything else. These packs are already visually loud and the type does not need to compete. A third weight in a layout is the most common way a tidy system starts to look accidental.

## 4. Scale — documents and print (A4)

| Role | Size | Leading |
|---|---|---|
| Cover title | 72 pt | 1.05 |
| Section opener | 48 pt | 1.1 |
| Page heading | 28 pt | 1.2 |
| Sub-heading | 16 pt | 1.3 |
| Body | 10.5 pt | 1.5 Latin · **1.7 Arabic** |
| Caption | 8.5 pt | 1.45 |
| Code (mono) | 9 pt | 1.4 |

## 5. Scale — social, in pixels

This is the table that actually gets used, because it is what the twelve monthly graphics are built against. Sizes are for a **1080 × 1350 feed post**; story at 1080 × 1920 uses the same values with more vertical breathing room.

| Role | Size | Leading | Weight |
|---|---|---|---|
| Hero line | 96 px | 1.1 | 700 |
| Headline | 64 px | 1.15 | 700 |
| Sub-head | 44 px | 1.25 | 600 |
| Body | 32 px | 1.5 Latin · **1.7 Arabic** | 400 |
| Caption and legal | 24 px | 1.4 | 400 |
| **Absolute floor** | **22 px** | — | — |

> **Nothing goes below 22 px on a feed asset.** Below that it is unreadable on a phone at thumbnail size, which is where most of the audience sees it, and it is the size everyone is tempted to use for the weight statement or the flavour name.

## 6. Bilingual rules

These are the ones that break layouts when ignored.

1. **Arabic is set first. English is fitted to it.** A layout designed in English and then filled with Arabic will break, every time. The line lengths, the optical weight and the direction are all different.
2. **Arabic is never a machine translation of the English.** It is written, then the English is matched to it. See [[Brand Voice Guide]].
3. **Arabic carries more leading than Latin: 1.7 against 1.5.** Arabic has deeper descenders and optional diacritics, so Latin leading crowds it and the marks collide with the line below. Setting both scripts at the same leading is the single most common tell of a layout built by someone who does not read Arabic.
4. **Layout direction is RTL** on anything Arabic-primary, including the order of columns, the side the logo sits on, and the direction a carousel reads.
5. **Western numerals throughout** — 0123456789, not ٠١٢٣٤٥٦٧٨٩. Not because one is better, but because these layouts carry both scripts at once and **mixing numeral systems inside one design reads as a mistake.** One rule, applied everywhere, removes a decision that otherwise gets made differently by every designer.
6. **Never stretch, skew or condense a wordmark.** The perspective on the mockups is the pack shape in a 3D render, not a distortion applied to the logo.

## 7. Type on colour

The contrast work is computed in [[Colour System]] §8, and it produced a result that inverts the category instinct:

> **Ink `#141414` is the default type colour on a flavour field. White is the exception, and it gets checked.**

White type fails on 11 of the 18 masters. It is genuinely correct on only four fields: BeBo Cola, AlRawy Cocktail, AlRawy Peach and POLEKA's Deep Purple.

**Bright Pink `#EC008C` always carries a keyline.** White gives 4.2:1 and ink gives 4.3:1, so neither is comfortable, and it is the most-used colour across 2MAN and POLEKA.

**The keyline is a legibility device, not decoration** — the same one holding the BeBo wordmark together on its own apple pack, where the banner sits at 1.30:1 against the field.

## 8. Still open

- **Vector logo files.** §1 cannot be verified against real artwork until they arrive, and every visual deliverable in both stages waits on them.
- **Licence confirmation** on the Plex family, §2.

---

**Related:** [[Alex Foods]] · [[Colour System]] · [[Colour and Type Kit]] · [[Brand Voice Guide]] · [[Foundation Roadmap]] · [[Brand Book Spec]]
