def sumaDigitos(num1):
    if (num1 == 0):      
        return num1
    else:
        return sumaDigitos(num1/10)+(num1%10)
num1 = int (input("Ingrese el numero: "))
suma = sumaDigitos(num1)
print "La suma de los digitos de ",num1," es: ",suma
