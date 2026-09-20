---
status: active
project: tsa
type: guide
---
# وصفة التصوير والتركيب · Shooting and Compositing Recipe

**Alex Foods · أليكس فودز**

**Brand Foundation deliverable 6 of 8**, and book section 16. Ships early and on its own, ahead of the rest of the book, because it is the document every visual asset in both stages is produced against.

> **Status 19 September, final: this is now §16 of the book.** The standalone `Alex Foods - Shooting and Compositing Recipe v1.0.pdf` shipped and stands. **`recipe.py` was deleted** and the section's content now lives once, in `design-system/book.py`; a standalone re-ship is `render(['16'])`, not a second script. **This note remains the readable source of the method.**
>
> **Status: RENDERED AND SHIPPED 19 September.** `Alex Foods - Shooting and Compositing Recipe v1.0.pdf`, **7 pages**, A4, 0.61 MB, built from `design-system/recipe.py`. **Seven pages rather than the six the spec estimated**, because the overflow probe caught two pages running past the live area and splitting one was the honest fix. Sends on WhatsApp comfortably.
>
> **Status: COMPLETE and ready to render.** Bilingual throughout, Arabic leading. Written to be worked from, not read once. Brand facts in [[Alex Foods Brands]], values in [[Colour System]], the never say list in [[Brand Voice Guide]] §7, format rules in [[Brand Book Spec]].
>
> **Internal note, not for the client: no em dashes anywhere below.** This is client facing copy and [[Brand Voice Guide]] §1 rule 8 bans them outright. Commas, full stops and brackets only.

---

## 00 · ما هذا المستند · What this document is

**بالعربية.** هذا المستند يشرح كيف تُنتَج كل صورة منتج لأليكس فودز. ليس اقتراحًا ولا مرجعًا عامًا. هو الطريقة الوحيدة المعتمدة، ومهمته أن تبدو ثمانية عشر منتجًا في أربع مجموعات وكأنها عائلة واحدة.

**In English.** This document defines how every Alex Foods product image is produced. It is not a suggestion and not a general reference. It is the single approved method, and its job is to make eighteen products across four ranges look like one family.

**الفرق عن النسخة الأولى · What changed from the first version.** لا يوجد تصوير فوتوغرافي من العميل. الصور تُنتَج داخليًا باستخدام مولّد مشاهد بالذكاء الاصطناعي. لذلك هذا المستند لم يعد تعليمات للعميل، بل أصبح طريقة عمل الوكالة.
There is no client photography. Images are produced in house using an AI scene generator. So this document is no longer instructions for the client, it is the agency's own production method.

---

## 01 · القاعدة الواحدة · The one rule

> ### المشهد يُولَّد. المنتج لا يُولَّد أبدًا.
> ### The scene is generated. The product never is.

**بالعربية.** الذكاء الاصطناعي لا يكتب حروفًا عربية صحيحة، ولا يعيد رسم شعار مسجّل بدقة. ينتج شيئًا يشبههما. على عبوة طعام، الشبيه ليس أسلوبًا، بل منتج مختلَق لا وجود له. لذلك: الذكاء الاصطناعي يصنع المكان فقط، والعبوة الحقيقية تُركَّب فوقه.

**In English.** AI does not render correct Arabic lettering, and it does not redraw a registered mark accurately. It produces something that resembles them. On a food pack, a resemblance is not a style choice, it is a fabricated product that does not exist. So: AI makes the place, and the real pack is composited into it.

**ثلاثة أشياء لا تُولَّد أبدًا · Three things are never generated:**

| | |
|---|---|
| العبوة · The pack | تُؤخذ من `packshots/single/` · taken from `packshots/single/` |
| العلامة · The mark | تُؤخذ من `logos-transparent/` · taken from `logos-transparent/` |
| أي حرف عربي · Any Arabic lettering | يأتي من فن العبوة نفسه أو يُكتب بخط Plex · comes from the pack artwork itself, or is set in Plex |

**لماذا هذه القاعدة تحمي العميل والوكالة معًا · Why this rule protects both sides.** فن العبوة ملك العميل، وكل بكسل منه في الصورة النهائية هو ملكه هو. لا يوجد ادعاء بصري لم يوافق عليه أحد، ولا علامة تجارية أُعيد رسمها خطأً.
The pack artwork belongs to the client, and every pixel of product in the final image is theirs. There is no visual claim nobody approved, and no trademark redrawn wrongly.

