"Dibuja un cuadrado"

import turtle
print dir()

turtle.setup(300,400)
turtle.shape("turtle")
turtle.color("red")

turtle.forward(100)
turtle.left(90)
turtle.color("blue")
turtle.forward(100)
turtle.left(90)
turtle.color("green")
turtle.forward(100)
turtle.left(90)
turtle.color("pink")
turtle.forward(100)
turtle.left(90)

turtle.up()
turtle.goto(-50,50)
turtle.color("black")
turtle.down()
turtle.circle(50)

turtle.up()
turtle.home()
turtle.down()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()
#turtle.home()
