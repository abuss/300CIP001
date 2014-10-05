from turtle import *

setup(300,300)

def mover(x,y):
    up()
    goto(x,y)
    down()

def rect(b,h):
    fd(b)
    left(90)
    fd(h)
    left(90)
    fd(b)
    left(90)
    fd(h)
    left(90)

for x in range(1,11):
    mover(-10*x,-10*x)
    rect(20*x,20*x)

goto(-10,-10)
mover(10,-10)
goto(100,-100)
mover(100,100)
goto(10,10)
mover(-10,10)
goto(-100,100)

mover(1000,0)
