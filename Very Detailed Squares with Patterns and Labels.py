import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("lightgray")
t.pensize(3)

# Square parameters
square_size = 120
spacing = 40
start_x = -400
start_y = -100

# Colors and patterns
colors = ["crimson", "forest green", "royal blue", "gold", "purple", "orange"]
patterns = ["Solid", "Striped", "Dotted", "Solid", "Striped", "Dotted"]
numbers = ["1st", "2nd", "3rd", "4th", "5th", "6th"]

# Function to draw a filled square
def draw_filled_square(x, y, size, color, label):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw filled square
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    
    # Add border outline
    t.pencolor("black")
    t.pensize(4)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    
    # Add diagonal lines inside (X pattern)
    t.pencolor("white")
    t.pensize(2)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + size, y + size)
    
    t.penup()
    t.goto(x + size, y)
    t.pendown()
    t.goto(x, y + size)
    
    # Add label
    t.penup()
    t.goto(x + size/2, y - 25)
    t.pencolor("black")
    t.write(f"{label}\nSquare", align="center", font=("Arial", 12, "bold"))
    
    # Add size label
    t.goto(x + size/2, y + size + 15)
    t.write(f"{size}px", align="center", font=("Arial", 10, "normal"))

# Draw all squares
for i in range(6):
    draw_filled_square(
        start_x + i * (square_size + spacing),
        start_y,
        square_size,
        colors[i],
        numbers[i]
    )

# Add title
t.penup()
t.goto(0, 200)
t.pencolor("darkblue")
t.write("MULTIPLE SQUARES IN A ROW", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()