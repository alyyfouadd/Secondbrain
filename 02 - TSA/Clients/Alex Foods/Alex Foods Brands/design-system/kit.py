# -*- coding: utf-8 -*-
# Alex Foods — Brand & Social Kit.
# TSA's kit layout AND its information architecture, section for section,
# rebuilt for Alex Foods on the client's own light neutrals.
# Shares colour.py, plex.css and fonts/ with gen.py. Nothing is duplicated.
import io, os
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'colour.py')).read().split('# sanity')[0])

# ---------------------------------------------------------------
# The document layer. Paper ground, per the client's own neutrals in
# Colour System §7 — and it is what TSA Brand System §6 wants for a
# client deliverable. Every relationship below is computed.
#   Ink on Paper 17.36:1 · Graphite 8.71:1 · Red 4.41:1 (display only)
# ---------------------------------------------------------------
PAPER  = '#FAF8F3'   # ground. Never pure white.
INK    = '#141414'   # primary type
GRAPH  = '#4A4742'   # secondary type
SLATE  = '#8A8681'   # captions at display size only. Never body.
SILVER = '#C9C5BC'   # rules and dividers. Never type.
MIST   = '#EDEAE3'   # panel and card fills. Never type.
RED    = '#E1251D'   # System Red. Accent. One key word. Never body copy.
NAVY   = '#0A0378'   # Alex Navy, the master's own value, sampled from the seal ring
DEEP   = '#05004B'   # the seal ring's dark gradient stop. Hero panels only.

RANGES = [
 dict(key='bebo', en='BeBo', ar='بيبو', sig='#1BA34C', logo='logo-bebo-transparent.png',
  packs=['bebo.png'],
  fmt_en='Powder sachets. One makes a jug.', fmt_ar='ظرف بودرة. الواحد يعمل إبريق.',
  who='The mother. The characters on the pack already own the child, so the copy talks to whoever is deciding.',
  idy='The face <b>is</b> the pack, and it takes the colour of its own flavour. KIDS ZONE sub-mark, red NEW flash, green banner with the navy keyline that never comes off.',
  fl=[('Peach · خوخ','#E4762A'),('Mango · مانجو','#F2A00C'),('Apple · تفاح','#2C8C3B'),('Cola · كولا','#1C74BC'),('Pineapple · أناناس','#C6D42E')]),
 dict(key='alrawy', en='AlRawy', ar='الراوي', sig='#1B4F9C', logo='logo-alrawy-transparent.png',
  packs=['alrawy.png'],
  fmt_en='Ready to drink. Straw on the pack.', fmt_ar='جاهز للشرب. بماصة على العبوة.',
  who='The buyer, and the only adult-facing range of the four. Reassurance rather than excitement.',
  idy='Real fruit photography, not illustration, and the most grown-up mark of the four. Carries the Alex seal and a registered ®. <b>It is a nectar and the pack says so</b>, so copy never calls it juice.',
  fl=[('Cocktail · كوكتيل','#D6006E'),('Apple · تفاح','#00A3E0'),('Guava · جوافة','#1BA34C'),('Peach · خوخ','#E1251D'),('Mango · مانجو','#F07F13')]),
 dict(key='2man', en='2MAN', ar='تومان', sig='#29ABE2', logo='logo-2man-transparent.png',
  packs=['2man-icepops.png','2man-buzz.png'],
  fmt_en='Ice pops. Two live pack lines.', fmt_ar='مثلجات. خطان في السوق.',
  who='The kid, directly. They are spending their own pocket money, so nobody has to be talked through a parent.',
  idy='Illustrated 3D lettering that <b>cannot be retyped</b>, and a running boy who carries the whole brand. The tagline عيش جو المغامرة is already written and it stays. <b>ICE POPS and Bu:Zz share one voice</b> and differ only in artwork.',
  fl=[('Blue · أزرق','#29ABE2'),('Red · أحمر','#E1251D'),('Green · أخضر','#8DC63F'),('Orange · برتقالي','#F07F13')]),
 dict(key='poleka', en='POLEKA', ar='بوليكا', sig='#EC008C', logo='logo-poleka-transparent.png',
  packs=['poleka.png'],
  fmt_en='Jelly candy in bottle pouches.', fmt_ar='حلوى جيلي في عبوات على شكل زجاجة.',
  who='The child, deliberately. The brand\u2019s whole job is being asked for by name, out loud, in a shop.',
  idy='A full-bleed animal per SKU, so <b>the character leads every frame</b> and a post without one is off-brand. Gel lettering, also artwork. <b>Cola and strawberry share one pink</b> at ΔE 0.00.',
  fl=[('Apple · التفاح','#1BA34C'),('Mango · المانجو','#FFF200'),('Cola · كولا','#EC008C'),('Strawberry · الفراولة','#EC008C')]),
]

def best(h):
    """The client's own rule: Ink is the default on a flavour field, white is the exception."""
    w=ratio('#FFFFFF',h); k=ratio(INK,h)
    if w>=4.5 and w>=k: return ('#FFFFFF', w, False)
    if k>=4.5:          return (INK, k, False)
    return (INK if k>=w else '#FFFFFF', max(w,k), True)

H=[]; PAGES=[0]
def p(s): H.append(s)
def page(body, label=''):
    PAGES[0]+=1
    p(f'<section class="page">{body}'
      f'<footer><span class="fm"><b>ALEX FOODS</b><em>أليكس فودز</em></span>'
      f'<span class="fr">{label} · v1.2 — PAGE {PAGES[0]} / @@TOTAL@@</span></footer></section>')

def eyebrow(ar,en): return f'<div class="eb"><span>{en}</span><i></i><b class="ar">{ar}</b></div>'
def corners(): return '<i class="cnr tl"></i><i class="cnr tr"></i><i class="cnr bl"></i><i class="cnr br"></i>'

