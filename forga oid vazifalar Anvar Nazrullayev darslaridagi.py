# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:40:07 2021

@author: Premium
"""
"""
#1 va 2
gullar=["lola","nilufar","boychechak","rayhon","atirgul"]
i=0
for gul in gullar:
    i+=1
    print(gul)
print("Kod",i," marta takrorlandi")

#3
sonlar=list(range(10,100+1))
for son in sonlar:
    print(f"{son}, ning kubi {son**3} ga teng")

#4
kinolar=[]
for n in range(5):
    print("kino nomilarini kiritamiz ")    
    kinolar.append(input(f"{n+1}-kino nomini kiriting: "))
print(kinolar)


n=int(input("bugun necha kishi bilan uchrashdiz?  "))
uchrashganlar=[]
for a in range(n):
    uchrashganlar.append(input(f"{a+1}-uchrashgan insoniz:"))
print(uchrashganlar)
"""

n=int(input("Nechta do'stiz bor ?__ "))
dostlar=[]
for a in range(n):
    dostlar.append(input(f"{a+1}-si :    "))
print(dostlar)
if n<5:
    print("Eee aldang kamuuu qo'shing hay ")
else:
    print("Ha yaxshi boladi")