# -*- coding: utf-8 -*-
"""
Created on Fri May 16 11:20:26 2019

@author: jario
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4*x+2*math.sin(2*x)

x=[]
y=[]
Seg=3 #Numero de segmentos
RangoInf=-1
RangoSup=2
h1=(RangoSup-RangoInf)/Seg
for i in range(Seg+1):
    x.append(RangoInf+h1*i)
    y.append(f(x[-1]))

A=[]
B=[]
n=len(y)
cte=2 #Segunda derivada al inicio
cte2=1 #Segunda derivada al final
df2=lambda p:(f(p+h)+f(p-h)-2*f(p))/(h**2)
h=0.0000001
cte=df2(x[0])
cte2=df2(x[-1])

for i in range (4*n-4):
    A.append([])
    for j in range (4*n-4):
        A[i].append(0)

for i in range(4*n-4):
    B.append(0)

for i in range (n-1):
    B[i]=y[i]
    A[i][4*i]=x[i]**3
    A[i][4*i+1]=x[i]**2
    A[i][4*i+2]=x[i]
    A[i][4*i+3]=1
    
for i in range(n-1):
    B[i+n-1]=y[i+1]
    A[i+n-1][4*i]=x[i+1]**3
    A[i+n-1][4*i+1]=x[i+1]**2
    A[i+n-1][4*i+2]=x[i+1]
    A[i+n-1][4*i+3]=1
    
for i in range(n-2):
    A[i+2*n-2][4*i]=3*x[i+1]**2
    A[i+2*n-2][4*i+1]=2*x[i+1]
    A[i+2*n-2][4*i+2]=1
    A[i+2*n-2][4*i+4]=-3*x[i+1]**2
    A[i+2*n-2][4*i+5]=-2*x[i+1]
    A[i+2*n-2][4*i+6]=-1
    
for i in range(n-2):
    A[i+3*n-4][4*i]=6*x[i+1]
    A[i+3*n-4][4*i+1]=2
    A[i+3*n-4][4*i+4]=-6*x[i+1]
    A[i+3*n-4][4*i+5]=-2

A[4*n-6][0]=6*x[0]
A[4*n-6][1]=2
B[-2]=cte
A[4*n-5][-4]=6*x[-1]
A[4*n-5][-3]=2
B[-1]=cte2
#
Am=np.matrix(A)
Bm=np.matrix(B)
Bm=np.transpose(Bm)
InvAm=np.linalg.inv(Am)
Sol=InvAm*Bm

a=[]
b=[]
c=[]
d=[]
for i in range (n-1):
    a.append(Sol[i*4])
    b.append(Sol[i*4+1])
    c.append(Sol[i*4+2])
    d.append(Sol[i*4+3])
    
#GRAFICACION
puntos=20
yk=[]
xk=[]
for i in range (n-1):
    h=((x[i+1]-x[i])/(puntos-1))
    for j in range (puntos):
        xk.append(x[i]+h*j)
        yk.append(float(a[i])*xk[-1]**3+float(b[i])*xk[-1]**2+float(c[i])*xk[-1]+float(d[i]))
        
print('Vector X:' + str(x))
print('Vector Y:' + str(y))
        
plt.plot(x,y,'o')        
plt.plot(xk,yk)
plt.title('Interpolacion cubica por segmentos 3 INTERVALOS')
plt.grid()
plt.show()
