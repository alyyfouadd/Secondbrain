# -*- coding: utf-8 -*-
# Alex Foods - Shooting & Compositing Recipe.
# Foundation deliverable 6, book section 16. Ships early and alone.
# Shares plex.css and fonts/ with gen.py and kit.py. Nothing is duplicated.
# NOTE: no em dashes anywhere in output copy. Voice Guide S1 rule 8.
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))

PAPER='#FAF8F3'; INK='#141414'; GRAPH='#4A4742'; SLATE='#8A8681'
SILVER='#C9C5BC'; MIST='#EDEAE3'; RED='#E1251D'; NAVY='#0A0378'; DEEP='#05004B'

H=[]; PAGES=[0]
def p(s): H.append(s)
def page(body, label=''):
    PAGES[0]+=1
    p(f'<section class="page">{body}'
      f'<footer><span class="fm"><b>ALEX FOODS</b><em>أليكس فودز</em></span>'
      f'<span class="fr">{label} · v1.0 · PAGE {PAGES[0]} / @@TOTAL@@</span></footer></section>')
def eb(ar,en): return f'<div class="eb"><span>{en}</span><i></i><b class="ar">{ar}</b></div>'
def cnr(): return '<i class="cnr tl"></i><i class="cnr tr"></i><i class="cnr bl"></i><i class="cnr br"></i>'
def bi(ar,en,cls='bi'):
    return f'<div class="{cls}"><p class="ar">{ar}</p><p class="en">{en}</p></div>'

# ============ PAGE 1 ============
page(f'''{eb('وصفة التصوير والتركيب','SHOOTING &amp; COMPOSITING RECIPE')}
<div class="hero">{cnr()}
 <div class="hx"><h1 class="ar">وصفة التصوير والتركيب</h1>
 <h2>SHOOTING &amp; COMPOSITING RECIPE</h2>
 <p class="ar sub">أليكس فودز · الأساس التجاري · التسليم رقم 6 من 8</p>
 <p class="sub">ALEX FOODS &nbsp;·&nbsp; BRAND FOUNDATION &nbsp;·&nbsp; DELIVERABLE 6 OF 8</p></div></div>

{eb('ما هذا المستند','00 · WHAT THIS DOCUMENT IS')}
{bi('هذا المستند يشرح كيف تُنتَج كل صورة منتج لأليكس فودز. ليس اقتراحًا ولا مرجعًا عامًا. هو الطريقة الوحيدة المعتمدة، ومهمته أن تبدو ثمانية عشر منتجًا في أربع مجموعات وكأنها عائلة واحدة.',
    'This document defines how every Alex Foods product image is produced. It is not a suggestion and not a general reference. It is the single approved method, and its job is to make eighteen products across four ranges look like one family.')}

{eb('القاعدة الواحدة','01 · THE ONE RULE')}
<div class="rule">{cnr()}
 <p class="ar rl">المشهد يُولَّد. المنتج لا يُولَّد أبدًا.</p>
 <p class="rl en">THE SCENE IS GENERATED. THE PRODUCT NEVER IS.</p></div>
{bi('الذكاء الاصطناعي لا يكتب حروفًا عربية صحيحة، ولا يعيد رسم شعار مسجّل بدقة. ينتج شيئًا يشبههما. على عبوة طعام، الشبيه ليس أسلوبًا، بل منتج مختلَق لا وجود له.',
    'AI does not render correct Arabic lettering, and it does not redraw a registered mark accurately. It produces something that resembles them. On a food pack, a resemblance is not a style choice, it is a fabricated product that does not exist.')}
<table class="t3"><thead><tr><th>لا يُولَّد أبدًا · NEVER GENERATED</th><th>من أين يأتي · WHERE IT COMES FROM</th></tr></thead><tbody>
<tr><td><b>العبوة</b> · The pack</td><td class="mono">packshots/single/</td></tr>
<tr><td><b>العلامة</b> · The mark</td><td class="mono">logos-transparent/</td></tr>
<tr><td><b>أي حرف عربي</b> · Any Arabic lettering</td><td>من فن العبوة نفسه أو بخط Plex · from the pack artwork, or set in Plex</td></tr>
</tbody></table>
<div class="note"><b>لماذا تحمي القاعدة الطرفين · Why the rule protects both sides</b>
<p class="ar">فن العبوة ملك العميل، وكل بكسل منه في الصورة النهائية هو ملكه هو.</p>
<p class="en">The pack artwork belongs to the client, so every pixel of product in the final image is theirs. No visual claim nobody approved, and no trademark redrawn wrongly.</p></div>''','THE ONE RULE')

