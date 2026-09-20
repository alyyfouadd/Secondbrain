import re, sys, zlib, math

def cmyk_hex(c,m,y,k):
    return "#%02X%02X%02X"%tuple(round(255*(1-v)*(1-k)) for v in (c,m,y))

def mul(a,b):
    return [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3],
            a[4]*b[0]+a[5]*b[2]+b[4], a[4]*b[1]+a[5]*b[3]+b[5]]
def ap(m,x,y): return (m[0]*x+m[2]*y+m[4], m[1]*x+m[3]*y+m[5])

def convert(content, H):
    toks=re.findall(rb"/[^\s/\[\]<>(){}]+|[-+]?[0-9]*\.?[0-9]+|[A-Za-z*]+", content)
    ctm=[1,0,0,1,0,0]; stack=[]
    fill="#000000"; stroke="#000000"; lw=1.0
    out=[]; d=[]; cur=(0,0); start=(0,0); ops=[]; pend_clip=False
    def P(x,y):
        X,Y=ap(ctm,x,y); return "%.4f %.4f"%(X,H-Y)
    def scale():
        return math.sqrt(abs(ctm[0]*ctm[3]-ctm[1]*ctm[2])) or 1.0
    def emit(do_fill, do_stroke, eo):
        if not d: return
        a=[]
        a.append('fill="%s"'%fill if do_fill else 'fill="none"')
        if eo and do_fill: a.append('fill-rule="evenodd"')
        if do_stroke:
            a.append('stroke="%s"'%stroke)
            a.append('stroke-width="%.4f"'%(lw*scale()))
        out.append('<path d="%s" %s/>'%(" ".join(d)," ".join(a)))
    for t in toks:
        s=t.decode('latin-1')
        if re.fullmatch(r"[-+]?[0-9]*\.?[0-9]+", s): ops.append(float(s)); continue
        if s.startswith("/"): ops.append(s); continue
        op=s
        if op=="q": stack.append((ctm[:],fill,stroke,lw))
        elif op=="Q":
            if stack: ctm,fill,stroke,lw = stack.pop(); ctm=ctm[:]
        elif op=="cm" and len(ops)>=6: ctm=mul(ops[-6:],ctm)
        elif op=="w" and ops: lw=ops[-1]
        elif op=="m" and len(ops)>=2: cur=(ops[-2],ops[-1]); start=cur; d.append("M "+P(*cur))
        elif op=="l" and len(ops)>=2: cur=(ops[-2],ops[-1]); d.append("L "+P(*cur))
        elif op=="c" and len(ops)>=6:
            a=ops[-6:]; d.append("C "+P(a[0],a[1])+" "+P(a[2],a[3])+" "+P(a[4],a[5])); cur=(a[4],a[5])
        elif op=="v" and len(ops)>=4:
            a=ops[-4:]; d.append("C "+P(*cur)+" "+P(a[0],a[1])+" "+P(a[2],a[3])); cur=(a[2],a[3])
        elif op=="y" and len(ops)>=4:
            a=ops[-4:]; d.append("C "+P(a[0],a[1])+" "+P(a[2],a[3])+" "+P(a[2],a[3])); cur=(a[2],a[3])
        elif op=="h": d.append("Z"); cur=start
        elif op=="re" and len(ops)>=4:
            x,y,w,h=ops[-4:]
            d.append("M "+P(x,y)+" L "+P(x+w,y)+" L "+P(x+w,y+h)+" L "+P(x,y+h)+" Z")
        elif op=="k" and len(ops)>=4: fill=cmyk_hex(*ops[-4:])
        elif op=="K" and len(ops)>=4: stroke=cmyk_hex(*ops[-4:])
        elif op=="g" and ops: v=round(255*ops[-1]); fill="#%02X%02X%02X"%(v,v,v)
        elif op=="G" and ops: v=round(255*ops[-1]); stroke="#%02X%02X%02X"%(v,v,v)
        elif op=="rg" and len(ops)>=3: fill="#%02X%02X%02X"%tuple(round(255*v) for v in ops[-3:])
        elif op=="RG" and len(ops)>=3: stroke="#%02X%02X%02X"%tuple(round(255*v) for v in ops[-3:])
        elif op in ("W","W*"): pend_clip=True
        elif op in ("f","F","f*"): emit(True,False,"*" in op); d=[]; pend_clip=False
        elif op in ("S","s"):
            if op=="s": d.append("Z")
            emit(False,True,False); d=[]; pend_clip=False
        elif op in ("B","B*","b","b*"):
            if op.startswith("b"): d.append("Z")
            emit(True,True,"*" in op); d=[]; pend_clip=False
        elif op=="n": d=[]; pend_clip=False
        if op: ops=[]
    return out

d=open("LOGO.pdf","rb").read()
objs={}
for m in re.finditer(rb"(\d+)\s+(\d+)\s+obj(.*?)endobj", d, re.S): objs[int(m.group(1))]=m.group(3)
content=b""
for n in [7,8,9,10,11,12,13,14]:
    b=objs[n]; st=b.find(b"stream"); e=b.rfind(b"endstream")
    content+=zlib.decompress(b[st+6:e].lstrip(b"\r\n"))
H=451.957
paths=convert(content,H)
print("paths:",len(paths), "(expect 114 fills + 2 strokes = 116)", file=sys.stderr)
# true bbox
nums=[]
for p in paths:
    dd=re.search(r'd="([^"]+)"',p).group(1)
    nums += [(float(a),float(b)) for a,b in re.findall(r"(-?[\d.]+) (-?[\d.]+)", dd)]
xs=[p[0] for p in nums]; ys=[p[1] for p in nums]
x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
pad=1.0
vb="%.3f %.3f %.3f %.3f"%(x0-pad,y0-pad,(x1-x0)+2*pad,(y1-y0)+2*pad)
print("bbox %.3f %.3f %.3f %.3f -> viewBox %s"%(x0,y0,x1,y1,vb), file=sys.stderr)
hdr=('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" width="%.0f" height="%.0f" '
     'role="img" aria-label="Alex Foods">\n<title>Alex Foods master seal</title>\n'%(vb,(x1-x0)+2*pad,(y1-y0)+2*pad))
open("alex-seal.svg","w").write(hdr+"\n".join(paths)+"\n</svg>\n")
