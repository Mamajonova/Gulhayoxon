# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 13:42:59 2021

@author: Premium
"""

lugat={
       "apple":"olma",
       "green":"yashil",
       "banana":"banan",
       "orange":"to'q sariq",
       "pink":"pushti",
       "home":"uy",
       "dear":"ayiq",
       "apricot":"o'rik"}
a=lugat.values()
b=list(a)
print(b)
n=lugat.keys()
g=list(n)
print(g)
for i in sorted(lugat.values()):
    print(i)
for j in sorted(lugat.keys()):
    print(j)
    
davlatlar={
    "O'zbekiston":"Toshkent",
    "Qozog'iston":"Nur-Sulton",
    "Tojikiston":"Dushanbe",
    "Qatar":"Doha",
    "Pokiston":"Islomobod",
    "Xitoy":"Pekin",
    "Yaponiya":"Tokio"}
for i in sorted(davlatlar.values()):
    print(i)
for j in sorted(davlatlar.keys()):
    print(j)
n=input("Osiyo davlatlari nomini kiriting: ")
if n in davlatlar:
    print("Pytaxti",davlatlar[n])
else:
    print("Bizda bunday davlat nomi yoq")
    
menyu={
    "osh":20000,
    "norin":30000,
    "lag'mon":15000,
    "manti":4000,
    "somsa":3000,
    "shashlik":10000,
    "xonim":12000,
    "salat":5000,
    "choy":1000,
    "sharbat":8000,
    "non":3000}
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menyu:
        print(buyurtma,menyu[buyurtma],"so'm")
    else:
        print("Kechirasiz, bizda",buyurtma,"yoq")


