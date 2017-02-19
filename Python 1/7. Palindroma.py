def palindroma(palabra):
    if len(palabra) < 2:
        return True
    else:
        if palabra[0] != palabra[-1]:
            return False
        else:
            return palindroma(palabra[1: len(palabra) - 1])

palabra = input("Ingrese una palabra: ")
if palindroma(palabra):
    print("Es palindroma.")
else :
    print("No es palindroma.")
