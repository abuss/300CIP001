import pprint

#espacio de juego
espacio = []
for i in range(6):
    espacio.append([0]*7)

espacio[4][2]=99

pp = pprint.PrettyPrinter()
pp.pprint(espacio)

def jugar(espacio,programa):
    # 0: arriba
    # 1: derecha
    # 2: abajo
    # 3: izquierda
    direccion = 0

    # posicion (fila,columna)
    pos = (5,0)

    print("Inicio en posicion:",pos)
    print("Direccion inicial:",direccion)

    # lineas = programa.split("\n")
    lineas = programa
    print(lineas)
    for cmd in lineas:
        cmd = cmd.strip()
        print(cmd)
        print("-> ",end="")
        if cmd == "mover":
            if direccion==0: # arriba
                pos = (pos[0]-1,pos[1])
            if direccion==1: # derecha
                pos = (pos[0],pos[1]+1)
            if direccion==2: # abajo
                pos = (pos[0]+1,pos[1])
            if direccion==3: # izquierda
                pos = (pos[0],pos[1]-1)
            print("Nueva posicion:",pos)

        if cmd[0:11] == "cambiar_dir":
            nueva_dir = cmd[12:-1]
            if nueva_dir=="arriba":
                direccion = 0
            if nueva_dir=="derecha":
                direccion = 1
            if nueva_dir=="abajo":
                direccion = 2
            if nueva_dir=="izquierda":
                direccion = 3

        if cmd == "tomar":
            if espacio[pos[0]][pos[1]]==99:
                print("Tomo la Caja!!")
                espacio[pos[0]][pos[1]]=0
            else:
                print("No hay caja")

            print("Nueva direccion:",direccion)
        print()


import sys

if len(sys.argv)<2:
    print("Falta nombre del archivo\n")
    exit(0)

nombre = sys.argv[1]
f = open(nombre)
prg = f.readlines()
f.close()

jugar(espacio,prg)
pp.pprint(espacio)
