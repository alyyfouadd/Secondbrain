# -*- coding: utf-8 -*-
# Alex Foods — Brand & Social Kit.
# TSA's kit LAYOUT, rebuilt in the client's colours and bilingual.
# Shares colour.py, plex.css and fonts/ with gen.py. Nothing is duplicated.
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'colour.py')).read().split('# sanity')[0])

def mix(a,b,t):
    A,B=hx(a),hx(b); return hs(tuple(A[i]+(B[i]-A[i])*t for i in range(3)))

# ---------------------------------------------------------------
# The document layer. This is ALEX FOODS' kit, so Alex Foods' colours
# own the page — the mapping mirrors TSA's own system one-for-one.
#   TSA Precision Navy #0A0F1E ground  -> Alex Navy   #0A0378
#   TSA Surface Navy   #1A2340 panels  -> Alex Surface (derived below)
#   TSA Signal Red     #E8203A accent  -> System Red  #E1251D
#   TSA Cold White     #F0F2F5 type    -> Paper       #FAF8F3
# Every relationship below is computed, never eyeballed.
# ---------------------------------------------------------------
NAVY  = '#0A0378'                 # Alex Navy, the master's own value, sampled from the seal ring
GROUND= '#05004B'                 # the seal ring's DARK gradient stop, already recorded in the vault.
                                  # Alex Navy at full strength is too hot across six pages, and this is
                                  # a real sampled value rather than an invented tint. Paper reads
                                  # 17.86:1 on it and red 4.05:1 - TSA's own ground gives 17.02 and 4.27.
RED   = '#E1251D'                 # System Red. The seal's inner red collapses into it at dE 3.31
PAPER = '#FAF8F3'                 # Paper. Never pure white.
INK   = '#141414'                 # Client Ink
SURF  = mix(GROUND, PAPER, .12)   # #221E5F - dE 7.57 from ground (TSA's own lift is dE 8.71)
LINE  = mix(GROUND, PAPER, .26)   # hairlines and dividers
MUTE  = mix(GROUND, PAPER, .55)   # de-emphasised type on the ground

RANGES = [
 ('BeBo','بيبو','Powdered drink sachets','مساحيق المشروبات','#1BA34C','logo-bebo-transparent.png',
  'The mother decides. The characters already own the child.',
  [('Peach · خوخ','#E4762A'),('Mango · مانجو','#F2A00C'),('Apple · تفاح','#2C8C3B'),('Pineapple · أناناس','#C6D42E')]),
 ('AlRawy','الراوي','Juice and nectar pouches','عصائر ونكتار','#1B4F9C','logo-alrawy-transparent.png',
  'The only adult-facing range. Reassurance, never excitement.',
  [('Cocktail · كوكتيل','#D6006E'),('Apple · تفاح','#00A3E0'),('Guava · جوافة','#1BA34C'),('Mango · مانجو','#F07F13')]),
 ('2MAN','تومان','Ice pops, two live lines','مثلجات','#29ABE2','logo-2man-transparent.png',
  'Talks to the kid directly. They spend their own money.',
  [('Blue · أزرق','#29ABE2'),('Red · أحمر','#E1251D'),('Green · أخضر','#8DC63F'),('Orange · برتقالي','#F07F13')]),
 ('POLEKA','بوليكا','Jelly candy','حلوى جيلي','#EC008C','logo-poleka-transparent.png',
  'Built to be asked for by name, out loud, in a shop.',
  [('Apple · التفاح','#1BA34C'),('Mango · المانجو','#FFF200'),('Strawberry · الفراولة','#EC008C')]),
]

def best(h):
    """The client's own rule: Ink is the default on a flavour field, white is the exception."""
    w=ratio('#FFFFFF',h); k=ratio(INK,h)
    if w>=4.5 and w>=k: return ('#FFFFFF', w, False)
    if k>=4.5:          return (INK, k, False)
    return (INK if k>=w else '#FFFFFF', max(w,k), True)   # True = needs a keyline

H=[]; PAGES=[0]
def p(s): H.append(s)
def page(body, label='', cls=''):
    PAGES[0]+=1
    p(f'<section class="page {cls}">{body}'
      f'<footer><span class="fm"><i></i><b>ALEX FOODS</b><em>أليكس فودز</em></span>'
      f'<span class="fr">{label} · v1.0 · {PAGES[0]} / 6</span></footer></section>')

def eyebrow(ar,en): return f'<div class="eb"><span>{en}</span><i></i><b class="ar">{ar}</b></div>'
def corners(): return '<i class="c tl"></i><i class="c tr"></i><i class="c bl"></i><i class="c br"></i>'

