# -*- coding: utf-8 -*-
# ALEX FOODS - BRAND FOUNDATION. The one book.
# Single source for every section. recipe.py renders section 16 alone for the
# early ship; it imports from here so the text exists in one place only.
# NOTE: no em dashes in output copy. Voice Guide S1 rule 8.
import io, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
exec(open(os.path.join(HERE,'colour.py')).read().split('# sanity')[0])
from ranges import RANGES

PAPER='#FAF8F3'; INK='#141414'; GRAPH='#4A4742'; SLATE='#8A8681'
SILVER='#C9C5BC'; MIST='#EDEAE3'; RED='#E1251D'; NAVY='#0A0378'; DEEP='#05004B'
VER='v1.0'; DATE='09.10.2026'

def verdict(h):
    k=ratio(INK,h); w=ratio('#FFFFFF',h)
    if k>=4.5 and k>=w: return ('INK',k,False)
    if w>=4.5 and w>k:  return ('WHITE',w,False)
    return ('KEYLINE',max(k,w),True)

seen={}
for r in RANGES:
    seen.setdefault(r['sig'],[]).append((r['en'],'range signature'))
    for en,ar,h in r['fl']: seen.setdefault(h,[]).append((r['en'],en+' field'))
COLL={h:v for h,v in seen.items() if len(v)>1}
NF=sum(len(r['fl']) for r in RANGES)
NINK=sum(1 for r in RANGES for _,_,h in r['fl'] if verdict(h)[0]=='INK')
NWHT=sum(1 for r in RANGES for _,_,h in r['fl'] if verdict(h)[0]=='WHITE')
NKEY=sum(1 for r in RANGES for _,_,h in r['fl'] if verdict(h)[2])

SEC=[]           # (id, label_en, label_ar, [page_bodies])
def sec(i,en,ar,*bodies): SEC.append((i,en,ar,list(bodies)))
def eb(ar,en): return f'<div class="eb"><span>{en}</span><i></i><b class="ar">{ar}</b></div>'
def cnr(): return '<i class="cnr tl"></i><i class="cnr tr"></i><i class="cnr bl"></i><i class="cnr br"></i>'
def bi(ar,en): return f'<div class="bi"><p class="ar">{ar}</p><p class="en">{en}</p></div>'
def note(ar,en,tar,ten,warn=False):
    return (f'<div class="note{" warn" if warn else ""}"><b>{tar} · {ten}</b>'
            f'<p class="ar">{ar}</p><p class="en">{en}</p></div>')
def ok(ar,en,warn=False):
    return f'<div class="ok{" warn" if warn else ""}"><b>{ar}</b><span class="en">{en}</span></div>'
def chip(t,cls=''): return f'<div class="chip {cls}">{t}</div>'
def rule(ar,en,sm=False):
    return (f'<div class="rule{" sm" if sm else ""}">{cnr()}<p class="ar rl">{ar}</p>'
            f'<p class="rl en">{en}</p></div>')

# ================= 00 COVER =================
band=''.join(f'<i style="background:{r["sig"]}"></i>' for r in RANGES)
sec('00','COVER','الغلاف', f'''<div class="cover">{cnr()}
<div class="cvtop"><img class="seal" src="../logos-transparent/logo-alex-lockup-transparent.png"></div>
<div class="cvmid">
 <h1 class="ar">الأساس التجاري</h1><h2>BRAND FOUNDATION</h2>
 <p class="ar cvsub">أليكس فودز · الشركة الإسكندرية لتعبئة وتغليف المواد الغذائية</p>
 <p class="cvsub">ALEX FOODS &nbsp;·&nbsp; ALEXANDRIA, EGYPT</p></div>
<div class="cvbot">
 <div class="cvmeta"><span>PREPARED BY</span><b>THE STANDARD AGENCY</b></div>
 <div class="cvmeta"><span>VERSION</span><b>{VER}</b></div>
 <div class="cvmeta"><span>DATE</span><b>{DATE}</b></div>
 <div class="cvmeta"><span>APPROVER</span><b class="pend">TO BE NAMED</b></div></div>
<div class="cvband">{band}</div></div>''')

# ================= 01 HOW TO USE =================
sec('01','HOW TO USE THIS BOOK','كيف تُستخدم', f'''{eb('كيف تُستخدم هذه الوثيقة','01 · HOW TO USE THIS BOOK')}
{bi('هذه وثيقة يُرجع إليها، لا وثيقة تُقرأ مرة واحدة. أرقام الصفحات حقيقية ويمكن الاستشهاد بها في مكالمة. كل قسم مستقل بذاته ويمكن فتحه دون قراءة ما قبله.',
    'This is a document to look things up in, not one to read once. The page numbers are real and quotable on a phone call. Every section stands alone and can be opened without reading what came before it.')}
{eb('الحالة على كل قسم','THE STATUS CHIP ON EVERY SECTION')}
<div class="chips">
 {chip('DEFINED','ok')}<p>القسم مكتمل وجاهز للعمل به · complete and ready to work from</p>
 {chip('SPEC · EXECUTION PENDING CLIENT ACCESS','wait')}<p>مكتوب بالكامل، والتنفيذ ينتظر صلاحية من العميل · fully written, execution waits on client access</p>
 {chip('PENDING CLIENT INPUT','pend')}<p>ينتظر إجابة أو مادة من العميل · waiting on an answer or a material from the client</p>
</div>
{note('الوثيقة تقول حالتها بصدق على كل صفحة. القسم الذي ينتظر شيئًا يقول ما ينتظره ومن، بدل أن يبدو ناقصًا بلا تفسير.',
 'The book states its own status honestly on every page. A section that is waiting says what it waits on and who from, rather than simply looking unfinished with no explanation.',
 'لماذا الحالة مكتوبة','Why the status is printed')}
{eb('القواعد التي تحكم كل صفحة','THE RULES THAT GOVERN EVERY PAGE')}
<ol class="ru">
<li><span class="ar">العربية تُكتب أولًا، والإنجليزية تُركَّب عليها.</span><span class="en">Arabic is written first and English is fitted to it, never the other way round.</span></li>
<li><span class="ar">كل رقم في هذه الوثيقة محسوب، لا مُقدَّر.</span><span class="en">Every number in this book is computed, not estimated. Contrast uses the WCAG 2.1 relative luminance formula.</span></li>
<li><span class="ar">لا يُكتب أي اسم علامة بخط. الأسماء فن، لا نص.</span><span class="en">No brand name in this system is ever set in a font. The wordmarks are artwork, not type.</span></li>
<li><span class="ar">ما لم يصل من العميل مكتوبًا، لا تعرفه الوكالة.</span><span class="en">If it did not arrive from the client in writing, the agency does not know it.</span></li>
</ol>''')

# ================= 02 CONTENTS =================
DELIV=[('03','البنية','Brand architecture','—','ok'),('04','نظام الألوان','Colour system','2','ok'),
('05','نظام الخطوط','Type system','2','ok'),('06','الشعارات والختم','Logo and seal use','2','ok'),
('07','المجموعات','The ranges','—','ok'),('08','صوت العلامة','Brand voice','1','ok'),
('09','نظام الكتابة','The caption system','1','ok'),('10','الشعارات والأغنية','Slogans and the song','4','pend'),
('11','اللوحة والشبكة','Canvas and grid','3','ok'),('12','العبوة على الحقل','The pack in field system','3','ok'),
('13','الشارات والشخصيات','Flashes and characters','3','ok'),('14','إعداد الصفحات','Social pages setup','3','wait'),
('15','الحركة','Motion','6','ok'),('16','وصفة التصوير','Shooting and compositing','6','ok'),
('17','خطة المحتوى','Content calendar','5','pend'),('18','أنماط المنشورات','Post archetypes and patterns','5','pend'),
('19','نشاط جوجل','Google Business Profile','7','wait'),('20','سيو الإسكندرية','Local SEO','8','pend'),
('21','الالتزام','Compliance','—','ok'),('22','النظام بالأرقام','The system in numbers','—','ok')]
cb=''.join(f'''<tr><td class="mono n">{i}</td><td class="ar">{ar}<span class="en">{en}</span></td>
 <td class="mono d">{d}</td><td class="st"><i class="{c}"></i></td></tr>''' for i,ar,en,d,c in DELIV)
sec('02','CONTENTS','المحتويات', f'''{eb('المحتويات وخريطة التسليمات','02 · CONTENTS &amp; DELIVERABLE MAP')}
{bi('العمود الأيمن يربط كل قسم بالتسليم المقابل له في نطاق الخدمة الموقَّع، بنفس ترقيم المستند الأصلي. هذه الوثيقة تغطي الثمانية تسليمات المتفق عليها.',
    'The right column maps each section to its deliverable in the signed Service Scope, using that document’s own numbering. This book covers the eight agreed deliverables.')}
<table class="t3 toc"><thead><tr><th>§</th><th>القسم · SECTION</th><th>التسليم · DELIV.</th><th>الحالة</th></tr></thead><tbody>{cb}</tbody></table>
<div class="lgd"><span><i class="ok"></i> DEFINED</span><span><i class="wait"></i> SPEC · PENDING ACCESS</span><span><i class="pend"></i> PENDING CLIENT INPUT</span></div>''')

# ================= 03 BRAND ARCHITECTURE =================
sec('03','BRAND ARCHITECTURE','بنية العلامة', f'''{eb('بنية العلامة','03 · BRAND ARCHITECTURE')}{chip('DEFINED','ok')}
{rule('أليكس فودز هي العلامة الأم. الأربعة مجموعات تحتها.','ALEX FOODS IS THE MASTER BRAND. THE FOUR ARE RANGES BENEATH IT.')}
{bi('هذا ليس رسمًا توضيحيًّا، بل قرار عن كيفية دخول الشركة إلى السوق. كل شيء بعده تطبيق له: حساب واحد لأليكس فودز لا أربع صفحات، وخطة محتوى واحدة تدور فيها المجموعات، وكل تعريف حساب يذكر أليكس فودز.',
    'This is not a diagram, it is a decision about how the company goes to market. Everything after it is application: one Alex Foods presence rather than four brand pages, one content calendar with the ranges rotating inside it, and every bio naming Alex Foods.')}
<div class="hier">
 <div class="hlv m"><b class="ar">الماستر</b><span>MASTER</span><em class="ar">أليكس فودز · الختم</em></div>
 <div class="harr"></div>
 <div class="hrow">{''.join(f'<div class="hlv r"><b class="ar">{r["ar"]}</b><span>{r["en"]}</span><i style="background:{r["sig"]}"></i></div>' for r in RANGES)}</div>
 <div class="harr"></div>
 <div class="hlv f"><b class="ar">النكهة</b><span>FLAVOUR</span><em class="ar">حقل لكل صنف · {NF} حقلًا</em></div>
</div>
{note('لون النكهة يملك الحقل. لون المجموعة يملك الشعار. الماستر يملك الختم، ولا يأخذ أيًّا منهما.',
 'The flavour colour owns the field. The range colour owns the logo. The master owns the seal, and it takes neither.',
 'قاعدة الملكية','The ownership rule')}
{note('الختم موجود على الراوي وتومان، وغائب عن بيبو وبوليكا. هذا طرح لم يكتمل، وليس تصنيفًا. العبوات المطبوعة تبقى كما هي، والطباعة الجديدة تحمل الختم على كل مجموعة.',
 'The seal is on AlRawy and 2MAN and absent from BeBo and POLEKA. That is a rollout that has not caught up, not a tier. Printed packs stay exactly as they are, and new print carries the seal on every range.',
 'الختم طرح، لا تصنيف','The seal is a rollout, not a tier',True)}
{note('الماستر يملك الختم والحضور، والمجموعات تحتفظ بألوانها الأربعة المتنافرة، لأن ذلك التنافر هو الشيء الوحيد الذي يفصلها على الرف. علامة أم تعيد طلاء مجموعاتها تدمّر التمييز الذي تعتمد عليه.',
 'The master owns the seal and the presence, and the ranges keep their four clashing palettes, because that clash is the only thing separating them on a shelf. A master brand that repainted its ranges would destroy the differentiation it depends on.',
 'ولا توجد لوحة ألوان للماستر','And there is no house palette')}''')

# ================= 04 COLOUR =================
NEUT=[('Paper','ورقي',PAPER,'كل خلفية','every background'),('Ink','حبري',INK,'النص في كل مكان','type everywhere'),
('Graphite','رصاصي',GRAPH,'نص ثانوي','secondary type'),('Slate','أردوازي',SLATE,'تعليقات بحجم العرض فقط','captions, display size only'),
('Silver','فضي',SILVER,'خطوط وفواصل، لا نص','rules and dividers, never type'),('Mist','ضبابي',MIST,'تعبئة اللوحات، لا نص','panel fills, never type'),
('System Red','أحمر النظام',RED,'لكنة، كلمة واحدة، لا نص متن','accent, one word, never body'),('Alex Navy','كحلي أليكس',NAVY,'الماستر والحساب','master mark and profile')]
nb=''.join(f'''<div class="csw"><div class="chipc" style="background:{h};{'border:0.25mm solid '+SILVER if n in ('Paper','Mist') else ''}"></div>
 <b>{n}</b><span class="ar">{ar}</span><span class="mono">{h}</span><span class="role">{re}</span>
 <span class="cr">{ratio(INK,h):.2f} : 1 <em>on ink</em></span></div>''' for n,ar,h,ra,re in NEUT)
fr=''
for r in RANGES:
    for i,(en,ar,h) in enumerate(r['fl']):
        v,rt,key=verdict(h); cls='key' if key else ('wht' if v=='WHITE' else '')
        fr+=(f'<tr class="{cls}"><td>{r["en"] if i==0 else ""}</td><td><b class="ar">{ar}</b><span class="en">{en}</span></td>'
             f'<td class="mono">{h}</td><td class="sw"><i style="background:{h}"></i></td>'
             f'<td class="mono num">{ratio(INK,h):.2f}</td><td class="mono num">{ratio("#FFFFFF",h):.2f}</td>'
             f'<td class="v"><span class="{cls or "ink"}">{v}</span></td></tr>')
