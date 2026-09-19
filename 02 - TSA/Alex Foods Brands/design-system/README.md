---
status: active
project: tsa
type: guide
---
# Design System — build

**This folder builds the book.** Both are generated, never hand-laid; a revision is an edit and a re-render, not a re-layout.

| Generator | Output | What it is |
|---|---|---|
| **`book.py`** | **`Alex Foods - Brand Foundation v1.0.pdf`** | **THE BOOK. 34 pages, 25 sections, bilingual, Arabic leading.** The single source for every section's content. **`render(ids)` renders any subset**, so section 16 alone is `render(['16'])` and no section text exists twice. |
| `gen.py` | `ds.pdf` | The 19pp Design System. **Retired as a client deliverable 19 Sep** when the one-book decision folded colour and type into the book as §04 to §06. Kept as the built source. |
| `kit.py` | *(retired)* | The 8pp Brand and Social Kit. **Retired as a client deliverable 19 Sep**, folded into the book as §07 and §11 to §14. |

> **`field.py` and `recipe.py` were deleted 19 September.** Their sections are §12 and §16 of `book.py`, and keeping standalone generators for them would have put the same governance text in two files, which is the drift this repo exists to avoid. **A standalone early ship is `book.py render(['16'])`, not a second script.**

They share `colour.py`, `plex.css`, `fonts/` and `tsafonts/`. **Nothing is duplicated — change the maths in one place.**

**Version strings live in four places in `gen.py`** — the page footer, the cover meta block, the governance page body, and the `<title>`. Bump all four together; a grep for `v1.` catches them. `kit.py` carries its version in the footer helper and the `<title>` only.

## Files
- `ranges.py` — **the canonical range and flavour data**: signatures, pack shapes, aspect ratios and every flavour field. **`kit.py` still carries its own inline copy and gets pointed here on its next edit**, which is the book rebuild. Do not add a third copy.
- `colour.py` — the colour maths: sRGB/Lab conversion, ΔE2000, WCAG contrast, ramps. Imported by the generator, and the source of every number in the document.
- `gen.py` — builds `ds.html` from the data. All content and CSS live here.
- `plex.css` — `@font-face` rules pointing at the local font files.
- `../packshots/` — the client's product mockups, keyed to transparency, with individual packs in `single/`. **`kit.py` references these by relative path**, so Chromium embeds them at render. Keep the paths stable.
- `fonts/` — IBM Plex Sans Arabic, Plex Sans, Plex Mono as woff2. **Committed on purpose:** the build then works offline on any machine, and a render that depends on a CDN is a render that breaks silently when the network changes.

## Build
```
python3 gen.py
$CHROME --headless --disable-gpu --no-sandbox \
  --virtual-time-budget=25000 --print-to-pdf=ds.pdf --no-pdf-header-footer ds.html
```

**`$CHROME` is not `chromium`.** See trap 9.

## The traps, so nobody pays the discovery tax twice

**1. Chromium does not trust the agent proxy's CA.** Loading fonts from the Google Fonts CDN fails its TLS handshake, and the failure is silent: the page still renders, using fallback fonts, and the PDF looks almost right. **Fonts are fetched with `curl` and referenced locally.** Never point the render at a CDN.

**2. A screenshot viewport the same height as the page clips the bottom of it.** Rendering a 297mm page into a 1123px window drops roughly the last 23mm, which is exactly where the footer and any full-bleed foot element live. **Always screenshot taller than the page** (`--window-size=794,1400`). Two real elements were wrongly diagnosed as broken CSS before this was understood.

**3. Do not trust `/BaseFont` greps to tell you which fonts embedded.** Chromium writes font descriptors into compressed object streams, so the check returns nothing on a perfectly good PDF. **Render to PNG and look at it.**

**4. `display:block` on a broad selector like `.def b` blockifies every bold inside the card**, not just the heading, which silently breaks sentences mid-line. Scope heading styles to the direct child: `.def > b`.