---

> **GAP FOUND 20 September: this recipe assumes the front of the pack, and the mechanic is on the back.** **Every consumer entry happens by scanning a QR code printed on the back of the باكو**, and **the retailer coupon is inside the carton.** Neither surface exists in `packshots/`, which holds front-facing packs only.
>
> **Two additions needed before the giveaway content can be produced: a back-of-pack frame with a legible QR, and a carton.** A QR that does not scan from a phone screen is a campaign that does not work. See [[Giveaway Programme]].

## 02 · مكتبة المصادر · The source library

**كل ما يلزم موجود بالفعل. لا شيء ينتظر العميل · Everything needed already exists. Nothing waits on the client.**

| المجلد · Folder | المحتوى · Contents | الحالة · State |
|---|---|---|
| `packshots/single/` | 5 بيبو · 5 الراوي · 4 تومان · 4 بوليكا | مقصوصة على خلفية شفافة · cut out on transparency |
| `packshots/` | خمسة صفوف كاملة للمجموعات · five full range lineups | جاهزة · ready |
| `logos-transparent/` | العلامات الأربع وختم أليكس · the four marks and the Alex seal | جاهزة · ready |
| `packs-bebo-transparent.png` · `packs-poleka-transparent.png` | أعلى دقة متاحة · the highest resolution held | جاهزة · ready |

**قاعدة الدقة · The resolution rule.** لا تُكبَّر عبوة فوق حجمها الأصلي أبدًا. إذا كان المشهد يحتاج عبوة أكبر مما تسمح به الصورة المصدر، صغّر المشهد، لا تكبّر العبوة.
Never scale a pack above its source size. If a scene needs a pack larger than the source allows, shrink the scene, do not enlarge the pack.

---

## 03 · الثوابت · The constants

**بالعربية.** هذه القيم لا تتغير أبدًا، في أي مجموعة، وفي أي صورة. هي السبب الوحيد في أن ثمانية عشر منتجًا مختلفًا تبدو عائلة واحدة. المجموعة تغيّر العالم من حولها، لا هذه القيم.

**In English.** These values never change, on any range, in any image. They are the only reason eighteen different products read as one family. The range changes the world around them, never these.

| الثابت · Constant | القيمة · Value | لماذا · Why |
|---|---|---|
| زاوية الكاميرا · Camera angle | من أعلى بمقدار 10 إلى 15 درجة · 10 to 15 degrees above | أعلى من ذلك يشوّه العبوة، وأقل يخفي الأرضية · higher distorts the pack, lower hides the surface |
| العدسة · Lens | ما يعادل 50 مم · 50 mm equivalent | العدسات الواسعة تقوّس حواف العبوة · wide lenses bow the pack edges |
| اتجاه الضوء · Light direction | من أعلى اليسار بزاوية 45 درجة · upper left at 45 degrees | ثابت واحد يجعل كل الظلال متفقة · one constant keeps every shadow in agreement |
| نوع الضوء · Light quality | ناعم، مصدر واسع · soft, broad source | الضوء الحاد يكسر ألوان العبوة المطبوعة · hard light breaks the printed pack colours |
| حرارة اللون · Colour temperature | 5200 كلفن، نهار محايد · 5200 K neutral daylight | حتى لا تتغير ألوان العلامة · so the brand colours do not shift |
| الظل · Shadow | ظل تلامس ناعم تحت العبوة مباشرة · soft contact shadow directly beneath | بدونه تبدو العبوة طائرة · without it the pack floats |
| عمق الميدان · Depth of field | العبوة حادة بالكامل، الخلفية ناعمة · pack fully sharp, background soft | العبوة هي البطل دائمًا · the pack is always the hero |
| نسبة التصوير · Capture ratio | مربع 1:1 ثم يُقتطع · square 1:1 then cropped | مصدر واحد يخدم الفيد والستوري · one source serves feed and story |

> **القاعدة التي تلخص كل ما سبق · The rule that summarises all of it:** العبوة هي البطل، والمشهد خادم. إذا سرق المشهد الانتباه، فالصورة مرفوضة.
> The pack is the hero and the scene is the servant. If the scene takes the attention, the image is rejected.

---

## 04 · عوالم المشاهد · The scene worlds

