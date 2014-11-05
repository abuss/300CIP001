def ordenar(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[j]<lista[i]:
                tmp = lista[i]
                lista[i] = lista[j]
                lista[j] = tmp
    return lista

l = [4,1,6,3,9,5,2,7,5,8]

print l
print ordenar(l)

