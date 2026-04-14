import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw circular spiral
for i in range(800):
    t.pencolor("crimson")
    t.circle(i * 0.5, 45)  # Increasing radius arcs

t.hideturtle()
turtle.done()