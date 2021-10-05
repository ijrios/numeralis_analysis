
"""
Created on Fri Apr 21 11:52:47 2019

@author: jario
"""
#INTERPOLACIÓN CÚBICA POR SEGMENTOS DIRECTA

import numpy as np
import matplotlib.pyplot as plt
import math

#HAY QUE MODIFICAR ESTA CON LOS VALORES RESULTANTES DE B Y LOS VALORES DE X
def p(t):
    return 4*t+2*math.sin(2*t)

#crear matriz n+1*n
n=5
a=[] 
b=[]

#CREA UNA MATRIZ DE 0 
for i in range (n):
    a.append([])
    for j in range (n+1):
        a[i].append(0)#EL VALOR QUE HAYA AQUI ES CON EL QUE ES LLENADO LA MATRIZ

#Vectores
x=[0,1,2,3,4]
y=[1.0, 1.103638323514327, 1.5413411329464508, 2.24893534183932, 3.10989383333]

#ASIGNA LOS VALORES DE LOS VECTORES X Y Y EN LAS POSICIONES CORRESPONDIENTES DE LA MATRIZ 
for i in range(n):
    a[i][0]=x[i]
    a[i][1]=y[i]
    
#CICLO ANIDADO PARA LLENAR LA MATRIZ
for j in range(2,n+1):#LLENA TODA MATRIZ CON LOS VALORES CALCULADOS
    for i in range(n-j+1):      
        a[i][j]= (a[i+1][j-1]-a[i][j-1])/(a[i+j-1][0]-a[i][0])
        
for k in range(n):
    b.append(a[0][k+1])#OBTIENE LOS PRIMEROS VALORES PARA LOS COEFICIENTES DE B
    
A=np.matrix(a)
#print("\n")
#print ("La matriz es igual a: ")
#print(A)
#print("\n")
#print ("Los coeficientes de b son: ")
#print(b)

#PROCEDIMIENTO DE GRAFICA
print("Gráfica Interpolación Cúbica por Segmentos Directa")
x1=0 #PRIMER VALOR DEL VECTOR X
xn=4 #ULTIMO VALOR DEL VECTOR X
n=800 #NUMERO DE PUNTOS PARA LA GRÁFICA
h=(xn-x1)/(n-1.0)
i=x1
X=[]
Y=[]
k=0
while i<=xn:
    X.append (x1+h*k)
    Y.append(p(X[k]))
    k=k+1
    i=i+h

plt.plot(x, y, "^")
plt.plot(X,Y,"magenta")
plt.grid()
plt.show()     
