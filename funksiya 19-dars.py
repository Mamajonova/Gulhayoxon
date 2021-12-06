# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:23:06 2021

@author: Premium
"""

def salom_ber(ism):
    '''foydalanuvchi ismini qabul qilib,unga salom beruvchi funksiya'''
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber("Gulhayo")
salom_ber("onajon")


def toliq_ism(ism,familiya):
    print(f"Foydalanuvchi ismi:{ism.title()}\n"
          f"Foydalanuvchi familiyasi:{familiya.title()}")
toliq_ism("Gulhayoxon","Mamajonova")


def yosh_hisobla(ism,tugilgan_yil):
    print(f"{ism.title()} {2021-tugilgan_yil} yoshda")
yosh_hisobla("Gulhayo",2000)

yosh_hisobla(ism="Hilola",tugilgan_yil=2001)


def ism_yosh(ism,yosh):
    """ism va yoshini kiritib tug'ilgan yilini chiqarib beruvchi dastur"""
    print(f"{ism.title()} {2021-yosh}-yili tug'ilgan")
ism_yosh("Gulhayo",21)

def darajaga_oshirish(son):
    """son olib kubi va kvadratini chiqaruvchi dastur"""
    print(f"{son} ning kvadrati {son**2},kubi {son**3}")
darajaga_oshirish(4)
darajaga_oshirish(-45)

def juft_toqqa_tekshirish(son):
    if son%2==0:
        print(f"{son} juft son")
    else:
        print(son," toq son")
juft_toqqa_tekshirish(23)
juft_toqqa_tekshirish((24))

def sonni_taqqoslash(a,b):
    """ikkita son kiritib ularni taqqoslash"""
    if a>b:
        print(a," kotta ",b," dan")
    elif(a<b):
        print(a," kichik ",b )
    else:
        print(a,"teng",b)
sonni_taqqoslash(3, 4)
sonni_taqqoslash(7, 1)
sonni_taqqoslash(10, 10)

def darajaga_oshirish(x,y):
    print(f"{x} ning {y}-darajasi ={x**y}")
darajaga_oshirish(5, 10)


def darajaga_oshirish(x,y=2):
    print(f"{x} ning {y}-darajasi ={x**y}")
darajaga_oshirish(5, 4)
darajaga_oshirish(4)

def sonni_bolish(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bolinadi")
sonni_bolish(320)


