---
status: active
project: tsa
type: reference
---
# logo-vector — the real Alex Foods master seal

**Received 19 September 2026. This is the first genuine source artwork the client has ever sent**, and it closes material #2 for the master mark. Everything before it was a photograph of a file somebody had open.

## What the file actually is

`Alex-master-seal.pdf` — the client's own file, unmodified.

| | |
|---|---|
| Authored in | **Adobe Illustrator 24.2 (Windows)**, Adobe PDF Library 15.00 |
| Created | **2026-09-19 11:54 (+03:00, Cairo)** — made the same day it was sent |
| Editability | Carries `/PieceInfo /Illustrator` and six `AIPDFPrivateData` blocks, so **the live Illustrator artwork is embedded**. It reopens in Illustrator as an editable file, not a flattened picture |
| Images | **Zero image XObjects.** Nothing raster anywhere in it |
| Fonts | **Zero.** All lettering is outlined, which is correct and normal for a logo |
| Geometry | 1,609 path-construction operators, **114 filled paths and 2 stroked paths** |
| Colour | **CMYK throughout.** No RGB, no spot colours, no gradients, no transparency, no clipping masks |

**No `/Shading`, no `/Pattern`, no separations.** It is flat vector, print-prepared.

## The files here

| File | What it is |
|---|---|
| `Alex-master-seal.pdf` | **The master.** The client's original. Never edit it, never re-save over it |
| `alex-seal.svg` | Converted to SVG for the HTML → PDF build in `design-system/`. 116 paths, 1:1 with the source |
| `alex-seal-2000.png` | 2000 × 2000 RGBA, transparent. For anything that will not take an SVG |
| `alex-profile-320.png` | 320 × 320 on **white**, the profile-picture export. See the warning below |
| `pdf2svg.py` | The converter. Kept so the conversion is reproducible rather than a one-off artefact |

## The conversion, and the trap in it

There is no `pdfinfo`, `pdftocairo`, `qpdf`, `mutool`, `inkscape` or PyMuPDF in this environment, so the SVG was produced by parsing the PDF content stream directly: inflate the eight content streams, walk the operators, map `m l c v y h re` to SVG path data, track `q`/`Q`/`cm` for the transform, `k`/`K` for CMYK fill and stroke, and flip Y because PDF counts up from the bottom and SVG counts down from the top.

> **The trap, and it nearly shipped: the first conversion dropped the two stroked paths.** It only handled `f`, so 114 of 116 paths came through and the render looked perfectly convincing. Those two strokes are **white, 1.22 pt**, and they are the crisp white keyline between the red disc and the blue ring and around the seal's outer edge. Without them the red butts straight into the blue and the mark looks subtly cheaper, in a way that is very hard to spot unless you put the two side by side.
>
> **The method that caught it:** counting paint operators in the source (`f` × 114, `S` × 2) against paths in the output, instead of looking at the render and being satisfied. Same family as the four CSS defects in `design-system/design-system.md` — **it did not error and it did not look broken.**

Anything else converted out of a PDF here gets the same check: count the operators, do not trust the picture.

## The client's own colour values

**These CMYK numbers are authoritative** — they are what the client's designer typed into Illustrator. The sRGB column is a naive conversion (`255 × (1−ink) × (1−K)`) done without a colour profile, so it is a working approximation and **not** what Illustrator would export through a proper profile.

| Role | CMYK — authoritative | sRGB — conversion |
|---|---|---|
| **Ring blue** | C98 M81.3 Y27 K12.9 | ~`#042AA2` |
| **Disc red** | C7.4 M93.8 Y83.6 K0.8 | ~`#EA1029` |
| Counter red | C1.6 M93.4 Y89.8 K0.4 | ~`#FA111A` |
| Sun disc | C7 M4.7 Y6.3 K0 | ~`#EDF3EF` |
| White | 0 0 0 0 | `#FFFFFF` |

**Two defects in the client's own file**, both harmless and both worth knowing before anyone "fixes" them:

1. **Two reds where there should be one.** The disc red and the red inside the letter counters sit at **ΔE2000 4.97** — just under the system's own 5.0 collapse threshold. Nobody will ever see it. It means the file carries two reds by accident.
2. **The sun disc is not white.** It is **ΔE2000 4.74** off pure white, a faint green-grey. Almost certainly an artefact rather than a decision.

## What this overturns

Recorded here because four notes stated the opposite with confidence, and the confidence was earned off a raster.

1. **The seal is FLAT, not a rendered 3D object.** Every note said it was a 3D object with gradients and gloss that must be "placed as supplied and never reconstructed." **That was true of the picture, not of the mark.** It can now be scaled, placed, and printed at any size.
2. **There is no Egyptian flag ribbon on this version.** `../logo-alex-seal.jpg` has one; this does not. **Two versions of the master mark now exist and the Foundation has to say which one governs.**
3. **Alex Navy `#0A0378` is wrong by ΔE2000 9.80.** It was sampled off a gradient render. The real ring is a brighter blue.
4. **`#05004B` is wrong by ΔE2000 15.38** and was never a brand colour — it was a gradient stop of a *rendering*. It currently carries hero panels and the sign-off block in the shipped Brand and Social Kit.
5. **The ring blue collapses into 2MAN blue `#2E3192` at ΔE2000 3.77**, under the system's own collapse rule. A governance decision, not a maths error.

## The placement rule this forces, with the numbers behind it

Contrast of the seal's own ring against the ground it is placed on:

| Ground | Ring | Disc | Verdict |
|---|---|---|---|
| Paper `#FAF8F3` | **10.65:1** | 4.30:1 | **Correct** |
| White `#FFFFFF` | **11.30:1** | 4.56:1 | **Correct** |
| Alex Navy `#0A0378` | **1.43:1** | 3.55:1 | **The ring disappears** |
| `#05004B` | **1.68:1** | 4.16:1 | **The ring disappears** |
| System Red `#E1251D` | 2.41:1 | **1.03:1** | **The disc disappears** |
| BeBo green `#1BA34C` | 3.44:1 | 1.39:1 | Fails |

> **The rule: the seal goes on white or Paper, and on nothing else.** It carries its own navy ring and its own red disc, so it needs a *light* ground to have an edge at all. Put it on navy and the ring dissolves into the background and the mark reads as a floating red blob.
>
> **This is a live defect in a shipped deliverable.** `design-system/kit.py` line 73 places the seal on `#05004B` and labels it **"ON NAVY — DEFAULT"**, and line 215 makes the 320 × 320 profile picture the seal on Alex Navy, with the claim *"It holds on a light feed and a dark one, which is the whole reason it needs no second version."* **With the real artwork that claim is false.** Confirmed by eye as well as by ratio.
>
> `alex-profile-320.png` here is therefore exported **on white**, not on navy.

---

**Written up in** `../Alex Foods Brands.md` · `../Colour System.md` · `../Brand and Social Kit.md`
