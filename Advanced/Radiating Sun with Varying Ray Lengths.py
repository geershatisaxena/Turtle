import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("darkblue")
t.pensize(3)

# Draw sun body with gradient effect
t.fillcolor("orange")
t.begin_fill()
t.circle(80)
t.end_fill()

# Inner circle
t.penup()
t.goto(0, -60)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(60)
t.end_fill()

# Draw rays with alternating lengths
for i in range(24):
    angle = i * 15
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(80)
    t.pendown()
    
    # Alternate ray lengths
    if i % 2 == 0:
        ray_length = 50
        t.pencolor("orange")
    else:
        ray_length = 35
        t.pencolor("gold")
    
    t.pensize(4)
    t.forward(ray_length)
    t.backward(ray_length)

t.hideturtle()
turtle.done()