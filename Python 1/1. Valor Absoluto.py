def absoluto(num):
    if(num >= 0):
        return num
    else:
        return absoluto(-num)

num = int (input("Ingrese un numero: "))
print "El valor absoluto de ", num, " es: ", absoluto(num)
