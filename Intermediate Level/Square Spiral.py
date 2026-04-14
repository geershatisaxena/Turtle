import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
t.pensize(2)
turtle.bgcolor("black")

# Draw square spiral
length = 1
for i in range(153):
    t.pencolor("cyan")
    t.forward(length)
    t.left(90)
    length += 5  # Increase length each time

t.hideturtle()
turtle.done()