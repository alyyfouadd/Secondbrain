---
status: active
project: tsa
type: reference
---
# Colour System — Alex Foods

**Brand Foundation deliverable 2 of 8, part 1** for [[Alex Foods]]. The governed colour system: which values survived rationalisation, what they are named, the ramps, the neutrals, every contrast pairing tested, and the rules binding them. Built from the sample set in [[Colour and Type Kit]].

> **This is the deliverable. [[Colour and Type Kit]] is the raw observation it was built from.** There were never any codes to collect from the client. Setting them is what the 20,000 buys.
> **Every number below is computed, not eyeballed** — ΔE2000 for colour difference, WCAG 2.1 for contrast. **But the input values were sampled by eye off rendered mockups**, so the maths tells you which pairs to look at and which pairings are unsafe. It does not make an eyeballed value press-accurate. See §10.

---

## 1. What rationalisation actually found

**Thirty-one sampled values across four brands. Eighteen governed masters.** Thirteen values were duplicates or near-duplicates that nobody could have told apart.

The four brands grew separately, so the roadmap predicted near-duplicate greens and reds that were never meant to relate. That turned out to be true, and understated.

| Finding | ΔE2000 | What it means |
|---|---|---|
| **2MAN and POLEKA share four values *exactly*** — ice blue, yellow, pink, green | **0.00** | Not near-duplicates. Identical. The two brands were drawn off one palette. |
| AlRawy ribbon light `#8CC63F` vs 2MAN/POLEKA green `#8DC63F` | 0.17 | One unit apart in red. The same ink, sampled twice. |
| BeBo flash red `#E1251D` vs AlRawy accent red `#E1251B` | 0.38 | The same red. |
| AlRawy peach `#E03127` vs that same red | 1.56 | Collapses in too. |
| BeBo banner green `#1BA34C` vs POLEKA apple `#00A651` | 1.28 | Indistinguishable. |
| AlRawy guava `#009A44` vs BeBo banner green | 3.03 | Collapses. |

**The architectural consequence, and it is the biggest finding in this pass: 2MAN and POLEKA do not separate on colour at all.** Four identical values is not coincidence, it is a shared palette. Two loud, kid-facing brands sitting on one set of brights.

That is not fixable by repainting, because the packs are printed and in market, and repainting is explicitly outside this scope. **So the system formalises it instead:** there is a shared **Kids Brights** set, and the separation burden moves to where it can actually be enforced — character, layout and type. Written down, that is a governed sub-system. Left unwritten, it is an accident that gets worse every time somebody designs a post.

---

## 2. The layers

Three layers were already established in [[Colour and Type Kit]]. Building the real system added a fourth, and it exists to serve Package A. **Rewritten 18 September for the umbrella model** — layer 1 is a master, not a parent standing alongside.

1. **Master — Alex Foods.** The seal sits at the **top** of the hierarchy, not beside it. Confirmed 18 September: Alex Foods is the master brand, and BeBo, AlRawy, 2MAN and POLEKA are ranges beneath it, per [[Brand Voice Guide]] §2. Every range below is a range *of* Alex Foods.
   **Values sampled 18 Sep from the seal artwork:** ring navy ~`#0A0378` (**a nineteenth master — ΔE 10.4 from BeBo Navy, so genuinely distinct**) and inner red ~`#E00000`, which is **ΔE 3.31 from System Red `#E1251D` and collapses into it.** The master layer adds one value, not two.
   ~~The seal is a rendered 3D object with gradients and gloss, so it is placed as supplied and never reconstructed, exactly like the 2MAN and POLEKA wordmarks.~~
   > **Superseded 19 September: the real Illustrator vector arrived.** The seal is **flat** — no gradients, no gloss, CMYK, 116 paths. Never retyped or redrawn, but no longer resolution-bound. **Both sampled values below are now wrong.** See §11 and `logos-vector/README.md`.
   **Still no house palette, and the reason changed.** Under the old endorsement model there was no house palette because a parent that endorses does not repaint what it endorses. Under a master brand it is a deliberate architectural choice: **the master owns the seal and the presence; the ranges keep their four clashing palettes**, because that clash is the only thing separating them on a shelf. A master brand that repainted its ranges would destroy the differentiation it depends on. **Alex Navy governs the seal, the corporate layer and the single Alex Foods presence — never a range's packaging.**
