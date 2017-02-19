def binAdec(n):
    if(n < 10):
        return n
    else:
        return(n%10)+binAdec(n/10)*2

numero = int (input("Ingrese el numero: "))
print "El numero decimal es: ", binAdec(numero)