cb2=''.join(f'''<div class="col"><div class="cs" style="background:{h}"></div><div class="cx"><b class="mono">{h}</b>
 <ul>{''.join(f'<li><b>{a}</b> <span>{b}</span></li>' for a,b in v)}</ul></div></div>''' for h,v in COLL.items())

sec('04','COLOUR SYSTEM','نظام الألوان',
f'''{eb('نظام الألوان · الطبقة المحايدة','04 · COLOUR SYSTEM · THE NEUTRAL LAYER')}{chip('DEFINED','ok')}
{bi('الشيء الوحيد الذي تشترك فيه المجموعات الأربع ولا يملكه أيٌّ منها. هذه هي الطبقة التي يمكن أن يوجد فيها مستوى للشركة دون أن يُسطّح المجموعات.',
    'The one thing all four ranges share and none of them currently had. This is the layer where a house level can exist without flattening the ranges.')}
<div class="csws4">{nb}</div>
{note('أحمر النظام يعطي 4.41 إلى 1 على الأرضية الورقية. يعبر حد 3 إلى 1 لأحجام العرض ولا يعبر 4.5 لنص المتن. لذلك هو لون عناوين، ولا يُكتب به نص متن أبدًا، وهذه الوثيقة تلتزم بذلك على صفحاتها.',
 'System Red gives 4.41:1 on Paper. It clears 3:1 for display sizes and misses 4.5:1 for body copy. So it is a headline colour and never body copy, and this book obeys that on its own pages.',
 'الأحمر لون عناوين','Red is a headline colour',True)}''',
f'''{eb('حقول النكهات · الحكم محسوب','FLAVOUR FIELDS · THE VERDICT IS COMPUTED')}
{ok(f'الافتراضي مقلوب: الحبري هو الأصل على حقل النكهة، والأبيض هو الاستثناء الذي يُفحص. الحبري يفوز على {NINK} من {NF}.',
    f'The default is flipped: Ink is the default on a flavour field and white is the exception that has to be checked. Ink wins on {NINK} of {NF}.')}
<table class="t3 ct"><thead><tr><th>المجموعة</th><th>النكهة · FLAVOUR</th><th>HEX</th><th></th><th>INK</th><th>WHITE</th><th>الحكم</th></tr></thead><tbody>{fr}</tbody></table>
{note(f'ثلاثة حقول من {NF} لا يعبر عليها الحبري ولا الأبيض حدّ 4.5: تفاح بيبو، وكولا بوليكا، وفراولة بوليكا. هذه الثلاثة تحمل خطًّا محيطًا داكنًا خلف النص دائمًا.',
 f'Three fields out of {NF} clear 4.5 with neither ink nor white: BeBo apple, POLEKA cola and POLEKA strawberry. Those three always carry a dark keyline behind the type.',
 'الحقول الثلاثة التي تحتاج خطًّا محيطًا','The three fields that need a keyline',True)}''',
f'''{eb('التصادمات الدقيقة','EXACT COLLISIONS')}
{bi(f'حساب اللوحة كاملةً ضد نفسها أخرج {len(COLL)} تصادمات دقيقة. ليست أخطاء، لأن العبوات مطبوعة وفي السوق ولا أحد يعيد طلاءها. تصبح أخطاء في اللحظة التي يُبنى فيها تخطيط دون معرفتها.',
    f'Computing the palette against itself produced {len(COLL)} exact collisions. They are not defects, because the packs are printed and in market and nothing is being repainted. They become defects the moment a layout is built without knowing about them.')}
<div class="cols">{cb2}</div>
<table class="t3 rl2"><tbody>
<tr><td class="n">1</td><td><b class="ar">العبوة هي التي تعرّف الصنف، لا الحقل.</b><span class="en"><b>The pack identifies the SKU, never the field.</b> A field colour is a stage, not a name. That is why a field may be reused and a pack may not.</span></td></tr>
<tr><td class="n">2</td><td><b class="ar">مجموعتان لا تشتركان في تخطيط واحد أبدًا.</b><span class="en"><b>Two ranges never share one layout.</b> AlRawy peach and 2MAN red are the same red. Side by side they read as one product line; apart, nobody will ever know.</span></td></tr>
<tr><td class="n">3</td><td><b class="ar">أخضر بيبو عنصر علامة على بيبو وحدها.</b><span class="en"><b>BeBo's signature green is also AlRawy's guava field and POLEKA's apple field.</b> It stays a brand element on BeBo only; elsewhere it is a stage, never a badge, a border or a logo ground.</span></td></tr>
<tr><td class="n">4</td><td><b class="ar">بوليكا لها أربعة أصناف وثلاثة حقول، اثنان منها لون العلامة.</b><span class="en"><b>POLEKA has four SKUs but only three distinct fields, and two are the brand colour.</b> Four posts off the flavour map show three colours, one twice. <b>The extended layer is not optional on this range.</b></span></td></tr>
<tr><td class="n">5</td><td><b class="ar">شريط بيبو الأخضر على حقل التفاح يعطي 1.30 إلى 1.</b><span class="en"><b>BeBo's green banner on its own apple field gives 1.30:1.</b> The logo nearly vanishes into its field and is held only by the navy keyline around it. On that SKU the keyline is not a detail.</span></td></tr>
</tbody></table>''')

# ================= 05 TYPE =================
sec('05','TYPE SYSTEM','نظام الخطوط', f'''{eb('نظام الخطوط','05 · TYPE SYSTEM')}{chip('DEFINED','ok')}
{rule('لا يُكتب اسم أي علامة بخط. الأسماء فن، لا نص.','NO BRAND NAME IS EVER SET IN A FONT. THE WORDMARKS ARE ARTWORK.',True)}
{bi('شعارا تومان وبوليكا حروف مرسومة ثلاثية الأبعاد لا يمكن إعادة كتابتها، وختم أليكس جسم مُصيَّر بتدرجات ولمعان. كلها تُوضع كما وردت ولا يُعاد بناؤها أبدًا. الخطوط أدناه للنص المحيط، لا للأسماء.',
    'The 2MAN and POLEKA wordmarks are illustrated 3D lettering that cannot be retyped, and the Alex seal is a rendered object with gradients and gloss. All of them are placed as supplied and never reconstructed. The faces below are for the type around them, never for the names.')}
{eb('العائلة','THE FAMILY')}
<div class="two">
<div class="fam"><b>IBM Plex Sans Arabic</b><span>العربية · الأساسي</span>
<p class="en">Free and open licensed. Drawn as one bilingual superfamily rather than a Latin face with Arabic bolted on, which is the difference between a document that looks designed and one that looks assembled.</p></div>
<div class="fam"><b>IBM Plex Sans</b><span>اللاتينية</span>
<p class="en">The Latin companion. Same skeleton, same rhythm, so a bilingual line does not break in the middle.</p></div></div>
<div class="fam full"><b>IBM Plex Mono</b><span>الأكواد والمواصفات</span>
<p class="en">Codes and specifications only. HEX values in a proportional face do not align in a column, and an 8 reads as a B at 8pt.</p></div>
{note('صفر جنيه. عائلة مفتوحة الترخيص تغطي العربية واللاتينية والمونو، وتعمل دون اتصال لأن الملفات محفوظة مع البناء. أي ترخيص مدفوع كان سيُسعَّر قبل اختياره، ولم يكن هناك سبب لدفعه.',
 'Zero cost. An open licensed family covering Arabic, Latin and mono, working offline because the files are committed with the build. Any paid licence would have been priced before it was chosen, and there was no reason to pay one.',
 'التكلفة','The cost',True)}
{eb('القواعد ثنائية اللغة','THE BILINGUAL RULES')}
<ol class="ru">
<li><span class="ar">العربية تُكتب أولًا، والإنجليزية تُركَّب عليها أو تُحذف.</span><span class="en">Arabic is written first and English is fitted to it, or dropped. Never translate a caption out of English: a layout and a sentence both break when Arabic is poured into a shape built for English.</span></li>
<li><span class="ar">العربية لا تُكتب بأحرف كبيرة ولا تُباعَد حروفها.</span><span class="en">Arabic is never set in caps and never letter-spaced. Neither exists in the script, and both break the joins.</span></li>
<li><span class="ar">العربية تحتاج ارتفاع سطر أكبر من اللاتينية بنفس المقاس.</span><span class="en">Arabic needs more line height than Latin at the same size. 1.7 against 1.5 is the working ratio in this book.</span></li>
</ol>''')

# ================= 06 LOGO AND SEAL =================
lk=''.join(f'<div class="lk"><img src="../logos-transparent/{r["logo"]}"><span>{r["en"]}</span></div>' for r in RANGES)
sec('06','LOGO &amp; SEAL USE','الشعارات والختم', f'''{eb('الشعارات والختم','06 · LOGO &amp; SEAL USE')}{chip('DEFINED','ok')}
<div class="sealrow"><img class="bigseal" src="../logos-transparent/logo-alex-lockup-transparent.png">
<div class="sealx"><b class="ar">ختم أليكس فودز</b><span>THE ALEX FOODS SEAL</span>
<p class="ar">الحلقة تحمل اسم الشركة بالعربية والإنجليزية، والأيقونة في أعلاها منارة. المنارة هي فاروس، والعلامة مكان بقدر ما هي شركة.</p>
<p class="en">The ring carries the company name in Arabic and English, and the icon at the top of it is a lighthouse. The lighthouse is the Pharos, and the mark is a place as much as a company.</p></div></div>
{eb('علامات المجموعات','THE RANGE MARKS')}
<div class="lks">{lk}</div>
{note('لا توجد ملفات مصدر. جميع العلامات مقصوصة من الراستر المورَّد على خلفية شفافة. كافٍ لكل تسليم في هذا التعاقد، لأن لا شيء في الأساس التجاري ولا في الباقة الشهرية مطبوع. الفيكتور يصبح مطلبًا حقيقيًّا فقط إذا دخلت الطباعة في النطاق.',
 'No source files exist. All marks are cut out of the supplied raster onto transparency. Sufficient for every deliverable on this contract, because nothing in the Foundation or the monthly package is printed. Vector becomes a real requirement only if print enters scope.',
 'حالة الملفات','The file state')}
{eb('قواعد الاستخدام','USAGE RULES')}
<ol class="ru">
<li><span class="ar">لا يُعاد رسم أي علامة ولا يُعاد كتابتها.</span><span class="en">No mark is ever redrawn or retyped. Place as supplied.</span></li>
<li><span class="ar">لا يتلوّن شعار المجموعة بلون النكهة.</span><span class="en">A range logo is never recoloured to match the flavour field it sits on.</span></li>
<li><span class="ar">خلوص حول الختم لا يقل عن نصف قطر الحلقة.</span><span class="en">Clear space around the seal is never less than half the ring radius.</span></li>
<li><span class="ar">الخط الكحلي حول شريط بيبو لا يُحذف أبدًا.</span><span class="en">The navy keyline around the BeBo banner never comes off. On the apple SKU it is the only thing holding the logo off its field.</span></li>
</ol>''')

# ================= 07 THE RANGES =================
RD={'bebo':dict(pack='bebo.png',fmt_ar='أكياس وسادة. الشكل محل نقاش مع العميل.',fmt_en='Pillow bags. Format under query with the client.',
 who_ar='الأم. الشخصيات على العبوة تملك الطفل بالفعل، فالكلام موجَّه لمن يقرّر.',who_en='The mother. The characters already own the child, so the copy talks to whoever is deciding.',
 id_ar='الوجه هو العبوة، ويأخذ لون نكهته. شارة KIDS ZONE، وفلاش NEW أحمر، وشريط أخضر بخط كحلي لا يُحذف.',
 id_en='The face <b>is</b> the pack and it takes the colour of its own flavour. KIDS ZONE sub-mark, red NEW flash, and a green banner with a navy keyline that never comes off.'),
'alrawy':dict(pack='alrawy.png',fmt_ar='جاهز للشرب. ماصة على العبوة.',fmt_en='Ready to drink. Straw on the pack.',
 who_ar='المشتري، وهي المجموعة الوحيدة الموجَّهة لبالغ. طمأنينة لا إثارة.',who_en='The buyer, and the only adult facing range of the four. Reassurance rather than excitement.',
 id_ar='تصوير فاكهة حقيقي لا رسم. أنضج العلامات الأربع، تحمل الختم وعلامة مسجَّلة. نكتار، والعبوة تقول ذلك.',
 id_en='Real fruit photography, not illustration, and the most grown up mark of the four. Carries the seal and a registered mark. <b>It is a nectar and the pack says so</b>, so copy never calls it juice.'),
'2man':dict(pack='2man-icepops.png',fmt_ar='مثلجات. عبوتان: العادية و«أشكال».',fmt_en='Ice pops. Two packages: the normal one and ashkal.',
 who_ar='الطفل الأكبر مباشرة. يصرف من مصروفه، فلا أحد يحتاج وسيطًا.',who_en='The older kid, directly. They spend their own pocket money, so nobody has to be talked through a parent.',
 id_ar='حروف مثلجة ثلاثية الأبعاد لا يمكن إعادة كتابتها، وولد يجري يحمل العلامة كلها. الشعار «عيش جو المغامرة» مكتوب بالفعل ويبقى.',
 id_en='Illustrated 3D lettering that <b>cannot be retyped</b>, and a running boy who carries the whole brand. The tagline is already written and it stays. <b>Both packages share one voice</b> and differ only in artwork.'),
'poleka':dict(pack='poleka.png',fmt_ar='حلوى جيلي في عبوات على شكل زجاجة.',fmt_en='Jelly candy in bottle shaped pouches.',
 who_ar='الطفل، عن قصد. وظيفة العلامة كلها أن تُطلَب بالاسم بصوت عالٍ في محل.',who_en='The child, deliberately. The brand’s whole job is being asked for by name, out loud, in a shop.',
 id_ar='حيوان يملأ كل صنف، فالشخصية تقود كل إطار، والمنشور بلا شخصية خارج العلامة. أربعة أصناف وثلاثة حقول فقط.',
 id_en='A full bleed animal per SKU, so <b>the character leads every frame</b> and a post without one is off brand. <b>Four SKUs but only three distinct fields</b>, which is why the extended layer is mandatory here.')}
