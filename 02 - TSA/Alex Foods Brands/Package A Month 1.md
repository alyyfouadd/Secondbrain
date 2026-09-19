---
status: active
project: tsa
type: plan
---
# Package A Month 1 — Alex Foods

How the first paid month of [[Alex Foods]] actually gets produced: what it contains, the order it gets built in, the rail it gets built on, and the honest list of what is missing. [[Foundation Roadmap]] covers the stage before this one. The campaign context is in [[Giveaway Programme]].

**Written 19 September 2026**, before month 1 has started, because the month starts on written Foundation sign-off and everything below wants deciding before that date rather than during it.

---

## 1. The decision that should shape the whole month

**Month 1 should BE the school-gifts campaign. Not a generic content month with a giveaway bolted onto it.**

Three facts point the same way and they were not all knowable until 19 September:

1. **The client ranked their own priorities** and school gifts is first, tied to the start of the school year ([[Giveaway Programme]] §2).
2. **They named BeBo as the hero product for advertising** — and BeBo talks to the mother, who is the person buying exercise books in September.
3. **The contract already contains a giveaway slogan and campaign lockup** as a month-1 line item. It is not extra work; it is work that was always in the month.

So the month's twenty deliverables get **weighted**, not split evenly across four ranges and eighteen SKUs. Something like: BeBo leads, the giveaway is the spine, the other three ranges rotate underneath.

**Why this matters beyond tidiness:** it is the only version of month 1 that solves the deadline collision. The school campaign needs assets before the Foundation is delivered; month 1 contains those assets; pointing the month at the campaign means TSA produces one thing well instead of two things late. **It also means the client's first paid month is spent on the thing they care most about**, which is worth more than any amount of on-time genericness.

**The cost to name:** a month aimed at one campaign is a month that looks thin if the campaign moves. If the client delays the school push, the weighting has to be re-cut. Cheap to re-cut, expensive to have never decided.

## 2. What the month contains

From the signed scope, repeating every month for the term:

| | Deliverable | Notes for month 1 |
|---|---|---|
| 2 | Product animations | The two heaviest items. See §3 |
| 6 | Animated stills | Static shot with simple motion |
| 12 | Graphics | Feed and story, split between the two |
| 1 | Content calendar | For **month 2**, delivered before month 2 begins |
| — | GBP + local SEO maintenance | Blocked until the Google account arrives |
| — | Paid campaign management | Blocked on budget and on the measurement problem in §5 |
| 1 | Giveaway slogan and campaign lockup | **The spine of the month**, per §1 |

**Twenty assets, eight of them motion.** That is the real shape of the workload and it is worth staring at before agreeing a date.

## 3. The production rail — tested 19 September, not assumed

The document rail already exists in `design-system/`: Python builds HTML, Chromium renders it. **The same rail builds social assets** — a 1080 × 1350 feed post is an HTML page rendered to PNG instead of an A4 page rendered to PDF. That is not a theory; `kit.py` already renders post mockups this way.

**What was tested on 19 September**, end to end, using the real vector seal and the client's own BeBo range:

- A parameterised HTML frame that takes a time value `t` from 0 to 1 and positions every element deterministically at that instant.
- **60 frames at 1080 × 1350 rendered in 54 seconds.** Arabic set correctly in IBM Plex Sans Arabic, the vector seal crisp at any size, packs composited on their flavour field, the caption taken from [[Brand Voice Guide]] §3.

> **So the answer to "what do the animations get made in" is: this, and it costs nothing.** That question has been sitting open in [[Active Priorities]] as the thing gating every visual deliverable. It is now answered for **stills and graphics outright**, and answered for **motion with one gap**, below.

### The gap, stated honestly

**The ffmpeg available here is Playwright's minimal build.** It carries **VP8 and WebM only** — no H.264, no MP4 — and its pipe protocol is broken, so it cannot even be fed a frame sequence in the normal way.

**Frames are not the problem. Encoding is.** Three routes, none of them tested yet:

