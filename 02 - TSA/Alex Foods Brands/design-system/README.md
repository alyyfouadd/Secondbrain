---
status: active
project: tsa
type: guide
---
# Design System — build

Source for `Alex Foods - Design System v1.1.pdf`. The PDF is generated, never hand-laid. A revision is an edit and a re-render, not a re-layout.

**Version strings live in four places in `gen.py`** — the page footer, the cover meta block, the governance page body, and the `<title>`. Bump all four together; a grep for `v1.` catches them.

## Files
- `colour.py` — the colour maths: sRGB/Lab conversion, ΔE2000, WCAG contrast, ramps. Imported by the generator, and the source of every number in the document.
- `gen.py` — builds `ds.html` from the data. All content and CSS live here.
- `plex.css` — `@font-face` rules pointing at the local font files.
- `fonts/` — IBM Plex Sans Arabic, Plex Sans, Plex Mono as woff2. **Committed on purpose:** the build then works offline on any machine, and a render that depends on a CDN is a render that breaks silently when the network changes.

## Build
```
python3 gen.py
chromium --headless --disable-gpu --no-sandbox \
  --virtual-time-budget=25000 --print-to-pdf=ds.pdf --no-pdf-header-footer ds.html
```

## The traps, so nobody pays the discovery tax twice

**1. Chromium does not trust the agent proxy's CA.** Loading fonts from the Google Fonts CDN fails its TLS handshake, and the failure is silent: the page still renders, using fallback fonts, and the PDF looks almost right. **Fonts are fetched with `curl` and referenced locally.** Never point the render at a CDN.

**2. A screenshot viewport the same height as the page clips the bottom of it.** Rendering a 297mm page into a 1123px window drops roughly the last 23mm, which is exactly where the footer and any full-bleed foot element live. **Always screenshot taller than the page** (`--window-size=794,1400`). Two real elements were wrongly diagnosed as broken CSS before this was understood.

**3. Do not trust `/BaseFont` greps to tell you which fonts embedded.** Chromium writes font descriptors into compressed object streams, so the check returns nothing on a perfectly good PDF. **Render to PNG and look at it.**

**4. `display:block` on a broad selector like `.def b` blockifies every bold inside the card**, not just the heading, which silently breaks sentences mid-line. Scope heading styles to the direct child: `.def > b`.

**This one bit a second time, on `.lay b`, during the v1.1 rebuild.** The original layer cards had no inline bold inside their paragraphs, so the unscoped selector looked harmless for a year; the moment the rebuilt copy used `<b>` mid-sentence, three sentences broke apart on the page. **The lesson is not "fix `.def`" — it is that any `display:block` on a descendant selector is a trap waiting for the next copy change.** `.lay` is now scoped to `.lay > b` as well. Check the rest before adding inline bold to a card.

## Verifying a render

**Measure the overflow, do not eyeball it.** A page is 1123px tall at 96dpi and the live area ends 26mm (~98px) above the foot, so content must end by **~1025px**. Inject a probe that walks the page's elements, skips the footer, and reports the lowest `getBoundingClientRect().bottom`, then read it from `--dump-dom`. Eyeballing a screenshot missed a page-3 overflow that the probe caught in one run.

Screenshot individual pages by hiding the others, then read the pixels rather than trusting a downscaled preview. A 7.5pt slate footer on cream paper is invisible in a scaled-down PNG and perfectly legible in the PDF.
