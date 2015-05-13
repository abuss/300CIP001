# __author__ = 'abuss'
#
#
# print("Creando archivo")
# f = open("demo.txt",mode="w")
# dato = "Hola Mundo\nesto es una prueba de archvo\n"
# f.write(dato)
# f.close()
#
# modo = 'r+'
# # modo = 'a'
#
# print("Adicionando a archivo")
# f = open("demo.txt",mode=modo)
# f.seek(5)
# dato = "--- Otra linea ---"
# f.write(dato)
# f.close()

nombre = "prueba3.box"
f = open(nombre)
prg = f.readline()
f.close()
print(prg)
