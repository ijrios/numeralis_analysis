"""
Created on Mon Apr  1 11:10:15 2019

@author: jario
"""
import numpy as np
import matplotlib.pyplot as plt

#SE CREA MATRIZ (n+1*n)
n=5 #FILAS
a=[] 
b=[]   

#SE CREA UNA MATRIZ DE CEROS
for i in range (n):
    a.append([])
    for j in range (n+1):
        a[i].append(0)
        
#VALOR X Y Y EN VECTORES
x=[-2.,-1,0,1,2]
y=[1,0,1,2,-1]
        
for i in range(n): 
    a[i][0]=x[i]
    a[i][1]=y[i]

for j in range(2,n+1): #For anidado para llegar a la matriz
    for i in range(n-j+1):
      
        a[i][j]= (a[i+1][j-1]-a[i][j-1])/(a[i+j-1][0]-a[i][0])

for k in range(n):
    b.append(a[0][k+1])
    

A=np.matrix(a)
print("_____________________________________________________________________________")
print("A es igual a: ")
print("-----------------------------------------------------------------------------")
print(A)   
print("_____________________________________________________________________________")
print("B es igual a:")
print("-----------------------------------------------------------------------------")
print(b)
print("_____________________________________________________________________________")

#GRAFICACION
#FUNCION 
def g(t):
    return 1-1*(t+2) +1*(t+2)*(t+1) -(1/3)*(t+2)*(t+1)*(t-0)-(1/12)*(t+2)*(t+1)*(t-0)*(t-1)

Ini=-2 #Inicial
Fin=2 #Final
n=400 #Numero de puntos
h=(Fin-Ini)/(n-1)
i=Ini
X=[]
Y=[]
k=0

while i<=Fin:
    X.append (Ini+h*k)
    Y.append(g(X[k]))
    k=k+1
    i=i+h

plt.plot(x, y, "k")
plt.plot(x, y, "o")
plt.plot(X,Y,"r--")
plt.title('Interpolación Diferencias Divididas')
plt.ylabel('F(x)')
plt.xlabel('Xn')
plt.grid()
plt.show()