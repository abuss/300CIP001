import math

def promedio(datos):
    "Calcula el promedio de los valores en el vector de datos"
    i = 0
    suma = 0.0
    while i<len(datos):
        suma += datos[i]
        i+=1
    return suma/len(datos)


def promedio(datos):
    "Calcula el promedio de los valores en el vector de datos"
    suma = 0.0
    for x in datos:
        suma += x
    return suma/len(datos)


def devstd(datos):
    "Calcula la desviacion estandar de los datos entrados"
    prom = promedio(datos)
    suma = 0.0
    i = 0
    while i<len(datos):
        tmp = datos[i]-prom
        suma += tmp**2
        i+=1
    return math.sqrt(suma/len(datos))

l = [2, 4, 5, 3, 7.3, 8.1, 2.1]
print l,"devstd:",devstd(l)
