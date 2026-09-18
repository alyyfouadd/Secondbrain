---
status: active
project: tsa
type: guide
---
# Design System — build

Source for `Alex Foods - Design System v1.0.pdf`. The PDF is generated, never hand-laid. A revision is an edit and a re-render, not a re-layout.

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

## Verifying a render
Screenshot individual pages by hiding the others, then read the pixels rather than trusting a downscaled preview. A 7.5pt slate footer on cream paper is invisible in a scaled-down PNG and perfectly legible in the PDF.
