---
status: active
project: tsa
type: reference
---
# Brand and Social Kit — Alex Foods

**Foundation deliverable 3 in kit form**, for [[Alex Foods]]. Six A4 pages: identity, architecture, the social setup, the rules, and the post and story templates. Built 18 September 2026 from `design-system/kit.py`, shipped as `Alex Foods - Brand and Social Kit v1.0.pdf`.

> **STATUS: BUILT AND RENDERED, pending Aly's read.** Every page was rendered and looked at. Two things it deliberately does not contain are named in §6.

---

## 1. What this is, and why it is not the Design System

Two documents, two jobs, and they are deliberately different objects.

| | [[Colour System]] / Design System v1.1 | **This kit** |
|---|---|---|
| **Job** | Governance. The system of record a designer looks things up in. | Application. The thing someone actually builds a post from. |
| **Ground** | Cold White, TSA's document ground | **Alex Navy. The client's own colours carry the page.** |
| **Governed by** | [[TSA Brand System]] §6 — TSA's system owns the document | Alex Foods' system, because this is the client's asset kit |
| **Printed?** | Yes, on an office A4 printer | No. Screen and phone. |

**The call, and it is a departure worth naming: [[TSA Brand System]] §6 says TSA's system owns a client deliverable's page furniture.** That rule was written for a governance document a client signs. **A kit whose entire content is Alex Foods post templates cannot be dressed in TSA's navy without lying about what it shows** — every frame in it is a mock Alex Foods post, and §6's own carve-out 1 already says client colour appearing as content is not drift. So the client's system carries this document and **TSA's mark stays in the sign-off block on page 6**, which is where authorship belongs.

Aly asked for TSA's kit layout in Alex Foods' colours on 18 September. This is that, and the departure is recorded here rather than left for a future session to trip over.

## 2. The colour mapping — computed, not eyeballed

TSA's own relationships were measured and matched one for one, so the kit carries the same structure in the client's palette.

| Role | TSA | Alex Foods | Check |
|---|---|---|---|
| Ground | Precision Navy `#0A0F1E` | **`#05004B`** | Paper reads **17.86:1** (TSA's: 17.02:1) |
| Accent | Signal Red `#E8203A` | **System Red `#E1251D`** | **4.05:1** on ground (TSA's: 4.27:1) |
| Type / light ground | Cold White `#F0F2F5` | **Paper `#FAF8F3`** | — |
| Cards and panels | Surface Navy `#1A2340` | **Alex Surface `#221E5F`** | ΔE **7.57** from ground (TSA's: 8.71) |
| Display face | Barlow Condensed 800 | **IBM Plex Sans Arabic 700** | Barlow is Latin-only and it is *TSA's* face |
| Text face | Inter | **IBM Plex Sans 400** | — |

> **The ground is `#05004B`, not Alex Navy `#0A0378`, and that is not a compromise.** `#05004B` is the seal ring's own dark gradient stop, already recorded in [[Alex Foods Brands]]. Alex Navy at full strength across six pages is too hot, and a value sampled from the artwork beats an invented tint. **Alex Navy is still the master's value** — it is the profile-picture circle, the first swatch, and the master post template.

> **Red is a headline colour on this ground, never body copy.** 4.05:1 clears 3:1 for display and misses 4.5:1 for body. The kit obeys this on its own pages: the red statement panel on page 1 carries display type only, and the explanatory note sits below it on the ground.

## 3. What the six pages carry

1. **Identity** — master lockup, the four range marks as artwork, the four document colours, the type specimen, and the client's own market line «طعم أحلى مع أليكس فودز».
2. **Architecture** — before and after the umbrella decision, the four ranges as numbered pillars with their flavour bars, the governing rule, and six usage rules.
3. **Social** — profile picture in both circles, the exact pixel sizes, and three repeatable post templates: navy is the master speaking, red is a launch, a flavour field is a product post.
4. **Rules, mix and rhythm** — ALWAYS and NEVER, the content mix, and the posting rhythm.
5. **Feed templates** — 1080 × 1350 with real draft captions, **each frame printing its own contrast verdict**, plus two defects shown rather than described.
6. **Stories and reels** — 1080 × 1920 covers, how to rebuild them in Canva, and what the kit does not do.

## 4. The two decisions that were derived here, not copied

**The content mix is not TSA's.** TSA's kit runs 40 proof / 30 authority / 20 offer / 10 brand, which is a lead-generation split for a video agency. An FMCG master brand with eighteen SKUs and four illustrated ranges needs a different one:

| Share | Pillar | Why |
|---|---|---|
| **40%** | Product · المنتج | Eighteen SKUs to rotate. The product is the hero. |
| **30%** | Character · الشخصيات | BeBo's faces, POLEKA's animals, 2MAN's boy. **The characters are already drawn and they are the cheapest content in the business.** |
| **20%** | Moment · اللحظة | The lunchbox, the hot afternoon, the family jug. The occasion, never a claim about it. |
| **10%** | Company · الشركة | Alex Foods itself. No age claim until the client confirms one. |

**Facebook is weighted higher than an agency would normally weight it.** BeBo and AlRawy talk to mothers, and in Egypt that audience is on Facebook. Copying a Reels-first split off TSA's own kit would have quietly aimed the client's spend at the wrong platform.

## 5. Where the copy came from

Every Arabic line in the kit already existed. **Nothing was invented for the layout.**

- Range captions are the draft captions from [[Brand Voice Guide]] §3–§6, written for Aly's ear.
- The master line «طعم أحلى مع أليكس فودز» is **the client's own market creative**, recorded in [[Alex Foods Brands]]. It is not a slogan proposal — slogans are deliverable 4, in [[Slogans and Song]].
- The NEVER column is [[Brand Voice Guide]] §7's never-say list. **That column is the legal shield, not styling.** TSA runs the ad account.

**Checked before shipping:** no health claims, no «طبيعي ١٠٠٪», no nutrition numbers, no price, no shop named, no company age, no POLEKA cola SKU featured, no em-dashes in outgoing Arabic.

## 6. What this kit does not do, and says so on page 6

1. **The master has no tone block.** The four ranges have register, sentence length and emoji policy. Alex Foods itself does not, and it is the account that posts. The kit uses the client's own line rather than guessing a voice. **Open in [[Active Priorities]]; needs Aly's ear.**
2. **Product photography has not arrived.** Every frame uses pack artwork, which is not the same thing. The posting-rhythm page carries `SPEC — EXECUTION PENDING CLIENT ACCESS`, because Meta admin and the Google account are also outstanding.

## 7. The build

Source is `design-system/kit.py`. It shares `colour.py`, `plex.css` and the fonts with the Design System generator — nothing is duplicated. Pack artwork is referenced from `logos-transparent/`, so the marks are placed as supplied and never reconstructed.

Build, verification method and the traps are in `design-system/README.md`. **Every page was rendered and measured against the live area before shipping**, which is how three real defects were caught: a class-name collision painting a Surface Navy square on the red panel, an Arabic caption split across an LTR span, and the `display:block` descendant trap for the third time.

---

**Related:** [[Alex Foods]] · [[Alex Foods Brands]] · [[Colour System]] · [[Brand Voice Guide]] · [[Brand Book Spec]] · [[TSA Brand System]] · [[Foundation Roadmap]]