# ================= PAGE 1 — IDENTITY =================
sw=''
for n,h,role_en,role_ar in [
  ('Alex Navy',NAVY,'Ground. The master value, sampled from the seal ring.','أساس الصفحة'),
  ('System Red',RED,'Accent. One key word. Never body copy.','لون مميز'),
  ('Paper',PAPER,'Type on dark, ground on light. Never pure white.','النص والخلفية الفاتحة'),
  ('Alex Surface',SURF,'Cards and panels only. Not a brand colour.','البطاقات فقط')]:
    tc = INK if n=='Paper' else PAPER
    sw+=f'''<div class="cs" style="background:{h};color:{tc}">
    <b>{n}</b><span class="ar">{role_ar}</span><span class="mono">{h}</span><p>{role_en}</p></div>'''

marks=''.join(f'<div class="mk"><img src="../logos-transparent/{f}"><span>{n}</span></div>'
              for n,ar,d,dar,c,f,who,fl in RANGES)

page(f'''{eyebrow('نظام العلامة والتواصل','BRAND &amp; SOCIAL KIT — ALEX FOODS')}
<div class="hero">{corners()}<div class="grid"></div>
 <img class="seal" src="../logos-transparent/logo-alex-lockup-transparent.png">
 <div class="hx"><h1 class="ar">أليكس فودز</h1><h2>ALEX FOODS</h2>
 <p class="ar sub">الشركة الإسكندرية لتعبئة وتغليف المواد الغذائية</p>
 <p class="sub">MASTER BRAND · FOUR RANGES · ALEXANDRIA, EGYPT</p></div></div>

{eyebrow('العلامات','THE RANGES — ARTWORK, NEVER RETYPED')}
<div class="marks">{marks}</div>

{eyebrow('نظام الألوان','COLOUR SYSTEM — THE DOCUMENT LAYER')}
<div class="cses">{sw}</div>
<p class="fn">Paper on the ground measures <b>{ratio(PAPER,GROUND):.2f}:1</b>. System Red on it measures <b>{ratio(RED,GROUND):.2f}:1</b>, which clears 3:1 for display and sits just under 4.5:1 for body — <b>red is a headline colour here, never body copy.</b> The eighteen range colours are governed separately in the Design System.</p>

{eyebrow('الخطوط','TYPOGRAPHY — ONE FAMILY, TWO WEIGHTS')}
<div class="typ">
 <div class="tspec"><p class="ar sp7">طعم أحلى</p><p class="sp7">ALEX FOODS</p>
 <p class="ar sp4">الأربعاء ٤٠٠ ريجولار</p><p class="sp4">Hamburgefonstiv 0123456789</p></div>
 <div class="tr">
  <div class="tf"><b>IBM Plex Sans Arabic</b><span>Display and Arabic text · 700 / 400</span></div>
  <div class="tf"><b>IBM Plex Sans</b><span>Latin set alone · 700 / 400</span></div>
  <div class="tf"><b>IBM Plex Mono</b><span>Codes and specifications · 400</span></div>
  <p class="tn"><b>Two weights in any one layout.</b> The packs are already loud. The type's job is order, not competition. Arabic carries 1.7 leading against Latin's 1.5, because the diacritics collide otherwise.</p>
 </div>
</div>

<div class="stmt">{corners()}<div class="grid"></div>
 <div class="sx"><p class="ar">طعم أحلى مع أليكس فودز</p>
 <p class="en">A BETTER TASTE WITH ALEX FOODS</p></div>
</div>
<p class="fn"><b>That line is the client's own</b>, already running in their market creative. It is recorded here, not invented here — slogans are Foundation deliverable 4 and this is not one. <b>Note where it sits:</b> the red panel carries display type only, because red gives body copy just {ratio(PAPER,RED):.2f}:1. This kit does not break its own rule on its own page.</p>''','IDENTITY')

# ================= PAGE 2 — ARCHITECTURE =================
pill=''
for i,(n,ar,d,dar,c,f,who,fl) in enumerate(RANGES):
    bar=''.join(f'<i style="background:{h}"></i>' for _,h in fl)
    pill+=f'''<div class="pil"><span class="no">0{i+1}</span>
    <b class="ar">{ar}</b><b>{n}</b><span class="rl ar">{dar}</span><span class="rl">{d}</span>
    <p>{who}</p><div class="bars">{bar}</div></div>'''

