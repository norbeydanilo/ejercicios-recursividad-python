def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int (input("Ingrese el numero: "))
factorial = factorial(num)
print "El factorial es: ", factorial
