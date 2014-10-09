def tabla(n,m):
    "imprime la tabla de multiplicacion del numero n del 1 hasta m"
    suma = 0
    k = 1
    while k<=m:
        res = k*n
        suma = suma + res
        print k,'x',n,'=',res
        k  = k +1
    return suma

def tablas(n1,n2,m):
    "Imprime las tablas de multiplicar desde el numero n1 hasta el n2 del 1 hasta m"
    r = n1
    suma = 0 
    while r <= n2:
        suma+=tabla(r,m)
        print "-"*10
        r+=1
    print "suma total",suma


def tablas_for(n1,n2,m):
    "Imprime las tablas de multiplicar desde el numero n1 hasta el n2 del 1 hasta m"
    suma = 0 
    for r in range(n1,n2+1):
        suma+=tabla(r,m)
        print "-"*10
    print "suma total",suma

r = tabla(7,10)
print "La suma de la tabla del 7 es",r

tablas(3,5,7)

tablas_for(3,5,7)

