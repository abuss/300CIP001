"Directorio de contactos"

def addContacto(directorio,contacto):
    """Adiciona un contacto a la lista de contactos
     direcorio es una lista de contactos
     contacto es una lista con el nombre, telefono y email
    """
    c = buscarContactoNombre(directorio,contacto[0])
    if len(c):
        directorio.remove(c)
    directorio.append(contacto)


def buscarContactoNombre(directorio,nombre):
    "Busca el contacto especificado (nombre) en la lista de contactos"
    for c in directorio:
        if nombre==c[0]:
            return c
    return []

def comparaNombres(x,y):
    return x[0]<y[0]

def comparaNumeros(x,y):
    return x<y

def ordenar(lista,comp):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if comp(lista[j],lista[i]):
                tmp = lista[i]
                lista[i] = lista[j]
                lista[j] = tmp
    return lista


l = [4,1,6,3,9,5,2,7,5,8]

print l
print ordenar(l,comparaNumeros)

# ----------------------------------------

directorio = []

addContacto(directorio,["Pedro Perez",3124567890,"pperez@correo.com"]) 
addContacto(directorio,["Pedro Perez",3218200,"pperez@correo.com"]) 
addContacto(directorio,["Pablo Marmol",3452341234,"pmarmol@correo.com"]) 

c = buscarContactoNombre(directorio,"Pablo Marmol")
if len(c):
    print "el telefono de Pablo Marmol es:",c[1]
else:
    print "Pablo Marmol no existe en el directorio"

c = buscarContactoNombre(directorio,"Pedro Perez")
if len(c):
    print "el telefono de Pedro Perez es:",c[1]
else:
    print "Pedro Perez no existe en el directorio"

print directorio
print ordenar(directorio,comparaNombres)
