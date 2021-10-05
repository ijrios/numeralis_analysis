"""
Created on Mon Apr 09 20:04:40 2018

@author: User
"""

"interpolacion cuadratica por segmentos con diferencias divididas"
import numpy as np
import matplotlib.pyplot as plt

a=[[0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0],[0.0,0.0,1.0,0.0,0.0,0.0,4.0,2.0,1.0],[1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,4.0,2.0,1.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,9.0,3.0,1.0],[2.0,1.0,0.0,-2.0,-1.0,0.0,0.0,0.0,0.0],[0.0,0.0,  0.0,4.0,1.0,0.0,-4.0,-1.0,0.0],[0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
b=[[1.0],[-2.0],[3.0],[-2.0],[3.0],[0.0],[0.0],[0.0],[-2.0]]
A=np.matrix(a)
B=np.matrix(b)
invA=np.linalg.inv(A)
s=invA*B
#debe dar: -1 -2 1 9 -22 11 -17 82 -93

x=[0.0, 1.0, 2.0, 3.0]
y=[1.0, -2.0, 3.0, 0.0]
ak=[]
bk=[]
ck=[]
u1=-2.0
i=1
n=4
u=[]

u.append(u1)
for i in range (1,n):
   
    u.append((-u[-1])+2.0*((y[i]-y[i-1])/(x[i]-x[i-1])))
    ak.append(0.5*((u[i]-u[i-1])/(x[i]-x[i-1])))
    bk.append(u[i-1]-2.0*ak[-1]*x[i-1])
    ck.append(y[i-1]-x[i-1]*u[i-1]+((x[i-1])**2)*ak[i-1])


f=lambda t:-1.0*t**2-2.0*t+1.0
g=lambda t:9.0*t**2-22.0*t+11.0
l=lambda t:-17.0*t**2+82.0*t-93.0
a=0.0
b=1.0
d=2.0
q=3.0
n=100.0
h1=(b-a)/(n-1.0)
h2=(d-b)/(n-1.0)
h3=(q-d)/(n-1.0)
i=a

X1=[]
Y1=[]
X2=[]
Y2=[]
X3=[]
Y3=[]
k=0
while i<=b:
    X1.append (a+h1*k)
    Y1.append(f(X1[k]))
    k=k+1
    i=i+h1


i=1
k=0
while i<=d:
    X2.append (b+h2*k)
    Y2.append(g(X2[k]))
    k=k+1
    i=i+h2
    
i=2
k=0
while i<=q:
    X3.append (d+h2*k)
    Y3.append(l(X3[k]))
    k=k+1
    i=i+h2
 

plt.plot(x,y,"--")
#plt.plot(X2,Y2,"g")
plt.plot(X1,Y1,X2,Y2,X3,Y3,"g")
plt.grid()
plt.show()

    