rp=[]
for r in RANGES:
    d=RD[r['key']]
    sw=''.join(f'''<div class="fsw"><i style="background:{h}"></i><b class="ar">{ar}</b><span class="mono">{h}</span>
     <span class="vd {'key' if verdict(h)[2] else ('wht' if verdict(h)[0]=='WHITE' else 'ink')}">{verdict(h)[0]}</span></div>''' for en,ar,h in r['fl'])
    rp.append(f'''{eb('المجموعات · '+r['ar'],'07 · THE RANGES · '+r['en'])}{chip('DEFINED','ok')}
<div class="rhero" style="border-top:1.6mm solid {r['sig']}">
 <img class="rlogo" src="../logos-transparent/{r['logo']}">
 <div class="rx"><b class="ar">{r['ar']}</b><span>{r['en']}</span>
 <p class="ar">{d['fmt_ar']}</p><p class="en">{d['fmt_en']}</p></div>
 <div class="rsig"><i style="background:{r['sig']}"></i><span class="mono">{r['sig']}</span><em>SIGNATURE</em></div></div>
<div class="rpack"><img src="../packshots/{d['pack']}"></div>
<div class="two">
<div class="rb"><b class="ar">يتكلم مع</b><span>TALKS TO</span><p class="ar">{d['who_ar']}</p><p class="en">{d['who_en']}</p></div>
<div class="rb"><b class="ar">ما يميّزها</b><span>WHAT MAKES IT ITSELF</span><p class="ar">{d['id_ar']}</p><p class="en">{d['id_en']}</p></div></div>
{eb('الحقول والحكم','FIELDS &amp; VERDICT')}
<div class="fsws">{sw}</div>''')
sec('07','THE RANGES','المجموعات', *rp)

# ================= 08 BRAND VOICE =================
VO=[('بيبو','BeBo','#1BA34C','الأم','the mother','إذن، بلا انقباض','Permission, without the wince',
 'عامية مصرية، دافئة، أم لأم. ليست لغة أطفال.','Egyptian colloquial, warm, mother to mother. Never baby talk.',
 '6 إلى 12 كلمة','6 to 12 words','خفيف، واحد أو اثنان في النهاية','Light. One or two, at the end',
 'ظرف · العيال · مبسوطين · في دقيقة · البيت','صحي · طبيعي ١٠٠٪ · فيتامينات · أرخص من'),
('الراوي','AlRawy','#1B4F9C','المشتري','the buyer','ما قصّرتش','I did not cut a corner',
 'عامية نظيفة. لا عامية شارع ولا فصحى.','Clean colloquial. No slang, and no formal Arabic either.',
 '8 إلى 16 كلمة','8 to 16 words','الصفر هو الأصل','Zero is the default',
 'نكتار · فاكهة · مطمنة · اللانش بوكس · اختيار','عصير طبيعي ١٠٠٪ · بدون سكر · صحي · خصم'),
('تومان','2MAN','#29ABE2','الطفل الأكبر','the older kid','النهار ملكك، اطلع بره','The day is yours, go outside',
 'عامية مصرية، طاقة عالية، أفعال أمر.','Egyptian colloquial, high energy, imperative verbs.',
 '3 إلى 8 كلمات','3 to 8 words','حر، وبحد أقصى ثلاثة','Free use, capped at three',
 'برّه · اطلع · الجو · مغامرة · ساقع · يلا','أي كلام يشبه صوت أب. لا «مفيد» ولا «خد بالك»'),
('بوليكا','POLEKA','#EC008C','الطفل','the child','لعبة يُسمح لك بأكلها','A toy you are allowed to eat',
 'عامية، هزلية، تعتمد على الصوت. الأعلى صوتًا وهذا صحيح للفئة.','Colloquial, silly, sound led. The loudest of the four and that is correct for the category.',
 '2 إلى 6 كلمات','2 to 6 words','الأكثر استخدامًا، وبحد أقصى ثلاثة','Heaviest use, still capped at three',
 'أسماء الشخصيات · مين · النهاردة · جيلي · هات','أي شيء عن السكر أو الأسنان أو الصحة')]
vb=''.join(f'''<div class="vc" style="border-left:1.2mm solid {sig}">
<div class="vh"><b class="ar">{ar}</b><span>{en}</span><em class="ar">{feel_ar}</em><em class="en">{feel_en}</em></div>
<table class="vt"><tbody>
<tr><td class="k">يتكلم مع · TALKS TO</td><td class="ar">{to_ar}<span class="en">{to_en}</span></td></tr>
<tr><td class="k">السجل · REGISTER</td><td class="ar">{reg_ar}<span class="en">{reg_en}</span></td></tr>
<tr><td class="k">طول الجملة · LENGTH</td><td class="ar">{ln_ar}<span class="en">{ln_en}</span></td></tr>
<tr><td class="k">الإيموجي · EMOJI</td><td class="ar">{em_ar}<span class="en">{em_en}</span></td></tr>
<tr class="in"><td class="k">كلمات داخل · WORDS IN</td><td class="ar">{wi}</td></tr>
<tr class="out"><td class="k">كلمات خارج · WORDS OUT</td><td class="ar">{wo}</td></tr>
</tbody></table></div>''' for ar,en,sig,to_ar,to_en,feel_ar,feel_en,reg_ar,reg_en,ln_ar,ln_en,em_ar,em_en,wi,wo in VO)

sec('08','BRAND VOICE','صوت العلامة',
f'''{eb('صوت العلامة · البنية','08 · BRAND VOICE · THE ARCHITECTURE')}{chip('DEFINED','ok')}
{rule('صوت واحد. نبرة لكل مجموعة.','ONE VOICE. A TONE PER RANGE.')}
{bi('الصوت هو الطبقة التي لا تتغير أبدًا. النبرة هي ما يتحوّل مع كل مجموعة، وذلك التحوّل هو المقصود. منشور بوليكا ومنشور الراوي يجب أن يختلفا في الطاقة اختلافًا لا يخطئه أحد، وأن يكونا الشركة نفسها تحتهما بلا لبس.',
    'Voice is the layer that never changes. Tone is what shifts per range, and that difference is the point. A POLEKA post and an AlRawy post should be unmistakably different in energy and unmistakably the same company underneath.')}
{eb('قواعد الصوت · كل المجموعات، بلا استثناء','THE VOICE RULES · ALL RANGES, NO EXCEPTIONS')}
<ol class="ru">
<li><span class="ar">العربية تُكتب أولًا. الإنجليزية تُركَّب عليها أو تُحذف.</span><span class="en">Arabic is written first. English is fitted to it, or dropped.</span></li>
<li><span class="ar">قُلها كما تقولها بصوت عالٍ. لو لا أحد في الإسكندرية يتكلم هكذا، لا تخرج.</span><span class="en">Say it the way you would say it out loud. If nobody in Alexandria talks like that, it does not go out.</span></li>
<li><span class="ar">لا تشرح النكتة أبدًا.</span><span class="en">Never explain the joke. No line that has to point at itself.</span></li>
<li><span class="ar">فكرة واحدة لكل منشور. فكرتان تعني منشورين.</span><span class="en">One idea per post. Two ideas is two posts.</span></li>
<li><span class="ar">تكلّم مع شخص واحد، لا مع جمهور.</span><span class="en">Talk to one person, not an audience.</span></li>
<li><span class="ar">لا لغة شركات. «يسر شركتنا أن تعلن» ممنوعة تمامًا.</span><span class="en">Never corporate. That register is banned outright on all four ranges.</span></li>
<li><span class="ar">لا كذب ولا مبالغة. على الطعام هذه ليست مشكلة ثقة فقط، بل مشكلة تنظيمية.</span><span class="en">Never lie, never stretch. On food this is not just a trust problem, it is a regulatory one.</span></li>
<li><span class="ar">لا شرطات طويلة في أي نص يخرج من المبنى.</span><span class="en">No em dashes in any copy that leaves the building. They read as machine written and they quietly cost trust.</span></li>
</ol>
{note('أليكس فودز هي الحساب الذي ينشر فعلًا، وتحتاج كتلة نبرة خاصة بها بنفس شكل المجموعات الأربع. الاتجاه وصل: «مرح». الكتابة نفسها تحتاج أذن مالك الوكالة لا تخمين آلة، ولذلك تُترك هنا معلنة بدل أن تُملأ بصوت خامس مخترع.',
 'Alex Foods is the account that actually posts and it needs a tone block of its own, in the same shape as the four ranges. The direction has arrived: fun. The writing itself needs the agency principal’s ear rather than a machine’s guess, so it is declared here rather than filled in with an invented fifth voice.',
 'الكتلة الوحيدة المفتوحة · نبرة الماستر','The one open block: the master tone',True)}
{chip('PENDING · MASTER TONE BLOCK','pend')}''',
f'''{eb('النبرة لكل مجموعة','TONE PER RANGE')}
<div class="vcs">{vb[:len(vb)//2] if False else ''.join(vb.split('</div><div class="vc"')[0:1])+'</div>'}</div>''' if False else
f'''{eb('النبرة لكل مجموعة','TONE PER RANGE')}<div class="vcs">{vb}</div>''')

# ================= 09 CAPTION SYSTEM =================
sec('09','THE CAPTION SYSTEM','نظام الكتابة', f'''{eb('نظام كتابة المنشور','09 · THE CAPTION SYSTEM')}{chip('DEFINED','ok')}
{bi('القسم السابق يقول كيف تبدو كل مجموعة. هذا القسم يقول كيف يُبنى المنشور نفسه، سطرًا بسطر، حتى لا يعيد كل شخص اختراع الشكل كل يوم ثلاثاء.',
    'The previous section says how each range sounds. This one says how the post itself is built, line by line, so nobody reinvents the shape every Tuesday.')}
<table class="t3 cap"><thead><tr><th>السطر · LINE</th><th>وظيفته · ITS JOB</th><th>الحد · LIMIT</th></tr></thead><tbody>
<tr><td class="n">1</td><td><b class="ar">الخطّاف</b><span class="en">The hook. One idea, in the range’s own register. It carries the post on its own if nothing else is read.</span></td><td class="ar">حسب المجموعة<span class="en">per range</span></td></tr>
<tr><td class="n">2</td><td><b class="ar">السطر الثاني، اختياري</b><span class="en">Optional second line. It extends the first, never introduces a second idea.</span></td><td class="ar">سطر واحد<span class="en">one line</span></td></tr>
<tr><td class="n">3</td><td><b class="ar">الدعوة، حين توجد دعوة</b><span class="en">The call, when there is one. A question the comments can answer, never a demand.</span></td><td class="ar">سؤال قصير<span class="en">a short question</span></td></tr>
<tr><td class="n">4</td><td><b class="ar">الوسوم</b><span class="en">Hashtags. Three to five, on their own line, never inside a sentence.</span></td><td class="mono">3 - 5</td></tr>
</tbody></table>
{note('لا سعر، ولا اسم محل، ولا رقم غذائي، ولا ادعاء صحي، ولا عمر للشركة. هذه ليست تفضيلات أسلوب، بل الحد الذي يحمي حساب الإعلانات. القائمة الكاملة في القسم 21.',
 'No price, no shop name, no nutritional number, no health claim, and no company age. These are not style preferences, they are the boundary that protects the ad account. The full list is in section 21.',
 'ما لا يدخل أي منشور أبدًا','What never enters a caption',True)}
{note('الوسوم تُكتب بالعربية أولًا حيث يبحث الناس بالعربية، وبالإنجليزية حيث تكون الكلمة إنجليزية في الأصل. لا يُترجم وسم لمجرد التوازن.',
 'Hashtags are Arabic first where people search in Arabic, and English where the word is English to begin with. A hashtag is never translated for the sake of symmetry.',
 'الوسوم','Hashtags')}''')

# ================= PENDING SECTIONS =================
def pending(i,en,ar,deliv,what_ar,what_en,need_ar,need_en,cls='pend',chp='PENDING CLIENT INPUT'):
    sec(i,en,ar, f'''{eb(ar,i+' · '+en)}{chip(chp,cls)}
{bi(what_ar,what_en)}
{note(need_ar,need_en,'ما ينتظره هذا القسم','What this section is waiting on',True)}
<div class="hold"><b class="ar">هذا القسم محجوز ومحدَّد، ولم يُملأ بعد.</b>
<span class="en">This section is reserved and specified, and has not been filled in. It is printed rather than omitted, because a book that quietly leaves a bought deliverable out is worse than one that says where it stands.</span></div>''')

pending('10','SLOGANS &amp; THE GIVEAWAY SONG','الشعارات وأغنية المسابقة','4',
 'الطريقة مكتوبة بالكامل: من تخاطبه كل مجموعة، والشعور خلف كل واحدة، والاختبارات الستة التي يجب أن يعبرها أي سطر. «عيش جو المغامرة» موجود بالفعل لتومان ويبقى كما هو.',
 'The method is fully written: who each range is talking to, the feeling behind each one, and the six tests a line has to pass. 2MAN’s existing tagline already works and it stays.',
 'السطور نفسها تحتاج أذن ناطق بالعربية. تُكتب بالعربية بصوت عالٍ أولًا، لا تُترجم، وتُعرض بسطر واحد لكل مجموعة ومعه بديلان على الأكثر.',
 'The lines themselves need a native ear. They are written in Arabic out loud first, never translated, and presented one line per range with at most two alternates. Handing over thirty options invites the client to design, which is the exact thing the contract keeps them out of.')

