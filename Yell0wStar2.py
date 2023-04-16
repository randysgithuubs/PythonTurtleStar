#(Made by:randysgithuubs on Github)

import turtle

scr = turtle.Screen()
scr.bgcolor("black")
turtle.speed(1)
turtle.showturtle()

turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.shape("turtle")

length1 = 75
length2 = 125
angle = 90

for x in range(5):
    turtle.forward(length1)
    turtle.right(angle)
    turtle.right(length2)

turtle.done()


