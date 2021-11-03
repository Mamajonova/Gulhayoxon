# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:33:47 2021

@author: Premium
"""

#a=input("1-sonni kiriting: ")
#b=int(input("2-sonni kiriting: )) # qo'shtirnoq yopilmay qoldi sintaksis xatolik
            
try:
    a=int(input("1-son: "))    # a ni int deb kiritdik 
                              #qiymat berayotganda floatga tegishli son kiritdik
    b=int(input("2-son: "))   #natijada xatolik berdi
    print(a/b)
except:
    print("Xatolik")
    
    
#a=input("Salom hammaga!")
# print(a)       # joy qogizib ketilgani uchun indentationError yuzaga keldi
  
#prnt("gggg")  nameerror nom berishdagi xatoliklar


#ismlar=["ali","vali","g'ani"]
#print(ismlar[3])      # index bilan bog'liq xatolik IndexError chunki 3-indeksli ifoda yoq

try:
    a=3
    b=0
    print(a/b)
except:
    print("Nolga bolishda xatolik")



    
