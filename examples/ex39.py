def buscar_impl(elem,lista,ini,fin):
    """Busca el elemento elem en la lista usando busqueda binaria de
manera recursiva. Precondicion: lista ordenada de menor a mayor"""
    if ini>fin:
        return False
    mitad = (ini+fin)/2
    if elem==lista[mitad]:
        return True
    if elem <= lista[mitad]:
        return buscar_impl(elem,lista,ini,mitad)
    if elem > lista[mitad]:
        return buscar_impl(elem,lista,mitad+1,fin)

def buscar(elem,lista):
    return buscar_impl(elem,lista,0,len(lista)-1)

l = [4,1,6,3,9,5,2,7,5,8]
l.sort()
print l
print buscar(7,l)
print buscar(17,l)
print buscar(2,l)

