# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:02:35 2021

@author: Premium

"""
# 1-misol
a=int(input("son kiriting:"))
if a>100:
    print("100 dan kotta")
elif a<100:
    print("100 dan kichkina")
else:
    print("100 ga teng")
    
# 2-misol
print("\n1,2,3 dan birini kiriting:")
a=int(input("son kiritng="))
if a==1:
    print("Django-phyton tilida veb ilovalar ishlab chiqish uchun ajoyib freymvork.",
         " Freymvork phyton tilida yozilgan. 1-bor 2005-yil 21-iyulda ishga tushirilgan.",
         "Djangoda yaratilgan sayt bir yoki bir nechta ilovadan tashkil topishi mumkin.")
elif a==2:
    print("Flask Phytonning Web-saytlari yaratish uchun ishlatiladigan frameworki hisoblanadi."
          " Flask asosan kichikroq web-saytlar yaratishda ishlatiladi. Kattaroq web saytlarni esa djangoda yaratiladi.")
elif a==3:
    print("Node yoki Node.js -V8 drijoki asosida yaratilgan dasturiy platforma."
          "Node.js JavaScript kodni native codega o'girib beradi.")
else:
    print("xatolik  1,2,3 dan birini kiriting")
    
# 3-misol
print("ikkita son kiriting:")
a=int(input("1-sonni kiriting: "))
b=int(input("2-sonni kiriting:"))
print("\nqaysi amalni bajarmoqchisiz:",
      "\n1:qo'shish +",
      "\n2:ayirish -",
      "\n3:ko'paytirish *",
      "\n4: bo'lish /")
c=input("biror ishorani kiriting:")
if c==1 or c=="qo'shish" or c=="+":
    print(a+b)
elif c==2 or c=="ayirish" or c=="-":
    print(a-b)
elif c==3 or c=="ko'paytirish" or c=="*":
    print(a*b)
elif c==4 or c=="bo'lish" or c=="/":
    print(a/b)
else:
    print("xatolik boshidan boshlang")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    