# ============ PAGE 2 ============
CONST=[('زاوية الكاميرا','Camera angle','من أعلى 10 إلى 15 درجة','10 to 15 degrees above','أعلى يشوّه العبوة، وأقل يخفي الأرضية','higher distorts the pack, lower hides the surface'),
('العدسة','Lens','ما يعادل 50 مم','50 mm equivalent','العدسات الواسعة تقوّس حواف العبوة','wide lenses bow the pack edges'),
('اتجاه الضوء','Light direction','أعلى اليسار بزاوية 45 درجة','upper left at 45 degrees','ثابت واحد يجعل كل الظلال متفقة','one constant keeps every shadow in agreement'),
('نوع الضوء','Light quality','ناعم، مصدر واسع','soft, broad source','الضوء الحاد يكسر ألوان العبوة المطبوعة','hard light breaks the printed pack colours'),
('حرارة اللون','Colour temperature','5200 كلفن، نهار محايد','5200 K neutral daylight','حتى لا تتغير ألوان العلامة','so the brand colours do not shift'),
('الظل','Shadow','ظل تلامس ناعم تحت العبوة','soft contact shadow beneath','بدونه تبدو العبوة طائرة','without it the pack floats'),
('عمق الميدان','Depth of field','العبوة حادة، الخلفية ناعمة','pack sharp, background soft','العبوة هي البطل دائمًا','the pack is always the hero'),
('نسبة التصوير','Capture ratio','مربع 1:1 ثم يُقتطع','square 1:1 then cropped','مصدر واحد يخدم الفيد والستوري','one source serves feed and story')]
rows=''.join(f'<tr><td><b>{a}</b><span class="en">{b}</span></td><td class="ar">{c}<span class="en">{d}</span></td>'
             f'<td class="ar sm">{e}<span class="en">{f}</span></td></tr>' for a,b,c,d,e,f in CONST)

page(f'''{eb('مكتبة المصادر','02 · THE SOURCE LIBRARY')}
<div class="ok"><b>كل ما يلزم موجود بالفعل. لا شيء ينتظر العميل.</b>
<span class="en">Everything needed already exists. Nothing waits on the client.</span></div>
<table class="t3"><thead><tr><th>المجلد · FOLDER</th><th>المحتوى · CONTENTS</th><th>الحالة · STATE</th></tr></thead><tbody>
<tr><td class="mono">packshots/single/</td><td>5 بيبو · 5 الراوي · 4 تومان · 4 بوليكا</td><td>مقصوصة شفافة · cut out</td></tr>
<tr><td class="mono">packshots/</td><td>خمسة صفوف كاملة · five range lineups</td><td>جاهزة · ready</td></tr>
<tr><td class="mono">logos-transparent/</td><td>العلامات الأربع والختم · four marks and the seal</td><td>جاهزة · ready</td></tr>
</tbody></table>
<div class="note warn"><b>قاعدة الدقة · The resolution rule</b>
<p class="ar">لا تُكبَّر عبوة فوق حجمها الأصلي أبدًا. إذا احتاج المشهد عبوة أكبر، صغّر المشهد، لا تكبّر العبوة.</p>
<p class="en">Never scale a pack above its source size. If a scene needs a larger pack, shrink the scene, do not enlarge the pack.</p></div>

{eb('الثوابت','03 · THE CONSTANTS')}
{bi('هذه القيم لا تتغير أبدًا، في أي مجموعة وفي أي صورة. هي السبب الوحيد في أن ثمانية عشر منتجًا تبدو عائلة واحدة. المجموعة تغيّر العالم من حولها، لا هذه القيم.',
    'These values never change, on any range, in any image. They are the only reason eighteen products read as one family. The range changes the world around them, never these.')}
<table class="t3 cn"><thead><tr><th>الثابت · CONSTANT</th><th>القيمة · VALUE</th><th>لماذا · WHY</th></tr></thead><tbody>{rows}</tbody></table>
<div class="note"><b>القاعدة التي تلخص ما سبق · The rule that summarises all of it</b>
<p class="ar">العبوة هي البطل، والمشهد خادم. إذا سرق المشهد الانتباه، فالصورة مرفوضة.</p>
<p class="en">The pack is the hero and the scene is the servant. If the scene takes the attention, the image is rejected.</p></div>''','CONSTANTS')

