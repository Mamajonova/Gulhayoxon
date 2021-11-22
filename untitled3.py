# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:38:07 2021

@author: Premium
"""

def dekotartiv_funksiya(func):
    def ichki(qiymatlar):
        return(func(val[0],val[1]) for val in qiymatlar)
    return ichki
@dekotartiv_funksiya
def qoshish(a,b):
    print(a+b)
print(qoshish([(14,24),(23,13),(12,22)]))