**بالعربية.** لكل مجموعة عالمها. الثوابت في القسم السابق لا تتغير، لكن المكان والأرضية والمزاج يتغيرون. العالم هو ما يفصل المجموعات عن بعضها، تمامًا كما تفعل ألوانها على الرف.

**In English.** Each range has its world. The constants above never change, but the place, the surface and the mood do. The world is what separates the ranges from each other, exactly as their colours do on a shelf.

### بيبو · BeBo
| | |
|---|---|
| المكان · Place | مطبخ بيت، سطح نظيف · a home kitchen, a clean counter |
| الأرضية · Surface | خشب فاتح أو سطح ورقي `#FAF8F3` · light wood or a paper surface `#FAF8F3` |
| الضوء · Light | ضوء صباح من نافذة · morning window light |
| المزاج · Mood | هادئ، مرتب، بيت شغّال · calm, tidy, a house that works |
| ممنوع هنا · Forbidden here | **لا تُعاد تلوين شارة KIDS ZONE لتطابق النكهة** · **never recolour the KIDS ZONE lozenge to match the flavour** |

> **سبب المنع، وهو سبب حقيقي · Why that ban, and it is a real one.** شكل استخدام بيبو غير محسوم حتى الآن بين الوكالة والعميل. الصورة التي تُظهر طريقة الاستخدام تعلن إجابة لا نملكها. تنتظر صورة ظهر العبوة.
> BeBo's format is not yet settled between the agency and the client. An image showing how it is used asserts an answer we do not have. It waits on a photo of the back of the pack.

### الراوي · AlRawy
| | |
|---|---|
| المكان · Place | طاولة نظيفة، أو حقيبة مدرسة مفتوحة · a clean table, or an open school bag |
| الأرضية · Surface | سطح فاتح محايد · a light neutral surface |
| الضوء · Light | نهار صافٍ · clear daylight |
| المزاج · Mood | اطمئنان، لا إثارة · reassurance, never excitement |
| ممنوع هنا · Forbidden here | لا أكوام فاكهة توحي بنسبة عصير · no fruit piles implying juice content |

> **الراوي نكتار، والعبوة نفسها تقول ذلك · AlRawy is a nectar and its own pack says so.** كومة فاكهة بجانب العبوة ادعاء بصري بنسبة فاكهة لم يؤكدها أحد. فاكهة واحدة كاملة مقبولة كإشارة إلى النكهة. الكومة ليست مقبولة.
> A pile of fruit beside the pack is a visual claim about fruit content that nobody has confirmed. One whole fruit as a flavour cue is fine. A pile is not.

### تومان · 2MAN
| | |
|---|---|
| المكان · Place | خارج البيت، شارع أو شاطئ · outdoors, a street or a beach |
| الأرضية · Surface | ثلج، ماء، إسمنت ساخن · ice, water, hot concrete |
| الضوء · Light | شمس قوية مباشرة · strong direct sun |
| المزاج · Mood | حركة، برودة، النهار ملكك · motion, cold, the day is yours |
| ملاحظة · Note | العبوتان، العادية و«أشكال»، لهما نفس العالم · both packs, the normal one and ashkal, share one world |

### بوليكا · POLEKA
| | |
|---|---|
| المكان · Place | خلفية لون مسطّح، بلا واقعية · a flat colour ground, no realism |
| الأرضية · Surface | لون واحد صريح من نظام الألوان · one plain colour from the colour system |
| الضوء · Light | ناعم ومتساوٍ · soft and even |
| المزاج · Mood | لعب. الشخصية أولًا والنكهة ثانيًا · play. Character first, flavour second |
| ممنوع هنا · Forbidden here | **صنف الكولا لا يظهر في أي إعلان مدفوع** · **the cola SKU appears in no paid campaign** |

> **سبب منع الكولا · Why the cola ban.** فن العبوة يحمل كلمة تشبه علامة تجارية عالمية معروفة جدًا، وحقوق استخدامها لم تؤكَّد كتابةً. الوكالة هي التي تدير الحساب الإعلاني، فالمسؤولية عليها أيضًا.
> The pack carries wording closely resembling a very well known global trademark, and the rights have not been confirmed in writing. The agency runs the ad account, so the exposure is the agency's too.

---

## 05 · صيغة الأمر · The prompt formula

