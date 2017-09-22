# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:57:29 2017

@author: nature
"""
import time
a1=["#"," "," "," ","#"," ","#","#","#"]
a2=[" ","#"," ","#"," "," ","#"," "," "]
a3=[" "," ","#"," "," "," ","#","#","#"]
a4=[" ","#"," ","#"," "," "," "," ","#"]
a5=["#"," "," "," ","#"," ","#","#","#"]
 
t=0
while t<10:
    
    for i1 in a1:
        print(i1,end='')
    print("\n")
    for i2 in a2:
        print(i2,end='')
    print("\n")
    for i3 in a3:
        print(i3,end='')
    print("\n")
    for i4 in a4:
        print(i4,end='')
    print("\n")
    for i5 in a5:
        print(i5,end='')
    print("\n")
    for j in (a1,a2,a3,a4,a5):
        j.insert(0," ")
    time.sleep(1)
    t+=1
    print(" ")
    