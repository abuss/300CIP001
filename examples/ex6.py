from turtle import *

def mover(x,y):
    "Mueve la tortuga a la posicion x,y"
    up()
    goto(x,y)
    down()

def cuadrado(b,h):
    "Dibuja un cuadrado"
    fd(b)
    left(90)
    fd(h)
    left(90)
    fd(b)
    left(90)
    fd(h)
    left(90)

def rectangulo(b,h,scala):
    "Dibuja un rectangulo con posibilidad de escala"
    fd(b*scala)
    left(90)
    fd(h*scala)
    left(90)
    fd(b*scala)
    left(90)
    fd(h*scala)
    left(90)

setup(300,300)
mover(-50,-50)

cuadrado(80,40)

mover(0,0)
left(30)
rectangulo(80,40,1.4)
rectangulo(80,40,0.4)