**5. A class name used for two different things will silently override one of them.** `kit.py` used `.tl` for both a corner frame mark (`.c.tl`) and the typography specimen's left column. The specimen's `background` won, and painted a Surface Navy square over the corner of the red statement panel. **A DOM probe found it in one run; three passes of looking at the PNG had not.** Prefix structural utility classes.

**6. Read computed styles, not a downscaled PNG, before "fixing" a colour.** The Paper swatch card looked blue in an 80dpi render and was `rgb(20,20,20)` in the DOM. The render was lying, not the CSS.

**8. Hardcoding a page total breaks the moment the document grows.** `kit.py` printed `PAGE n / 6` in its footer and the kit went to eight pages. The footer now writes a `@@TOTAL@@` token that is substituted once, after generation, when the real count is known.

**7. A descendant selector will silently beat a class you wrote later.** `.tyl p` (0,1,1) beat `.d1` (0,1,0), so a 21pt display statement rendered at 7.2pt and simply looked like a design choice. **Nothing errors, nothing warns, and a screenshot will not tell you** — the text is just quietly the wrong size. Scoped to `.tyl p.d1`.

**9. `chromium` is not on `PATH` in this environment, and the failure looks like the tool is missing.** The binary lives at **`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`** (Playwright's install, pointed at by `PLAYWRIGHT_BROWSERS_PATH`). A plain `which chromium` returns nothing and `chromium --headless` reports *command not found*, which reads as "no browser here" rather than "wrong name". **Set `CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome` and use `"$CHROME"`.** The version number in that path will move; `ls /opt/pw-browsers/` finds the current one.

**10. Expect one SSL handshake error in the render log, and do not chase it.** `handshake failed ... net_error -202` appears on every render. **It is not the fonts** — `plex.css` contains zero `http` references and every face is local, which a `grep -c http plex.css` confirms in one second. It is Chromium's own background traffic against the agent proxy, and the PDF is unaffected. **Confirm fonts by screenshotting a page with Arabic on it and looking at the shaping**, per trap 3.

> **Traps 4, 5 and 7 are one trap wearing three coats: a CSS rule silently beating the one you meant.** A descendant `display:block`, a reused class name, a specificity override. None of them error and none of them look broken in a screenshot. **The only reliable check is a DOM probe** — walk the elements, read `getComputedStyle`, and compare against what you intended. Four real defects in the kit build were found that way after repeated passes of looking at PNGs had missed every one.

**Trap 4 bit a second time, on `.lay b`, during the v1.1 rebuild.** The original layer cards had no inline bold inside their paragraphs, so the unscoped selector looked harmless for a year; the moment the rebuilt copy used `<b>` mid-sentence, three sentences broke apart on the page. **The lesson is not "fix `.def`" — it is that any `display:block` on a descendant selector is a trap waiting for the next copy change.** `.lay` is now scoped to `.lay > b` as well. **And a third time in `kit.py`**, on `.how b`, `.card.hd b`, `.cs b`, `.stat b` and `.pil b` — all now scoped to the direct child. **Assume every `display:block` on a descendant selector is broken until proven otherwise.**

## Verifying a render

**The probe earns its keep every single time.** On `recipe.py`'s first render it caught **two overflowing pages that looked completely fine** in the page-count output: page 5 at 1176px and page 6 at 1200px against a 1025px limit. Both were fixed by turning the two-line list rows into a 2-column grid and splitting one page in two, and the document went from 6 pages to 7. **Neither overflow was visible without the probe**, because an overflowing `.page` has `overflow:hidden` and simply crops what falls off the bottom.

**Measure the overflow, do not eyeball it.** A page is 1123px tall at 96dpi and the live area ends 26mm (~98px) above the foot, so content must end by **~1025px**. Inject a probe that walks the page's elements, skips the footer, and reports the lowest `getBoundingClientRect().bottom`, then read it from `--dump-dom`. Eyeballing a screenshot missed a page-3 overflow that the probe caught in one run.

Screenshot individual pages by hiding the others, then read the pixels rather than trusting a downscaled preview. A 7.5pt slate footer on cream paper is invisible in a scaled-down PNG and perfectly legible in the PDF.
