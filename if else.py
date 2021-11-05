# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:25:32 2021

@author: Premium
"""
# 1-misol
#a=float(input("ixtiyoriy son kiriting: "))
#if a>0:
#    print(a,"musbat son")
#elif a<0:
#    print(a,"manfiy son")
#else:
#    print("nolga teng")
#    
# 2-misol
#a=int(input("ixtiyoriy son kiriting: "))
#if a%2==0:
#    print(a,"juft son")
#else:
#    print(a,"toq son")
#
#3-misol
#a=int(input("ixtiyoriy son kiriting: "))
#if a%10==0:
#    print(True,"oxiri nol bilan tugaydi")
#
#else:
#    print(False,"oxiri",a%10," bilan tugaydi")


 #4-misol  
#print("1 dan 7 gacha bo'lgan sonlarni kiriting: ")
#a=int(input("son kiritng: "))
#if a==1:
#    print("Dushanba")
#elif a==2:
#    print("Seshanba")
#elif a==3:
#    print("Chorshanba")
#elif a==4:
#    print("Payshanba")
#elif a==5:
#    print("Juma")
#elif a==6:
#    print("Shanba")
#elif a==7:
#    print("Yakshanba")
#else:
#    print("Xatolik 1 dan 7 gacha son kiriting")

# 5-misol
#print("Uchburchakni tomonlarini kiriting: ")
#a=float(input("1-tomonni kiriting="))
#b=float(input("2-tomonni kiriting="))
#c=float(input("3-tomonni kiriting="))
#if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
#    print(True,"uchburchak yasash mumkin")
#else:
#    print(False,"uchburchak yasash mumkin emas")
    




# 6-misol
#print("3 xonali son kiriting: ")
#a=int(input("son: "))
#b=a%100          # oxirgi 2ta raqamni topish uchun 100 ga bo'lib b ga yuklab qo'ydim
#if b%3==0:
#    print(a,"sonni oxirgi 2 ta raqami",b,"    3 ga bo'linadi")
#else:
#    print(a,"sonni oxirgi 2 ta raqami",b,"    3 ga bo'linmaydi")


#7-misol
#print("ikkta son kiriting ")
#a=float(input("1-sonn: "))
#b=float(input("2-sonn: "))
#kopaytma=a*b
#if kopaytma>10 and kopaytma<50:
#    print(True,kopaytma,"ko'paytma (10;50) oraliqqa kiradi")
#else:
#    print(False,kopaytma," ko'paytma (10;50) oraliqqa kirmaydi")








s=int(input("6 xonali son kiriting: "))
if s>99999 and s<1000000:
    a=s//100000
    b=(s%100000)//10000
    c=s%10000//1000
    d=s%1000//100
    e=s%100//10
    f=s%10
    print(a,b,c,d,e,f)
    if(a+b+c==d+e+f):
        print(True,"boshidagi 3 ta sonni yig'indisi keyingi 3 ta sonni yig'indisiga teng")
    else:
        print(False,a+b+c,"1-uchta son yig'indisi",d+e+f,"keyingi 3 ta son yig'indisi teng emas" )
else:
    print(" xatolik 6 xonali son kiriting")

























