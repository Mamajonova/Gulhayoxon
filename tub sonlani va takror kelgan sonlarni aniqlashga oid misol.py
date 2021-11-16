# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:19:21 2021

@author: Premium
"""

#(100 ; 1000)gacha oraliuq berilgan raqamlari takrorlanmaganlarini chiqarsin masalan 110 ni 202 larni chiqarmasin
s=list()
i=100
while i<=999:
    a=i%10
    b=(i//10)%10
    c=i//100
    if a!=b and a!=c and b!=c:
        s.append(i)
    i+=1
user=tuple(s)
print(user)







# (a,b) oraliq berilgan orasidagi tub sonlarni topish
a=int(input("a="))

b=int(input("b="))

sonlar=list(range(a,b+1))

k=0

for son in sonlar:
    
    sonlar1=list(range(2,son+1))
    
    s=0
    
    for son1 in sonlar1:
        
        if son %son1==0:
            
            s+=1
            
    if s==1:
        
        print(son)
        
        k+=1
print(k)    
        









