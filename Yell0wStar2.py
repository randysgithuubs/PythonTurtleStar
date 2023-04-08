
import turtle

scr = turtle.Screen()
scr.bgcolor("black")

turtle.showturtle()

turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.shape("turtle")
turtle.end_fill()

length1 = 75
length2 = 125
angle = 90

for x in range(5):
    turtle.forward(length1)
    turtle.right(angle)
    turtle.right(length2)



turtle.done()


























