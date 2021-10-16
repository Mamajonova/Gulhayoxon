from math import *

hafta_kunlari={1:'Dushanba',2:'Seshanba',3:'Chorshanba',4:'Payshanba',5:'Juma',6:'Shanba',7:'Yakshanba'}
print(hafta_kunlari)
print(hafta_kunlari[1])
print(hafta_kunlari[2])
print(hafta_kunlari[3])
print(hafta_kunlari[4])
print(hafta_kunlari[5])
print(hafta_kunlari[6])
print(hafta_kunlari[7])
h=int(input("1 dan 7 gacha son kiriting: "))
if h==1:
    print("Dushanba")
elif h==2:
    print("Seshanba")
elif h==3:
    print("Chorshanba")
elif h==4:
    print("Payshanba")
elif h==5:
    print("Juma")
elif h==6:
    print("Shanba")
elif h==7:
    print("Yakshanba")
else:
    print("noto'g'ri son kiritdiz!")


k=int(input("Siz necha bahoga o'qisiz? "))
if h==1:
    print("yomon baho")
elif h==2:
    print("qoniqarsiz baho")
elif h==3:
    print("qoniqarli baho")
elif h==4:
    print("yaxshi baho😀")
elif h==5:
    print("a'lo ✰")
else:
    print("xatolik! 1 dan 5 gacha son kiriting")

oy=int(input("Nechanchi oyda tug'ilgansiz?"))
if oy==1:
    print("Qish faslida tug'ilgan ekansiz🎂")
elif oy == 2:
    print("Qish faslida tug'ilgan ekansiz🎂")
elif oy==3:
    print("Bahor faslida tug'ilgan ekansiz🎂")
elif oy==4:
    print("Bahor faslida tug'ilgan ekansiz🎂")
elif oy==5:
    print("Bahor faslida tug'ilgan ekansiz🎂")
elif oy==6:
    print("Yoz faslida tug'ilgan ekansiz🎂")
elif oy==7:
    print("Yoz faslida tug'ilgan ekansiz🎂")
elif oy==8:
    print("Yoz faslida tug'ilgan ekansiz🎂")
elif oy==9:
    print("Kuz faslida tug'ilgan ekansiz🎂")
elif oy==10:
    print("Kuz faslida tug'ilgan ekansiz🎂")
elif oy==11:
    print("Kuz faslida tug'ilgan ekansiz🎂")
elif oy==12:
    print("Qish faslida tug'ilgan ekansiz🎂")
else:
    print("Voy axir bir yil 12 oyku ")


oy_sanasi=int(input("Sizga nechanchi oy kerak:"))
if oy_sanasi==1:
    print("Yanvar 31 kundan iborat")
elif oy_sanasi==2:
    print("Fevral 28 kundan iborat agar hozirgi yil 4 ga qoldiqsiz bo'linadigan son bolsa 29 kundan iborat")
elif oy_sanasi==3:
    print("Mart 31 kundan iborat")
elif oy_sanasi==4:
    print("Aprel 30 kundan iborat")
elif oy_sanasi==5:
    print("May 31 kundan iborat")
elif oy_sanasi==6:
    print("Iyun 30 kundan iborat")
elif oy_sanasi==7:
    print("Iyul 31 kundan iborat")
elif oy_sanasi==8:
    print("Avgust 31 kundan iborat")
elif oy_sanasi==9:
    print("Sentabr 30 kundan iborat")
elif oy_sanasi==10:
    print("Oktabr 31 kundan iborat")
elif oy_sanasi==11:
    print("Noyabr 30 kundan iborat")
elif oy_sanasi==12:
    print("Dekabr 31 kundan iborat")
else:
    print("bir yil 12 oydan iborat")


A=float(input("A="))
B=float(input("B="))


print("ikki son yig'indisi=",A+B)
print("ikki son ayirmasi=",A-B)
print("ikki son ko'paytmasi=",A*B)
print("ikki son bo'linmasi=",A/B)

uzunlik={ 1:'milimetr',2:'santimetr',3:'detsimetr',4:'kilometr'}
print(uzunlik)
print ("tepadagi ma'lumotlarga ko'ra 1 dan 4 gacha ixtiyoriy son kiriting:")
e=int(input("son kiritng:"))
f=float(input("metrni boshqa uzunlik birligiga o'tkazamiz necha metr="))
print(f," metr")
if e==1:
    print(f*0.001," millimetr")
elif e==2:
    print(f*0.01," santimetr")
elif e==3:
    print(f*0.1," detsimetr")
elif e==4:
    print(f*1000," kilometr")
else:
    print("xatolik!!! Shartga ko'ra boshidan harakat qiling!")


ogirlik={ 1:'miligramm',2:'gramm',3:'tonna',4:'sentner'}
print(ogirlik)
print ("tepadagi ma'lumotlarga ko'ra 1 dan 4 gacha ixtiyoriy son kiriting:")
e=int(input("son kiritng:"))
f=float(input("kilogramni boshqa ogirlik birligiga o'tkazamiz necha kilogramm="))
print(f," kilogram")
if e==1:
    print(f*0.000001," milligramm")
elif e==2:
    print(f*0.001," gramm")
elif e==3:
    print(f*1000," tonna")
elif e==4:
    print(f*100," sentner")
else:
    print("xatolik!!! Shartga ko'ra boshidan harakat qiling!")

print("shimol,janub ,g'arb,sharqdan birini kirit")
n=input("yo'nalishni kirit:")
if n=="shimol":
    print("men shimolga qarab turibman")
    m=int(input("1 o'ngga 2 chapga 3 orqaga 1 dan 3 gacha bitta son kiriting:"))
    if m==1:
        print(" o'ngga burilib sharqqa qaradiz")
    elif m==2:
        print("chapga burilib g'arbga qaradiz")
    elif m==3:
        print("180 gradusga burilib janubga qaradiz")
    else:
        print("xatolik 1 dan 3 gacha son kiriting!!!")
elif n=="janub":
    print("men janubga qarab turibman")
    m=int(input("1 o'ngga 2 chapga 3 orqaga 1 dan 3 gacha bitta son kiriting:"))
    if m==1:
        print(" o'ngga burilib g'arbga qaradiz")
    elif m==2:
        print("chapga burilib sharqqa qaradiz")
    elif m==3:
        print("180 gradusga burilib shimolga qaradiz")
    else:
        print("xatolik 1 dan 3 gacha son kiriting!!!")
elif n=="g'arb":
    print("men g'arbga qarab turibman")
    m=int(input("1 o'ngga 2 chapga 3 orqaga 1 dan 3 gacha bitta son kiriting:"))
    if m==1:
        print(" o'ngga burilib shimolqa qaradiz")
    elif m==2:
        print("chapga burilib janubga qaradiz")
    elif m==3:
        print("180 gradusga burilib sharqga qaradiz")
    else:
        print("xatolik 1 dan 3 gacha son kiriting!!!")
elif n=="sharq":
    print("men sharqga qarab turibman")
    m=int(input("1 o'ngga 2 chapga 3 orqaga 1 dan 3 gacha bitta son kiriting:"))
    if m==1:
        print(" o'ngga burilib janubga qaradiz")
    elif m==2:
        print("chapga burilib shimolga qaradiz")
    elif m==3:
        print("180 gradusga burilib g'arbga qaradiz")
    else:
        print("xatolik 1 dan 3 gacha son kiriting!!!")
else:
    print(" xatolik!!! shimol,g'arb,sharqdan birini kiriting")

