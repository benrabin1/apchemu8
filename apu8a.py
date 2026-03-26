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
 po=14-ph;h=10**-ph;o=10**-po
 print("pH ="+str(round(ph,4)))
 print("pOH="+str(round(po,4)))
 print("[H+]="+fmt(h))
 print("[OH-]="+fmt(o))
def phb():
 while True:
  hdr("pH/pOH")
  print("1.[H+] 2.pH")
  print("3.[OH-] 4.pOH")
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
   if ch=="1":oh=c
   else:oh=2*c
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
def main():
 while True:
  hdr("AP Chem U8 Part A")
  print("1.pH/pOH")
  print("2.Strong Acids")
  print("3.Strong Bases")
  print("4.Weak Acids")
  print("5.Weak Bases")
  print("0.Quit")
  ch=input(":")
  if ch=="0":clr();break
  elif ch=="1":phb()
  elif ch=="2":stra()
  elif ch=="3":strb()
  elif ch=="4":wka()
  elif ch=="5":wkb()
  else:print("?");pa()
main()