2. **Range** — each range's own fixed colours. Never change, for any reason. *(§5 and the shipped document's per-range pages still say "brand", because that is what the contract, the client and every designer call them. The hierarchy is what changed, not the vocabulary.)*
3. **Flavour** — the field colour that owns a pack for a given SKU. Changes per product.
4. **Extended** — colours a range may use **in social layouts only, never on a pack.** This layer is new and it is not decoration. POLEKA's four SKUs use only three distinct fields, and twelve monthly graphics built from three colours look like three graphics repeated four times.

> **The rule that governs all four, now with the master in it, and still the most-broken rule in food design:**
> **The flavour colour owns the field. The range colour owns the logo. The master owns the seal, and it takes neither.**
>
> A BeBo mango pack is a mango-coloured field carrying the standard green banner. The banner does not turn orange to match the flavour, **and it does not turn navy to match Alex.**

**And the new rule rationalisation forced:**

> **A value may be shared between ranges where neither owns it as a signature. It may not be shared where one does.**

**And the rule the umbrella model retires:**

> ~~The seal appears exactly where it appears today, never added and never removed.~~ **Retired 18 September.** The absence on BeBo and POLEKA is a rollout that has not caught up, not deliberate tiering. **Printed packs stay exactly as they are. New print carries the seal on every range.**

## 3. Colours that live inside a logo are not system values

The AlRawy ribbon's deep green stop, 2MAN's four letter colours, POLEKA's gel-lettering spectrum: none of these are masters and none get published as codes.

They exist inside vector artwork that is placed as supplied and never rebuilt, exactly as [[Colour and Type Kit]] §6 requires. **Publishing them as system values invites somebody to reconstruct a logo out of swatches**, which is precisely the failure that section exists to prevent.

---

## 4. The master set — 18 values

Contrast is measured against pure white and against Ink `#141414`. **"pass"** clears WCAG AA for body text at 4.5:1. **"headline"** clears 3:1, so it is safe at large display sizes only. **"fail"** is not usable for type at any size without a keyline.

| Name | HEX | RGB | CMYK *(conversion)* | White text | Ink text |
|---|---|---|---|---|---|
| **Brand Green** | `#1BA34C` | 27 163 76 | 83 0 53 36 | 3.3:1 headline | 5.6:1 pass |
| **Deep Green** | `#2C8C3B` | 44 140 59 | 69 0 58 45 | 4.3:1 headline | 4.3:1 headline |
| **Leaf Green** | `#8DC63F` | 141 198 63 | 29 0 68 22 | 2.0:1 **fail** | 9.0:1 pass |
| **Lime** | `#C6D42E` | 198 212 46 | 7 0 78 17 | 1.6:1 **fail** | 11.3:1 pass |
| **BeBo Navy** | `#1E2A6B` | 30 42 107 | 72 61 0 58 | 13.1:1 pass | 1.4:1 **fail** |
| **AlRawy Navy** | `#1B4F9C` | 27 79 156 | 83 49 0 39 | 7.9:1 pass | 2.3:1 **fail** |
| **Cola Blue** | `#1C74BC` | 28 116 188 | 85 38 0 26 | 4.9:1 pass | 3.7:1 headline |
| **Ice Blue** | `#29ABE2` | 41 171 226 | 82 24 0 11 | 2.6:1 **fail** | 7.0:1 pass |
| **Nectar Blue** | `#00A3E0` | 0 163 224 | 100 27 0 12 | 2.9:1 **fail** | 6.4:1 pass |
| **System Red** | `#E1251D` | 225 37 29 | 0 84 87 12 | 4.7:1 pass | 3.9:1 headline |
| **Peach Orange** | `#E4762A` | 228 118 42 | 0 48 82 11 | 3.0:1 headline | 6.1:1 pass |
| **Mango Orange** | `#F07F13` | 240 127 19 | 0 47 92 6 | 2.7:1 **fail** | 6.8:1 pass |
| **Golden Yellow** | `#F2A00C` | 242 160 12 | 0 34 95 5 | 2.1:1 **fail** | 8.6:1 pass |
| **Bright Yellow** | `#FFC20E` | 255 194 14 | 0 24 95 0 | 1.6:1 **fail** | 11.4:1 pass |
| **Acid Yellow** | `#FFF200` | 255 242 0 | 0 5 100 0 | 1.2:1 **fail** | 15.7:1 pass |
| **Bright Pink** | `#EC008C` | 236 0 140 | 0 100 41 7 | 4.2:1 headline | 4.3:1 headline |
| **Deep Magenta** | `#D6006E` | 214 0 110 | 0 100 49 16 | 5.1:1 pass | 3.6:1 headline |
| **Deep Purple** | `#92278F` | 146 39 143 | 0 73 2 43 | 7.2:1 pass | 2.6:1 **fail** |

