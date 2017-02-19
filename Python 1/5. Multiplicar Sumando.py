def multiplicar(num1, num2):
    if (num2 <= 1):
        return num1
    else:
        
        return num1 + multiplicar(num1, num2-1)
        
num1 = int (input("Ingrese numero 1: "))
num2 = int (input("Ingrese numero 2: "))
resultado = multiplicar(num1, num2)
print "El resultado es: ",resultado
        

    
