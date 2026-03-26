KW=1.0e-14
def sq(x):return x**0.5
def fl(x):
 n=int(x)
 if float(n)>x:n-=1
 return n
def l10(x):
 y=0
 while x>=10:x/=10;y+=1
 while x<1:x*=10;y-=1
 a=0.0;b=1.0
 for i in range(20):
  m=(a+b)/2
  if 10**m<=x:a=m
  else:b=m
 return y+(a+b)/2
def fmt(v):
 if v==0:return "0"
 e=int(fl(l10(abs(v))))
 return str(round(v/10**e,3))+"e"+str(e)
def clr():print("\n"*10)
def hdr(t):
 clr()
 print("-"*26)
 print(t)
 print("-"*26)
def pa():input("Enter...")
def gf(p):
 try:return float(input(p))
 except:print("Err");pa();return None
def qd(a,b,c):
 d=b*b-4*a*c
 if d<0:return None
 r=(-b+sq(d))/(2*a)
 if r>0:return r
 return(-b-sq(d))/(2*a)
def sa(ph):
 po=14-ph;h=10**-ph;o=10**-po
 print("pH ="+str(round(ph,4)))
 print("pOH="+str(round(po,4)))
 print("[H+]="+fmt(h))
 print("[OH-]="+fmt(o))
def phb():
 while True:
  hdr("pH/pOH")
  print("1.[H+]->pH 2.pH")
  print("3.[OH-]  4.pOH")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   v=gf("[H+]M:")
   if v is None or v<=0:pa();continue
   sa(-l10(v));pa()
  elif ch=="2":
   v=gf("pH:")
   if v is None:pa();continue
   sa(v);pa()
  elif ch=="3":
   v=gf("[OH-]M:")
   if v is None or v<=0:pa();continue
   sa(14+l10(v));pa()
  elif ch=="4":
   v=gf("pOH:")
   if v is None:pa();continue
   sa(14-v);pa()
def stra():
 hdr("Strong Acids")
 c=gf("Conc M:")
 if c is None or c<=0:pa();return
 if c<1e-7:h=(c+sq(c*c+4*KW))/2
 else:h=c
 sa(-l10(h));pa()
def strb():
 while True:
  hdr("Strong Bases")
  print("1.Mono(NaOH)")
  print("2.Di(Ca(OH)2)")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1" or ch=="2":
   c=gf("Conc M:")
   if c is None or c<=0:pa();continue
   oh=c if ch=="1" else 2*c
   if oh<1e-7:oh=(oh+sq(oh*oh+4*KW))/2
   sa(14+l10(oh));pa()
