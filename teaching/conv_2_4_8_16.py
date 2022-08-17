#convert a number into binary
#base=16
#numb0-9=string.digits
#numb10-16=ABCDEF

def convert_to_base(base,num):
    conv_num = ""
    auxStr = ""
    mod2 = num%base
    div2 = int(num/base)
    auxStr += str(mod2)
    while div2 >= base:
        auxdiv = div2
        auxmod = mod2
        mod2 = div2%base
        auxStr += str(mod2)
        div2 = int(div2/base)
    conv_num = str(div2) + auxStr[::-1]
    return conv_num

def base16(num):
    base=16
    r = num % base
    if num - r == 0:
        return toChar(r)
    return str(int((num - r) / base)) + toChar(r)

def toChar(n):
    alpha = "0123456789ABCDEF"
    return alpha[n]

def call_function(base,number):
    if base == 16:
        return base16(number)
    else:
        return convert_to_base(base,number)

numb = int(input("Intro number: "))
print("bin",call_function(2,numb))
print("tet",call_function(4,numb))
print("oct",call_function(8,numb))
print("hex",call_function(16,numb))
