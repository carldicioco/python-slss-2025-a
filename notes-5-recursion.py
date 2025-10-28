# Recursion
# Author: Carl Dicioco
# 20 October

import turtle

wn = turtle.Screen()
t = turtle.Turtle()

# Dictionary to hold colours
LEAF_COLOURS = {
    "mimi": "#eccbd9",
    "alice": "#e1eff6",
    "lightsky": "#97d2fb",
    "jordy": "#83bcff",
}


def draw_complicated_tree(level: int, branch_length: float):
    """Draw a recursive tree with more than 2 branches per level."""
    if level == 0:
        # Draw a leaf`                                                                                                                `
        t.color(LEAF_COLOURS["mimi"])
        t.stamp()
        t.color("brown")
    else:
        t.forward(branch_length)

        # First branch (left)
        t.left(40)
        draw_complicated_tree(level - 1, branch_length * 0.7)

        # Second branch (middle)
        t.right(30)  # back to center
        draw_complicated_tree(level - 1, branch_length * 0.7)

        # Third branch (right)
        t.right(40)
        draw_complicated_tree(level - 1, branch_length * 0.7)

        # Return to center orientation
        t.left(30)

        # Go back to where we started
        t.backward(branch_length)


# Set up the turtle
t.left(90)
t.speed(0.1)
t.color("brown")
t.pensize(3)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()

draw_complicated_tree(5, 100)

wn.exitonclick()
