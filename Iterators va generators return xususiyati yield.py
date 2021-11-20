# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:11:06 2021

@author: Premium
"""
"""
from typing import Iterator

sonlar=[17,14,16,63]
iterator=iter(sonlar)
print(iterator.__next__())
print(next(iterator))
print(next(iterator))
print(next(iterator))



mevalar=["olma","anor","nok","shaftoli","behi"]
iterator=iter(mevalar)
print(iterator.__next__())
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
"""
a=int(input("a="))
def oddiy():
    print(a,"^2")
    yield a**2
    
    print(a,"^3")
    yield a**3
    
    print(a,"^4")
    yield a**4
    
    print(a,"^5")
    yield a**5
    
    print(a,"^6")
    yield a**6
    
    print(a,"^7")
    yield a**7
    
    print(a,"^8")
    yield a**8
    
    print(a,"^9")
    yield a**9
    
    print(a,"^10")
    yield a**10
    
values=oddiy()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
"""
"""

a=int(input("a="))
def oddiy():
    yield a**2
    yield (a+1)**2
    yield (a+2)**2
    yield (a+3)**2
    yield (a+4)**2
    yield (a+5)**2
    yield (a+6)**2
    yield (a+7)**2
    yield (a+8)**2
    yield (a+9)**2
    
values=oddiy()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
"""

    
    