> **Two governed exceptions, both deliberate:**
> **Peach Orange vs Mango Orange, ΔE 4.93.** Tight. They stay separate because they belong to different brands that never share a surface. Within one brand this gap would be forbidden.
> **Ice Blue vs Nectar Blue, ΔE 2.74.** Tighter still, and this one nearly caused a mistake worth recording. The instinct was to move AlRawy's apple field off 2MAN's signature blue. **That would have been repainting a printed pack, which is outside this scope.** The real fix is governance: 2MAN owns Ice Blue as a *brand* colour, AlRawy's Nectar Blue is a *flavour field* on one SKU. Different layers, so no collision, provided AlRawy never uses that blue as a brand element and the two brands never share a layout. Rule, not repaint.

## 5. Which brand owns what

Every colour on every pack, mapped to a master. **If a colour is not in this table, it is not in the system**, and anything using it is off-brand.

### BeBo
| Role | Master | HEX |
|---|---|---|
| Banner green *(logo pillow, never recoloured)* | Brand Green | `#1BA34C` |
| Wordmark keyline *(non-negotiable, see §9)* | BeBo Navy | `#1E2A6B` |
| "NEW" flash only | System Red | `#E1251D` |
| Peach · خوخ | Peach Orange | `#E4762A` |
| Mango · مانجو | Golden Yellow | `#F2A00C` |
| Apple · تفاح | Deep Green | `#2C8C3B` |
| Cola · كولا | Cola Blue | `#1C74BC` |
| Pineapple · أناناس | Lime | `#C6D42E` |

### AlRawy
| Role | Master | HEX |
|---|---|---|
| Wordmark | AlRawy Navy | `#1B4F9C` |
| The "y" only, never extended | System Red | `#E1251D` |
| Ribbon swoosh | Leaf Green | `#8DC63F` |
| Cocktail · كوكتيل | Deep Magenta | `#D6006E` |
| Apple · تفاح | Nectar Blue | `#00A3E0` |
| Guava · جوافة | Brand Green | `#1BA34C` *(collapsed from `#009A44`)* |
| Peach · خوخ | System Red | `#E1251D` *(collapsed from `#E03127`)* |
| Mango · مانجو | Mango Orange | `#F07F13` |

### 2MAN
| Role | Master | HEX |
|---|---|---|
| Home colour, the brand's whole world | Ice Blue | `#29ABE2` |
| Colourway: blue | Ice Blue | `#29ABE2` |
| Colourway: red | System Red | `#E1251D` |
| Colourway: green | Leaf Green | `#8DC63F` |
| Colourway: orange | Mango Orange | `#F07F13` |
| Extended, social only | Bright Yellow · Bright Pink | `#FFC20E` · `#EC008C` |

*Wordmark letter colours live inside the artwork and are not system values. See §3.*

### POLEKA
| Role | Master | HEX |
|---|---|---|
| Apple · التفاح *(caterpillar)* | Brand Green | `#1BA34C` *(collapsed from `#00A651`)* |
| Mango · المانجو *(lion)* | Acid Yellow | `#FFF200` |
| Cola *(no character)* | Bright Pink | `#EC008C` **← see §9.2** |
| Strawberry · الفراولة *(giraffe)* | Bright Pink | `#EC008C` **← see §9.2** |
| Extended, social only | Deep Purple · Ice Blue · Bright Yellow | `#92278F` · `#29ABE2` · `#FFC20E` |

*The gel wordmark's full spectrum lives inside the artwork and is not a system value.*

> **The Kids Brights set**, shared by 2MAN and POLEKA because the packs already share it: Ice Blue, Bright Yellow, Bright Pink, Leaf Green. **Neither brand owns any of the four.** 2MAN owns Ice Blue only as its *home* colour, which is a usage claim and not an exclusive one. Separation between these two brands is carried by character, layout and type, never by colour, because colour cannot carry it.

## 6. The ramps

Each master gets tints toward paper and shades toward ink, so a designer has a usable range instead of one flat swatch. **One flat swatch is what forces off-system colour picking**, which is how a palette dies.

500 is the master and the only value that appears on a pack. 100 and 300 are backgrounds and fills. 700 and 900 are type, borders and depth.

