__author__ = 'abuss'

print("Creando archivo 1")
f = open("demotext1.txt",mode="w")
lista = [0,1,2,3,4,5,302,405]
dato = "{}".format(lista)
f.write(dato)
f.close()

print("Creando archivo 2")
f = open("demotext2.txt",mode="w")
lista = [0,1,2,3,4,5,302,405]
for x in lista:
    f.write(str(x))
f.close()

print("Creando archivo binario")
f = open("demoBin.txt",mode="wb")
lista = [0,1,2,3,4,5,202,105]
dato = bytearray(lista)
f.write(dato)
f.close()
