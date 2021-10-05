# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:15:33 2019

@author: Asus
"""

#METODO RECTA SECANTE

import math
import matplotlib.pyplot as plt


def g(x):
    return x**3+3*x-6 #Esta es la que hay que cambiar



t = float(input("Ingrese la tolerancia: ")) #tolerancia
sem1 = float(input("Ingrese la semilla 1: ")) #semilla(cercana a la solución)
sem2 = float(input("Ingrese la semilla 2: ")) #semilla(cercana a la solución)

x = []
x.append(sem1)
x.append(sem2)

#m = (g(x[-1])-g(x[-2]))/(x[-1]-x[-2])

if (g(sem1)*g(sem2) > 0):
    print ("ingrese un intervalo")
else:
        
    while abs(x[-1]-x[-2])>t:
        m = (g(x[-1])-g(x[-2]))/(x[-1]-x[-2])
        x.append(x[-1]-g(x[-1])/m) #evaluacion de la ultima posicion del vector
            
           
#print(m)
print(x)                
print("La solución es x= " + str(x[-1]))

