# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:33:18 2021

@author: Premium
"""
'''
s1=[1,2,3,"Tmi"]
s2=list(s1)
print(type(s1))
print(type(s2))

print(3*s1)
print(range(12))
for i in s1:
    print(i)
s1.insert(2,"7")
print(s1)
s1.count(1)
print(s1.count(12))#s1 ro'yxatda 12 ni necha marta ishtirok etgani
'''


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matrix)
n=int(input("n-satr: "))
k=int(input("k-ustun: "))
if n==1 and k==1:
    print([[5,6],[8,9]])
elif n==2 and k==1:
    print([[2,3],[8,9]])
elif n==3 and k==1:
    print([[2,3],[5,6]])
elif n==1 and k==2:
    print([[4,6],[7,9]])
elif n==2 and k==2:
    print([[1,3],[7,9]])
elif n==3 and k==2:
    print([[1,3],[4,6]])
elif n==1 and k==3:
    print([[4,5],[7,8]])
elif n==2 and k==3:
    print([[1,2],[7,8]])
elif n==3 and k==3:
    print([[1,2],[4,5]])
else:
    print("boshqa son kiriting")
    
m=max(matrix)
print(max(m))
    