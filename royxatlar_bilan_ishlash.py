#Ro'yxatlar bilan ishlash
#Phyton dasturlash tilida ruyxatlar [ ] qavslar ichida turli xil turdagi o'zgaruvchilarni
# qabul qila oladigan maxsus turga aytiladi
# Masalan list1=[1,2,3,4.24,"tmi"]
#Phyton dasturlash tilida list turidagi massivlar indexsi 0 dan boshlanib -1 bilan tugaydi.
#va quyidagi amallarni qo'llab quvvatlaydi
list1=[1,2,3,4.23,"tmi"]
list2=[1,-3,-4.05]
print(list1+list2)
print(list1*2+list2*3)# ko'paytirib chiqarib beradi
print(list1[2:5])
#Ruyxatni butun (1...cheksiz)songa ko'paytirish
s=[1]*6
print(s)# 6 ta bir chiqadi
#Biror bir takrorlanuvchi sonni n marta yozmoqchi bo'lganda yordam beradi
#Bundan tashqari sonlar ketma-ketligini range funksiyasi yordamida hosil qilish ham mumkin
#Range funksiyasining 3 xil xolati mavjud
#1- range(end)
n=list(range(6))
print(n)
#2-range(start,end)
#startdan n endgacha bolgan sonlar ketma-ketligini qabul qiladi
b=list(range(3,6))
print(b)
#3-range(start,end,step) startdan endgacha bolgan sonlar step qadami bilan e'lon qilinadi
n=list(range(2,6,2))
print(n)

#Ruyxatdagi elementlarni birma bir chiqarish
tmi=["ikkichi","a'lochi","aqilli"]
for t in tmi:
    print(t)
tmi=["ikkichi","a'lochi","aqilli"]
i=0
while i<len(tmi):
    print(tmi[i])
    i+=1


#Ruyxatlar bilan ishlash uchun qo'llaniladigan funksiyalar
#append(item) ruyxat oxiriga item elementini qo'shadi
t=["tmi","iat"]
print(t.append("atmdt"))
#insert(index,item) ro'yxatga indesi bo'yicha item elementini qo'shish
print(t.insert(2,"IT"))
#removee(item) ruyxatdan item elementini o'chirish ushbu funksiya ruyxatdagi 1- uchragan item elementini o'chiradi

#Agar bunda element ruyxatda mavjud bolmasa ValueError istisno holati ro'y beradi.
#clear ruyxatdagi barcha elementlarni o'chirish
# index joylashgan indexsi bo'yicha o'chirish.Value Error xtolik yuz beradi
print(t.index("tmi"))
#pop([index]) indeksi bo'yicha elementni o'chiradi va qiymat sifatida qaytaradi
#Agar ko'rsatilgan index ko'rsatilmasa ruyxatdan elementni o'chiradi va qiymat sifatida qaytaradi
#Bundan tashqari ko'rsatilgan ruyxat bosh bolsa ValueError istisno holati yuz beradi.
#Count(item)
#Ruyxatdagi elementlar sonini chiqarib beradi
#sort([key]) ruyxat elementlarini o'sish bo'yicha tartiblaydi
#key parametri bo'yicha tartiblash funksiyasini holatini berishimiz mumkin.
#ruyxat elementlarini teskari tartibda joylashtirish uchun qo'llaniladi
#len(list1)
#ruyxat uzunligini (elementlar sonini qiymat sifatida qaytaradi)
#sorted(list1,[Key])
#Tartiblanga ruyxatni qiymat sifatida qaytaradi
#min(list1)
#max(list1)

t=["tmi","iat"]

#list1 id, ism, familiya, viloyat, faculty,kurs
#list2 .....list 3
# 10 ta talaba haqida ma'lumot yaratish




