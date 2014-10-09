import math

def plot(f,xi,xf):
    "Grafica de manera textual la evaluacion de la funcion f entre xi y xf"
    x = xi
    while x<xf:
        y = f(x)
        if x==0:
            print '+'+'-'*y+'*'+'-'*(60-y)
        else:
            print '|'+" "*y+'*'
        x+=1

def f1(x):
    return x*x

def f2(x):
    return x*x+4

def f3(x):
    return int(math.sqrt(x))

plot(f2,-10,10)
