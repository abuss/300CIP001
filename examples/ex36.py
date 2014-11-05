def menor(lista):
    "Retorna el elemento menor de la lista"
    menor = lista[0]
    for e in lista:
        if e<menor:
            menor = e
    return menor

def remove_menor(lista):
    "Retorna el elemento menor eliminandolo de la lista"
    i = 0
    pos = 0
    menor = lista[pos]
    while i<len(lista):
        if lista[i] < menor:
            menor = lista[i]
            pos = i
        i+=1
    lista.remove(pos)


def ordenar(lista):
    res = []
    while len(lista)>0:
        m = menor(lista)
        res.append(m)
        lista.remove(m)
    return res



l = [4,1,6,3,9,5,2,7,5,8]

print l
print ordenar(l)

