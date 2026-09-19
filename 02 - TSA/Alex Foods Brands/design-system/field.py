# -*- coding: utf-8 -*-
# Alex Foods - Book section 12: THE PACK IN FIELD SYSTEM.
# A book section, not a standalone deliverable. Renders as proven pages that
# drop into the book build. Shares colour.py, ranges.py, plex.css and fonts/.
# NOTE: no em dashes in output copy. Voice Guide S1 rule 8.
import io, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
exec(open(os.path.join(HERE,'colour.py')).read().split('# sanity')[0])
from ranges import RANGES

PAPER='#FAF8F3'; INK='#141414'; GRAPH='#4A4742'; SLATE='#8A8681'
SILVER='#C9C5BC'; MIST='#EDEAE3'; RED='#E1251D'; NAVY='#0A0378'; DEEP='#05004B'

def verdict(h):
    k=ratio(INK,h); w=ratio('#FFFFFF',h)
    if k>=4.5 and k>=w: return ('INK',INK,k,False)
    if w>=4.5 and w>k:  return ('WHITE','#FFFFFF',w,False)
    return ('KEYLINE',INK if k>=w else '#FFFFFF',max(k,w),True)

# every exact collision, computed
seen={}
for r in RANGES:
    seen.setdefault(r['sig'],[]).append((r['en'],'range signature','إشارة المجموعة'))
    for en,ar,h in r['fl']:
        seen.setdefault(h,[]).append((r['en'],en+' field','حقل '+ar))
COLL={h:v for h,v in seen.items() if len(v)>1}
NFIELD=sum(len(r['fl']) for r in RANGES)
NKEY=sum(1 for r in RANGES for _,_,h in r['fl'] if verdict(h)[3])
NINK=sum(1 for r in RANGES for _,_,h in r['fl'] if verdict(h)[0]=='INK')

H=[]; PAGES=[0]
def p(s): H.append(s)
def page(body,label=''):
    PAGES[0]+=1
    p(f'<section class="page">{body}'
      f'<footer><span class="fm"><b>ALEX FOODS</b><em>أليكس فودز</em></span>'
      f'<span class="fr">{label} · BOOK §12 · PAGE {PAGES[0]} / @@TOTAL@@</span></footer></section>')
def eb(ar,en): return f'<div class="eb"><span>{en}</span><i></i><b class="ar">{ar}</b></div>'
def cnr(): return '<i class="cnr tl"></i><i class="cnr tr"></i><i class="cnr bl"></i><i class="cnr br"></i>'
def bi(ar,en): return f'<div class="bi"><p class="ar">{ar}</p><p class="en">{en}</p></div>'

# ---------- PAGE 1 : THE DEVICE ----------
SHAPES=[('بيبو','BeBo','pillow','كيس وسادة','pillow bag','عريض','wide','62٪ من عرض الإطار','62% of frame width'),
('الراوي','AlRawy','pouch','عبوة قائمة','standing pouch','قائم','upright','58٪ من ارتفاع الإطار','58% of frame height'),
('تومان','2MAN','stick','إصبع مثلج','ice stick','طويل ورفيع','tall and narrow','70٪ من ارتفاع الإطار','70% of frame height'),
('بوليكا','POLEKA','bottle','عبوة زجاجة','bottle pouch','قائم','upright','58٪ من ارتفاع الإطار','58% of frame height')]
sh=''.join(f'''<tr><td><b class="ar">{a}</b><span class="en">{b}</span></td>
 <td class="ar">{sa}<span class="en">{se}</span></td><td class="ar">{oa}<span class="en">{oe}</span></td>
 <td class="ar"><b>{za}</b><span class="en">{ze}</span></td></tr>''' for a,b,k,sa,se,oa,oe,za,ze in SHAPES)

