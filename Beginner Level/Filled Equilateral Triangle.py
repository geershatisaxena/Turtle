import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(4)

# Set dimensions for BIG triangle
side_length = 350

# Position to center on screen
t.penup()
t.goto(-side_length/2, -150)
t.pendown()

# Draw filled equilateral triangle
t.fillcolor("forest green")
t.begin_fill()

for _ in range(3):
    t.forward(side_length)
    t.left(120)

t.end_fill()

# Add border outline
t.pencolor("gold")
t.pensize(5)
for _ in range(3):
    t.forward(side_length)
    t.left(120)

# Add vertex dots
t.penup()
t.pencolor("red")
t.pensize(8)

# Dot at each vertex
positions = [(0, 0), (side_length, 0), (side_length/2, 87)]  # Approximate height
for pos in positions:
    t.goto(pos)
    t.dot(15, "red")

# Add side length labels
t.pencolor("white")
t.pensize(2)
t.penup()

# Label bottom side
t.goto(side_length/2, -30)
t.write(f"Side: {side_length}px", align="center", font=("Arial", 14, "bold"))

# Label height
t.goto(side_length + 30, 40)
t.write(f"Height: {int(side_length * 0.866)}px", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()