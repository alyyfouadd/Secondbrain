# -*- coding: utf-8 -*-
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,'colour.py')).read().split('# sanity')[0])

# TSA brand system governs the document. Client colours appear only as content.
PAPER='#F0F2F5'  # Cold White - the only white in the system
INK='#0A0F1E'    # Precision Navy
RED='#E8203A'    # Signal Red - accent, reserved
SURF='#1A2340'   # Surface Navy - panels only, never a brand colour
MIST='#E2E5EA'; SILVER='#C3C8D2'; SLATE='#6E7687'; GRAPHITE='#2A3348'
# The client's own neutrals. Contrast verdicts describe ALEX FOODS' system, not this document's,
# so they are measured against the client's ink and never against TSA's Precision Navy.
CLIENT_INK='#141414'; CLIENT_PAPER='#FAF8F3'
def cmyk(h):
    r,g,b=[c/255 for c in hx(h)]; k=1-max(r,g,b)
    if k>=1: return (0,0,0,100)
    return tuple(round(x*100) for x in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def mix(a,b,t):
    A,B=hx(a),hx(b); return hs(tuple(A[i]+(B[i]-A[i])*t for i in range(3)))
def ramp(h): return [mix(h,CLIENT_PAPER,.72),mix(h,CLIENT_PAPER,.36),h,mix(h,CLIENT_INK,.26),mix(h,CLIENT_INK,.52)]
def best(h):
    w=ratio('#FFFFFF',h); k=ratio(CLIENT_INK,h)
    if w>=4.5 and w>=k: return ('WHITE','#FFFFFF',w)
    if k>=4.5: return ('INK',CLIENT_INK,k)
    return ('KEYLINE', CLIENT_INK if k>=w else '#FFFFFF', max(w,k))

M=[('Brand Green','#1BA34C','أخضر العلامة'),('Deep Green','#2C8C3B','أخضر غامق'),('Leaf Green','#8DC63F','أخضر ورقي'),
   ('Lime','#C6D42E','ليموني'),('BeBo Navy','#1E2A6B','كحلي بيبو'),('AlRawy Navy','#1B4F9C','كحلي الراوي'),
   ('Cola Blue','#1C74BC','أزرق كولا'),('Ice Blue','#29ABE2','أزرق ثلجي'),('Nectar Blue','#00A3E0','أزرق نكتار'),
   ('System Red','#E1251D','أحمر النظام'),('Peach Orange','#E4762A','برتقالي خوخي'),('Mango Orange','#F07F13','برتقالي مانجو'),
   ('Golden Yellow','#F2A00C','أصفر ذهبي'),('Bright Yellow','#FFC20E','أصفر زاهي'),('Acid Yellow','#FFF200','أصفر حامضي'),
   ('Bright Pink','#EC008C','وردي زاهي'),('Deep Magenta','#D6006E','ماجنتا غامق'),('Deep Purple','#92278F','بنفسجي غامق')]
NEU=[('Paper','#FAF8F3','Every background. Never pure white.'),('Mist','#EDEAE3','Panel fills. Never type.'),
     ('Silver','#C9C5BC','Rules and dividers. Never type.'),('Slate','#8A8681','Captions at display size only.'),
     ('Graphite','#4A4742','Secondary body text.'),('Ink','#141414','Primary text everywhere.')]
BRANDS=[
 ('BeBo','بيبو','Powdered drink sachets',
  [('Banner green — logo pillow, never recoloured','Brand Green','#1BA34C'),('Wordmark keyline — non-negotiable','BeBo Navy','#1E2A6B'),('"NEW" flash only','System Red','#E1251D')],
  [('Peach · خوخ','#E4762A'),('Mango · مانجو','#F2A00C'),('Apple · تفاح','#2C8C3B'),('Cola · كولا','#1C74BC'),('Pineapple · أناناس','#C6D42E')],
  'The banner never appears on any green without its keyline. On the apple pack it sits at 1.30:1 against the field and the keyline is the only thing holding it.'),
 ('AlRawy','الراوي','Juice and nectar pouches',
  [('Wordmark','AlRawy Navy','#1B4F9C'),('The "y" only, never extended','System Red','#E1251D'),('Ribbon swoosh','Leaf Green','#8DC63F')],
  [('Cocktail · كوكتيل','#D6006E'),('Apple · تفاح','#00A3E0'),('Guava · جوافة','#1BA34C'),('Peach · خوخ','#E1251D'),('Mango · مانجو','#F07F13')],
  'Nectar Blue is a field colour only. It is never an AlRawy brand element, and AlRawy never shares a layout with 2MAN.'),
 ('2MAN','تو مان','Ice pops — two live lines',
  [('Home colour, the brand’s whole world','Ice Blue','#29ABE2')],
  [('Colourway blue','#29ABE2'),('Colourway red','#E1251D'),('Colourway green','#8DC63F'),('Colourway orange','#F07F13')],
  'Wordmark letter colours live inside the artwork and are not system values. The voice and the system are identical across ICE POPS and Bu:Zz.'),
 ('POLEKA','بوليكا','Jelly candy',
  [('Extended, social only','Deep Purple','#92278F')],
  [('Apple · التفاح','#1BA34C'),('Mango · المانجو','#FFF200'),('Cola','#EC008C'),('Strawberry · الفراولة','#EC008C')],
  'Cola and strawberry share one field at ΔE 0.00. They never appear in the same grid, carousel or story sequence, and the character always leads the frame.'),
]

H=[]
def p(s): H.append(s)
PAGES=[0]
def page(cls, body, label=''):
    PAGES[0]+=1
    p(f'<section class="page {cls}">{body}<footer><span class="fm"><i></i><b>TSA</b></span>'
      f'<span>Alex Foods · Design System v1.0 · 18.09.2026</span>'
      f'<span>{label}</span><span>{PAGES[0]}</span></footer></section>')

def sw(h,name='',code=True,hgt='22mm'):
    mode,col,r=best(h)
    tag='' if not code else f'<span class="hexl" style="color:{col}">{h}</span>'
    return f'<div class="sw" style="background:{h};height:{hgt}"><span style="color:{col}">{name}</span>{tag}</div>'

# ---------- COVER ----------
page('cover', f'''<div class="cov">
<div class="covtop"><div class="lockup"><i></i><span>THE STANDARD AGENCY</span></div></div>
<div class="covmid">
<div class="eyebrow">Brand Foundation · Deliverable 2 of 8</div>
<h1>نظام التصميم</h1><h2>DESIGN SYSTEM</h2>
<div class="covsub">Alex Foods &nbsp;·&nbsp; BeBo &nbsp;·&nbsp; AlRawy &nbsp;·&nbsp; 2MAN &nbsp;·&nbsp; POLEKA</div>
</div>
<div class="covbot"><div class="meta"><span>Version 1.0</span><span>18 September 2026</span><span>Prepared for Alex Foods</span></div>
<div class="tag">Grow the <em>standard</em>.</div>
<div class="bands"></div></div></div>''')

# ---------- HOW TO USE ----------
page('', f'''<h3 class="ar">كيف يُستخدم هذا المستند</h3><h4>How to use this document</h4>
<div class="two">
<div><p class="lead">This document defines the colour and type system for all four Alex Foods brands. It is the reference anyone designing for these brands works from.</p>
<p>Everything in it is <b>governed</b>. A value that is not in this document is not in the system, and anything using one is off-brand.</p>
<h5>What this replaces</h5><p>Nothing. There was no colour manual and there were no codes. Building them is what this stage delivers. The packaging was the input, not the answer.</p>
<h5>What this is not</h5><p>This is structure and governance, not a repaint. The packs are printed and in market. Where this document records a problem on an existing pack, it records it and writes the rule that contains it. Changing printed artwork is a separate quotation.</p></div>
<div><h5>Who decides</h5><p>TSA owns execution. The client approves or rejects a delivery as a whole, as an outcome rather than an instruction.</p>
<h5>Contents</h5>
<table class="toc"><tr><td>1</td><td>The four layers</td><td>3</td></tr>
<tr><td>2</td><td>The master set</td><td>4</td></tr><tr><td>3</td><td>Brand assignments</td><td>6</td></tr>
<tr><td>4</td><td>Ramps</td><td>10</td></tr><tr><td>5</td><td>Neutrals</td><td>11</td></tr>
<tr><td>6</td><td>Type on colour</td><td>12</td></tr><tr><td>7</td><td>The wordmarks</td><td>13</td></tr>
<tr><td>8</td><td>The faces and weights</td><td>14</td></tr><tr><td>9</td><td>Scales</td><td>15</td></tr>
<tr><td>10</td><td>Bilingual rules</td><td>16</td></tr><tr><td>11</td><td>Never do this</td><td>17</td></tr>
<tr><td>12</td><td>Known defects</td><td>18</td></tr><tr><td>13</td><td>Governance</td><td>19</td></tr></table>
<div class="chip">DEFINED</div></div></div>''','How to use')

# ---------- LAYERS ----------
page('', f'''<h3 class="ar">الطبقات الأربع</h3><h4>1 · The four layers</h4>
<div class="layers">
<div class="lay"><b>1 · Parent</b><p>The Alex seal. Alex is the parent company, endorsing selected lines. <b>There is no house palette.</b> A parent that endorses does not repaint what it endorses.</p><p class="sm">The seal appears exactly where it appears today. Never added to a pack without it, never removed from one with it.</p></div>
<div class="lay"><b>2 · Brand</b><p>Each brand's own fixed colours. These never change, for any reason, in any medium.</p></div>
<div class="lay"><b>3 · Flavour</b><p>The field colour that owns a pack for a given SKU. Changes per product.</p></div>
<div class="lay"><b>4 · Extended</b><p>Colours a brand may use <b>in social layouts only, never on a pack.</b> Twelve monthly graphics built from three colours look like three graphics repeated four times.</p></div>
</div>
<div class="rule"><b>The flavour colour owns the field. The brand colour owns the logo. They never trade places.</b>
<p>A BeBo mango pack is a mango-coloured field with the standard green banner on it. The banner does not turn orange to match. That unchanged banner across five colour fields is what makes a shelf of BeBo read as one brand.</p></div>
<div class="rule alt"><b>A value may be shared between brands where neither owns it as a signature. It may not be shared where one does.</b></div>''','The four layers')

# ---------- MASTERS ----------
for chunk,start in ((M[:9],0),(M[9:],9)):
    rows=''
    for n,h,ar in chunk:
        r,g,b=hx(h); c,m,y,k=cmyk(h); mode,col,cr=best(h)
        rows+=f'''<tr><td class="cell"><div class="chipsw" style="background:{h}"></div></td>
        <td><b>{n}</b><span class="ar sm">{ar}</span></td>
        <td class="mono">{h}</td><td class="mono sm">{r} {g} {b}</td><td class="mono sm">{c} {m} {y} {k}</td>
        <td class="sm"><b>{mode}</b> · {cr:.1f}:1</td></tr>'''
    page('', f'''<h3 class="ar">المجموعة الأساسية</h3><h4>2 · The master set{" (continued)" if start else " — 18 values"}</h4>
    {"<p class='lead'>Thirty-one sampled values across four brands, rationalised to eighteen. Thirteen were duplicates nobody could tell apart.</p>" if not start else ""}
    <table class="mt"><thead><tr><th></th><th>Name</th><th>HEX</th><th>RGB</th><th>CMYK<sup>*</sup></th><th>Type colour</th></tr></thead><tbody>{rows}</tbody></table>
    <p class="fn"><sup>*</sup> CMYK is an unmanaged conversion, a starting point for a printer and not a press specification.</p>''','The master set')

# ---------- BRANDS ----------
for name,ar,desc,brand,flav,rule in BRANDS:
    bl=''.join(f'<tr><td class="cell"><div class="chipsw sm2" style="background:{h}"></div></td><td class="sm">{lab}</td><td class="mono sm">{m}</td><td class="mono sm">{h}</td></tr>' for lab,m,h in brand)
    fl=''.join(sw(h,lab,hgt='26mm') for lab,h in flav)
    page('', f'''<h3 class="ar">{ar}</h3><h4>3 · {name} — {desc}</h4>
    <h5>Brand colours — fixed</h5><table class="mt sm"><tbody>{bl}</tbody></table>
    <h5>Flavour fields</h5><div class="flav">{fl}</div>
    <div class="rule"><b>Rule</b><p>{rule}</p></div>''', f'{name}')

# ---------- RAMPS ----------
rows=''
for n,h,ar in M:
    cells=''.join(f'<td class="rc"><div class="chipsw sm2" style="background:{c}"></div><span class="mono xs">{c}</span></td>' for c in ramp(h))
    rows+=f'<tr><td class="sm"><b>{n}</b></td>{cells}</tr>'
page('', f'''<h3 class="ar">التدرجات</h3><h4>4 · Ramps</h4>
<p class="lead">Every master gets tints toward paper and shades toward ink. One flat swatch is what forces off-system colour picking, and that is how a palette dies.</p>
<p class="sm"><b>500 is the master</b> and the only value that appears on a pack. 100 and 300 are backgrounds and fills. 700 and 900 are type, borders and depth.</p>
<table class="mt xs2"><thead><tr><th></th><th>100</th><th>300</th><th>500</th><th>700</th><th>900</th></tr></thead><tbody>{rows}</tbody></table>
<p class="fn">Mixed toward paper and ink rather than white and black. Black-mixed shades go muddy.</p>''','Ramps')

# ---------- NEUTRALS ----------
nl=''.join(f'''<tr><td class="cell"><div class="chipsw" style="background:{h};border:0.3mm solid {SILVER}"></div></td><td><b>{n}</b></td><td class="mono">{h}</td><td class="sm">{u}</td><td class="mono sm">{ratio(h,CLIENT_PAPER):.2f}:1</td></tr>''' for n,h,u in NEU)
page('', f'''<h3 class="ar">الألوان المحايدة</h3><h4>5 · Neutrals</h4>
<p class="lead">The layer all four brands share and none of them had. Every document, template, calendar and this book are built from it.</p>
<table class="mt"><thead><tr><th></th><th>Name</th><th>HEX</th><th>Use</th><th>On Paper</th></tr></thead><tbody>{nl}</tbody></table>
<div class="rule"><b>Paper is #FAF8F3, never pure white.</b><p>Pure white glares on screen and looks cheap in print.</p></div>''','Neutrals')

# ---------- CONTRAST ----------
rows=''
for n,h,ar in M:
    w=ratio('#FFFFFF',h); k=ratio(CLIENT_INK,h)
    def v(x): return ('pass' if x>=4.5 else ('head' if x>=3 else 'fail'))
    rows+=f'''<tr><td class="cell"><div class="chipsw sm2" style="background:{h}"></div></td><td class="sm">{n}</td>
    <td class="mono sm t{v(w)}">{w:.1f}:1 {v(w)}</td><td class="mono sm t{v(k)}">{k:.1f}:1 {v(k)}</td></tr>'''
page('', f'''<h3 class="ar">النص على اللون</h3><h4>6 · Type on colour</h4>
<div class="rule big"><b>The client's Ink #141414 is the default type colour on a flavour field. White is the exception, and it gets checked.</b>
<p>White type fails on 11 of the 18 masters. Ink passes on 12. The instinct in this category is white on a bright field, and on this palette it is wrong more often than it is right.</p></div>
<table class="mt"><thead><tr><th></th><th>Master</th><th>White text</th><th>Client Ink #141414</th></tr></thead><tbody>{rows}</tbody></table>
<p class="fn">pass = WCAG AA body text at 4.5:1 · head = 3:1, display sizes only · fail = not usable for type without a keyline</p>''','Type on colour')

# ---------- WORDMARKS ----------
page('', f'''<h3 class="ar">العلامات النصية</h3><h4>7 · The wordmarks are artwork</h4>
<div class="rule big"><b>No brand name in this system is ever set in a font.</b></div>
<table class="mt"><thead><tr><th>Brand</th><th>The wordmark is</th><th>Consequence</th></tr></thead><tbody>
<tr><td><b>BeBo</b></td><td class="sm">Heavy rounded italic sans, customised</td><td class="sm">Close to typeset. Still artwork.</td></tr>
<tr><td><b>AlRawy</b></td><td class="sm">Rounded sans with a script quality, plus flowing Arabic</td><td class="sm">Artwork.</td></tr>
<tr><td><b>2MAN</b></td><td class="sm">Custom illustrated 3D lettering, dripping ice</td><td class="sm"><b>Cannot be retyped. Ever.</b></td></tr>
<tr><td><b>POLEKA</b></td><td class="sm">Custom illustrated 3D gel lettering</td><td class="sm"><b>Cannot be retyped. Ever.</b></td></tr></tbody></table>
<p class="lead">All four are placed as supplied vector artwork. Anyone who rebuilds a logo because the file was missing has produced something unusable, and it will be spotted.</p>
<div class="chip warn">PENDING CLIENT INPUT — vector logo files</div>
<p class="sm">This is also the hard argument for why vector files are not an optional material: without them there is no legal way to produce a single asset in either stage.</p>''','The wordmarks')

# ---------- FACES ----------
page('', f'''<h3 class="ar">الخطوط</h3><h4>8 · The faces and weights</h4>
<table class="mt"><thead><tr><th>Role</th><th>Face</th><th>Weights</th><th>Cost</th></tr></thead><tbody>
<tr><td class="sm">Arabic and Latin text</td><td><b>IBM Plex Sans Arabic</b></td><td class="mono sm">400 · 600 · 700</td><td class="sm">Free</td></tr>
<tr><td class="sm">Latin, set alone</td><td><b>IBM Plex Sans</b></td><td class="mono sm">400 · 600 · 700</td><td class="sm">Free</td></tr>
<tr><td class="sm">Codes and specifications</td><td><b>IBM Plex Mono</b></td><td class="mono sm">400 · 600</td><td class="sm">Free</td></tr></tbody></table>
<div class="spec"><div class="sp400">الأربعاء ٤٠٠ Regular Hamburgefonstiv</div><div class="sp600">الأربعاء ٦٠٠ SemiBold Hamburgefonstiv</div><div class="sp700">الأربعاء ٧٠٠ Bold Hamburgefonstiv</div><div class="spm">IBM Plex Mono · #1BA34C 0123456789</div></div>
<div class="rule"><b>Two weights maximum in any single layout.</b><p>One for the headline, one for everything else. These packs are already visually loud and the type does not need to compete. A third weight is the most common way a tidy system starts to look accidental.</p></div>
<p class="sm"><b>Why this family.</b> Drawn as one bilingual superfamily rather than a Latin face with Arabic bolted on, so there is no visible seam where a line switches script. The mono sibling matters more than it sounds: HEX values in a proportional face do not align in a column, and an <span class="mono">8</span> reads as a <span class="mono">B</span> at 9pt.</p>
<p class="sm"><b>The honest tradeoff.</b> Plex runs cool. On BeBo and POLEKA it will not supply warmth, and it is not supposed to — the packs carry the personality and the type carries order.</p>''','Faces')

# ---------- SCALES ----------
pr=''.join(f'<tr><td class="sm">{a}</td><td class="mono sm">{b}</td><td class="mono sm">{c}</td></tr>' for a,b,c in
  [('Cover title','72 pt','1.05'),('Section opener','48 pt','1.1'),('Page heading','28 pt','1.2'),('Sub-heading','16 pt','1.3'),('Body','10.5 pt','1.5 Latin · 1.7 Arabic'),('Caption','8.5 pt','1.45'),('Code (mono)','9 pt','1.4')])
so=''.join(f'<tr><td class="sm">{a}</td><td class="mono sm">{b}</td><td class="mono sm">{c}</td><td class="mono sm">{d}</td></tr>' for a,b,c,d in
  [('Hero line','96 px','1.1','700'),('Headline','64 px','1.15','700'),('Sub-head','44 px','1.25','600'),('Body','32 px','1.5 / 1.7 ar','400'),('Caption and legal','24 px','1.4','400')])
page('', f'''<h3 class="ar">المقاسات</h3><h4>9 · Scales</h4>
<h5>Documents and print — A4</h5>
<table class="mt"><thead><tr><th>Role</th><th>Size</th><th>Leading</th></tr></thead><tbody>{pr}</tbody></table>
<h5>Social — 1080 × 1350 feed</h5>
<p class="sm">Story at 1080 × 1920 uses the same values with more vertical breathing room.</p>
<table class="mt"><thead><tr><th>Role</th><th>Size</th><th>Leading</th><th>Weight</th></tr></thead><tbody>{so}</tbody></table>
<div class="rule big"><b>Absolute floor: 22 px. Nothing goes below it on a feed asset.</b>
<p>Below that it is unreadable on a phone at thumbnail size, which is where most of the audience sees it. It is also exactly the size everyone is tempted to use for the weight statement and the flavour name.</p></div>''','Scales')

# ---------- BILINGUAL ----------
items=[('Arabic is set first. English is fitted to it.','A layout designed in English and then filled with Arabic will break, every time. Line lengths, optical weight and direction are all different.'),
('Arabic is never a machine translation of the English.','It is written, then the English is matched to it.'),
('Arabic carries more leading than Latin: 1.7 against 1.5.','Arabic has deeper descenders and optional diacritics. Latin leading crowds it and the marks collide with the line below. Equal leading on both scripts is the clearest tell of a layout built by someone who does not read Arabic.'),
('Layout direction is RTL on anything Arabic-primary.','Including column order, the side the logo sits on, and the direction a carousel reads.'),
('Western numerals throughout — 0123456789.','Not because one system is better. These layouts carry both scripts at once, and mixing numeral systems inside one design reads as a mistake. One rule removes a decision that otherwise gets made differently by every designer.'),
('Never stretch, skew or condense a wordmark.','The perspective on the mockups is the pack shape in a 3D render, not a distortion applied to the logo.')]
lis=''.join(f'<div class="bi"><b>{i+1} · {a}</b><p>{b}</p></div>' for i,(a,b) in enumerate(items))
page('', f'''<h3 class="ar">قواعد اللغتين</h3><h4>10 · Bilingual rules</h4>
<p class="lead">These are the ones that break layouts when they are ignored.</p>{lis}''','Bilingual rules')

# ---------- NEVER ----------
nev=[('Never recolour a brand colour to match a flavour.','The green BeBo banner stays green on every field. That is what makes five packs read as one brand.'),
('Never set white type on a field that fails contrast.','Eleven of the eighteen masters fail white. Check the table on page 12 before assuming.'),
('Never rebuild a wordmark in a font.','All four are artwork. Two of them are illustrated 3D lettering and cannot be retyped at all.'),
('Never use a colour outside the master set.','If it is not in this document it is not in the system, and the work is off-brand.'),
('Never use three weights in one layout.','Two. One headline, one for everything else.'),
('Never put POLEKA cola and strawberry in the same grid.','They share one field colour at ΔE 0.00 and read as one product at thumbnail size.'),
('Never mix Arabic-Indic and Western numerals.','Pick the rule, which is Western, and hold it everywhere.'),
('Never set Arabic at Latin leading.','1.7, not 1.5. The diacritics collide.')]
cards=''.join(f'<div class="nev"><div class="x">✕</div><div><b>{a}</b><p>{b}</p></div></div>' for a,b in nev)
page('', f'''<h3 class="ar">ممنوع</h3><h4>11 · Never do this</h4><div class="nevs">{cards}</div>''','Never do this')

# ---------- DEFECTS ----------
page('', f'''<h3 class="ar">عيوب معروفة</h3><h4>12 · Known defects in current packaging</h4>
<p class="lead">Recording these is part of the job. Changing printed artwork is not, and is quoted separately.</p>
<div class="def"><b>1 · The BeBo banner nearly disappears on the BeBo apple pack</b>
<div class="cmp"><div class="sw2" style="background:#2C8C3B"><div class="badge" style="background:#1BA34C;border:0.8mm solid #1E2A6B">BeBo</div></div>
<div class="sw2" style="background:#E4762A"><div class="badge" style="background:#1BA34C;border:0.8mm solid #1E2A6B">BeBo</div></div></div>
<p class="sm">Banner <span class="mono">#1BA34C</span> on the apple field <span class="mono">#2C8C3B</span> is <b>ΔE 7.62 at 1.30:1</b>, where every other flavour puts it 27 to 54 ΔE clear.</p><p class="sm"><b>The navy keyline is the only thing holding it together, which is why it is non-negotiable.</b></p></div>
<div class="def"><b>2 · POLEKA cola and strawberry are the same field colour</b>
<div class="cmp"><div class="sw2" style="background:#EC008C"><span class="lbl">Cola</span></div><div class="sw2" style="background:#EC008C"><span class="lbl">Strawberry</span></div></div>
<p class="sm"><b>ΔE 0.00.</b> Verified against the supplied artwork, and differentiated only by the character. At thumbnail size in a feed they are one product.</p><p class="sm"><b>Rule: never in the same grid, carousel or story sequence, and the character always leads the frame.</b></p></div>
<div class="def warn2"><b>3 · Trademark exposure on the POLEKA cola pouch</b>
<p class="sm">The pouch carries a photoreal contour bottle in red-and-white livery with near-identical Spencerian script. The bottle silhouette is protected trade dress independently of the wordmark. Under the retainer, <b>TSA's own advertising account carries this to a paid audience.</b></p>
<p class="sm"><b>Until rights are confirmed in writing, this SKU stays out of paid campaigns and out of copy.</b></p></div>''','Known defects')

# ---------- GOVERNANCE ----------
page('', f'''<h3 class="ar">الحوكمة</h3><h4>13 · Governance</h4>
<div class="two"><div>
<h5>Version</h5><p>This is <b>v1.0</b>, dated 18 September 2026. Every page carries the version in its footer, so a page found loose on a desk identifies itself.</p>
<h5>What triggers a new version</h5><p>A new brand or SKU · a change to a printed pack · original artwork files arriving, which would allow values to be re-sampled from source and reissued as v1.1 · a decision on whether the Alex seal extends to BeBo and POLEKA.</p>
<h5>Honest limits</h5><p class="sm">Values were sampled from supplied artwork rather than measured from printed packs or read from source files. The relationships between values are sound and the contrast verdicts hold, because those depend on the values as published here. <b>What is not guaranteed is that a published value matches the ink currently on a shelf.</b></p>
<p class="sm">From approval onward these values are the brand's colours and the packs are the legacy. That is the correct direction for a system nobody had written down before.</p>
</div><div>
<h5>Still open</h5>
<table class="mt sm"><tbody>
<tr><td>Vector logo files</td><td class="chip2 warn">PENDING</td></tr>
<tr><td>Seal rule: tiering or rollout</td><td class="chip2 warn">PENDING</td></tr>
<tr><td>Cola artwork rights</td><td class="chip2 warn">PENDING</td></tr>
<tr><td>Type licence confirmation</td><td class="chip2">TSA</td></tr></tbody></table>
<h5>Approval</h5>
<div class="sign"><p class="sm">This document is submitted for written approval. Approving it fixes the values above as the system of record for all four brands.</p>
<div class="sigline"><span>Name</span></div><div class="sigline"><span>Role</span></div><div class="sigline"><span>Date</span></div><div class="sigline"><span>Signature</span></div></div>
</div></div>''','Governance')

CSS = f'''
@page {{ size:210mm 297mm; margin:0; }}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:{PAPER};color:{INK};
 font-family:'Inter',sans-serif;
 -webkit-print-color-adjust:exact;print-color-adjust:exact;}}
.page{{width:210mm;height:297mm;padding:20mm 20mm 26mm;position:relative;overflow:hidden;
 background:{PAPER};page-break-after:always;break-after:page;}}
.page:last-child{{page-break-after:auto}}
footer{{position:absolute;left:20mm;right:20mm;bottom:12mm;display:flex;justify-content:space-between;
 align-items:center;font-size:6.5pt;color:{SLATE};letter-spacing:.14em;text-transform:uppercase;
 font-weight:600;border-top:0.25mm solid {SILVER};padding-top:2.5mm}}
footer .fm{{display:flex;align-items:center;gap:1.6mm}}
footer .fm i{{display:block;width:1mm;height:3.4mm;background:{RED}}}
footer .fm b{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:9pt;
 letter-spacing:.04em;color:{INK}}}
h3.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;font-size:24pt;font-weight:600;margin:0;
 direction:rtl;text-align:right;line-height:1.3;color:{INK}}}
h4{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:16pt;color:{INK};
 margin:1mm 0 7mm;letter-spacing:.01em;text-transform:uppercase;
 border-bottom:0.6mm solid {RED};padding-bottom:3mm}}
h5{{font-family:'Inter',sans-serif;font-size:7pt;font-weight:600;margin:6mm 0 2.5mm;
 letter-spacing:.2em;text-transform:uppercase;color:{RED}}}
p{{font-size:9.5pt;line-height:1.55;margin:0 0 3mm}}
p.lead{{font-size:11pt;line-height:1.5}}
p.sm,.sm{{font-size:8.5pt;line-height:1.5}}
.xs{{font-size:6pt}} p.fn{{font-size:7.5pt;color:{SLATE};margin-top:4mm}}
.mono{{font-family:'IBM Plex Mono',monospace}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:10mm}}
table.mt{{width:100%;border-collapse:collapse;margin:2mm 0}}
table.mt th{{font-size:6.5pt;text-transform:uppercase;letter-spacing:.2em;color:{SLATE};text-align:left;
 font-weight:600;padding:0 2mm 2mm 0;border-bottom:0.25mm solid {SILVER}}}
table.mt td{{padding:1.8mm 2mm 1.8mm 0;border-bottom:0.2mm solid {MIST};vertical-align:middle;font-size:9pt}}
table.mt.xs2 td{{padding:1.2mm 1mm 1.2mm 0}}
td.cell{{width:12mm}} .chipsw{{width:10mm;height:7mm;border-radius:0.6mm}}
.chipsw.sm2{{width:9mm;height:5.5mm}} td.rc{{text-align:left}} td.rc .xs{{display:block;color:{SLATE};margin-top:.6mm}}
span.ar{{display:block;direction:rtl;color:{SLATE};font-size:8pt}}
.tpass{{color:#17592F}} .thead{{color:#B87C0E}} .tfail{{color:#AC211B}}
.rule{{border-right:1.2mm solid {RED};background:{MIST};padding:4mm 5mm;margin:5mm 0}}
.rule.alt{{border-right-color:{SURF}}} .rule.big b{{font-size:11.5pt;line-height:1.35;display:block;margin-bottom:2mm}}
.rule > b{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:12pt;letter-spacing:.01em;display:block;margin-bottom:1.5mm}} .rule p{{margin:2mm 0 0;font-size:8.5pt}}
.layers{{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-bottom:2mm}}
.lay{{border:0.25mm solid {SILVER};padding:4mm;border-radius:1mm}}
.lay b{{font-size:9.5pt;display:block;margin-bottom:1.5mm}} .lay p{{font-size:8.5pt;margin:0 0 1.5mm}}
.flav{{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm;margin:2mm 0 0}}
.sw{{border-radius:1mm;padding:2.5mm;display:flex;flex-direction:column;justify-content:space-between;font-size:7.5pt;font-weight:600}}
.hexl{{font-family:'IBM Plex Mono',monospace;font-size:6.5pt;opacity:.9}}
.spec{{margin:5mm 0;border-top:0.25mm solid {SILVER};border-bottom:0.25mm solid {SILVER};padding:4mm 0}}
.sp400{{font-size:17pt;font-weight:400;margin-bottom:2mm;direction:rtl;text-align:right}}
.sp600{{font-size:17pt;font-weight:600;margin-bottom:2mm;direction:rtl;text-align:right}}
.sp700{{font-size:17pt;font-weight:700;margin-bottom:2mm;direction:rtl;text-align:right}}
.spm{{font-family:'IBM Plex Mono',monospace;font-size:12pt;color:{GRAPHITE}}}
.bi{{border-top:0.25mm solid {MIST};padding:3mm 0}} .bi b{{font-size:9.5pt}} .bi p{{font-size:8.5pt;margin:1mm 0 0;color:{GRAPHITE}}}
.nevs{{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}}
.nev{{display:flex;gap:3mm;border:0.25mm solid {SILVER};padding:3.5mm;border-radius:1mm}}

.nev .x{{color:{RED};font-weight:700;font-size:12pt;line-height:1}}
.nev b{{font-size:8.5pt;display:block}} .nev p{{font-size:7.5pt;margin:1mm 0 0;color:{GRAPHITE}}}
.def{{border:0.25mm solid {SILVER};padding:4mm;margin-bottom:4mm;border-radius:1mm}}
.def.warn2{{border-color:{RED};border-width:0.4mm}}
.def > b{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:12pt;display:block;margin-bottom:2.5mm}}
.cmp{{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-bottom:2.5mm}}
.sw2{{height:26mm;border-radius:1mm;display:flex;align-items:center;justify-content:center}}
.badge{{background:#1BA34C;color:#fff;font-weight:700;font-size:10pt;padding:2mm 5mm;border-radius:4mm}}
.lbl{{color:#fff;font-weight:600;font-size:9pt}}
chip-x{{}}
.chip{{display:inline-block;background:{INK};color:{PAPER};font-size:7pt;letter-spacing:.08em;
 padding:1.5mm 3mm;border-radius:0.8mm;font-family:'IBM Plex Mono',monospace;margin-top:4mm}}
.chip.warn{{background:{RED}}} .chip2{{font-size:7pt;font-family:'IBM Plex Mono',monospace;color:{SLATE}}}
.chip2.warn{{color:#B87C0E;font-weight:600}}
table.toc td{{font-size:8.5pt;padding:1.4mm 2mm 1.4mm 0;border-bottom:0.2mm solid {MIST}}}
table.toc td:first-child{{width:6mm;color:{SLATE};font-family:'IBM Plex Mono',monospace}}
table.toc td:last-child{{text-align:right;color:{SLATE};font-family:'IBM Plex Mono',monospace}}
.sign{{border:0.25mm solid {SILVER};padding:4mm;border-radius:1mm;margin-top:3mm}}
.sigline{{border-bottom:0.25mm solid {SLATE};height:9mm;margin-top:5mm;position:relative}}
.sigline span{{position:absolute;bottom:1mm;font-size:7pt;color:{SLATE};font-family:'IBM Plex Mono',monospace}}
/* cover */
.page.cover{{padding:0;background:{INK}}}
.cov{{height:100%;display:flex;flex-direction:column;padding:22mm 20mm 0;color:{PAPER}}}
.lockup{{display:flex;align-items:center;gap:3mm}}
.lockup i{{display:block;width:2.2mm;height:8mm;background:{RED}}}
.lockup span{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:14pt;
 letter-spacing:.03em;color:{PAPER}}}
.covmid{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.eyebrow{{font-family:'Inter',sans-serif;font-weight:600;font-size:7pt;letter-spacing:.2em;
 text-transform:uppercase;color:{RED};margin-bottom:6mm}}
.covmid h1{{font-family:'IBM Plex Sans Arabic',sans-serif;font-size:46pt;font-weight:600;margin:0;
 direction:rtl;text-align:right;line-height:1.2;color:{PAPER}}}
.covmid h2{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:40pt;margin:2mm 0 0;
 color:{PAPER};letter-spacing:.02em}}
.covsub{{margin-top:8mm;font-size:8.5pt;color:{SILVER};letter-spacing:.06em}}
.covbot{{padding-bottom:0}}
.meta{{display:flex;gap:8mm;font-size:7pt;color:{SLATE};letter-spacing:.12em;
 text-transform:uppercase;font-weight:600;margin-bottom:5mm}}
.tag{{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:19pt;
 color:{PAPER};margin-bottom:16mm}}
.tag em{{font-style:normal;color:{RED}}}
.bands{{position:absolute;left:0;right:0;bottom:0;height:9mm;
 background:linear-gradient(90deg,#1BA34C 0 25%,#29ABE2 25% 50%,#EC008C 50% 75%,#FFC20E 75% 100%);
 -webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page.cover footer{{display:none}}
'''
html=f'''<!doctype html><html lang="en" dir="ltr"><head><meta charset="utf-8">
<title>Alex Foods — Design System v1.0</title><link rel="stylesheet" href="plex.css"><link rel="stylesheet" href="tsa.css">
<style>{CSS}</style></head><body>{''.join(H)}</body></html>'''
io.open(os.path.join(HERE,'ds.html'),'w',encoding='utf-8').write(html)
print("pages:",PAGES[0])
