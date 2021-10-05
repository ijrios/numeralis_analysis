"""
Created on Thu Apr 11 09:11:02 2019

@author: jario
"""

import numpy as np
import matplotlib.pyplot as plt



#VECTORES x y - recoleccion de datos
n = int(input("Ingrese numero de datos a ingresar: "))
tra = int(input("Ingrese el tamaño de la trama del mensaje: "))
nom = input("Ingrese el nombre del destinatario: ")
ap = input("Ingrese el apellido del destinatario: ")

# CREACION DE ARRAYS
a=[[0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0],[0.0,0.0,1.0,0.0,0.0,0.0,4.0,2.0,1.0],[1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,4.0,2.0,1.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,9.0,3.0,1.0],[2.0,1.0,0.0,-2.0,-1.0,0.0,0.0,0.0,0.0],[0.0,0.0,  0.0,4.0,1.0,0.0,-4.0,-1.0,0.0],[0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
b=[[1.0],[-2.0],[3.0],[-2.0],[3.0],[0.0],[0.0],[0.0],[-2.0]]

A=np.matrix(a)
B=np.matrix(b)
invA=np.linalg.inv(A)
s=invA*B

x=[0.0, 1.0, 2.0, 3.0]
y=[1.0, -2.0, 3.0, 0.0]
ak=[]
bk=[]
ck=[]
u=[]
u1=-2.0
i=1

u.append(u1)
for i in range (1,n):
   
    u.append((-u[-1])+2.0*((y[i]-y[i-1])/(x[i]-x[i-1])))
    ak.append(0.5*((u[i]-u[i-1])/(x[i]-x[i-1])))
    bk.append(u[i-1]-2.0*ak[-1]*x[i-1])
    ck.append(y[i-1]-x[i-1]*u[i-1]+((x[i-1])**2)*ak[i-1])

#funciones
def f(t):
    return -1.0*t**2-2.0*t+1.0 
def g(t):
    return 9.0*t**2-22.0*t+11.0 
def l(t):
    return -17.0*t**2+82.0*t-93.0 
    
#graficacion
a=0.0
b=1.0
c=2.0
d=3.0
n=100.0
h1=(b-a)/(n-1.0)
h2=(c-b)/(n-1.0)
h3=(d-c)/(n-1.0)
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
while i<=c:
    X2.append (b+h2*k)
    Y2.append(g(X2[k]))
    k=k+1
    i=i+h2
    
i=2
k=0
while i<=d:
    X3.append (c+h2*k)
    Y3.append(l(X3[k]))
    k=k+1
    i=i+h2
 


print("\n")
print("Mensaje dirigido a: "+ nom +" "+ap)
print("\n")
print("================ INICIO DEL MENSAJE ================================")
print(" ¿Cuál olvido bebesitaaa?, es puro sueño. En su maximo esplendor jajaja.")
print("-------------------   Regaleme un blon   -------------------------------")
print("================ FIN DEL MENSAJE ================================")
print("\n")
print("============================================================")
print("CALCULO DE ESTADO DE ANIMO ESTIMADO PARA EL SEÑOR : " + nom +'  '+ap)
print("---------------------- resultado ---------------------------")
print('El resultado es: ' + str(ak))
print('Existencialismo fase 2, con cuadro de insomnio en el rango: ' + str(bk))
print("============================================================")
plt.plot(x,y,"^", color = 'black')
plt.plot(X1,Y1,X2,Y2,X3,Y3,"-")
plt.title("VARIACION DE ESTADO DE ANIMO")
plt.ylabel("Señal de analisis")
plt.xlabel("t(s)")
plt.grid()
plt.show()    


