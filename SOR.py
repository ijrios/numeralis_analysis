# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:09:35 2019

@author: jario
"""
#JOSE RIOS - ANALISIS NUMERICO
#ITERACIÓN Regla SOR

import math
import matplotlib.pyplot as plt

pi = math.pi
e = math.e
sen = math.sin
cos = math.cos

def g(x):
    return 10*(e**(-x))*(sen(pi*x)) 
def h(x):
    return -10*e**(-x)*(sen(pi*x)-pi(cos(x*pi))) 

a = float(input("Ingrese la variable inicial: "))
b = float(input("Ingrese la variable final: "))
semilla = float(input("Ingrese la semilla: "))
tol= float(input("Ingrese la tolerancia: ")) 
m = ((g(b)-g(a))/(b-a))


x = [] 

if m==1:
    print("No es posible encontrara la solucion M diferente de 1")
else:
    def G(x):
        return ((m*x-g(x))/(m-1))
    x.append(semilla) 
    x.append(G(x[-1]))

    print("La pendiente es:"+str(m))
    while abs(x[-1]-x[-2])>tol:
            x.append(G(x[-1])) 
        
             
print(m)                
print("La solución es X = " + str(x[-1]))
plt.plot(x)
plt.grid
