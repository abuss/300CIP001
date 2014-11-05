def existe(elem,lista):
    "Retorna True si elem existe en la lista, Falso en caso contrario"
    i = 0
    while i<len(lista) and lista[i]!=elem:
        i+=1
    if i==len(lista):
        return False
    return True

def existe2(elem,lista):
    "Retorna True si elem existe en la lista, Falso en caso contrario"
    for x in lista:
        if x==elem:
            return True
    return False



print "Busca 10:",existe(10,[3,6,2,8,5,3,9])
print "Busca 8:",existe(8,[3,6,2,8,5,3,9])

print "Busca 10:",existe2(10,[3,6,2,8,5,3,9])
print "Busca 8:",existe2(8,[3,6,2,8,5,3,9])