page(f'''{eyebrow('هيكل العلامة','BRAND ARCHITECTURE')}
<div class="two">
 <div class="card hd"><span class="eb2">BEFORE · قبل</span><b>FOUR BRANDS.<br>FOUR AUDIENCES.</b>
 <p>Four pages, four follower counts, each starting from zero. The company that makes all four stays invisible.</p></div>
 <div class="card hd red"><span class="eb2">NOW · الآن</span><b>ONE COMPANY.<br>FOUR RANGES.</b>
 <p>Confirmed 18 September 2026. Alex Foods is the master brand. One presence compounds, and the ranges rotate inside it.</p></div>
</div>

{eyebrow('النطاقات الأربعة','THE FOUR RANGES')}
<div class="pils">{pill}</div>

{eyebrow('القاعدة','THE RULE THAT GOVERNS EVERY LAYOUT')}
<div class="hero sm">{corners()}<div class="grid"></div>
 <div class="hx"><p class="ar big">لون النكهة يملك الخلفية. لون النطاق يملك الشعار.</p>
 <h3>The flavour colour owns the field.<br>The range colour owns the logo.<br><em>The master owns the seal, and takes neither.</em></h3></div></div>

{eyebrow('قواعد الاستخدام','USAGE RULES')}
<div class="rules">
 <div class="ru"><i></i>Arabic is written first. English is fitted to it, never translated into.</div>
 <div class="ru"><i></i>Red on one word per headline, at display size only.</div>
 <div class="ru"><i></i>Corner frame marks on every hero block.</div>
 <div class="ru"><i></i>Grid overlay stays under 5% opacity. Always subtle.</div>
 <div class="ru"><i></i>Two weights in any one layout. 400 and 700.</div>
 <div class="ru"><i></i>The seal is placed as supplied. Never reconstructed.</div>
</div>''','ARCHITECTURE')

# ================= PAGE 3 — SOCIAL KIT =================
sizes=[('Profile picture','320 × 320','صورة الحساب','IG, FB, TikTok — square, shown as a circle'),
 ('Feed post, square','1080 × 1080','منشور مربع','The default post'),
 ('Feed post, portrait','1080 × 1350','منشور طولي','Takes more feed space. Use for the ones that matter'),
 ('Story / Reel','1080 × 1920','ستوري وريلز','Full screen vertical'),
 ('Google Business photo','1200 × 900','صورة جوجل','Minimum. The listing is the company’s, not a range’s')]
srows=''.join(f'''<tr><td><b>{a}</b><span class="ar sm">{ar}</span></td><td class="mono">{b}</td><td class="sm">{c}</td></tr>'''
              for a,b,ar,c in sizes)

tpl=''
for bg,tag_ar,tag_en,kind,fg in [
 (NAVY,'طعم أحلى مع أليكس فودز','THE MASTER SPEAKS','MASTER · statement',PAPER),
 (RED,'جديد من أليكس فوودز','A LAUNCH OR AN OFFER','LAUNCH · offer',PAPER),
 ('#1BA34C','قوليلهم آه.','A PRODUCT POST','RANGE · product',None)]:
    kl=False
    if fg is None: fg,_,kl = best(bg)
    ks = f'text-shadow:0 0 0.9mm {INK};' if kl else ''
    tpl+=f'''<div class="tp" style="background:{bg};color:{fg}">{corners()}<div class="grid"></div>
    <div class="tph"><i style="background:{RED}"></i><span>ALEX FOODS</span></div>
    <div class="tpb" style="{ks}"><b class="ar">{tag_ar}</b><span class="tpe">{tag_en}</span></div>
    <span class="tpk">{kind}</span></div>'''

page(f'''{eyebrow('التواصل الاجتماعي','SOCIAL — ONE PRESENCE, FOUR RANGES')}
<h3 class="ar lead">حساب واحد. أربعة نطاقات.</h3>
<h4>ONE ACCOUNT. <em>FOUR RANGES.</em></h4>

{eyebrow('صورة الحساب','01 — PROFILE PICTURE')}
<div class="two">
 <div class="card ctr"><div class="pfp" style="background:{NAVY}"><img src="../logos-transparent/logo-alex-lockup-transparent.png"></div>
 <span class="cap">PRIMARY — ALEX NAVY · الأساسي</span><p>Default everywhere. Holds on a light feed and a dark one.</p></div>
 <div class="card ctr"><div class="pfp" style="background:{RED}"><img src="../logos-transparent/logo-alex-lockup-transparent.png"></div>
 <span class="cap">ALT — SYSTEM RED · للحملات</span><p>Campaigns and launches only, when the grid needs to break.</p></div>
</div>

{eyebrow('المقاسات','02 — EXACT SIZES (PIXELS)')}
<table class="mt"><thead><tr><th>Asset · الأصل</th><th>Pixels</th><th>Where</th></tr></thead><tbody>{srows}</tbody></table>

{eyebrow('قوالب المنشورات','03 — POST TEMPLATES')}
<div class="tpls">{tpl}</div>
<p class="fn">Three repeatable layouts. <b>Navy</b> is the master speaking. <b>Red</b> is a launch or an offer, and it is the only full-bleed red in the system. <b>A flavour field</b> is a product post, and its type colour is set by the contrast table, never by eye.</p>''','SOCIAL KIT')

# ================= PAGE 4 — RULES, MIX, RHYTHM =================
always=['Arabic is written first. English is fitted to it.',
 'One idea per post. Two ideas is two posts.',
 'The character leads the frame on POLEKA and BeBo.',
 'Ink #141414 is the default type colour on a flavour field.',
 'White type on a colour field carries a dark keyline.',
 'The BeBo banner keeps its navy keyline on any green.',
 'Every bio names Alex Foods.']
