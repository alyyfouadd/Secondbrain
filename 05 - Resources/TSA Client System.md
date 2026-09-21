---
status: active
project: tsa
type: guide
---
# TSA Client System

**The repeatable structure every TSA client gets, derived from what [[Alex Foods]] actually needed rather than from what looked tidy in advance.**

Aly's instruction, 19 September 2026: the shape built for the first client is the shape every client gets. This note is that shape. **It exists so the second client costs a fraction of what the first one did**, and so no future session has to reverse-engineer the pattern out of one client's folder.

> **The rule this note is built on: a template is only worth writing after the first real one is finished.** Everything below was paid for once, on a live 146,000 EGP ([[Alex Foods]]) contract. Nothing here is theoretical.

---

## 1. The folder shape

**Verified against the vault on 21 September.** This is what is on disk, not what was planned.

```
02 - TSA/
  <Prospect> Pitch.md                <- a business that has NOT signed. Lives here, not in Clients/
  TSA Money.md
  TSA Brand/                         <- the agency's own locked identity
  Jobs/                              <- one note per recurring agency job
  Clients/
    Clients.md                       <- the roster
    <Client>/
      <Client>.md                    <- the contract AND this folder's index. The one sanctioned double-duty
      <Client> Discovery Brief.md    <- the commercial layer: goals, distribution, competitors
      <Client> Marketing Plan.md     <- the strategy layer: what the marketing is trying to do
      <Client> Delivery Plan.md      <- the dated plan to delivery
      <Client> Week 1 Messages.md    <- messages ready to send
      <Client> - Company Brief.md    <- the one-pager a supplier reads. Explicitly derived
      Decisions.md                   <- every decision, dated, with what it overturned
      Delivery Register.md           <- every deliverable, one row, one status
      <signed scope>.pdf             <- the source document
      <Client> Brands/
        <Client> Brands.md           <- folder index and product inventory
        Foundation Roadmap.md · Brand Voice Guide.md · Colour System.md
        Type System.md · Slogans and Song.md · Content Plan.md · Post Archetypes.md
        Brand and Social Kit.md · Giveaway Programme.md · Brand Book Spec.md
        Shooting and Compositing Recipe.md · Package A Month 1.md · Month 1 Asset Brief.md
        <Client> - Brand Foundation v1.0.pdf     <- THE DELIVERABLE
        design-system/               <- the build
        packshots/ · logos-transparent/ · logos-vector/ · client-legacy-creative/
```

**Three placement rules, and each one was a decision rather than a habit:**

1. **`Clients/` exists at one client, not at three.** [[Decisions]] #8, 19 September. **The structure that scales gets built before it hurts**, which is the whole reason this vault exists. Full reasoning in [[Clients]].
2. **A client folder is created at signature, never at the first deliverable.** A business that has not signed is a prospect, and a prospect is one note in `02 - TSA/` — [[El Ghaly Motors Pitch]] is the first. **The second prospect is what earns a `Pipeline/` folder; one does not.**
3. **The client note doubles as its folder index**, carrying `type: index` and opening with a "What's in this folder" block. **This is the only place in the vault a note wears two hats** — a client has exactly one master note, and splitting the map away from the deal makes two thin notes where one full one belongs.

### How we got here

> **This section described the pre-`Clients/` shape until 21 September**, with every client note flat in `02 - TSA/` and the line *"when the third client signs, all client notes move into `02 - TSA/Clients/` — that trigger has not fired yet."* **It had fired two days earlier.** [[Decisions]] #8 built `Clients/` at one client on 19 September and [[Clients]] recorded why, while this note went on telling the next session to file client two flat. **Two notes disagreeing about where a client lives is rule 14 failing on the one fact this document exists to carry.**

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

## 4c. Getting platform access

**Never ask for a login.** The partner route in [[Meta Access Runbook]] means credentials never move, access survives staff changes on both sides, and the client revokes it in one click when the engagement ends. **And the ad account must be the client's, not the agency's** — otherwise the agency becomes payer of record for media spend the contract says the client pays directly.

## 4d. The pre-flight, and it exists because client one paid for it eight times

**Before writing a single line of copy, a positioning, a mechanic or a calendar, answer these four.** **Every one of them was skipped on client one and every skip cost a rewrite.**

