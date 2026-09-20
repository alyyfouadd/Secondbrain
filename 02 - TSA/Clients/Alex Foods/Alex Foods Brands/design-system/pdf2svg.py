# -*- coding: utf-8 -*-
# Minimal PDF vector path extractor -> SVG.
# Written for the Alex Foods LOGO.pdf, which is pure vector: no images, no
# fonts, and only the path operators m l c v y re h, the painting operators
# f f* B b S n, the state operators q Q cm, and CMYK fills via k.
# Not a general PDF renderer. It handles exactly what that file uses.
import re, zlib, sys, io

def cmyk(c,m,y,k):
    r=round(255*(1-min(1,c+k))); g=round(255*(1-min(1,m+k))); b=round(255*(1-min(1,y+k)))
    return '#%02X%02X%02X'%(max(0,r),max(0,g),max(0,b))

def mul(a,b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3],
            a[4]*b[0]+a[5]*b[2]+b[4], a[4]*b[1]+a[5]*b[3]+b[5])

def apply(m,x,y): return (m[0]*x+m[2]*y+m[4], m[1]*x+m[3]*y+m[5])

def convert(path, out):
    d=open(path,'rb').read()
    mb=re.search(rb'/MediaBox\s*\[([^\]]*)\]',d)
    W,Hh=595.276,451.957
    if mb:
        v=[float(x) for x in mb.group(1).split()]
        W,Hh=v[2]-v[0], v[3]-v[1]
    streams=[]
    for mm in re.finditer(rb'stream\r?\n',d):
        s=mm.end(); e=d.find(b'endstream',s)
        if e<0: continue
        try: raw=zlib.decompress(d[s:e])
        except Exception: continue
        if re.search(rb'[\s](?:m|c|l)[\s]',raw): streams.append(raw)
    # Document order, never size order: fill colour is graphics state and
    # reordering streams loses it. Cost one wrong-coloured swoosh to learn.
    body=[]; carry=['#000000']
    for raw in streams:
        t=raw.decode('latin-1')
        toks=re.findall(r'[-\d\.]+|[A-Za-z\*\'\"]+', t)
        st=[]; ctm=(1,0,0,1,0,0); args=[]
        fill=carry[0]
        seg=[]; cur=(0,0); start=(0,0)
        for tk in toks:
            if re.match(r'^[-\d\.]+$',tk):
                try: args.append(float(tk))
                except ValueError: args=[]
                continue
            op=tk
            if op=='q': st.append((ctm,fill))
            elif op=='Q':
                if st: ctm,fill=st.pop()
            elif op=='cm' and len(args)>=6:
                ctm=mul(tuple(args[-6:]),ctm)
            elif op=='k' and len(args)>=4:
                fill=cmyk(*args[-4:])
            elif op=='g' and len(args)>=1:
                v=round(255*args[-1]); fill='#%02X%02X%02X'%(v,v,v)
            elif op=='rg' and len(args)>=3:
                fill='#%02X%02X%02X'%tuple(round(255*x) for x in args[-3:])
            elif op=='m' and len(args)>=2:
                cur=apply(ctm,args[-2],args[-1]); start=cur
                seg.append('M%.2f %.2f'%cur)
            elif op=='l' and len(args)>=2:
                cur=apply(ctm,args[-2],args[-1]); seg.append('L%.2f %.2f'%cur)
            elif op=='c' and len(args)>=6:
                p1=apply(ctm,args[-6],args[-5]); p2=apply(ctm,args[-4],args[-3]); p3=apply(ctm,args[-2],args[-1])
                seg.append('C%.2f %.2f %.2f %.2f %.2f %.2f'%(p1+p2+p3)); cur=p3
            elif op=='v' and len(args)>=4:
                p2=apply(ctm,args[-4],args[-3]); p3=apply(ctm,args[-2],args[-1])
                seg.append('C%.2f %.2f %.2f %.2f %.2f %.2f'%(cur+p2+p3)); cur=p3
            elif op=='y' and len(args)>=4:
                p1=apply(ctm,args[-4],args[-3]); p3=apply(ctm,args[-2],args[-1])
                seg.append('C%.2f %.2f %.2f %.2f %.2f %.2f'%(p1+p3+p3)); cur=p3
            elif op=='re' and len(args)>=4:
                x,y,w,h=args[-4:]
                pts=[apply(ctm,x,y),apply(ctm,x+w,y),apply(ctm,x+w,y+h),apply(ctm,x,y+h)]
                seg.append('M%.2f %.2f L%.2f %.2f L%.2f %.2f L%.2f %.2f Z'%(pts[0]+pts[1]+pts[2]+pts[3]))
            elif op=='h':
                seg.append('Z'); cur=start
            elif op in ('f','f*','F','B','b','b*','B*'):
                if seg:
                    rule=' fill-rule="evenodd"' if '*' in op else ''
                    body.append(f'<path d="{" ".join(seg)}" fill="{fill}"{rule}/>')
                seg=[]
            elif op in ('S','s','n'):
                seg=[]
            args=[]
        carry[0]=fill
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {Hh:.2f}" width="{W:.0f}" height="{Hh:.0f}">'
         f'<g transform="translate(0,{Hh:.2f}) scale(1,-1)">{"".join(body)}</g></svg>')
    io.open(out,'w',encoding='utf-8').write(svg)
    return len(body), W, Hh

if __name__=='__main__':
    n,w,h=convert(sys.argv[1], sys.argv[2])
    print(f'paths: {n} | {w:.0f} x {h:.0f} pt')