never=['No health claims. صحي · مفيد · يقوي المناعة · غني بالفيتامينات',
 'Never «طبيعي ١٠٠٪» or "100% juice". BeBo is a powder. AlRawy is a nectar.',
 'No nutrition numbers without the client’s written spec sheet.',
 'No price claims. «الأرخص» is unverifiable and starts an argument.',
 'No availability promises. Never name a shop that is not confirmed.',
 'Never POLEKA cola and strawberry in the same grid. ΔE 0.00.',
 'No company age claim. Their own materials say 20 and 25.']
al=''.join(f'<li><i>+</i>{x}</li>' for x in always)
nv=''.join(f'<li><i>–</i>{x}</li>' for x in never)

mix4=[('40','PRODUCT','المنتج','The packs, the ranges, the flavours. The product is the hero and there are eighteen SKUs to rotate.'),
 ('30','CHARACTER','الشخصيات','BeBo’s faces, POLEKA’s animals, 2MAN’s boy. The characters are the brands and they are already drawn.'),
 ('20','MOMENT','اللحظة','The lunchbox, the hot afternoon, the family jug. The occasion, never a health claim about it.'),
 ('10','COMPANY','الشركة','Alex Foods itself. The city, the people, the ranges together. No age claim until they confirm one.')]
mx=''.join(f'''<div class="stat"><span class="n">{a}<em>%</em></span><b>{b}</b><span class="ar">{ar}</span><p>{c}</p></div>'''
           for a,b,ar,c in mix4)

rhythm=[('Instagram — Reels + posts','5 / week','Main platform. Reels for reach, posts for the range grid.'),
 ('Instagram Stories','Daily','Keeps the account warm. Polls and questions do the engagement work.'),
 ('Facebook','4 / week','<b>Bigger here than it is for most brands.</b> BeBo and AlRawy talk to mothers, and in Egypt that audience is on Facebook.'),
 ('TikTok','3–4 / week','Repurpose the Reels. Free extra reach, no extra shoot.')]
rr=''.join(f'<tr><td><b>{a}</b></td><td class="mono rate">{b}</td><td class="sm">{c}</td></tr>' for a,b,c in rhythm)

page(f'''{eyebrow('افعل ولا تفعل','04 — ALWAYS &amp; NEVER')}
<div class="two">
 <div class="card lst"><b class="hh">ALWAYS <span class="ar">افعل</span></b><ul>{al}</ul></div>
 <div class="card lst nev"><b class="hh">NEVER <span class="ar">ممنوع</span></b><ul>{nv}</ul></div>
</div>
<p class="fn"><b>The NEVER column is not style, it is exposure.</b> A food page can be reported and a paid ad account restricted on a single sentence. TSA runs the ad account, so it is TSA’s risk as much as the client’s. Governing principle: <b>if it did not come from the client in writing, we do not know it.</b></p>

{eyebrow('ماذا ننشر','05 — WHAT TO POST')}
<div class="stats">{mx}</div>

{eyebrow('إيقاع النشر','06 — POSTING RHYTHM')}
<table class="mt"><thead><tr><th>Platform</th><th>Frequency</th><th>Why</th></tr></thead><tbody>{rr}</tbody></table>
<div class="chip">SPEC — EXECUTION PENDING CLIENT ACCESS · Meta admin and the Google account have not arrived</div>''','RULES &amp; RHYTHM')

# ================= PAGE 5 — FEED TEMPLATES =================
feed=''
for rn,ar,d,dar,c,f,who,fl in RANGES[:2]:
    lab,fld = fl[0]
    fg,cr,kl = best(fld)
    ks = f'text-shadow:0 0 1mm {INK};' if kl else ''
    cap = {'BeBo':('قوليلهم آه.','ظرف واحد يعمل إبريق كامل.'),
           'AlRawy':('نكتار الراوي.','فاكهة، مش كلام.')}[rn]
    feed+=f'''<div class="fd" style="background:{fld};color:{fg}">{corners()}
    <div class="tph"><i style="background:{RED}"></i><span>ALEX FOODS</span></div>
    <img class="pk" src="../logos-transparent/{f}">
    <div class="fdb" style="{ks}"><b class="ar">{cap[0]}</b><span class="ar">{cap[1]}</span>
    <span class="rg">{rn} · {lab}</span></div>
    <span class="ver">{fld} · type {"WHITE" if fg=="#FFFFFF" else "INK"} at {cr:.1f}:1{" · keyline" if kl else ""}</span></div>'''

