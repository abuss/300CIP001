# Esto es un comentario

def cuadrado_f(x):
    """Calcula el numero
al cuadrado"""
    y = x * x
    return y

def cuadrado_p(x):
    """Imprime el numero al cuadrado"""
    # return 1000
    y = x * x
    print("El cuadrado es:",y)


# a = cuadrado_f(5)
# print("el cuadrado de 5 es",a)

# b = cuadrado_p(5)
# print("el cuadrado de 5 es",b)

z = cuadrado_p(cuadrado_f(3))

print("el cuadrado al cuadrado de 3 es",z)



print("done")
