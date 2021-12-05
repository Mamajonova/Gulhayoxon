# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:15:37 2021

@author: Premium
"""

mashxur1={
    "ismi_sharif":"Alisher Navoiy",
    "t_yili":1441,
    "yunalishi":"Shoir_yozuvchi",
    "ishlari":"Xamsa asari",
    "lavozimi":"Vazir"}
mashxur2={
    "ismi_sharif":"Ozodbek Nazarbekov",
    "t_yili":1974,
    "yunalishi":"Xonanda",
    "ishlari":"O'zbekiston,Lola qo'shiqlari",
    "lavozimi":"Sanat vaziri"}
mashxur3={
    "ismi_sharif":"Islom Karimov",
    "t_yili":1938,
    "yunalishi":"Davlat xizmati",
    "ishlari":"Yuksak ma'naviyat yengilmas kuch asari",
    "lavozimi":"Prezident"}
mashxurlar=[mashxur1,mashxur2,mashxur3]
for i in mashxurlar:
    print({i['ismi_sharif']})

mashxur1["t_shahri"]="Hirot"

mashxur2["t_shahri"]="Andijon"

mashxur3["t_shahri"]="Samarqand"
print(mashxurlar)
for i in mashxurlar:
    print({i['t_shahri']})
    

kinolar={
    "otam":["Urush va tinchlik","Terminator"],
    "onam":["Fotima va Zuhra","Novda"],
    "singlim":["Osmondagi bolalar","Malikaning kundaligi"],
    "ukam":["Zumrad tosh ortidan","Kichkina tabib"]
    }
for ism,kinolar in kinolar.items():
    print(ism,"ning sevimli kinolari: ")
    for kino in kinolar:
        print(kino)
        
davlatlar={
    "O'zbekiston":{"maydoni":"448,978",
                   "pul_birligi":"so'm",
                   "poytaxti":"Toshkent"
        },
    "Qozog'iston":{"maydoni":"2724,902",
                   "pul_birligi":"som",
                   "poytaxti":"Nur-Sulton"
        },
    "Qirg'iziston":{"maydoni":"198,500",
                   "pul_birligi":"so'm",
                   "poytaxti":"Bishkek"
        }
    }
    
print(davlatlar)
davlat=input("Davlat nomini kiriting: ")
if davlat in davlatlar:
    print(davlatlar[davlat])
else:
    print("Bizda bunday davlat yoq")
















    

