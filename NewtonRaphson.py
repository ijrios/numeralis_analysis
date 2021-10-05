# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:33:48 2019

@author: Asus
"""

#METODO NEWTON RAPHSON

import math
import matplotlib.pyplot as plt


def g(x):
    return x**3+3*x-6 #Esta es la que hay que cambiar

def G(x):
    return 3*x**2+3 #Derivada

def NR(x):
    return x-g(x)/G(x) #Formula Newton Raphson

a = float(input("Ingrese la variable inicial: "))

b = float(input("Ingrese la variable final: "))

t = float(input("Ingrese la tolerancia: ")) #tolerancia
sem = float(input("Ingrese la semilla: ")) #semilla(cercana a la solución)

#m = abs((g(b)-g(a))/(b-a))

x = []
x.append(sem)
x.append(NR(x[-1]))

#xk=t-g(s)/G(s)
if (g(a)*g(b) > 0):
    print ("ingrese un intervalo")
else: 
    while abs(x[-1]-x[-2])>t:
        x.append(NR(x[-1])) #evaluacion de la ultima posicion del vector
        
             
print(x)                
print("La solución es x= " + str(x[-1]))