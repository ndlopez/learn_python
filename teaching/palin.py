'''a=1038431
z=a
aux=0
while a > 0:
    b=int(a/10)
    c=a%10
    a=b
    aux=aux*10+c

if aux == z:
    print(z," es palindromo")
else:
    print(z," no es palin")
#print(b,c,a,aux)'''
#calc log(number,base)
import math
base=2
number=-0.5
if number > 0:
    aux=math.log(number)/math.log(base)
else:
    aux="Nan"
print("log",number,"base",base," es",aux)