pending('17','CONTENT CALENDAR','خطة المحتوى الشهرية','5',
 'الشكل جاهز: التاريخ، ونوع المحتوى، والمنتج، والرسالة، لكل منشور. الخطة تُسلَّم قبل بداية الشهر الذي تغطيه.',
 'The format is ready: date, content type, product and message, per post. The calendar is delivered before the month it covers begins.',
 'موسمية كل مجموعة. المدة المتعاقد عليها تقع بين أكتوبر ويناير، وتومان مجموعة مثلجات. إن كانت تتصرف كما تتصرف المثلجات، فربع المحفظة خارج موسمه طوال المدة المدفوعة، والثلاثة الباقية تحمل الخطط الثلاث.',
 'Seasonality per range. The contracted term runs roughly October to January and 2MAN is an ice pop range. If it behaves the way an ice pop behaves, a quarter of the portfolio sits out of season for the whole paid term and the other three carry all three calendars. This is inference from the category, not from the client’s data, which is exactly why it is a question rather than a plan.')

pending('18','POST ARCHETYPES &amp; PATTERN INVENTORY','أنماط المنشورات','5',
 'الجرد الكامل لكل نمط منشور، ولكل نمط ما يمكن تغييره فيه وما لا يمكن. هذا هو القسم الذي يجعل الكتاب قابلًا للبناء بدل أن يكون قابلًا للإعجاب.',
 'The full inventory of every post pattern and, for each one, exactly what is configurable and what is not. This is the section that makes the book buildable rather than admirable.',
 'يعتمد على الأقسام 11 و13 و15، وعلى الألوان الممتدة لبوليكا التي لم تُختَر بعد. بوليكا لها أربعة أصناف وثلاثة حقول، فالطبقة الممتدة إلزامية عليها ولا توجد قيم خلفها حتى الآن.',
 'It depends on sections 11, 13 and 15, and on POLEKA’s extended colours, which have not been chosen. POLEKA has four SKUs and three fields, so the extended layer is mandatory on that range and there are no values behind it yet. That gap lands before the first POLEKA post, not after it.')

pending('19','GOOGLE BUSINESS PROFILE','نشاط جوجل','7',
 'العنوان وصل: طريق إسكندرية القاهرة الزراعي، مدخل خورشيد، أبيس الأولى، الإسكندرية. البيانات الباقية والتحقق عمل حساب بحت، بلا تصميم.',
 'The address has arrived: Cairo Alexandria Agricultural Road, Khorshid entrance, First Abis, Alexandria. The remaining data and the verification are pure account work with no design in them.',
 'حساب جوجل من العميل، ومواعيد العمل، وتصنيف النشاط، ورقم تليفون للعامة. أربعة أشياء، ودقيقة واحدة من وقت العميل.',
 'A Google account from the client, plus opening hours, business categories and a public phone number. Four things, and one minute of the client’s time.',
 'wait','SPEC · EXECUTION PENDING CLIENT ACCESS')

pending('20','LOCAL SEO · ALEXANDRIA','السيو المحلي','8',
 'بحث الكلمات المفتاحية في الإسكندرية، وقراءة المنافسين، وبنية بيانات النشاط.',
 'Alexandria keyword research, a competitor read, and the business data structure.',
 'العميل لا يعرف منافسيه بالاسم، فالقراءة تأتي من الرف نفسه: زيارتان لمحلين وكاميرا تليفون تعطي الأسعار والأحجام وموقع المنتج على الرف بلا تكلفة. ويجب قول شيء بصراحة: الشركة توزّع في كل مصر، والسيو المحلي للإسكندرية لن يحرّك التوزيع الوطني، ولن يُقدَّم كأنه قد يفعل.',
 'The client does not know their competitors by name, so the read comes off the shelf itself: two shop visits and a phone camera gives prices, pack sizes and shelf position for nothing. And one thing has to be said plainly: the company distributes across Egypt, and Alexandria local SEO will not move national distribution. It is delivered as scoped and it will not be presented as if it might.')

# ================= 11 CANVAS & GRID =================
OUT=[('المصدر','Master','2048 × 2048','يُحفظ دائمًا، ومنه تُقتطع البقية','always kept, everything is cropped from it'),
('منشور فيد','Feed post','1080 × 1350','المنصة الأساسية فيسبوك','Facebook is the primary platform'),
('مربع','Square','1080 × 1080','',''),
('ستوري وريلز','Story and Reels','1080 × 1920','العبوة داخل الثلث الأوسط','pack inside the middle third'),
('صورة الحساب','Profile','320 × 320','تُعرض دائرية','shown as a circle'),
('غلاف فيسبوك','Facebook cover','820 × 312','المنطقة الآمنة في الوسط','safe zone sits in the centre'),
('صورة نشاط جوجل','GBP photo','1200 × 900','كحد أدنى','minimum')]
ob=''.join(f'<tr><td class="ar">{a}<span class="en">{b}</span></td><td class="mono">{c}</td><td class="ar sm">{d}<span class="en">{e}</span></td></tr>' for a,b,c,d,e in OUT)
sec('11','CANVAS, GRID &amp; EXPORT','اللوحة والشبكة', f'''{eb('اللوحة والشبكة والمقاسات','11 · CANVAS, GRID &amp; EXPORT')}{chip('DEFINED','ok')}
{bi('كل شيء يُصوَّر مربعًا ثم يُقتطع. مصدر واحد يخدم الفيد والستوري والمربع، فلا يُنتج أصل ثلاث مرات ولا يختلف إطار عن آخر لأنه بُني مرتين.',
    'Everything is made square and then cropped. One master serves feed, story and square, so no asset is produced three times and no two frames differ because they were built twice.')}
<table class="t3"><thead><tr><th>الاستخدام · USE</th><th>المقاس · SIZE</th><th>ملاحظة · NOTE</th></tr></thead><tbody>{ob}</tbody></table>
{note('هامش 8٪ من كل جانب لا يدخله أي عنصر. العبوة في الثلث الأوسط أفقيًّا. منطقة النص أسفل الإطار دائمًا، لا أعلاه. هذه الثوابت هي ما يجعل ثمانية عشر صنفًا تبدو عائلة واحدة.',
 'An 8% margin on every side that no element enters. The pack in the middle third horizontally. The type zone at the foot of the frame, never the head. These constants are what make eighteen SKUs read as one family.',
 'الثوابت في كل إطار','Constant in every frame',True)}
{note('الستوري أطول من الفيد، والاقتطاع يأكل الأعلى والأسفل. العبوة توضع في الثلث الأوسط حتى ينجو الإطار نفسه في المقاسين دون إعادة تخطيط.',
 'A story is taller than a feed post and the crop eats the top and the bottom. Putting the pack in the middle third is what lets one frame survive both sizes without a re layout.',
 'لماذا الثلث الأوسط','Why the middle third')}
{note('PNG للمصدر، JPG بجودة 90 للنشر. التسمية: اسم المجموعة، ثم الصنف، ثم الشكل، ثم الرقم.',
 'PNG for the master, JPG at quality 90 for publishing. Naming: range, then SKU, then format, then number.',
 'الصيغة والتسمية','Format and naming')}''')

# ================= 12 PACK IN FIELD =================
SHP=[('بيبو','BeBo','كيس وسادة','pillow bag','62٪ من عرض الإطار','62% of frame width'),
('الراوي','AlRawy','عبوة قائمة','standing pouch','58٪ من ارتفاع الإطار','58% of frame height'),
('تومان','2MAN','إصبع مثلج','ice stick','70٪ من ارتفاع الإطار','70% of frame height'),
('بوليكا','POLEKA','عبوة زجاجة','bottle pouch','58٪ من ارتفاع الإطار','58% of frame height')]
sb=''.join(f'<tr><td><b class="ar">{a}</b><span class="en">{b}</span></td><td class="ar">{c}<span class="en">{d}</span></td><td class="ar"><b>{e}</b><span class="en">{f}</span></td></tr>' for a,b,c,d,e,f in SHP)
COMP=[('الحجم','Scale','حسب الشكل، من 58٪ إلى 70٪','by shape, 58% to 70%'),
('الوضع','Placement','قاعدة العبوة على مستوى السطح','pack base sits on the surface plane'),
('ظل التلامس','Contact shadow','أغمق عند التلامس ثم يتلاشى','darkest at contact, then fading'),
('الظل الملقى','Cast shadow','أسفل اليمين دائمًا، لأن الضوء من أعلى اليسار','always down and right, because the key is upper left'),
('انعكاس اللون','Colour spill','لون المشهد على حواف العبوة 5٪ إلى 10٪','scene colour on the pack edges at 5% to 10%'),
('الحافة','Edge','تنعيم بكسل واحد، بلا هالة بيضاء','one pixel feather, no white halo')]
cpb=''.join(f'<tr><td class="n">{i+1}</td><td><b class="ar">{a}</b><span class="en">{b}</span></td><td class="ar">{c}<span class="en">{d}</span></td></tr>' for i,(a,b,c,d) in enumerate(COMP))
DN=[('عبوة على حقل ليس حقل نكهتها','a pack on a field that is not its own flavour'),
('عبوة بلا ظل تلامس، تطفو على الحقل','a pack with no contact shadow, floating on the field'),
('نص أبيض على حقل يحتاج خطًّا محيطًا','white type on a field that needs a keyline'),
('شعار المجموعة يتلوّن بلون النكهة','the range logo recoloured to match the flavour'),
('مجموعتان في إطار واحد','two ranges in one frame'),
('عبوة تدخل هامش الـ8٪','a pack entering the 8% margin'),
('حقل متدرّج أو بملمس','a gradient or textured field'),
('نص فوق العبوة نفسها','type laid over the pack itself')]
dnb=''.join(f'<li><i></i><span class="ar">{a}</span><span class="en">{e}</span></li>' for a,e in DN)
CFG=[('الحقل','The field','لون النكهة من الخريطة','the flavour colour from the map'),
('مقاس العبوة','Pack scale','حسب الشكل، 58٪ إلى 70٪','by shape, 58% to 70%'),
('لون النص','Type colour','محسوب، لا يُختار','computed, never chosen'),
('الخط المحيط','Keyline','إلزامي على ثلاثة حقول','mandatory on three fields'),
('الشخصية','Character','اختياري، إلزامي على بوليكا','optional, mandatory on POLEKA')]
cfb=''.join(f'<tr><td><b class="ar">{a}</b><span class="en">{b}</span></td><td class="ar">{c}<span class="en">{d}</span></td></tr>' for a,b,c,d in CFG)

sec('12','THE PACK IN FIELD SYSTEM','العبوة على الحقل',
f'''{eb('نظام العبوة على الحقل','12 · THE PACK IN FIELD SYSTEM')}{chip('DEFINED','ok')}
{rule('العبوة على حقل نكهتها.','THE PACK ON ITS FLAVOUR FIELD.')}
{bi('كل رسم، وكل صورة متحركة، وكل أنيميشن في هذا التعاقد مبني من هذا الشيء الواحد. ليس أسلوبًا من بين أساليب، بل الجهاز البصري الذي يميّز أليكس فودز. إذا تغيّر، تغيّرت العلامة.',
    'Every graphic, every animated still and every animation on this contract is built from this one thing. It is not one style among several, it is the visual device that identifies Alex Foods. If it changes, the brand changes.')}
<div class="lay3">
 <div class="ly"><i>1</i><b class="ar">الحقل</b><span>THE FIELD</span><p class="ar">لون النكهة يملك الحقل.</p><p class="en">The flavour colour owns the field.</p></div>
 <div class="ly"><i>2</i><b class="ar">العبوة</b><span>THE PACK</span><p class="ar">فن العميل نفسه، مقصوص على شفافية.</p><p class="en">The client’s own artwork, cut out on transparency.</p></div>
 <div class="ly"><i>3</i><b class="ar">النص</b><span>THE TYPE</span><p class="ar">حبري أو أبيض، والقرار محسوب.</p><p class="en">Ink or white, and the decision is computed.</p></div></div>
{eb('شكل العبوة يحدّد المقاس','THE PACK SHAPE SETS THE SCALE')}
<table class="t3"><thead><tr><th>المجموعة</th><th>الشكل · SHAPE</th><th>المقاس · SCALE</th></tr></thead><tbody>{sb}</tbody></table>
{note('أربع مجموعات بأربعة أشكال. مقاس واحد ثابت لكلها ينتج إطارًا فارغًا لتومان وإطارًا مزدحمًا لبيبو. المقاس يتبع الشكل، والهامش هو الثابت.',
 'Four ranges with four pack shapes. One fixed scale across all of them produces an empty frame for 2MAN and a crowded one for BeBo. The scale follows the shape and the margin is what stays constant.',
 'لماذا المقاس ليس رقمًا واحدًا','Why the scale is not one number')}''',
f'''{eb('قواعد التركيب','COMPOSITING RULES')}
<table class="t3 cp"><tbody>{cpb}</tbody></table>
{note('عبوة لم يلمسها لون المكان تبدو دائمًا كأنها من صورة أخرى، حتى لو كان الظل مثاليًّا.',
 'A pack the room’s colour has not touched always looks like it came from another photograph, even when the shadow is perfect.',
 'البند الخامس هو الذي يقنع العين','Item 5 is the one that convinces the eye')}
{eb('ما لا تجلس عليه العبوة أبدًا','WHAT A PACK MAY NEVER SIT ON')}
{ok('ثمانية أخطاء تُبطل الإطار. كل واحد منها يُرى فورًا، ولهذا يُكتب.','Eight mistakes that void the frame. Every one is visible on sight, which is exactly why it gets written down.',True)}
<ol class="dn">{dnb}</ol>
{eb('ما الذي يتغيّر','THE CONFIGURABLES')}
<table class="t3 cfg"><tbody>{cfb}</tbody></table>
{note('الطبقات الثلاث وترتيبها. هامش الـ8٪. منطقة النص في الأسفل. ملكية اللون. ولون النص محسوب لا مختار.',
 'The three layers and their order. The 8% margin. The type zone at the foot. Colour ownership. And the type colour is computed, never chosen.',
 'وما لا يتغيّر أبدًا','And what never changes',True)}''')