| Master | 100 | 300 | 500 | 700 | 900 |
|---|---|---|---|---|---|
| **Brand Green** | `#BCE0C4` | `#6BC288` | `#1BA34C` | `#197E3D` | `#17592F` |
| **Deep Green** | `#C0DABF` | `#76B37D` | `#2C8C3B` | `#266D31` | `#204E27` |
| **Leaf Green** | `#DBEAC1` | `#B4D880` | `#8DC63F` | `#6E9834` | `#4E6929` |
| **Lime** | `#EBEEBC` | `#D9E175` | `#C6D42E` | `#98A227` | `#697020` |
| **BeBo Navy** | `#BCBECD` | `#6D749C` | `#1E2A6B` | `#1B2454` | `#191F3E` |
| **AlRawy Navy** | `#BCC9DB` | `#6B8CBB` | `#1B4F9C` | `#194079` | `#173055` |
| **Cola Blue** | `#BCD3E4` | `#6CA4D0` | `#1C74BC` | `#1A5B90` | `#184265` |
| **Ice Blue** | `#BFE2EE` | `#74C7E8` | `#29ABE2` | `#2484AC` | `#1E5C77` |
| **Nectar Blue** | `#B4E0EE` | `#5AC2E7` | `#00A3E0` | `#057EAB` | `#0A5976` |
| **System Red** | `#F3BDB7` | `#EA716A` | `#E1251D` | `#AC211B` | `#761C18` |
| **Peach Orange** | `#F4D4BB` | `#ECA572` | `#E4762A` | `#AE5D24` | `#78431F` |
| **Mango Orange** | `#F7D6B4` | `#F4AB64` | `#F07F13` | `#B76313` | `#7E4714` |
| **Golden Yellow** | `#F8DFB2` | `#F5C05F` | `#F2A00C` | `#B87C0E` | `#7F5710` |
| **Bright Yellow** | `#FBE9B3` | `#FDD560` | `#FFC20E` | `#C29510` | `#856811` |
| **Acid Yellow** | `#FBF6AF` | `#FDF457` | `#FFF200` | `#C2B805` | `#857F0A` |
| **Bright Pink** | `#F6B3D6` | `#F159B1` | `#EC008C` | `#B4056D` | `#7C0A4E` |
| **Deep Magenta** | `#F0B3CE` | `#E3599E` | `#D6006E` | `#A40557` | `#710A3F` |
| **Deep Purple** | `#DDBDD7` | `#B772B3` | `#92278F` | `#71226F` | `#501D4F` |

*Mixed in sRGB toward paper and toward ink rather than toward pure white and pure black. Pure-black shades go muddy and dead; ink-mixed shades keep the hue alive.*

## 7. The neutrals

**The layer all four brands share and none of them currently have.** This is where a house layer can exist without flattening the brands, and it is what the brand book, the templates, the calendar and every document are built from.

| Name | HEX | On Paper | Use |
|---|---|---|---|
| **Paper** | `#FAF8F3` | — | Every background. Never pure white, which glares on screen and looks cheap in print. |
| **Mist** | `#EDEAE3` | 1.13:1 | Panel fills, table stripes. Never type. |
| **Silver** | `#C9C5BC` | 1.62:1 | Rules, dividers, disabled states. Never type. |
| **Slate** | `#8A8681` | 3.41:1 | Captions at display size only. **Not body text.** |
| **Graphite** | `#4A4742` | 8.71:1 | Secondary body text. |
| **Ink** | `#141414` | **17.36:1** | Primary text everywhere. |

## 8. Contrast, and the finding that inverts the obvious

Every text-on-field pairing was tested. The result is not what food design assumes.

**White type fails on 11 of the 18 masters. Ink passes on 12.**

The instinct in this category is white type on a bright field, and on this palette it is wrong more often than it is right. Half these fields are pale yellow, lime and acid yellow, where white is invisible: Acid Yellow gives white **1.2:1**, against **15.7:1** for ink.

> **So the default flips: Ink is the default type colour on a flavour field, and white is the exception that has to be checked.**

**White is genuinely correct on only four:** BeBo Cola, AlRawy Cocktail, AlRawy Peach and POLEKA's Deep Purple.

**Bright Pink `#EC008C` is the trap.** White gives 4.2:1, ink gives 4.3:1. Both marginal, neither comfortable. **That field always carries a keyline**, and it is 2MAN's and POLEKA's most-used colour.

That is also the arithmetic behind the rule already in [[Colour and Type Kit]]: white type on a flavour field carries a dark keyline. **The keyline is a legibility device, not decoration**, and now there is a number proving it rather than an assertion.

