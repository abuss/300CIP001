def buscar(elem,lista):
    "Busca el elemento elem en la lista usando busqueda binaria. Precondicion: lista ordenada de menor a mayor"
    ini = 0
    fin = len(lista)-1
    mitad = (ini+fin)/2
    while elem!=lista[mitad] and ini<fin:
        if elem <= lista[mitad]:
            fin = mitad
        if elem > lista[mitad]:
            ini = mitad+1
        mitad = (ini+fin)/2
    if elem==lista[mitad]:
        return True
    return False


l = [4,1,6,3,9,5,2,7,5,8]
l.sort()
print l
print buscar(7,l)
print buscar(17,l)
print buscar(2,l)

