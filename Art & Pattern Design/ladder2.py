import turtle
import math

# =========================
# Floating 3D Ladder Illusion
# =========================

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Floating 3D Ladder Illusion")
screen.setup(900, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)

# Draw a quadrilateral
def quad(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for p in points[1:]:
        t.goto(p)

    t.goto(points[0])
    t.end_fill()

# Perspective ladder
rails = []

# Left rail
for y in range(-250, 251, 10):
    scale = (y + 300) / 600
    x = -200 + scale * 120
    rails.append((x, y))

# Right rail
rails2 = []
for y in range(-250, 251, 10):
    scale = (y + 300) / 600
    x = 200 - scale * 120
    rails2.append((x, y))

# Draw glowing rails
t.pensize(5)
t.pencolor("cyan")

t.penup()
t.goto(rails[0])
t.pendown()
for p in rails:
    t.goto(p)

t.penup()
t.goto(rails2[0])
t.pendown()
for p in rails2:
    t.goto(p)

# Draw 3D rungs
for y in range(-220, 240, 35):

    scale = (y + 300) / 600

    left = -200 + scale * 120
    right = 200 - scale * 120

    depth = 20

    top = [
        (left, y),
        (right, y),
        (right + depth, y + depth),
        (left + depth, y + depth)
    ]

    side = [
        (right, y),
        (right + depth, y + depth),
        (right + depth, y - 10 + depth),
        (right, y - 10)
    ]

    front = [
        (left, y),
        (right, y),
        (right, y - 10),
        (left, y - 10)
    ]

    quad(front, "#666666")
    quad(side, "#444444")
    quad(top, "#FFD700")

# Floating glow particles
for angle in range(0, 360, 12):
    r = 280
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))

    t.penup()
    t.goto(x, y)
    t.dot(4, "deepskyblue")

screen.update()
screen.mainloop()