## 9. Three defects found in the packaging

Naming these is the job. Fixing the printed packs is not, and is a clause 7 quote if the client wants it.

**1. BeBo's green banner nearly disappears on BeBo's own apple pack.**
Banner `#1BA34C` on the apple field `#2C8C3B`: **ΔE 7.62, contrast 1.30:1.** Every other BeBo flavour puts the banner 27 to 54 ΔE clear of its field. Apple is the one SKU where the brand's own logo pillow sits on a near-identical green and is held together only by the navy keyline.
**That is why the navy keyline is non-negotiable**, and the system now says so with the number attached. **Rule: the BeBo banner never appears on any green without its keyline, at any size, in any medium.**

**2. POLEKA's cola and strawberry are the same pack colour.** Both `#EC008C`, ΔE 0.00. **Checked against `mockup-poleka.png` rather than assumed:** the cola pouch and the strawberry pouch are the same magenta, differentiated only by the character and the bottle image. At thumbnail size in a feed they are one product.
Repainting is out of scope, so the rule does the work: **cola and strawberry never appear in the same grid, carousel or story sequence, and the character always leads the frame.**

**3. The trademark exposure is worse than previously recorded, and I looked at the pack to be sure.** The POLEKA cola pouch does not merely carry an imitative wordmark. It shows a **photoreal contour bottle in red-and-white livery with "Cola Cola" set in near-identical Spencerian script.** The bottle silhouette is itself protected trade dress in most jurisdictions, independent of the wordmark.
Under Package A, **TSA's own ad account pushes this to a paid audience.** Until the client confirms rights in writing, that SKU stays out of paid campaigns and out of copy. See [[Alex Foods Brands]].

## 10. What would make this press-accurate

The values are computed honestly from sampled inputs. Two limits, stated plainly rather than buried:

1. **The inputs were sampled by eye off rendered mockups**, not measured off printed packs or read from source artwork. The relationships between values are sound and the contrast verdicts hold, because those depend on the values as published from here on. **What is not guaranteed is that a published value matches the ink currently on a shelf.**
2. **The CMYK column is an unmanaged conversion**, not a press specification. It is a starting point for a printer, not an instruction to one. A real press spec needs the printer's profile and stock, and a proof.

**Neither blocks the Foundation.** From the moment this system is approved, these values *are* the brand's colours and the packs are the legacy. That is the correct direction for a system nobody had written down before. The one thing worth doing cheaply: if the client ever produces the original artwork files, re-sample from those and re-issue as v1.1.

---

## 10b. Exact collisions across layers — computed 19 September 2026

**§9 records the near-collisions, measured in ΔE. This section records the five places where two things are the *same hex value*.** Found by computing the whole palette against itself while building book §12, and **none of them had been written down.**

| Value | What shares it |
|---|---|
| `#1BA34C` | **BeBo range signature** · AlRawy guava field · POLEKA apple field |
| `#EC008C` | **POLEKA range signature** · POLEKA cola field · POLEKA strawberry field |
| `#29ABE2` | **2MAN range signature** · 2MAN blue field |
| `#E1251D` | AlRawy peach field · 2MAN red field |
| `#F07F13` | AlRawy mango field · 2MAN orange field |

**They are not defects.** The packs are printed and in market and nothing here is being repainted. **They become defects the moment a layout is built without knowing about them**, which is precisely what had been about to happen.

**The five rules that resolve them**, governed in book §12:

1. **The pack identifies the SKU, never the field.** A field colour is a stage, not a name. **That is why a field may be reused and a pack may not.**
2. **Two ranges never share one layout.** AlRawy peach and 2MAN red are the same red; side by side they read as one product line, and apart nobody will ever know. *(Same shape as the Ice Blue versus Nectar Blue rule in §9: governance, not repaint.)*
3. **`#1BA34C` is a brand element on BeBo only.** On AlRawy and POLEKA it is a stage, never a badge, a border or a logo ground.
4. **POLEKA has four SKUs but only three distinct fields, and two of them are the brand colour.** Four posts built straight off the flavour map show three colours, one of them twice. **This is what the extended layer exists for, and on POLEKA it is not optional.**
5. **2MAN's signature is its own blue field**, so on that SKU the brand layer and the flavour layer are the same colour. There the mark carries the brand by shape, and the field carries nothing.

### And the type verdict, computed across all 18 fields

**Ink wins on 11 of 18. White on 4. Three clear 4.5 with neither.**