page(f'''{eb('نظام العبوة على الحقل','12 · THE PACK IN FIELD SYSTEM')}
<div class="rule">{cnr()}
 <p class="ar rl">العبوة على حقل نكهتها.</p>
 <p class="rl en">THE PACK ON ITS FLAVOUR FIELD.</p></div>
{bi('كل رسم، وكل صورة متحركة، وكل أنيميشن في هذا التعاقد مبني من هذا الشيء الواحد. ليس أسلوبًا من بين أساليب، بل الجهاز البصري الذي يميّز أليكس فودز. إذا تغيّر، تغيّرت العلامة.',
    'Every graphic, every animated still and every animation on this contract is built from this one thing. It is not one style among several, it is the visual device that identifies Alex Foods. If it changes, the brand changes.')}

{eb('الطبقات الثلاث','THE THREE LAYERS')}
<div class="lay3">
 <div class="ly"><i>1</i><b class="ar">الحقل</b><span>THE FIELD</span>
  <p class="ar">لون النكهة يملك الحقل. يتغيّر مع كل صنف.</p><p class="en">The flavour colour owns the field. It changes per SKU.</p></div>
 <div class="ly"><i>2</i><b class="ar">العبوة</b><span>THE PACK</span>
  <p class="ar">فن العميل نفسه، مقصوص على شفافية. لا يُعاد رسمه أبدًا.</p><p class="en">The client's own artwork, cut out on transparency. Never redrawn.</p></div>
 <div class="ly"><i>3</i><b class="ar">النص</b><span>THE TYPE</span>
  <p class="ar">حبري أو أبيض، والقرار محسوب لا مُخمَّن.</p><p class="en">Ink or white, and the decision is computed rather than guessed.</p></div>
</div>
<div class="note"><b>القاعدة التي تحكم الطبقات · The rule that governs the layers</b>
<p class="ar">لون النكهة يملك الحقل. لون المجموعة يملك الشعار. الماستر يملك الختم، ولا يأخذ أيًّا منهما.</p>
<p class="en">The flavour colour owns the field. The range colour owns the logo. The master owns the seal, and takes neither.</p></div>

{eb('الهندسة · شكل العبوة يحدّد المقاس','GEOMETRY · THE PACK SHAPE SETS THE SCALE')}
{bi('أربع مجموعات بأربعة أشكال عبوات. مقاس واحد ثابت لكلها ينتج إطارًا فارغًا لتومان وإطارًا مزدحمًا لبيبو. المقاس يتبع الشكل، والهامش هو الثابت.',
    'Four ranges with four pack shapes. One fixed scale across all of them produces an empty frame for 2MAN and a crowded one for BeBo. The scale follows the shape, and the margin is what stays constant.')}
<table class="t3"><thead><tr><th>المجموعة · RANGE</th><th>الشكل · SHAPE</th><th>الاتجاه · ORIENTATION</th><th>المقاس · SCALE</th></tr></thead><tbody>{sh}</tbody></table>
<div class="note warn"><b>الثوابت في كل إطار · Constant in every frame</b>
<p class="ar">هامش 8٪ من كل جانب لا تدخله العبوة أبدًا. العبوة في الثلث الأوسط أفقيًّا. منطقة النص أسفل الإطار دائمًا، لا فوقه.</p>
<p class="en">An 8% margin on every side that the pack never enters. The pack sits in the middle third horizontally. The type zone is always at the foot of the frame, never the head.</p></div>''','THE DEVICE')

# ---------- PAGE 2 : TYPE ON THE FIELD ----------
rows=''
for r in RANGES:
    for i,(en,ar,h) in enumerate(r['fl']):
        v,col,rt,key=verdict(h)
        cls='key' if key else ('wht' if v=='WHITE' else '')
        rows+=(f'<tr class="{cls}"><td>{r["en"] if i==0 else ""}</td>'
               f'<td><b class="ar">{ar}</b><span class="en">{en}</span></td>'
               f'<td class="mono">{h}</td>'
               f'<td class="sw"><i style="background:{h}"></i></td>'
               f'<td class="mono num">{ratio(INK,h):.2f}</td><td class="mono num">{ratio("#FFFFFF",h):.2f}</td>'
               f'<td class="v"><span class="{cls or "ink"}">{v}</span></td></tr>')

