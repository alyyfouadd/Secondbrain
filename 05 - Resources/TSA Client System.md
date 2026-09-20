---
status: active
project: tsa
type: guide
---
# TSA Client System

**The repeatable structure every TSA client gets, derived from what [[Alex Foods]] actually needed rather than from what looked tidy in advance.**

Aly's instruction, 19 September 2026: the shape built for the first client is the shape every client gets. This note is that shape. **It exists so the second client costs a fraction of what the first one did**, and so no future session has to reverse-engineer the pattern out of one client's folder.

> **The rule this note is built on: a template is only worth writing after the first real one is finished.** Everything below was paid for once, on a live 146,000 EGP contract. Nothing here is theoretical.

---

## 1. The folder shape

```
02 - TSA/
  <Client>.md                      <- the contract: deal, gates, clauses, money
  <Client> Discovery Brief.md      <- the commercial layer: goals, distribution, competitors
  <Client> Brands/
    <Client> Brands.md             <- folder index and product inventory
    Foundation Roadmap.md          <- sequenced build plan, dependencies, what needs a human
    Brand Voice Guide.md           <- one voice, a tone per range, the comment-reply policy
    Colour System.md               <- computed: masters, ramps, contrast, collisions
    Type System.md                 <- faces, weights, scales, bilingual rules
    Slogans and Song.md            <- method, audience map, the lines
    Shooting and Compositing Recipe.md
    Brand Book Spec.md             <- the spec for the one book
    <Client> - Brand Foundation v1.0.pdf   <- THE DELIVERABLE
    design-system/                 <- the build
    packshots/ · logos-transparent/ · logos-vector/ · client-legacy-creative/
```

**When the third client signs, all client notes move into `02 - TSA/Clients/` with its own index.** That trigger is already recorded in [[TSA]] and it has not fired yet.

---

## 2. What is reusable code and what is client content

**This is the distinction that decides how fast client two goes.**

| File | Reusable? | Note |
|---|---|---|
| `colour.py` | **Fully.** Copy untouched. | sRGB/Lab, ΔE2000, WCAG contrast, ramps. No client data in it. |
| `plex.css` · `fonts/` | **Fully.** Copy untouched. | IBM Plex Arabic/Latin/Mono, committed so the build works offline. |
| `book.py` CSS block | **Fully.** ~300 lines. | The page furniture: grid, eyebrows, notes, tables, chips, footer. **This is the single biggest saving.** |
| `book.py` section scaffolding | **Structurally.** | `sec()`, `render(ids)`, the status-chip system, the 25-section architecture. |
| `book.py` section *content* | **No. Per client.** | Every word is that client's. |
| `ranges.py` | **No. Per client.** | The shape is reusable, the values never are. |

> **The saving is real and worth naming: roughly the CSS, the maths, the fonts, the page architecture and the build method carry over.** What does not carry is every sentence, which is correct, because that is the part being sold.

---

## 3. The order of work, and why it is this order

Learned the hard way on client one. **Sequenced by dependency, not by the order the contract lists deliverables.**

1. **Read the signed scope and write `<Client>.md` from it.** Deal, gates, clauses, money in and money due. **Before any creative work.** The gating chain is what tells you which deliverables are even startable.
2. **Write `<Client> Discovery Brief.md` and send the questions.** The commercial layer. **This is the step that was done late on client one and it cost real rework.**
3. **Ingest whatever artwork exists.** Cut packs to transparency, file marks, record what is raster and what is vector.
4. **Phase 1, needs nothing external:** colour system, type system, voice guide. **Six of eight Foundation deliverables can be built with nothing from the client.**
5. **Ship the shooting recipe early and alone.** It unblocks the client's imagery, which blocks everything visual.
6. **Phase 2:** slogans, canvas and grid, the pack-in-field device, motion, social spec, calendar format.
7. **Assemble the one book, render, probe, proof.** One document, never three.
8. **Deliver with the sign-off page, the month-1 start condition, and honest status on anything pending.**

---

## 4. The rules that were paid for once

**These are the findings from client one that generalise. Each one cost something to learn.**

