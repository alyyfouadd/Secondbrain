---
status: active
project: tsa
type: reference
---

> **CORRECTED 19 September 2026: a true vector master EXISTS for the Alex Foods seal.** `LOGO.pdf` arrived from the client and it is genuine vector artwork: **zero embedded images, zero fonts, 1,612 vector path operations, CMYK fills.** Filed as `logos-vector/alex-seal-master.pdf`. **It is also the FLAT two-colour seal, not the rendered 3D object** in `logo-alex-seal.jpg` — navy ring, red disc, white type, no gradients and no gloss, which is far more usable at every size. **The standing claim that no source files exist was true of the four range marks and is now false of the master.** Nobody has sent vector for BeBo, AlRawy, 2MAN or POLEKA yet, and **the chase should restart, because this proves the client can produce vector when asked.**

# Logos — transparent working set

**All four [[Alex Foods]] brand marks, cut out on transparency, ready to place.** Produced 18 September 2026 by extracting them from the raster material the client supplied, because no source files were ever sent and none are coming.

| File | Source | How it was cut |
|---|---|---|
| `logo-bebo-transparent.png` | Canva mockup, 3645 × 1515 render | Cropped from artwork that already carried an alpha mask |
| `logo-poleka-transparent.png` | Canva mockup, 4859 × 2020 render | Same — alpha was already present |
| `logo-2man-transparent.png` | Screenshot of a PDF viewer | White keyed out by flood fill **from the page edges only**, then reduced to the largest connected component to drop the viewer's interface |
| `logo-alex-lockup-transparent.png` | The Alex master lockup on flat navy | Navy keyed by a **hue-aware** test — dark **and** blue-dominant — because a plain distance test ate the black band of the Egyptian flag, which sits within tolerance of the navy. Edges feathered and the navy un-premultiplied, so it composites on white with no halo |
| `logo-alrawy-transparent.png` | Screenshot, iOS status bar cropped | Same flood fill. **The faint concentric rings around the roundel stopped the fill**, which is the only reason the white disc survived — a global white removal would have destroyed it |

**Why the Alex key had to be hue-aware:** the background navy is `#050221` and the flag's black band is about `#202020`. By straight colour distance they are 40 apart, inside any tolerance loose enough to catch the background's noise, so the fill ran straight through the flag and deleted half the ribbon. Testing for *dark **and** blue-dominant* separates them cleanly: navy has blue well above red and green, neutral black does not.

**Why flood fill from the edges and never a global white removal:** three of these marks contain white *inside* them — BeBo's letterforms, AlRawy's roundel, 2MAN's ice highlights. Removing white everywhere would have punched holes through all three. Filling inward from the page edge only removes white that is connected to the background.

## What these are good for

**Everything in the signed contract.** Nothing in the Brand Foundation or in Package A is printed — it is all social, digital and screen. At this resolution these are comfortably enough for feed posts, stories, animations, profile and cover images, and the Business Profile.

## What they are not good for

- **Print of any kind**, at any size.
- **Very large scale** — beyond roughly twice the pixel dimensions the edges will soften.
- **Recolouring, or a single-colour version.** That needs the paths.

If print or large format ever enters scope, it is a clause 7 quote and the source files become a real requirement rather than a convenience.

---
**Related:** [[Alex Foods Brands]] · [[Colour System]] · [[Type System]]
