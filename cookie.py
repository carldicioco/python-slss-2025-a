# Drawing and Loops
# Author: Ubial
# 14 October 2025

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles
mikey = turtle.Turtle()
# mikey.turtlesize(5)  # size
# mikey.color("orange") # colour
# mikey.pencolor("blue")
# mikey.shape("turtle")
# mikey.speed(2)
# mikey.width(5)
# mikey.penup()
# mikey.forward(500)
# mikey.left(90)
# mikey.pendown()
# mikey.forward(500)

# mikey.goto(0, 0) # return to the middle
# mikey.circle(50)
# mikey.hideturtle()

mikey.color("lightblue")
mikey.pencolor("lightblue")
mikey.fillcolor("lightblue")
mikey.width(5)

# Snowman
# mikey.begin_fill()
# mikey.circle(100)
# mikey.end_fill()
# mikey.penup()
# mikey.goto(0, 200)
# mikey.pd()
# mikey.begin_fill()
# mikey.circle(80)
# mikey.end_fill()
# mikey.penup()
# mikey.goto(0, 360)
# mikey.pd()
# mikey.begin_fill()
# mikey.circle(60)
# mikey.end_fill()

# MAKE 100 COOKIES
for counter in range(100):
    counter = counter * 50
    # Make sure that turtle is pointing east
    mikey.setheading(0)
    # change the cookie colour
    mikey.color("brown")
    # draw a circle
    mikey.pu()
    mikey.goto(-5 + counter, -30 + counter)
    mikey.pd()
    mikey.circle(30)

    # put a chocolate chip on the top left side
    mikey.pu()
    mikey.goto(-10 + counter, 10 + counter)
    mikey.stamp()

    # chocolate chip on the top right
    mikey.goto(10 + counter, 10 + counter)
    mikey.stamp()

    # choco chip on the bottom right
    mikey.goto(10 + counter, -10 + counter)
    mikey.stamp()

    # ch chip on the bottom left
    mikey.goto(-10 + counter, -10 + counter)
    mikey.stamp()

    # ch chip in the middle
    mikey.goto(0 + counter, 0 + counter)
    mikey.stamp()


window.exitonclick()