# ============ PAGE 3 ============
WORLDS=[('بيبو','BeBo','#1BA34C','مطبخ بيت، سطح نظيف','a home kitchen, a clean counter','خشب فاتح أو سطح ورقي','light wood or a paper surface','ضوء صباح من نافذة','morning window light','هادئ، مرتب، بيت شغّال','calm, tidy, a house that works','لا تُظهر العبوة وهي تُحضَّر أو يُشرب منها','never show the pack being prepared or drunk from'),
('الراوي','AlRawy','#1B4F9C','طاولة نظيفة أو حقيبة مدرسة','a clean table, or an open school bag','سطح فاتح محايد','a light neutral surface','نهار صافٍ','clear daylight','اطمئنان، لا إثارة','reassurance, never excitement','لا أكوام فاكهة توحي بنسبة عصير','no fruit piles implying juice content'),
('تومان','2MAN','#29ABE2','خارج البيت، شارع أو شاطئ','outdoors, a street or a beach','ثلج، ماء، إسمنت ساخن','ice, water, hot concrete','شمس قوية مباشرة','strong direct sun','حركة، برودة، النهار ملكك','motion, cold, the day is yours','العبوتان العادية و«أشكال» لهما نفس العالم','both packs share one world'),
('بوليكا','POLEKA','#EC008C','خلفية لون مسطّح، بلا واقعية','a flat colour ground, no realism','لون واحد صريح','one plain colour','ناعم ومتساوٍ','soft and even','لعب. الشخصية أولًا','play. Character first','صنف الكولا لا يظهر في أي إعلان مدفوع','the cola SKU appears in no paid campaign')]
wb=''
for ar,en,sig,pa,pe,sa,se,la,le,ma,me,fa,fe in WORLDS:
    wb+=f'''<div class="wld"><div class="wh" style="border-left:1.2mm solid {sig}">
    <b class="ar">{ar}</b><span>{en}</span></div>
    <table class="wt"><tbody>
    <tr><td class="k">المكان · Place</td><td class="ar">{pa}<span class="en">{pe}</span></td></tr>
    <tr><td class="k">الأرضية · Surface</td><td class="ar">{sa}<span class="en">{se}</span></td></tr>
    <tr><td class="k">الضوء · Light</td><td class="ar">{la}<span class="en">{le}</span></td></tr>
    <tr><td class="k">المزاج · Mood</td><td class="ar">{ma}<span class="en">{me}</span></td></tr>
    <tr class="no"><td class="k">ممنوع · Forbidden</td><td class="ar"><b>{fa}</b><span class="en"><b>{fe}</b></span></td></tr>
    </tbody></table></div>'''

page(f'''{eb('عوالم المشاهد','04 · THE SCENE WORLDS')}
{bi('لكل مجموعة عالمها. الثوابت لا تتغير، لكن المكان والأرضية والمزاج يتغيرون. العالم هو ما يفصل المجموعات عن بعضها، تمامًا كما تفعل ألوانها على الرف.',
    'Each range has its world. The constants never change, but the place, the surface and the mood do. The world is what separates the ranges, exactly as their colours do on a shelf.')}
<div class="wlds">{wb}</div>
<div class="note warn"><b>سبب منع بيبو · Why the BeBo ban, and it is a real one</b>
<p class="ar">شكل استخدام بيبو غير محسوم بعد. الصورة التي تُظهر طريقة الاستخدام تعلن إجابة لا نملكها. تنتظر صورة ظهر العبوة.</p>
<p class="en">BeBo's format is not yet settled. An image showing how it is used asserts an answer we do not have. It waits on a photo of the back of the pack.</p></div>''','SCENE WORLDS')

# ============ PAGE 4 ============
PR=[('BeBo','#1BA34C','Empty home kitchen counter, no products, pale wood surface, soft morning window light from upper left at 45 degrees, blurred warm kitchen background, calm and tidy, 50mm lens, camera 12 degrees above the surface, square 1:1, clear empty space in the centre foreground'),
('AlRawy','#1B4F9C','Empty clean light table top, no products, one whole fresh peach resting to the right, clear daylight from upper left at 45 degrees, soft neutral background, calm and reassuring, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre'),
('2MAN','#29ABE2','Empty wet concrete surface with scattered ice cubes and water droplets, no products, strong direct sunlight from upper left, blurred bright outdoor street background, high energy summer, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre'),
('POLEKA','#EC008C','Flat solid colour studio background, no products, soft even light from upper left, no texture, no realism, playful and bright, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre')]
pb=''.join(f'<div class="pr"><b style="color:{c}">{n}</b><code>{t}</code></div>' for n,c,t in PR)

