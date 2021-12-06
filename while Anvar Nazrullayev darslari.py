# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 10:31:01 2021

@author: Premium
"""
'''
a=1
while a<5:
    print(a,end=' ')
    a=a+1
print("Dastur tugadi")


savol='son kiriting \n'
savol+=" dasturni to'xtatish uchun 'exit' deb yozing: "
qiymat=''
while qiymat!='exit':
    qiymat=input(savol)
    if qiymat!='exit':
        print(float(qiymat)**2)
print("Dastur tugadi")
'''
'''
savol='son kiriting \n'
savol+=" dasturni to'xtatish uchun 'exit' deb yozing: "
qiymat=''
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat=='exit':
        ishora=False
    else:
        print(float(qiymat)**2)
print("Dastur tugadi")

savol='son kiriting \n'
savol+=" dasturni to'xtatish uchun 'exit' deb yozing: "
while True:
    qiymat=input(savol)
    if qiymat=='exit':
        break
    else:
        print(float(qiymat)**2)
print("Dastur tugadi")
'''
'''
sonlar=list(range(1,11))
for son in sonlar:
    if son==5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
   
    
#continue bitta tashlab chiqarib beradi
sonlar=list(range(1,11))
for son in sonlar:
    if son==5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")


#juft sonlarni chiqaradigan kod
son=0
while son<10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)
        '''
'''        
kitob="yaxshi ko'rgan kitoblariz nomini kiriting: "
kitob+="To'xtatish uchun stop deb yozing: "
qiymat=''
ishora=True
while ishora:
    qiymat=input(kitob)
    if qiymat=="stop":
        ishora=False
print("Dastur tugadi")
'''
"""
yosh="yoshingizni kiriting: "
yosh+="To'xtatish uchun exit yoki quit  deb yozing: "
qiymat=''
ishora=True
while ishora:
    qiymat=input(yosh)
    if qiymat=="exit" or qiymat=="quit":
        ishora=False
    elif int(qiymat)<=7:
        print("chipta narxi 2000 so'm")
    elif int(qiymat)<=18 and int(qiymat)>7:
        print("chipta narxi 3000 so'm")
    elif int(qiymat)>18 and int(qiymat)<=65:
        print("sizga chipta narxi 10000 so'm")
    else:
        print("sizga chipta narxi bepul")
print("Dastur tugadi")
"""

savol="kiritilgan sonni ildizini qaytaruvchi dastur: "
savol+="\nmusbat son kiriting: "
savol+="\ndasturni to'xtatish uchun ''exit' deb yozing: "
while True:
    qiymat=input(savol)
    if qiymat=='exit':
        break
    elif int(qiymat)<0:
        print("musbat son kiriting")
        continue
    else:
        ildiz=float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
