import math

def fact(n):
    r = 1
    for i in range(1,n+1):
        r *=i
    return r

def sen(x):
    "Calcula el seno de x usando la serie de Taylor"
    i = 0
    suma = 0
    signo = 1
    while i < 8:
        p = 2*i+1
        suma = suma + signo*(x**p)/fact(p)
        # suma = suma + signo*(x**p)/math.factorial(p)
        # print signo*(x**p)/fact(p)
        signo *=-1
        i+=1
    return suma

print "sen(30)=",sen(math.pi/3)
print "sin(30)=",math.sin(math.pi/3)