# ============ PAGE 1 — IDENTITY ============
lock = f'''
<div class="lk" style="background:{DEEP};color:{PAPER}"><img src="../logos-vector/alex-seal-flat.svg"><span>ON NAVY — DEFAULT</span></div>
<div class="lk" style="background:{PAPER};color:{INK};border-top:0.4mm solid {INK}"><img src="../logos-vector/alex-seal-flat.svg"><span>ON PAPER — DOCUMENTS</span></div>
<div class="lk wide" style="background:transparent;color:{INK}">
  <div class="minis">{''.join(f'<img src="../logos-transparent/{r["logo"]}">' for r in RANGES)}</div>
  <span>THE FOUR RANGES</span></div>'''

sysc=''
for n,h,ar,role in [('Alex Navy',NAVY,'كحلي أليكس','MASTER MARK &amp; PROFILE'),
                    ('System Red',RED,'أحمر النظام','ACCENT — NEVER BODY COPY'),
                    ('Paper',PAPER,'ورقي','EVERY BACKGROUND'),
                    ('Ink',INK,'حبري','TYPE EVERYWHERE')]:
    sysc+=f'''<div class="csw"><div class="chip" style="background:{h};{'outline:0.25mm solid '+SILVER if n=='Paper' else ''}"></div>
    <b>{n}</b><span class="ar">{ar}</span><span class="mono">{h}</span><span class="role">{role}</span></div>'''

rngc=''.join(f'''<div class="rsw"><i style="background:{r['sig']}"></i><b>{r['en']}</b>
 <span class="ar">{r['ar']}</span><span class="mono">{r['sig']}</span></div>''' for r in RANGES)

page(f'''{eyebrow('نظام الهوية — الإصدار الأول','BRAND IDENTITY SYSTEM V1 — ALEX FOODS')}
<div class="hero">{corners()}<div class="grid"></div>
 <img class="seal" src="../logos-vector/alex-seal-flat.svg">
 <div class="hx"><h1 class="ar">أليكس فودز</h1><h2>ALEX FOODS</h2>
 <p class="ar sub">الشركة الإسكندرية لتعبئة وتغليف المواد الغذائية</p>
 <p class="sub">MASTER BRAND &nbsp;·&nbsp; FOUR RANGES &nbsp;·&nbsp; ALEXANDRIA, EGYPT</p></div></div>
<div class="locks">{lock}</div>

{eyebrow('نظام الألوان','COLOUR SYSTEM')}
<div class="csws">{sysc}</div>
<div class="rsws"><span class="rlab">RANGE SIGNATURES</span>{rngc}</div>

{eyebrow('الخطوط','TYPOGRAPHY')}
<div class="typ"><div class="tyl">
 <p class="ar d1">أربع نطاقات.</p><p class="ar d1">شركة واحدة.</p><p class="ar d1 red">طعم أحلى.</p>
 <div class="tspec"><span>DISPLAY — IBM PLEX SANS ARABIC 700</span><span>BODY — IBM PLEX SANS REGULAR 400</span></div>
 <p>One bilingual superfamily, not a Latin face with Arabic bolted on. The packs already carry every bit of energy this brand needs, so the type's job is order. <b>Two weights in any one layout.</b></p>
</div><div class="tyr">
 <div class="tf"><b>IBM Plex Sans Arabic</b><span>Arabic and Latin · 700 / 400</span></div>
 <div class="tf"><b>IBM Plex Sans</b><span>Latin set alone · 700 / 400</span></div>
 <div class="tf"><b>IBM Plex Mono</b><span>Codes and sizes · 400</span></div>
 <div class="tf note"><b>Arabic leads. Always.</b><span>Written first, English fitted to it. 1.7 leading against Latin's 1.5, or the diacritics collide.</span></div>
</div></div>

{eyebrow('السطر','THE LINE ALREADY IN MARKET')}
<div class="promise">{corners()}<div class="grid"></div>
 <div class="px"><p class="ar">طعم أحلى مع أليكس فودز</p><p class="en">A BETTER TASTE WITH ALEX FOODS</p></div>
</div>
<p class="fn"><b>This is the client's own line</b>, already running across their market creative, recorded here so nobody invents a second one by accident. <b>A real brand line is Foundation deliverable 4</b> and this is not it. &nbsp;·&nbsp; <b>One Alex Foods mark, and only one:</b> no secondary lockup, no wordmark version, no alternate colourway. The ground changes underneath it, the mark does not. <b>Placed as supplied, never rebuilt, never set in a font.</b></p>''','BRAND IDENTITY')

# ============ PAGE 2 — POSITIONING ============
pill=''
for i,(no,en,ar,body) in enumerate([
 ('01','RANGE','النطاق','Four ranges, eighteen SKUs, one company. Each range keeps its own colours and its own audience, and none of them pretends to be the others.'),
 ('02','CHARACTER','الشخصية','BeBo’s faces, POLEKA’s animals, 2MAN’s boy. Every range already leads with a character, and they are drawn and paid for. The cheapest content this business owns.'),
 ('03','ALEXANDRIA','الإسكندرية','The mark carries the Pharos lighthouse and the company name is the city. Alex Foods is a place as much as a company, and that is a story no competitor can copy.')]):
    pill+=f'''<div class="pil"><span class="no">{no}</span><b>{en}</b><span class="par ar">{ar}</span><p>{body}</p></div>'''

