import zlib,struct,sys
def rows(path):
    d=open(path,"rb").read(); pos=8; idat=b""
    while pos<len(d):
        ln=struct.unpack(">I",d[pos:pos+4])[0]; typ=d[pos+4:pos+8]
        if typ==b"IHDR": w,h,bd,ct=struct.unpack(">IIBB",d[pos+8:pos+18])
        if typ==b"IDAT": idat+=d[pos+8:pos+8+ln]
        pos+=12+ln
    raw=zlib.decompress(idat); ch=4 if ct==6 else 3; stride=w*ch
    out=[]; prev=bytearray(stride); i=0
    for y in range(h):
        f=raw[i]; i+=1; line=bytearray(raw[i:i+stride]); i+=stride
        for x in range(stride):
            a=line[x-ch] if x>=ch else 0; b=prev[x]; c=prev[x-ch] if x>=ch else 0
            if f==1: line[x]=(line[x]+a)&255
            elif f==2: line[x]=(line[x]+b)&255
            elif f==3: line[x]=(line[x]+(a+b)//2)&255
            elif f==4:
                p=a+b-c; pa,pb,pc=abs(p-a),abs(p-b),abs(p-c)
                pr=a if (pa<=pb and pa<=pc) else (b if pb<=pc else c)
                line[x]=(line[x]+pr)&255
        out.append(bytes(line)); prev=line
    return out,w,h,ch
def px(r,x,ch): return (r[x*ch],r[x*ch+1],r[x*ch+2])
