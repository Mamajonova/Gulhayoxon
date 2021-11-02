# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:25:56 2021

@author: Premium
"""

dasturlash_tillari=["Ada","Algol","ARL","DELPHI","VASIS","C","C++","Kobol",
                    "Fort","FORTRAN","Java"]
print(dasturlash_tillari[-1])
print(dasturlash_tillari.index("C"))
print(dasturlash_tillari.index("Fort"))
dasturlash_tillari[6]="HTML"# 6-indexli so'z o'rniga boshqasini yukladim
print(dasturlash_tillari)
dasturlash_tillari.append("C#")#ro'yxat oxiriga qo'shish
print(dasturlash_tillari)
dasturlash_tillari.insert(1,"JavaScript")# istalgan indexni o'rniga qo'shish
print(dasturlash_tillari)
dasturlash_tillari.remove("DELPHI")# o'chirish nomiga ko'ra
print(dasturlash_tillari)
m=dasturlash_tillari.pop(2)
print(m)