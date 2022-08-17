#!/usr/bin/python3.8
#a=[7,13,9,2.5,0.99,12]

a0,a1,a2,a3=map(float,input("ingrese 4 numeros: ").split())

a=[]
a.append(a0)
a.append(a1)
a.append(a2)
a.append(a3)
b=[]
myLen=len(a)
for j in range(myLen):
    aux=0
    z=[]
    i=0
    while i < len(a):
        if a[i] > aux:
            aux=a[i]
            idx=i

        i+=1
    b.append(aux)
    a.pop(idx)
print("orden desc",b)
