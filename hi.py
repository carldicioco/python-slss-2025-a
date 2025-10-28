import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles
# create a turtle called mikey
mikey = turtle.Turtle()
mikey.turtlesize(0.5)  # size
mikey.color("white")  # colour
mikey.shape("turtle")


mikey.turtlesize(10)  # size
mikey.color("orange")  # colour
mikey.pencolor("black")
mikey.shape("turtle")  # shape
mikey.speed(2)
mikey.width(5)

mikey.penup()
mikey.forward(100)
mikey.left(90)
mikey.pendown()

mikey.forward(50)
mikey.left(90)
mikey.forward(200)
mikey.right(90)
mikey.forward(50)
mikey.right(90)
mikey.forward(75)
mikey.pencolor("gold")
mikey.forward(50)
mikey.right(90)
mikey.forward(50)
mikey.right(90)
mikey.forward(50)
mikey.right(90)
mikey.forward(50)
mikey.right(90)
mikey.forward(50)
mikey.pencolor("black")
mikey.forward(75)
mikey.right(90)
mikey.forward(50)
mikey.right(180)

mikey.forward(200)
mikey.left(90)
mikey.forward(200)
mikey.left(90)
mikey.forward(250)
mikey.right(90)
mikey.forward(50)
mikey.backward(300)

mikey.goto(0, 0)
mikey.forward(25)
mikey.left(90)
mikey.penup()
mikey.forward(25)
mikey.pendown()
mikey.circle(25)

mikey.penup()
mikey.forward(75)
mikey.right(90)
mikey.forward(25)
mikey.left(90)
mikey.pendown()
mikey.circle(50)

mikey.hideturtle()


window.exitonclick()