def wka():
 while True:
  hdr("Weak Acids")
  print("1.pH  2.%Ion  0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1" or ch=="2":
   ka=gf("Ka:");c=gf("[HA]M:")
   if ka is None or c is None or ka<=0 or c<=0:pa();continue
   x=qd(1,ka,-ka*c)
   if x is None or x<=0:print("Err");pa();continue
   sa(-l10(x))
   if ch=="2":print("%="+str(round(x/c*100,2)))
   print("Aprx:"+fmt(sq(ka*c)))
   pa()
def wkb():
 while True:
  hdr("Weak Bases")
  print("1.pH  2.%Ion  0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1" or ch=="2":
   kb=gf("Kb:");c=gf("[B]M:")
   if kb is None or c is None or kb<=0 or c<=0:pa();continue
   x=qd(1,kb,-kb*c)
   if x is None or x<=0:print("Err");pa();continue
   sa(14+l10(x))
   if ch=="2":print("%="+str(round(x/c*100,2)))
   pa()
def buf():
 while True:
  hdr("Buffers")
  print("1.H-H 2.+Acid 3.+Base")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   ka=gf("Ka:");a=gf("[A-]M:");ha=gf("[HA]M:")
   if ka is None or a is None or ha is None:pa();continue
   if ka<=0 or a<=0 or ha<=0:pa();continue
   pk=-l10(ka)
   print("pKa="+str(round(pk,4)))
   print("pH="+str(round(pk+l10(a/ha),4)))
   pa()
  elif ch=="2" or ch=="3":
   ka=gf("Ka:");ac=gf("[A-]M:");hc=gf("[HA]M:")
   vb=gf("BufVolL:");cc=gf("AddCM:");va=gf("AddVL:")
   if ka is None or ac is None or hc is None:pa();continue
   if vb is None or cc is None or va is None:pa();continue
   if ka<=0 or ac<=0 or hc<=0 or vb<=0 or cc<=0 or va<=0:pa();continue
   pk=-l10(ka);ma=ac*vb;mh=hc*vb;mx=cc*va;vt=vb+va
   if ch=="2":na=ma-mx;nh=mh+mx
   else:na=ma+mx;nh=mh-mx
   if na<=0:print("Exceeded!");print("pH="+str(round(-l10(-na/vt),4)))
   elif nh<=0:print("Exceeded!");print("pH="+str(round(14+l10(-nh/vt),4)))
   else:print("pH="+str(round(pk+l10(na/nh),4)))
   pa()
def tsas():
 hdr("SA+SB Titration")
 ca=gf("Ca M:");va=gf("Va L:")
 cb=gf("Cb M:");vb=gf("Vb L:")
 if ca is None or va is None or cb is None or vb is None:return
 if ca<=0 or va<=0 or cb<=0 or vb<0:pa();return
 ve=ca*va/cb;vt=va+vb
 print("Vep="+str(round(ve*1000,2))+"mL")
 if abs(vb-ve)<1e-9:print("EP:pH=7")
 elif vb<ve:print("pH="+str(round(-l10((ca*va-cb*vb)/vt),4)))
 else:print("pH="+str(round(14+l10((cb*vb-ca*va)/vt),4)))
 pa()
def twas():
 hdr("WA+SB Titration")
 ka=gf("Ka:");ca=gf("Ca M:");va=gf("Va L:")
 cb=gf("Cb M:");vb=gf("Vb L:")
 if ka is None or ca is None or va is None or cb is None or vb is None:return
 if ka<=0 or ca<=0 or va<=0 or cb<=0 or vb<0:pa();return
 pk=-l10(ka);ve=ca*va/cb;vt=va+vb
 print("Vep="+str(round(ve*1000,2))+"mL pKa="+str(round(pk,4)))
 if vb==0:
  x=qd(1,ka,-ka*ca)
  print("pH="+str(round(-l10(x),4)))
 elif abs(vb-ve/2)<1e-9:
  print("Half-EP pH=pKa="+str(round(pk,4)))
 elif abs(vb-ve)<1e-9:
  kc=KW/ka;cn=ca*va/vt
  x=qd(1,kc,-kc*cn)
  if x is None or x<=0:print("Err");pa();return
  print("EP(basic)pH="+str(round(14+l10(x),4)))
 elif vb<ve:
  print("Buf pH="+str(round(pk+l10(cb*vb/(ca*va-cb*vb)),4)))
 else:
  print("pH="+str(round(14+l10((cb*vb-ca*va)/vt),4)))
 pa()
def tit():
 while True:
  hdr("Titrations")
  print("1.SA+SB  2.WA+SB")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":tsas()
  elif ch=="2":twas()
def kakb():
 while True:
  hdr("Ka/Kb  Ka*Kb=1e-14")
  print("1.Ka->Kb 2.Kb->Ka")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   ka=gf("Ka:")
   if ka is None or ka<=0:pa();continue
   kb=KW/ka
   print("Kb="+fmt(kb))
   print("pKa="+str(round(-l10(ka),4)))
   print("pKb="+str(round(-l10(kb),4)))
   print("pKa+pKb=14")
   pa()
  elif ch=="2":
   kb=gf("Kb:")
   if kb is None or kb<=0:pa();continue
   ka=KW/kb
   print("Ka="+fmt(ka))
   print("pKa="+str(round(-l10(ka),4)))
   print("pKb="+str(round(-l10(kb),4)))
   pa()
def ref():
 hdr("Ka/Kb Ref")
 print("HF    6.8e-4 3.17")
 print("HAc   1.8e-5 4.74")
 print("H2CO3 4.3e-7 6.37")
 print("HCN   6.2e-10 9.21")
 print("NH4+  5.6e-10 9.25")
 print("NH3   Kb=1.8e-5")
 pa()
 hdr("Formulas")
 print("pH=-log[H+]")
 print("pH+pOH=14")
 print("Ka*Kb=1e-14")
 print("H-H: pH=pKa+log(r)")
 print("Vep=CaVa/Cb")
 print("Half-EP: pH=pKa")
 print("At EP(wkA): pH>7")
 pa()
def main():
 while True:
  hdr("AP Chem U8")
  print("1.pH/pOH  2.StrAcid")
  print("3.StrBase 4.WkAcid")
  print("5.WkBase  6.Buffer")
  print("7.Titrate 8.Ka/Kb")
  print("9.Ref     0.Quit")
  ch=input(":")
  if ch=="0":clr();print("Good luck!");break
  elif ch=="1":phb()
  elif ch=="2":stra()
  elif ch=="3":strb()
  elif ch=="4":wka()
  elif ch=="5":wkb()
  elif ch=="6":buf()
  elif ch=="7":tit()
  elif ch=="8":kakb()
  elif ch=="9":ref()
  else:print("?");pa()
main()