| Verdict | Fields |
|---|---|
| **INK** (11) | BeBo peach, mango, pineapple · AlRawy apple, guava, mango · 2MAN blue, green, orange · POLEKA apple, mango |
| **WHITE** (4) | BeBo cola · AlRawy cocktail, peach · 2MAN red |
| **KEYLINE REQUIRED** (3) | **BeBo apple** `4.32 / 4.27` · **POLEKA cola** `4.34 / 4.25` · **POLEKA strawberry** `4.34 / 4.25` |

**Those three carry a dark keyline behind the type, always.** The keyline is a legibility device rather than decoration: not added because it looks good, not dropped because a designer prefers it without, added when the number says it is needed.

## 11. Still open

- ~~**Vector logo files.** Blocks §3 being verified against real artwork, and blocks every visual deliverable in both stages.~~ **Closed 18 September.** No source files exist; all four marks are cut out on transparency in `logos-transparent/`. §3's rule — colours inside a logo are not system values — stands on its own and never needed vector to be true. Vector returns only if print enters scope under clause 7.
- ~~**The seal's rule** — tiering or rollout.~~ **Closed 18 September: rollout**, and the freeze rule retired with it. See §2.
- ~~**Alex Navy `#0A0378` is a governed master with no ramp and no contrast row.**~~ **Superseded 19 September 2026 — and the problem is the value, not the ramp.**

### §11 rewritten: the master layer's real values

The client sent true Illustrator vector of the seal on 19 September. **The 19th master was sampled off a gradient-rendered raster and it is wrong.**

| | Sampled off the raster | **Authored in the client's file** | Error |
|---|---|---|---|
| Ring | `#0A0378` | **CMYK 98 / 81.3 / 27 / 12.9** ≈ `#042AA2` | **ΔE2000 9.80** |
| Ring gradient dark | `#05004B` | *does not exist* — a gradient stop of a rendering | ΔE2000 15.38 |
| Ring gradient light | `#110691` | *does not exist* | ΔE2000 7.37 |
| Inner disc | `#E00000` | **CMYK 7.4 / 93.8 / 83.6 / 0.8** ≈ `#EA1029` | ΔE2000 6.44 |

**The CMYK column is authoritative** — it is what the designer typed. Any sRGB here is a naive profile-free conversion and is a working approximation, exactly as this system already flags its own CMYK as conversions in the other direction.

**Three consequences, and the second one is a governance decision rather than arithmetic:**

1. **The disc red still collapses into System Red** (ΔE2000 3.19 to AlRawy peach, 3.69 to BeBo flash red). The earlier finding holds. The master layer still adds **one** value, not two.
2. **The real ring blue collapses into 2MAN blue `#2E3192` at ΔE2000 3.77** — under this system's own 5.0 threshold. So on the maths the master's blue and a range's blue are one colour. **They should almost certainly stay separate anyway**, because a master brand sharing its only colour with one of its four ranges destroys the hierarchy §2 exists to state. **Aly's call, and it needs stating in the book either way.**
3. **`#05004B` was never a brand colour.** It is a gradient stop of a picture. It currently carries the hero panels and the sign-off block in the shipped Brand and Social Kit, justified in that note as "the seal ring's own dark gradient stop." **That justification is dead.** See [[Brand and Social Kit]] §2.

### And the placement rule the vector makes computable

Contrast of the seal's own ring against its ground:

| Ground | Ring | Disc | |
|---|---|---|---|
| Paper `#FAF8F3` | **10.65:1** | 4.30:1 | **correct** |
| White `#FFFFFF` | **11.30:1** | 4.56:1 | **correct** |
| Alex Navy `#0A0378` | **1.43:1** | 3.55:1 | ring vanishes |
| `#05004B` | **1.68:1** | 4.16:1 | ring vanishes |
| System Red `#E1251D` | 2.41:1 | **1.03:1** | disc vanishes |
| BeBo green `#1BA34C` | 3.44:1 | 1.39:1 | fails |

> **The rule: the seal goes on white or Paper, and on nothing else.** It carries its own ring and its own disc, so it needs a light ground to have an edge at all. **This is a live defect in a shipped deliverable** — `design-system/kit.py` places the seal on `#05004B` labelled "ON NAVY — DEFAULT" and makes the profile picture the seal on Alex Navy. Confirmed by eye as well as by ratio.
- **Type system**, the other half of deliverable 2. Next in Phase 1 of [[Foundation Roadmap]].

**Up:** [[Alex Foods Brands]] · [[Alex Foods]]
