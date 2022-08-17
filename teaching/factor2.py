#factor of 2
#e.g. n=7 -> factor=7
#n=6 -> factor=3*2; n=68 -> factor=2*2*17, 17*17*2

def factoresDos(number):
    z = int(number/2)
    count2 = 1
    myStr = ""
    if number % 2 == 1:
        return str(number)
    else:
        while z > 2 and z %2 == 0:
            aux = int(z/2)
            count2 += 1
            z = aux
        auxStr = ""
        for i in range(count2):
            auxStr += "2*"
        myStr += auxStr + str(z)
        return myStr

numero = int(input("Intro number: "))
result = factoresDos(numero)
print("factores",result)

'''
        while True:
            if z > 2 and z % 2 == 0:
                aux = int(z/2)
                count2 += 1
                z = aux
            else:
                auxStr = ""
                for i in range(count2):
                    auxStr += "2*"
                myStr += auxStr+str(z)
                return myStr
'''
