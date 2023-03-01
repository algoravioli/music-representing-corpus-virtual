import numpy as np
import turtle as t
import random as r

# Set up the screen
t.setup(800, 800)
t.bgcolor('black')
t.speed(0)
t.pensize(2)

# Define the colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white']

# Define the number of circles
n = 50

# Define the number of sides
sides = 5

# Define the angle
angle = 360 / sides

# Define the radius
radius = 200

# Define the step
step = 10

# Define the number of circles
for i in range(n):
    # Define the color
    t.color(r.choice(colors))

    # Define the number of sides
    for j in range(sides):
        t.forward(radius)
        t.left(angle)

    # Move to the next circle
    t.penup()
    t.forward(step)
    t.pendown()

    # Increase the radius
    radius += step

# Hide the turtle
t.hideturtle()

# Exit on click
t.exitonclick()
