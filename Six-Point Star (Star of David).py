import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("lightblue")
t.pensize(4)

# Big six-point star
side_length = 200

# Draw first triangle
t.fillcolor("red")
t.begin_fill()
for _ in range(3):
    t.forward(side_length)
    t.left(120)
t.end_fill()

# Move to draw second triangle
t.penup()
t.goto(0, 0)
t.left(60)
t.pendown()

# Draw second triangle (inverted)
t.fillcolor("blue")
t.begin_fill()
for _ in range(3):
    t.forward(side_length)
    t.right(120)
t.end_fill()

# Add outline
t.pencolor("gold")
t.pensize(6)
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()
for _ in range(3):
    t.forward(side_length)
    t.left(120)

t.penup()
t.goto(0, 0)
t.left(60)
t.pendown()
for _ in range(3):
    t.forward(side_length)
    t.right(120)

t.hideturtle()
turtle.done()