"Conjuntos"


def interseccion(A:list, B:list) -> list:
    "Retorna los elementos comunes entre los conjuntos A y B"
    c = []
    for a in A:
        for b in B:
            if a==b:
                 c.append(a)
    return c

def interseccionI(A:list, B:list) -> list:
    "Retorna los elementos comunes entre los conjuntos A y B"
    c = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i]==B[j]:
                c.append(A[i])
    return c

def interseccionW(A:list, B:list) -> list:
    "Retorna los elementos comunes entre los conjuntos A y B"
    c = []
    i = 0
    while i<len(A):
        j = 0
        while j<len(B):
            if A[i]==B[j]:
                c.append(A[i])
            j+=1
        i+=1
    return c


def union(A:list, B:list) -> list:
    "Retorna la union de elementos de A y B sin repetir elementos"
    c = A
    for b in B:
        if not b in A:
            c.append(b)
    return c


# a = [1,2,3,4,5]
# b = [7,2,4,5,8,9]
# print(interseccion(a,b))
# print(interseccionW(a,b))
#
# print(interseccion(['a','b','d','e','h'],['z','f','h','i','b']))
# print(interseccionW(['a','b','d','e','h'],['z','f','h','i','b']))
#
# print("union",union(a,b))
# print("union",union(['a','b','d','e','h'],['z','f','h','i','b']))

import random

def generarConj(n=4) -> list:
    c = []
    i = 0
    while i<n:
        valor = chr(ord('a')+random.randint(0,9))
        if not valor in c:
            c.append(valor)
            i+=1
    return c

print(generarConj())
print(generarConj(6))
print(generarConj(10))
