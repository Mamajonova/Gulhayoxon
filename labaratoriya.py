# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 07:11:03 2021

@author: Premium
"""
import math

"""
#1         shunday boladimi
print("(x^x)' ning hosilasi=")
print("x^x*(ln(x)+1)")

#2
print("ln(ctg(x)-1)=a  tenglamaning yechimi (pi,2*pi) oraliqda")
a=float(input("a="))
x=math.atan(1/(math.e**a+1))
if x>math.pi and x<2*math.pi:
    print("oraliqqa kiradi")
else:
    print("oraliqqa kirmaydi")
print(x)       


#3
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
M=(a*b*c)**(1/3)
print(M)           #butun qismini chiqarish qanday

#4  c1 va c2 noldan farqli tenglamar sistemasini yechamiz
print("a1*x+b1*y=c1")
print("a2*x+b2*y=c2")
a1=float(input("a1="))
b1=float(input("b1="))
c1=float(input("c1="))
a2=float(input("a2="))
b2=float(input("b2="))
c2=float(input("c2="))
D=a1*b2-a2*b1
Dx=c1*b2-b1*c2
Dy=a1*c2-c1*a2
x=Dx/D
y=Dy/D
print(x)
print(y)

#5  radius berilgan yuzi uzunligi hajmini topish
r=float(input("r="))
S=math.pi*r**2
L=2*r*math.pi
V=math.pi*r**3
print("shar hajmi=",V)
print("doira uzunligi=",L)
print("doira yuzi=",S)

#6 to'g'ri burchakli uchburchak katetlari berilgan yuzi va perimetrini toping
a=float(input("a="))
b=float(input("b="))
S=a*b/2
c=(a**2+b**2)**(1/2)
P=a+b+c
print("to'g'ri burchakli uchburchak yuzi=",S)
print("to'g'ri burchakli uchburchak perimetri=",P)


#7 uchburchak burchaklari koordinatalari berilgan shu uchburchak yuzini toping
x1=float(input("x1="))
y1=float(input("y1="))
x2=float(input("x2="))
y2=float(input("y2="))
x3=float(input("x3="))
y3=float(input("y3="))
a1=x2-x1
b1=y2-y1
a2=x3-x2
b2=y3-y2
a3=x3-x1
b3=y3-y1
c1=(a1**2+b1**2)**(1/2)
c2=(a2**2+b2**2)**(1/2)
c3=(a3**2+b3**2)**(1/2)
p=(c1+c2+c3)/2
S=p*(p-a)*(p-b)*(p-c)
print("S=",S)

#8 uchburchakni ikki tomoni va orasidagi burchagi berilgan shu uchburchak yuzini toping
a=float(input("a="))
b=float(input("b="))
alfa=float(input("alfa="))
S=a*b*math.sin(alfa)
print(S)

#9 4 xonali son beerilgan raqamlari ko'paytmasini toping
print("4 xonali son kiriting")
a=int(input("a="))
a1=a//1000
print(a1)
a2=(a%1000)//100
print(a2)
a3=(a%100)//10
print(a3)
a4=a%10
print(a4)
print("raqamlari ko'paytmasi=",a1*a2*a3*a4)

#10 3 xonali son berilgan shu sonni raqamlarini teskarisiga almashtirib chiqaramiz
print("3 xonali son kiriting")
a=int(input("a="))
a1=a//100
print(a1)
a2=(a%100)//10
print(a2)
a3=a%10
print(a3)
print(str(a3)+str(a2)+str(a1))

#11 p son va oraliq kiritamiz va berilgan tenglama yechimi shu oraliqda bor yoqlikka tekshiramiz
print("p son va (a,b) oraliq kiritamiz")
p=float(input("p="))
a=float(input("a="))
b=float(input("b="))
x=math.log2((p)+math.tan(2**(1/2)))
print(x)
if x>a and x<b:
    print("tenglama yechimi (a,b) oraliqda bor")
else:
    print("berilgan oraliqda emas yechim")
    
#12  4 xonali son berilgan boshki ikkita raqami yig'indisi keyingi 2 tasi yig'indisiga tengmi
print("4 xonali son kiriting")
a=int(input("a="))
a1=a//1000
print(a1)
a2=(a%1000)//100
print(a2)
a3=(a%100)//10
print(a3)
a4=a%10
print(a4)
print("boshidagi ikkita raqam yig'indisi qolgan ikkitasiga tengmi",a1+a2==a3+a4)

#13  3 xonali son berilgan raqamlari yig'indisi kubi berilgan son kvadratiga tengmi
print("3 xonali son kiriting")
a=int(input("a="))
a1=a//100
print(a1)
a2=(a%100)//10
print(a2)
a3=a%10
print(a3)
print("raqamlari yig'indisi kubi berilgan son kvadratiga tengmi",a**2==(a1+a2+a3)**3)