page(f'''{eb('صيغة الأمر','05 · THE PROMPT FORMULA')}
<div class="rule sm">{cnr()}
 <p class="ar rl">اطلب الغرفة، لا تطلب المنتج.</p>
 <p class="rl en">ASK FOR THE ROOM, NEVER FOR THE PRODUCT.</p></div>
{bi('هذه هي الحيلة الكاملة. لا تطلب «عبوة عصير على طاولة»، لأن المولّد سيرسم عبوة مختلَقة. اطلب مشهدًا فارغًا فيه مساحة خالية واضحة، ثم ركّب العبوة الحقيقية في تلك المساحة.',
    'This is the whole trick. Never ask for "a juice pack on a table", because the generator will draw a fabricated pack. Ask for an empty set with a clear open space, then composite the real pack into it.')}
<div class="fm2"><code>[EMPTY SCENE, no product] + [SURFACE] + [LIGHT] + [BACKGROUND] + [MOOD]<br>
+ [CAMERA: 50mm, 12&deg; above, soft key upper-left 45&deg;] + [square 1:1]<br>
+ [clear empty space, centre, for compositing]</code></div>
<div class="note"><b>الأوامر بالإنجليزية، وهذا مقصود · Prompts are in English, deliberately</b>
<p class="ar">المولّدات تفهم الإنجليزية أفضل بكثير. هذا الاستثناء الوحيد لقاعدة «العربية أولًا»، لأن الأمر أداة داخلية لا يراها أحد خارج الوكالة.</p>
<p class="en">Generators understand English far better. This is the one exception to the Arabic first rule, because a prompt is an internal tool nobody outside the agency sees.</p></div>
<div class="prs">{pb}</div>

{eb('ما يُستبعد من كل أمر','06 · WHAT EVERY PROMPT EXCLUDES')}
<div class="neg"><code>no text, no lettering, no arabic script, no logos, no brands, no packaging,<br>
no bottles, no sachets, no hands, no people, no faces, no watermark</code></div>
{bi('أهم بند هو منع أي كتابة. المولّد إذا كتب حرفًا واحدًا، ولو في الخلفية، فقد صنع لغة مزيفة على صورة علامة غذائية. والثاني منع الأيدي والوجوه: أيدي الذكاء الاصطناعي غالبًا خاطئة، ولا تملك الوكالة إذن تصوير لأي شخص.',
    'The most important entry is the ban on lettering. If the generator writes one character, even in the background, it has invented a fake language on a food brand image. The second is hands and faces: AI hands are frequently wrong, and the agency holds no model release for anybody.')}''','PROMPTS')

# ============ PAGE 5 ============
COMP=[('1','الحجم','Scale','ارتفاع العبوة بين 55٪ و70٪ من الإطار','pack height 55% to 70% of frame height'),
('2','الوضع','Placement','قاعدة العبوة على مستوى السطح','pack base sits on the surface plane'),
('3','ظل التلامس','Contact shadow','أغمق عند التلامس ثم يتلاشى','darkest at contact, then fading'),
('4','الظل الملقى','Cast shadow','أسفل اليمين دائمًا، لأن الضوء من أعلى اليسار','always down and right, because the key is upper left'),
('5','انعكاس اللون','Colour spill','لون المشهد على حواف العبوة 5٪ إلى 10٪','scene colour on the pack edges at 5% to 10%'),
('6','الحافة','Edge','تنعيم بكسل واحد، بلا هالة بيضاء','one pixel feather, no white halo'),
('7','الفحص','Check','افحص القص على أسود وأبيض','check the cutout on black and on white')]
cb=''.join(f'<tr><td class="n">{n}</td><td><b class="ar">{a}</b><span class="en">{e}</span></td>'
           f'<td class="ar">{ra}<span class="en">{re}</span></td></tr>' for n,a,e,ra,re in COMP)
REJ=[('أي حرف لم يأتِ من فن العبوة الأصلي','any lettering not from the original pack artwork'),
('أي شعار لم يأتِ من مجلد العلامات','any mark not taken from the logos folder'),
('عبوة بلا ظل تلامس، أي عبوة طائرة','a pack with no contact shadow, a floating pack'),
('ظل العبوة في اتجاه مخالف لظل المشهد','the pack shadow disagreeing with the scene'),
('هالة بيضاء حول القص','a white halo around the cutout'),
('يد أو وجه أو شخص','a hand, a face, or a person'),
('فاكهة لا تخص النكهة المعروضة','fruit that is not the flavour shown'),
('بيبو وهي تُحضَّر أو يُشرب منها','BeBo being prepared or drunk from'),
('صنف كولا بوليكا في أي مادة مدفوعة','the POLEKA cola SKU in any paid material'),
('عبوة مكبَّرة فوق دقتها الأصلية','a pack enlarged beyond its source resolution')]
rb=''.join(f'<li><i>{i+1}</i><span class="ar">{a}</span><span class="en">{e}</span></li>' for i,(a,e) in enumerate(REJ))

