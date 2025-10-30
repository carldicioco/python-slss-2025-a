import turtle

wn = turtle.Screen()
t = turtle.Turtle()

mikey = turtle.Turtle()
mikey.turtlesize(0.5)  # size
mikey.color("white")  # colour
mikey.shape("turtle")
mikey.speed(0.5)
mikey.width(5)
mikey.penup()
mikey.left(90)
mikey.pendown()

wn.exitonclick()
