---
status: active
project: tsa
type: reference
---
# Delivery Register — Alex Foods

**Every deliverable on this contract, one row each, with one status.** This note owns delivery state for [[Alex Foods]]. Nothing else does.

> **Why this note exists.** Delivery status used to be written in prose across [[Alex Foods]], [[Foundation Roadmap]], [[Alex Foods Brands]] and [[Alex Foods Discovery Brief]] — four notes, four wordings, no way to see the state of eight deliverables at once. It took a full read of the vault to discover that four of them had no content in them at all.
>
> **The rule: notes describe what a deliverable IS. This note describes where it GOT TO.** If you are about to write "drafted", "shipped" or "pending" into any other note, put it in a row here instead and link to it.

**Status vocabulary, and it is closed** — no other words:
`NOT STARTED` · `IN PROGRESS` · `BUILT` (content complete, not rendered) · `SHIPPED` (rendered and in the vault) · `DELIVERED` (sent to the client) · `APPROVED` (client signed it off) · `BLOCKED`

---

## Stage 1 — Brand Foundation · 20,000 EGP · target 9 October 2026

| # | Deliverable | Status | Blocked on | Where it lives |
|---|---|---|---|---|
| 1 | Brand Voice Guide | **IN PROGRESS** | Alex Foods' own tone block — **Aly's ear, not a client answer.** Direction received: "fun" | [[Brand Voice Guide]] |
| 2 | Colour and Type System | **BUILT** | — folded into the book as §04–06 | [[Colour System]] · [[Type System]] |
| 3 | Social Pages Setup | **BLOCKED** | **The logins have still not been used** (Aly, 23 Sep). The spec is written and **the FB and IG bios were drafted 23 Sep** (§8). Execution needs the access | [[Brand and Social Kit]] |
| 4 | Slogans and the giveaway song | **IN PROGRESS** | BeBo's line needs confirming — see [[Decisions]]. The song is drafted | [[Slogans and Song]] |
| 5 | Monthly Content Calendar | **BUILT for month 1** | **Month 1 is complete** — twenty assets, dated against campaign go-live, in [[Month 1 Asset Brief]] §2. Months 2 and 3 wait on the seasonality answer, and the contract delivers each before the month it covers | [[Month 1 Asset Brief]] · [[Content Plan]] · [[Post Archetypes]] |
| 6 | Shooting and Compositing Recipe | **SHIPPED, thin** | **Three sections lost when `recipe.py` was deleted** — the reject list, the source library and the resolution rule. Re-render is 2pp against the original 7pp. Prompts out and BeBo corrected. See [[Alex Foods Week 1 Messages]] §6 | `Alex Foods - Shooting and Compositing Recipe v1.0.pdf` |
| 7 | Google Business Profile | **BLOCKED** | **The logins have still not been used** (Aly, 23 Sep) — same block as row 3, and the *"unblocking 21 Sep"* this row carried until 24 Sep was stale by three days. Address in 19 Sep; **phone read off the back of a BeBo pack**. Hours and categories still outstanding | — |
| 8 | Local SEO — Alexandria | **IN PROGRESS** | Content built 23 Sep: footprint audit, business-data master, keyword map, digital-shelf read, monthly routine. **Missing:** the client's answers on name, phone, hours and website · search volumes (need the Google access) · Aly's 30-minute pass on the iPad (Ad Library, one delivery app, autocomplete) | [[Local SEO — Alexandria]] |
| — | **Brand Identity & Guidelines** — §03–07, 11, 12, 13, ~46pp | **CONTENT BUILT · AWAITING DESIGNER** | **Mahmoud.** Brief written, not yet sent or re-quoted | [[Mahmoud Kit Brief]] · [[Brand Book Spec]] |
| — | **Operating Guide** — everything else, TSA's own | **CONTENT BUILT** | Content for the four waiting sections | `Alex Foods - Brand Foundation v1.0.pdf` becomes this · [[Brand Book Spec]] |