page(f'''{eb('النص على الحقل','TYPE ON THE FIELD')}
<div class="ok"><b>الافتراضي مقلوب: الحبري هو الأصل على حقل النكهة، والأبيض هو الاستثناء الذي يُفحص.</b>
<span class="en">The default is flipped: Ink is the default on a flavour field, and white is the exception that has to be checked.</span></div>
{bi(f'الغريزة في هذه الفئة أن يكون النص أبيض على حقل لامع، وعلى هذه اللوحة تحديدًا الغريزة خاطئة أكثر مما هي صحيحة. نصف الحقول أصفر باهت وليموني، والأبيض عليها يختفي. الحبري يفوز على {NINK} حقلًا من {NFIELD}.',
    f'The instinct in this category is white type on a bright field, and on this palette that instinct is wrong more often than it is right. Half these fields are pale yellow and lime, where white disappears. Ink wins on {NINK} of {NFIELD} fields.')}
<table class="t3 ct"><thead><tr><th>المجموعة</th><th>النكهة · FLAVOUR</th><th>HEX</th><th></th><th>INK</th><th>WHITE</th><th>الحكم · VERDICT</th></tr></thead><tbody>{rows}</tbody></table>
<div class="note warn"><b>الحقول الثلاثة التي تحتاج خطًّا محيطًا · The three fields that need a keyline</b>
<p class="ar">ثلاثة حقول من {NFIELD} لا يعبر عليها الحبري ولا الأبيض حدّ 4.5. تفاح بيبو، وكولا بوليكا، وفراولة بوليكا. هذه الثلاثة تحمل خطًّا محيطًا داكنًا خلف النص دائمًا.</p>
<p class="en">Three fields out of {NFIELD} clear 4.5 with neither ink nor white: BeBo apple, POLEKA cola and POLEKA strawberry. Those three always carry a dark keyline behind the type.</p></div>''','TYPE ON FIELD')

# ---------- PAGE 3 : THE COLLISIONS ----------
cb=''
for h,v in COLL.items():
    who=''.join(f'<li><b>{a}</b> <span>{b}</span></li>' for a,b,c in v)
    cb+=f'''<div class="col"><div class="cs" style="background:{h}"></div>
     <div class="cx"><b class="mono">{h}</b><ul>{who}</ul></div></div>'''

page(f'''{eb('التصادمات','THE COLLISIONS')}
{bi(f'حساب اللوحة كاملةً أخرج {len(COLL)} تصادمات لونية دقيقة. ليست أخطاء، لأن العبوات مطبوعة وفي السوق بالفعل ولا أحد يعيد طلاءها. لكنها تصبح أخطاء في اللحظة التي يُبنى فيها تخطيط دون معرفتها.',
    f'Computing the whole palette produced {len(COLL)} exact colour collisions. They are not defects, because the packs are printed and in market and nobody is repainting them. They become defects the moment a layout is built without knowing about them.')}
<div class="cols">{cb}</div>

{eb('القواعد التي تحلّها','THE RULES THAT RESOLVE THEM')}
<table class="t3 rl2"><tbody>
<tr><td class="n">1</td><td><b class="ar">العبوة هي التي تعرّف الصنف، لا الحقل.</b>
 <span class="en"><b>The pack identifies the SKU, never the field.</b> A field colour is a stage, not a name. The artwork on it is what says which product this is, which is why a field may be reused and a pack may not.</span></td></tr>
<tr><td class="n">2</td><td><b class="ar">مجموعتان لا تشتركان في تخطيط واحد أبدًا.</b>
 <span class="en"><b>Two ranges never share one layout.</b> AlRawy peach and 2MAN red are the same red. Side by side in one frame they read as one product line. Apart, in their own posts, nobody will ever know.</span></td></tr>
<tr><td class="n">3</td><td><b class="ar">أخضر بيبو <span class="mono">#1BA34C</span> إشارة مجموعة، وحقل نكهة لمجموعتين أخريين. لا يُستخدم كعنصر علامة إلا على بيبو.</b>
 <span class="en"><b>BeBo's signature green is also AlRawy's guava field and POLEKA's apple field, a three way collision.</b> It stays a brand element on BeBo only. On the other two it is a stage and never a badge, a border or a logo ground.</span></td></tr>
<tr><td class="n">4</td><td><b class="ar">بوليكا لها أربعة أصناف وثلاثة حقول فقط، واثنان منها لون العلامة نفسه.</b>
 <span class="en"><b>POLEKA has four SKUs but only three distinct fields, and two of them are the brand colour.</b> Four posts built straight off the flavour map show three colours, twice. <b>This is what the extended colour layer exists for</b>, and on POLEKA it is not optional.</span></td></tr>
<tr><td class="n">5</td><td><b class="ar">إشارة تومان هي نفسها حقل الأزرق. على ذلك الصنف تُحمل العلامة بالشكل لا باللون.</b>
 <span class="en"><b>2MAN's signature is its own blue field.</b> On the blue SKU the brand layer and the flavour layer are the same colour, so nothing separates them. There, the mark carries the brand by shape, and the field carries nothing.</span></td></tr>
</tbody></table>
<div class="note warn"><b>التصادم الذي يخصّ الشعار لا النص · The collision that hits the logo, not the type</b>
<p class="ar">شريط بيبو الأخضر <span class="mono">#1BA34C</span> على حقل التفاح <span class="mono">#2C8C3B</span> يعطي تباينًا قدره 1.30 إلى 1. الشعار يكاد يختفي في حقله، ولا يمسكه إلا الخط الكحلي المحيط به. على هذا الصنف تحديدًا، الخط الكحلي ليس تفصيلًا.</p>
<p class="en">BeBo's green banner on the apple field gives 1.30:1. The logo nearly vanishes into its own field and is held together only by the navy keyline around it. On that one SKU, the navy keyline is not a detail.</p></div>
<div class="note"><b>الخط المحيط أداة وضوح، لا زينة · The keyline is a legibility device, not decoration</b>
<p class="ar">لا يُضاف لأنه يبدو جميلًا، ولا يُحذف لأن المصمم يفضّل بدونه. يُضاف حين يقول الرقم إنه لازم.</p>
<p class="en">It is not added because it looks good, and not dropped because a designer prefers it without. It is added when the number says it is needed.</p></div>''','COLLISIONS')

