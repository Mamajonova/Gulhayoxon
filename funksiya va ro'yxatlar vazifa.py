# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:21:55 2021

@author: Premium
"""

def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism} ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar=["Gulhayo",'Hilola',"Ra'no"]
baholar=bahola(talabalar[:])
print(baholar)
print(talabalar)

#funksiya va ro'yxat 1-misol
def bosh_harf_bilan_yozmoq(matnlar):
    ruyxatlar={}
    while matnlar:
        matn=matnlar.pop()
        matn1=matn.title()
        print(f"{matn} ni bosh harf bilan yozish",matn1)
        ruyxatlar[matn]=matn1
    return ruyxatlar
ruyxatlar1=["ona yer","ota va ona","muqaddas tuproq"]
ruyxatlar=bosh_harf_bilan_yozmoq(ruyxatlar1[:])
print(ruyxatlar)
        
  #3-misol
talabalar=["ali","vali","hasan"]
def bahola(ismlar):
    ismlar={}
    for ism in ismlar:
        baho=input(f"Talaba {ism} ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
baholar=bahola(talabalar[:])
print(baholar)

    
        