# Qudrat Abdurahimov shart operatoriga oid misollar
# 1
from math import *
x=int(input("x="))  # x degan son kiritamiz musbat bolsa 1 ga oshiradi aks holda hech narsa
if x>0:
    print(x+1)


#2
y=int(input("y=")) # y musbat bolsa 1 ga oshirsin aks holda -2 ga kamaytirsin
if y>0:
    print(y+1)
else:
    print(y-2)


# 3
z=int(input("y=")) # z musbat bolsa 1 ga oshirsin nolga teng bolsa 10  aks holda -2 ga kamaytirsin
if z>0:
    print(z+1)
elif z==0:
    print(10)
else:
    print(z-2)
# 4 3 ta son kiritamiz musbat va manfiylar sonini aniqlash
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a>0 and b>0 and c>0:
    print("3 ta musbat son bor")
elif a<0 and b<0 and c<0:
    print("3 ta manfiy son bor")
elif a>0 and b<0 and c<0 or a<0 and b>0 and c<0 or a<0 and b<0 and c>0:
    print(" 1 ta musbat 2 ta manfiy son bor")
elif  a>0 and b>0 and c<0 or a>0 and b<0 and c>0 or a<0 and b>0 and c>0:
    print(" 2 ta musbat 1 ta manfiy son bor")
elif a==0 and b==0 and c==0:
    print("3 ta nol bor" )
elif a==0 and b>0 and c>0 or a>0 and b==0 and c>0 or a>0 and b>0 and c==0:
    print("1 ta nol 2 ta musbat son bor")
elif a==0 and b==0 and c>0 or a>0 and b==0 and c==0 or a==0 and b>0 and c==0:
    print("2 ta nol 1 ta musbat son bor")
elif a==0 and b<0 and c<0 or a<0 and b==0 and c<0 or a<0 and b<0 and c==0:
    print("1 ta nol 2 ta manfiy son bor")
elif a==0 and b==0 and c<0 or a<0 and b==0 and c==0 or a==0 and b<0 and c==0:
    print("2 ta nol 1 ta manfiy son bor")
elif a==0 and b>0 and c<0 or a==0 and b<0 and c>0 or a>0 and b==0 and c<0 or a<0 and b==0 and c>0 or a<0 and b>0 and c==0 or a>0 and b<0 and c==0 :
    print("1 ta nol 1 ta musbat son 1 ta manfiy son bor")
else:
    print("1 ta manfiy 2 ta musbat")


# 6 uchta son kiritamiz qaysi biri kotta ekanligini chiqarish
a=float(input("a="))
b=float(input("b="))
if a>b:
    print(a,"kotta")
elif a==b:
    print("teng")
else:
    print(b,"kotta")


# 8 2 ta son kiritamiz qaysi  biri kotta
a=float(input("a="))
b=float(input("b="))
if a>b:
    print(a,">",b)
elif a<b:
    print(b,">",a)
else:
    print(a,"=",b)


# 9
print("a dan b kotta bolgan son  kiriting")
a=float(input("a="))
b=float(input("b="))
a==b
b==a
print(b,a)


#11  ikkita son berilgan teng bolsa nol chiqsin a va b ni ham chiqarib bersin
a=float(input("a="))
b=float(input("b="))
if a==b:
    print(0,a,b)
else:
    print(a+b)

#12  3 ta son berilgan eng kottasini topish
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a==b and b==c:
    print("uchalasi teng")
elif a==b and b<c:
    print(c,"kotta")
elif a==b and b>c:
    print("a va b eng kotta",b)
elif a>b and b==c:
    print("a kotta",a)
elif a<b and b==c:
    print("b va c eng kotta",b)
elif a==c and b>c:
    print("b eng kotta",b)
elif a==c and b<c:
    print("c eng kotta",c)
elif a>b and b>c:
    print("a kotta",a)
elif a>c and b<c:
    print("a kotta",a)
elif a<b and a>c:
    print("b kotta",b)
elif a>c and b>a:
    print("b kotta",b)
elif a>b and a<c:
    print("c kotta",c)
elif a<b and b<c:
    print("c kotta",c)
else:
    print("boshqa son kiritib ko'ring")


# 16 3 ta son berilgan o'sish tartibida chiqarish
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a==b and b==c:
    print(a,"=",b,"=",c)
elif a==b and b<c:
    print(a,"=",b,"<c")
elif a==b and b>c:
    print(a,"=",b," > ",c)
elif a>b and b==c:
    print(a,">",b,"=",c)
elif a<b and b==c:
    print(b,"=",c,">",a)
elif a==c and b>c:
    print(b,">",a,"=",c)
elif a==c and b<c:
    print(c,"=",a,">",b)
elif a>b and b>c:
    print(c,"<",b,"<",a)
elif a>c and b<c:
    print(b,"<",c,"<",a)
elif a<b and a>c:
    print(c,"<",a,"<",b)
elif a<c and b>c:
    print(a,"<",c,"<",b)
elif a>b and a<c:
    print(b,"<",a,"<",c)
elif a<b and b<c:
    print(a,"<",b,"<",c)
else:
    print("boshqa sonlar kiritib ko'ring")

print("21 kordinata boshida bolsa x va y nol, ox o'qida bolsa 1 , oy o'qida bolsa 2, boshqa holatda 3 chiqarsin")
print("(x,y) larni kiriting")
x=float(input("x="))
y=float(input("y="))
if x==0 and y==0:
    print(0)
elif y==0:
    print(1)
elif x==0:
    print(2)
else:
    print(3)

#22 nuqtalar koordinata tekisligini qaysi choragida yotganini aniqlash
print("(x,y) larni kiriting")
x=float(input("x="))
y=float(input("y="))
if x==0 and y==0:
    print("koordinata boshida")
elif y==0:
    print("OX o'qida")
elif x==0:
    print("OY o'qida")
elif x>0 and y>0:
    print("I chorak")
elif x>0 and y<0:
    print("IV chorak")
elif x<0 and y>0:
    print("II chorak")
elif x<0 and y<0:
    print("III chorak")
else:
    print("xatolik")







