import math
import random

def calculoPi(n):
    "Calculo del numero Pi con el metodo de Monte Carlo"
    i = 0
    c = 0.0
    while i<n:
        i += 1
        x = random.random()
        y = random.random()
        d = math.sqrt(x*x+y*y)
        if d<1:
            c +=1
    return c/n*4

print calculoPi(10)
print calculoPi(100)
print calculoPi(1000)
print calculoPi(10000)
print calculoPi(100000)
print calculoPi(1000000)
print calculoPi(10000000)