| # | The check | What it cost when skipped |
|---|---|---|
| **1** | **Have I opened the actual product image, or am I working from a note?** | Ten slogans written for a product the note misdescribed. **The photograph was in the same folder the whole time.** |
| **2** | **Has the client said anything that contradicts what I inferred?** | A range's whole voice section built on the wrong audience, **after the contradiction had been spotted, written down, and deferred.** |
| **3** | **What are they already running?** | **Two giveaway mechanics and three live campaigns** designed around rather than found. One of them was the client's most urgent priority. |
| **4** | **Which of my facts are CONFIRMED and which are OBSERVED?** | The tag system existed and was ignored. **An OBSERVED fact drove four decisions as if it were CONFIRMED.** |

### The failure shape, named so it is recognisable next time

**Every one of client one's eight rework cycles was the same move: an inference from packaging outranking a statement from the client.**

Packaging is honest about one thing only — **what the artwork is doing.** It does not tell you what the product is, who buys it, how it is consumed, what it costs, or what campaigns are running behind it. **A pack is a picture of a decision somebody else made, and reading it is not research.**

> **The tell, and it is worth memorising: the moment you write "worth one more question rather than a rewrite", you have already made the mistake.** That sentence is a deferral, and a deferral on a contradiction is a decision to build on the thing you suspect is wrong.

### What to ask on day one, before any creative work

Added to the discovery brief for every client after the first:

- **What are you already running right now?** Campaigns, giveaways, promotions, trade programmes.
- **How does a customer actually enter or buy?** The mechanic, physically.
- **What is printed on the back of the pack?** **Client one's entire consumer mechanic lived on a surface nobody had photographed.**
- **What is your most urgent deadline in the next month?** **Client one's was a back-to-school campaign the agency did not know existed.**

## 5. The questions that shaped client one, and will shape the next

**Ask these before building anything.** On client one, several were asked late and the answers moved work that was already done.

1. **Who is the one named approver?** Not two, not three. The contract allows one, and it is what makes a delivery approvable. **Ask it once, at signature, on the page they are signing anyway — never as a separate chase.**

   > **The agency rule stands and client one did not follow it, which is the useful part.** Alex Foods named three, never returned a signed page, and on 21 September Aly stopped asking ([[Decisions]] #35) — four asks in, against a client who had already paid and was cooperative. **The judgement was that a fourth paperwork chase costs more relationship than clause 4 was buying.** That is defensible and it is a real trade rather than a lapse. **What it costs, so the next client can price it:** clause 4's rejection protection has no single voice of record, the 48-hour auto-approval has no subject, and **every delivery has to be closed on a written reply instead.** **The cheap version is the one client one discovered too late — put name, role and contact on the Foundation sign-off page, which the client signs regardless, and never send a message whose only job is asking for a signature.**
2. **What is the goal, as a number?** If they cannot say, **set it from their own baseline and put it in the delivery message.**
3. **Is the bottleneck consumer demand or distribution?** For any business selling through retail, this changes the whole content mix.
4. **What is the monthly ad budget?** Managing an unnamed spend is not a plan.
5. **Which platform actually has an audience?** Client one: Facebook 52,000 ([[Alex Foods Discovery Brief]]), TikTok 500, Instagram 40. **"All platforms" was the stated answer and the real answer was one.**
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

## The first-client rule — added 21 September 2026

**[[Alex Foods]] is TSA's first client, and every prospect after them will be shown this work.** Aly's instruction, 21 September: deliver as much as we can, because the portfolio is being built at the same time as the contract.

**That is right, and it changes how "in scope" gets decided — but it needs a boundary or it eats the month.**

> **The line: a free extra that costs TSA a few dollars and shows well is a portfolio investment. A free extra that costs a SUPPLIER money is not.**

| | Example | Verdict |
|---|---|---|
| Cheap, visible, TSA's own time | The recorded voice-over, at about $6 of licence | **Do it.** It is a showreel asset that happens to also delight the client |
| Cheap, invisible | A tidier file-naming convention | Do it, but it buys nothing in the portfolio |
| **Costs a supplier cash** | Extra graphics beyond the twelve, at 300 each | **No.** That is real money out of a month that has to fund its own delivery — [[TSA Money]] |
| Costs a month of capacity | A third campaign built rather than a prize swapped | **No.** [[Giveaway Programme]] §7.1 |

### And the thing nobody thinks of until it is too late

**A portfolio piece TSA is not allowed to show is not a portfolio piece.**

The signed scope keeps the working method as agency property, **but showing a client's finished creative in TSA's own marketing is a different permission and no document grants it.** **Ask for it in writing at delivery, in the same message as the sign-off page** — one line, free on the day, awkward to raise six months later when the work is good and the relationship has cooled.

**This applies to every client after them too, which is why it is here and not in the client folder.**