page(f'''{eyebrow('قوالب المنشورات','FEED TEMPLATES — 1080 × 1350')}
<h3 class="ar lead">النكهة تملك الخلفية.</h3>
<h4>THE FLAVOUR OWNS THE <em>FIELD.</em></h4>
<p class="lead">The pack sits on its own flavour colour and the copy sits under it. The type colour is not a taste decision: it is read off the contrast table, and the verdict is printed on every frame below so anyone can check the layout against the system.</p>
<div class="feeds">{feed}</div>
<p class="fn">Both captions above are drafts from the Brand Voice Guide, written in Egyptian colloquial for Aly’s ear rather than translated out of English. <b>No em-dashes, no health claims, no price, no shop named.</b></p>

{eyebrow('ممنوع','NEVER — SHOWN, NOT DESCRIBED')}
<div class="dont">
 <div class="dc"><div class="dpair">
   <div style="background:#EC008C"><span>Cola</span></div><div style="background:#EC008C"><span>Strawberry</span></div>
  </div><b>Never in the same grid</b>
  <p>Both POLEKA fields are <span class="mono">#EC008C</span> at <b>&#916;E 0.00</b>. At thumbnail size they are one product. Separate them across the calendar, and let the character lead the frame.</p></div>
 <div class="dc"><div class="dpair">
   <div style="background:#2C8C3B"><span class="bdg">BeBo</span></div>
   <div style="background:#2C8C3B"><span class="bdg kl">BeBo</span></div>
  </div><b>The keyline is not decoration</b>
  <p>The banner on the apple field is <b>1.30:1</b>. Left is what happens without the navy keyline. <b>It is non-negotiable on any green, at any size.</b></p></div>
</div>''','FEED TEMPLATES')

# ================= PAGE 6 — STORIES + HOW TO USE =================
st=''
for rn,capar,fld in [('2MAN','برّه أحلى.','#29ABE2'),('POLEKA','مين معاك النهاردة؟','#EC008C'),('AlRawy','كل يوم.','#00A3E0')]:
    fg,cr,kl = best(fld)
    ks = f'text-shadow:0 0 1mm {INK};' if kl else ''
    logo = {'2MAN':'logo-2man-transparent.png','POLEKA':'logo-poleka-transparent.png','AlRawy':'logo-alrawy-transparent.png'}[rn]
    st+=f'''<div class="sty" style="background:{fld};color:{fg}">{corners()}
    <div class="tph"><i style="background:{RED}"></i><span>ALEX FOODS</span></div>
    <img class="pk" src="../logos-transparent/{logo}">
    <div class="styb" style="{ks}"><b class="ar">{capar}</b>
    <span class="cta" style="background:{RED};color:{PAPER}">اعرف أكتر</span></div>
    <span class="ver">{fld} · {cr:.1f}:1{" · keyline" if kl else ""}</span></div>'''

page(f'''{eyebrow('قوالب الستوري','STORIES &amp; REELS COVERS — 1080 × 1920')}
<div class="stys">{st}</div>

{eyebrow('كيف تستخدم هذا','HOW TO USE THIS')}
<div class="how"><b>The swap is simple · التبديل بسيط</b>
<p>In Canva or Figma: flavour field as the background layer, pack cut-out from <span class="mono">logos-transparent/</span> on top, red bar and ALEX FOODS at the corner, Arabic at the bottom in Plex Sans Arabic 700. <b>Arabic first, then fit the English.</b> That is the whole formula.</p></div>
<div class="how"><b>Check the type colour, do not guess it · تحقق من لون النص</b>
<p>Every field in this kit prints its own contrast verdict. If a field is not in the Design System’s eighteen, it is not in the system and the post is off-brand. <b>Bright Pink #EC008C is the trap</b> — white gives 4.2:1, ink gives 4.3:1, neither is comfortable, so that field always carries a keyline.</p></div>
<div class="how warn"><b>Two things this kit will not do for you</b>
<p><b>The master has no tone block yet.</b> The four ranges have register, sentence length and emoji policy written. Alex Foods itself does not, and it is the account that actually posts. <b>And product photography has not arrived</b> — every frame here uses pack artwork, which is not the same thing.</p></div>
<div class="sign">{corners()}<div class="grid"></div>
<p class="ar big">أليكس فودز</p><p class="mono">BRAND &amp; SOCIAL KIT · v1.0 · 18.09.2026</p>
<div class="by"><i></i><span>PREPARED BY THE STANDARD AGENCY · ALEXANDRIA</span></div></div>''','STORIES')

