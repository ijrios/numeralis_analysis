"""
Created on Mon Apr  8 06:44:13 2019

@author: jario
"""
import numpy as np
import matplotlib.pyplot as plt

#funcion
def f(t):
    return (-1.0*t**2)-(2.0*t)+1.0     

x=[0.0, 1.0, 2.0, 3.0]
y=[1.0, -2.0, 3.0, 0.0]
xx =[]
yy =[]

n = int(input("Ingrese numero de datos a ingresar: "))
ak=[]
bk=[]
i=0
j=0
    
for i in range (n-1):
    ak.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    bk.append(y[i]-x[i]*ak[-1])

#GRAFICACION 
Ini=0.0#Inicial
Fin=1.0 #Final
n=400 #Numero de puntos
h=(Fin-Ini)/(n-1)
i=Ini
X1=[]
Y1=[]
k=0

while i<=Fin:
    X1.append (Ini+h*k)
    Y1.append(f(X1[k]))
    k=k+1
    i=i+h

plt.plot(x, y, "^", color='red')
plt.plot(x, y, "--", color='magenta')
plt.plot(X1,Y1,"r--") 
print('El resultado en A es: ' + str(ak))
print('El resultado en B es: ' + str(bk))
