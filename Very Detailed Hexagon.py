import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(4)

# Big hexagon dimensions
side_length = 200
radius = side_length  # For a regular hexagon, radius = side length

# Position to center
start_x = -side_length
start_y = 0

t.penup()
t.goto(start_x, start_y)
t.pendown()

# Draw filled hexagon
t.fillcolor("darkorange")
t.begin_fill()

for _ in range(6):
    t.forward(side_length)
    t.left(60)

t.end_fill()

# Gold outline
t.pencolor("gold")
t.pensize(5)
for _ in range(6):
    t.forward(side_length)
    t.left(60)

# Draw inner hexagon
t.pencolor("white")
t.pensize(3)
t.penup()
t.goto(start_x + 30, start_y)
t.pendown()
for _ in range(6):
    t.forward(side_length - 60)
    t.left(60)

# Draw smallest hexagon in center
t.pencolor("red")
t.pensize(2)
t.penup()
t.goto(start_x + 80, start_y)
t.pendown()
for _ in range(6):
    t.forward(side_length - 140)
    t.left(60)

# Draw diagonals (from center to vertices)
t.pencolor("cyan")
t.pensize(2)
center_x = 0
center_y = 0

for angle in range(0, 360, 60):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.penup()
    t.goto(center_x, center_y)
    t.pendown()
    t.goto(x, y)
    t.dot(10, "yellow")

# Draw lines connecting opposite vertices (3 main diagonals)
t.pencolor("lime")
t.pensize(3)
vertices = []
for angle in range(0, 360, 60):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    vertices.append((x, y))

# Connect opposite vertices
for i in range(3):
    t.penup()
    t.goto(vertices[i])
    t.pendown()
    t.goto(vertices[i + 3])

# Mark all vertices with dots
t.pencolor("white")
t.pensize(8)
for vertex in vertices:
    t.penup()
    t.goto(vertex)
    t.dot(15, "red")
    t.dot(8, "yellow")

# Add vertex labels
t.pencolor("white")
t.pensize(1)
labels = ['A', 'B', 'C', 'D', 'E', 'F']
for i, vertex in enumerate(vertices):
    t.penup()
    t.goto(vertex[0] + 15, vertex[1] + 10)
    t.write(f"Vertex {labels[i]}", font=("Arial", 12, "bold"))

# Add side labels
t.penup()
for i in range(6):
    # Midpoint of each side
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i+1) % 6]
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    t.goto(mid_x, mid_y + 15)
    t.write(f"{side_length}px", align="center", font=("Arial", 10, "bold"))

# Add angle labels (120° interior angles)
t.penup()
for i, vertex in enumerate(vertices):
    t.goto(vertex[0] - 25, vertex[1] - 15)
    t.write("120°", font=("Arial", 10, "bold"))

# Draw circumcircle (circle passing through all vertices)
t.pencolor("gray")
t.pensize(2)
t.penup()
t.goto(center_x, center_y - radius)
t.pendown()
t.circle(radius)

# Add measurements
t.penup()
t.goto(-300, 250)
t.pencolor("yellow")
t.write("REGULAR HEXAGON", font=("Arial", 22, "bold"))

t.goto(-300, 210)
t.write(f"Side Length: {side_length} pixels", font=("Arial", 14, "bold"))

t.goto(-300, 180)
t.write(f"Radius (circumcircle): {radius} pixels", font=("Arial", 14, "bold"))

t.goto(-300, 150)
t.write(f"Perimeter: {side_length * 6} pixels", font=("Arial", 14, "bold"))

t.goto(-300, 120)
t.write(f"Interior Angle: 120°", font=("Arial", 14, "bold"))

t.goto(-300, 90)
t.write(f"Exterior Angle: 60°", font=("Arial", 14, "bold"))

# Calculate area
area = (3 * math.sqrt(3) * side_length ** 2) / 2
t.goto(-300, 60)
t.write(f"Area ≈ {int(area)} sq pixels", font=("Arial", 14, "bold"))

# Add central angles
t.penup()
t.goto(center_x + 20, center_y + 20)
t.write("60°", font=("Arial", 12, "bold"))

# Add title at top
t.goto(0, 320)
t.pencolor("orange")
t.write("COMPLETE HEXAGON GEOMETRY", align="center", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()