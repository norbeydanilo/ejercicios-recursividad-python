def potencia(n, m):
    if m <= 0:
        return 1
    else:
        return n * potencia(n, m-1)

n = int (input("Ingrese n: "))
m = int (input("Ingrese m: "))
potencia = potencia(n, m)
print "La potencia es: ", potencia
