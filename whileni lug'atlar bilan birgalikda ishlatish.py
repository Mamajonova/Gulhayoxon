# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:36:27 2021

@author: Premium
"""
'''
print("Buyurtmalarni qabul qilamiz. ")
buyurtmalar=[]
n=1#buyurtmalarni sanash
while True:
    savol=f"{n}-buyurtmani nomini kiriting: "
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    takrorlash=input("Yana nimanidir buyurtma qilasizmi? (ha/yo'q)")
    n+=1
    if takrorlash!='ha':
        break
print("Buyurtmalar qabul qilindi")
'''
'''
print("Maxsulotlani narxini kiritamiz. ")
maxsulotlar={}
ishora=True
while ishora:
    maxsulot=input("Maxsulotlarni nomini kiriting: ")
    narx=input(f"{maxsulot}ning narxini kiriting: ")
    maxsulotlar[maxsulot]=int(narx)
    savol=input("Yana maxsulot qo'shasizmi? (ha/yo'q)")
    if savol=="yo'q":
        ishora=False
print(maxsulotlar)
#for maxsulot,narx in maxsulotlar.items():
#   print(f"{maxsulot.title()} {narx} narxda")
'''
    
buyurtmalar=["daftar","kitob","ruchka","qalam","chizg'ich","marker","bo'yoq"]
maxsulotlar={"daftar":3000,
             "ruchka":1000,
             "qalam":2000,
             "chizg'ich":4000,
             "marker":6000,
             "bo'yoq":10000
}
while maxsulotlar:
    maxsulot=input("Maxsulotning nomini kiriting: ")
    if maxsulot in maxsulotlar:
        print(maxsulotlar[maxsulot],"so'm")
    else:
        print(f"bizda {maxsulot} yoq")
        
    

        
    
