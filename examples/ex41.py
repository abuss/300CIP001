def encriptar(texto,clave):
    "Retorna el texto encriptado basado en la clave data"
    vocales = ['a','e','i','o','u']
    t = {}
    pos = 0
    for letra in clave:
        if letra in vocales:
            if not t.has_key(letra):
                t[letra] = pos
        pos +=1

    for k in t.keys():      
        texto = texto.replace(k,str(t[k]))

    return texto
    # i = 0
    # res = [x for x in texto]
    # print res
    # while i<len(res):
    #     if res[i] in vocales:
    #         if t.has_key(res[i]):
    #             res[i] = "%s" % t[texto[i]]
    #     i+=1
    # return ''.join(res)

def desencriptar(texto,clave):
    "Retorna el texto desencriptado basado en la clave data"
    numeros = [str(x) for x in range(10)]
    res = [x for x in texto]
    pos = 0
    for letra in res:
        if letra in numeros:
            res[pos] = clave[int(letra)]
        pos+=1
    return ''.join(res)


cad = encriptar("Hola mundo","murcielago")
print cad
print desencriptar(cad,"murcielago")

cad = encriptar("Hola mundo","pepito")
print cad
print desencriptar(cad,"murcielago")