#14 butunli son berilgan kasr qismini boshki 3 ta raqamida nol bormi
print("kasr qismini boshki uchta raqamida nol bormi")
a=float(input("a="))
a1=(a*1000)%1000
b1=a//100
b2=(a%100)//10
b3=a%10
if b1==0 or b2==0 or b3==0:
    print("nol bor")
else:
    print("nol yoq")
    
#15 3 xonali son berilgan bir xil raqamlari bormi
print("3 xonali son kiriting")
a=int(input("a="))
a1=a//100
print(a1)
a2=(a%100)//10
print(a2)
a3=a%10
print(a3)
if a1==a2 or a1==a3 or a2==a3:
    print("bir xil raqamlari bor")
else:
    print("bir xil raqamlari yoq")

#16 3 uchburchakni 3 ta tomoni berilgan bulardan uchburchak yasash mumkinmi
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    print("berilgan tomonli uchburchak bor")
else:
    print("uchburchak yasab bolmaydi")
    """
"""
#17 ot turgan nuqtasidan 2-nuqtaga ko'cha oladimi
print("ot qayerda turibdi ")
x1=int(input("x1="))
x2=int(input("x2="))
print("otni qayerga o'tkazish kerak")
y1=int(input("y1="))
y2=int(input("y2="))
if (y1==x1+1 and y2==x2+2 or y1==x1+1 and y2==x2-2 or y1==x1-1 and y2==x2+2 or y1==x1-1 and y2==x2-2 or y1==x1+2 and y2==x2+1 or y1==x1+2 and y2==x2-1 or y1==x1-2 and y2==x2+1 or y1==x1-2 and y2==x2-1)and x1>=1 and x1<=8 and x2>=1 and x2<=8 and y1>=1 and y1<=8 and y2>=1 and y2<=8 :
    print("o'ta oladi")
else:
    print("o'ta olmaydi")
    
#if_else shart operatori
x=float(input("x="))
a=(math.e**x+math.e**(-x))/2
b=1+math.fabs(x)
c=(1+x**2)**x
if (a>=b and b>=c):
    print(c,b,a)
elif (a>=c and c>=b):
    print(b,c,a)
elif (b>=a and a>=c):
    print(c,a,b)
elif(b>=c and c>=a):
    print(a,c,b)
elif (c>=b and b>=a):
    print(a,b,c)
elif(c>=a and a>=b):
    print(b,a,c)
else:
    print("boshqa son kiritib ko'ring")

#2-misol
print("a1*x+b1*y=c1")
print("a2*x+b2*y=c2")
a1=float(input("a1="))
b1=float(input("b1="))
c1=float(input("c1="))
a2=float(input("a2="))
b2=float(input("b2="))
c2=float(input("c2="))
if (a1/a2)!=(b1/b2) and (c1/c2)!=(b1/b2):
    print("tenglamalar sistemasi ustma-ust tushadi")
elif a1/a2!=c1/c2 and b1/b2!=c1/c2:
    print("bitta yechimga ega")
elif a1/a2==b1/b2 and a1/a2!=c1/c2:
    print("yechimga ega emas")
else:
    print("boshqa son kiriting")

#3-misol
print("a*x**4+b*x**2+c=0")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
D=b**2-4*a*c
if D>0:
    t1=(-b+math.sqrt(D))/(2*a)
    t2=(-b-math.sqrt(D))/(2*a)
    if t1>=0 and t2>=0:
        x1=math.sqrt(t1)
        x2=-math.sqrt(t1)
        x3=math.sqrt(t2)
        x4=-math.sqrt(t2)
        print("ildizlari",x1,x2,x3,x4)
    elif t1>=0 and t2<=0:
        x1=math.sqrt(t1)
        x2=-math.sqrt(t1)
        print("ildizlari",x1,x2)
    elif t1<=0 and t2>=0:
         x3=math.sqrt(t2)
         x4=-math.sqrt(t2)
         print("ildizlari",x3,x4)
    else:
        print("ildizi yoq")
elif D==0:
    t1=-b/(2*a)
    if t1>=0:
        x1=math.sqrt(t1)
        x2=-math.sqrt(t1)
        print("ldizlari",x1,x2)
    else:
        print("ildizi yoq")
else:
    print("ildizi yoq")
