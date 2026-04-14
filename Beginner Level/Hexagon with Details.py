import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("lightblue")
t.pensize(4)

# Big hexagon dimensions
side_length = 180

# Position to center
t.penup()
t.goto(-side_length, 0)
t.pendown()

# Draw filled hexagon
t.fillcolor("purple")
t.begin_fill()

for _ in range(6):
    t.forward(side_length)
    t.left(60)

t.end_fill()

# Outline
t.pencolor("gold")
t.pensize(6)
for _ in range(6):
    t.forward(side_length)
    t.left(60)

t.hideturtle()
turtle.done()