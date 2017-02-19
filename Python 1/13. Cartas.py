def contador(lista):
    if(len(lista)==0):
        return 0
    else:
        if(identificador(lista[0])=='j' or identificador(lista[0])=='q' or identificador(lista[0])=='k'):
            return contador(lista[1:])+10
        if(identificador(lista[0])=='A'):
            return contador(lista[1:])+1
        else:
            return contador(lista[1:])+ identificador(lista[0])

def suma(lista):
    if(len(lista)==0):
        return 0
    if(contador(lista)>11):
        return contador(lista)
    else:
        if(identificador(lista[0])=='A'):
            return contador(lista)+10
        else:
            if(identificador(lista[0])=='j' or identificador(lista[0])=='q' or identificador(lista[0])=='k'):
                return suma(lista[1:])+10
            else:
                return suma(lista[1:])+ identificador(lista[0])


def identificador(lista):
    return lista[0]
    
lista=[['A','diamante'],['j','diamante'],['A','diamante']]
print(suma(lista))


    