page(f'''{eyebrow('ما الذي يميز أليكس فودز','WHAT MAKES ALEX FOODS DIFFERENT')}
<div class="two">
 <div class="vs"><span class="vl">FOUR SEPARATE BRANDS</span><b>FOUR AUDIENCES.<br>NONE COMPOUND.</b>
 <p>Four pages, four follower counts, four content calendars, each starting from zero. The company that actually makes all four stays invisible, and every range pays the cost of being unknown twice.</p></div>
 <div class="vs win"><span class="vl">ALEX FOODS</span><b>ONE COMPANY.<br>FOUR RANGES.</b>
 <p>Confirmed 18 September 2026. One presence carries all four, the ranges rotate inside it, and every post builds the same audience. A new SKU launches to people who already know the name.</p></div>
</div>

{eyebrow('ركائز العلامة','BRAND PILLARS')}
<div class="pils">{pill}</div>

{eyebrow('القاعدة','THE RULE THAT GOVERNS EVERY LAYOUT')}
<div class="hero rule">{corners()}<div class="grid"></div>
 <div class="hx"><p class="ar rl">لون النكهة يملك الخلفية.<br>لون النطاق يملك الشعار.</p>
 <h3>The flavour colour owns the field.<br>The range colour owns the logo.<br><em>The master owns the seal, and takes neither.</em></h3>
 <p class="sub">A BeBo mango pack is a mango field carrying the standard green banner. The banner does not turn orange to match the flavour, and it does not turn navy to match Alex.</p></div></div>

{eyebrow('قواعد الاستخدام','USAGE RULES')}
<div class="rules">
 <div class="ru"><i></i><b>Arabic is written first.</b> English is fitted to it, never translated into.</div>
 <div class="ru"><i></i><b>Red on one word per headline.</b> Display size only. Never a paragraph.</div>
 <div class="ru"><i></i><b>The character leads the frame</b> on POLEKA and BeBo. Always.</div>
 <div class="ru"><i></i><b>Two weights in one layout.</b> 700 and 400. A third looks accidental.</div>
 <div class="ru"><i></i><b>Corner frame marks on every hero block.</b> Grid overlay under 5%.</div>
 <div class="ru"><i></i><b>The seal is placed as supplied.</b> Never redrawn, never retyped.</div>
</div>''','POSITIONING')

# ============ PAGES 3-4 — THE RANGES ============
def rangeblock(r):
    pal = f'<div class="pchip sig" style="background:{r["sig"]}"><b>SIGNATURE</b><span class="mono">{r["sig"]}</span></div>'
    for lab,h in r['fl']:
        fg,cr,kl = best(h)
        pal += (f'<div class="pchip" style="background:{h};color:{fg}">'
                f'<b>{lab}</b><span class="mono">{h}</span></div>')
    packs = ''.join(f'<img src="../packshots/{f}">' for f in r['packs'])
    return f'''<div class="rng" style="border-top-color:{r["sig"]}">
 <div class="rtop">
  <div class="rlogo"><img src="../logos-transparent/{r["logo"]}"></div>
  <div class="rid"><b class="ar">{r["ar"]}</b><b class="ren">{r["en"]}</b>
   <span class="rfmt ar">{r["fmt_ar"]}</span><span class="rfmt">{r["fmt_en"]}</span></div>
  <div class="rwho"><span class="cap">TALKS TO</span><p>{r["who"]}</p></div>
 </div>
 <div class="rpacks c{len(r["packs"])}">{packs}</div>
 <div class="rpal">{pal}</div>
 <p class="ridy"><b>Identity.</b> {r["idy"]}</p></div>'''

page(f'''{eyebrow('النطاقات','THE RANGES — 1 &amp; 2 OF 4')}
<p class="lead">Four ranges, one company. <b>Each keeps its own colours, its own format and its own audience</b> — that separation is the asset, and the master never repaints it.</p>
{rangeblock(RANGES[0])}
{rangeblock(RANGES[1])}''','THE RANGES')

page(f'''{eyebrow('النطاقات','THE RANGES — 3 &amp; 4 OF 4')}
{rangeblock(RANGES[2])}
{rangeblock(RANGES[3])}
<p class="fn"><b>2MAN runs two pack architectures and both are live.</b> ICE POPS and Bu:Zz / Meyveli are one brand with one voice and two sets of artwork. A caption should never need to know which line it is for. <b>The POLEKA cola SKU stays out of paid campaigns and out of copy</b> until the client confirms the artwork rights in writing.</p>''','THE RANGES')

# ============ PAGE 3 — SOCIAL KIT ============
sizes=[('Profile picture','320 × 320','صورة الحساب','IG, FB, TikTok. Square, shown as a circle'),
 ('Feed post, square','1080 × 1080','منشور مربع','The default post'),
 ('Feed post, portrait','1080 × 1350','منشور طولي','More feed space. Use it for the ones that matter'),
 ('Story / Reel','1080 × 1920','ستوري وريلز','Full screen vertical'),
 ('Facebook cover','820 × 312','غلاف فيسبوك','Safe zone sits in the centre'),
 ('Google Business photo','1200 × 900','صورة جوجل','Minimum. The listing is the company’s, never a range’s')]
srows=''.join(f'''<tr><td><b>{a}</b><span class="ar sm">{ar}</span></td><td class="mono">{b}</td><td class="sm">{c}</td></tr>'''
              for a,b,ar,c in sizes)

tpl=''
for bg,cap_ar,kind,note,fg in [
 (DEEP,'طعم أحلى مع أليكس فودز','NAVY — THE MASTER SPEAKS','Brand, company, the ranges together.',PAPER),
 (RED,'جديد من أليكس فوودز','RED — A LAUNCH OR AN OFFER','The only full-bleed red in the system.',PAPER),
 ('#2C8C3B','قوليلهم آه.','FIELD — A PRODUCT POST','Flavour colour, the pack leads.',None)]:
    kl=False
    if fg is None: fg,_,kl = best(bg)
    ks = f'text-shadow:0 0 0.9mm {INK};' if kl else ''
    tpl+=f'''<div class="tpw"><div class="tp" style="background:{bg};color:{fg}">{corners()}<div class="grid"></div>
    <div class="tph"><img src="../logos-vector/alex-seal-flat.svg"></div>
    {'<img class="tpk2" src="../packshots/single/bebo-3.png">' if kind.startswith('FIELD') else ''}
    <div class="tpb" style="{ks}"><b class="ar">{cap_ar}</b></div></div>
    <span class="tpk">{kind}</span><span class="tpn">{note}</span></div>'''

