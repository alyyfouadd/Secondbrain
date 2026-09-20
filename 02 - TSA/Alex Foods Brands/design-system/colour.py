import math, itertools

def hx(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def hs(t): return '#%02X%02X%02X'%tuple(max(0,min(255,round(c))) for c in t)

def srgb_lin(c):
    c/=255.0
    return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4

def lum(h):
    r,g,b=[srgb_lin(c) for c in hx(h)]
    return 0.2126*r+0.7152*g+0.0722*b

def ratio(a,b):
    la,lb=lum(a),lum(b)
    if la<lb: la,lb=lb,la
    return (la+0.05)/(lb+0.05)

def lab(h):
    r,g,b=[srgb_lin(c) for c in hx(h)]
    X=r*0.4124564+g*0.3575761+b*0.1804375
    Y=r*0.2126729+g*0.7151522+b*0.0721750
    Z=r*0.0193339+g*0.1191920+b*0.9503041
    Xn,Yn,Zn=0.95047,1.0,1.08883
    def f(t): return t**(1/3) if t>216/24389 else (841/108)*t+4/29
    fx,fy,fz=f(X/Xn),f(Y/Yn),f(Z/Zn)
    return (116*fy-16, 500*(fx-fy), 200*(fy-fz))

def de2000(h1,h2):
    L1,a1,b1=lab(h1); L2,a2,b2=lab(h2)
    kL=kC=kH=1.0
    C1=math.hypot(a1,b1); C2=math.hypot(a2,b2); Cb=(C1+C2)/2
    G=0.5*(1-math.sqrt(Cb**7/(Cb**7+25**7))) if Cb>0 else 0.5
    a1p=(1+G)*a1; a2p=(1+G)*a2
    C1p=math.hypot(a1p,b1); C2p=math.hypot(a2p,b2)
    h1p=math.degrees(math.atan2(b1,a1p))%360 if (a1p or b1) else 0
    h2p=math.degrees(math.atan2(b2,a2p))%360 if (a2p or b2) else 0
    dLp=L2-L1; dCp=C2p-C1p
    if C1p*C2p==0: dhp=0
    elif abs(h2p-h1p)<=180: dhp=h2p-h1p
    elif h2p-h1p>180: dhp=h2p-h1p-360
    else: dhp=h2p-h1p+360
    dHp=2*math.sqrt(C1p*C2p)*math.sin(math.radians(dhp)/2)
    Lbp=(L1+L2)/2; Cbp=(C1p+C2p)/2
    if C1p*C2p==0: hbp=h1p+h2p
    elif abs(h1p-h2p)<=180: hbp=(h1p+h2p)/2
    elif h1p+h2p<360: hbp=(h1p+h2p+360)/2
    else: hbp=(h1p+h2p-360)/2
    T=(1-0.17*math.cos(math.radians(hbp-30))+0.24*math.cos(math.radians(2*hbp))
       +0.32*math.cos(math.radians(3*hbp+6))-0.20*math.cos(math.radians(4*hbp-63)))
    dTh=30*math.exp(-(((hbp-275)/25)**2))
    Rc=2*math.sqrt(Cbp**7/(Cbp**7+25**7)) if Cbp>0 else 0
    Sl=1+(0.015*(Lbp-50)**2)/math.sqrt(20+(Lbp-50)**2)
    Sc=1+0.045*Cbp; Sh=1+0.015*Cbp*T
    Rt=-math.sin(math.radians(2*dTh))*Rc
    return math.sqrt((dLp/(kL*Sl))**2+(dCp/(kC*Sc))**2+(dHp/(kH*Sh))**2
                     +Rt*(dCp/(kC*Sc))*(dHp/(kH*Sh)))

# sanity checks
print("SANITY  identical:%.2f  white/black:%.1f  (expect 0.00 and ~100)"
      % (de2000('#1BA34C','#1BA34C'), de2000('#FFFFFF','#000000')))
print("SANITY  contrast white/black: %.2f (expect 21.00)" % ratio('#FFFFFF','#000000'))

C = {
 'BeBo banner green':'#1BA34C','BeBo outline navy':'#1E2A6B','BeBo flash red':'#E1251D',
 'BeBo peach':'#E4762A','BeBo mango':'#F2A00C','BeBo apple':'#2C8C3B','BeBo cola':'#1C74BC','BeBo pineapple':'#C6D42E',
 'AlRawy navy':'#1B4F9C','AlRawy accent red':'#E1251B','AlRawy ribbon light':'#8CC63F','AlRawy ribbon deep':'#5EA818',
 'AlRawy cocktail':'#D6006E','AlRawy apple':'#00A3E0','AlRawy guava':'#009A44','AlRawy peach':'#E03127','AlRawy mango':'#F07F13',
 '2MAN ice blue':'#29ABE2','2MAN yellow':'#FFC20E','2MAN pink':'#EC008C','2MAN green':'#8DC63F','2MAN blue':'#2E3192',
 'POLEKA pink':'#EC008C','POLEKA purple':'#92278F','POLEKA green':'#8DC63F','POLEKA yellow':'#FFC20E','POLEKA blue':'#29ABE2',
 'POLEKA apple':'#00A651','POLEKA mango':'#FFF200','POLEKA cola':'#EC008C','POLEKA strawberry':'#EC008C',
}

print("\n=== PAIRS UNDER dE2000 5.0 (candidates to collapse) ===")
for (n1,v1),(n2,v2) in itertools.combinations(C.items(),2):
    d=de2000(v1,v2)
    if d<5.0:
        print("  %-22s %s  vs  %-22s %s   dE=%5.2f%s"%(n1,v1,n2,v2,d," IDENTICAL" if v1==v2 else ""))
