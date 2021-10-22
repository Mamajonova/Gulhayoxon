def salom_ber():
    print("Assalomu alaykum!")


salom_ber()


def salom_ber(ism):
    print("Assalomu alaykum, hurmatli ", ism.title())


salom_ber("Gulhayo")


def toliq_ism(ism, familiya):
    print("Foydalanuvchi ismi:", ism.title(), "\n", "Foydalanuvchi familiyasi: ", familiya.title())


toliq_ism("Gulhayo", "Mamajonova")


def yosh_hisoblash(ism, tugilgan_yil):
    print(ism.title(), 2021 - tugilgan_yil, "yoshda")


yosh_hisoblash("Gulhayo", 2000)
# yosh_hisoblash(2000,"Gulhayo")  xatolik beradi int va string joyi almashib qoldi
yosh_hisoblash(tugilgan_yil=2000, ism="Gulhayo")  # bu holatda o'rni almashsa ham xatolik bermaydi


def yosh_hisoblash(tugilgan_yil, joriy_yil=2021):
    print("Siz ", joriy_yil - tugilgan_yil, " yoshdasiz")


yosh_hisoblash(2003, 2020)
yosh_hisoblash(2002)  # joriy yil kiritilmasa ham hisoblay veradi funksiya ichida 2021 deb qiymat berib qo'yganmiz

# ism va yosh kiritilgan holda tug'ilgan yilini chiqarib beradi
def yosh_va_ism_hisoblash(ism, yosh):
    print(ism.title(), 2021 - yosh, "-yilda tug'ilgansiz")
yosh_va_ism_hisoblash("guli",5)

# son olib uni kvadratini va kubini konsolga chiqaramiz
def kvga_oshirish(son):
    print(son,"berilgan son")
    print(son**2,"kvadrati")
    print(son**3,"kubi")
kvga_oshirish(6)

# son olib juft yoki toqligini konsolga chiqaramiz
def juf_yoki_toqligini_aniqlash(son):
    print(son)
    if son%2==0:
        print("juft son")
    elif son%2==1:
        print("toq son")
    else:
        print("xatolik boshqa son kiriting")
juf_yoki_toqligini_aniqlash(78)

# sonni konsolga chiqarish
def sonni_chiqarish(x,y):
    print("x=",x)
    print("y=",y)
    print("y ni kvadrati=",y**2)
sonni_chiqarish(4,5)



def sonni_bolinishi(son):
    print(son)
    if son%2==0:
        print(son,"son 2 ga qoldiqsiz bo'linadi")
    if son%3==0:
        print(son,"son 3 ga qoldiqsiz bo'linadi")
    if son%4==0:
        print(son,"son 4 ga qoldiqsiz bo'linadi")
    if son%5==0:
        print(son,"son 5 ga qoldiqsiz bo'linadi")
    if son%6==0:
        print(son,"son 6 ga qoldiqsiz bo'linadi")
    if son%7==0:
        print(son,"son 7 ga qoldiqsiz bo'linadi")
    if son%8==0:
        print(son,"son 8 ga qoldiqsiz bo'linadi")
    if son%9==0:
        print(son,"son 9 ga qoldiqsiz bo'linadi")
    if son%10==0:
        print(son,"son 10 ga qoldiqsiz bo'linadi")
    else:
        print("xatolik, boshqa son kiritib ko'ring!")
sonni_bolinishi(360)


def sonni_bolish(son):
    for n in range(2,11):
        if not son%n:
            print(son,n,"ga qoldiqsiz bo'linadi")
sonni_bolish(450)



