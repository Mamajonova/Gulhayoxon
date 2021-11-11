# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:56:15 2021

@author: Premium
"""
class Xona:
    def __init__ (self,mehmonxona,oshxona,yotoqxona,kirxona):
        self.mehmonxona=mehmonxona
        self.oshxona=oshxona
        self.yotoqxona=yotoqxona
        self.kirxona=kirxona
    def __str__(self):
        return "Xonalar ketma -ketligi {} {} {} {}".format(self.mehmonxona,self.oshxona,self.yotoqxona,self.kirxona)
class Tuzilishi(Xona):
    def __init__(self,mehmonxona,oshxona,yotoqxona,kirxona,rangi,ulchovi):
        super().__init__(mehmonxona,oshxona,yotoqxona,kirxona)
        self.rangi=rangi
        self.ulchovi=ulchovi
    def __str__(self):
        t=super(Tuzilishi,self).__str__()
        t+=",xona rangi:{},ulchovi:{}".format(self.rangi,self.ulchovi)
        return t
xona1=Tuzilishi("mehmonxona", "oshxona", "yotoqxona"," kirxona", "pushti", "430X400")
print(xona1)























