# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:36:07 2019

@author: jario
"""

"Ecuaciones Runge-kutta"

import numpy as np
import math
import matplotlib.pyplot as plt

a=0.0
b=2.0

def f(x,y):
    return math.exp(-x)-y

xo=0.0
yo=1.0
n=18#numero de puntos
h=(b-a)/(n-1.0)

#VARIACIONES DEL METODO
a1=0.5
a2=0.5
alfa=1.0
# Euler modificado: =0.5, a1=0 y a2=1
#Heun: =1, a1=0,5 y a2=0,5
#Ralston: =0.75, a1=1/3 y a2=2/3


i=a
m=n-1
X1=[]
Y1=[]
X1.append(xo)
Y1.append(yo)


while i<= n:
    M1=f(X1[-1],Y1[-1])
    yp=Y1[-1]+alfa*h*M1
    xp=X1[-1]+alfa*h
    M2=f(xp,yp)
    M=a1*M1+a2*M2
    Y1.append(Y1[-1]+h*M)
    X1.append (X1[-1]+h)
    YA.append((3/4)*((X1[-1])**2))
    i=i+1


    
plt.plot(X1,Y1,"G", color = "green")
plt.title("Metodo Runge Kutta Segundo Orden (Ralston)")
print("La respuesta del vector X: "+"\n" + str(X1))
print("La respuesta del vector Y: " +"\n" + str(Y1))
plt.grid()
plt.show()