> ### اطلب الغرفة، لا تطلب المنتج.
> ### Ask for the room, never for the product.

**بالعربية.** هذه هي الحيلة الكاملة. لا تطلب من المولّد «عبوة عصير على طاولة»، لأنه سيرسم عبوة مختلَقة. اطلب منه مشهدًا فارغًا فيه مساحة خالية واضحة، ثم ركّب العبوة الحقيقية في تلك المساحة.

**In English.** This is the whole trick. Never ask the generator for "a juice pack on a table", because it will draw a fabricated pack. Ask it for an empty set with a clear open space, then composite the real pack into that space.

**الصيغة · The formula:**

```
[EMPTY SCENE, no product] + [SURFACE] + [LIGHT] + [BACKGROUND] +
[MOOD] + [CAMERA: 50mm, 12° above, soft key upper-left 45°] +
[square 1:1] + [clear empty space, centre, for compositing]
```

**الأوامر تُكتب بالإنجليزية، وهذا مقصود · Prompts are written in English, and that is deliberate.** مولّدات الصور تفهم الإنجليزية أفضل بكثير. هذا الاستثناء الوحيد لقاعدة «العربية أولًا»، لأن الأمر أداة داخلية ولا يراه أحد خارج الوكالة.
Image generators understand English far better. This is the one exception to the Arabic first rule, because a prompt is an internal tool and nobody outside the agency sees it.

**أربعة أوامر جاهزة، واحد لكل مجموعة · Four ready prompts, one per range:**

**BeBo**
```
Empty home kitchen counter, no products, pale wood surface, soft morning
window light from upper left at 45 degrees, blurred warm kitchen background,
calm and tidy, 50mm lens, camera 12 degrees above the surface, square 1:1,
clear empty space in the centre foreground
```

**AlRawy**
```
Empty clean light table top, no products, one whole fresh peach resting to
the right, clear daylight from upper left at 45 degrees, soft neutral
background, calm and reassuring, 50mm lens, camera 12 degrees above,
square 1:1, clear empty space in the centre
```

**2MAN**
```
Empty wet concrete surface with scattered ice cubes and water droplets, no
products, strong direct sunlight from upper left, blurred bright outdoor
street background, high energy summer, 50mm lens, camera 12 degrees above,
square 1:1, clear empty space in the centre
```

**POLEKA**
```
Flat solid colour studio background, no products, soft even light from upper
left, no texture, no realism, playful and bright, 50mm lens, camera
12 degrees above, square 1:1, clear empty space in the centre
```

---

## 06 · ما يُستبعد من كل أمر · What every prompt excludes

**تُضاف هذه القائمة إلى كل أمر بلا استثناء · This list is added to every prompt without exception:**

```
no text, no lettering, no arabic script, no logos, no brands, no packaging,
no bottles, no sachets, no hands, no people, no faces, no watermark
```

**بالعربية.** أهم بند هنا هو منع أي كتابة. المولّد إذا كتب حرفًا واحدًا، ولو في الخلفية، فقد صنع لغة مزيفة على صورة علامة غذائية. والبند الثاني هو منع الأيدي والوجوه: أيدي الذكاء الاصطناعي غالبًا خاطئة، ولا تملك الوكالة أي إذن تصوير لأي شخص.

**In English.** The most important entry is the ban on lettering. If the generator writes one character, even in the background, it has invented a fake language on a food brand's image. The second is hands and faces: AI hands are frequently wrong, and the agency holds no model release for anybody.

---

## 07 · قواعد التركيب · The compositing rules

**بالعربية.** هذا القسم هو الفرق بين صورة تبدو حقيقية وصورة تبدو ملصقة. كلها خطوات صغيرة، وكل واحدة منها تُرى فورًا إذا نُسيت.

**In English.** This section is the difference between an image that looks real and one that looks pasted. All small steps, and every one of them is visible the moment it is skipped.

