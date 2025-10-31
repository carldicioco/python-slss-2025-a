# Turtle Artist
# Author:
# 28 October

import turtle

# A one-of-a-kind drawing

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(1)
t.color("tan")

# ---------- Bottom bun ----------
x, y = -150, -100
width, height = 300, 50
radius = 10

t.up()
t.goto(x + radius, y)
t.down()
t.begin_fill()

# Bottom line with rounded corners
t.forward(width - 2 * radius)
t.circle(radius, 90)
t.forward(height - 2 * radius)
t.circle(radius, 90)
t.forward(width - 2 * radius)
t.circle(radius, 90)
t.forward(height - 2 * radius)
t.circle(radius, 90)
t.end_fill()
t.up()

t.color("limegreen")
# size of each triangle
x_positions = [-150, -100, -50, 0, 50, 100]  # horizontal positions
y = 150  # same vertical position for all triangles

for x in x_positions:
    t.penup()
    t.goto(x, y)  # position each triangle
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(60)
    t.right(125)
    t.forward(50)
    t.right(125)
    t.forward(50)
    t.right(125)
    t.end_fill()
t.up()

# ---------- Top bun ----------
t.color("tan")
t.goto(-150, 150)
t.down()
t.begin_fill()
t.setheading(0)
t.forward(300)
t.left(90)
t.circle(150, 180)
t.end_fill()
t.up()

wn.exitonclick()
