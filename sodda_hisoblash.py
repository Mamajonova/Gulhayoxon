# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum")
salom_ber()


def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}")
    
salom_ber("Guli")
salom_ber("ustoz")

def toliq_ism(ism,familiya):
    print(f"Foydalanuvchi ismi:{ism.title()}\n",
          f"Foydalanuvchi familiyasi:{familiya.title()}")
toliq_ism("Gulhayo", "Mamajonova")


def yosh_hisobla(ism,t_yil):
    print(f"{ism.title()},{2021-t_yil} yoshdasiz")
yosh_hisobla("Gulhayo",2015)
    
yosh_hisobla(t_yil=2016,ism="guli")

def yosh_hisobla(tugilgan_yil,joriy_yil=2021):
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
yosh_hisobla(1900,2020)
yosh_hisobla(1900)

def toliq_ism_yasa(ism,familiya):
    toliq_ism=f"{ism} {familiya}"
    return toliq_ism
talaba=toliq_ism_yasa("Olim", "Hakimov")
print(talaba)

def toliq_ism_yasa(ism,familiya, otasining_ismi=" "):
    if otasining_ismi:
        toliq_ism=f"{ism} {familiya} {otasining_ismi}"
    else:
        toliq_ism=f"{ism} {familiya}"
    return toliq_ism.title()
print(toliq_ism_yasa("Olim", "Hakimov","Nizom ugli"))






























