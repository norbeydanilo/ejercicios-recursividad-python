def division(num1, num2):
    if(num1 < num2):
        return 0;
    else:
        return division((num1 - num2), (num2)) + 1
    
num1 = int (input("Ingrese el dividendo: "))
num2 = int (input("Ingrese el divisor: "))
div = division(num1, num2)
print "La division de ",num1," en: ",num2, " es: ",div