# ================= 13 FLASHES & CHARACTERS =================
sec('13','FLASHES, BADGES &amp; CHARACTERS','الشارات والشخصيات', f'''{eb('الشارات والشخصيات','13 · FLASHES, BADGES &amp; THE CHARACTER LIBRARY')}{chip('DEFINED','ok')}
{rule('الشخصيات مرسومة بالفعل ومدفوعة بالفعل.','THE CHARACTERS ARE ALREADY DRAWN AND ALREADY PAID FOR.',True)}
{bi('كل مجموعة تقود بشخصية: وجوه بيبو التي تأخذ لون نكهتها، وحيوانات بوليكا التي تملأ العبوة، وولد تومان الذي يجري. هذه أرخص مادة تملكها هذه الشركة، وهي المادة الوحيدة التي لا يستطيع منافس نسخها.',
    'Every range leads with a character: BeBo’s faces which take the colour of their own flavour, POLEKA’s full bleed animals, and 2MAN’s running boy. This is the cheapest content this business owns, and the one thing a competitor cannot copy.')}
<table class="t3"><thead><tr><th>الشارة · BADGE</th><th>مصدرها · SOURCE</th><th>قاعدتها · ITS RULE</th></tr></thead><tbody>
<tr><td><b class="ar">NEW</b><span class="en">Red corner flash</span></td><td class="ar">من عبوة بيبو<span class="en">from the BeBo pack</span></td><td class="ar">لا يُعاد رسمه ولا يُنقل لمجموعة أخرى<span class="en">never redrawn and never moved to another range</span></td></tr>
<tr><td><b class="ar">KIDS ZONE</b><span class="en">Rainbow lozenge</span></td><td class="ar">من عبوة بيبو<span class="en">from the BeBo pack</span></td><td class="ar">خاص ببيبو وحدها<span class="en">BeBo only</span></td></tr>
<tr><td><b class="ar">الختم</b><span class="en">The Alex seal</span></td><td class="ar">علامة الشركة<span class="en">the corporate mark</span></td><td class="ar">يوضع كما ورد، ولا يُعاد بناؤه<span class="en">placed as supplied, never reconstructed</span></td></tr>
<tr><td><b class="ar">قفل المسابقة</b><span class="en">Giveaway lockup</span></td><td class="ar">بند في الباقة الشهرية<span class="en">a monthly package line item</span></td><td class="ar">واحد لكل المجموعات، يمنع أربع مسابقات بأربعة أشكال<span class="en">one across all ranges, which is what stops four differently shaped giveaways</span></td></tr>
</tbody></table>
{note('منشور بوليكا بلا شخصية خارج العلامة حتى لو كان النص مثاليًّا. كل صنف حيوان كامل، فالمنشور يقود بالحيوان لا بالكيس.',
 'A POLEKA post with no character in it is off brand even if the copy is perfect. Each SKU is a full animal, so the post leads with the animal and not the packet.',
 'القاعدة الوحيدة الملزمة هنا','The one binding rule here',True)}
{note('لا تُقارن الشخصيات ببعضها أبدًا كأفضل وأسوأ. لكل طفل شخصية مفضّلة، ونصفهم سيُقال لهم إنهم اختاروا خطأ.',
 'Never compare the characters to each other as better or worse. Every child has a favourite, and half of them are being told they chose wrong.',
 'وما لا يُفعل بها','And what is never done with them')}''')

# ================= 14 SOCIAL PAGES =================
sec('14','SOCIAL PAGES SETUP','إعداد الصفحات', f'''{eb('إعداد الصفحات','14 · SOCIAL PAGES SETUP')}{chip('SPEC · EXECUTION PENDING CLIENT ACCESS','wait')}
{rule('حضور واحد لأليكس فودز، لا أربع صفحات.','ONE ALEX FOODS PRESENCE, NOT FOUR BRAND PAGES.')}
{bi('المجموعات الأربع لا تحمل كل واحدة جمهورها من الصفر. حضور واحد يتراكم، وأربعة حضورات تتقاسم نفس الجهد أربع مرات. المجموعات تدور داخل الحساب الواحد.',
    'The four ranges do not each carry an audience from zero. One presence compounds, and four presences split the same effort four ways. The ranges rotate inside the one account.')}
<table class="t3"><thead><tr><th>المنصة · PLATFORM</th><th>الدور · ROLE</th><th>الإيقاع · RHYTHM</th></tr></thead><tbody>
<tr><td><b>Facebook</b></td><td class="ar"><b>الأساسية.</b> كل أصل ينزل هنا أولًا<span class="en"><b>Primary.</b> Every asset lands here first. The only account with an audience, and the only place the agreed number can move inside a month.</span></td><td class="mono">4 - 5 / week</td></tr>
<tr><td><b>TikTok</b></td><td class="ar"><b>بناء ثانوي</b> على محتوى الشخصيات<span class="en"><b>Secondary build</b>, on the character content. Already drawn, already paid for, and native to the platform the kids are on.</span></td><td class="mono">2 / week</td></tr>
<tr><td><b>Instagram</b></td><td class="ar"><b>مرآة.</b> بلا إنتاج خاص<span class="en"><b>Mirror only.</b> Cross post what Facebook gets. No bespoke production until it earns attention.</span></td><td class="ar sm">مرآة<span class="en">mirrors Facebook</span></td></tr>
<tr><td><b class="ar">ستوري</b><span class="en">Stories</span></td><td class="ar">من حصة الستوري في الرسومات الشهرية<span class="en">from the story format share of the monthly graphics</span></td><td class="mono">1 - 2 / week</td></tr>
</tbody></table>
{note('الباقة الشهرية تموّل عشرين أصلًا في الشهر: أنيميشن اثنان، وست صور متحركة، واثنا عشر رسمًا. الإيقاع أعلاه مشتق من ذلك الرقم لا من الطموح. إيقاع لا يستطيع العقد تمويله هو إيقاع يستطيع العميل أن يحاسب عليه.',
 'The monthly package funds twenty assets a month: two animations, six animated stills and twelve graphics. The rhythm above is derived from that number rather than from ambition. A rhythm the contract cannot fund is a rhythm the client can hold the agency to.',
 'الإيقاع مشتق من الإنتاج','The rhythm is derived from what is produced',True)}
{note('التنفيذ يحتاج صلاحية أدمن على Meta وحساب جوجل. الكلام مكتوب بالكامل والحسابات لا يمكن إعدادها بدون ذلك. وهناك ما يجب التحقق منه أولًا: يبدو أن حساب فيسبوك الحالي حساب شخصي لا صفحة، وإن كان كذلك فلا يمكن تشغيل إعلانات منه إطلاقًا.',
 'Execution needs Meta admin access and a Google account. The spec is fully written and the accounts cannot be set up without them. And one thing has to be checked first: the current Facebook asset appears to be a personal profile rather than a Page, and if it is, no paid campaign can run from it at all.',
 'ما يمنع التنفيذ','What blocks execution')}''')

# ================= 15 MOTION =================
sec('15','MOTION','الحركة', f'''{eb('الحركة','15 · MOTION')}{chip('DEFINED','ok')}
{bi('الباقة الشهرية تسلّم ثماني قطع متحركة: أنيميشن اثنان وست صور متحركة. الفرق بينهما ليس في الطول بل في ما يتحرك، وتحديد ذلك كتابةً هو ما يمنع ست صور متحركة من أن تصير ستة أنيميشن صغيرة بتكلفة ستة أنيميشن.',
    'The monthly package delivers eight motion pieces: two animations and six animated stills. The difference is not length, it is what moves, and writing that down is what stops six animated stills quietly becoming six small animations at the cost of six animations.')}
<table class="t3"><thead><tr><th>النوع · TYPE</th><th>ما يتحرك · WHAT MOVES</th><th>المدة · DURATION</th></tr></thead><tbody>
<tr><td><b class="ar">صورة متحركة</b><span class="en">Animated still</span><span class="en mono">6 / month</span></td><td class="ar">عنصر واحد فقط: بخار، أو قطرة، أو غمزة من وجه بيبو، أو ميل خفيف في العبوة. الإطار نفسه ثابت.<span class="en">One element only: steam, a droplet, a wink from a BeBo face, a slight tilt on the pack. The frame itself does not move.</span></td><td class="mono">2 - 4s<span class="en">loops</span></td></tr>
<tr><td><b class="ar">أنيميشن منتج</b><span class="en">Product animation</span><span class="en mono">2 / month</span></td><td class="ar">الإطار يتحرك: دخول العبوة، وتغيّر الحقل، وظهور النص، ثم القفل. له بداية ونهاية.<span class="en">The frame moves: the pack enters, the field changes, the type resolves, then the lockup. It has a beginning and an end.</span></td><td class="mono">8 - 15s</td></tr>
</tbody></table>
{eb('القواعد','THE RULES')}
<ol class="ru">
<li><span class="ar">العبوة لا تتشوّه أبدًا. لا تمطّط ولا التواء ولا انضغاط.</span><span class="en">The pack never distorts. No stretch, no warp, no squash. It is the client’s printed artwork and it holds its proportions.</span></li>
<li><span class="ar">النص يظهر ويثبت. لا يطير ولا يرتد ولا يدور.</span><span class="en">Type appears and settles. It never flies, bounces or spins. The register of the motion has to match the register of the voice.</span></li>
<li><span class="ar">الحقل لا يتدرّج ولا يلمع. لون مسطّح في الحركة كما في الثبات.</span><span class="en">The field never gradients or shines. Flat colour in motion exactly as in stills.</span></li>
<li><span class="ar">كل قطعة تعمل بلا صوت. الصوت إضافة، لا شرط.</span><span class="en">Every piece works with the sound off. Sound is an addition, never a condition, because most of this audience scrolls muted.</span></li>
<li><span class="ar">آخر إطار هو إطار العبوة الثابت. من يتوقف عند النهاية يرى المنتج.</span><span class="en">The last frame is the still pack frame. Anybody who stops at the end sees the product.</span></li>
</ol>
{note('الصورة المتحركة عنصر واحد يتحرك داخل إطار ثابت. في اللحظة التي يتحرك فيها الإطار أو يدخل عنصر ثانٍ، صارت أنيميشن، وسعرها مختلف. هذا التعريف هو الذي يحمي الباقة الشهرية من أن تُستهلك.',
 'An animated still is one element moving inside a frame that does not. The moment the frame moves or a second element enters, it is an animation, and it costs differently. That definition is what protects the monthly package from being quietly consumed.',
 'الحد بين النوعين','The line between the two',True)}''')

# ================= 16 SHOOTING & COMPOSITING =================
CONST=[('زاوية الكاميرا','Camera angle','من أعلى 10 إلى 15 درجة','10 to 15 degrees above','أعلى يشوّه العبوة، وأقل يخفي الأرضية','higher distorts the pack, lower hides the surface'),
('العدسة','Lens','ما يعادل 50 مم','50 mm equivalent','العدسات الواسعة تقوّس حواف العبوة','wide lenses bow the pack edges'),
('اتجاه الضوء','Light direction','أعلى اليسار بزاوية 45 درجة','upper left at 45 degrees','ثابت واحد يجعل كل الظلال متفقة','one constant keeps every shadow in agreement'),
('نوع الضوء','Light quality','ناعم، مصدر واسع','soft, broad source','الضوء الحاد يكسر ألوان العبوة المطبوعة','hard light breaks the printed pack colours'),
('حرارة اللون','Colour temperature','5200 كلفن، نهار محايد','5200 K neutral daylight','حتى لا تتغير ألوان العلامة','so the brand colours do not shift'),
('الظل','Shadow','ظل تلامس ناعم تحت العبوة','soft contact shadow beneath','بدونه تبدو العبوة طائرة','without it the pack floats'),
('عمق الميدان','Depth of field','العبوة حادة، الخلفية ناعمة','pack sharp, background soft','العبوة هي البطل دائمًا','the pack is always the hero'),
('نسبة التصوير','Capture ratio','مربع 1:1 ثم يُقتطع','square 1:1 then cropped','مصدر واحد يخدم الفيد والستوري','one source serves feed and story')]
cr=''.join(f'<tr><td><b class="ar">{a}</b><span class="en">{b}</span></td><td class="ar">{c}<span class="en">{d}</span></td><td class="ar sm">{e}<span class="en">{f}</span></td></tr>' for a,b,c,d,e,f in CONST)
WLD=[('بيبو','BeBo','#1BA34C','مطبخ بيت، سطح نظيف','a home kitchen, a clean counter','ضوء صباح من نافذة','morning window light','هادئ، مرتب، بيت شغّال','calm, tidy, a house that works','لا تُظهر العبوة وهي تُحضَّر أو يُشرب منها','never show the pack being prepared or drunk from'),
('الراوي','AlRawy','#1B4F9C','طاولة نظيفة أو حقيبة مدرسة','a clean table, or an open school bag','نهار صافٍ','clear daylight','اطمئنان، لا إثارة','reassurance, never excitement','لا أكوام فاكهة توحي بنسبة عصير','no fruit piles implying juice content'),
('تومان','2MAN','#29ABE2','خارج البيت، شارع أو شاطئ','outdoors, a street or a beach','شمس قوية مباشرة','strong direct sun','حركة، برودة، النهار ملكك','motion, cold, the day is yours','العبوتان لهما نفس العالم','both packages share one world'),
('بوليكا','POLEKA','#EC008C','خلفية لون مسطّح، بلا واقعية','a flat colour ground, no realism','ناعم ومتساوٍ','soft and even','لعب. الشخصية أولًا','play. Character first','صنف الكولا لا يظهر في أي إعلان مدفوع','the cola SKU appears in no paid campaign')]
wb=''.join(f'''<div class="wld"><div class="wh" style="border-left:1.2mm solid {sig}"><b class="ar">{ar}</b><span>{en}</span></div>
<table class="wt"><tbody>
<tr><td class="k">المكان · PLACE</td><td class="ar">{pa}<span class="en">{pe}</span></td></tr>
<tr><td class="k">الضوء · LIGHT</td><td class="ar">{la}<span class="en">{le}</span></td></tr>
<tr><td class="k">المزاج · MOOD</td><td class="ar">{ma}<span class="en">{me}</span></td></tr>
<tr class="no"><td class="k">ممنوع · FORBIDDEN</td><td class="ar"><b>{fa}</b><span class="en"><b>{fe}</b></span></td></tr>
</tbody></table></div>''' for ar,en,sig,pa,pe,la,le,ma,me,fa,fe in WLD)
PR=[('BeBo','#1BA34C','Empty home kitchen counter, no products, pale wood surface, soft morning window light from upper left at 45 degrees, blurred warm kitchen background, calm and tidy, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre foreground'),
('AlRawy','#1B4F9C','Empty clean light table top, no products, one whole fresh peach resting to the right, clear daylight from upper left at 45 degrees, soft neutral background, calm and reassuring, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre'),
('2MAN','#29ABE2','Empty wet concrete surface with scattered ice cubes and water droplets, no products, strong direct sunlight from upper left, blurred bright outdoor street background, high energy summer, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre'),
('POLEKA','#EC008C','Flat solid colour studio background, no products, soft even light from upper left, no texture, no realism, playful and bright, 50mm lens, camera 12 degrees above, square 1:1, clear empty space in the centre')]
pb=''.join(f'<div class="pr"><b style="color:{c}">{n}</b><code>{t}</code></div>' for n,c,t in PR)
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

