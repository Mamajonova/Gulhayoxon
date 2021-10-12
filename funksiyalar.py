# lambda ifodalar funksiyalar ma'lum bir vazifani bajaradigan va dasturning boshqa qismlarida qayta ishlatilishi mumkin bolgan kod blagini ifodalaydi
# def funksiya_nomi (parametr1, parametr2):
#     amallar
# funksiya nomi
def salom():
    print("Assalom -")
salom()
# pitonda o'zgaruvchilarni ko'rinish sohasi 2 xil 2-lokal 1-global
# global barcha funksiyalardan tashqarida aniqlangan bo'lib ixtiyoriy f-yalarning ichki sohasida foydalanishi mumkin
#masalan a="TM"
#def salom():
 #   print("Assalom -")
#salom()
a="TM"
def salom():
    print("Assalom -",a)
salom()
# pitonda lakal o'zgaruvchilar o'zi aniqlangan funksiyaning ichki sohasida yani ta'na sohasida ishlatilishi mumkin
def Kirish():
    a='TM'
    print(a,'ikkichilar')
Kirish()
# global va lakal bir xil nomga ega bolsa u holda lokal o'zgaruvch o'zining o'zgarish sohasida globalni yashirib qo'yadi
a='Tm'
def Kirish():
    a='tm'
    print(a,'ikkichilar')
Kirish()
#Agar funksiyalar ichida global o'zgaruvchining qiymatini o'zgartirish talab etilsa u holda global kalit so'zidan foydalaniladi
a='tmi'
def Kirish():
    global a
    a='TMI'
    print('Assalom',a)
Kirish()
#pitonda lambda funksiyalar nomga ega bolmagan funksiyalarni bildiradi.Anonim funksiyalar deb ham ataladi. Standart nomga ega bolmagan funksiyalar lambda funksiyalar d-di
# lambda funksiyalar 3 xil boladi
# 1-lambda funksiya boshqa funksiyaga argument sifatida uzatilishi mumkin
# 2-lambda funksiyani qiymat sifatida boshqa funksiya qaytarishi mumkin
# 3- bir marta qo'llaniladigan funksiyalarni lambda funksiyalar orqali ifodalash mumkin
lambda argumentlar:"natijalar"
def funk(x):
    return lambda y:y**x
def funk1(f,x):
    print('x=',x,'f(x)=',f(x))
m=lambda x:x*2+x
funk1(m,0.5)
funk1(lambda x:1/(x+2),2.0)
z=1+((lambda x,y:(x+y)/3)(12,3)**2)
print(z)
print(funk(2)(3))
#modullar pitonda modullar alohida faylda yozilgan va boshqa dasturlarda qayta qo'llanilishi mumkin bolgan kodlar majmui
#modullarni hosil qilish uchun .py kengaytmali fayl ochiladi va unga bir yoki bir nechta funksiyalar yoziladi
def Summa(n):
    s=0
    for i in range(n+1):
        s+=i
        return  s
def Faktorial(n):
    if n==1 or n==0:
        return 1
    return n*Faktorial(n-1)
print(Summa(5))
print(Faktorial(3))