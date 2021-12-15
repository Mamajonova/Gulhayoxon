# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:24:10 2021

@author: Premium
"""
try:
    a1=float(input("a1="))
    a2=float(input("a2="))
    a3=float(input("a3="))
    a4=float(input("a4="))
    if a1+a2==a3 or a1+a2==a4 or a2+a3==a1 or a2+a3==a4 or a1+a3==a4:
        print(True,"fibonachi soni bor")
    else:
        print(False,"Fibonachi son yoq")     
except TypeError:
    print("TypeError xatolik bor")
except NameError:
    print("NameError xatolik bor")
except ValueError:
    print("ValueError xatolik bor")
    
    
