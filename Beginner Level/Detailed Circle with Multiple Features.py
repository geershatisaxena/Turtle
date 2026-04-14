import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("lightgray")
t.pensize(3)

# BIG circle dimensions
radius = 200

# Position
t.penup()
t.goto(0, -radius)
t.pendown()

# Draw filled circle
t.fillcolor("crimson")
t.begin_fill()
t.circle(radius)
t.end_fill()

# Draw white outline
t.pencolor("white")
t.pensize(6)
t.circle(radius)

# Draw inner circles (rings)
t.pencolor("gold")
t.pensize(4)
t.penup()
t.goto(0, -radius + 30)
t.pendown()
t.circle(radius - 30)

t.pencolor("silver")
t.pensize(3)
t.penup()
t.goto(0, -radius + 60)
t.pendown()
t.circle(radius - 60)

# Draw center point
t.penup()
t.goto(0, 0)
t.pendown()
t.dot(25, "gold")
t.dot(15, "white")

# Add radius lines (spokes)
t.pencolor("white")
t.pensize(2)
for angle in range(0, 360, 45):  # Every 45 degrees
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(radius)
    t.dot(8, "yellow")

# Draw radius label
t.penup()
t.goto(100, 100)
t.pencolor("black")
t.write(f"Radius: {radius} pixels", font=("Arial", 14, "bold"))

# Draw diameter label
t.penup()
t.goto(100, 70)
t.write(f"Diameter: {radius * 2} pixels", font=("Arial", 14, "bold"))

# Draw circumference label
t.penup()
t.goto(100, 40)
t.write(f"Circumference: {int(2 * 3.14159 * radius)} pixels", font=("Arial", 14, "bold"))

# Add title
t.penup()
t.goto(0, 250)
t.pencolor("darkblue")
t.write("BIG CIRCLE", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()