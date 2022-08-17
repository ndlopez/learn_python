input_n = int(input("Enter a number: "))

def factorial(num):
	fac = 1
	perm = []
	for i in range(1,num+1):
		fac = fac * i
		perm.append(i)
	return fac, perm

myarr = []
choose = 2 #choose 2 out of n
combi,myarr = factorial(input_n)
sel,_=factorial(input_n-choose)
print("combi",int(combi/(sel*2)),"perm",myarr)
for item in range(len(myarr)):
	print(myarr[item],myarr[item+1])

