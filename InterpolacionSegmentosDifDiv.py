import numpy as np
import matplotlib.pyplot as plt




x=[]
y=[]

m=int((input("ingrese el numero de puntos : ")))


x=[0,1,2,3]
y=[1,-2,3,0]




uk=[-2]
ak=[]
bk=[]
ck=[]
A=[]


for i in range (m-1):
    U=(-uk[-1])+2*(y[i+1]-y[i])/(x[i+1]-x[i])
    uk.append(U)
    
for i in range(m-1):
  
    ak.append(1/2*((uk[i+1]-uk[i])/(x[i+1]-x[i])))
    bk.append(uk[i]-2*(x[i]*ak[i]))
    ck.append(y[i]-x[i]*uk[i]+(x[i]**2)*ak[i])

print("uk",uk) 
print("ck",ak)
print("bk",bk)
print("ck",ck)


for i in range(3):
    A.append([])
    for j in range(6):
        A[i].append(0)


for i in range (m-1):
    A[i][0]=(x[i])
    A[i][1]=(y[i])
    A[i][2]=(uk[i])
    A[i][3]=ak[i]
    A[i][4]= bk[i]
    A[i][5]= ck[i]

a=np.matrix(A)
print("La matriz resultante es: ")
print (a)


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
 
    
#print X
#print Y
plt.plot(x,y,"o")
#plt.plot(X2,Y2,"g")
plt.plot(X1,Y1,X2,Y2,X3,Y3,"g")
plt.grid()
plt.show()
        
        


    




