import turtle
import math

# ==========================
# Glowing Yin-Yang Symbol
# ==========================

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Glowing Yin-Yang")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)

R = 180

# Draw Yin-Yang
t.pensize(3)

# Outer border
t.penup()
t.goto(0, -R)
t.setheading(0)
t.pendown()

t.color("white")
t.circle(R)

# Black half
t.penup()
t.goto(0, -R)
t.setheading(0)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(R, 180)
t.circle(R / 2, 180)
t.circle(-R / 2, 180)
t.end_fill()

# White half
t.fillcolor("white")
t.begin_fill()
t.circle(R, -180)
t.circle(-R / 2, -180)
t.circle(R / 2, -180)
t.end_fill()

# Top black circle
t.penup()
t.goto(0, R / 2 - R / 6)
t.setheading(0)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(R / 2)
t.end_fill()

# Bottom white circle
t.penup()
t.goto(0, -R / 2 - R / 6)
t.setheading(0)
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.circle(R / 2)
t.end_fill()

# Small white dot
t.penup()
t.goto(0, R / 2 + 30)
t.dot(40, "white")

# Small black dot
t.penup()
t.goto(0, -R / 2 + 30)
t.dot(40, "black")

# ==========================
# Neon Spiral Aura
# ==========================

colors = [
    "cyan",
    "deepskyblue",
    "dodgerblue",
    "blue",
    "mediumpurple"
]

for i in range(320):
    angle = i * 8
    radius = 220 + i * 0.4

    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    t.penup()
    t.goto(x, y)
    t.dot(3, colors[i % len(colors)])

# ==========================
# Outer Glow Ring
# ==========================

for r in range(195, 215, 4):
    t.penup()
    t.goto(0, -r)
    t.pendown()
    t.pencolor("cyan")
    t.pensize(1)
    t.circle(r)

screen.update()
screen.mainloop()