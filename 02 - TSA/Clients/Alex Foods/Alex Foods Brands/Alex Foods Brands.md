---
status: active
project: tsa
type: index
---
# Alex Foods Brands

What [[Alex Foods]] actually sells, read off the packaging mockups the client sent on **18 September 2026**. This is the index for this folder and the working inventory the Foundation is built from.

**Everything below is read off rendered mockup images, not from a brand manual.** Colours are eyeballed and marked as such. Nothing here is confirmed by the client yet.

---

## Notes in this folder
- [[Foundation Roadmap]] — the sequenced build plan for all 8 Foundation deliverables: order, dependencies, what needs a designer and what the client still owes. **Read this first.**
- [[Colour and Type Kit]] — the sample set feeding Foundation deliverable 2: every colour read off the four packs, the type audit, and the usage rules that hold four brands apart. Values are eyeballed from these mockups **and that is the intended state** — there are no codes to wait for, because setting them is the deliverable.
- **`Alex Foods - Brand Foundation v1.0.pdf` — THE BOOK. 39 pages, 25 sections, bilingual, 8.26 MB.** Rebuilt 20 September from `design-system/book.py`, which is the single source for every section's content. **21 sections DEFINED and complete; 4 carry an honest waiting chip naming what they wait on and who from** — §10 slogans, §14 social setup, §19 Google, §20 local SEO. **§17 and §18 closed on 20 Sep** from [[Content Plan]]. Still v1.0 because the book has not shipped once: this is the current build of the 9 October delivery, not a revision of something the client holds. This is the only document the client receives. See [[Brand Book Spec]] §5c.
- `Alex Foods - Design System v1.1.pdf` — **RETIRED AS A DELIVERABLE 19 September: folded into the one book as §04–06.** Kept as the built source of the colour and type content, not as something the client receives. See [[Brand Book Spec]] §5b. *(Was: the shipped deliverable 2,* 19 pages, A4, generated from `design-system/`. Colour and type in one governed document, with the sign-off page. **v1.1, 18 Sep: section 1 rebuilt as a master-brand hierarchy** after Alex Foods was confirmed as the master brand. No colour value, ramp or contrast verdict changed. *(v1.0 was superseded the same day and removed — it was never sent for approval, and two Design System PDFs in one folder is how the wrong file gets handed over. Git history retains it.)*
- `Alex Foods - Brand and Social Kit v1.2.pdf` — **RETIRED AS A DELIVERABLE 19 September: folded into the one book** as §07 and §11–14, and it carries four known page-4 defects that die in the rewrite. Never goes to the client. See [[Brand and Social Kit]] §3b–3c. *(Was: Foundation deliverable 3 in kit form,* 8 pages, A4, bilingual. **TSA's own kit rebuilt section for section for Alex Foods**, plus two range pages the TSA kit has no equivalent of. Identity, positioning and pillars, **every range with its own colours, format and identity**, profile and exact sizes, post templates, the rules, content mix, posting rhythm, and the product and story frames carrying **real pack artwork**. **Paper ground**, client's own neutrals. Written up in [[Brand and Social Kit]].
- `packshots/` — **the client's own product mockups for all four ranges**, received 19 Sep, cropped and keyed to transparency, with individual packs sliced out in `packshots/single/`. See its README.
- [[Brand and Social Kit]] — the slot-for-slot map against TSA's kit, the measured colour layer, why the pillars are observable facts rather than claims, why the content mix is not TSA's, where every Arabic line came from, and the two things the kit deliberately does not do.
- `design-system/` — the build for the PDFs: the colour maths, the two generators (`gen.py` for the Design System, `kit.py` for the kit), the fonts, and the traps worth not rediscovering. See its README.
- [[Colour System]] — Foundation deliverable 2, part 1. **The governed system**: 31 sampled values rationalised to 18 masters, ramps, neutrals, every contrast pairing computed, the SKU map, and the three packaging defects the maths exposed.
- [[Type System]] — Foundation deliverable 2, part 2. Wordmarks as artwork, the Plex family and why, weights, print and social scales, and the bilingual rules.
- [[Brand Voice Guide]] — Foundation deliverable 1, drafted. One voice and four tones beneath one master, the words each range uses and avoids, sentence length and emoji policy per range, the never-say list that keeps a food page out of trouble, and the full comment-reply procedure including the complaint script. **§2 rebuilt 18 Sep on the umbrella model.** One block outstanding: Alex Foods' own tone, which needs Aly's ear.
- `Alex Foods - Shooting and Compositing Recipe v1.0.pdf` — **the shipped deliverable 6**, 7 pages, A4, bilingual, 0.61 MB, built from `design-system/recipe.py`. **The first Foundation deliverable that is finished rather than pending.**
- [[Shooting and Compositing Recipe]] — **Foundation deliverable 6, COMPLETE and RENDERED.** Book section 16, and the one that ships early and alone because every visual asset in both stages is produced against it. Bilingual throughout, Arabic leading. Carries the one rule (**the scene is generated, the product never is**), the eight camera and light constants that make eighteen SKUs read as one family, a scene world per range, four ready prompts, the seven compositing rules, a ten item reject list, the visual claims ban, output specs and a pre publish checklist.
- [[Giveaway Programme]] — **how the client's giveaways actually work**, and they already do. **Two mechanics already in the packaging** — a coupon in the carton for retailers, a QR code on the back of the pack for consumers. **Three campaigns, ranked by the client himself:** school gifts running now and urgent, bicycles and scooters running long-term, the Umrah trade programme paused. **Carries the commercial problem the school deadline creates.** **§11, added 21 September, is the month-1 school campaign planned and ready to announce** — the launch order (mechanic before prize), drafted announcement copy, the correction that confirmed the QR as the entry route, and the one missing asset that can actually stop the launch.
- [[Content Plan]] — **book sections 17 and 18, and the answer to what to post, why, and what it looks like.** Written 20 Sep, once enough was known to write it honestly. **The spine is the three campaigns, not a four-range rotation**: school gifts racing a deadline, bicycles and scooters running continuously, Umrah paused. Carries the four jobs every post has to do and **explicitly replaces the 40/30/20/10 mix in [[Brand and Social Kit]]**, which was derived from packaging before anyone knew there was a live giveaway programme. Seven post archetypes, each with why it exists, what is fixed, what changes and what is never done. Month 1 costed against the 20 assets Package A actually funds, and **the two animations assigned on purpose** — the mechanic explainer and the school moment, not a product film.
- [[Package A Month 1]] — **how the first paid month actually gets produced**: why month 1 should *be* the school campaign, the twenty deliverables, the render rail proven on 19 September, the pack-resolution audit that found the real blocker, the consolidated client ask, and the commercial terms nobody has defined yet.
- [[Month 1 Asset Brief]] — **the twenty month-1 assets specified to the point a supplier builds one without asking a question.** Written 20 Sep, because Aly directs and two suppliers execute, which makes the brief the deliverable. Carries the standing spec stated once — sizes, safe areas, motion lengths, the seal rule, the computed type-colour rule, the filename convention — then all twenty rows with range, SKU, field colour by name, copy and a deadline relative to campaign go-live. **Also the month-1 posting calendar** — every asset dated against campaign go-live with its platform, which is Package A's contracted content calendar — **the production split at Mahmoud's agreed rates, and the assets that are blocked with exactly what each one waits on.** **It supersedes [[Content Plan]] §5's allocation**, having found that §5 and [[Post Archetypes]] §3 split the same twenty two different ways.
- [[Slogans and Song]] — Foundation deliverable 4. Why a slogan is not a headline, who each brand is actually talking to, the feeling behind each of the four, the six tests a line has to pass, and why the giveaway song plays by campaign rules instead.
- [[Brand Book Spec]] — the design and production specification for the PDF the whole Foundation ships inside: format, grid, type, bilingual handling, page-by-page architecture, and how it gets built and rendered from an iPad.
- `mockup-bebo.png` · `mockup-poleka.png` · `mockup-alrawy.png` · `mockup-2man-a.png` · `mockup-2man-b.png` — the packaging the client sent on 18 September, screen-resolution.
- `packs-bebo-transparent.png` · `packs-poleka-transparent.png` — **the most usable artwork received so far.** The full BeBo and POLEKA ranges at high resolution **on a transparent background**, extracted 18 Sep from a Canva mockup PDF. Cut out and ready to composite onto any layout, which is exactly what the monthly graphics need. Still raster.
- **`logos-vector/alex-seal-master.pdf` — THE VECTOR MASTER, received 19 September.** True vector, no images and no fonts. **The flat two-colour seal**, not the 3D rendered object. `alex-seal-master.svg` beside it is a working conversion for HTML layouts, **carrying one known defect: the x of "Alex" does not survive the conversion, so the PDF is the master and the SVG is checked before use.**
- `logo-alex-seal.jpg` — the **3D rendered** master seal with the Egyptian flag ribbon. Superseded as a source by the vector above; kept because it is what is currently printed on pack, and **it is the only evidence of the ribbon version — which version governs is still open.**
- [[client-social-copy]] — the client's own published captions, transcribed. **The first primary source on how Alex Foods actually speaks**, and the note every voice decision is checked against.
- `client-legacy-creative/` — two of the client's own existing graphics, kept as the "before" reference: what Alex Foods currently looks like in market, which is what the system is replacing. Useful for the voice guide and for the do-not pages.
- `logo-alrawy-screencap.png` · `logo-2man-screencap.png` · `logo-bebo-screencap.png` · `logo-poleka-screencap.png` — **all four brand marks**, isolated on white, **received 18 September as iPad screenshots of files open in the Files app.** Far better than reading a mark off a pack: clean edges, no perspective, full colour. **Still not vector.** They are screen captures, so they do not close material #2 and they cannot be used for print or at large scale. **What they do prove is that the source files exist and are on the client's device**, which turns the chase from "do these exist?" into "send the file, not a picture of it."


---

## The headline problem: four brands arrived, the contract names three

The Service Scope V2 says the Brand Voice Guide covers "one brand voice, a different tone per family: **BeBo, AlRawy, Freeze Pops**." What the client actually sent is **four** brands:

| Brand | What it is | In the contract? |
|---|---|---|
| **BeBo** | Powdered drink sachets, "Kids Zone" sub-mark | Yes, named |
| **AlRawy** | **Ready-to-drink** nectar pouches, straw on the pack | Yes, named |
| **2MAN** | Ice pops — **two live lines**, ICE POPS and Bu:Zz/Meyveli | Yes — the "Freeze Pops" family, under its actual brand name |
| **POLEKA** | Jelly candy in bottle-shaped pouches | **Not named in the scope. Confirmed verbally as in, 18 Sep 2026.** |

**POLEKA is in, by Aly's decision on 18 September 2026** — a fourth brand inside the Foundation at no change to fee. The work proceeds on that basis. **It still needs papering:** clause 4 lets the client reject anything not matching the *approved* foundation guide, and the signed document does not mention this brand, so a one-line written confirmation closes a gap that costs nothing to close now.

**And the SKU count moved.** The contract asks for "5 SKU names." Roughly **eighteen** arrived across the four brands. If the 12 monthly graphics were priced against five SKUs, they are now being spread across nearly four times that. Worth knowing before month one, not after.

---

## BeBo — **juice**

> **SETTLED 20 September from the client's own page: BeBo is a juice and you drink it.** «عصير بيبو» · «اشرب بيبو». **TSA's *powdered drink sachets* was read off a pack graphic and was wrong for three days.**

## BeBo — *(was: powdered drink sachets)*

> **FORMAT CONTESTED, 19 September.** The client described BeBo as *"juice in a sachet you drink directly with a straw, hand-sized package."* **That does not match this artwork.** The packs are **pillow bags**, they read «مشروب بطعم X / X Drink», their serving graphics are a **cup with a straw standing in it** (peach) and a **tall glass of cola over ice** (cola), and **none of them carries «أدخل الماصة هنا» — AlRawy prints it on every pouch.** Most likely the answer described AlRawy and applied it to both. **But "powdered" is TSA's inference too** — the word appears nowhere on the front, and a pillow bag could hold a strip of sachets, which would reconcile both accounts. **One photo of the back of a pack settles it.** Until then the heading below is unproven. See [[Alex Foods Discovery Brief]] §A1.

> **Also confirmed 19 September: BeBo is the client's priority range and their best seller. AlRawy is the weaker seller.**

`mockup-bebo.png`

- **Logo:** white "BeBo" wordmark, navy outline, on a green pillow-shaped banner. Arabic **بيبو** set above it in white.
- **Sub-mark:** "KIDS ZONE" lozenge in rainbow colours, bottom right of pack.
- **Character:** a winking, smiling cartoon face rendered in the flavour's own colour and liquid. The face IS the pack — it changes per flavour rather than sitting as a fixed mascot.
- **Flash:** red "NEW" corner banner, top left.
- **Bilingual:** Arabic flavour name over English, bottom of pack.
- **No Alex seal on this one.**

**5 SKUs:** Peach · Mango · Apple · Cola · Pineapple

> **BeBo is the hero product, named by the client on 19 September:** *«اهم منتج هنركز عليه في الاعلانات هو منتج البيبو»*. The advertising leads with this range. **It also collapses the SKU-spread problem below** — 12 monthly graphics across BeBo's 5 SKUs is the shape the contract was priced for, rather than spread across eighteen. **And note the tension:** BeBo is one of the two ranges with no Alex seal on the pack, so on the most-seen campaign the master brand has to be carried by the layout rather than by the product. See [[Giveaway Programme]] §4.

**Approximate colours** *(eyeballed, must be confirmed)*
| | |
|---|---|
| Logo green | ~`#1BA34C` |
| Wordmark navy | ~`#1E2A6B` |
| Peach | ~`#E4762A` |
| Mango | ~`#F2A00C` |
| Apple | ~`#2C8C3B` |
| Cola | ~`#1C74BC` with red base |
| Pineapple | ~`#C6D42E` |

---

## AlRawy — juice and nectar pouches

`mockup-alrawy.png`

- **Logo:** "AlRawy®" in navy with a **red "y"**, Arabic **الراوى** below in navy, inside a white roundel wrapped by a green leaf-and-ribbon swoosh. The most grown-up of the four marks.
- **Endorsement:** carries the **Alex** seal, bottom left of pack.
- **Format, and this was corrected on 19 September: ready to drink, not a powder to mix.** Every pouch prints `Insert Straw Here / أدخل الماصة هنا` across the top. **BeBo is the powder range; AlRawy is the juice.** Copy must never imply AlRawy needs preparing.
- **Photography-led:** real fruit photography dominates each pack, unlike the illustrated character work everywhere else.
- **Bilingual:** English "…Nectar" plus Arabic, with a weight line.
- **Registered mark** — note the ® on the logo.

**5 SKUs:** Cocktail Nectar · Apple Nectar · Guava Nectar · Peach Nectar · Mango Nectar

**Approximate colours** *(eyeballed, must be confirmed)*
| | |
|---|---|
| Wordmark navy | ~`#1B4F9C` |
| Accent red | ~`#E1251B` |
| Leaf green | ~`#5EA818` |
| Cocktail | ~`#D6006E` |
| Apple | ~`#00A3E0` |
| Guava | ~`#009A44` |
| Peach | ~`#E03127` |
| Mango | ~`#F07F13` |

---

## 2MAN — ice pops *(the contract's "Freeze Pops")*

`mockup-2man-a.png` · `mockup-2man-b.png`

**Two designs arrived and both are live products — the client sells both.**

> **NAMED AND SIMPLIFIED, 19 September.** Aly: **2MAN runs two packages — the normal one and one called «أشكال» (ashkal, "shapes") — and they are the same thing.** That settles what the vault had been treating as a governance problem. **It is not two pack architectures needing separate rules. It is one brand, one voice, one identity, in two packs.**
>
> **Note the naming gap, because it will bite whoever writes the file names:** the client calls it **ashkal** internally — the Canva export carried a screenshot of a file literally called `ashkal mucup` — but **the pack itself prints "Bu:Zz" and "Meyveli".** Internal name and printed name are different. Use *ashkal* when talking to the client and *Bu:Zz* when describing what is on the shelf.
>
> **What it changes:** the sub-brand rule gets shorter rather than longer. 2MAN is governed once. A caption still never needs to know which pack it is for, and now neither does a layout.


**Design A** (`mockup-2man-a.png`) — "ICE POPS 2MAN", a running boy character, the **Alex** seal, a "YUM" flash, and the Arabic tagline **عيش جو المغامرة** ("live the adventure"). Four colourways: blue, red, green, orange.

**Design B — «أشكال» / ashkal** (`mockup-2man-b.png`) — the second package. Prints "Bu:Zz" and "Meyveli" (Turkish for "fruity"), different characters, different layout, four flavours including a cola. **Same brand, same voice, same identity as the normal pack**, by the client's own account.

- **Logo (shared):** "2MAN" in dripping ice-cream letters — yellow 2, pink M, green A, blue N — on a splash of water and ice cubes.
- **Tagline:** عيش جو المغامرة — the only brand of the four with a tagline already written. Worth keeping; the Slogans deliverable should build around it, not replace it.

**Approximate colours** *(eyeballed, must be confirmed)*
| | |
|---|---|
| Ice blue | ~`#29ABE2` |
| Letter yellow | ~`#FFC20E` |
| Letter pink | ~`#EC008C` |
| Letter green | ~`#8DC63F` |

---

## POLEKA — **«مشروب بطعم الفاكهة»**, sold frozen *(in the Foundation, not yet in the signed scope)*

> **FOURTH CORRECTION, 20 September, and the only one from a primary source.** The client's own post reads **«بوليكا مشروب بطعم الفاكهة»** — *POLEKA is a drink with fruit flavour.* **That is the exact construction printed on the BeBo packs**, so the client files POLEKA in the same category as BeBo. *(Earlier readings, all TSA's: chew candy, drinkable jelly, frozen juice.)*
>
> **And the market has a word for the format that TSA had never heard: «لوليتا».** The client uses it as a generic and brands with it — **«لوليتا تومان»**. Verbatim source in `client-legacy-creative/client-social-copy.md`.

> **CORRECTED AGAIN, 20 September: POLEKA is a FROZEN JUICE.** Aly: *"it's more of a frozen juice."* Not a chew candy, and not a room-temperature drinkable jelly either. **The «جيلي» on the pack describes the texture, not the category.** The scissors and the cut neck are real; what comes out of the neck is frozen or near-frozen juice.



> **CORRECTED 20 September 2026: POLEKA is a DRINKABLE jelly, not a chew candy.** Opened the packshot properly for the first time. **Every pouch carries a scissors icon and a cut line at the bottle neck** — you snip it and suck the jelly out. **The bottle shape is not decoration, it is the product idea: a sweet pretending to be a drink.** The earlier description, *jelly candy in bottle-shaped pouches*, was read off the silhouette and is what every failed POLEKA slogan was built on.



`mockup-poleka.png`

- **Logo:** "POLEKA" in fat rainbow gel letters on a cloud, with "jelly" and Arabic **جيلي كيدز** and small jelly-blob faces. The loudest, youngest mark of the four.
- **Format: a frozen juice in a stand-up pouch moulded to a bottle silhouette, with a snip-off neck.** Cut the neck and suck it out. **Not a chew candy, and not a shelf-stable jelly.** Each pouch is wrapped in a full-bleed animal — caterpillar (apple), lion (mango), a cola bottle (cola), giraffe and friends (strawberry).
- **The cola SKU is a photoreal Coca-Cola bottle rendered on a pink pouch**, with «Cola Cola» in near-identical script. The trademark flag is worse seen than described.
- **No Alex seal.**
- **4 SKUs visible:** apple (التفاح) · mango (المانجو) · cola · strawberry (الفراولة)

---

> **CORRECTED 19 September 2026: a true vector master EXISTS for the Alex Foods seal.** `LOGO.pdf` arrived from the client and it is genuine vector artwork: **zero embedded images, zero fonts, 1,612 vector path operations, CMYK fills.** Filed as `logos-vector/alex-seal-master.pdf`. **It is also the FLAT two-colour seal, not the rendered 3D object** in `logo-alex-seal.jpg` — navy ring, red disc, white type, no gradients and no gloss, which is far more usable at every size. **The standing claim that no source files exist was true of the four range marks and is now false of the master.** Nobody has sent vector for BeBo, AlRawy, 2MAN or POLEKA yet, and **the chase should restart, because this proves the client can produce vector when asked.**

## The Canva mockup, and what it proves

A file named `bebo_mucup.pdf` arrived 18 September. **It is not in this vault** — it is a 9.9 MB Canva deck whose entire value is two images, both of which were extracted and kept (see below), so committing it would bloat every clone forever for nothing. **It is not a BeBo file and it is not artwork either.** It is a one-page Canva export carrying all four brands, assembled from raster images, and taking it apart settled the vector question for good.

| What is inside | What it is |
|---|---|
| BeBo range, 3645 × 1515, with an alpha mask | High-res pack render, **transparent** — extracted and kept |
| POLEKA range, 4859 × 2020, with an alpha mask | High-res pack render, **transparent** — extracted and kept |
| AlRawy logo, 1433 × 1001 | **A screenshot.** The iOS status bar is still in the image |
| 2MAN logo, 1194 × 834 | **A screenshot of a PDF viewer**, toolbar visible, showing a file called **`ashkal mucup`** |

**No embedded fonts, and roughly 93,000 vector path operations.** That is Canva's signature: it outlines all text on export. Those paths are outlined type and layout shapes, **not logo artwork.**

So the conclusion is firm rather than cautious: **every route the artwork has taken to TSA so far has been a photograph of a file somebody had open.** The sources exist. Nobody has sent one.

> **And superseded again on 19 September, in the other direction: a real Illustrator file arrived for the master seal.** It was authored that morning, which is the likely explanation — it did not exist to send, and somebody made it. **The lesson is not "the chase was right all along."** It is that "the client has nothing" was a fact about a moment, not about the world, and the master mark is now the one asset in this project held at full quality. **The four range marks are still raster.**

**Superseded 18 Sep: there are no source files to ask for.** Aly confirmed the client has nothing but screenshots. So the chase is over, and it should have ended sooner — **the signed material list asks for "logo files, vector if available"**, which makes vector a convenience the contract already anticipated might not exist, not a condition anyone is failing.

**All four marks were cut out of the supplied raster onto transparency instead** — see `logos-transparent/`. Sufficient for every deliverable in the contract, because **nothing in the Foundation or Package A is printed.**

**What it did deliver:** the BeBo and POLEKA ranges at high resolution with real transparency, which is the most usable artwork received so far and exactly what the monthly graphics need.

## Open questions — what the client still has to answer

**This list got shorter on 18 September, and the two that left were the loud ones.** "Which 2MAN design is live" is dead — both are live, and governing both is a sub-brand rule. "Exact colour codes and font names from the designer" is dead — there is no designer and there are no codes, and building the values *is* what the Foundation was bought for. Neither was ever a gate. See [[Foundation Roadmap]].

**And "what is Alex" closed on 18 September: Alex Foods is the MASTER BRAND**, and the four are ranges beneath it. It **does** have a consumer voice and it leads — one Alex Foods presence rather than four brand pages. Still no house palette, now by architectural choice rather than endorsement etiquette: the master owns the seal and the presence, the ranges keep the four clashing palettes that separate them on a shelf. The seal's absence on BeBo and POLEKA is **a rollout that has not caught up**, not a tier. Consequences written up in [[Brand Voice Guide]] §2 and governed in [[Colour System]] §2.

One real client answer remains from the brand read, and **five more arrived with the giveaway brief on 19 September** — see [[Giveaway Programme]] §9:

1. **Do they hold the rights to the "Cola Cola" artwork?** See the trademark flag below. TSA runs the paid campaigns, so this is TSA's exposure, not just theirs.

And one chase, which is paperwork rather than a question:

2. **POLEKA in writing** — the decision is taken and it is in; this is paperwork closing a clause 4 gap.

*(Vector logo files used to sit here as item 3. **Closed 18 September** — see "Superseded 18 Sep" above. Kept out rather than struck through, because a closed material on an open-questions list is what made four other notes keep chasing it.)*

## Alex Foods — the master brand, now seen properly

`logo-alex-seal.jpg` · `client-legacy-creative/`

The seal arrived in full on 18 September and it answers more than it was asked to.

**Alex is الشركة الإسكندرية لتعبئة وتغليف المواد الغذائية** — the Alexandria Company for Food Packing and Packaging. The ring carries the name in Arabic and English, and **the icon at the top of the ring is a lighthouse**, which is the Pharos. The mark is a place as much as a company.

**Construction:** navy outer ring, red inner disc, "Alex" in white with a sun burst above and a green leaf swoosh below, wrapped in an Egyptian flag ribbon.

> **OVERTURNED 19 September 2026 — the real vector arrived.** `logos-vector/alex-seal-master.pdf`, authored in Adobe Illustrator 24.2 that morning, with the live Illustrator artwork embedded. **The seal is FLAT vector: no gradients, no gloss, no raster, no fonts, CMYK throughout.** The 3D read was true of the *picture* the client had been sending, not of the mark.
>
> **What that changes:** the seal can now be scaled to any size, placed on any ground, and printed. It is still never *retyped or redrawn* — that rule stands and always did — but "placed as supplied" no longer means "stuck at whatever resolution arrived."
>
> **And this version carries no Egyptian flag ribbon.** `logo-alex-seal.jpg` has one. **Two versions of the master mark now exist, and the Foundation has to say which one governs.** See `logos-vector/README.md`.

*Sampled off the artwork. [[Colour System]] owns the governed values these resolve to.*

| Role | Value *(sampled)* | Note |
|---|---|---|
| ~~Ring navy~~ | ~~`#0A0378`~~ | **WRONG — superseded.** Sampled off the gradient render. The authored value is **CMYK 98 / 81.3 / 27 / 12.9**, about `#042AA2`, and the sampled value is **ΔE2000 9.80** away from it |
| Inner red | ~`#E00000` | **ΔE 3.31 from System Red `#E1251D`** — the same red. It collapses rather than adding a value. |

**So the master layer adds exactly one value to [[Colour System]]: Alex Navy.** Not two.

> **Revised 19 September, and the revision is bigger than a ramp.** The value itself was wrong, not just un-ramped. **The authoritative ring blue is the client's own CMYK 98 / 81.3 / 27 / 12.9**, and `#0A0378` misses it by ΔE2000 9.80. Worse, it **collapses into 2MAN blue `#2E3192` at ΔE2000 3.77** — under the system's own 5.0 rule — so the master's blue and a range's blue are arguably one colour. That is a governance decision, not a maths error, and it is Aly's. The disc red holds: it still collapses into System Red. See [[Colour System]] §11 and `logos-vector/README.md`.

### The tension this creates, and it matters

Aly's first answer on 18 September was **parent company, endorsing selected lines**, and the packs alone support it: the seal is on AlRawy and 2MAN, absent from BeBo and POLEKA. **It was overturned the same day** — see the decision below.

**Their own marketing does not behave that way.** Both legacy graphics lead with the parent as a consumer brand: *«طعم أحلى مع ALEX FOODS»* and *«جديد من أليكس فوودز»*, with every brand's products arranged underneath. That is **umbrella branding**, not selective endorsement.

Both models are legitimate and they produce opposite instructions:

| Model | Then social work | And the bios |
|---|---|---|
| **Selective endorsement** (the packs) | Four brand pages, each speaking for itself. Alex never posts. | Only sealed brands may name the parent |
| **Umbrella** (their marketing) | One Alex Foods presence carrying all four, brands as ranges inside it | Everything names Alex Foods |

> **DECIDED 18 September: umbrella.** Aly sent the Alex seal and called it **"the main logo"**. Taken with the marketing evidence below and the seal being the corporate mark, Alex Foods is the master brand and the four are ranges beneath it. **One Alex Foods presence, not four brand pages.** Consequences written up in [[Brand Voice Guide]] §2.

*Superseded — kept because the reasoning is what the decision rests on:* **the Foundation has to pick one, and it is a real strategic question rather than a detail** — it decides how many pages get set up under deliverable 3, how the calendar is structured, and whose follower count grows. Recorded in [[Brand Voice Guide]] §2.

### Two more things the legacy creative exposed

1. **New SKUs nobody had counted: mini 2MAN and mini BeBo**, sold in 25 and 50 piece cartons. The SKU list grows again, against a contract that asked for five.
2. **SETTLED 19 September: 20 years, not 25.** The client answered *"20 at least."* Copy uses **«أكتر من ٢٠ سنة» / 20+** and never 25. The 25 YEARS badge on their own mini-sizes creative is inconsistent with their own seal and is worth one line back to them. *Original finding kept below, because the conflict is theirs and it is still live in market:*

2. **The company's own age is inconsistent in its own materials.** One seal reads *«جودة نثق بها منذ 20 عامًا»* and a legacy graphic *«جودة من 20 سنة دائماً»*, while the mini-sizes creative carries an Alex badge reading **25 YEARS**. **Copy cannot claim either number until the client confirms it**, and a heritage claim is exactly the kind of line that ends up in every bio and every ad.

*2MAN's Arabic name is **تومان**, confirmed on the carton artwork.*

## The trademark flag

The POLEKA cola pouch carries a **"Cola Cola"** wordmark set in a red-and-white script closely imitating a very well-known trademark, and 2MAN's Design B shows a cola bottle in similar territory. This is not TSA's decision to make, but it is TSA's exposure: under Package A, **TSA runs the paid campaigns**, which means TSA's hands are on the ad account pushing those packs to a paid audience.

Get the client's written confirmation that they hold the rights to that artwork, or keep those specific SKUs out of paid campaigns. Cheap to ask now, expensive to discover after a platform takedown or a letter.

---

**Up:** [[VAULT-INDEX]] · [[Clients]] · [[Alex Foods]]
