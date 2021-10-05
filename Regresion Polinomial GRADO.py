# -*- coding: utf-8 -*-
"""
Created on Tue Mar 6 07:23:34 2019

@author: jario
"""
import numpy as np
import math
import matplotlib.pyplot as plt

xk=[-2,-1,0,1,2]
yk=[2,0,2,3,-1]
n=len(xk)
#El grado debe ser m<n-1
m=int(input('Ingrese el mayor grado deseado: '))
A=[]
B=[]
for i in range(m+1):
    A.append([])
    for j in range(m+1):
        suma=0
        for k in range(n):
            suma=suma+xk[k]**(j+i)
        A[i].append(suma)
for i in range(m+1):
    B.append([])
    for j in range(1):
        suma=0
        for k in range(n):
            suma=suma+yk[k]*xk[k]**(j+i)
        B[i].append(suma)
A=np.matrix(A)
InvA=np.linalg.inv(A)
B=np.matrix(B)
x=InvA*B
#Para poder hacer la función dinámica
def y(X,t):
    valor=0
    for i in range(len(X)):
        valor=valor + X[i,0]*t**(i)
    return valor
ET2=0
for j in range(n):
    ET2=(yk[j]-float(y(x,xk[j])))**2+ET2
ET=math.sqrt(ET2)
Erms=ET/n
rango = xk[-1]-xk[0]
numeroPuntos = 200
h = rango/(numeroPuntos-1)
i=xk[0] 
xg = []
yg = []
while (i<=xk[-1]):
    xg.append(i)
    yg.append(y(x,i))
    i+=h
plt.plot(xk,yk,"o")
plt.plot(xg,yg)
plt.grid()
plt.show()

print(x)
