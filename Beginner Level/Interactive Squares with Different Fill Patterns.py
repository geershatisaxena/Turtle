import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("lightblue")
t.pensize(2)

# Square parameters
square_size = 100
spacing = 20
start_x = -350
start_y = -100

# Different patterns
patterns = ["Solid", "Horizontal\nLines", "Vertical\nLines", "Dots", "Checker", "Diagonal"]
colors = ["pink", "lightgreen", "lightblue", "yellow", "orange", "lavender"]

# Function to draw horizontal lines
def draw_horizontal_lines(x, y, size):
    t.penup()
    t.goto(x, y)
    for i in range(5):
        t.goto(x, y + i * (size/4))
        t.pendown()
        t.forward(size)
        t.penup()

# Function to draw vertical lines
def draw_vertical_lines(x, y, size):
    t.penup()
    t.goto(x, y)
    for i in range(5):
        t.goto(x + i * (size/4), y)
        t.pendown()
        t.goto(x + i * (size/4), y + size)
        t.penup()

# Function to draw dots
def draw_dots(x, y, size):
    t.penup()
    for i in range(4):
        for j in range(4):
            t.goto(x + (i + 0.5) * (size/4), y + (j + 0.5) * (size/4))
            t.dot(6, "white")

# Function to draw checker pattern
def draw_checker(x, y, size):
    cell_size = size / 4
    t.penup()
    for i in range(4):
        for j in range(4):
            if (i + j) % 2 == 0:
                t.goto(x + i * cell_size, y + j * cell_size)
                t.pendown()
                t.fillcolor("white")
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
                t.penup()

# Draw squares with different patterns
for i in range(6):
    x = start_x + i * (square_size + spacing)
    y = start_y
    
    # Draw base square
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(colors[i])
    t.begin_fill()
    for _ in range(4):
        t.forward(square_size)
        t.right(90)
    t.end_fill()
    
    # Add pattern
    t.pencolor("black")
    if i == 0:  # Solid - no extra pattern
        pass
    elif i == 1:  # Horizontal lines
        draw_horizontal_lines(x, y, square_size)
    elif i == 2:  # Vertical lines
        draw_vertical_lines(x, y, square_size)
    elif i == 3:  # Dots
        draw_dots(x, y, square_size)
    elif i == 4:  # Checker
        draw_checker(x, y, square_size)
    elif i == 5:  # Diagonal
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x + square_size, y + square_size)
        t.penup()
        t.goto(x + square_size, y)
        t.pendown()
        t.goto(x, y + square_size)
    
    # Add border
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("black")
    t.pensize(4)
    for _ in range(4):
        t.forward(square_size)
        t.right(90)
    
    # Add pattern label
    t.penup()
    t.goto(x + square_size/2, y - 25)
    t.write(patterns[i], align="center", font=("Arial", 10, "bold"))

# Title
t.penup()
t.goto(0, 200)
t.pencolor("darkblue")
t.write("SQUARES WITH DIFFERENT FILL PATTERNS", align="center", font=("Arial", 18, "bold"))

t.hideturtle()
turtle.done()