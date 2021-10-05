
"""
Created on Fri May 10 10:37:51 2019

@author: jario
"""


"Ecuaciones diferenciales: Euler"

import numpy as np
import math
import matplotlib.pyplot as plt

a=2.0
b=8.0

def f(x,y):
    return math.exp(-x)-y

xo=0.0
yo=1.0
yanal=3.0
n=21#numero de puntos
n2=100
h=(b-a)/(n-1.0)
h2=(b-a)/(n2-1.0)
i=a
j=a
m=n-1
X1=[]
Y1=[]
YA=[]
X2=[]
YA2=[]
error = []
X1.append(xo)
Y1.append(yo)
YA.append(yanal)
X2.append(xo)
YA2.append(yanal)


while i<= n:
    Y1.append(Y1[-1]+h*f(X1[-1],Y1[-1]))
    X1.append (X1[-1]+h)
    YA.append((3/4)*((X1[-1])**2))
    i=i+1

while j<= n2:
    X2.append(X2[-1]+h2)
    YA2.append((3/4)*((X2[-1])**2))
    j=j+1
    
for i in range(n):
    error.append(abs(Y1[i]-YA[i]))
    
print("La respuesta del vector X: "+"\n" + str(X1))
print("La respuesta del vector Y: " +"\n" + str(Y1))  
print("La respuesta del vector Y Analitica: " +"\n" + str(YA))    
print("el error es: " +"\n" + str(error))
plt.plot(X1,Y1,"o", color= "blue")
plt.plot(X2,YA2,"g", color= "cyan")
plt.title("SHE DONE ALREADY DONE HAD HERSE")
plt.grid()
plt.show()
