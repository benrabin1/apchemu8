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
 clr();print("-"*26);print(t);print("-"*26)
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
 po=14-ph
 print("pH="+str(round(ph,4)))
 print("pOH="+str(round(po,4)))
 print("[H+]="+fmt(10**-ph))
 print("[OH-]="+fmt(10**-po))
def buf():
 while True:
  hdr("Buffers")
  print("1.H-H 2.+Acid 3.+Base")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   ka=gf("Ka:");a=gf("[A-]M:");h=gf("[HA]M:")
   if ka is None or a is None or h is None:pa();continue
   if ka<=0 or a<=0 or h<=0:pa();continue
   pk=-l10(ka)
   print("pKa="+str(round(pk,4)))
   print("pH="+str(round(pk+l10(a/h),4)))
   pa()
  elif ch=="2" or ch=="3":
   ka=gf("Ka:");ac=gf("[A-]M:");hc=gf("[HA]M:")
   vb=gf("BufVL:");cc=gf("AddCM:");va=gf("AddVL:")
   if ka is None or ac is None or hc is None:pa();continue
   if vb is None or cc is None or va is None:pa();continue
   if ka<=0 or ac<=0 or hc<=0 or vb<=0 or cc<=0 or va<=0:pa();continue
   pk=-l10(ka);mx=cc*va;vt=vb+va
   if ch=="2":na=ac*vb-mx;nh=hc*vb+mx
   else:na=ac*vb+mx;nh=hc*vb-mx
   if na<=0:print("pH="+str(round(-l10(-na/vt),4)))
   elif nh<=0:print("pH="+str(round(14+l10(-nh/vt),4)))
   else:print("pH="+str(round(pk+l10(na/nh),4)))
   pa()
def tsas():
 hdr("SA+SB")
 ca=gf("Ca:");va=gf("Va:");cb=gf("Cb:");vb=gf("Vb:")
 if ca is None or va is None or cb is None or vb is None:return
 if ca<=0 or va<=0 or cb<=0 or vb<0:pa();return
 ve=ca*va/cb;vt=va+vb
 print("Vep="+str(round(ve*1000,2))+"mL")
 if abs(vb-ve)<1e-9:print("EP:pH=7")
 elif vb<ve:print("pH="+str(round(-l10((ca*va-cb*vb)/vt),4)))
 else:print("pH="+str(round(14+l10((cb*vb-ca*va)/vt),4)))
 pa()
def twas():
 hdr("WA+SB")
 ka=gf("Ka:");ca=gf("Ca:");va=gf("Va:")
 cb=gf("Cb:");vb=gf("Vb:")
 if ka is None or ca is None or va is None or cb is None or vb is None:return
 if ka<=0 or ca<=0 or va<=0 or cb<=0 or vb<0:pa();return
 pk=-l10(ka);ve=ca*va/cb;vt=va+vb
 print("Vep="+str(round(ve*1000,2))+"mL pKa="+str(round(pk,4)))
 if vb==0:
  x=qd(1,ka,-ka*ca)
  print("pH="+str(round(-l10(x),4)))
 elif abs(vb-ve/2)<1e-9:
  print("Half-EP:pH=pKa")
 elif abs(vb-ve)<1e-9:
  kc=KW/ka;x=qd(1,kc,-kc*ca*va/vt)
  if x is None or x<=0:print("Err");pa();return
  print("EP pH="+str(round(14+l10(x),4)))
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
  hdr("Ka/Kb")
  print("Ka*Kb=1e-14  pKa+pKb=14")
  print("1.Ka->Kb 2.Kb->Ka")
  print("0.Back")
  ch=input(":")
  if ch=="0":break
  elif ch=="1":
   k=gf("Ka:")
   if k is None or k<=0:pa();continue
   kb=KW/k
   print("Kb="+fmt(kb))
   print("pKa="+str(round(-l10(k),4)))
   print("pKb="+str(round(-l10(kb),4)))
   pa()
  elif ch=="2":
   k=gf("Kb:")
   if k is None or k<=0:pa();continue
   ka=KW/k
   print("Ka="+fmt(ka))
   print("pKa="+str(round(-l10(ka),4)))
   print("pKb="+str(round(-l10(k),4)))
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
 hdr("Key Formulas")
 print("pH=-log[H+]  pH+pOH=14")
 print("Ka*Kb=1e-14")
 print("H-H:pH=pKa+log([A]/[HA])")
 print("Vep=CaVa/Cb")
 print("Half-EP:pH=pKa")
 print("At EP(wkA):pH>7")
 pa()
def main():
 while True:
  hdr("AP Chem U8 Part B")
  print("1.Buffers")
  print("2.Titrations")
  print("3.Ka/Kb")
  print("4.Reference")
  print("0.Quit")
  ch=input(":")
  if ch=="0":clr();break
  elif ch=="1":buf()
  elif ch=="2":tit()
  elif ch=="3":kakb()
  elif ch=="4":ref()
  else:print("?");pa()
main()
