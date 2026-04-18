import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(3)

# Draw two interlocking rotating square patterns
colors1 = ["red", "orange", "yellow"]
colors2 = ["blue", "green", "purple"]

# First set of squares
for i in range(36):
    t.pencolor(colors1[i % len(colors1)])
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.left(10)

# Second set (smaller, rotated differently)
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(36):
    t.pencolor(colors2[i % len(colors2)])
    for _ in range(4):
        t.forward(70)
        t.left(90)
    t.left(15)

t.hideturtle()
turtle.done()