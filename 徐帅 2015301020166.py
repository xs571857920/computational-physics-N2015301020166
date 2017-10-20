#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:56:42 2017

@author: xu shuai
"""

import math
import numpy as np
import matplotlib.pyplot as plt
H=float(1)
V0=float(input("please input the initial speed:"))
An=float(input("please input the initial angle:"))
An=(An/180)*np.pi
Vx=(V0)*math.cos(An)
Vy=(V0)*math.sin(An)
w=float(input("please input the angular rotation speed:"))
w=w/60*np.pi*2
Vz=0
x=0
y=H
z=0
X_list=[x]
Y_list=[y]
Z_list=[z]
dt=float(0.01)
x_end=200
n=0
while y>=0 and x<x_end :
    V=np.sqrt(Vx**2+Vy**2+Vz**2)
    x=x+Vx*dt
    y=y+Vy*dt
    z=z+Vz*dt
    Vz=Vz+0.00041*Vx*w*dt
    Vx=Vx-(0.0039+0.0058/(1+np.exp((V-35)/5)))*V*Vx*dt
    Vy=Vy-9.8*dt
    X_list.append(x)
    Y_list.append(y)
    Z_list.append(z)
    n=n+1
if y<0:
    r=Y_list[n-1]/(Y_list[n-1]-Y_list[n])
    X_list[n]=X_list[n-1]+(X_list[n]-X_list[n-1])*r
    Y_list[n]=0
    Z_list[n]=Z_list[n-1]+(Z_list[n]-Z_list[n-1])*r
if x>=x_end:
    r=(x_end-X_list[n-1])/(X_list[n-1]-X_list[n])
    Y_list[n]=Y_list[n-1]-(Y_list[n-1]-Y_list[n])*r
    Z_list[n]=Z_list[n-1]+(Z_list[n]-Z_list[n-1])*r
    X_list[n]=x_end  
plt.plot(X_list,Y_list,label="vertical deflection")
plt.xlabel("X/m")
plt.ylabel("Y or Z/m")
plt.title("Curve Ball Trajectory")
plt.plot(X_list,Z_list,label="horizontal deflection")
plt.legend(loc="upper right")
plt.show()
print(Z_list[n])
