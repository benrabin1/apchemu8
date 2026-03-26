KW=1.0e-14
def sq(x):
 return x**0.5
def fl(x):
 n=int(x)
 if float(n)>x:n=n-1
 return n
def l10(x):
 y=0
 while x>=10.0:
  x=x/10.0
  y=y+1
 while x<1.0:
  x=x*10.0
  y=y-1
 a=0.0
 b=1.0
 for i in range(30):
  m=(a+b)*0.5
  if 10.0**m<=x:a=m
  else:b=m
 return float(y)+(a+b)*0.5
def fmt(v):
 if v==0:return "0"
 e=int(fl(l10(abs(v))))
 m=v/(10.0**e)
 return str(round(m,3))+"e"+str(e)
def clr():print("\n"*10)
def hdr(t):
 clr()
 print("-"*26)
 print(t)
 print("-"*26)
def pa():input("Enter...")
def gf(p):
 try:return float(input(p))
 except:
  print("Bad input")
  pa()
  return None
def qd(a,b,c):
 d=b*b-4.0*a*c
 if d<0:return None
 r1=(-b+sq(d))/(2.0*a)
 r2=(-b-sq(d))/(2.0*a)
 if r1>0:return r1
 return r2
def sa(ph):
 po=14.0-ph
 h=10.0**(-ph)
 o=10.0**(-po)
 print("pH ="+str(round(ph,4)))
 print("pOH="+str(round(po,4)))
 print("[H+]="+fmt(h)+"M")
 print("[OH-]="+fmt(o)+"M")
def phb():
 while True:
  hdr("pH/pOH Basics")
  print("1.[H+]->pH")
  print("2.pH->[H+]")
  print("3.[OH-]->pH")
  print("4.pOH->pH")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   v=gf("[H+] M:")
   if v is None or v<=0:
    print("Error")
    pa()
    continue
   sa(-l10(v))
   pa()
  elif ch=="2":
   v=gf("pH:")
   if v is None or v<0 or v>14:
    print("Error")
    pa()
    continue
   sa(v)
   pa()
  elif ch=="3":
   v=gf("[OH-] M:")
   if v is None or v<=0:
    print("Error")
    pa()
    continue
   sa(14.0+l10(v))
   pa()
  elif ch=="4":
   v=gf("pOH:")
   if v is None or v<0 or v>14:
    print("Error")
    pa()
    continue
   sa(14.0-v)
   pa()
def stra():
 hdr("Strong Acids")
 print("HA->H++A-  [H+]=C")
 c=gf("Conc M:")
 if c is None or c<=0:
  print("Error")
  pa()
  return
 if c<1e-7:
  h=(c+sq(c*c+4.0*KW))/2.0
 else:
  h=c
 sa(-l10(h))
 pa()
def strb():
 while True:
  hdr("Strong Bases")
  print("1.Mono (NaOH)")
  print("2.Di (Ca(OH)2)")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1" or ch=="2":
   c=gf("Conc M:")
   if c is None or c<=0:
    print("Error")
    pa()
    continue
   if ch=="1":oh=c
   else:oh=2.0*c
   if oh<1e-7:
    oh=(oh+sq(oh*oh+4.0*KW))/2.0
   sa(14.0+l10(oh))
   pa()
def wka():
 while True:
  hdr("Weak Acids")
  print("HA<->H++A-")
  print("1.Find pH")
  print("2.% Ioniz")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1" or ch=="2":
   ka=gf("Ka:")
   if ka is None or ka<=0:
    print("Error")
    pa()
    continue
   c=gf("[HA] M:")
   if c is None or c<=0:
    print("Error")
    pa()
    continue
   x=qd(1.0,ka,-ka*c)
   if x is None or x<=0:
    print("No solution")
    pa()
    continue
   sa(-l10(x))
   if ch=="2":print("%ion="+str(round(x/c*100,2))+"%")
   print("Aprx:"+fmt(sq(ka*c)))
   if x/c<0.05:print("<5%:approx OK")
   else:print(">5%:use quad")
   pa()
def wkb():
 while True:
  hdr("Weak Bases")
  print("B+H2O<->BH++OH-")
  print("1.Find pH")
  print("2.% Ioniz")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1" or ch=="2":
   kb=gf("Kb:")
   if kb is None or kb<=0:
    print("Error")
    pa()
    continue
   c=gf("[B] M:")
   if c is None or c<=0:
    print("Error")
    pa()
    continue
   x=qd(1.0,kb,-kb*c)
   if x is None or x<=0:
    print("No solution")
    pa()
    continue
   sa(14.0+l10(x))
   if ch=="2":print("%ion="+str(round(x/c*100,2))+"%")
   pa()