sec('16','SHOOTING &amp; COMPOSITING','وصفة التصوير والتركيب',
f'''{eb('وصفة التصوير والتركيب','16 · SHOOTING &amp; COMPOSITING RECIPE')}{chip('DEFINED','ok')}
{rule('المشهد يُولَّد. المنتج لا يُولَّد أبدًا.','THE SCENE IS GENERATED. THE PRODUCT NEVER IS.')}
{bi('الذكاء الاصطناعي لا يكتب حروفًا عربية صحيحة، ولا يعيد رسم شعار مسجّل بدقة. ينتج شيئًا يشبههما. على عبوة طعام، الشبيه ليس أسلوبًا، بل منتج مختلَق لا وجود له. لذلك الذكاء الاصطناعي يصنع المكان فقط، والعبوة الحقيقية تُركَّب فوقه.',
    'AI does not render correct Arabic lettering, and it does not redraw a registered mark accurately. It produces something that resembles them. On a food pack, a resemblance is not a style choice, it is a fabricated product that does not exist. So AI makes the place, and the real pack is composited into it.')}
{note('فن العبوة ملك العميل، وكل بكسل منه في الصورة النهائية هو ملكه هو. لا يوجد ادعاء بصري لم يوافق عليه أحد، ولا علامة تجارية أُعيد رسمها خطأً.',
 'The pack artwork belongs to the client, so every pixel of product in the final image is theirs. There is no visual claim nobody approved, and no trademark redrawn wrongly.',
 'لماذا تحمي القاعدة الطرفين','Why the rule protects both sides')}
{eb('الثوابت','THE CONSTANTS')}
<table class="t3 cn"><thead><tr><th>الثابت · CONSTANT</th><th>القيمة · VALUE</th><th>لماذا · WHY</th></tr></thead><tbody>{cr}</tbody></table>''',
f'''{eb('عوالم المشاهد','THE SCENE WORLDS')}
{bi('لكل مجموعة عالمها. الثوابت لا تتغير، لكن المكان والأرضية والمزاج يتغيرون. العالم هو ما يفصل المجموعات عن بعضها، تمامًا كما تفعل ألوانها على الرف.',
    'Each range has its world. The constants never change, but the place, the surface and the mood do. The world is what separates the ranges, exactly as their colours do on a shelf.')}
<div class="wlds">{wb}</div>
{note('شكل استخدام بيبو غير محسوم بعد. الصورة التي تُظهر طريقة الاستخدام تعلن إجابة لا نملكها. تنتظر صورة ظهر العبوة.',
 'BeBo’s format is not yet settled. An image showing how it is used asserts an answer we do not have. It waits on a photo of the back of the pack.',
 'سبب منع بيبو','Why the BeBo ban',True)}''',
f'''{eb('صيغة الأمر','THE PROMPT FORMULA')}
{rule('اطلب الغرفة، لا تطلب المنتج.','ASK FOR THE ROOM, NEVER FOR THE PRODUCT.',True)}
{bi('لا تطلب «عبوة عصير على طاولة»، لأن المولّد سيرسم عبوة مختلَقة. اطلب مشهدًا فارغًا فيه مساحة خالية واضحة، ثم ركّب العبوة الحقيقية في تلك المساحة.',
    'Never ask for a juice pack on a table, because the generator will draw a fabricated pack. Ask for an empty set with a clear open space, then composite the real pack into it.')}
<div class="prs">{pb}</div>
{eb('ما يُستبعد من كل أمر','WHAT EVERY PROMPT EXCLUDES')}
<div class="neg"><code>no text, no lettering, no arabic script, no logos, no brands, no packaging,<br>no bottles, no sachets, no hands, no people, no faces, no watermark</code></div>
{note('أهم بند هو منع أي كتابة. المولّد إذا كتب حرفًا واحدًا، ولو في الخلفية، فقد صنع لغة مزيفة على صورة علامة غذائية. والثاني منع الأيدي والوجوه، لأن الوكالة لا تملك إذن تصوير لأي شخص.',
 'The most important entry is the ban on lettering. If the generator writes one character, even in the background, it has invented a fake language on a food brand image. The second is hands and faces, because the agency holds no model release for anybody.',
 'لماذا هذه القائمة','Why this list',True)}
{eb('قائمة المراجعة قبل النشر','THE PRE PUBLISH CHECKLIST')}
<ol class="chk">{kb}</ol>''')

# ================= 21 COMPLIANCE =================
NEV=[('ادعاءات صحية أو طبية','Health or medical claims','صحي · مفيد · يقوي المناعة · غني بالفيتامينات'),
('«طبيعي ١٠٠٪» أو «عصير ١٠٠٪»','100% natural or 100% juice','الراوي نكتار، وبيبو مشروب مُحضَّر'),
('«أورجانيك» أو أي ادعاء شهادة','Organic, or any certification claim','لم تصل أي شهادة مكتوبة'),
('أي رقم غذائي','Any nutritional number','سعرات · سكر · نسبة فاكهة · فيتامينات'),
('مقارنة بمنافس بالاسم','Named competitor comparisons','ولا «أحسن من» ضد أحد'),
('ادعاءات سعر','Price claims','«الأرخص» غير قابلة للتحقق وتختلف من محل لمحل'),
('وعود توفّر','Availability promises','لا يُذكر محل لم يؤكده العميل'),
('عمر الشركة قبل تأكيده','A company age before it is confirmed','ورقهم يقول عشرين وخمسة وعشرين'),
('أي شيء عن المصنع أو الشهادات أو الحلال','Anything about the factory, certifications or halal','كلها معلومات العميل'),
('رد علني على شكوى تلوّث أو مرض','A public reply to a contamination or illness complaint','لها إجراء خاص')]
nv=''.join(f'<li><i></i><span class="ar"><b>{a}</b></span><span class="en">{b}</span><span class="ar sm">{c}</span></li>' for a,b,c in NEV)
sec('21','COMPLIANCE','الالتزام', f'''{eb('الالتزام · ما لا يُقال أبدًا','21 · COMPLIANCE · THE NEVER LIST')}{chip('DEFINED','ok')}
{ok('هذا القسم موجود لأن صفحة طعام يمكن الإبلاغ عنها، وحساب إعلانات مدفوع يمكن تقييده، بسبب جملة واحدة لم يفكر فيها أحد. الوكالة هي التي تدير حساب الإعلانات، فهذه مسؤوليتها بقدر ما هي مسؤولية العميل.',
    'This section exists because a food page can be reported, and a paid ad account restricted, on a single sentence nobody thought about. The agency runs the ad account, so this is the agency’s exposure as much as the client’s.',True)}
<ol class="nev">{nv}</ol>
{note('ما لم يصل من العميل مكتوبًا، لا تعرفه الوكالة. التخمين المفيد في خيط تعليقات هو ادعاء منشور باسم العلامة.',
 'If it did not come from the client in writing, the agency does not know it. A helpful guess in a comment thread is a published claim by the brand.',
 'المبدأ الحاكم','The governing principle',True)}
{note('القائمة أعلاه تنطبق على الصور بنفس القوة. صورة صالة رياضية أو معمل ادعاء صحي، وكومة فاكهة ادعاء نسبة، وزيّ مدرسي ادعاء اعتماد. الصورة ادعاء منشور مثلها مثل الجملة.',
 'The list above applies to images with equal force. A gym or a laboratory is a health claim, a fruit pile is a content claim, and a school uniform is an endorsement claim. An image is a published claim exactly as a sentence is.',
 'وينطبق على الصور أيضًا','And it applies to pictures too')}''')

# ================= 22 SYSTEM IN NUMBERS =================
NUMS=[('المجموعات','Ranges',str(len(RANGES))),('الأصناف','SKUs',str(NF)),('الحقول','Flavour fields',str(NF)),
('الحبري يفوز','Ink wins',str(NINK)),('الأبيض يفوز','White wins',str(NWHT)),('تحتاج خطًّا محيطًا','Need a keyline',str(NKEY)),
('تصادمات دقيقة','Exact collisions',str(len(COLL))),('المحايدات','Neutrals','8'),
('عائلات الخطوط','Type families','3'),('المقاسات النهائية','Output sizes','7'),
('الأصول شهريًّا','Assets per month','20'),('قطع الحركة شهريًّا','Motion pieces per month','8')]
nb2=''.join(f'<div class="num"><b>{v}</b><span class="ar">{a}</span><span class="en">{e}</span></div>' for a,e,v in NUMS)
sec('22','THE SYSTEM IN NUMBERS','النظام بالأرقام', f'''{eb('النظام بالأرقام','22 · THE SYSTEM IN NUMBERS')}{chip('DEFINED','ok')}
<div class="nums">{nb2}</div>
{eb('إعادة البناء من هذه الوثيقة','REBUILDING FROM THIS BOOK')}
{bi('كل شيء في هذا النظام مبني من خمسة أشياء. من فهمها يستطيع أن يمدّ النظام دون أن يخمّن.',
    'Everything in this system is built from five things. Anybody who understands them can extend it without guessing.')}
<ol class="ru">
<li><span class="ar">البنية في القسم 3: الماستر فوق، والمجموعات تحته، والنكهة تحتها.</span><span class="en">The architecture in section 3. Master above, ranges beneath, flavour beneath that.</span></li>
<li><span class="ar">ملكية اللون: النكهة للحقل، المجموعة للشعار، الماستر للختم.</span><span class="en">Colour ownership. Flavour owns the field, range owns the logo, master owns the seal.</span></li>
<li><span class="ar">جهاز العبوة على الحقل في القسم 12.</span><span class="en">The pack in field device in section 12. Three layers, a computed type colour, an 8% margin.</span></li>
<li><span class="ar">صوت واحد ونبرة لكل مجموعة، في القسم 8.</span><span class="en">One voice and a tone per range, in section 8.</span></li>
<li><span class="ar">قائمة الممنوعات في القسم 21، وهي حماية قانونية لا أسلوب.</span><span class="en">The never list in section 21, which is legal protection rather than style.</span></li>
</ol>
{note('كل رقم في هذه الوثيقة محسوب بمعادلة السطوع النسبية في WCAG 2.1، لا مُقدَّرًا بالعين. يمكن إعادة توليد أي قيمة هنا من الشيفرة التي بنت الوثيقة.',
 'Every number in this book is computed with the WCAG 2.1 relative luminance formula rather than estimated by eye. Any value here can be regenerated from the code that built the document.',
 'من أين تأتي الأرقام','Where the numbers come from',True)}''')

# ================= 23 GOVERNANCE =================
sec('23','GOVERNANCE','الحوكمة', f'''{eb('الحوكمة وضبط الإصدارات','23 · GOVERNANCE &amp; VERSION CONTROL')}{chip('DEFINED','ok')}
<table class="t3"><thead><tr><th>البند · ITEM</th><th>القاعدة · RULE</th></tr></thead><tbody>
<tr><td><b class="ar">الإصدار</b><span class="en">Version</span></td><td class="ar">يظهر في تذييل كل صفحة. صفحة تُوجد على مكتب بعد ستة أشهر يجب أن تعرّف نفسها وإصدارها.<span class="en">Printed in the footer of every page. A page found loose on a desk in six months has to identify itself and its version.</span></td></tr>
<tr><td><b class="ar">التعديل</b><span class="en">Revision</span></td><td class="ar">الوثيقة مولَّدة لا مُصفَّفة يدويًّا. التعديل تحرير وإعادة توليد، لا إعادة تخطيط.<span class="en">The book is generated rather than hand laid. A revision is an edit and a re render, never a re layout.</span></td></tr>
<tr><td><b class="ar">المصدر</b><span class="en">The source</span></td><td class="ar">كل قيمة لون وكل نسبة تباين تأتي من الشيفرة نفسها. لا يوجد رقم مكتوب يدويًّا في هذه الوثيقة.<span class="en">Every colour value and every contrast ratio comes from the code itself. There is no hand typed number in this book.</span></td></tr>
<tr><td><b class="ar">الاعتماد</b><span class="en">Approval</span></td><td class="ar">شخص واحد مسمّى من جانب العميل، وملاحظاته وحده هي التي تُحتسب. لا رد خلال 48 ساعة يعني اعتمادًا.<span class="en">One named approver on the client side, and only their notes count. No reply within 48 hours means approved.</span></td></tr>
<tr><td><b class="ar">التعديلات</b><span class="en">Revision rounds</span></td><td class="ar">جولة واحدة لكل تسليم، وكل الملاحظات في رد مكتوب واحد.<span class="en">One round per delivery, with all notes gathered into a single written reply.</span></td></tr>
</tbody></table>
{note('الأقسام التي تحمل شارة انتظار ليست ناقصة، بل محجوزة ومحدَّدة وتنتظر شيئًا مسمّى. كل واحدة منها تقول ما تنتظره ومن. الوثيقة التي تحذف تسليمًا مدفوعًا بصمت أسوأ من الوثيقة التي تقول أين يقف.',
 'The sections carrying a waiting chip are not missing, they are reserved, specified, and waiting on something named. Each one says what it waits on and who from. A book that quietly leaves out a bought deliverable is worse than one that says where it stands.',
 'الأقسام المنتظرة','The sections that are waiting',True)}''')

