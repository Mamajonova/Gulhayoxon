# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:13:28 2021

@author: Premium
"""

#lambda argument: ifoda
import math
uzunlik =lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))

perimetr=lambda a,b,c:a+b+c
print(perimetr(2,3,4))

daraja=lambda x,y:x**y
print(daraja(3,2))

def daraja(n):
    return lambda x:x**n
kvadrat=daraja(2)
kub=daraja(3)
print(kub(3))
print(kvadrat(3))
print(round(3.44999,2))# yaxlitlab beradi

# 3 ta haqiqiy o'zaro teng bolmagan x,y,z sonlar yig'indisi 1 dan kichik bo'lsa
# 3 ta sonning eng kichigi qolganlari yig'indisining yarmisining yarmisi bilan almashtirilsin, 
# aks holda x va y kichigi qolganlarining yig'indisining yarmi bilan almashtirilsin


print("BIR BIRIGA TENG BOLMAGAN 3 TA SON KIRITING!!!")
x=float(input("1-son="))
y=float(input("2-son="))
z=float(input("2-son="))
print(x,y,z)
if(x!=y and y!=z and x+y+z<1 and x!=z):
    if(x<y and y<=z):
        print((y+z)/2,y,z)
    elif(y<x and x<=z):
        print(x,(x+z)/2,z)
    elif(z<x and x<=y):
        print(x,y,(x+y)/2)
    elif(x<z and z<=y):
        print((y+z)/2,y,z)
    elif(y<z and z<=x):
        print(x,(x+z)/2,z)
    elif(z<y and y<=x):
        print(x,y,(x+y)/2)
    else:
        print("boshqa son kiriting")
elif(x+y+z>=1 ):
    if(x<y and y<=z):
        print(x,(x+z)/2,(x+y)/2)
    elif(y<x and x<=z):
        print((y+z)/2,y,(x+y)/2)
    elif(z<x and x<=y):
        print((y+z)/2,(x+z)/2,z)
    elif(x<z and z<=y):
        print(x,(x+z)/2,(x+y)/2)
    elif(y<z and z<=x):
        print((y+z)/2,y,(x+y)/2)
    elif(z<y and y<=x):
        print((y+z)/2,(x+z)/2,z)
    else:
        print("boshqa sonlar kiriting.")
else:
    print("boshqa sonlar kiriting.")

def hisobla(x,y):
    return lambda a,b:a**x+b**y
s=hisobla(4, 3)
print(s(1,2))

from math import sqrt
sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))
print(ildizlar)

sonlar=list(range(10))
def daraja(x):
    return x*x
print(list(range(10)))
print(list(map(daraja,sonlar)))
    
    
    

 