def buf():
 while True:
  hdr("Buffers")
  print("1.H-H eqn")
  print("2.Add str acid")
  print("3.Add str base")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   ka=gf("Ka:")
   if ka is None or ka<=0:
    print("Error")
    pa()
    continue
   a=gf("[A-] M:")
   ha=gf("[HA] M:")
   if a is None or ha is None or a<=0 or ha<=0:
    print("Error")
    pa()
    continue
   pk=-l10(ka)
   print("pKa="+str(round(pk,4)))
   print("pH="+str(round(pk+l10(a/ha),4)))
   pa()
  elif ch=="2" or ch=="3":
   if ch=="2":hdr("Buf+Acid")
   else:hdr("Buf+Base")
   ka=gf("Ka:")
   ac=gf("[A-] M:")
   hc=gf("[HA] M:")
   vb=gf("Buf vol L:")
   cc=gf("Add conc M:")
   va=gf("Add vol L:")
   if ka is None or ac is None or hc is None:
    continue
   if vb is None or cc is None or va is None:
    continue
   if ka<=0 or ac<=0 or hc<=0 or vb<=0 or cc<=0 or va<=0:
    print("Error")
    pa()
    continue
   pk=-l10(ka)
   ma=ac*vb
   mh=hc*vb
   mx=cc*va
   vt=vb+va
   if ch=="2":
    na=ma-mx
    nh=mh+mx
   else:
    na=ma+mx
    nh=mh-mx
   if na<=0:
    print("Buf exceeded!")
    print("pH="+str(round(-l10(-na/vt),4)))
   elif nh<=0:
    print("Buf exceeded!")
    print("pH="+str(round(14.0+l10(-nh/vt),4)))
   else:
    print("pH="+str(round(pk+l10(na/nh),4)))
   pa()
def tsas():
 hdr("StrongA+StrongB")
 ca=gf("C_acid M:")
 va=gf("V_acid L:")
 cb=gf("C_base M:")
 vb=gf("Vb added L:")
 if ca is None or va is None or cb is None or vb is None:return
 if ca<=0 or va<=0 or cb<=0 or vb<0:
  print("Error")
  pa()
  return
 ve=ca*va/cb
 vt=va+vb
 print("Vep="+str(round(ve*1000,2))+"mL")
 if abs(vb-ve)<1e-9:print("At EP: pH=7")
 elif vb<ve:
  h=(ca*va-cb*vb)/vt
  print("BeforeEP")
  print("pH="+str(round(-l10(h),4)))
 else:
  oh=(cb*vb-ca*va)/vt
  print("AfterEP")
  print("pH="+str(round(14.0+l10(oh),4)))
 pa()
def twas():
 hdr("WeakA+StrongB")
 ka=gf("Ka:")
 ca=gf("C_acid M:")
 va=gf("V_acid L:")
 cb=gf("C_base M:")
 vb=gf("Vb added L:")
 if ka is None or ca is None or va is None or cb is None or vb is None:return
 if ka<=0 or ca<=0 or va<=0 or cb<=0 or vb<0:
  print("Error")
  pa()
  return
 pk=-l10(ka)
 ve=ca*va/cb
 vt=va+vb
 print("Vep="+str(round(ve*1000,2))+"mL")
 print("pKa="+str(round(pk,4)))
 if vb==0.0:
  x=qd(1.0,ka,-ka*ca)
  print("WeakAcid")
  print("pH="+str(round(-l10(x),4)))
 elif abs(vb-ve/2.0)<1e-9:
  print("Half-EP:pH=pKa")
  print("pH="+str(round(pk,4)))
 elif abs(vb-ve)<1e-9:
  cn=ca*va/vt
  kc=KW/ka
  x=qd(1.0,kc,-kc*cn)
  if x is None or x<=0:
   print("Error")
   pa()
   return
  print("AtEP:pH>7")
  print("pH="+str(round(14.0+l10(x),4)))
 elif vb<ve:
  mh=ca*va-cb*vb
  ma=cb*vb
  print("Buffer region")
  print("pH="+str(round(pk+l10(ma/mh),4)))
 else:
  oh=(cb*vb-ca*va)/vt
  print("AfterEP")
  print("pH="+str(round(14.0+l10(oh),4)))
 pa()
def tit():
 while True:
  hdr("Titrations")
  print("1.StrongA+StrongB")
  print("2.WeakA+StrongB")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":tsas()
  elif ch=="2":twas()
def kakb():
 while True:
  hdr("Ka/Kb")
  print("Ka*Kb=1e-14")
  print("1.Ka->Kb")
  print("2.Kb->Ka")
  print("3.pKa+pKb=14")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   ka=gf("Ka:")
   if ka is None or ka<=0:
    print("Error")
    pa()
    continue
   kb=KW/ka
   pk=-l10(ka)
   pkb=-l10(kb)
   print("Kb="+fmt(kb))
   print("pKa="+str(round(pk,4)))
   print("pKb="+str(round(pkb,4)))
   print("Sum="+str(round(pk+pkb,4)))
   pa()
  elif ch=="2":
   kb=gf("Kb:")
   if kb is None or kb<=0:
    print("Error")
    pa()
    continue
   ka=KW/kb
   pk=-l10(ka)
   pkb=-l10(kb)
   print("Ka="+fmt(ka))
   print("pKa="+str(round(pk,4)))
   print("pKb="+str(round(pkb,4)))
   pa()
  elif ch=="3":
   hdr("pKa+pKb=14")
   print("Ka*Kb=Kw=1e-14")
   print("pKa+pKb=14")
   pa()
