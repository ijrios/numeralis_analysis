# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 04:24:17 2019

@author: jario
"""
import math
import matplotlib.pyplot as plt

def g(x):
    
    return 10*(-(math.exp(-x))*math.sin(math.pi*x)+math.pi*math.exp(-x)*math.cos(math.pi*x)) + x

def G(m,x):
    
    return ((m*x)-g(x))/(m-1) ##Se define la funcion a solucionar

def f(z):
    
    y = 10*math.exp(-x)*math.sin(math.pi*x)
    return y

vector = []

a = int(input("Ingrese la variable inicial: "))
b = int(input("Ingrese la variable final: "))
tol= float(input("Ingrese la tolerancia: ")) 

m = ((g(b)-g(a))/(b-a))
print('La pendiente es:', str(m))

if (m!=1): 
    
    terminado = False
    x = 0.5
    vector.append(x)
    
    while(not terminado):
        
        vector.append(G(m,vector[-1]))
        
    
        if (abs(vector[-1]-vector[-2]) < tol):
            
            print (str(vector))
            print('El maximo se encuentra en x=',vector[-1])
            terminado = True
    
    maximoy = f(vector[-1])
    print("El valor maximo es y=", maximoy)
    
    vecx = []
    vecy = []
    
    inicial = 0
    final = 5
    puntos = 300
    
    h = (final - inicial)/(puntos-1)
    
    for i in range (puntos):
        
        x = inicial + i*h
        vecx.append(x)
        y = f(x)
        vecy.append(y)
    
    plt.plot(vecx,vecy)
    plt.grid()
    
else:
    
    print('Seleccione otra g(x)')