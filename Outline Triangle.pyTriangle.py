import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(6)

# Make triangle BIG
side_length = 400

# Position to center
t.penup()
t.goto(-200, -150)
t.pendown()

# Draw each side with different color
colors = ["red", "blue", "green"]
sides = ["Side 1", "Side 2", "Side 3"]

for i in range(3):
    t.pencolor(colors[i])
    t.forward(side_length)
    
    # Add label on each side
    t.penup()
    t.forward(30)
    t.write(f"{sides[i]}", font=("Arial", 12, "bold"))
    t.backward(30)
    t.pendown()
    
    t.left(120)

# Add vertex markers
t.penup()
t.pencolor("purple")
t.pensize(10)

# Calculate vertex positions
vertices = [
    (-200, -150),                           # Bottom-left
    (200, -150),                            # Bottom-right
    (0, 200)                                # Top
]

for i, vertex in enumerate(vertices):
    t.goto(vertex)
    t.dot(20, "purple")
    t.write(f"  Vertex {i+1}", font=("Arial", 12, "bold"))

# Add angle labels
t.penup()
t.goto(-120, -100)
t.write("60°", font=("Arial", 14, "bold"))
t.goto(100, -100)
t.write("60°", font=("Arial", 14, "bold"))
t.goto(0, 140)
t.write("60°", font=("Arial", 14, "bold"))

# Add title
t.goto(0, 280)
t.pencolor("black")
t.write("EQUILATERAL TRIANGLE", align="center", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()