PN=["H2CO3","H2SO3","H3PO4","H2S"]
P1=[4.3e-7,1.5e-2,7.5e-3,1.0e-7]
P2=[4.7e-11,6.3e-8,6.2e-8,1.0e-19]
P3=[0.0,0.0,4.8e-13,0.0]
def dip(k1,k2,c):
 hdr("Diprotic")
 x=qd(1.0,k1,-k1*c)
 if x is None or x<=0:
  print("Error")
  pa()
  return
 print("S1:[H+]="+fmt(x))
 y=qd(1.0,x+k2,-k2*x)
 if y is None:y=0.0
 ht=x+y
 print("S2:[H+]="+fmt(y))
 sa(-l10(ht))
 pa()
def trip(k1,k2,k3,c):
 hdr("Triprotic")
 x=qd(1.0,k1,-k1*c)
 if x is None or x<=0:
  print("Error")
  pa()
  return
 print("S1:[H+]="+fmt(x))
 y=qd(1.0,x+k2,-k2*x)
 if y is None:y=0.0
 h2=x+y
 print("S2:[H+]="+fmt(y))
 if k3>0:
  z=qd(1.0,h2+k3,-k3*h2)
  if z is None:z=0.0
  ht=h2+z
  print("S3:[H+]="+fmt(z))
 else:ht=h2
 sa(-l10(ht))
 pa()
def poly():
 while True:
  hdr("Polyprotic")
  print("1.Diprotic")
  print("2.Triprotic")
  print("3.Presets")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   k1=gf("Ka1:")
   k2=gf("Ka2:")
   c=gf("[H2A] M:")
   if k1 is None or k2 is None or c is None:
    continue
   if k1<=0 or k2<=0 or c<=0:
    print("Error")
    pa()
    continue
   dip(k1,k2,c)
  elif ch=="2":
   k1=gf("Ka1:")
   k2=gf("Ka2:")
   k3=gf("Ka3:")
   c=gf("[H3A] M:")
   if k1 is None or k2 is None or k3 is None or c is None:
    continue
   if k1<=0 or k2<=0 or k3<=0 or c<=0:
    print("Error")
    pa()
    continue
   trip(k1,k2,k3,c)
  elif ch=="3":
   hdr("Presets")
   for i in range(len(PN)):
    print(str(i+1)+"."+PN[i])
   print("0.Back")
   ps=input(":")
   if ps=="0":continue
   try:idx=int(ps)-1
   except:
    print("Error")
    pa()
    continue
   if idx<0 or idx>=len(PN):
    print("Error")
    pa()
    continue
   hdr(PN[idx])
   print("Ka1="+fmt(P1[idx]))
   print("Ka2="+fmt(P2[idx]))
   if P3[idx]>0:print("Ka3="+fmt(P3[idx]))
   c=gf("Conc M:")
   if c is None or c<=0:
    print("Error")
    pa()
    continue
   if P3[idx]>0:trip(P1[idx],P2[idx],P3[idx],c)
   else:dip(P1[idx],P2[idx],c)
def ref():
 hdr("Ka Values")
 print("HF     6.8e-4  3.17")
 print("HAc    1.8e-5  4.74")
 print("H2CO3  4.3e-7  6.37")
 print("HCN    6.2e-10 9.21")
 print("NH4+   5.6e-10 9.25")
 print("HCO3-  4.7e-11 10.33")
 pa()
 hdr("Kb Values")
 print("CH3NH2 4.4e-4 3.36")
 print("NH3    1.8e-5 4.74")
 print("Pyr    1.7e-9 8.77")
 print("CO3-2  2.1e-4 3.68")
 pa()
 hdr("Formulas")
 print("pH=-log[H+]")
 print("pH+pOH=14")
 print("Ka*Kb=1e-14")
 print("H-H:pH=pKa+log(r)")
 print("Vep=CaVa/Cb")
 print("Half-EP:pH=pKa")
 print("AtEP(wkA):pH>7")
 pa()
def main():
 while True:
  hdr("AP Chem U8")
  print("1.pH/pOH")
  print("2.Str Acids")
  print("3.Str Bases")
  print("4.Wk Acids")
  print("5.Wk Bases")
  print("6.Buffers")
  print("7.Titrations")
  print("8.Ka/Kb")
  print("9.Polyprotic")
  print("10.Reference")
  print("0.Quit")
  ch=input(":")
  if ch=="0":
   clr()
   print("Good luck!")
   break
  elif ch=="1":phb()
  elif ch=="2":stra()
  elif ch=="3":strb()
  elif ch=="4":wka()
  elif ch=="5":wkb()
  elif ch=="6":buf()
  elif ch=="7":tit()
  elif ch=="8":kakb()
  elif ch=="9":poly()
  elif ch=="10":ref()
  else:
   print("Invalid")
   pa()
main()
