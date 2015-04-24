from turtle import *
import math

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

def area_circulo(r):
    "Calcula el area de un circulo de radio r"
    area = math.pi * r**2
    return area

def cuadrado(lado):
    radio = lado / 2
    fd(lado/2)
    left(90)
    fd(lado)
    left(90)
    fd(lado)
    left(90)
    fd(lado)
    left(90)
    fd(lado/2)
    begin_fill()
    circle(radio,360)
    end_fill()
    area = area_circulo(radio)
    return area

def triangulo_equilatero(base):
    radio = math.tan(math.pi/6)*base/2
    fd(base/2)
    left(120)
    fd(base)
    left(120)
    fd(base)
    left(120)
    fd(base/2)
    begin_fill()
    circle(radio,360)
    end_fill()
    area = area_circulo(radio)
    return area

setup(300,300)
mover(0,50)
print("Area:", cuadrado(28.8675*2))
mover(0,-100)
print("Area:", triangulo_equilatero(100))