page(f'''{eb('قواعد التركيب','07 · THE COMPOSITING RULES')}
{bi('هذا القسم هو الفرق بين صورة تبدو حقيقية وصورة تبدو ملصقة. كلها خطوات صغيرة، وكل واحدة تُرى فورًا إذا نُسيت.',
    'This section is the difference between an image that looks real and one that looks pasted. All small steps, and every one is visible the moment it is skipped.')}
<table class="t3 cp"><tbody>{cb}</tbody></table>
<div class="note"><b>البند الخامس هو الذي يقنع العين · Item 5 is the one that convinces the eye</b>
<p class="ar">عبوة لم يلمسها لون المكان تبدو دائمًا كأنها من صورة أخرى، حتى لو كان الظل مثاليًا.</p>
<p class="en">A pack the room's colour has not touched always looks like it came from another photograph, even when the shadow is perfect.</p></div>

{eb('قائمة الرفض','08 · THE REJECT LIST')}
<div class="ok warn"><b>أي صورة تحمل واحدًا من هذه لا تُنشَر ولا تُصلَح، بل تُعاد.</b>
<span class="en">Any image carrying one of these is not published and not patched. It is redone.</span></div>
<ol class="rej">{rb}</ol>''','COMPOSITING')

# ============ PAGE 6 ============
CLAIM=[('رموز الصحة: صالة رياضية، رياضي، معمل','health signifiers: a gym, an athlete, a laboratory','ادعاء طبي غير موثَّق','an unsupported medical claim'),
('أوراق خضراء حول منتج مسحوق','green leaves around a powdered product','يوحي بمحتوى طبيعي لا يؤكده الملصق','implies a natural content the label does not support'),
('كومة فاكهة توحي بنسبة عصير','a fruit pile implying juice content','الراوي نكتار وليس عصيرًا','AlRawy is a nectar, not a juice'),
('زيّ مدرسي أو شعار مدرسة','a school uniform or badge','يوحي باعتماد لا وجود له','implies an endorsement that does not exist'),
('منتج منافس داخل الإطار','a competitor product in frame','مقارنة مباشرة ممنوعة','a direct comparison, which is banned'),
('واجهة محل محدَّد','a named shop front','وعد توفّر لا تملكه الوكالة','an availability promise the agency does not hold'),
('أي رقم غذائي مكتوب','any nutritional number set in type','يحتاج ورقة مواصفات مكتوبة','needs the written spec sheet')]
clb=''.join(f'<tr><td class="ar">{a}<span class="en">{e}</span></td><td class="ar sm">{wa}<span class="en">{we}</span></td></tr>' for a,e,wa,we in CLAIM)
OUT=[('المصدر · Master','2048 × 2048','يُحفظ دائمًا · always kept'),
('منشور فيد · Feed','1080 × 1350','فيسبوك أولًا · Facebook first'),
('مربع · Square','1080 × 1080',''),
('ستوري وريلز · Story','1080 × 1920','العبوة في الثلث الأوسط · pack in the middle third'),
('صورة الحساب · Profile','320 × 320','تُعرض دائرية · shown as a circle'),
('صورة جوجل · GBP','1200 × 900','كحد أدنى · minimum')]
ob=''.join(f'<tr><td>{a}</td><td class="mono">{b}</td><td class="sm">{c}</td></tr>' for a,b,c in OUT)
CHK=[('العبوة من مجلد المصادر ولم تُولَّد','pack came from the source folder, not generated'),
('لا يوجد أي حرف في المشهد','no lettering anywhere in the scene'),
('ظل التلامس موجود وناعم','contact shadow present and soft'),
('اتجاه الظل يوافق الضوء من أعلى اليسار','shadow agrees with the upper left key'),
('لا توجد هالة حول حواف العبوة','no halo on the pack edges'),
('لون المشهد لمس حواف العبوة','the scene colour has touched the pack edges'),
('لا يد، لا وجه، لا شخص','no hand, no face, no person'),
('لا ادعاء صحي ولا نسبة فاكهة ولا رقم غذائي','no health cue, no fruit ratio, no nutritional number'),
('بيبو ليست معروضة أثناء التحضير أو الشرب','BeBo not shown being prepared or drunk from'),
('صنف كولا بوليكا خارج أي مادة مدفوعة','POLEKA cola out of all paid material')]
kb=''.join(f'<li><i></i><span class="ar">{a}</span><span class="en">{e}</span></li>' for a,e in CHK)

