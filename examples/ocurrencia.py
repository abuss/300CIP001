__author__ = 'abuss'

cad = "Hola, esto es una cadena de texto de prueba para el problema de ocurrencia"

occur = {}

p = 0
for x in cad:
    # print(p,x)
    if not (x == ' '):
        n = occur.setdefault(x,{'pos':[],'n':0})
        occur[x]['pos'].append(p)
        occur[x]['n'] += 1
    # print(occur)
    p+=1

mayorL = ''
mayorV = 0
for item in occur.items():
    # print(item)
    k,v = item
    if v['n'] > mayorV:
        mayorL = k
        mayorV = v['n']

print("Letra que mas se repite es '{1}', se repite {0} veces".format(mayorV,mayorL))
print(occur)

arch = open('letras.mi_extencion','w')
arch.write('{}\n'.format(len(cad)))
for item in occur.items():
    k,v = item
    arch.write(k+'\n')
    cad = ','.join(['{}'.format(x) for x in v['pos']])
    arch.write(' pos:'+cad+'\n')
    arch.write(' n:{}\n'.format(v['n']))

arch.close()
