# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:51:58 2021

@author: Premium
"""

def summa(*sonlar):
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi

print(summa(1,2))

def summa(*sonlar):
    return sum(sonlar)
print(summa(23,5554,67,321))   # *sonlarga istalgancha qiymat joylash mumkin

def summa(x,y,*sonlar):
    return x+y+sum(sonlar)
print(summa(3,4,65))   # bu yerga x va y majburiy argumentlar kiritdik

def avto_info(kompaniya,model,**malumotlar):
    malumotlar["kompaniya"]=kompaniya
    malumotlar["model"]=model
    return malumotlar
avto1=avto_info("GM","malibu",yili=2018,rang="qora",karobka="avtomat")
print(avto1)

def kopaytma(*kopaytuvchi):
    kk=1
    for i in kopaytuvchi:
        kk*=i
    return kk
print(kopaytma(1,4,6,34,-56))

def malumot(ism,familiya,**lugat):
    lugat["ism"]=ism
    lugat["familiya"]=familiya
    return lugat
m1=malumot("Gulhayo","Mamajonova",yil=2000,hudud="Farg'ona")
print(m1)
    
    
    
    
    
    
    
    
    