| الخطوة · Step | القاعدة · Rule |
|---|---|
| 1. الحجم · Scale | ارتفاع العبوة بين 55٪ و70٪ من ارتفاع الإطار · pack height between 55% and 70% of frame height |
| 2. الوضع · Placement | قاعدة العبوة على مستوى السطح، لا تحته ولا فوقه · pack base sits on the surface plane, not below it and not above it |
| 3. ظل التلامس · Contact shadow | أغمق نقطة عند نقطة التلامس، ثم يتلاشى خلال ما يعادل عرض العبوة · darkest at the contact point, fading over about one pack width |
| 4. الظل الملقى · Cast shadow | إلى أسفل اليمين دائمًا، لأن الضوء من أعلى اليسار · always down and to the right, because the key is upper left |
| 5. انعكاس اللون · Colour spill | خذ لون المشهد وضعه على حواف العبوة بنسبة 5٪ إلى 10٪ · sample the scene colour and lay it on the pack edges at 5% to 10% |
| 6. الحافة · Edge | تنعيم بمقدار بكسل واحد، وبلا هالة بيضاء · one pixel feather, and no white halo |
| 7. الفحص · Check | افحص القص على خلفية سوداء وأخرى بيضاء · check the cutout against a black ground and a white one |

> **البند الخامس هو الذي يقنع العين · Item 5 is the one that convinces the eye.** عبوة لم يلمسها لون المكان تبدو دائمًا كأنها من صورة أخرى، حتى لو كان الظل مثاليًا.
> A pack that the room's colour has not touched always looks like it came from another photograph, even when the shadow is perfect.

---

## 08 · قائمة الرفض · The reject list

**بالعربية.** أي صورة تحمل واحدًا من هذه البنود لا تُنشَر، ولا تُصلَح، بل تُعاد.

**In English.** Any image carrying one of these is not published and not patched. It is redone.

1. أي حرف لم يأتِ من فن العبوة الأصلي · **any lettering that did not come from the original pack artwork**
2. أي شعار لم يأتِ من `logos-transparent/` · any mark not taken from `logos-transparent/`
3. عبوة بلا ظل تلامس، أي عبوة طائرة · a pack with no contact shadow, a floating pack
4. ظل العبوة في اتجاه مخالف لظل المشهد · the pack's shadow disagreeing with the scene's
5. هالة بيضاء حول القص · a white halo around the cutout
6. يد أو وجه أو شخص · a hand, a face, or a person
7. فاكهة لا تخص النكهة المعروضة · fruit that is not the flavour shown
8. شارة KIDS ZONE مُعاد تلوينها · the KIDS ZONE lozenge recoloured
9. صنف كولا بوليكا في أي مادة مدفوعة · the POLEKA cola SKU in any paid material
10. عبوة مكبَّرة فوق دقتها الأصلية · a pack enlarged beyond its source resolution

---

## 09 · الادعاءات داخل الصورة · Claims inside the picture

**بالعربية.** قائمة الممنوعات في دليل الصوت تنطبق على الصور بنفس القوة. الصورة ادعاء منشور مثلها مثل الجملة، وصفحة الطعام يمكن الإبلاغ عنها، والحساب الإعلاني يمكن تقييده، بسبب صورة واحدة.

**In English.** The never say list in the voice guide applies to pictures with equal force. An image is a published claim exactly as a sentence is, and a food page can be reported, and an ad account restricted, over a single image.

| ممنوع بصريًا · Visually forbidden | لماذا · Why |
|---|---|
| رموز الصحة: صالة رياضية، رياضي، معمل، سمّاعة طبيب · health signifiers: a gym, an athlete, a laboratory, a stethoscope | ادعاء طبي غير موثَّق · an unsupported medical claim |
| أوراق خضراء كرمز للطبيعة حول منتج مسحوق · green leaves as a nature cue around a powdered product | يوحي بمحتوى طبيعي لا يؤكده الملصق · implies a natural content the label does not support |
| كومة فاكهة توحي بنسبة عصير · a fruit pile implying juice content | الراوي نكتار وليس عصيرًا · AlRawy is a nectar, not a juice |
| زيّ مدرسي أو شعار مدرسة · a school uniform or a school badge | يوحي بشراكة أو اعتماد لا وجود له · implies an endorsement that does not exist |
| منتج منافس داخل الإطار · a competitor product in frame | مقارنة مباشرة ممنوعة · a direct comparison, which is banned |
| واجهة محل محدَّد · a named shop front | وعد توفّر لا تملك الوكالة معلوماته · an availability promise the agency does not hold |
| أي رقم غذائي مكتوب · any nutritional number set in type | يحتاج ورقة مواصفات مكتوبة من العميل · needs the client's written spec sheet |

