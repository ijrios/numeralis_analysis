
"""
Created on Fri Apr 21 10:46:12 2019

@author: jario
"""
#METODO DE DIFERENCIAS DIVIDAS

import numpy as np
import matplotlib.pyplot as plt

#HAY QUE MODIFICAR ESTA CON LOS VALORES RESULTANTES DE B Y LOS VALORES DE X
def p(t):
    return 1 +(-1)*(t+2) +1*(t+2)*(t+1) +(-1/3)*(t+2)*(t+1)*(t+0) +(-1/12)*(t+2)*(t+1)*(t+0)*(t-1)

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
print("\n")
print ("La matriz es igual a: ")
print(A)
print("\n")
print ("Los coeficientes de b son: ")
print(b)

#PROCEDIMIENTO DE GRAFICA
x1=0 #PRIMER VALOR DEL VECTOR X
xn=4 #ULTIMO VALOR DEL VECTOR X
n=600 #NUMERO DE PUNTOS PARA LA GRÁFICA
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

    
    


