def mcd(num1, num2):
    if(num2 == 0):
        return num1
    else:
        return mcd(num2, num1%num2)

num1 = int (input("Ingrese primer numero: "))
num2 = int (input("Ingrese segundo numero: "))
mcd = mcd(num1,num2)
print "El mcd de ",num1," y ",num2," es: ",mcd
