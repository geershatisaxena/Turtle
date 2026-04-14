import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flower Pattern using Circles")

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Color palette
colors = ["#FF6B6B", "#FF8E72", "#FFB347", "#FFD93D", "#6BCB77", "#4D96FF"]

def draw_circle_arc(radius, extent, direction="left"):
    """Draw a circle arc with given radius and extent (angle in degrees)."""
    if direction == "left":
        t.circle(radius, extent)
    else:
        t.circle(-radius, extent)

def petal(radius, angle):
    """Draw one petal as two intersecting circle arcs."""
    # First arc
    t.begin_fill()
    draw_circle_arc(radius, angle, "left")
    # Second arc to complete petal shape
    t.left(180 - angle)
    draw_circle_arc(radius, angle, "left")
    t.left(180 - angle)
    t.end_fill()

# Draw central flower
t.penup()
t.goto(0, -50)
t.pendown()

num_petals = 12
angle_step = 360 / num_petals
petal_radius = 120
petal_angle = 60  # arc extent for each half-petal

for i in range(num_petals):
    t.color(colors[i % len(colors)])
    petal(petal_radius, petal_angle)
    t.left(angle_step)

# Draw inner decorative circles
t.penup()
t.goto(0, -40)
t.pendown()
t.color("#FFB347")
t.width(3)
t.circle(40)

t.penup()
t.goto(0, -25)
t.pendown()
t.color("#FF6B6B")
t.width(2)
t.circle(25)

t.penup()
t.goto(0, -10)
t.pendown()
t.color("#FFD93D")
t.width(2)
t.circle(10)

# Draw outer ring of small circles (stamens style)
t.penup()
t.width(2)
outer_radius = 130
for i in range(24):
    angle = i * 15
    x = outer_radius * math.cos(math.radians(angle))
    y = outer_radius * math.sin(math.radians(angle))
    t.goto(x, y - 10)
    t.pendown()
    t.color(colors[i % len(colors)])
    t.circle(8)
    t.penup()

# Draw a subtle dotted circle around the flower
t.goto(0, -150)
t.pendown()
t.color("#4D96FF")
t.width(1)
for _ in range(72):
    t.forward(6.5)  # circumference ~ 150*2*pi / 72
    t.penup()
    t.forward(2)
    t.pendown()

t.hideturtle()
screen.mainloop()