1. **A full ffmpeg in the session.** Most likely fine, unblocks MP4 directly, costs nothing but needs installing and verifying.
2. **Encode on the iPad.** The frames come down through the repo and any video app assembles them. Works, but it puts a manual step into a twenty-asset month, eight times.
3. **Deliver WebM.** Facebook generally accepts it; **Instagram is much less reliable and I would not stake a paid campaign on it.** Not recommended without checking.

**Route 1 first, and it wants testing before month 1 is agreed, not during it.**

### The design rules the test surfaced

- **The seal needs a white disc behind it on any coloured field.** Dropped straight onto BeBo peach it loses its edge, exactly as the contrast table in [[Colour System]] §11 predicts. The packaging already solves this — AlRawy sets the seal in a white roundel. **Copy the pack, do not invent.**
- **Build three or four template families, not twenty bespoke layouts.** Twelve graphics from a filled template is a day. Twelve original designs is not, and it is how one person on an iPad drowns in month two.
- **Every template renders from data.** Flavour, pack, caption, range. Changing a month means changing a list, not a layout.

## 4. The thing that actually blocks production, and it is not what the notes said

The vault has said for days that the blocker is "product photography." **That is half right and the imprecision is costing us.** The pack artwork we hold was audited on 19 September:

| Asset | Size | Usable at 1080 × 1350? |
|---|---|---|
| Range lineups (`mockup-*.png`) | ~2622 × 1206 | Yes, as a **strip of packs** |
| `packs-bebo-transparent.png` | 1822 × 757 | Marginal |
| **`packshots/single/bebo-*.png`** | **199 × 251** | **No. Nowhere close** |
| `packshots/single/alrawy-*.png` | ~250 × 410 | No |
| `packshots/single/poleka-*.png` | ~130 × 520 | No |
| `packshots/single/2man-*.png` | ~830 × 175 | No |

**Every single-pack cut-out — the thing that goes in a post as the hero — is far too small.** A BeBo sachet at 199 × 251 blown up to fill a 1080-wide frame is mush. They were sliced out of iPad screenshots, which was the right call at the time and is not good enough for production.

**So the ask splits into two, and it has been one item until now:**

1. **Pack artwork at high resolution, or vector.** For any asset where the pack is the hero, which is most of them. **They can supply this — they proved it on 19 September by sending real Illustrator artwork of the seal.** The route exists. Ask for the pack files the same way.
2. **Actual product photography.** Real product, real setting, real light. This is a different thing and it needs a shoot, which is not in either stage. The Animation and Shooting Recipe is the document that tells them how to get it.

**Conflating the two has made the ask vague, and a vague ask is why it has not arrived.**

## 5. What we still need from the client

Grouped by what each one blocks, so the list can be sent as one message rather than dribbled out.

### Blocks production immediately
1. **Pack artwork, high resolution or vector, all four ranges.** §4. The single biggest unblock available.
2. **Product photography, or samples to shoot.** Separate from 1.
3. **Meta admin access** — and a question nobody has asked yet: **do they already have pages, with followers and history?** The kit specifies *one* Alex Foods presence. **Creating a page and merging four existing ones with real followers are completely different jobs**, and only one of them is in the scope.
4. **Google account and GBP details** — address, hours, categories, phone.

### Blocks the paid campaigns
5. **The media budget.** TSA is contracted to build and manage campaigns and **nobody has ever asked what the spend is.** A structure for 5,000 EGP a month and one for 100,000 are not the same structure. Spend does not pass through TSA, which is exactly why the number has to be asked for rather than observed.
6. **Where they actually sell** — which governorates, which chains, Alexandria only or national. This drives targeting, local SEO, and the standard answer to "where can I buy it."
7. **Price points.** Not for copy — §7 of [[Brand Voice Guide]] forbids price claims — but for targeting and for judging what a campaign is worth.
8. **Do they export?** The 2MAN Bu:Zz pack carries **"Meyveli," which is Turkish.** That is in [[Alex Foods Brands]] and nobody has chased what it means. **A Turkish-language pack implies a market outside Egypt**, and if so the audience picture is wrong.
9. **Any existing analytics** — page insights, past ad performance, what has worked before.

