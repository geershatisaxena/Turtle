import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("white")
t.pensize(2)

# Square parameters
square_size = 100
spacing = 25
start_x = -350
start_y = -50

# Gradient colors (light to dark)
colors = [
    "#FFE5E5", "#FFB3B3", "#FF8080", "#FF4D4D", "#FF1A1A", "#CC0000",
    "#E5FFE5", "#B3FFB3", "#80FF80", "#4DFF4D", "#1AFF1A", "#00CC00"
]

# Function to draw square with shadow
def draw_square_with_shadow(x, y, size, color):
    # Draw shadow
    t.penup()
    t.goto(x + 8, y - 8)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    
    # Draw main square
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    
    # Add border
    t.pencolor("black")
    t.pensize(3)
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Draw 12 squares with gradient effect
for i in range(12):
    draw_square_with_shadow(
        start_x + i * (square_size + spacing),
        start_y,
        square_size,
        colors[i]
    )

# Add labels
t.penup()
for i in range(12):
    x = start_x + i * (square_size + spacing) + square_size/2
    t.goto(x, start_y - 30)
    t.pencolor("black")
    t.write(f"Square {i+1}", align="center", font=("Arial", 10, "bold"))

t.hideturtle()
turtle.done()