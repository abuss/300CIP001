from turtle import *
import math

setup(300,300)

def mover(x,y):
    up()
    goto(x,y)
    down()

def draw(x0,y0,d):
    ang = heading()
    mover(x0,y0)
    forward(d)
    (xm,ym) = pos()
    if d>30:
        mover(xm,ym)
        left(30)
        draw(xm,ym,d-15)
        mover(xm,ym)
        seth(ang)
        right(40)
        draw(xm,ym,d-12)

left(90)
draw(0,-200,100)

