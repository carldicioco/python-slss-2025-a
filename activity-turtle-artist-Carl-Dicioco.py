# Turtle Artist
# Author: Carl Dicioco
# 28 October
import turtle
import random

# A one-of-a-kind drawing
wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.speed(40)
x, y = -150, -90


# ----FUNCTIONS----
# Flat buns function
def flatbun():
    t.color("burlywood3")
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


# Top bun function
def topbun():
    t.color("burlywood3")
    t.goto(-150, 100)
    t.down()
    t.begin_fill()
    t.setheading(0)
    t.forward(300)
    t.left(90)
    t.circle(150, 180)
    t.end_fill()
    t.up()


# Sesame seed function
def sesame_seeds():
    t.color("ivory")
    for _ in range(25):
        x = random.randint(-120, 120)
        y = random.randint(145, 200)
        t.up()
        t.goto(x, y)
        t.setheading(random.randint(0, 360))
        t.down()
        t.begin_fill()
        for _ in range(2):
            t.circle(4, 90)
            t.circle(2, 90)
        t.end_fill()
        t.up()


# Meat function
def meat():
    width, height = 260, 40
    radius = 10
    t.color("#492C1D")
    t.setheading(270)
    t.up()
    t.goto(x + radius, y)
    t.left(90)
    t.down()
    t.begin_fill()
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


# Big mac sauce function
def bigmacsauce():
    x_positions1 = [-150, -90, -30, 30, 90]
    y = 60
    for x in x_positions1:
        t.up()
        t.goto(x, y)
        t.setheading(270)
        t.color("khaki")
        t.down()
        t.begin_fill()
        t.circle(30, 180)
        t.end_fill()


# Lettuce function
def lettuce():
    t.color("olivedrab3")
    for _ in range(8):
        x = random.randint(-130, 130)
        t.penup()
        t.goto(x, y)  # position each triangle
        t.pendown()
        t.begin_fill()
        t.setheading(0)
        t.forward(25)
        t.right(120)
        t.forward(25)
        t.right(120)
        t.forward(25)
        t.right(120)
        t.end_fill()
    t.up()


# Cheese function
def cheese():
    t.goto(-130, -28)
    t.setheading(210)
    t.color("gold")
    t.down()
    t.begin_fill()
    t.forward(40)
    t.setheading(3)
    t.forward(160)
    t.setheading(-3)
    t.forward(165)
    t.setheading(150)
    t.forward(40)
    t.end_fill()
    t.up()


# Onions function
def onions():
    for _ in range(11):
        x = random.randint(-130, 130)
        t.up()
        t.goto(x, y)
        t.setheading(random.randint(0, 360))
        t.color("papayawhip")
        t.down()
        t.begin_fill()
        for _ in range(4):
            t.forward(6)
            t.setheading(t.heading() + 90)
        t.end_fill()
        t.up()


# ----EXECUTIONS----
# Flat bun
flatbun()
x, y = -150, 10
flatbun()
# Top bun
t.goto(-150, 100)
topbun()
# sesame seeds
sesame_seeds()
# Meat
x, y = -130, 60
meat()
x, y = -130, -30
meat()
# Big Mac Sauce
bigmacsauce()
# Lettuce
y = 60
lettuce()
y = -41
lettuce()
# Cheese
cheese()
# Onions
y = 85
onions()
y = 0
onions()

wn.exitonclick()
