def insertar(x,L):
    "Inserta el valor x en la lista ordenada L y el resultado queda ordenado"
    pos = 0
    while pos < len(L):
        if L[pos] > x:
            L.insert(pos,x)
            return L
        pos += 1
    L.append(x)
    return L



datos = [1,3,5,6,9,12,15,20]

print "insert 7 en",datos,":",insertar(7,datos)

print "insert 7 en",datos,":",insertar(7,datos)

print "insert 200 en",datos,":",insertar(200,datos)

