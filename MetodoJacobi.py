# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:42:33 2019

@author: jario
"""
#METODO JACOBI
import math
import matplotlib.pyplot as plt

def g(x,y,z):
    return ((10+y)/4)

def h(x,y,z):
    return ((-3*x +8)/2)

def i(x,y,z):
    return 0

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
xn.append(g(semillax, semillay, semillaz))
yn.append(h(semillax, semillay, semillaz))
zn.append(i(semillax, semillay, semillaz))

while (abs(xn[-1]-xn[-2]) > tol or abs(yn[-1]-yn[-2]) >tol or abs(zn[-1]-zn[-2]) > tol):
    x = xn[-1]
    y = yn[-1]
    z = zn[-1]
    xn.append(g(x,y,z)) 
    yn.append(h(x,y,z)) 
    zn.append(i(x,y,z)) 

   
print("La solución es x= " + str(xn))
print("La solución es y= " + str(yn))
print("La solución es z= " + str(zn))
#plt.plot(x)
#plt.grid