CSS=f'''
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:{GROUND};color:{PAPER};
 font-family:'IBM Plex Sans',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:14mm 14mm 20mm;position:relative;overflow:hidden;
 background:{GROUND};page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto}}
.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;line-height:1.7}}
.mono{{font-family:'IBM Plex Mono',monospace}}
b,strong{{font-weight:700}}
/* eyebrow + rule, TSA's section device */
.eb{{display:flex;align-items:center;gap:3mm;margin:5.5mm 0 2.6mm}}
.eb span{{font-size:6pt;font-weight:700;letter-spacing:.22em;color:{RED};text-transform:uppercase;white-space:nowrap}}
.eb i{{flex:1;height:0.25mm;background:{LINE}}}
.eb b.ar{{font-size:8pt;font-weight:400;color:{MUTE}}}
.page > .eb:first-child{{margin-top:0}}
/* corner frame marks */
.c{{position:absolute;width:4mm;height:4mm;border:0.5mm solid {RED};z-index:3}}
.c.tl{{top:2.5mm;left:2.5mm;border-right:0;border-bottom:0}}
.c.tr{{top:2.5mm;right:2.5mm;border-left:0;border-bottom:0}}
.c.bl{{bottom:2.5mm;left:2.5mm;border-right:0;border-top:0}}
.c.br{{bottom:2.5mm;right:2.5mm;border-left:0;border-top:0}}
.grid{{position:absolute;inset:0;z-index:1;opacity:.05;
 background-image:repeating-linear-gradient(0deg,{PAPER} 0 0.2mm,transparent 0.2mm 7mm),
 repeating-linear-gradient(90deg,{PAPER} 0 0.2mm,transparent 0.2mm 7mm)}}
/* hero */
.hero{{position:relative;background:{SURF};padding:9mm 10mm;overflow:hidden;min-height:50mm;
 display:flex;align-items:center;gap:8mm}}
.hero.sm{{min-height:0;padding:8mm 10mm}}
.hero .hx{{position:relative;z-index:2;flex:1}}
.hero .seal{{position:relative;z-index:2;width:32mm;height:auto}}
.hero h1{{font-size:26pt;font-weight:700;margin:0;line-height:1.35}}
.hero h2{{font-size:17pt;font-weight:700;margin:1mm 0 0;letter-spacing:.14em}}
.hero h3{{font-size:13pt;font-weight:700;margin:2.5mm 0 0;line-height:1.35}}
.hero h3 em{{font-style:normal;color:{RED}}}
.sub{{font-size:7.5pt;color:{MUTE};margin:2.5mm 0 0;letter-spacing:.05em}}
p.ar.big{{font-size:14pt;font-weight:700;margin:0;color:{PAPER}}}
/* range marks */
.marks{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.mk{{background:{SURF};border:0.25mm solid {LINE};padding:3mm;text-align:center;height:24mm;
 display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2mm}}
.mk img{{max-width:100%;max-height:14mm;object-fit:contain}}
.mk span{{font-size:6pt;font-weight:700;letter-spacing:.18em;color:{MUTE}}}
/* colour cards */
.cses{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.cs{{padding:3.6mm;min-height:26mm;display:flex;flex-direction:column;border:0.25mm solid {LINE}}}
.cs > b{{font-size:9pt}} .cs .ar{{font-size:7.5pt;opacity:.8;margin-bottom:1mm}}
.cs .mono{{font-size:7.5pt;margin-bottom:2mm}}
.cs p{{font-size:6.5pt;line-height:1.45;margin:auto 0 0;opacity:.85}}
/* generic */
h3.ar.lead{{font-size:19pt;font-weight:700;margin:0}}
h4{{font-size:16pt;font-weight:700;margin:1mm 0 3mm;letter-spacing:.06em}}
h4 em{{font-style:normal;color:{RED}}}
p.lead{{font-size:8.5pt;line-height:1.6;color:{PAPER};opacity:.92;margin:0 0 2mm;max-width:150mm}}
p.fn{{font-size:6.8pt;line-height:1.55;color:{MUTE};margin:3mm 0 0}}
p.fn b{{color:{PAPER}}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}}
.card{{background:{SURF};border:0.25mm solid {LINE};padding:5mm}}
.card.hd{{border-top:0.7mm solid {LINE}}}
.card.hd.red{{border-top-color:{RED}}}
.eb2{{font-size:5.5pt;font-weight:700;letter-spacing:.2em;color:{RED};display:block;margin-bottom:2mm}}
.card.hd > b{{font-size:13pt;line-height:1.2;display:block}}
.card p{{font-size:7.5pt;line-height:1.55;margin:2.5mm 0 0;opacity:.88}}
.card.ctr{{text-align:center}}
.pfp{{width:26mm;height:26mm;border-radius:50%;margin:1mm auto 3mm;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.pfp img{{width:19mm;height:auto}}
.cap{{font-size:6pt;font-weight:700;letter-spacing:.16em;color:{RED};display:block}}
/* pillars */
.pils{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.pil{{background:{SURF};border:0.25mm solid {LINE};padding:4mm;position:relative;display:flex;flex-direction:column}}
.pil .no{{font-size:17pt;font-weight:700;color:{MUTE};opacity:.45;line-height:1}}
.pil b.ar{{font-size:11pt;display:block;margin-top:1mm}}
.pil > b{{font-size:11pt;display:block;letter-spacing:.04em}}
.rl{{font-size:6.2pt;color:{MUTE};display:block;line-height:1.5}}
.rl.ar{{font-size:7pt}}
.pil p{{font-size:6.8pt;line-height:1.5;margin:2mm 0 2.5mm;opacity:.9}}
.bars{{display:flex;gap:0.8mm;margin-top:auto}}
.bars i{{flex:1;height:2.2mm}}
/* usage rules */
.rules{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm}}
.ru{{background:{SURF};border:0.25mm solid {LINE};padding:3mm 4mm;font-size:7.2pt;display:flex;align-items:center;gap:2.5mm}}
.ru i{{width:1.4mm;height:1.4mm;background:{RED};border-radius:50%;flex:none}}
/* tables */
table.mt{{width:100%;border-collapse:collapse;margin:1mm 0}}
table.mt th{{font-size:5.8pt;text-transform:uppercase;letter-spacing:.2em;color:{RED};text-align:left;
 font-weight:700;padding:2mm 2mm;background:{SURF}}}
table.mt td{{padding:2mm;border-bottom:0.2mm solid {LINE};font-size:7.5pt;vertical-align:middle}}
table.mt td b{{font-size:8pt}}
table.mt td .ar.sm{{font-size:7pt;color:{MUTE};display:block}}
td.mono{{font-size:8pt;font-weight:700}} td.rate{{font-size:9pt;font-weight:700}}
.sm{{font-size:7pt;opacity:.85}}
/* post templates */
.tpls{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}
.tp{{position:relative;height:64mm;padding:4mm;display:flex;flex-direction:column;overflow:hidden}}
.tph{{position:relative;z-index:2;display:flex;align-items:center;gap:1.5mm}}
.tph i{{width:0.9mm;height:3.2mm;display:block}}
.tph span{{font-size:5.8pt;font-weight:700;letter-spacing:.14em}}
.tpb{{position:relative;z-index:2;margin-top:auto}}
.tpb b.ar{{font-size:11.5pt;display:block;line-height:1.4}}
.tpe{{font-size:5.8pt;font-weight:700;letter-spacing:.16em;display:block;margin-top:1.5mm;opacity:.85}}
.tpk{{position:relative;z-index:2;font-size:5.5pt;font-weight:700;letter-spacing:.14em;
 margin-top:2mm;opacity:.75}}
/* always / never */
.card.lst{{padding:0}} .card.lst > .hh{{display:block;font-size:11pt;padding:3.5mm 5mm;background:{PAPER};color:{GROUND};letter-spacing:.06em}}
.card.lst.nev .hh{{background:{RED};color:{PAPER}}}
.card.lst .hh .ar{{font-size:9pt;font-weight:400;float:right}}
.card.lst ul{{margin:0;padding:3mm 5mm 4mm;list-style:none}}
.card.lst li{{font-size:7pt;line-height:1.5;padding:1.8mm 0;border-bottom:0.2mm solid {LINE};
 display:flex;gap:2.5mm;align-items:baseline}}
.card.lst li:last-child{{border:0}}
.card.lst li i{{font-style:normal;font-weight:700;color:{RED};flex:none;width:2.5mm}}
/* stats */
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.stat{{background:{SURF};border:0.25mm solid {LINE};padding:4mm}}
.stat .n{{font-size:24pt;font-weight:700;line-height:1;display:block}}
.stat .n em{{font-style:normal;color:{RED};font-size:15pt}}
.stat > b{{font-size:8.5pt;display:block;margin-top:1.5mm;letter-spacing:.08em}}
.stat .ar{{font-size:8pt;color:{MUTE};display:block}}
.stat p{{font-size:6.5pt;line-height:1.5;margin:2mm 0 0;opacity:.88}}
.chip{{display:inline-block;background:{RED};color:{PAPER};font-size:6pt;letter-spacing:.1em;
 padding:2mm 3.5mm;font-family:'IBM Plex Mono',monospace;margin-top:4mm;font-weight:700}}
/* feed + story frames */
.feeds{{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:2mm}}
.fd{{position:relative;height:96mm;padding:5mm;display:flex;flex-direction:column;overflow:hidden}}
.fd .pk{{position:absolute;z-index:1;right:4mm;top:12mm;max-width:52%;max-height:44mm;object-fit:contain}}
.fdb{{position:relative;z-index:2;margin-top:auto}}
.fdb b.ar{{font-size:17pt;display:block;line-height:1.35}}
.fdb span.ar{{font-size:9pt;display:block;opacity:.9}}
.rg{{font-size:5.8pt;font-weight:700;letter-spacing:.16em;display:block;margin-top:2.5mm;opacity:.8}}
.ver{{position:absolute;z-index:2;bottom:1.6mm;left:4.5mm;right:4.5mm;font-family:'IBM Plex Mono',monospace;
 font-size:5pt;opacity:.62;letter-spacing:.04em}}
.stys{{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm}}
.sty{{position:relative;height:84mm;padding:4.5mm;display:flex;flex-direction:column;overflow:hidden}}
.sty .pk{{position:absolute;z-index:1;left:50%;transform:translateX(-50%);top:14mm;max-width:66%;max-height:34mm;object-fit:contain}}
.styb{{position:relative;z-index:2;margin-top:auto}}
.styb b.ar{{font-size:13pt;display:block;line-height:1.4;margin-bottom:3mm}}
.cta{{font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;display:inline-block;
 font-size:7.5pt;font-weight:700;padding:1.8mm 4mm}}
/* typography specimen */
.typ{{display:grid;grid-template-columns:1.15fr 1fr;gap:4mm}}
.tspec{{background:{SURF};border:0.25mm solid {LINE};padding:4mm}}
.sp7{{font-size:17pt;font-weight:700;margin:0 0 1mm;line-height:1.35}}
.sp4{{font-size:9pt;font-weight:400;margin:0 0 1mm;color:{MUTE};line-height:1.5}}
.tr{{display:flex;flex-direction:column;gap:2mm}}
.tf{{background:{SURF};border:0.25mm solid {LINE};padding:2.6mm 4mm}}
.tf b{{font-size:8.5pt;display:block}}
.tf span{{font-size:6.3pt;color:{MUTE};letter-spacing:.06em}}
.tn{{font-size:6.6pt;line-height:1.55;margin:auto 0 0;opacity:.88}}
/* master statement */
.stmt{{position:relative;background:{RED};color:{PAPER};padding:4.5mm 7mm;margin-top:2.5mm;overflow:hidden}}
.stmt .sx{{position:relative;z-index:2}}
.stmt .ar{{font-size:16pt;font-weight:700;margin:0}}
.stmt .en{{font-size:8pt;font-weight:700;letter-spacing:.2em;margin:1.2mm 0 0}}
/* do-not pairs */
.dont{{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}}
.dc{{background:{SURF};border:0.25mm solid {LINE};padding:4mm}}
.dc > b{{font-size:8.5pt;display:block;margin:2.5mm 0 1mm}}
.dc p{{font-size:6.6pt;line-height:1.5;margin:0;opacity:.9}}
.dpair{{display:grid;grid-template-columns:1fr 1fr;gap:2mm}}
.dpair > div{{height:19mm;display:flex;align-items:center;justify-content:center;
 font-size:7pt;font-weight:700;color:{INK}}}
.bdg{{background:#1BA34C;color:{PAPER};padding:1.4mm 3.5mm;font-size:7.5pt}}
.bdg.kl{{border:0.7mm solid #1E2A6B}}
/* how to use */
.how{{background:{SURF};border-left:0.8mm solid {RED};padding:4mm 5mm;margin-bottom:2.5mm}}
.how.warn{{border-left-color:{PAPER}}}
.how > b{{font-size:9pt;display:block;margin-bottom:1.5mm}}
.how p{{font-size:7.2pt;line-height:1.55;margin:0;opacity:.9}}
.sign{{position:relative;background:{SURF};padding:8mm;margin-top:3mm;overflow:hidden;text-align:center}}
.sign p.ar.big{{font-size:17pt;position:relative;z-index:2}}
.sign p.mono{{font-size:7pt;color:{MUTE};margin:1mm 0 4mm;position:relative;z-index:2}}
.by{{position:relative;z-index:2;display:inline-flex;align-items:center;gap:2.5mm}}
.by i{{width:1mm;height:3.4mm;background:{RED};display:block}}
.by span{{font-size:6pt;font-weight:700;letter-spacing:.16em;color:{MUTE}}}
/* footer */
footer{{position:absolute;left:14mm;right:14mm;bottom:9mm;display:flex;justify-content:space-between;
 align-items:center;font-size:6pt;letter-spacing:.14em;text-transform:uppercase;font-weight:700;
 color:{MUTE};border-top:0.25mm solid {LINE};padding-top:2.5mm}}
footer .fm{{display:flex;align-items:center;gap:2mm}}
footer .fm i{{width:1mm;height:3.2mm;background:{RED};display:block}}
footer .fm b{{color:{PAPER};letter-spacing:.1em}}
footer .fm em{{font-family:'IBM Plex Sans Arabic',sans-serif;font-style:normal;
 direction:rtl;font-weight:400;letter-spacing:0;text-transform:none;font-size:7pt}}
'''
html=f'''<!doctype html><html lang="ar" dir="ltr"><head><meta charset="utf-8">
<title>Alex Foods — Brand &amp; Social Kit v1.0</title>
<link rel="stylesheet" href="plex.css"><style>{CSS}</style></head><body>{''.join(H)}</body></html>'''
io.open(os.path.join(HERE,'kit.html'),'w',encoding='utf-8').write(html)
print("Alex Surface:",SURF,"| Line:",LINE,"| Mute:",MUTE)
print("pages:",PAGES[0])
