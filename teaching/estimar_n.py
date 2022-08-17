#estimar pi
'''
def estimar(n):
    i=1
    s=0
    while (i <= n):
        a=((-1)**(i+1))/(2*i -1)
        s+=a
        i+=1
    m=4*s
    return m

n=int(input("intro n:"))
print("n    i    m(i)")
k=0
for i in range(1,n+1,100):
    print("{:<2d}    {:3d}    {:.4f}".format(k+1,i,estimar(i)))
    #i+=1
    k+=1
    #m+=1
'''

#CO2 problem
'''input_line = input()
data=[]
data=input_line.split()
m=int(data[0]) #kg
p=int(data[1]) #%
q=int(data[2]) #%
if m >= 1 and m <= 1000:
    if p >=0 or q <= 100:
        if p==100:
            q=0
    
        pKg=m*p/100 #p in kg
        leftKg=m-pKg
        foodLeftKg=leftKg*q/100 #q in Kg
        leftResult=leftKg-foodLeftKg
        print("{:.4f}".format(leftResult))
'''

input_n=int(input("ingrese n: "))
input_m=int(input("ingrese m: "))
def factorial(num):
    fact=1
    perm=[]
    for i in range(1,num+1):
        fact = fact * i
        perm.append(i)
    return fact,perm

myarr=[]
fact_n,myarr=factorial(input_n)
fact_m,_=factorial(input_m)
fact_nm,_=factorial(input_n-input_m)
combi_num=int(fact_n/(fact_m*fact_nm))
print(combi_num,myarr)
jdx,count=1,0
for idx in range(len(myarr)-1):
    while(jdx < len(myarr)):
        if myarr[idx] != myarr[jdx]:
            aux=myarr[idx],myarr[jdx]
            print(myarr[idx],myarr[jdx])
            count+=1
        jdx+=1
        if count >= combi_num:
            break
    jdx=jdx-count

'''
import math
def desv(vec,prom):
    n=len(vec)
    sum=0.0
    for i in range(n):
        sum+=(vec[i]-prom)**2
        print(sum)
    sum/=(n-1)
    sum=sum**(1/2)
    return sum

def promedio(vec):
    sum=0.0
    for i in range(len(vec)):
        sum+=vec[i]

    return sum/len(vec)

vlist=(1.9,2.5,3.7,2,1,6,3,4,5,2)
x=promedio(vlist)
y=desv(vlist,x)
print(x,y)

def factorial(num):
    i=1
    fact=1
    while(i<num):
        i+=1
        fact*=i
    return fact
def comb(n,m):
    combi=factorial(n)/(factorial(m)*factorial(n-m))
    return combi
new_combi=comb(input_n,2)
print(new_combi)'''