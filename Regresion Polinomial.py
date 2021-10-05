
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
sumxk=0
sumxk2=0
sumyk=0
sumykxk=0

for i in range(n):
    sumxk=xk[i]+sumxk
    sumxk2=xk[i]**2+sumxk2
    sumyk=yk[i]+sumyk
    sumykxk=yk[i]*xk[i]+sumykxk
A=np.matrix([[n,sumxk],[sumxk,sumxk2]])
b=np.matrix([[sumyk],[sumykxk]])
InvA=np.linalg.inv(A)
x=InvA*b
ET2=0
y=lambda t: float(x[0])+float(x[1])*t
print(x)
for j in range(n):
    ET2=(yk[j]-y(xk[j]))**2+ET2
ET=math.sqrt(ET2)
Erms=ET/n
rango = xk[-1]-xk[0]
numeroPuntos = 10
h = rango/(numeroPuntos-1)
i=xk[0] 
xg = []
yg = []
while (i<=xk[-1]):
    xg.append(i)
    yg.append(y(i))
    i+=h
plt.plot(xk,yk,"o")
plt.plot(xg,yg)
plt.grid()
plt.show()
print(ET)
print(Erms)
