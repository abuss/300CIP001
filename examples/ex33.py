from turtle import *

setup(400,400)

t1 = Turtle()
t2 = Turtle()

register_shape("x.gif")
# addshape('x')
# t1.pensize(20)
t1.shape('x.gif')

def do_move():
    t1.fd(10)
    ontimer(do_move,250)

def do_left():
    t1.left(15)

def do_right():
    t1.right(15)

onkey(do_move,"Up")
onkey(do_left,"Left")
onkey(do_right,"Right")

do_move()

running = True
def f():
    if running:
        fd(50)
        lt(60)
        ontimer(f, 250)
f()   ### makes the turtle march around
running = False

listen()
mainloop()