page(f'''{eyebrow('التواصل الاجتماعي','THE STANDARD AGENCY — SOCIAL MEDIA KIT')}
<h3 class="ar big">حساب واحد. أربعة نطاقات.</h3>
<h4>ONE ACCOUNT. <em>FOUR RANGES.</em></h4>
<p class="lead">Everything needed to set up and run the Alex Foods presence. No designer required.</p>

{eyebrow('صورة الحساب','01 — PROFILE PICTURE')}
<div class="two">
 <div class="card ctr"><div class="pfp" style="background:{NAVY}"><img src="../logos-vector/alex-seal-flat.svg"></div>
 <span class="cap">THE ONLY PROFILE PICTURE</span><p>The seal on Alex Navy, centred, exported at 320 × 320. <b>There is no alternate.</b> It holds on a light feed and a dark one, which is the whole reason it needs no second version.</p></div>
 <div class="card"><span class="cap">CLEAR SPACE &amp; MINIMUMS</span>
 <div class="clr"><div class="clrbox"><img src="../logos-vector/alex-seal-flat.svg"></div>
 <div><p><b>Clear space:</b> a margin equal to one quarter of the seal's height on all four sides. Nothing enters it — no text, no image edge, no second mark.</p>
 <p><b>Minimum size:</b> 12 mm in print, 56 px on screen. Below that the ring text closes up and the lighthouse disappears.</p></div></div></div>
</div>

{eyebrow('المقاسات','02 — EXACT SIZES (PIXELS)')}
<table class="mt"><thead><tr><th>Asset</th><th>Dimensions</th><th>Where</th></tr></thead><tbody>{srows}</tbody></table>

{eyebrow('قوالب المنشورات','03 — POST TEMPLATES')}
<div class="tpls">{tpl}</div>
<p class="fn">Three repeatable layouts. <b>Navy</b> is the company speaking · <b>Red</b> is a launch or an offer · <b>a flavour field</b> is a product post. On a flavour field the type colour is read off the contrast table, never picked by eye.</p>''','SOCIAL KIT')

# ============ PAGE 4 — RULES, MIX, RHYTHM ============
always=['Write the Arabic first, then fit the English to it.',
 'One idea per post. Two ideas is two posts.',
 'Let the character lead the frame on POLEKA and BeBo.',
 'Use Ink #141414 as the default type colour on a flavour field.',
 'Put a dark keyline behind white type on any colour field.',
 'Keep the navy keyline on the BeBo banner over any green.',
 'Name Alex Foods in every bio, sealed pack or not.']
never=['Health claims. صحي · مفيد · يقوي المناعة · غني بالفيتامينات',
 '«طبيعي ١٠٠٪» or "100% juice". BeBo is a powder. AlRawy is a nectar.',
 'Nutrition numbers without the client’s written spec sheet.',
 'Price claims. «الأرخص» is unverifiable and starts a public argument.',
 'Availability promises. Never name a shop that is not confirmed.',
 'POLEKA cola and strawberry in the same grid. They are ΔE 0.00 apart.',
 'A company age. Their own materials say 20 years and 25 years.']
al=''.join(f'<li><i>+</i>{x}</li>' for x in always)
nv=''.join(f'<li><i>–</i>{x}</li>' for x in never)

mix4=[('40','PRODUCT','المنتج','The packs, the ranges, the flavours. Eighteen SKUs to rotate, and the product is the hero.'),
 ('30','CHARACTER','الشخصيات','BeBo’s faces, POLEKA’s animals, 2MAN’s boy. Already drawn, already paid for.'),
 ('20','MOMENT','اللحظة','The lunchbox, the hot afternoon, the family jug. The occasion, never a claim about it.'),
 ('10','COMPANY','الشركة','Alex Foods itself. The city, the people, the ranges together.')]
mx=''.join(f'''<div class="stat"><span class="n">{a}<em>%</em></span><b>{b}</b><span class="par ar">{ar}</span><p>{c}</p></div>'''
           for a,b,ar,c in mix4)

rhythm=[('Instagram — Reels + posts','5 / week','Main platform. Reels for reach, posts for the range grid.'),
 ('Instagram Stories','Daily','Keeps the account warm. Polls and questions do the engagement.'),
 ('Facebook','4 / week','<b>Weighted higher than usual, deliberately.</b> BeBo and AlRawy talk to mothers, and in Egypt that audience is on Facebook.'),
 ('TikTok','3–4 / week','Repurpose the Reels. Free extra reach, no extra shoot.')]
rr=''.join(f'<tr><td><b>{a}</b></td><td class="mono rate">{b}</td><td class="sm">{c}</td></tr>' for a,b,c in rhythm)

page(f'''{eyebrow('افعل ولا تفعل','04 — RULES: DO &amp; DON&#39;T')}
<div class="two">
 <div class="lst"><b class="hh">ALWAYS <span class="ar">افعل</span></b><ul>{al}</ul></div>
 <div class="lst nev"><b class="hh">NEVER <span class="ar">ممنوع</span></b><ul>{nv}</ul></div>
</div>
<p class="fn"><b>The NEVER column is exposure, not style.</b> A food page can be reported and a paid ad account restricted on one sentence, and TSA runs the ad account. The rule underneath all of it: <b>if it did not come from the client in writing, we do not know it.</b></p>

{eyebrow('ماذا ننشر','05 — WHAT TO POST (CONTENT MIX)')}
<div class="stats">{mx}</div>

{eyebrow('إيقاع النشر','06 — POSTING RHYTHM')}
<table class="mt"><thead><tr><th>Platform</th><th>Frequency</th><th>Priority</th></tr></thead><tbody>{rr}</tbody></table>
<div class="chip2">SPEC — EXECUTION PENDING CLIENT ACCESS &nbsp;·&nbsp; Meta admin and the Google account have not arrived</div>''','RULES &amp; RHYTHM')

# ============ PAGE 5 — PRODUCT TEMPLATES ============
feed=''
CAPS={'BeBo':('قوليلهم آه.','ظرف واحد يعمل إبريق كامل.'),
      'AlRawy':('نكتار الراوي.','فاكهة، مش كلام.')}