### Blocks copy
10. **The company's age: 20 years or 25.** Their own materials say both. Still open.
11. **The giveaway's five** — school dates, QR destination, coupon artwork, permission to publish winner media, prize and draw facts. [[Giveaway Programme]] §9.
12. **Seasonality.** Ice pops in September are a different proposition from ice pops in June. What sells when decides the calendar.
13. **Who they consider competition.** For positioning and for local SEO.

### Blocks approval itself
14. **The signed acceptance page and a named approver.** Still the most exposed item on the job.
15. **Rights confirmation on the "Cola Cola" artwork.**

## 6. What does not make sense yet — commercial terms, not client facts

These are ambiguities in how the work runs. **None of them are urgent today and every one of them becomes expensive in week three.**

1. **What is "a delivery"?** Clause 2 gives one revision round **per delivery**, and the contract never defines the unit. If each of twenty assets is a delivery, that is twenty revision rounds a month. If the month is one delivery, it is one. **The honest middle is a batch** — the calendar is one delivery, each production batch is one delivery. Worth agreeing in writing at Foundation sign-off, in the same message as everything else.
2. **Does TSA post, or hand over files?** The scope buys social pages setup and campaign management, which implies TSA runs the account. But with no Meta admin TSA cannot post anything, and if the client posts, the content calendar is a document rather than a schedule. **Two different services and the contract does not say which.**
3. **How do assets get delivered?** WhatsApp, Drive, something else. Twenty assets a month needs an answer that is not "in the chat."
4. **The 48-hour auto-approval has nobody to run against.** Clause 3 makes one named approver the only voice that counts. Until that person exists, neither approval nor rejection has a subject.

## 7. What is missing on TSA's side

Not the client's fault and not fixable by chasing them.

1. **Cost of delivery — X.** Still the largest blank in the vault. Until one month of Package A has a number, no owner's draw is safe or reckless, only lucky. [[TSA Money]].
2. **The encoder.** §3. Test a full ffmpeg before agreeing a delivery date that contains eight motion pieces.
3. **The generators have not been rebuilt on the real vector.** `kit.py` and `gen.py` still reference the raster cut-out, still carry the wrong master colour, and still place the seal on navy grounds where its ring reads 1.43:1. **Source-code change, waiting on Aly's go-ahead.** See `logo-vector/README.md`.
4. **Alex Foods' master tone block**, still unwritten, still needs Aly's ear.
5. **The slogans and the song are not written.** Method only, in [[Slogans and Song]].

## 8. How the month should run

Assumes the gates in [[Alex Foods]] have closed and month 1 has actually started.

**Before day 1 — the things that should already be true**
- The month-1 start condition agreed in writing.
- Pack artwork in hand at production resolution.
- One template family built and one test asset rendered and looked at, **before twenty get poured into an untested layout.** Same rule the brand book was built under, and it caught four real defects there.

**Week 1 — the spine**
- The giveaway platform: lockup with its prize slot, slogan, song. This is the campaign's identity and everything else hangs on it.
- The month-2 content calendar drafted, so it can be delivered before month 2 rather than during it.
- Template families built and proven.

**Week 2 — batch one**
- The 12 graphics, BeBo-weighted, giveaway-led. Rendered from data against the proven templates.
- Delivered as **one batch, one revision round**, per §6.1.

**Week 3 — batch two**
- The 6 animated stills and the 2 product animations.
- Campaigns built and live, once budget and measurement are settled.

**Week 4 — close and hand forward**
- Revisions landed, month-2 calendar delivered.
- **Cost of delivery measured for real**, not estimated. This month is the only chance to get X from observation rather than guesswork, and it is the number the whole business plan waits on.

> **The discipline that makes it repeatable:** [[Active Priorities]] already carries a task to turn the repeating month into a Job note once the first one has run. **Month 1 is the draft of that note.** Every decision made here about batching, templates, revision units and rendering is a decision that gets made three times on this contract alone.

---

**Related:** [[Alex Foods]] · [[Foundation Roadmap]] · [[Giveaway Programme]] · [[Brand Voice Guide]] · [[Colour System]] · [[Brand and Social Kit]] · [[TSA Money]] · [[Slogans and Song]]
