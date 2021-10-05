#INTEGRACION NUMERICA

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return t**2*np.e**(-t)

liminf=int(input("Ingrese el valor del límite inferior: "))
limsup=int(input("Ingrese el valor del límite superior: "))
h=float(input("Ingrese el valor de h: "))
xk=((limsup-liminf)/2)

yk=f(xk)

xk1=xk+h
xk2=xk-h

yk1=f(xk1)
yk2=f(xk2)

print("\n")
print("Función original: " + str(yk))

f1=(yk1-yk2)/(2.0*h) #primera derivada
f2=(yk1-2*yk+yk2)/(h**2) #segunda derivada

print("Primera derivada: "+str(f1))
print("Segunda derivada: "+str(f2))


a=(f2/2)
b=(f1-xk*f2)
c=((f2/2)*xk**2)

print("a= "+str(a))
print("b= "+str(b))
print("c= "+str(c))

def g(t):
    return ((a*t**3)/3)+(b*t**2)/2+c*t

F=g(limsup)-g(liminf)

print("El resultado de la integral aproximadamente es: "+str(F))

#GRAFICA
x=[]
y=[]
n=100
hg=(limsup-liminf)/(n-1)

for i in range(n):
    x.append(liminf + (i*hg))
    y.append(f(x[i]))

x1=[]
y1=[]

def m(t):
    return (a*t**2)+(b*t)+c

for i in range(n):
    x1.append(liminf + (i*hg))
    y1.append(m(x1[i]))
    
plt.plot(x,y,x1,y1, "purple") 
plt.grid()
plt.show()
