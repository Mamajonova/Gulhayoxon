#while
# ism=input("Ismingiz nima? ")
# print("SALOM",ism)
# savol="SALOM",ism.title(),"Yoshingiz nechada? "
# print(savol)
# yosh=input(savol)
# print(yosh)
# height=input("Bo'yingiz necha metr? ")
# height=float(height)
# print(height)

# son=1
# while son<=5:
#     print(son,end=' ')
#     son=son+1
# print("Dastur tugadi")
#
#
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan son kiriting "
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat=' '
# while qiymat !='exit':
#     qiymat=input(savol)
#     if qiymat !='exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi")

#ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan son kiriting "
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing):"
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtatildi!")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan son kiriting "
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing):"
# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi! ")

#
# sonlar=list(range(1,11))
# for son in sonlar:
#     if son==5:
#         break
#     print(son,"sonning kvadrati",son**2," ga teng")


#continue
#
# sonlar=list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     print(son,"sonning kvadrati",son**2," ga teng")
#
#
# son=0
# while son<10:
#     son+=1
#     if son%2==0:
#         continue
#     else:
#         print(son)


# son=1
# while son<10:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


# kitob="kitoblarizni kiriting:"
# kitob+="  (barcha kitoblarni kiritib bo'lgach 'stop' deb yozing)n"
#
# while True:
#     kitob=input( kitob),
#     if kitob=='stop':
#         break
# print('Raxmat!')



yosh=int(input("Yoshingizni kiriting: "))
while yosh<7:

    if yosh=="exit"and "quite":
        break
    else:
        print("Sizga chipta narxi 2000 so'm", end=" ")
while yosh>=7 and yosh<18:

    if yosh=="exit"and "quite":
        break
    else:
        print("Sizga chopta narxi 3000 so'm", end=" ")
while yosh>=18 and yosh<65:

    if yosh=="exit" and"quite":
        break
    else:
        print("Sizga chipta narxi 10000 so'm", end=" ")
while yosh>=65:
    if yosh=="exit" and "quite":
        break
    else:
        print("Sizga chipta bepul", end=" ")
pr#int("Raxmat")



yosh=input("Yoshingizni kiriting")
while True:
    sss=input(yosh)
    if sss=='exit' or sss=='quite':
        break
    yoshi=int(sss)
    if yoshi<7:
        print("Sizga chipta narxi 2000 so'm")
    elif yoshi>=7 and yoshi<18:
        print("Sizga chipta narxi 3000 so'm")
    elif yoshi>=18 and yoshi<65:
        print("Sizga chipta narxi 2000 so'm")
    else:
        print("Sizga chipta bepul")


























