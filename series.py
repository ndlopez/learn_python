#!/usr/bin/python3.8
#https://www.thespruce.com/stylish-small-entryway-ideas-4121671
n=2
for i in range(n):
    for j in range(n):
        #print(pow(2,j))
        print("this j",j,end=",")
        #j+=1
    #j=n-1
    while j > 0:
        #print(pow(2,j))
        j-=1
        print("anot j",j,end=",")
    print("this i",i)
'''
comp=True
while comp:
    n=29
    if n>0:
        comp=False
        for i in range(2,n):
            cre=2
            esP=True
            while esP and cre <i:
                if i % cre == 0:
                    esP=False
                else:
                    cre +=1
            if esP:
                print(i,end=",")
else:
    print(" ")'''
