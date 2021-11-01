# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:38:35 2021

@author: Premium
"""

users=["Tom","bob"]
users.append("Alise")
print(users)
users.insert(1,"bill")
print(users)
users.remove("bob")
print(users)
users.pop(0)
print(users)
users.clear()
print(users)

us=["tom","bob","alise"]
item="bob"
if item in us:
    us.remove(item)
print(us)
us.count("alise")
ism=["Tom","Bob","Alise","bob"]
ism.sort()
print(ism)
ism.reverse()
print(ism)
sorted(ism,key=str.lower)
print(ism)
import copy

users1=["Tom","Bob","Alice","bob"]
users2=copy.deepcopy(users1)
users2.append("Garri")
print(users1)
print(users2)
users3=users1[:2]
print(users3)
users4=users1[2:4]
print(users4)
users5=users1[1:5:2]
print(users5)
a=["guli","nilu"]
b=["a","b"]
print(a[0]+b[0])

ishchi=[
        ["bobur",20],
        ["tohir",25],
        ["sobir",30]
        ]
print(ishchi[0])
ishchi1=list()
ishchi1.append("rustam")
ishchi1.append(31)
ishchi.append(ishchi1)
print(ishchi[-1])
ishchi[-1].append("+999")
ishchi.pop[-1]
ishchi[0]=["sobir",18]


















