def min(a,b):
    "Retorna el valor minimo entre a y b"
    if a<b:
        return a
    else:
        return b

def max(a,b):
    "Retorna el valor maximo entre a y b"
    if a>b:
        return a
    else:
        return b

suma = 0
n = 0
tecla = raw_input("Numero? (o 'q' para salir)")
min_tmp = float(tecla)
max_tmp = float(tecla)
while (tecla!='q'):
    print tecla
    nota = float(tecla)
    suma = suma + nota
    n = n + 1
    min_tmp = min(nota,min_tmp)
    max_tmp = max(nota,max_tmp)
    tecla = raw_input("Numero? (o 'q' para salir)")

print "Promedio:",suma/n, "minima noto:",min_tmp,"maxima nota:",max_tmp