for r in RANGES[:2]:
    lab,fld = r['fl'][0]
    fg,cr,kl = best(fld)
    ks = f'text-shadow:0 0 1mm {INK};' if kl else ''
    cap = CAPS[r['en']]
    feed+=f'''<div class="fdw"><div class="fd" style="background:{fld};color:{fg}">{corners()}
    <div class="tph"><img src="../logos-vector/alex-seal-flat.svg"></div>
    <img class="pk" src="../packshots/single/{r['key']}-1.png">
    <div class="fdb" style="{ks}"><b class="ar">{cap[0]}</b><span class="ar">{cap[1]}</span></div></div>
    <span class="tpk">{r['en']} · {lab} · <span class="mono">{fld}</span></span>
    <span class="tpn">Type {"white" if fg=="#FFFFFF" else "ink"} at {cr:.1f}:1{", keyline required" if kl else ", no keyline needed"}.</span></div>'''

page(f'''{eyebrow('قوالب المنتج','ALEX FOODS — PRODUCT TEMPLATES')}
<h3 class="ar big">النكهة تملك الخلفية.</h3>
<h4>PUT THE PACK IN THE <em>FRAME.</em></h4>
<p class="lead">For a food brand the pack IS the creative. These templates put the cut-out pack on its own flavour field with the copy underneath. Swap the pack and the field for the SKU you are posting. Nothing else moves.</p>

{eyebrow('منشورات الصفحة','FEED POSTS — 1080 × 1350')}
<div class="feeds">{feed}</div>
<p class="fn">Both captions are drafts from the Brand Voice Guide, written in Egyptian colloquial rather than translated out of English. <b>No em-dashes, no health claims, no price, no shop named.</b></p>

{eyebrow('ممنوع','SHOWN, NOT DESCRIBED')}
<div class="dont">
 <div class="dc"><div class="dpair">
   <div style="background:#EC008C"><span>Cola</span></div><div style="background:#EC008C"><span>Strawberry</span></div>
  </div><b>Never in the same grid</b>
  <p>Both POLEKA fields are <span class="mono">#EC008C</span> at <b>&#916;E 0.00</b>. At thumbnail size they read as one product. Split them across the calendar and let the character carry the difference.</p></div>
 <div class="dc"><div class="dpair">
   <div style="background:#2C8C3B"><span class="bdg">BeBo</span></div>
   <div style="background:#2C8C3B"><span class="bdg kl">BeBo</span></div>
  </div><b>The keyline is not decoration</b>
  <p>The banner on the apple field sits at <b>1.30:1</b>. Left is what happens without the navy keyline. <b>It is non-negotiable on any green, at any size.</b></p></div>
</div>''','PRODUCT TEMPLATES')

# ============ PAGE 6 — STORIES + HOW TO USE ============
st=''
for rn,capar,fld,logo in [('2MAN','برّه أحلى.','#29ABE2','single/2man-1.png'),
                          ('POLEKA','مين معاك النهاردة؟','#EC008C','single/poleka-4.png'),
                          ('AlRawy','كل يوم.','#00A3E0','single/alrawy-2.png')]:
    fg,cr,kl = best(fld)
    ks = f'text-shadow:0 0 1mm {INK};' if kl else ''
    st+=f'''<div class="styw"><div class="sty" style="background:{fld};color:{fg}">{corners()}
    <div class="tph"><img src="../logos-vector/alex-seal-flat.svg"></div>
    <img class="pk" src="../packshots/{logo}">
    <div class="styb" style="{ks}"><b class="ar">{capar}</b>
    <span class="cta" style="background:{RED};color:{PAPER}">اعرف أكتر</span></div></div>
    <span class="tpk">{rn} · <span class="mono">{fld}</span> · {cr:.1f}:1</span></div>'''

page(f'''{eyebrow('قوالب الستوري','STORIES &amp; REELS COVERS — 1080 × 1920')}
<div class="stys">{st}</div>
<p class="fn">Same formula vertical: pack centred, caption at the bottom, one red call to action. The story covers are where a range gets to be loud on its own.</p>

{eyebrow('كيف تستخدم هذا','HOW TO USE THIS')}
<div class="how"><b>The swap is simple</b><span class="ar hcap">التبديل بسيط</span>
<p>In Canva or Figma: flavour field as the background layer, the pack cut-out from <span class="mono">packshots/single/</span> on top, <b>the Alex seal</b> at the top corner, Arabic at the bottom in Plex Sans Arabic 700. <b>Write the Arabic first, then fit the English.</b> That is the whole formula.</p></div>
<div class="how"><b>Check the type colour, do not guess it</b><span class="ar hcap">تحقق من لون النص</span>
<p>If a colour is not one of the eighteen in the Design System, it is not in the system and the post is off-brand. <b>Bright Pink <span class="mono">#EC008C</span> is the trap</b> — white gives 4.2:1, ink gives 4.3:1, neither is comfortable, so that field always carries a keyline.</p></div>
<div class="how warn"><b>Two things this kit cannot do for you</b><span class="ar hcap">أمران خارج نطاق هذا الملف</span>
<p><b>Alex Foods has no tone block yet.</b> The four ranges have register, sentence length and emoji policy written down. The master account does not, and it is the one that actually posts. <b>And product photography has not arrived</b> — every frame here uses pack artwork, which is not the same thing.</p></div>

<div class="sign">{corners()}<div class="grid"></div>
 <p class="ar">أليكس فودز</p><p class="mono">BRAND &amp; SOCIAL KIT · v1.2 · 19.09.2026</p>
 <div class="by"><i></i><span>PREPARED BY THE STANDARD AGENCY · ALEXANDRIA, EGYPT</span></div></div>''','STORIES')

