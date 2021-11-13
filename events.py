# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:18:01 2021

@author: Premium
"""

import threading as thr
event=thr.Event()
def jarayon():
    print("Bottleni o'rnatish")
    event.wait()
    print("Bottleni o'rnatish boshlandi")
t1=thr.Thread(target=jarayon)
t1.start()
sorov=input("Bottleni o'rnatish boshlansinmi: (h)")
if sorov=="h":
    event.set()
    
"""    
Frameworks
1.AIOHTTP
2.Bottle
3.CherryPy
4.CubicWeb
5.Dash
6.Django
7.Falcon
8.Flask
9.Giotto
10.Growler
11.Hug
12.MorePath
13.Pycnic
14.Pylons
15.Pyramid
16.Sanic
17.Tarnado
18.TurboGears
19.Web2Py
"""