# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:17:40 2021

@author: Premium
"""
"""
maxsulotlar=["non","choy","salat","osh","manti","sok","shurva","somsa","kofe","bishteks"]
savat=[]
print("5 ta mahsulot kiriting")
for a in range(5):
    savat.append(input(f"{a+1}-maxsulotni kiriting  "))
print(savat)
for maxsulot in savat:
    if maxsulot in maxsulotlar:
        print(f"menyuda {maxsulot} bor")
    else:
        print(f"kechirasiz, menyuda {maxsulot} yoq")
        """
        
"""     
maxsulotlar=["non","choy","salat","osh","manti","sok","shurva","somsa","kofe","bishteks"]
savat=[]
bor_maxsulotlar=[]
yoq_maxsulotlar=[]
print("5 ta mahsulot kiriting")
for a in range(5):
    savat.append(input(f"{a+1}-maxsulotni kiriting  "))
print(savat)
for maxsulot in savat:
    if maxsulot in maxsulotlar:
        bor_maxsulotlar.append(maxsulot)
    else:
        yoq_maxsulotlar.append(maxsulot)
print("bor buyurtmalar",bor_maxsulotlar)
print("yoq buyurtmalar",yoq_maxsulotlar)
if len(bor_maxsulotlar)==5:
    print("siz so'ragan barcha buyurtma bor")
elif len(yoq_maxsulotlar)==5:
    print("siz so'ragan barcha buyurtma yoq")
    """
    
    
"""
loginlar=[]
print("5 ta login kiriting")
for a in range(5):
    loginlar.append(input(f"{a+1}-loginni kiriting  "))
print(loginlar)
yangi_l=input("yangi login kiriting: ")
if yangi_l.lower() in loginlar:
    print("LOGIN BAND")
else:
    print("XUSH KELIBSIZ")
"""
"""
a=int(input("a="))
sonlar=list(range(2,10+1))
for son in sonlar:
    if a%son==0:
        print(son)
        print(a,"qoldiqsiz bo'linadi",son,"ga")
        """
    





