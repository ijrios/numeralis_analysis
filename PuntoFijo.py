# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 01:18:13 2019

@author: jario
"""
#JOSE RIOS - ANALISIS NUMERICO
#ITERACIÓN PUNTO FIJO

import math
import matplotlib.pyplot as plt

def g(x):
    return -(2*x**2-4*x+3)**(1/3) 


a = float(input("Ingrese la variable inicial: "))
b = float(input("Ingrese la variable final: "))
semilla = float(input("Ingrese la semilla: "))
tol= float(input("Ingrese la tolerancia: ")) 
m = abs((g(b)-g(a))/(b-a))


x = [] 
x.append(semilla) 
x.append(g(x[-1]))

if m > 1:
    print("La pendiente es:"+str(m))
    print("No es posible encontrar la solucion con este metodo, intente otro valor")
  
else:
    print("La pendiente es:"+str(m))
    while abs(x[-1]-x[-2])>tol:
        x.append(g(x[-1])) 
        
             
print(x)                
print("La solución es X = " + str(x[-1]))
plt.plot(x)
plt.grid