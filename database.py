# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:00:46 2021

@author: Premium
"""

#import sqlite3
#boglanish=sqlite3.connect("mydatabase.db")



#cursor=boglanish.cursor()
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS odamlar(
#ism TEXT,
#familiyasi TEXT,
#yoshi INTEGER )

 #             """)
#print(boglanish)

#import sqlite3
#boglanish=sqlite3.connect("mydatabase1.db")
#cursor=boglanish.cursor()
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS odam(
#   ism TEXT,
#   familiyasi TEXT,
#   yoshi INTEGER,
#   manzili TEXT
#   )
#""")

#cursor.execute("""
#INSERT INTO odam VALUES
#("Abbos","Turobov",24,"Toshkent"),
#("Gulhayo","Mamajonova",20,"Farg'ona")""")
#cursor.execute("SELECT * FROM odam")
#print(cursor.fetchall())

import sqlite3
b=sqlite3.connect("talaba.db")




#import logging
#logging.basicConfig(level=logging.INFO)
#logging.info("Dastur haqida ma'lumot")
#ogging.error("Xatolik haqida ma'lumot")

#import time
#import threading
#def birinchi():
#   print("1-ishga tushdi")
#   time.sleep(2)
#   print("1-ishni yaknladi")
    
#def ikkinchi():
#   print("2-ishga tushdi")
#   print("2-ishni yaknladi")

#birinchi()
#ikkinchi()
#t1=threading.Thread(target=birinchi,daemon=True)
#t2=threading.Thread(target=ikkinchi)
#t1.start()
#t2.start()
























