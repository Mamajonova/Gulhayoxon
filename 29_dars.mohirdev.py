# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:38:02 2021

@author: Premium
"""

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
    def get_info(self):
        return f"{self.ism}{self.familiya}. {self.bosqich}-bosqich talabasi"
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def set_bosqich(self,yangi_bosqich):  # talabaning kursini yangilovchi metod
        self.bosqich=yangi_bosqich
    def update_bosqich(self):
        self.bosqich +=1
    # get xususiyatlarni ko'rsatuvchi
    # set xususiyatlarni o'zgartiruvchi
    
    
    
class Fan():
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni +=1 # qo'shganimizdan so'ng talabalar sonini bittaga oshiradi
    def get_name(self):
        return self.nomi
    def get_students(self):
        return[x.get_info() for x in self.talabalar]
    def get_students_num(self):
        return self.talabalar_soni
def see_methods(klass):
    return[method for method in dir (klass) if method.startswith('__')]
matematika=Fan("Oliy matematika")
talaba1=Talaba("Alijon","Valiyev",2000)
talaba2=Talaba("Hasan","Alimov",1999)
talaba3=Talaba("Akrom","Boriyev",2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
print(matematika.talabalar_soni)
print(matematika.talabalar)
mat_talabalar=matematika.get_students()
print(mat_talabalar)
   
class Avto:
    def __init__(self,model,rang,karobka,narx):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.narx=narx
        self.kilometr=0
    def get_info(self):
        return f"Modeli:{self.model},Rangi:{self.rang},Karobkasi:{self.karobka},Narxi:{self.narx}"
        
    def update_kmmasofa(self,km):
        self.km+=km
class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobillar):
        self.salon_nomi=salon_nomi
        self.manzili=manzili
        self.sotuvdagi_avtomobillar=sotuvdagi_avtomobillar
    def get_name(self):
        return self.salon_nomi
    def add_kmmasofa(self,km):
        self.kmmasofa+=km
avtosalon1=Avtosalon("AvtoMotors", "Toshkent", "Nexia,Cobalt")
avto1=Avto("Damas","Oq","GM",12000) 
print(avto1.get_info())
 