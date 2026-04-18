import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("white")
t.pensize(3)

# Draw rotating squares of different sizes
sizes = [180, 140, 100, 60, 20]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

for size in sizes:
    for i in range(24):
        t.pencolor(colors[i % len(colors)])
        t.fillcolor(colors[(i+3) % len(colors)])
        t.begin_fill()
        
        for _ in range(4):
            t.forward(size)
            t.left(90)
        
        t.end_fill()
        t.left(15)
    
    t.penup()
    t.goto(0, 0)
    t.pendown()

t.hideturtle()
turtle.done()