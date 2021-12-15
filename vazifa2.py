# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:20:23 2021

@author: Premium
"""
import math
try:
    def hisobla_komplex(a1,b1,a2,b2):
        """(a1+i*b1) va (a2+i*b2) komplex sonlarga oid qoshish, ayirish, ko'paytirish bolish amallari"""
        print(f"qoshish={a1+a2}+{b1+b2}i")
        print(f"ayirish={a1-a2}+{b1-b2}i")
        print(f"kopaytirish={a1*a2-b1*b2}+{a1*b2+b1*a2}i")
        print(f"{(a1*a2+b1*b2)/(a2*a2+b2*b2)}+{(-a1*b2++b1*a2)/(a2*a2+b2*b2)}i")
    hisobla_komplex(2, -3, -6, -8)
except ZeroDivisionError:
    print("xatolik")
except ValueError:
    print("xarolik")
finally:
    print("Dastur yakunlandi") 

















'''
def toliq_ism_yasa(ism,familiya):
    toliq_ism=f"{ism} {familiya}"
    print(toliq_ism)
toliq_ism_yasa("Hasan", "Husanov")


def toliq_ism_yasa(ism,familiya):
    toliq_ism=f"{ism} {familiya}"
    return toliq_ism

talaba=toliq_ism_yasa("Olim","Olimov")
print(talaba)

def toliq_ism_yasa(ism,familiya,otasining_ismi=''):
    """Toliq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism=f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism=f"{ism} {familiya}"
    return toliq_ism.title()
talaba1=toliq_ism_yasa("olim","hakimov")
talaba2=toliq_ism_yasa("olim", "hakimov","abrorivich")
print(talaba1)
print(talaba2)

print(f"Bugun darsga kelmadi: {talaba1},{talaba2}")

def avto_info(kompaniya,model,rang,karobka,yil,narh= None):
    avto={"kompaniya":kompaniya,
         "model":model,
         "rang":rang,
         "karobka":karobka,
         "yil":yil,
         "narh":narh}
    return avto
avto1=avto_info("GM","Malibu","Qora","Avtomat",2018)
avto2=avto_info("GM","Gentra","Oq","Mexanika",2015,15000)
print(avto1)
print(avto2)


def oraliq(min,max,qadam=1 ):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
print(oraliq(0,10,3))


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi malumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rang=input("Rangi: ")
    karobka=input("Karobka: ")
    yil=input("Yili: ")
    narh=input("Narhi: ")
    avtolar.append(avto_info(kompaniya,model,rang,karobka,yil,narh))
    javob=input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
print("\nSaloimizdagi avtolar:")
for avto in avtolar:
    if avto ['narh']:
        narh=avto['narh']
    else:
        narh="Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()} ,{karobka},karobka.Narhi: {narh}")
    '''
'''
def foydalanuvchi_malumot(ism,familiya,t_yil,manzil,email=None,tel_raqam=None):
    foydalanuvchi={"ism":ism,
                   "familiya":familiya,
                   "t_yil":t_yil,
                   "email":email,
                   "manzil":manzil,
                   "tel_raqam":tel_raqam }
    return foydalanuvchi
foydalanuvchi1=("Gulhayo","Mamajonova",2000,"Farg'ona")
print(foydalanuvchi1)


foydalanuvchilar=[]
while True:
    print("Quyidagi malumotlarni kiriting: ",end='')
    ism=input("Ismi: ")
    familiya=input("Familiya: ")
    t_yil=input("Tug'ilgan yili: ")
    manzil=input("Manzili: ")
    email=input("Email: ")
    tel_raqami=input("Tel_raqami:")
    foydalanuvchilar.append(foydalanuvchi_malumot(ism,familiya,t_yil,email,manzil,tel_raqami))
    javob=input("Yana foydalanuvchi qo'shasizmi (no/yes)")
    if javob=='no':
        break
print("Bizning foydalanuvchilar: ")
print(foydalanuvchilar)
'''
'''
def kottasini_topish(x,y,z):
    max=x
    if y>=max:
        max=y
    if z>=max:
        max=z
    return max
print(kottasini_topish(4.7, 3.21, -8))

def aylana_hisobla(r):
    aylana={"radius":r,
            "diametr":2*r,
            "perimetr":2*r*math.pi,
            "yuza":r*r*math.pi}
    return aylana
a=aylana_hisobla(5)
print(a)
'''