| Rule | What it prevents |
|---|---|
| **One book, never three.** | Three documents stating the same hex value, and a client asking which one wins. |
| **Compute, never assert.** Contrast, ΔE and collisions come from code. | A governance document that is wrong and confident. |
| **Compute the palette against itself.** | Client one had **five exact colour collisions nobody had noticed**, including a range signature that was two other ranges' flavour fields. |
| **The rhythm is derived from what the retainer funds.** | Client one's kit asked for ~83 posts a month against 20 funded assets. **A rhythm the contract cannot fund is one the client can hold you to.** |
| **Print the status chip; never omit a bought deliverable.** | A book that quietly drops a section looks unfinished. One that says what it waits on looks governed. |
| **Look at the product before writing copy for it. Not the note about it.** | Ten slogans written from a text description of a client product that turned out to misdescribe it. **The photograph was in the same folder the whole time.** A note is somebody else's reading, and copy written off a reading is copy about a reading. |
| **Packaging tells you what the artwork is doing, never what the product means to the buyer.** | Three failures in one week from the same move: a product's format, its audience, and its entire positioning, all inferred from looking at a pack. **When the client states who buys it or what it is, that outranks the read.** |
| **Never generate a pack, a mark or Arabic lettering with AI.** | A fabricated product on a food brand. The scene is generated; the artwork is composited. |
| **The never-say list is legal, not stylistic.** | A reported page or a restricted ad account. **The agency runs the ad account, so it is the agency's exposure.** |
| **No em dashes in outgoing copy.** | Copy that reads as machine-written. |
| **Surface a deviation from a written spec; never override it silently.** | A decision nobody remembers making. |
| **Measure page overflow with a DOM probe.** | An overflowing page has `overflow:hidden`, so **it does not look broken, it silently crops.** |

---

## 4b. How to propose a Foundation so the client chooses without designing it

**Reusable, and it is the part most likely to decide whether a Foundation gets approved fast or argued over.** Full version in [[Foundation Roadmap]].

**Every section sits in exactly one of three tiers:**

- **Governed** — computed or legal. Colour, contrast, type, compliance. **No choice is offered, because offering one is offering to be wrong.**
- **Recommended** — real judgement calls where the client's market knowledge adds something. **One recommendation, at most two alternates, the trade named.**
- **Theirs to state** — facts only they hold. Approver, budget, seasonality, rights. **Inputs, not options.**

**The four rules for the middle tier:** lead with a recommendation rather than a menu · **never show an option you would be unhappy to ship** · name the trade rather than the taste · two alternates maximum.

**And use the 48-hour clause actively:** state the recommended option as the default in writing, so **silence produces the preferred outcome rather than a stall.**

**Present the architecture page first, then the choices batched into one message, then the honest status, then the sign-off.** Never send the whole book cold.

> **Tested on client one's slogans and it worked twice**, including once where the client chose against the recommendation and was right to.

## 5. The questions that shaped client one, and will shape the next

**Ask these before building anything.** On client one, several were asked late and the answers moved work that was already done.

1. **Who is the one named approver?** Not two, not three. The contract allows one, and it is what makes a delivery approvable.
2. **What is the goal, as a number?** If they cannot say, **set it from their own baseline and put it in the delivery message.**
3. **Is the bottleneck consumer demand or distribution?** For any business selling through retail, this changes the whole content mix.
4. **What is the monthly ad budget?** Managing an unnamed spend is not a plan.
5. **Which platform actually has an audience?** Client one: Facebook 52,000, TikTok 500, Instagram 40. **"All platforms" was the stated answer and the real answer was one.**
6. **Is the social asset a Page or a personal profile?** If a profile, **no paid campaign can run from it at all.**
7. **Seasonality per product line.** A term that sits in a product's off-season changes every calendar.
8. **Do they hold rights to the artwork you will be putting behind paid spend?**

---

## 6. What a new client's first week looks like

- **Day 1** — scope note, discovery brief, questions sent.
- **Day 2** — artwork ingested, colour and type computed.
- **Day 3** — voice guide drafted, shooting recipe shipped early and alone.
- **Day 4 to 7** — the remaining sections, assembled into the one book, probed and proofed.

**That is achievable only because the CSS, the maths, the fonts and the architecture already exist.** Client one spent most of its time building those. Client two spends its time on the client.

---

**Related:** [[TSA]] · [[Alex Foods]] · [[Brand Book Spec]] · [[Foundation Roadmap]] · [[Colour System]] · [[Brand Voice Guide]] · [[Slogans and Song]] · [[Shooting and Compositing Recipe]] · [[TSA Money]] · [[Marketing]] · [[Resources]]