> ### 21 September: the client-facing layout moved to Mahmoud, and the critical path moved with it.
>
> **[[Decisions]] #36.** The generator output stops being what the client sees. **TSA still owns all 25 sections of content; Mahmoud owns the layout.** Nothing above changes status on content — what changes is that **the shipped PDFs are no longer the delivery.**
>
> **CORRECTED the same afternoon by [[Decisions]] #37, and the correction matters: Mahmoud takes the identity half only, not the whole book.** He owns **one** of the eight contracted deliverables — #2, the Colour and Type Kit — plus the identity spine around it. **Seven of the eight still ship whatever he does**, so #27's protection is mostly intact rather than spent. *(The earlier reading here was that Mahmoud gated the whole target. That was written before the scope was set and it overstated the exposure.)*
>
> **What he does gate: deliverable 2, and the visual language the rest should follow.** That is a sequencing dependency, not a blocker — his pages want to land before TSA finalises the look of the operating guide.
>
> **Eighteen days as of 21 September**, and inside them Mahmoud must take a brief that does not exist yet, lay out a bilingual document currently at 38 pages and specced toward ~105 ([[Brand Book Spec]] §5), take a revision round, **and** produce month 1's twelve graphics. **Three of those four things have no date on them.**
>
> **Two hard dependencies to clear before he can start rather than after:**
>
> 1. **The production-resolution artwork** — [[Alex Foods Week 1 Messages]] §8b. It was the graphics blocker; **it is now the book blocker too.** No designer makes a 20,000 EGP document premium around a 199 × 251 pixel pack.
> 2. **The master navy in the brief must be the authored value, not the generators'.** `book.py:12`, `kit.py:23` and `gen.py` all still carry `#0A0378`, which [[Colour System]] §11 puts **ΔE2000 9.80** off the client's own file. **The authoritative value is CMYK 98 / 81.3 / 27 / 12.9 ≈ `#042AA2`**, and the inner disc is CMYK 7.4 / 93.8 / 83.6 / 0.8 ≈ `#EA1029`. **This stops being a render defect and becomes a brief defect** — hand him the wrong number and he builds a beautiful book around a colour the client never authored.

**Honest read: one deliverable is finished but too thin to send until three lost sections are restored. Two are blocked on client access and will ship as specification with a waiting chip. Five are part-built. And as of 21 September none of them reaches the client until a designer who has not been briefed lays them out.** Eighteen days to target as of 21 September. Dated plan in [[Alex Foods Delivery Plan]].

---

## Stage 2 — Package A · 42,000 EGP/month × 3

**Month 1 has not started and cannot start until the Foundation is approved in writing.** The 42,000 is received against it.

| Deliverable | Qty/month | Status | Note |
|---|---|---|---|
| Product animations | 2 | **NOT STARTED** | Assigned on purpose in [[Content Plan]]: the mechanic explainer and the school moment, not a product film |
| Animated stills | 6 | **NOT STARTED** | CGI animator role **unfilled** — 8 of the 20 assets |
| Graphics, feed and story | 12 | **NOT STARTED** | Weighted to BeBo as the client's named hero product |
| Content calendar | 1 | **BUILT** | Month 1 dated and platform-assigned in [[Month 1 Asset Brief]] §2 |
| GBP + local SEO maintenance | — | **BLOCKED** | Follows Foundation deliverables 7 and 8 |
| Paid campaign management | — | **BLOCKED** | Meta admin, and **no ad budget has been named** |
| Giveaway slogan and lockup | 1 | **IN PROGRESS** | Slogan written. **Lockup still to design** — one lockup with a swappable prize slot, not three builds |

---

## The client's seven materials

| # | Material | Status |
|---|---|---|
| 1 | SKU names | **IN** — roughly 18 against a contract asking for 5 |
| 2 | Logo files | **CLOSED.** Master seal is real vector; the four range marks are raster cut-outs, sufficient because nothing here is printed |
| 3 | Product photos or samples | **NO LONGER BLOCKING** — TSA produces the imagery with the AI product shooter. See [[Decisions]] #13 |
| 4 | Packaging artwork | **IN** |
| 5 | **Meta admin access** | **IN, 20 Sep, as a shared login.** Verification code 21 Sep. **Used once to grant partner access, then never again** — [[Decisions]] #28 |
| 6 | **Google account** | **IN, 20 Sep, as a shared login.** Verification code 21 Sep |
| 7 | GBP details | **PART IN** — address 19 Sep; **phone, WhatsApp and the registered legal name read off `packshots/bebo-mango-back.png` 20 Sep.** Hours and categories outstanding |
| + | **Back-of-pack photo with a legible QR** | **IN, 20 Sep** — `packshots/bebo-mango-back.png`, BeBo mango. **The QR is confirmed as the entry route by the client's own brief** ([[Decisions]] #33); only its destination URL is still unknown |
| + | **Carton artwork and the coupon** | **OUTSTANDING.** Hussein offered the coupon; blocks both trade posts in month 1 |

---

## Money

| Item | Amount | State |
|---|---|---|
| Package A month 1 | 42,000 | **RECEIVED** 18 Sep |
| Foundation instalment 1 | 10,000 | Invoiced 18 Sep, **due 26 September** |
| Foundation instalment 2 | 10,000 | **Due 8 October** — chase it *before* delivering on the 9th |
| Package A months 2 and 3 | 84,000 | Contracted, not yet due |

Full books, and the cost-of-delivery gap, in [[TSA Money]].

**Up:** [[Alex Foods]] · [[Clients]]
