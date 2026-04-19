import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
turtle.bgcolor("lightblue")
t.pensize(3)

# Draw sun body
t.fillcolor("yellow")
t.begin_fill()
t.circle(80)
t.end_fill()

# Draw rays
t.pencolor("orange")
t.pensize(4)
for i in range(16):
    t.penup()
    t.goto(0, 80)
    t.setheading(i * 22.5)
    t.pendown()
    t.forward(45)
    t.backward(45)

# Draw eyes
t.penup()
t.goto(-30, 40)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.goto(30, 40)
t.pendown()
t.begin_fill()
t.circle(8)
t.end_fill()

# Draw smile
t.penup()
t.goto(-40, 10)
t.pendown()
t.pencolor("black")
t.pensize(3)
t.setheading(-60)
t.circle(45, 120)

# Draw rosy cheeks
t.penup()
t.goto(-50, 15)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(50, 15)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.hideturtle()
turtle.done()