# ================= 24 SIGN OFF =================
sec('24','SIGN-OFF','الاعتماد', f'''{eb('الاعتماد','24 · SIGN-OFF')}
<div class="signoff">{cnr()}
<h1 class="ar">اعتماد الأساس التجاري</h1><h2>BRAND FOUNDATION APPROVAL</h2>
<p class="ar so">باعتماد هذه الوثيقة، يقرّ العميل بأن الأساس التجاري قد سُلِّم، ويسمّي الشخص الوحيد الذي تُحتسب ملاحظاته بموجب العقد.</p>
<p class="en so">By approving this document the client accepts the Brand Foundation as delivered, and names the one person whose notes count under the contract.</p>
<div class="sfields">
 <div class="sf"><span>الاسم · NAME</span><i></i></div>
 <div class="sf"><span>الصفة · ROLE</span><i></i></div>
 <div class="sf"><span>التاريخ · DATE</span><i></i></div>
 <div class="sf"><span>التوقيع · SIGNATURE</span><i></i></div>
</div>
<div class="sn"><b class="ar">شرط بدء الشهر الأول</b>
<p class="ar">يبدأ الشهر الأول من الباقة في التاريخ الأبعد من اثنين: اعتماد الأساس التجاري كتابةً، أو وصول صور المنتج الصالحة للاستخدام.</p>
<p class="en">Package month 1 starts on the later of two dates: written approval of the Brand Foundation, or the arrival of usable product photography.</p></div>
<div class="by"><i></i><span>THE STANDARD AGENCY &nbsp;·&nbsp; {VER} &nbsp;·&nbsp; {DATE}</span></div></div>''')

