#Qatorlar va qatorlar ustida amallar . Matematika sinfi
import math
print(math.ceil(1.1))# sonni yuqoriga qarab yaxlitlash    2
print(math.ceil(-1.1)) # javob -1
print(math.fabs(-1.1))# sonni absalut qiymatini hisoblaydi javob 1.1
print(math.factorial(0)) # berilgan songacha bo'lgan faktorialni hisoblaydi javob 0
print(math.floor(23.11))# sonni pastga qarab yaxlitlaydi
print(math.frexp(3))     # berilgan x sonini x=m*2**n m va n larni topadi
print(math.fsum([2,3,2.4,-34]))    # haqiqiy turdagi ketma-ketlik elementlari yig'indisi
print(math.isinf(float("inf")))   # bu holatda True qiymat beradi
print(math.isinf(float("-inf")))  # bu holatda true qaytaradi
#print(math. isinf(math. nan))# xotiraga sig'masa xatolik beradi
print(math.ldexp(3,2)) # x*2^i ni hisoblaydi (x,i)
print(math.modf(100.12))  # raqamni haqiqiy va butun qismini qaytaradi
print(math.modf(-100.12))
print(math.trunc(12.34))   # x sonining butun qismini chiqaradi
print(math.trunc(-12.34))  # manfiy bolsa ham butun qismini qaytaradi yaxlitlamaydi
print(math.exp(2))     # e darajaga ko'ra hisoblab chiqaradi
print(math.log(14))  # logarifm e asosga ko'ra chiqaradi
print(math.log(125,5)) # log 5 asosga ko'ra 125 ni hisoblaydi taqribiy hisoblaydi
print(math.pow(2,3))  # 2 ni 3- darajasi
print(math.sqrt(4))  # sonni ildizini chiqaradi
print(math.asin(1))  # radianda chiqarib berasi arcsinusni
print(math.atan(0))
print(math.atan2(2,3))
print(math.acos(1))
print(math.hypot(2,3))  # sqrt(x**2+y**2) ni hisoblaydi
print(math.degrees(3)) #radiandan gradusga o'tish
print(math.radians(13)) # gradusdan radianga o'tish
x=16.55*10**(-3)
y=-2.75
z=0.15
B=math.sqrt(10*(x**(1/3))+math.pow(x,y+2))*(((math.asin(z))**2)-math.fabs(x-y))
print(B)
x=float(input("x="))
y=float(input("y="))
z=float(input("z="))
a=(2*math.cos(x-math.pi/6))/(1/2+math.sin(y))
b=1+z*z/(3+z*z/5)
print(a,b)