page(f'''{eb('الادعاءات داخل الصورة','09 · CLAIMS INSIDE THE PICTURE')}
{bi('قائمة الممنوعات في دليل الصوت تنطبق على الصور بنفس القوة. الصورة ادعاء منشور مثلها مثل الجملة، وصفحة الطعام يمكن الإبلاغ عنها، والحساب الإعلاني يمكن تقييده، بسبب صورة واحدة.',
    'The never say list applies to pictures with equal force. An image is a published claim exactly as a sentence is, and a food page can be reported, and an ad account restricted, over a single image.')}
<table class="t3 cl"><thead><tr><th>ممنوع بصريًا · VISUALLY FORBIDDEN</th><th>لماذا · WHY</th></tr></thead><tbody>{clb}</tbody></table>
<div class="note warn"><b>المبدأ الحاكم · The governing principle</b>
<p class="ar">ما لم يصل من العميل مكتوبًا، لا تعرفه الوكالة، ولا ترسمه.</p>
<p class="en">If it did not arrive from the client in writing, the agency does not know it, and does not draw it.</p></div>''','CLAIMS')

page(f'''<div class="two">
<div><div class="eb"><span>10 · OUTPUT SPECS</span><i></i><b class="ar">المقاسات</b></div>
<table class="t3 sm2"><tbody>{ob}</tbody></table>
<p class="fn">PNG للمصدر، JPG بجودة 90 للنشر · PNG master, JPG q90 to publish<br>
<span class="mono">range-sku-format-NN</span></p></div>
<div><div class="eb"><span>11 · TOOLCHAIN</span><i></i><b class="ar">أدوات العمل</b></div>
<table class="t3 sm2"><tbody>
<tr><td>توليد المشهد · Generation</td><td class="sm">داخل جلسة الوكالة · in the agency session</td></tr>
<tr><td>القص · Cutting out</td><td class="sm">غير مطلوب · not needed</td></tr>
<tr><td>التركيب · Compositing</td><td class="sm">تطبيق طبقات على الآيباد · a layers app on iPad</td></tr>
<tr><td>النص · Typesetting</td><td class="sm">IBM Plex, مجاني · free</td></tr></tbody></table>
<p class="fn">أسعار أدوات التوليد تتغير، ولا يُكتب رقم لا يمكن التحقق منه. يُسعَّر أي اشتراك قبل اختياره.<br>
Generation pricing changes constantly. Any subscription is priced before it is chosen.</p></div></div>

{eb('قائمة المراجعة قبل النشر','12 · THE PRE PUBLISH CHECKLIST')}
<ol class="chk">{kb}</ol>''','CHECKLIST')

