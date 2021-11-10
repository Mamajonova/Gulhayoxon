# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:34:23 2021

@author: Premium
"""

class Talaba: # sinf nomi iloji boricha boish harf bn berish kk ajralib turishi uchun
    def __init__(self,ism,familiya,tyil): # xususiyatlar familiya ism tyil
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
    def get_name(self):  #get_name metod def funksiya
        return self.ism
    def get_age(self,yili):
        return yili-self.tyil
    def tanishtir(self):  # tanishtir metod
        return f"Ismim {self.ism} familiyam {self.familiya},tug'ilgan yilim {self.tyil}"
talaba1=Talaba("Gulhayo","Mamajonova",2000)# talaba1 talaba2 lar bular obektlar
talaba2=Talaba("Sevinch","Muminova",1980)
talaba3=Talaba("Hasan","Husanov",2003)
talaba4=Talaba("olim","Olimov",1990)
print(talaba1.ism)







class User:
    def __init__(self,ism,familiya,email,tel_nomer,parol):
        self.ism=ism
        self.familiya=familiya
        self.email=email
        self.tel_nomer=tel_nomer
        self.parol=parol
    def __str__(self):
        return "Ismi: {}, Familiyasi: {},Emaili: {}, Tel_nomeri: {}, Paroli: {}".format(self.ism,self.familiya,self.email,self.tel_nomer,self.parol)
    
    def get_info(self):
        return f"Ismim {self.ism} Familiyam {self.familiya} emailim {self.email} tel nomer+998{self.tel_nomer} parol {self.parol} "
foydalanuvchi1=User("Gulhayo","Mamajonova","@gulhayo20gmail.com",941601237,"guli20")
foydalanuvchi2=User("Hilola","Bahriddinova","@bahriddinovagmail.com",935761309,"hilol")






















#class Odam:
#    def __init__(self,ismi):
#        self.ismi=ismi
#odam1=Odam("Guli")
#print(odam1.ismi)
        