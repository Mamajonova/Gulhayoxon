#NESTING
# bir narsani ichida boshqa narsa joylash
car0={'model':'lacetti',
      'rang':'oq',
      'yil':2018,
      'narh':13000,
      'km':50000,
      'karobka':'avtomat'
      }
car1={'model':'nexia 3',
      'rang':'qora',
      'yil':2015,
      'narh':9000,
      'km':89000,
      'karobka':'mexanika'
      }
car2={'model':'gentra',
      'rang':'qizil',
      'yil':2019,
      'narh':15000,
      'km':20000,
      'karobka':'mexanika'
      }
car=car0
print(car['model'].title(),car['rang'],"rang",car['yil'],"-yil",car['narh'],"$",car['km'],'km',car['karobka'],'karobka')
car=car1
print(car['model'].title(),car['rang'],"rang",car['yil'],"-yil",car['narh'],"$",car['km'],'km',car['karobka'],'karobka')
car=car2
print(car['model'].title(),car['rang'],"rang",car['yil'],"-yil",car['narh'],"$",car['km'],'km',car['karobka'],'karobka')
cars=[car0,car1,car2]
for car in cars:
    print(car['model'].title(), car['rang'], "rang", car['yil'], "-yil", car['narh'], "$", car['km'], 'km',
          car['karobka'], 'karobka')
malibus=[]
for n in range(10):
    new_car={
        'model':'malibu',
        'rang':None,
        'yil':2021,
        'km':0,
        'karobka':'avto'
    }
    malibus.append(new_car)
    #print(malibus)
for malibu in malibus[:3]:
    malibu ['rang']='qizil'
# for malibu in malibus:
#     print(malibu)
for malibu in malibus[3:6]:
    malibu ['rang']='qizil'
for malibu in malibus[6:]:
    malibu ['rang']='qora'
    malibu['karobka']='mexanika'
# for malibu in malibus:
#     print(malibu)
for malibu in malibus:
    if malibu['karobka']=='avto':
        malibu['narh']=40000
    else:malibu['narh']=35000
for malibu in malibus:
     print(malibu)

dasturchilar={
    'ali':['phyton','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['phyton','php'],
    'maryam':['c++','c#']
}
for ism,tillar in  dasturchilar.items():
    print(ism.title(),"quyidagi dasturlash tillarini biladi.")
    for til in tillar:
        print(til.upper())
for ism,tillar in  dasturchilar.items():
    print("\n",ism.title(),"quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper(),' ')

# hamkasiblar={
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            "tillar":  ["phyton", "c++"]
#             },
#     'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':"o'rta-maxsus",
#            "tillar":  ["html", "css","js"]
#             },
#     'hasan':{'familiya':'husanov',
#            'tyil':1999,
#            'malumot':'maxsus',
#            "tillar":  ["phyton", "php"]
#             }
#
# }
# for ism,info in hamkasiblar.items():
#     print(info['ism'].title(),info['familiya'].title(),info['tyil'].title(),"-yilda tug'ilgan.","Ma'lumoti:",info['malumot'],"Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
#         print(hamkasiblar)

Islom_Karimov={"sharifi":"Abdug'anivich",
      'millati':"o'zbek",
      'tyil':1938,
      'turmush_ortogi':"Tatyana_Karimova",
      'farzandlari_soni':3,
      't_joyi':'Samarqand'
      }
Shavkat_Mirziyoyev={"sharifi":"Miromonivich",
      'millati':"o'zbek",
      'tyil':1957,
      'turmush_ortogi':"Ziroatxon_Mirziyoyeva",
      'farzandlari_soni':3,
      't_joyi':'Jizzax'
     }

prezident=Islom_Karimov
 #print(prezident["sharifi"].title(),prezident['millati'],prezident['tyil'],prezident['turmush_ortogi'],prezident['farzandlari_soni'],prezident['t_joyi'])
prezident=Shavkat_Mirziyoyev
# print(prezident["sharifi"].title(),prezident['millati'],prezident['tyil'],prezident['turmush_ortogi'],prezident['farzandlari_soni'],prezident['t_joyi'])
prezidents=[Islom_Karimov,Shavkat_Mirziyoyev]
# #for prezident in prezidents:
#      shrifi=prezident["sharifi"]
#      millati=prezident['millati']
#      tyil=prezident['tyil']
#      turmush_ortogi=prezident['turmush_ortogi']
#      farzandlari_soni=prezident['farzandlari_soni']
#      t_joyi=prezident['t_joyi']
#      print(prezident["sharifi"].title(), prezident['millati'], prezident['tyil'], prezident['turmush_ortogi'], prezident['farzandlari_soni'],prezident['t_joyi'])

Islom_Karimov["kitobi"]="Yuksak ma'naviyat yengilmas kuch"
print(Islom_Karimov)
Shavkat_Mirziyoyev["kitobi"]="Niyati ulug' xalqning-ishi ham ulug',hayoti yorug' va kelajagi farovon bo'ladi"
print(Shavkat_Mirziyoyev)