# ---------- PAGE 4 : DO NOT + CONFIGURABLES ----------
DN=[('عبوة على حقل ليس حقل نكهتها','a pack on a field that is not its own flavour'),
('عبوة بلا ظل تلامس، تطفو على الحقل','a pack with no contact shadow, floating on the field'),
('نص أبيض على حقل يحتاج خطًّا محيطًا','white type on a field that needs a keyline'),
('شعار المجموعة يتلوّن بلون النكهة','the range logo recoloured to match the flavour'),
('مجموعتان في إطار واحد','two ranges in one frame'),
('عبوة تدخل هامش الـ8٪','a pack entering the 8% margin'),
('حقل متدرّج أو بملمس','a gradient or textured field'),
('نص فوق العبوة نفسها','type laid over the pack itself')]
dn=''.join(f'<li><i></i><span class="ar">{a}</span><span class="en">{e}</span></li>' for a,e in DN)
CFG=[('الحقل','The field','لون النكهة من الخريطة، أو لون ممتد لبوليكا','the flavour colour from the map, or an extended colour on POLEKA'),
('مقاس العبوة','Pack scale','حسب الشكل، من 58٪ إلى 70٪','by shape, 58% to 70%'),
('لون النص','Type colour','محسوب، لا يُختار','computed, never chosen'),
('الخط المحيط','Keyline','إلزامي على ثلاثة حقول','mandatory on three fields'),
('المقاس النهائي','Output size','مربع، فيد، ستوري','square, feed, story'),
('الشخصية','Character','اختياري، إلزامي على بوليكا','optional, mandatory on POLEKA')]
cf=''.join(f'<tr><td><b class="ar">{a}</b><span class="en">{b}</span></td><td class="ar">{c}<span class="en">{d}</span></td></tr>' for a,b,c,d in CFG)