CSS=f'''
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:{PAPER};color:{INK};
 font-family:'IBM Plex Sans',sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:14mm 14mm 20mm;position:relative;overflow:hidden;
 background:{PAPER};page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto}}
.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;line-height:1.7}}
.mono{{font-family:'IBM Plex Mono',monospace}}
b,strong{{font-weight:700}}
.eb{{display:flex;align-items:center;gap:3mm;margin:4.6mm 0 2.4mm}}
.eb span{{font-size:6pt;font-weight:700;letter-spacing:.22em;color:{RED};text-transform:uppercase;white-space:nowrap}}
.eb i{{flex:1;height:0.25mm;background:{SILVER}}}
.eb b.ar{{font-size:8pt;font-weight:400;color:{SLATE}}}
.page > .eb:first-child{{margin-top:0}}
.cnr{{position:absolute;width:4mm;height:4mm;border:0.5mm solid {RED};z-index:3}}
.cnr.tl{{top:2.5mm;left:2.5mm;border-right:0;border-bottom:0}}
.cnr.tr{{top:2.5mm;right:2.5mm;border-left:0;border-bottom:0}}
.cnr.bl{{bottom:2.5mm;left:2.5mm;border-right:0;border-top:0}}
.cnr.br{{bottom:2.5mm;right:2.5mm;border-left:0;border-top:0}}
.grid{{position:absolute;inset:0;z-index:1;opacity:.05;
 background-image:repeating-linear-gradient(0deg,{PAPER} 0 0.2mm,transparent 0.2mm 7mm),
 repeating-linear-gradient(90deg,{PAPER} 0 0.2mm,transparent 0.2mm 7mm)}}
/* hero */
.hero{{position:relative;background:{DEEP};color:{PAPER};padding:7mm 9mm;overflow:hidden;
 display:flex;align-items:center;gap:7mm;min-height:38mm}}
.hero .hx{{position:relative;z-index:2;flex:1}}
.hero .seal{{position:relative;z-index:2;width:30mm;height:auto}}
.hero h1{{font-size:24pt;font-weight:700;margin:0;line-height:1.35}}
.hero h2{{font-size:16pt;font-weight:700;margin:1mm 0 0;letter-spacing:.16em}}
.hero.rule{{min-height:0;padding:7mm 9mm}}
.hero h3{{font-size:12.5pt;font-weight:700;margin:2.5mm 0 0;line-height:1.35}}
.hero h3 em{{font-style:normal;color:#FF6A60}}
.hero .rl{{font-size:13pt;font-weight:700;margin:0;line-height:1.55}}
.sub{{font-size:7pt;color:#B9B5D8;margin:2.5mm 0 0;letter-spacing:.05em;line-height:1.55}}
/* lockups */
.locks{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin-top:2.5mm}}
.lk{{height:23mm;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2mm;padding:3mm}}
.lk img{{max-width:80%;max-height:16mm;object-fit:contain}}
.lk.wide .minis img{{max-height:11mm;max-width:100%}}
.lk span{{font-size:5.2pt;font-weight:700;letter-spacing:.14em;opacity:.75}}
.minis{{display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;width:100%;align-items:center;justify-items:center}}
.minis img{{max-height:6.5mm;max-width:90%;object-fit:contain}}
/* colour swatches */
.csws{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.rsws{{display:grid;grid-template-columns:auto repeat(4,1fr);gap:3mm;align-items:center;
 margin-top:2.5mm;border-top:0.4mm solid {INK};padding:2.6mm 3.5mm}}
.rlab{{font-size:5pt;font-weight:700;letter-spacing:.14em;color:{RED};white-space:nowrap}}
.rsw{{display:flex;align-items:center;gap:2mm}}
.rsw i{{width:5mm;height:5mm;display:block;flex:none}}
.rsw b{{font-size:7.5pt}}
.rsw .ar{{font-size:6.6pt;color:{SLATE}}}
.rsw .mono{{font-size:6.4pt;color:{GRAPH};margin-left:auto}}
.csw{{border-top:0.4mm solid {INK};padding:0 0 3mm}}
.csw .chip{{height:9.5mm;width:100%;display:block;margin-bottom:2.5mm}}
.csw b{{font-size:8.5pt;display:block;padding:0 3mm}}
.csw .ar{{font-size:7pt;color:{SLATE};display:block;padding:0 3mm}}
.csw .mono{{font-size:7.5pt;display:block;padding:0 3mm;margin-top:0.8mm}}
.csw .role{{font-size:5pt;font-weight:700;letter-spacing:.14em;color:{RED};display:block;padding:1.5mm 3mm 0}}
/* typography */
.typ{{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}}
.tyl{{background:{MIST};padding:4mm}}
.tyl p.d1{{font-size:19pt;font-weight:700;margin:0;line-height:1.32;color:{INK}}}
.tyl p.d1.red{{color:{RED}}}
.tspec{{border-top:0.25mm solid {SILVER};margin:3mm 0 2mm;padding-top:2mm}}
.tspec span{{display:block;font-size:5.6pt;font-weight:700;letter-spacing:.16em;color:{GRAPH};margin-bottom:1mm}}
.tyl p{{font-size:7.2pt;line-height:1.6;margin:0;color:{GRAPH}}}
.tyr{{display:flex;flex-direction:column;gap:2mm}}
.tf{{border-top:0.4mm solid {INK};padding:1.9mm 3.5mm}}
.tf b{{font-size:8pt;display:block}}
.tf span{{font-size:6.2pt;color:{SLATE};line-height:1.5;display:block}}
.tf.note{{background:{MIST};border-color:{MIST};margin-top:auto}}
.tf.note span{{color:{GRAPH}}}
/* the promise */
.promise{{position:relative;background:{RED};color:{PAPER};padding:4mm 7mm;overflow:hidden;
 display:flex;align-items:center;justify-content:space-between;gap:6mm}}
.promise .px{{position:relative;z-index:2}}
.promise .ar{{font-size:14pt;font-weight:700;margin:0}}
.promise .en{{font-size:7.5pt;font-weight:700;letter-spacing:.2em;margin:1.5mm 0 0}}
/* positioning */
.two{{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}}
.vs{{border-top:0.7mm solid {INK};padding:4.5mm 5mm;background:transparent}}
.vs.win{{border-top-color:{RED};background:{MIST}}}
.vl{{font-size:5.5pt;font-weight:700;letter-spacing:.2em;color:{RED};display:block;margin-bottom:2mm}}
.vs > b{{font-size:13pt;line-height:1.2;display:block}}
.vs p{{font-size:7.2pt;line-height:1.6;margin:2.5mm 0 0;color:{GRAPH}}}
.pils{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}
.pil{{border-top:0.4mm solid {INK};padding:4mm}}
.pil .no{{font-size:19pt;font-weight:700;color:{SILVER};line-height:1;display:block}}
.pil > b{{font-size:11pt;display:block;margin-top:1.5mm;letter-spacing:.04em}}
.par{{font-size:8pt;color:{SLATE};display:block}}
.pil p{{font-size:7pt;line-height:1.6;margin:2mm 0 0;color:{GRAPH}}}
.rules{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm}}
.ru{{border-top:0.4mm solid {INK};padding:3mm 4mm;font-size:7pt;display:flex;align-items:baseline;gap:2.5mm;
 line-height:1.55;color:{GRAPH}}}
.ru i{{width:1.4mm;height:1.4mm;background:{RED};border-radius:50%;flex:none;position:relative;top:-0.5mm}}
.ru b{{color:{INK}}}
/* headings */
h3.ar.big{{font-size:19pt;font-weight:700;margin:0}}
h4{{font-size:16pt;font-weight:700;margin:1mm 0 3mm;letter-spacing:.05em}}
h4 em{{font-style:normal;color:{RED}}}
p.lead{{font-size:8pt;line-height:1.6;color:{GRAPH};margin:0 0 2mm;max-width:155mm}}
p.fn{{font-size:6.8pt;line-height:1.55;color:{SLATE};margin:3mm 0 0}}
p.fn b{{color:{INK}}}
.sm{{font-size:7pt;color:{GRAPH}}}
/* cards + tables */
.card{{background:{MIST};padding:5mm}}
.card.ctr{{text-align:center}}
.pfp{{width:21mm;height:21mm;border-radius:50%;margin:1mm auto 3mm;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.pfp img{{width:19mm;height:auto}}
.cap{{font-size:5.8pt;font-weight:700;letter-spacing:.16em;color:{RED};display:block}}
.card p{{font-size:7.2pt;line-height:1.55;margin:2mm 0 0;color:{GRAPH}}}
table.mt{{width:100%;border-collapse:collapse;margin:1mm 0}}
table.mt th{{font-size:5.6pt;text-transform:uppercase;letter-spacing:.2em;color:{RED};text-align:left;
 font-weight:700;padding:2mm;background:{MIST}}}
table.mt td{{padding:1.7mm 2mm;border-bottom:0.2mm solid {SILVER};font-size:7.5pt;vertical-align:middle;color:{GRAPH}}}
table.mt td b{{font-size:8pt;color:{INK}}}
table.mt td .ar.sm{{font-size:7pt;color:{SLATE};display:block}}
td.mono{{font-size:8pt;font-weight:700;color:{INK}}} td.rate{{font-size:9pt;font-weight:700;color:{INK}}}
/* post templates */
.tpls{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}
.tp{{position:relative;height:45mm;padding:4mm;display:flex;flex-direction:column;overflow:hidden}}
.tph{{position:relative;z-index:2;display:flex;align-items:center}}
.tph img{{height:9mm;width:auto}}
.tpk2{{position:absolute;z-index:1;right:3mm;top:8mm;max-height:24mm;width:auto}}
.tpb{{position:relative;z-index:2;margin-top:auto}}
.tpb b.ar{{font-size:11pt;display:block;line-height:1.45}}
.tpk{{font-size:5.4pt;font-weight:700;letter-spacing:.14em;display:block;margin-top:2mm;color:{INK}}}
.tpn{{font-size:6.3pt;display:block;color:{SLATE};line-height:1.5;margin-top:0.6mm}}
/* always / never */
.lst{{border:0.25mm solid {SILVER}}}
.lst > .hh{{display:block;font-size:11pt;padding:3.2mm 5mm;background:{INK};color:{PAPER};letter-spacing:.06em}}
.lst.nev > .hh{{background:{RED}}}
.lst > .hh .ar{{font-size:9pt;font-weight:400;float:right}}
.lst ul{{margin:0;padding:2.5mm 5mm 3.5mm;list-style:none}}
.lst li{{font-size:7pt;line-height:1.55;padding:1.7mm 0;border-bottom:0.2mm solid {MIST};
 display:flex;gap:2.5mm;align-items:baseline;color:{GRAPH}}}
.lst li:last-child{{border:0}}
.lst li i{{font-style:normal;font-weight:700;color:{RED};flex:none;width:2.5mm}}
/* stats */
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.stat{{border-top:0.4mm solid {INK};padding:4mm}}
.stat .n{{font-size:24pt;font-weight:700;line-height:1;display:block}}
.stat .n em{{font-style:normal;color:{RED};font-size:15pt}}
.stat > b{{font-size:8.5pt;display:block;margin-top:1.5mm;letter-spacing:.08em}}
.stat p{{font-size:6.6pt;line-height:1.55;margin:2mm 0 0;color:{GRAPH}}}
.chip2{{display:inline-block;background:{RED};color:{PAPER};font-size:6pt;letter-spacing:.1em;
 padding:2mm 3.5mm;font-family:'IBM Plex Mono',monospace;margin-top:4mm;font-weight:700}}
/* feed + story */
.feeds{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.fd{{position:relative;height:74mm;padding:4.5mm;display:flex;flex-direction:column;overflow:hidden}}
.fd .pk{{position:absolute;z-index:1;right:4mm;top:10mm;max-width:52%;max-height:34mm;object-fit:contain}}
.fdb{{position:relative;z-index:2;margin-top:auto}}
.fdb b.ar{{font-size:15pt;display:block;line-height:1.35}}
.fdb span.ar{{font-size:8.5pt;display:block;opacity:.92}}
.stys{{display:grid;grid-template-columns:repeat(3,1fr);gap:3.5mm}}
.sty{{position:relative;height:74mm;padding:4mm;display:flex;flex-direction:column;overflow:hidden}}
.sty .pk{{position:absolute;z-index:1;left:50%;transform:translateX(-50%);top:11mm;max-width:66%;max-height:29mm;object-fit:contain}}
.styb{{position:relative;z-index:2;margin-top:auto}}
.styb b.ar{{font-size:12pt;display:block;line-height:1.4;margin-bottom:2.5mm}}
.cta{{font-family:'IBM Plex Sans Arabic',sans-serif;direction:rtl;display:inline-block;
 font-size:7pt;font-weight:700;padding:1.6mm 3.5mm}}
/* do-not */
.dont{{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}}
.dc{{border-top:0.4mm solid {INK};padding:4mm}}
.dc > b{{font-size:8.5pt;display:block;margin:2.5mm 0 1mm}}
.dc p{{font-size:6.6pt;line-height:1.55;margin:0;color:{GRAPH}}}
.dpair{{display:grid;grid-template-columns:1fr 1fr;gap:2mm}}
.dpair > div{{height:18mm;display:flex;align-items:center;justify-content:center;
 font-size:7pt;font-weight:700;color:{INK}}}
.bdg{{background:#1BA34C;color:{PAPER};padding:1.3mm 3.5mm;font-size:7.5pt}}
.bdg.kl{{border:0.7mm solid #1E2A6B}}
/* range blocks */
.rng{{border-top:0.9mm solid {INK};padding:4mm 4.5mm 4.5mm;margin-bottom:3.5mm}}
.rtop{{display:grid;grid-template-columns:24mm 1fr 62mm;gap:5mm;align-items:center}}
.rlogo{{height:17mm;display:flex;align-items:center;justify-content:center}}
.rlogo img{{max-width:100%;max-height:17mm;object-fit:contain}}
.rid b.ar{{font-size:12pt;display:block;line-height:1.3}}
.rid b.ren{{font-size:13pt;display:block;letter-spacing:.04em;line-height:1.1}}
.rfmt{{display:block;font-size:7pt;color:{GRAPH};line-height:1.5}}
.rfmt.ar{{font-size:7.6pt;color:{INK};margin-top:1.2mm}}
.rwho p{{font-size:6.8pt;line-height:1.55;margin:1mm 0 0;color:{GRAPH}}}
.rpacks{{margin:3.5mm 0 3mm;display:grid;gap:4mm;align-items:center;justify-items:center}}
.rpacks.c1{{grid-template-columns:1fr}}
.rpacks.c2{{grid-template-columns:1fr 1fr}}
.rpacks img{{width:100%;height:auto;max-height:46mm;object-fit:contain}}
.rpal{{display:flex;gap:1.6mm}}
.pchip{{flex:1;padding:1.8mm 2mm;min-height:10mm;display:flex;flex-direction:column;justify-content:center}}
.pchip b{{font-size:5.4pt;letter-spacing:.06em;display:block;line-height:1.3}}
.pchip .mono{{font-size:5.4pt;opacity:.9}}
.pchip.sig{{color:{PAPER};flex:0 0 26mm}}
.ridy{{font-size:6.6pt;line-height:1.6;margin:2.5mm 0 0;color:{GRAPH}}}
.ridy b{{color:{INK}}}
/* clear space card */
.clr{{display:grid;grid-template-columns:26mm 1fr;gap:4mm;align-items:center;margin-top:2.5mm}}
.clrbox{{border:0.4mm dashed {SILVER};padding:3.5mm;display:flex;align-items:center;justify-content:center}}
.clrbox img{{width:100%;height:auto}}
.clr p{{font-size:6.8pt;line-height:1.55;margin:0 0 1.5mm;color:{GRAPH}}}
.clr p b{{color:{INK}}}
/* how to use */
.how{{background:{MIST};border-left:0.8mm solid {RED};padding:3.5mm 5mm;margin-bottom:2.5mm}}
.how.warn{{border-left-color:{INK}}}
.how > b{{font-size:9pt;display:inline}}
.hcap{{font-size:8pt;color:{SLATE};margin-left:2.5mm}}
.how p{{font-size:7pt;line-height:1.6;margin:1.5mm 0 0;color:{GRAPH}}}
.sign{{position:relative;background:{DEEP};color:{PAPER};padding:7mm;margin-top:3mm;overflow:hidden;text-align:center}}
.sign .ar{{font-size:16pt;font-weight:700;position:relative;z-index:2;margin:0}}
.sign .mono{{font-size:6.6pt;color:#B9B5D8;margin:1mm 0 3.5mm;position:relative;z-index:2}}
.by{{position:relative;z-index:2;display:inline-flex;align-items:center;gap:2.5mm}}
.by i{{width:1mm;height:3.4mm;background:{RED};display:block}}
.by span{{font-size:5.8pt;font-weight:700;letter-spacing:.16em;color:#B9B5D8}}
/* footer */
footer{{position:absolute;left:14mm;right:14mm;bottom:9mm;display:flex;justify-content:space-between;
 align-items:center;font-size:6pt;letter-spacing:.14em;text-transform:uppercase;font-weight:700;
 color:{SLATE};border-top:0.25mm solid {SILVER};padding-top:2.5mm}}
footer .fm{{display:flex;align-items:center;gap:2mm}}
footer .fm b{{color:{INK};letter-spacing:.1em}}
footer .fm em{{font-family:'IBM Plex Sans Arabic',sans-serif;font-style:normal;
 direction:rtl;font-weight:400;letter-spacing:0;text-transform:none;font-size:7pt}}
'''
html=f'''<!doctype html><html lang="ar" dir="ltr"><head><meta charset="utf-8">
<title>Alex Foods — Brand &amp; Social Kit v1.2</title>
<link rel="stylesheet" href="plex.css"><style>{CSS}</style></head><body>{''.join(H)}</body></html>'''
html=html.replace('@@TOTAL@@', str(PAGES[0]))
io.open(os.path.join(HERE,'kit.html'),'w',encoding='utf-8').write(html)
print("pages:",PAGES[0])
