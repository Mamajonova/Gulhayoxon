# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:12:21 2021

@author: Premium
"""

amal=input("Amalni kiriting: ")
if amal=="*" or amal=="ko'paytirish":
    a=float(input("1-son= "))
    b=float(input("2-son= "))
    def kupaytma (a,b):
        print("kupaytmasi= ",a*b)
    kupaytma(a, b)
    
elif amal=="/" or amal=="bo'lish":
    a=float(input("1-son= "))
    b=float(input("2-son= "))
    def bulinma (a,b):
        print("bo'linmasi= ",a/b)
    bulinma(a, b)
    
elif amal=="+" or amal=="qo'shish":
    a=float(input("1-son= "))
    b=float(input("2-son= "))
    def yigindi (a,b):
        print("yig'indisi= ",a+b)
    yigindi(a, b)
    
elif amal=="-" or amal=="ayirish":
    a=float(input("1-son= "))
    b=float(input("2-son= "))
    def ayirma (a,b):
        print("kupaytmasi= ",a-b)
    ayirma(a, b)
    
else:
    print("Xatolik boshqa amal kiriting: Masalan,+  -  *  / ")
    
    
    