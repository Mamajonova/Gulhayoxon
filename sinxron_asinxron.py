# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:59:40 2021

@author: Premium
"""

#sinxron va asinxron
#tartib bilan xizmat ko'rsatish sinxron php
#birdaniga hammaga xizmat ko'rsatsa asinxron nojec

"""
for x in range(10):
    print("Assalomu")        #sinxron
for x in range(10):
    print("alaykum")
   """
import threading
   
def func():
    for x in range(30):
        print("Assalomu")
        
        
def func2():
    for x in range(30):
        print("alaykum")
t1=threading.Thread(target=func)
t2=threading.Thread(target=func2)
t1.start()
t2.start()