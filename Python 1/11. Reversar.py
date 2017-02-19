def rev(lista):
    if len(lista)==0:
        return []
    else:
        return [lista[-1]] + rev(lista[:-1])

lista = [0,1,2,3,4]
print (rev(lista))


    
