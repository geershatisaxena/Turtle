import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("navy")
t.pensize(4)

# Star parameters
side_length = 220
center_x, center_y = 0, 0

# Calculate points for detailed star
def calculate_star_points(radius, center_x, center_y):
    points = []
    for i in range(10):  # 10 points for a 5-point star (inner and outer)
        angle = math.radians(90 - i * 36)  # Start from top
        if i % 2 == 0:
            r = radius  # Outer points
        else:
            r = radius / 2.3  # Inner points
        x = center_x + r * math.cos(angle)
        y = center_y + r * math.sin(angle)
        points.append((x, y))
    return points

# Draw star outline
points = calculate_star_points(200, 0, 0)

t.penup()
t.goto(points[0])
t.pendown()

t.fillcolor("red")
t.begin_fill()
for point in points[1:]:
    t.goto(point)
t.goto(points[0])
t.end_fill()

# Add gold outline
t.pencolor("gold")
t.pensize(5)
t.penup()
t.goto(points[0])
t.pendown()
for point in points[1:]:
    t.goto(point)
t.goto(points[0])

# Draw inner pentagon
inner_points = points[1::2]  # Every other point (inner vertices)
t.pencolor("white")
t.pensize(3)
t.penup()
t.goto(inner_points[0])
t.pendown()
for point in inner_points[1:]:
    t.goto(point)
t.goto(inner_points[0])

# Draw lines from center to outer points (rays)
t.pencolor("cyan")
t.pensize(2)
for i in range(0, 10, 2):
    t.penup()
    t.goto(center_x, center_y)
    t.pendown()
    t.goto(points[i])

# Add center dot
t.penup()
t.goto(center_x, center_y)
t.dot(20, "yellow")
t.dot(10, "orange")

# Add vertex labels
t.pencolor("white")
t.pensize(1)
for i, point in enumerate(points[::2]):  # Only outer points
    t.penup()
    t.goto(point[0] + 15, point[1] + 10)
    t.write(f"Point {i+1}", font=("Arial", 10, "bold"))

# Add measurements
t.penup()
t.goto(-300, 250)
t.pencolor("yellow")
t.write("FIVE-POINT STAR", font=("Arial", 22, "bold"))

t.goto(-300, 210)
t.write(f"Outer Radius: 200 pixels", font=("Arial", 14, "bold"))

t.goto(-300, 180)
t.write(f"Side Length: {side_length} pixels", font=("Arial", 14, "bold"))

t.goto(-300, 150)
t.write("Internal Angle: 36°", font=("Arial", 14, "bold"))

t.goto(-300, 120)
t.write("Turn Angle: 144°", font=("Arial", 14, "bold"))

# Add angle markers
t.penup()
t.goto(80, 180)
t.write("36°", font=("Arial", 12, "bold"))
t.goto(-120, 80)
t.write("144°", font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()