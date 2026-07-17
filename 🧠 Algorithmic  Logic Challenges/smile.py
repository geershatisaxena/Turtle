import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Face
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# Left eye
t.penup()
t.goto(-40, 20)
t.pendown()
t.circle(15)

# Right eye
t.penup()
t.goto(40, 20)
t.pendown()
t.circle(15)

# Mouth
t.penup()
t.goto(-40, -20)
t.pendown()
t.right(90)
t.circle(40, 180)

turtle.done()