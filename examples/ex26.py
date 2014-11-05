# def bin2dec(n)
#     "Convierte un numero binario a base 10"
#     pass

def descomponer(n,base=2):
    """
    Keyword Arguments:
    n -- numero 
    """
    x = n
    i = 0
    suma = 0
    while x != 0:
        t = x%10
        x = x/10
        # print t,i,2**i,t*2**i
        suma += t*base**i
        i+=1
    return suma

print descomponer(100101101)
# print descomponer()

    

