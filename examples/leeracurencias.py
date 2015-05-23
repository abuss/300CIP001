__author__ = 'abuss'

arch = open('letras.mi_extencion','r')
lineas = arch.readlines()
lineas = [l.strip() for l in lineas]
print(lineas)
arch.close()

n = int(lineas[0])
occur = {}
j = 1

while j< len(lineas):
    letra = lineas[j]
    j+=1
    k,val = lineas[j].split(':')
    occur[letra] = [int(v) for v in val.split(',')]
    j+=2

print(occur)
cad = [' ']*n
for letra,pos in occur.items():
    for p in pos:
        cad[p] = letra
print(''.join(cad))