CSS=f'''
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:{PAPER};color:{INK};
 font-family:'IBM Plex Sans',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:14mm 14mm 20mm;position:relative;overflow:hidden;
 background:{PAPER};page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto}}
.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;line-height:1.75;text-align:right}}
.mono{{font-family:'IBM Plex Mono',monospace}}
b,strong{{font-weight:700}}
.eb{{display:flex;align-items:center;gap:3mm;margin:4.4mm 0 2.2mm}}
.eb > span{{font-size:6pt;font-weight:700;letter-spacing:.2em;color:{RED};text-transform:uppercase;white-space:nowrap}}
.eb > i{{flex:1;height:0.25mm;background:{SILVER}}}
.eb > b.ar{{font-size:8pt;font-weight:400;color:{SLATE}}}
.page > .eb:first-child{{margin-top:0}}
.cnr{{position:absolute;width:4mm;height:4mm;border:0.5mm solid {RED};z-index:3}}
.cnr.tl{{top:2.5mm;left:2.5mm;border-right:0;border-bottom:0}}
.cnr.tr{{top:2.5mm;right:2.5mm;border-left:0;border-bottom:0}}
.cnr.bl{{bottom:2.5mm;left:2.5mm;border-right:0;border-top:0}}
.cnr.br{{bottom:2.5mm;right:2.5mm;border-left:0;border-top:0}}
/* hero */
.hero{{position:relative;background:{DEEP};color:{PAPER};padding:8mm 9mm;overflow:hidden;min-height:34mm;
 display:flex;align-items:center}}
.hero .hx{{position:relative;z-index:2;flex:1}}
.hero h1{{font-size:21pt;font-weight:700;margin:0;line-height:1.4;direction:rtl;text-align:right;
 font-family:'IBM Plex Sans Arabic',sans-serif}}
.hero h2{{font-size:12pt;font-weight:700;margin:1.5mm 0 0;letter-spacing:.14em}}
.sub{{font-size:6.8pt;color:#B9B5D8;margin:2.5mm 0 0;letter-spacing:.04em;line-height:1.6}}
.hero p.ar.sub{{text-align:right}}
/* the rule panel */
.rule{{position:relative;background:{RED};color:#FFF;padding:7mm 9mm;text-align:center;overflow:hidden;margin-bottom:2.5mm}}
.rule.sm{{padding:5mm 9mm}}
.rule p.rl{{margin:0;font-weight:700;position:relative;z-index:2}}
.rule p.ar.rl{{font-size:17pt;line-height:1.5;text-align:center;
 font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl}}
.rule.sm p.ar.rl{{font-size:14pt}}
.rule p.rl.en{{font-size:8.5pt;letter-spacing:.16em;margin-top:2mm;opacity:.92}}
.rule .cnr{{border-color:#FFF}}
/* bilingual block */
.bi{{margin:0 0 2.5mm}}
.bi > p{{margin:0;font-size:7.4pt;line-height:1.7;color:{GRAPH}}}
.bi > p.ar{{font-size:8pt;color:{INK};margin-bottom:1.2mm}}
/* tables */
table.t3{{width:100%;border-collapse:collapse;margin:0 0 2.5mm}}
table.t3 th{{font-size:5.8pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{SLATE};
 text-align:left;padding:0 2.5mm 1.5mm;border-bottom:0.3mm solid {SILVER}}}
table.t3 td{{font-size:7pt;line-height:1.5;padding:1.7mm 2.5mm;border-bottom:0.2mm solid {SILVER};
 vertical-align:top;color:{GRAPH}}}
table.t3 td > b{{color:{INK};display:inline}}
table.t3 td.ar{{font-size:7.6pt;color:{INK}}}
table.t3 td.sm{{font-size:6.6pt;color:{SLATE}}}
table.t3 td span.en{{display:block;font-family:'IBM Plex Sans',sans-serif;direction:ltr;text-align:left;
 font-size:6.4pt;color:{SLATE};margin-top:0.6mm;line-height:1.5}}
table.t3 td.n{{font-family:'IBM Plex Mono',monospace;color:{RED};font-weight:700;width:7mm;font-size:8pt}}
table.t3.cn td:first-child{{width:34mm}} table.t3.cn td:nth-child(2){{width:52mm}}
table.t3.cp td:nth-child(2){{width:42mm}}
table.t3.cl td:first-child{{width:50%}}
table.t3.sm2 td{{font-size:6.6pt;padding:1.4mm 2mm}}
/* notes */
.note{{background:{MIST};border-left:0.8mm solid {RED};padding:3mm 4.5mm;margin:0 0 2.5mm}}
.note.warn{{border-left-color:{INK}}}
.note > b{{font-size:7.6pt;display:inline;color:{INK}}}
.note > p{{font-size:7pt;line-height:1.65;margin:1.2mm 0 0;color:{GRAPH}}}
.note > p.ar{{font-size:7.6pt;color:{INK}}}
.ok{{background:{DEEP};color:{PAPER};padding:2.6mm 4.5mm;margin:0 0 2.5mm;
 font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;text-align:right;font-size:8pt}}
.ok.warn{{background:{INK}}}
.ok > b{{display:inline;font-weight:700}}
.ok > span.en{{display:block;direction:ltr;text-align:left;font-family:'IBM Plex Sans',sans-serif;
 font-size:6.6pt;color:#C9C5BC;margin-top:1mm;letter-spacing:.02em}}
/* scene worlds */
.wlds{{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-bottom:2.5mm}}
.wld{{background:#FFF;border:0.25mm solid {SILVER}}}
.wh{{padding:2.4mm 3mm;display:flex;align-items:baseline;gap:2.5mm;background:{MIST}}}
.wh > b.ar{{font-size:11pt;font-weight:700;color:{INK}}}
.wh > span{{font-size:7pt;font-weight:700;letter-spacing:.12em;color:{SLATE};margin-left:auto}}
table.wt{{width:100%;border-collapse:collapse}}
table.wt td{{font-size:6.6pt;padding:1.6mm 3mm;border-bottom:0.2mm solid {MIST};vertical-align:top;color:{INK}}}
table.wt td.k{{width:22mm;font-size:5.8pt;font-weight:700;letter-spacing:.08em;color:{SLATE};
 text-transform:uppercase;font-family:'IBM Plex Sans',sans-serif}}
table.wt td.ar{{font-size:7pt}}
table.wt td span.en{{display:block;direction:ltr;text-align:left;font-family:'IBM Plex Sans',sans-serif;
 font-size:6pt;color:{SLATE};margin-top:0.5mm;line-height:1.45}}
table.wt tr.no td{{background:#FDF0EF}}
table.wt tr:last-child td{{border-bottom:0}}
/* prompts */
.fm2{{background:{INK};padding:3.5mm 4.5mm;margin:0 0 2.5mm}}
.fm2 > code{{font-family:'IBM Plex Mono',monospace;font-size:6.6pt;line-height:1.85;color:#8DC63F}}
.prs{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm}}
.pr{{background:#FFF;border:0.25mm solid {SILVER};padding:2.6mm 3mm}}
.pr > b{{font-size:8pt;display:block;margin-bottom:1.4mm;letter-spacing:.06em}}
.pr > code{{font-family:'IBM Plex Mono',monospace;font-size:5.6pt;line-height:1.7;color:{GRAPH};display:block}}
.neg{{background:{INK};padding:3mm 4.5mm;margin:0 0 2.5mm}}
.neg > code{{font-family:'IBM Plex Mono',monospace;font-size:6.6pt;line-height:1.8;color:#FF8A82}}
/* lists */
ol.rej{{list-style:none;margin:0;padding:0;columns:2;column-gap:5mm}}
ol.rej li{{break-inside:avoid;display:grid;grid-template-columns:4mm 1fr;gap:0 2mm;padding:1.4mm 0;
 border-bottom:0.2mm solid {SILVER}}}
ol.rej li > i{{font-style:normal;font-family:'IBM Plex Mono',monospace;font-size:6.4pt;font-weight:700;
 color:{RED};grid-row:1/3}}
ol.rej li > span.ar{{font-size:6.8pt;color:{INK};line-height:1.5}}
ol.rej li > span.en{{font-size:5.6pt;color:{SLATE};line-height:1.4}}
ol.chk{{list-style:none;margin:0;padding:0;columns:2;column-gap:5mm}}
ol.chk li{{break-inside:avoid;display:grid;grid-template-columns:3.4mm 1fr;gap:0 2mm;padding:1.3mm 0;
 border-bottom:0.2mm solid {SILVER}}}
ol.chk li > i{{width:2.8mm;height:2.8mm;border:0.3mm solid {INK};display:block;grid-row:1/3;margin-top:0.6mm}}
ol.chk li > span.ar{{font-size:6.6pt;color:{INK};line-height:1.5}}
ol.chk li > span.en{{font-size:5.6pt;color:{SLATE};line-height:1.4}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:5mm}}
.fn{{font-size:6pt;line-height:1.6;color:{SLATE};margin:0}}
/* footer */
footer{{position:absolute;left:14mm;right:14mm;bottom:9mm;display:flex;justify-content:space-between;
 align-items:center;font-size:6pt;letter-spacing:.14em;text-transform:uppercase;font-weight:700;
 color:{SLATE};border-top:0.25mm solid {SILVER};padding-top:2.5mm}}
footer .fm{{display:flex;align-items:center;gap:2mm}}
footer .fm > b{{color:{INK};letter-spacing:.1em}}
footer .fm > em{{font-family:'IBM Plex Sans Arabic',sans-serif;font-style:normal;direction:rtl;
 font-weight:400;letter-spacing:0;text-transform:none;font-size:7pt}}
'''
html=f'''<!doctype html><html lang="ar" dir="ltr"><head><meta charset="utf-8">
<title>Alex Foods - Shooting and Compositing Recipe v1.0</title>
<link rel="stylesheet" href="plex.css"><style>{CSS}</style></head><body>{''.join(H)}</body></html>'''
html=html.replace('@@TOTAL@@', str(PAGES[0]))
io.open(os.path.join(HERE,'recipe.html'),'w',encoding='utf-8').write(html)
print("pages:",PAGES[0])
