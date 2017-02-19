def minimos(lista):
    if(len(lista)==1):
        return [encontrar(lista[0])]
    else:
        return [encontrar(lista[0])]+minimos(lista[1:])
    
def encontrar(lista):
    if(len(lista)==1):
        return lista[0]
    else:
        if(lista[0]<lista[1]):
            return encontrar(lista[2:]+[lista[0]])
        else:
            return encontrar(lista[1:])
        
lista=[[2,3,4],[2,1,-2,3],[4,3,2,4,5],[20,10],[24,43,21,34,45,64,22],[0,4,2]]
print(minimos(lista))
    
    