page(f'''{eb('ممنوع · افعل ولا تفعل','WHAT A PACK MAY NEVER SIT ON')}
<div class="ok warn"><b>ثمانية أخطاء تُبطل الإطار. كل واحد منها يُرى فورًا، ولهذا يُكتب.</b>
<span class="en">Eight mistakes that void the frame. Every one of them is visible on sight, which is exactly why it gets written down.</span></div>
<ol class="dn">{dn}</ol>

{eb('ما الذي يتغيّر وما الذي لا يتغيّر','THE CONFIGURABLES')}
{bi('هذا هو الجدول الذي يجعل هذا القسم قابلًا للبناء بدل أن يكون قابلًا للإعجاب. أي شخص يصنع منشور يوم الثلاثاء يقرأ هذا الجدول ويعرف ما يملك تغييره وما لا يملكه، دون أن يسأل أحدًا.',
    'This is the table that makes the section buildable rather than admirable. Anybody making the Tuesday post reads it and knows what they may change and what they may not, without asking.')}
<table class="t3 cfg"><thead><tr><th>القابل للتغيير · CONFIGURABLE</th><th>المدى · RANGE OF VALUES</th></tr></thead><tbody>{cf}</tbody></table>
<div class="note"><b>وما لا يتغيّر أبدًا · And what never changes</b>
<p class="ar">الطبقات الثلاث وترتيبها. هامش الـ8٪. منطقة النص في الأسفل. ملكية اللون: النكهة للحقل، المجموعة للشعار، الماستر للختم. لون النص محسوب لا مختار.</p>
<p class="en">The three layers and their order. The 8% margin. The type zone at the foot. Colour ownership: flavour owns the field, range owns the logo, master owns the seal. And the type colour is computed, never chosen.</p></div>
<div class="sign">{cnr()}<p class="ar">إذا تغيّر هذا الجهاز، تغيّرت العلامة.</p>
<p class="en">IF THIS DEVICE CHANGES, THE BRAND CHANGES.</p></div>''','DO NOT')

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
.rule{{position:relative;background:{RED};color:#FFF;padding:6mm 9mm;text-align:center;overflow:hidden;margin-bottom:2.5mm}}
.rule p.rl{{margin:0;font-weight:700;position:relative;z-index:2}}
.rule p.ar.rl{{font-size:16pt;line-height:1.5;text-align:center;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl}}
.rule p.rl.en{{font-size:8.5pt;letter-spacing:.16em;margin-top:2mm;opacity:.92}}
.rule .cnr{{border-color:#FFF}}
.bi{{margin:0 0 2.5mm}}
.bi > p{{margin:0;font-size:7.4pt;line-height:1.7;color:{GRAPH}}}
.bi > p.ar{{font-size:8pt;color:{INK};margin-bottom:1.2mm}}
table.t3{{width:100%;border-collapse:collapse;margin:0 0 2.5mm}}
table.t3 th{{font-size:5.6pt;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:{SLATE};
 text-align:left;padding:0 2mm 1.4mm;border-bottom:0.3mm solid {SILVER}}}
table.t3 td{{font-size:7pt;line-height:1.5;padding:1.6mm 2mm;border-bottom:0.2mm solid {SILVER};
 vertical-align:top;color:{GRAPH}}}
table.t3 td > b{{color:{INK};display:inline}}
table.t3 td.ar{{font-size:7.4pt;color:{INK}}}
table.t3 td span.en{{display:block;font-family:'IBM Plex Sans',sans-serif;direction:ltr;text-align:left;
 font-size:6.2pt;color:{SLATE};margin-top:0.5mm;line-height:1.5}}
table.t3 td.n{{font-family:'IBM Plex Mono',monospace;color:{RED};font-weight:700;width:6mm;font-size:8pt}}
table.t3 td.num{{text-align:right;font-size:7pt;color:{INK}}}
table.t3 td.sw{{width:8mm;padding:1.6mm 1mm}}
table.t3 td.sw > i{{display:block;width:100%;height:3.4mm;border:0.2mm solid {SILVER}}}
table.t3.ct td{{padding:0.72mm 2mm}}
table.t3.ct td:first-child{{font-size:6pt;font-weight:700;letter-spacing:.08em;color:{INK}}}
table.t3.ct td.v{{width:22mm}}
table.t3.ct td.v > span{{font-size:5.6pt;font-weight:700;letter-spacing:.1em;padding:0.7mm 1.6mm;display:inline-block}}
table.t3.ct td.v > span.ink{{background:{INK};color:{PAPER}}}
table.t3.ct td.v > span.wht{{background:#FFF;color:{INK};border:0.2mm solid {SILVER}}}
table.t3.ct td.v > span.key{{background:{RED};color:#FFF}}
table.t3.ct tr.key td{{background:#FDF0EF}}
table.t3.rl2 td{{padding:2mm}}
table.t3.cfg td:first-child{{width:42mm}}
.lay3{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin-bottom:2.5mm}}
.ly{{background:#FFF;border:0.25mm solid {SILVER};padding:3mm;position:relative}}
.ly > i{{font-style:normal;font-family:'IBM Plex Mono',monospace;font-size:10pt;font-weight:700;color:{RED};
 display:block;line-height:1}}
.ly > b.ar{{font-size:10pt;display:block;margin-top:1.5mm;color:{INK}}}
.ly > span{{font-size:5.6pt;font-weight:700;letter-spacing:.14em;color:{SLATE};display:block;margin-bottom:1.5mm}}
.ly > p{{margin:0;font-size:6.4pt;line-height:1.6;color:{GRAPH}}}
.ly > p.ar{{font-size:7pt;color:{INK};margin-bottom:0.8mm}}
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
 font-size:6.6pt;color:#C9C5BC;margin-top:1mm}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin-bottom:2.5mm}}
.col{{display:flex;gap:2.5mm;background:#FFF;border:0.25mm solid {SILVER};padding:2.4mm}}
.cs{{width:11mm;min-width:11mm;border:0.2mm solid {SILVER}}}
.cx > b{{font-size:7pt;color:{INK};display:block;margin-bottom:1mm}}
.cx > ul{{list-style:none;margin:0;padding:0}}
.cx > ul li{{font-size:6pt;line-height:1.55;color:{GRAPH}}}
.cx > ul li b{{color:{INK}}}
ol.dn{{list-style:none;margin:0 0 2.5mm;padding:0;columns:2;column-gap:5mm}}
ol.dn li{{break-inside:avoid;display:grid;grid-template-columns:3.4mm 1fr;gap:0 2mm;padding:1.3mm 0;
 border-bottom:0.2mm solid {SILVER}}}
ol.dn li > i{{width:2.8mm;height:2.8mm;background:{RED};display:block;grid-row:1/3;margin-top:0.8mm}}
ol.dn li > span.ar{{font-size:6.8pt;color:{INK};line-height:1.5}}
ol.dn li > span.en{{font-size:5.6pt;color:{SLATE};line-height:1.4}}
.sign{{position:relative;background:{DEEP};color:{PAPER};padding:6mm;margin-top:3mm;text-align:center;overflow:hidden}}
.sign > p{{margin:0;position:relative;z-index:2}}
.sign > p.ar{{font-size:13pt;font-weight:700;text-align:center;font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl}}
.sign > p.en{{font-size:7pt;letter-spacing:.18em;font-weight:700;color:#B9B5D8;margin-top:2mm}}
footer{{position:absolute;left:14mm;right:14mm;bottom:9mm;display:flex;justify-content:space-between;
 align-items:center;font-size:6pt;letter-spacing:.14em;text-transform:uppercase;font-weight:700;
 color:{SLATE};border-top:0.25mm solid {SILVER};padding-top:2.5mm}}
footer .fm{{display:flex;align-items:center;gap:2mm}}
footer .fm > b{{color:{INK};letter-spacing:.1em}}
footer .fm > em{{font-family:'IBM Plex Sans Arabic',sans-serif;font-style:normal;direction:rtl;
 font-weight:400;letter-spacing:0;text-transform:none;font-size:7pt}}
'''
html=f'''<!doctype html><html lang="ar" dir="ltr"><head><meta charset="utf-8">
<title>Alex Foods - Book section 12 - Pack in Field</title>
<link rel="stylesheet" href="plex.css"><style>{CSS}</style></head><body>{''.join(H)}</body></html>'''
html=html.replace('@@TOTAL@@',str(PAGES[0]))
io.open(os.path.join(HERE,'field.html'),'w',encoding='utf-8').write(html)
print("pages:",PAGES[0],"| collisions:",len(COLL),"| keyline fields:",NKEY,"| ink wins:",NINK,"/",NFIELD)
