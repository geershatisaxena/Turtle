import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("skyblue")
t.pensize(2)

# Draw white petals
num_petals = 16
for i in range(num_petals):
    t.fillcolor("white")
    t.begin_fill()
    
    # Draw petal
    t.circle(70, 60)
    t.left(120)
    t.circle(70, 60)
    t.left(120)
    
    t.end_fill()
    t.left(360 / num_petals)

# Petal outlines
t.pencolor("lightgray")
t.pensize(1)
for i in range(num_petals):
    t.circle(70, 60)
    t.left(120)
    t.circle(70, 60)
    t.left(120)
    t.left(360 / num_petals)

# Center circle
t.penup()
t.goto(0, -25)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(25)
t.end_fill()

# Center texture
t.pencolor("darkgoldenrod")
t.pensize(2)
for i in range(12):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 30)
    t.forward(18)
    t.pendown()
    t.dot(5)

t.hideturtle()
turtle.done()