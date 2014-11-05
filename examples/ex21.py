def fact(n):
    "Calcula el factorial de n (n!)"
    res = 1
    for i in range(1,n+1):
        res *=i
    return res

def comb(n,m):
    "Calcula el combinatorio de (n,m)"
    return fact(n)/(fact(n-m)*fact(m))

def triangulo_pascal(n):
    "Imprime el triangulo de pascal hasta el nivel n"
    for i in range(n):
        print ' '*(2*n-(i*2)),
        for j in range(i+1):
            print "%3d" % comb(i,j),
        print

print
triangulo_pascal(8)
