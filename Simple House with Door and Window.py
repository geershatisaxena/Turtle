import turtle

# Setup
t = turtle.Turtle()
t.speed(6)
t.pensize(3)

# Draw square base (house body)
t.fillcolor("lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# Draw triangle roof
t.fillcolor("red")
t.begin_fill()
t.left(45)
t.forward(106)
t.left(90)
t.forward(106)
t.end_fill()

# Draw door (rectangle)
t.penup()
t.goto(60, -150)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.left(135)  # Reset orientation
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.forward(40)
t.end_fill()

# Draw window (square)
t.penup()
t.goto(20, -80)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
for _ in range(4):
    t.forward(35)
    t.left(90)
t.end_fill()

# Draw window cross
t.penup()
t.goto(37.5, -80)
t.pendown()
t.forward(35)
t.penup()
t.goto(20, -62.5)
t.pendown()
t.left(90)
t.forward(35)

t.hideturtle()
turtle.done()