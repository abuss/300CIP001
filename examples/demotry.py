__author__ = 'abuss'


nombre = "prueba4.box"

try:
    f = open(nombre)
    prg = f.readlines()
    f.close()
except:
    print("Archivo",nombre,"no existe")
    exit()

print(prg)

# x = 1
# y = 2
# try:
#     y = 100
#     x = x/0
# except:
#     pass
#
# print(x,y)
