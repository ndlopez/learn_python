#intervalo entre dos tiempos
time1,min1=map(int,input("Ingrese hora 1 y minutos: ").split())
time2,min2=map(int,input("Ingrese hora 2 y minutos: ").split())

a=time1+min1/60.0
b=time2+min2/60.0
print(time2,":",min2,"-",time1,":",min1)
if min2-min1 < 0:
    d=int((b-a)/1)
    if d == 0:
        c=(b-a)*60.0
    else:
        c=(b-a)%d*60.0
    print("Dif",d,":",int(c/1))
else:
    print("Dif",time2-time1,":",min2-min1)