"""
'''
#4-misol

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            print(3,"teng tomonli uchburchak")
        elif a==b!=c or a==c!=b or c==b!=a:
            print(2,"teng yonli uchburchak")
        else:
            print(1,"ixtiyoriy uchburchak")
    else:
        print(0,"bunday uchburchak yasab bolmaydi")
else:
    print("xatolik")
    '''
    
#5-misol
print("rux x va y nuqtada turibdi: ")
x=int(input("x="))
y=int(input("y="))
print("ruh ikkinchi k va l ga o'ta oladimi")
k=int(input("k="))
l=int(input("l="))
if k==x+1 and l==y+1 or  k==x+2 and l==y+2 or  k==x+3 and l==y+3 or  k==x+4 and l==y+4 or  k==x+5 and l==y+5 or  k==x+6 and l==y+6 or  k==x+7 and l==y+7 :
    print("o'ta oladi")
elif k==x-1 and l==y-1 or  k==x-2 and l==y-2 or  k==x-3 and l==y-3 or  k==x-4 and l==y-4 or  k==x-5 and l==y-5 or  k==x-6 and l==y-6 or  k==x-7 and l==y-7 :
    print("o'ta oladi")
elif k==x+1 and l==y-1 or  k==x+2 and l==y-2 or  k==x+3 and l==y-3 or  k==x+4 and l==y-4 or  k==x+5 and l==y-5 or  k==x+6 and l==y-6 or  k==x+7 and l==y-7 :
    print("o'ta oladi")
elif k==x-1 and l==y+1 or  k==x-2 and l==y+2 or  k==x-3 and l==y+3 or  k==x-4 and l==y+4 or  k==x-5 and l==y+5 or  k==x-6 and l==y+6 or  k==x-7 and l==y+7 :
    print("o'ta oladi")
else:
    print("o'ta olmaydi")

#6-misol
print("farzin x va y nuqtada turibdi: ")
x=int(input("x="))
y=int(input("y="))
print("farzin ikkinchi k va l ga o'ta oladimi")
k=int(input("k="))
l=int(input("l="))
if (k==x+1 and l==y+1 or  k==x+2 and l==y+2 or  k==x+3 and l==y+3 or  k==x+4 and l==y+4 or  k==x+5 and l==y+5 or  k==x+6 and l==y+6 or  k==x+7 and l==y+7) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")#bir tekisda yuqoriga harakatlansa
elif (k==x-1 and l==y-1 or  k==x-2 and l==y-2 or  k==x-3 and l==y-3 or  k==x-4 and l==y-4 or  k==x-5 and l==y-5 or  k==x-6 and l==y-6 or  k==x-7 and l==y-7) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")#bir tekisqa quyiga harakatlansa
elif (k==x+1 and l==y-1 or  k==x+2 and l==y-2 or  k==x+3 and l==y-3 or  k==x+4 and l==y-4 or  k==x+5 and l==y-5 or  k==x+6 and l==y-6 or  k==x+7 and l==y-7) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")#k tomon oshib 2- tarafi kamayib harakatlansa
elif (k==x-1 and l==y+1 or  k==x-2 and l==y+2 or  k==x-3 and l==y+3 or  k==x-4 and l==y+4 or  k==x-5 and l==y+5 or  k==x-6 and l==y+6 or  k==x-7 and l==y+7) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8 :
    print("o'ta oladi")#l tomon oshib k tomon kamayib harakatlansa 
elif (k==x and l==y+1 or  k==x and l==y+2 or  k==x and l==y+3 or  k==x and l==y+4 or  k==x and l==y+5 or  k==x and l==y+6 or  k==x and l==y+7) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")# k tomon o'zgarmi l ortib harakatlansa
elif (k==x-1 and l==y or  k==x-2 and l==y or  k==x-3 and l==y or  k==x-4 and l==y or  k==x-5 and l==y or  k==x-6 and l==y or  k==x-7 and l==y) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")#l tomon o'zgarmi k tomon kamayib harakatlansa
elif (k==x and l==y-1 or  k==x and l==y-2 or  k==x and l==y-3 or  k==x and l==y-4 or  k==x and l==y-5 or  k==x and l==y-6 or  k==x and l==y-7) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")# k tomon o'zgarmi l tomon kamayib harakatlansa
elif (k==x+1 and l==y or  k==x+2 and l==y or  k==x+3 and l==y or  k==x+4 and l==y or  k==x+5 and l==y or  k==x+6 and l==y or  k==x+7 and l==y) and x>=1 and x<=8 and y>=1 and y<=8 and k>=1 and k<=8 and l>=1 and l<=8:
    print("o'ta oladi")# k tomon oshib l o'zgarmasa
else:#boshqa holatlarda o'ta olmaydi
    print("o'ta olmaydi")
    
#8-misol uchburchak nuqtalari berilgan berilgan nuqta uchburchak ichida yotadimi
print("uchburchak joylashgan nuqta koordinatalarini kiriting")
x1=float(input("x1="))
y1=float(input("y1="))
x2=float(input("x2="))
y2=float(input("y2="))
x3=float(input("x3="))
y3=float(input("y3="))
print("M nuqta koordinatalarini kiriting u uchburchak ichida yotadimi?")
x=float(input("x1="))
y=float(input("x1="))



a1=float(input("a1="))
a1=float(input("a1="))
a1=float(input("a1="))
a1=float(input("a1="))

a=input("matn kiriting:")
print(len(a))