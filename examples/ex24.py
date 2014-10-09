def factorial(n):
    "Calcula el factorial de n de manera recursiva"
    if n==1:
        return 1
    else:
        return factorial(n-1)*n

def suma_r():
    "Suma un valores hasta que el numero leido es negativo"
    valor = int(input("numero?"))
    if valor < 0:
        return 0
    else:
        return valor+suma_r()


print suma_r()

# print "5!",factorial(5)
