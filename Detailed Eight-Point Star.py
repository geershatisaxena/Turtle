import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# Star parameters
outer_radius = 200
inner_radius = 80
points = 8

# Calculate star points
star_points = []
for i in range(points * 2):
    angle = math.radians(90 - i * (360 / (points * 2)))
    if i % 2 == 0:
        r = outer_radius
    else:
        r = inner_radius
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    star_points.append((x, y))

# Draw filled star
t.fillcolor("purple")
t.begin_fill()
t.penup()
t.goto(star_points[0])
t.pendown()
for point in star_points[1:]:
    t.goto(point)
t.goto(star_points[0])
t.end_fill()

# Add gold outline
t.pencolor("gold")
t.pensize(5)
t.penup()
t.goto(star_points[0])
t.pendown()
for point in star_points[1:]:
    t.goto(point)
t.goto(star_points[0])

# Draw inner octagon
inner_points = star_points[1::2]
t.pencolor("cyan")
t.pensize(3)
t.penup()
t.goto(inner_points[0])
t.pendown()
for point in inner_points[1:]:
    t.goto(point)
t.goto(inner_points[0])

# Draw rays from center
t.pencolor("white")
t.pensize(2)
for i in range(0, len(star_points), 2):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(star_points[i])

# Center decoration
t.penup()
t.goto(0, 0)
t.dot(25, "yellow")
t.dot(12, "orange")

# Labels
t.penup()
t.goto(-300, 280)
t.pencolor("white")
t.write("EIGHT-POINT STAR", font=("Arial", 24, "bold"))

t.goto(-300, 240)
t.write(f"Outer Radius: {outer_radius}px", font=("Arial", 14, "bold"))

t.goto(-300, 210)
t.write(f"Inner Radius: {inner_radius}px", font=("Arial", 14, "bold"))

t.goto(-300, 180)
t.write(f"Points: {points}", font=("Arial", 14, "bold"))

t.goto(-300, 150)
t.write("Angle between points: 45°", font=("Arial", 14, "bold"))

t.hideturtle()
turtle.done()