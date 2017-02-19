def fibonacci(num):
    if(num < 2):
        return num;
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int (input("Ingrese el numero para saber su sucesion de fibonacci: "))
fib = fibonacci(num)
print "La sucesion de fibonacci de ",num," es: ",fib
