__author__ = 'abuss'

tablero = [[0,0,0],[0,0,0],[0,0,0]]

def poner(tbl,figura):
    i = int(input("fila:"))
    j = int(input("columna:"))
    tbl[i][j]=figura

def printTablero(tbl):
    for fila in tbl:
        for e in fila:
            if e==0:
                print('_ ',end='')
            else:
                print(e+' ',end='')
        print()


while not (ganar(tablero) or empate(tablero)):
    printTablero(tablero)
    poner(tablero,'X')
    printTablero(tablero)
    poner(tablero,'O')

