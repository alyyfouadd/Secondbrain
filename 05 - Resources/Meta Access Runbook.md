---
status: active
project: tsa
type: guide
---
# Meta Access Runbook

**How TSA gets working access to a client's Facebook and Instagram without anybody's password changing hands.** Written for [[Alex Foods]] and reusable on every client after them.

> **The rule underneath all of it: never ask for a login.** A password in a WhatsApp thread is a liability for both sides, it breaks the vault's own secrets rule, and **Meta has a proper mechanism that exists precisely so credentials never move.** Asking for a password also tells a client you do not know how this works.

---

## What Claude can and cannot see — a standing constraint

**Claude cannot open Facebook. At all.** Not a login wall: **the session's network policy blocks the domain outright**, confirmed against the egress proxy on 20 September 2026. Instagram and TikTok are the same.

**So every fact about a client's social presence reaches TSA through Aly, and no future session should spend time trying to fetch one.**

### What works instead, in order of value

| Route | What it unlocks |
|---|---|
| **Screenshots** | **The highest-bandwidth option, and it is how the packshots worked.** Claude reads images properly — the POLEKA product truth came out of opening one. |
| **Pasted text** | Their own copy pasted into chat is a primary source. **Two posts pasted on 20 September overturned six things the voice guide asserted.** |
| **Insights exports** | Business Suite exports a CSV. Send the file, not a summary of it. |

### The four screenshots that would unblock the most, right now

1. **The page header.** Settles Page-versus-profile instantly, because the buttons are visible, and carries the name, follower count and category in the same frame.
2. **Business Suite → Insights, last 28 or 90 days.** **The engagement baseline: reach, comments, views.** The contracted number is comments and views and TSA currently has follower counts and nothing else.
3. **The last ten posts.** **Their voice at volume.** Two posts already rewrote the voice guide; ten would settle the register properly instead of by inference.
4. **Business Suite home.** Shows whether the Page sits in a Business Manager at all, which decides whether the partner route below is even available.

> **That is four screenshots and it closes the Page-versus-profile question, the engagement baseline, the voice re-pass and the access route.** Cheaper than any other four things on the job.

## Step 0 — Find out what the asset actually is. Ten seconds.

**Everything below branches here, so it goes first.**

The Alex Foods URL is `facebook.com/profile.php?id=`**`100067105295519`**. **Meta IDs beginning `1000…` are the personal user account range.** New Pages carry `profile.php?id=` URLs too, but those IDs characteristically begin `61…`.

**The check:** open it and look at the buttons.

| What you see | What it is |
|---|---|
| **Like · Follow · Message**, and page tools if you are an admin | **A Page.** Go to Path A. |
| **Add Friend · Follow** | **A personal profile.** Go to Path B. |
| It does not appear in Meta Business Suite as a Page | **A profile.** Path B. |

---

## Path A — It is a Page. The partner route.

**This is the correct way and it takes about five minutes on each side.**

**Why partner access rather than "make me an admin":** TSA holds its own Business Manager, the client assigns the Page and ad account to it, and **access survives staff changes on both sides.** Nobody shares a login, and when the engagement ends the client removes the partner in one click rather than changing a password.

### What TSA does once, ever

1. Go to **business.facebook.com** and create a Business Manager for The Standard Agency. Free.
2. Find the **Business ID** — Business Settings → Business Info. It is a long number.
3. **That number is the only thing you ever send a client.** It is not a secret.

### What the client does, per engagement

4. Client opens **business.facebook.com** → **Business Settings** → **Partners** → **Add** → *Give a partner access to your assets*.
5. They paste **TSA's Business ID**.
6. They assign: **the Page** (full control), **the Instagram account**, and **the ad account**.

### The ad account detail that matters commercially

**The ad account must be the CLIENT'S, inside the CLIENT'S Business Manager, with TSA added as a partner.** Never TSA's own.

**The signed scope says media spend does not pass through TSA and the client pays the platforms directly.** If campaigns run from a TSA ad account, **TSA becomes the payer of record**, which contradicts the scope, puts the client's spend on TSA's books, and makes TSA liable for it. **This is a five-minute setup choice with a real financial consequence.**

### Adding the media buyer

The media buyer is added **as a user inside TSA's Business Manager**, then granted task access to the client's ad account through TSA's partner relationship. **They never receive the client's credentials and never appear in the client's Business Manager directly.** Clause 1 keeps execution TSA's; this is what that looks like operationally.

---

## Path B — It is a personal profile. Bigger problem, and it is the likely one.

**If those 52,000 followers sit on a personal profile:**

- **No paid campaigns can run from it. At all.** Package A includes campaign management, and that deliverable would have nowhere to run.
- **Partner access does not exist for profiles.** There is nothing to grant.
- **An agency cannot manage it without the personal login**, which is exactly what this runbook exists to avoid.
- **Meta can restrict a personal account operating commercially.**

### What to do about it

**Meta provides a profile-to-Page migration** that carries followers across. **It is a real operation with real risk and it is not a five-minute job**, so it gets scheduled deliberately rather than attempted casually.

**The honest sequence:**

1. **Confirm it is a profile.** Do not act on the URL alone.
2. **Create a proper Page for Alex Foods** and set it up correctly from the start, per book §14.
3. **Then decide on migration versus rebuild.** Migration keeps the 52,000 and carries risk. A rebuild is clean and starts from zero. **On a three-month contract measured in comments and views, losing the 52,000 would be severe** — so migration is almost certainly right, but it is the client's asset and the client's call.
4. **Flag it as the first item on the job.** It can invalidate the platform strategy rather than merely block a deliverable.

---

## The message to send

**One message, no jargon, no password request.**

> محتاجين نوصل لصفحة فيسبوك وانستجرام عشان نبدأ الشغل، ومش محتاجين أي باسوورد.
>
> الطريقة الرسمية من فيسبوك إنكم تدخلوا على **business.facebook.com** من اللاب أو الموبايل، وتختاروا **Business Settings** ثم **Partners** ثم **Add**، وتحطوا رقم الشركة بتاعنا: **[TSA Business ID]**.
>
> وبعدها تختاروا الصفحة وحساب انستجرام وحساب الإعلانات. **حساب الإعلانات يفضل عندكم إنتوا** لأن الدفع بيتم منكم مباشرة لفيسبوك زي ما متفقين.
>
> وقبل ده بخطوة: ممكن تفتحوا لينك الصفحة وتقولولنا بتظهر **Like و Follow** ولا **Add Friend**؟ ده بيفرق معانا كتير في طريقة الإعداد.

**That last paragraph is the important one** and it is phrased as a small favour rather than a diagnosis, because **"your page might not be a page" is not a sentence to open with.**

---

## Doing it from an iPad

- **business.facebook.com works in Safari.** If the layout collapses, use **AA → Request Desktop Website**.
- **The Meta Business Suite app** handles day-to-day posting and inbox, but **partner and permission settings are more reliable in the desktop-mode browser.**
- **Do the setup in Safari desktop mode, then live in the app.**

---

**Related:** [[Alex Foods]] · [[Alex Foods Discovery Brief]] · [[TSA Client System]] · [[TSA]]
