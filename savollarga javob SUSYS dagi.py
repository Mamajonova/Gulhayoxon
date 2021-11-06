# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:59:23 2021

@author: Premium
"""
#1 + ishlatmasdan ikkita sonni qo'shing
#a=int(input("a="))
#b=int(input("b="))
#print(a-(-b))   # 2 ta - + bo'lib ketadi

#2 hello phyton so'zini chiqaring
#print("Hello,Phyton")

#3 3 ta son berilgan eng kottasini toping
#print("3 ta har xil son kiriting")
#a=float(input("a="))
#b=float(input("b="))
#c=float(input("c="))
#if a>b and b>=c or a>c and c>b:
#    print(a,"eng kottasi")
#elif b>a and a>c or b>c and c>a:
#    print(b,"eng kottasi")
#elif c>b and b>a or c>a and a>b:
#    print(c,"eng kottasi")
#else:
#    print("xatolik 3 ta har xil son kiriting")

#4 n soni berilgan n*(n+1)*(n+2) ko'paytma 6 ga bo'lingandagi qoldiqni toping
#n=int(input("n="))
#print(a%6," ga teng")
#a=n*(n+1)*(n+2)


import math
 #9 n soni m dan necha marta katta bolsa n dan shuncha marta kotta sonni toping
#n=int(input("n="))
#m=int(input("m="))
#a=n/m
#b=(n/m)*n
#print(b)

#7 1 dan n gacha bolgan sonlarni kiriting har bir sonni ildizlar yig'indisini toping
#n=int(input("n="))
#sonlar=list(range(1,n+1))
#s=0
#for i in sonlar:
#    i+=1
#    s+=i**(1/2)
#print(n,"gacha sonlar ildizlar yig'indisi",s," gateng")


#10 1 dan n gacha sonlar ro'yxatini kiriting teskari tartibda chiqarib bersin
#n=int(input("n="))
#sonlar=list(range(1,n+1))
#print(sonlar)
#sonlar.reverse()
#print(sonlar)


#5
#a=int(input("a="))
#b=int(input("b="))
#oraliq=list(range(a,b))
#k=0
#for i in oraliq:
#    if i%4==0:
 #       k+=1
#print("4 ga bo'linadiganlar soni: ",k)



#8
#n=int(input("n="))
#oraliq=list(range(1,n+1))
#k=0
#for i in oraliq:
#    if i%4==0 or i%5==0 or i%6==0:
#        k+=1
#print("4,6,5 ga bo'linadiganlar soni: ",k)












a=int(input("a="))
k=0
while a%10==0:
        k+=1
        a=a/10
print("berilgan son quyidagicha son bilan tugaydi: ",k)








