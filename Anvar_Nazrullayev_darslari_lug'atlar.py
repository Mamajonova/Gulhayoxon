# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:58:42 2021

@author: Premium
"""
otam={
      "ismi":"Turobjon",
      "t_yili":1978,
      "shahri":"Farg'ona"
      }

onam={
      "ismi":"Gulshodaxon",
      "t_yili":1979,
      "shahri":"Farg'ona"
      }

ukam={
      "ismi":"Qilichbek",
      "t_yili":2007,
      "shahri":"Farg'ona"
      }
singlim={
      "ismi":"Dilnoza",
      "t_yili":2004,
      "shahri":"Farg'ona"
      }
print(f"otamning ismi {otam['ismi']}, u {otam['t_yili']}-yilda tug'ilgan,{otam['shahri']}da")

sevimli_taomlar={
    "otam":"manti",
    "onam":"sho'rva",
    "ukam":"lag'mon",
    "singlim":"osh"}
print(f"Ukamning sevimli taomi {sevimli_taomlar['ukam']}")
print(f"Otamning sevimli taomi {sevimli_taomlar['otam']}")
print(f"Singlimning sevimli taomi {sevimli_taomlar['singlim']}")

python_lugat={
    "print":"chop qilib beruvchi funksiya",
    "if":"shart operatori",
    "string":"matnli qiymatlarni qabul qiluvchi tur",
    "int":"butun qiymat turi",
    "EOL":"qator oxirida xatolik yuz bersa ekranda chiqadigan so'z",
    "upper":"berilgan barcha harflarni bosh harifga o'tkazib beruvchi metod",
    "lower":"berilgan barcha so'zlarni kichik harfga o'tkazib beruvchi metod"}
n=input("sizga pythonga oid qanday so'z kerak: ")
if n in python_lugat:
    print(python_lugat[n])
else:
    print("uzur bizda bunday so'z mavjuda emas")