> **المبدأ الحاكم · The governing principle:** ما لم يصل من العميل مكتوبًا، لا تعرفه الوكالة، ولا ترسمه.
> If it did not arrive from the client in writing, the agency does not know it, and does not draw it.

---

## 10 · المقاسات النهائية · Output specifications

| الاستخدام · Use | المقاس · Size | ملاحظة · Note |
|---|---|---|
| المصدر · Master | 2048 × 2048 | يُحفظ دائمًا، ومنه تُقتطع البقية · always kept, everything else is cropped from it |
| منشور فيد · Feed post | 1080 × 1350 | المنصة الأساسية فيسبوك · Facebook is the primary platform |
| مربع · Square | 1080 × 1080 | |
| ستوري وريلز · Story and Reels | 1080 × 1920 | العبوة داخل الثلث الأوسط · pack inside the middle third |
| صورة الحساب · Profile | 320 × 320 | تُعرض دائرية · shown as a circle |
| صورة نشاط جوجل · GBP photo | 1200 × 900 كحد أدنى · minimum | |

**الصيغة · File format:** PNG للمصدر، JPG بجودة 90 للنشر · PNG for the master, JPG at quality 90 for publishing.
**التسمية · Naming:** `range-sku-format-NN` مثل `bebo-peach-feed-01` · for example `bebo-peach-feed-01`.

---

## 11 · أدوات العمل · The working toolchain

**بالعربية.** الوكالة تعمل من جهاز آيباد فقط، بلا حاسوب مكتبي وبلا سطر أوامر. كل ما سبق مكتوب ليعمل على هذا الأساس.

**In English.** The agency works from an iPad only, with no desktop machine and no command line. Everything above is written to work on that basis.

| المرحلة · Stage | الأداة · Tool |
|---|---|
| توليد المشهد · Scene generation | داخل جلسة الوكالة، حيث المولّد متاح · inside the agency session, where the generator is available |
| القص · Cutting out | غير مطلوب، العبوات مقصوصة بالفعل · not needed, the packs are already cut out |
| التركيب · Compositing | تطبيق طبقات على الآيباد · a layers app on the iPad |
| النص · Typesetting | IBM Plex Sans Arabic و IBM Plex Sans، مجانيان · both free |
| الحركة · Motion | يُحدَّد في القسم 15 من الكتاب · specified in book section 15 |

> **ملاحظة أمانة عن التكلفة · An honest note on cost.** أسعار أدوات التوليد تتغير باستمرار، ولا يُكتب هنا رقم لا يمكن التحقق منه اليوم. القاعدة: يُسعَّر أي اشتراك قبل اختياره، والمجاني يُجرَّب أولًا.
> Generation tool pricing changes constantly, and no number is written here that cannot be verified today. The rule: any subscription is priced before it is chosen, and the free option is tried first.

---

## 12 · قائمة المراجعة قبل النشر · The pre publish checklist

**بالعربية.** عشرة أسطر. تُمرَّ على كل صورة قبل خروجها، بلا استثناء.
**In English.** Ten lines. Every image passes them before it leaves, without exception.

- [ ] العبوة من `packshots/single/` ولم تُولَّد · pack came from `packshots/single/`, not generated
- [ ] لا يوجد أي حرف في المشهد · no lettering anywhere in the scene
- [ ] ظل التلامس موجود وناعم · contact shadow present and soft
- [ ] اتجاه الظل يوافق الضوء من أعلى اليسار · shadow direction agrees with the upper left key
- [ ] لا توجد هالة حول حواف العبوة · no halo on the pack edges
- [ ] لون المشهد لمس حواف العبوة · the scene's colour has touched the pack edges
- [ ] لا يد، لا وجه، لا شخص · no hand, no face, no person
- [ ] لا ادعاء صحي ولا نسبة فاكهة ولا رقم غذائي · no health cue, no fruit ratio, no nutritional number
- [ ] شارة KIDS ZONE بلونها الأصلي · the KIDS ZONE lozenge in its original colours
- [ ] صنف كولا بوليكا خارج أي مادة مدفوعة · the POLEKA cola SKU is out of all paid material

---

**Related:** [[Alex Foods]] · [[Type System]] · [[Foundation Roadmap]] · [[Brand and Social Kit]]

**Up:** [[Alex Foods Brands]] · [[Alex Foods]]