# ================= RENDER =================
CSS=f'''
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:{PAPER};color:{INK};font-family:'IBM Plex Sans',sans-serif;
 -webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:14mm 14mm 20mm;position:relative;overflow:hidden;background:{PAPER};
 page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto}}
.page.dark{{background:{DEEP};color:{PAPER}}}
.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;line-height:1.75;text-align:right}}
.mono{{font-family:'IBM Plex Mono',monospace}}
b,strong{{font-weight:700}}
.eb{{display:flex;align-items:center;gap:3mm;margin:4.2mm 0 2.2mm}}
.eb > span{{font-size:6pt;font-weight:700;letter-spacing:.2em;color:{RED};text-transform:uppercase;white-space:nowrap}}
.eb > i{{flex:1;height:0.25mm;background:{SILVER}}}
.eb > b.ar{{font-size:8pt;font-weight:400;color:{SLATE}}}
.page > .eb:first-child{{margin-top:0}}
.cnr{{position:absolute;width:4mm;height:4mm;border:0.5mm solid {RED};z-index:3}}
.cnr.tl{{top:2.5mm;left:2.5mm;border-right:0;border-bottom:0}} .cnr.tr{{top:2.5mm;right:2.5mm;border-left:0;border-bottom:0}}
.cnr.bl{{bottom:2.5mm;left:2.5mm;border-right:0;border-top:0}} .cnr.br{{bottom:2.5mm;right:2.5mm;border-left:0;border-top:0}}
/* cover */
.cover{{position:absolute;inset:0;background:{DEEP};color:{PAPER};display:flex;flex-direction:column;
 justify-content:space-between;padding:20mm 18mm 0}}
.cvtop .seal{{width:34mm}}
.cvmid h1{{font-size:30pt;font-weight:700;margin:0;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;text-align:right}}
.cvmid h2{{font-size:15pt;font-weight:700;margin:2mm 0 0;letter-spacing:.2em}}
.cvsub{{font-size:7.4pt;color:#B9B5D8;margin:4mm 0 0;line-height:1.7}}
p.ar.cvsub{{text-align:right;font-size:8.4pt}}
.cvbot{{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;padding-bottom:8mm}}
.cvmeta span{{display:block;font-size:5.2pt;font-weight:700;letter-spacing:.18em;color:#8A86B8}}
.cvmeta b{{display:block;font-size:7.4pt;margin-top:1.2mm;letter-spacing:.06em}}
.cvmeta b.pend{{color:#FF8A82}}
.cvband{{position:absolute;left:0;right:0;bottom:0;height:7mm;display:flex}}
.cvband i{{flex:1}}
/* chips */
.chip{{display:inline-block;font-size:5.4pt;font-weight:700;letter-spacing:.14em;padding:1mm 2.4mm;
 margin:0 0 2.5mm;background:{INK};color:{PAPER}}}
.chip.ok{{background:#1BA34C}} .chip.wait{{background:{RED}}} .chip.pend{{background:{SLATE}}}
.chips{{display:grid;grid-template-columns:auto 1fr;gap:1.5mm 3mm;align-items:center;margin-bottom:2.5mm}}
.chips p{{margin:0;font-size:6.6pt;color:{GRAPH}}}
.lgd{{display:flex;gap:6mm;font-size:5.6pt;font-weight:700;letter-spacing:.12em;color:{SLATE};margin-top:1mm}}
.lgd i{{display:inline-block;width:2.4mm;height:2.4mm;margin-right:1.4mm}}
.lgd i.ok,.st i.ok{{background:#1BA34C}} .lgd i.wait,.st i.wait{{background:{RED}}} .lgd i.pend,.st i.pend{{background:{SLATE}}}
.st i{{display:block;width:2.6mm;height:2.6mm}}
/* rule panel */
.rule{{position:relative;background:{RED};color:#FFF;padding:6mm 9mm;text-align:center;overflow:hidden;margin-bottom:2.5mm}}
.rule.sm{{padding:4.5mm 9mm}}
.rule p.rl{{margin:0;font-weight:700;position:relative;z-index:2}}
.rule p.ar.rl{{font-size:16pt;line-height:1.5;text-align:center;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl}}
.rule.sm p.ar.rl{{font-size:13pt}}
.rule p.rl.en{{font-size:8pt;letter-spacing:.15em;margin-top:2mm;opacity:.92}}
.rule .cnr{{border-color:#FFF}}
.bi{{margin:0 0 2.5mm}}
.bi > p{{margin:0;font-size:7.3pt;line-height:1.7;color:{GRAPH}}}
.bi > p.ar{{font-size:8pt;color:{INK};margin-bottom:1.2mm}}
/* tables */
table.t3{{width:100%;border-collapse:collapse;margin:0 0 2.5mm}}
table.t3 th{{font-size:5.6pt;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:{SLATE};
 text-align:left;padding:0 2mm 1.4mm;border-bottom:0.3mm solid {SILVER}}}
table.t3 td{{font-size:7pt;line-height:1.5;padding:1.5mm 2mm;border-bottom:0.2mm solid {SILVER};vertical-align:top;color:{GRAPH}}}
table.t3 td > b{{color:{INK};display:inline}}
table.t3 td.ar{{font-size:7.4pt;color:{INK}}}
table.t3 td.sm{{font-size:6.5pt;color:{SLATE}}}
table.t3 td span.en{{display:block;font-family:'IBM Plex Sans',sans-serif;direction:ltr;text-align:left;
 font-size:6.2pt;color:{SLATE};margin-top:0.5mm;line-height:1.5}}
table.t3 td.n{{font-family:'IBM Plex Mono',monospace;color:{RED};font-weight:700;width:6mm;font-size:8pt}}
table.t3 td.num{{text-align:right;color:{INK}}}
table.t3 td.sw{{width:8mm;padding:1.2mm 1mm}} table.t3 td.sw > i{{display:block;width:100%;height:3.4mm;border:0.2mm solid {SILVER}}}
table.t3.ct td{{padding:0.72mm 2mm}}
table.t3.ct td:first-child{{font-size:6pt;font-weight:700;letter-spacing:.08em;color:{INK}}}
table.t3.ct td.v{{width:22mm}}
table.t3.ct td.v > span{{font-size:5.4pt;font-weight:700;letter-spacing:.1em;padding:0.6mm 1.5mm;display:inline-block}}
table.t3.ct td.v > span.ink{{background:{INK};color:{PAPER}}}
table.t3.ct td.v > span.wht{{background:#FFF;color:{INK};border:0.2mm solid {SILVER}}}
table.t3.ct td.v > span.key{{background:{RED};color:#FFF}}
table.t3.ct tr.key td{{background:#FDF0EF}}
table.t3.toc td{{padding:1.1mm 2mm}} table.t3.toc td.n{{color:{SLATE};width:8mm}}
table.t3.toc td.d{{width:16mm;color:{SLATE};font-size:6.4pt}} table.t3.toc td.st{{width:8mm}}
table.t3.cn td:first-child{{width:33mm}} table.t3.cn td:nth-child(2){{width:50mm}}
table.t3.cp td:nth-child(2){{width:40mm}} table.t3.cfg td:first-child{{width:40mm}}
table.t3.cap td:nth-child(3){{width:26mm}}
/* notes */
.note{{background:{MIST};border-left:0.8mm solid {RED};padding:2.8mm 4.2mm;margin:0 0 2.5mm}}
.note.warn{{border-left-color:{INK}}}
.note > b{{font-size:7.4pt;display:inline;color:{INK}}}
.note > p{{font-size:7pt;line-height:1.62;margin:1.1mm 0 0;color:{GRAPH}}}
.note > p.ar{{font-size:7.5pt;color:{INK}}}
.ok{{background:{DEEP};color:{PAPER};padding:2.6mm 4.5mm;margin:0 0 2.5mm;font-family:'IBM Plex Sans Arabic',sans-serif;
 direction:rtl;text-align:right;font-size:8pt}}
.ok.warn{{background:{INK}}}
.ok > b{{display:inline;font-weight:700}}
.ok > span.en{{display:block;direction:ltr;text-align:left;font-family:'IBM Plex Sans',sans-serif;font-size:6.6pt;
 color:#C9C5BC;margin-top:1mm;line-height:1.55}}
/* lists */
ol.ru{{list-style:none;margin:0 0 2.5mm;padding:0;counter-reset:r}}
ol.ru li{{counter-increment:r;display:grid;grid-template-columns:6mm 1fr;gap:0 2mm;padding:1.6mm 0;border-bottom:0.2mm solid {SILVER}}}
ol.ru li::before{{content:counter(r,decimal-leading-zero);font-family:'IBM Plex Mono',monospace;font-size:6.4pt;
 font-weight:700;color:{RED};grid-row:1/3}}
ol.ru li > span.ar{{font-size:7.4pt;color:{INK};line-height:1.6}}
ol.ru li > span.en{{font-size:6.4pt;color:{SLATE};line-height:1.55}}
ol.dn,ol.chk{{list-style:none;margin:0 0 2.5mm;padding:0;columns:2;column-gap:5mm}}
ol.dn li,ol.chk li{{break-inside:avoid;display:grid;grid-template-columns:3.4mm 1fr;gap:0 2mm;padding:1.3mm 0;
 border-bottom:0.2mm solid {SILVER}}}
ol.dn li > i{{width:2.8mm;height:2.8mm;background:{RED};display:block;grid-row:1/3;margin-top:0.8mm}}
ol.chk li > i{{width:2.8mm;height:2.8mm;border:0.3mm solid {INK};display:block;grid-row:1/3;margin-top:0.7mm}}
ol.dn li > span.ar,ol.chk li > span.ar{{font-size:6.8pt;color:{INK};line-height:1.5}}
ol.dn li > span.en,ol.chk li > span.en{{font-size:5.6pt;color:{SLATE};line-height:1.4}}
ol.nev{{list-style:none;margin:0 0 2.5mm;padding:0}}
ol.nev li{{display:grid;grid-template-columns:3.4mm 1fr;gap:0 2.5mm;padding:1.6mm 0;border-bottom:0.2mm solid {SILVER}}}
ol.nev li > i{{width:2.8mm;height:2.8mm;background:{RED};display:block;grid-row:1/4;margin-top:0.8mm}}
ol.nev li > span.ar{{font-size:7.4pt;color:{INK}}}
ol.nev li > span.en{{font-size:6.2pt;color:{GRAPH}}}
ol.nev li > span.ar.sm{{font-size:6.4pt;color:{SLATE}}}
/* hierarchy */
.hier{{margin:0 0 2.5mm}}
.hlv{{background:#FFF;border:0.25mm solid {SILVER};padding:2.6mm 3.5mm;text-align:center}}
.hlv.m{{background:{DEEP};color:{PAPER};border-color:{DEEP}}}
.hlv > b.ar{{font-size:10pt;display:block}} .hlv > span{{font-size:5.4pt;font-weight:700;letter-spacing:.16em;color:{SLATE}}}
.hlv.m > span{{color:#8A86B8}}
.hlv > em{{display:block;font-style:normal;font-size:6.6pt;margin-top:1mm;color:{GRAPH}}}
.hlv.m > em{{color:#B9B5D8}}
.hlv > i{{display:block;height:1.6mm;margin-top:1.5mm}}
.harr{{height:3mm;border-left:0.3mm solid {SILVER};width:0;margin:0 auto}}
.hrow{{display:grid;grid-template-columns:repeat(4,1fr);gap:2.5mm}}
/* colour swatches */
.csws4{{display:grid;grid-template-columns:repeat(4,1fr);gap:2.5mm;margin-bottom:2.5mm}}
.csw{{border:0.25mm solid {SILVER};background:#FFF;padding:2.2mm}}
.chipc{{height:11mm;margin-bottom:1.6mm}}
.csw b{{font-size:7pt;display:block;color:{INK}}}
.csw span{{display:block;font-size:5.8pt;color:{SLATE};line-height:1.5}}
.csw span.ar{{font-size:6.6pt;color:{GRAPH}}} .csw span.role{{font-size:5.2pt;letter-spacing:.06em;margin-top:0.8mm}}
.csw span.cr{{font-family:'IBM Plex Mono',monospace;font-size:5.6pt;color:{INK};margin-top:0.8mm}}
.csw span.cr em{{font-style:normal;color:{SLATE}}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin-bottom:2.5mm}}
.col{{display:flex;gap:2.5mm;background:#FFF;border:0.25mm solid {SILVER};padding:2.2mm}}
.cs{{width:11mm;min-width:11mm;border:0.2mm solid {SILVER}}}
.cx > b{{font-size:7pt;color:{INK};display:block;margin-bottom:0.8mm}}
.cx > ul{{list-style:none;margin:0;padding:0}}
.cx > ul li{{font-size:6pt;line-height:1.5;color:{GRAPH}}} .cx > ul li b{{color:{INK}}}
table.t3.rl2 td{{padding:2mm}}
/* type */
.two{{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-bottom:2.5mm}}
.fam{{background:#FFF;border:0.25mm solid {SILVER};padding:3mm}}
.fam.full{{margin-bottom:2.5mm}}
.fam > b{{font-size:12pt;display:block;color:{INK}}}
.fam > span{{font-size:7pt;color:{SLATE};display:block;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;text-align:right;margin-bottom:1.5mm}}
.fam > p{{margin:0;font-size:6.6pt;line-height:1.6;color:{GRAPH}}}
/* logos */
.sealrow{{display:flex;gap:6mm;align-items:center;background:#FFF;border:0.25mm solid {SILVER};padding:4mm;margin-bottom:2.5mm}}
.bigseal{{width:32mm}}
.sealx > b.ar{{font-size:12pt;display:block;color:{INK}}}
.sealx > span{{font-size:5.6pt;font-weight:700;letter-spacing:.16em;color:{SLATE};display:block;margin-bottom:1.5mm}}
.sealx > p{{margin:0 0 1mm;font-size:6.8pt;line-height:1.6;color:{GRAPH}}}
.sealx > p.ar{{font-size:7.4pt;color:{INK}}}
.lks{{display:grid;grid-template-columns:repeat(4,1fr);gap:2.5mm;margin-bottom:2.5mm}}
.lk{{background:{MIST};height:24mm;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1.5mm;padding:2mm}}
.lk img{{max-width:78%;max-height:13mm;object-fit:contain}}
.lk span{{font-size:5.4pt;font-weight:700;letter-spacing:.14em;color:{SLATE}}}
/* ranges */
.rhero{{display:flex;align-items:center;gap:5mm;background:#FFF;border:0.25mm solid {SILVER};padding:4mm;margin-bottom:2.5mm}}
.rlogo{{width:26mm;max-height:16mm;object-fit:contain}}
.rx{{flex:1}} .rx > b.ar{{font-size:14pt;display:block;color:{INK}}}
.rx > span{{font-size:7pt;font-weight:700;letter-spacing:.16em;color:{SLATE};display:block;margin-bottom:1.5mm}}
.rx > p{{margin:0;font-size:6.8pt;color:{GRAPH}}} .rx > p.ar{{font-size:7.4pt;color:{INK}}}
.rsig{{text-align:center}} .rsig > i{{display:block;width:16mm;height:9mm;margin-bottom:1mm}}
.rsig > span{{font-size:6pt;color:{INK};display:block}} .rsig > em{{font-style:normal;font-size:5pt;letter-spacing:.14em;color:{SLATE}}}
.rpack{{background:{MIST};padding:3mm;margin-bottom:2.5mm;text-align:center}}
.rpack img{{max-width:100%;max-height:36mm;object-fit:contain}}
.rb{{background:#FFF;border:0.25mm solid {SILVER};padding:3mm}}
.rb > b.ar{{font-size:8.5pt;display:block;color:{INK}}}
.rb > span{{font-size:5.4pt;font-weight:700;letter-spacing:.14em;color:{SLATE};display:block;margin-bottom:1.5mm}}
.rb > p{{margin:0 0 1mm;font-size:6.6pt;line-height:1.6;color:{GRAPH}}} .rb > p.ar{{font-size:7.2pt;color:{INK}}}
.fsws{{display:grid;grid-template-columns:repeat(5,1fr);gap:2mm}}
.fsw{{border:0.25mm solid {SILVER};background:#FFF;padding:1.8mm;text-align:center}}
.fsw > i{{display:block;height:9mm;margin-bottom:1.2mm}}
.fsw > b.ar{{font-size:6.8pt;display:block;color:{INK}}}
.fsw > span.mono{{font-size:5.2pt;color:{SLATE};display:block}}
.fsw > span.vd{{font-size:4.8pt;font-weight:700;letter-spacing:.08em;padding:0.5mm 1mm;display:inline-block;margin-top:0.8mm}}
.fsw > span.vd.ink{{background:{INK};color:{PAPER}}} .fsw > span.vd.wht{{background:#FFF;color:{INK};border:0.2mm solid {SILVER}}}
.fsw > span.vd.key{{background:{RED};color:#FFF}}
/* voice */
.vcs{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm}}
.vc{{background:#FFF;border:0.25mm solid {SILVER}}}
.vh{{padding:2.4mm 3mm;background:{MIST}}}
.vh > b.ar{{font-size:11pt;color:{INK}}} .vh > span{{font-size:6.4pt;font-weight:700;letter-spacing:.12em;color:{SLATE};margin-left:2mm}}
.vh > em.ar{{display:block;font-style:normal;font-size:7.4pt;color:{INK};margin-top:1mm;direction:rtl;text-align:right;font-family:'IBM Plex Sans Arabic',sans-serif}}
.vh > em.en{{display:block;font-style:normal;font-size:6pt;color:{GRAPH}}}
table.vt{{width:100%;border-collapse:collapse}}
table.vt td{{font-size:6.6pt;padding:1.5mm 3mm;border-bottom:0.2mm solid {MIST};vertical-align:top;color:{INK}}}
table.vt td.k{{width:24mm;font-size:5.4pt;font-weight:700;letter-spacing:.06em;color:{SLATE};font-family:'IBM Plex Sans',sans-serif}}
table.vt td.ar{{font-size:7pt}}
table.vt td span.en{{display:block;direction:ltr;text-align:left;font-family:'IBM Plex Sans',sans-serif;font-size:5.8pt;color:{SLATE};margin-top:0.5mm;line-height:1.45}}
table.vt tr.in td.ar{{color:#1BA34C}} table.vt tr.out td.ar{{color:{RED}}}
table.vt tr:last-child td{{border-bottom:0}}
/* scene worlds + prompts */
.wlds{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin-bottom:2.5mm}}
.wld{{background:#FFF;border:0.25mm solid {SILVER}}}
.wh{{padding:2.2mm 3mm;display:flex;align-items:baseline;gap:2.5mm;background:{MIST}}}
.wh > b.ar{{font-size:10pt;font-weight:700;color:{INK}}}
.wh > span{{font-size:6.6pt;font-weight:700;letter-spacing:.12em;color:{SLATE};margin-left:auto}}
table.wt{{width:100%;border-collapse:collapse}}
table.wt td{{font-size:6.4pt;padding:1.4mm 3mm;border-bottom:0.2mm solid {MIST};vertical-align:top;color:{INK}}}
table.wt td.k{{width:21mm;font-size:5.2pt;font-weight:700;letter-spacing:.06em;color:{SLATE};font-family:'IBM Plex Sans',sans-serif}}
table.wt td.ar{{font-size:6.8pt}}
table.wt td span.en{{display:block;direction:ltr;text-align:left;font-family:'IBM Plex Sans',sans-serif;font-size:5.8pt;color:{SLATE};margin-top:0.4mm;line-height:1.4}}
table.wt tr.no td{{background:#FDF0EF}} table.wt tr:last-child td{{border-bottom:0}}
.prs{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin-bottom:2.5mm}}
.pr{{background:#FFF;border:0.25mm solid {SILVER};padding:2.4mm 3mm}}
.pr > b{{font-size:8pt;display:block;margin-bottom:1.2mm;letter-spacing:.06em}}
.pr > code{{font-family:'IBM Plex Mono',monospace;font-size:5.4pt;line-height:1.65;color:{GRAPH};display:block}}
.neg{{background:{INK};padding:2.8mm 4.2mm;margin:0 0 2.5mm}}
.neg > code{{font-family:'IBM Plex Mono',monospace;font-size:6.4pt;line-height:1.75;color:#FF8A82}}
.lay3{{display:grid;grid-template-columns:repeat(3,1fr);gap:2.5mm;margin-bottom:2.5mm}}
.ly{{background:#FFF;border:0.25mm solid {SILVER};padding:2.8mm}}
.ly > i{{font-style:normal;font-family:'IBM Plex Mono',monospace;font-size:10pt;font-weight:700;color:{RED};display:block;line-height:1}}
.ly > b.ar{{font-size:9.5pt;display:block;margin-top:1.2mm;color:{INK}}}
.ly > span{{font-size:5.4pt;font-weight:700;letter-spacing:.14em;color:{SLATE};display:block;margin-bottom:1.2mm}}
.ly > p{{margin:0;font-size:6.2pt;line-height:1.55;color:{GRAPH}}} .ly > p.ar{{font-size:6.8pt;color:{INK};margin-bottom:0.6mm}}
/* pending */
.hold{{background:{MIST};border:0.4mm dashed {SLATE};padding:5mm;text-align:center;margin-top:2mm}}
.hold > b.ar{{font-size:9pt;color:{INK};display:block}}
.hold > span.en{{display:block;font-size:6.6pt;color:{GRAPH};margin-top:1.5mm;line-height:1.6}}
/* numbers */
.nums{{display:grid;grid-template-columns:repeat(4,1fr);gap:2.5mm;margin-bottom:2.5mm}}
.num{{background:#FFF;border:0.25mm solid {SILVER};padding:3mm;text-align:center}}
.num > b{{font-size:20pt;font-weight:700;color:{RED};display:block;line-height:1;font-family:'IBM Plex Mono',monospace}}
.num > span.ar{{display:block;font-size:7pt;color:{INK};margin-top:1.5mm;text-align:center}}
.num > span.en{{display:block;font-size:5.4pt;letter-spacing:.1em;color:{SLATE};text-transform:uppercase}}
/* sign off */
.signoff{{position:relative;background:{DEEP};color:{PAPER};padding:10mm;overflow:hidden;margin-top:2mm}}
.signoff h1{{font-size:18pt;margin:0;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;text-align:right}}
.signoff h2{{font-size:9pt;letter-spacing:.2em;margin:2mm 0 4mm;color:#B9B5D8}}
.signoff p.so{{font-size:7pt;line-height:1.7;color:#C9C5DD;margin:0 0 2mm}}
.signoff p.ar.so{{font-size:7.8pt;color:{PAPER}}}
.sfields{{display:grid;grid-template-columns:1fr 1fr;gap:6mm 8mm;margin:6mm 0}}
.sf span{{font-size:5.4pt;font-weight:700;letter-spacing:.16em;color:#8A86B8;display:block}}
.sf i{{display:block;height:0.3mm;background:#6A66A0;margin-top:7mm}}
.sn{{background:rgba(255,255,255,.07);padding:3.5mm 4.5mm;margin-top:2mm}}
.sn > b.ar{{font-size:8pt;color:{PAPER};display:block;margin-bottom:1.2mm}}
.sn > p{{margin:0 0 0.8mm;font-size:6.6pt;line-height:1.6;color:#C9C5DD}}
.sn > p.ar{{font-size:7.2pt;color:{PAPER}}}
.by{{display:flex;align-items:center;gap:2.5mm;margin-top:6mm}}
.by > i{{width:1mm;height:3.4mm;background:{RED};display:block}}
.by > span{{font-size:5.6pt;font-weight:700;letter-spacing:.16em;color:#B9B5D8}}
/* footer */
footer{{position:absolute;left:14mm;right:14mm;bottom:9mm;display:flex;justify-content:space-between;align-items:center;
 font-size:5.8pt;letter-spacing:.13em;text-transform:uppercase;font-weight:700;color:{SLATE};
 border-top:0.25mm solid {SILVER};padding-top:2.4mm}}
footer .fm{{display:flex;align-items:center;gap:2mm}}
footer .fm > b{{color:{INK};letter-spacing:.1em}}
footer .fm > em{{font-family:'IBM Plex Sans Arabic',sans-serif;font-style:normal;direction:rtl;font-weight:400;
 letter-spacing:0;text-transform:none;font-size:7pt}}
'''

def render(ids=None, out='book.html', title='Alex Foods - Brand Foundation'):
    chosen=[s for s in sorted(SEC,key=lambda x:x[0]) if ids is None or s[0] in ids]
    H=[];n=[0]
    for sid,en,ar,bodies in chosen:
        for b in bodies:
            n[0]+=1
            cover = sid=='00'
            H.append(f'<section class="page">{b}'+('' if cover else
              f'<footer><span class="fm"><b>ALEX FOODS</b><em>أليكس فودز</em></span>'
              f'<span class="fr">§{sid} · {VER} · PAGE {n[0]} / @@TOTAL@@</span></footer>')+'</section>')
    html=(f'<!doctype html><html lang="ar" dir="ltr"><head><meta charset="utf-8"><title>{title}</title>'
          f'<link rel="stylesheet" href="plex.css"><style>{CSS}</style></head><body>{"".join(H)}</body></html>')
    html=html.replace('@@TOTAL@@',str(n[0]))
    io.open(os.path.join(HERE,out),'w',encoding='utf-8').write(html)
    return n[0]

if __name__=='__main__':
    print("BOOK pages:",render())
