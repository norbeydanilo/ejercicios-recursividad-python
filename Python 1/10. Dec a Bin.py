def decAbin(numero):
    if numero < 2:
        return numero
    else :
        return (10 * decAbin(numero/2)) + numero%2

numero = int (input("Ingrese el numero: "))
decAbin = decAbin(numero)
print "El numero en binario es: ", decAbin





