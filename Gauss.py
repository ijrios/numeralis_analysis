# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:50:08 2019

@author: jario
"""

import math
import matplotlib.pyplot as plt

def g(x,y,z):
    return ((3*y)-(2*z)+ 6)

def h(x,y,z):
    return ((-6*x +4*z)/3)

def i(x,y,z):
    return ((x + 6*y - 9)/8)

semillax = float(input("Ingrese la semilla de x: "))
semillay = float(input("Ingrese la semilla de y: "))
semillaz = float(input("Ingrese la semilla de z: "))
tol= float(input("Ingrese la tolerancia: ")) 
#m = abs((g(b)-g(a))/(b-a))

xn = []
yn = [] 
zn = []
xn.append(semillax) 
yn.append(semillay) 
zn.append(semillaz) 
xn.append(g(xn[-1],yn[-1],zn[-1]))
yn.append(h(xn[-1],yn[-1],zn[-1]))
zn.append(i(xn[-1],yn[-1],zn[-1]))

while (abs(xn[-1]-xn[-2]) > tol or abs(yn[-1]-yn[-2]) >tol or abs(zn[-1]-zn[-2]) > tol):
    x = xn[-1]
    y = yn[-1]
    z = zn[-1]
    xn.append(g(x,y,z)) 
    x = xn[-1]
    yn.append(h(x,y,z)) 
    y = yn[-1]
    zn.append(i(x,y,z)) 
    z = zn[-1]

   
print("La solución es x= " + str(xn))
print("La solución es y= " + str(yn))
print("La solución es z= " + str(zn))
#plt.plot(x)
#plt.grid