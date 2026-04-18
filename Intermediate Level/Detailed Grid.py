import turtle
import time

# Setup
turtle.speed(0)
turtle.tracer(0)  # We'll manually update for animation effect
turtle.penup()
turtle.goto(-280, 280)
turtle.pendown()

# Settings
board_size = 400
rows = 8
cols = 8
cell_size = board_size / rows
border_margin = 30

# Colors
dark_color = "#B58863"   # Wood brown
light_color = "#F0D9B5"  # Light cream
border_color = "#2C2C2C"
text_color = "#333333"

# --- Draw border frame (animated) ---
turtle.penup()
turtle.goto(-280 - border_margin//2, 280 + border_margin//2)
turtle.pendown()
turtle.color(border_color)
turtle.pensize(3)

for side in range(4):
    for step in range(20):  # Animate each side in small steps
        turtle.forward((board_size + border_margin) / 20)
        turtle.update()
        time.sleep(0.01)
    turtle.right(90)
turtle.pensize(1)

# --- Function to draw a single square with animation ---
def draw_square_animated(x, y, fill_color, delay=0.05):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    
    # Draw 4 sides with animation
    for side in range(4):
        for step in range(10):  # Each side drawn in 10 steps
            turtle.forward(cell_size / 10)
            turtle.update()
            time.sleep(delay / 10)
        turtle.right(90)
    
    turtle.end_fill()
    turtle.update()
    time.sleep(delay)

# --- Draw chessboard squares (animated row by row) ---
turtle.speed(0)
turtle.tracer(0)

for row in range(rows):
    # Animate moving to start of row
    turtle.penup()
    turtle.goto(-280, 280 - row * cell_size)
    turtle.pendown()
    turtle.update()
    time.sleep(0.1)
    
    for col in range(cols):
        x = -280 + col * cell_size
        y = 280 - row * cell_size
        if (row + col) % 2 == 0:
            fill = light_color
        else:
            fill = dark_color
        draw_square_animated(x, y, fill, delay=0.03)
    
    # Small pause between rows
    time.sleep(0.2)

# --- Draw thin grid lines (animated) ---
turtle.penup()
turtle.color("#666666")
turtle.pensize(1)

for i in range(rows + 1):
    # Horizontal line
    turtle.penup()
    turtle.goto(-280, 280 - i * cell_size)
    turtle.pendown()
    for step in range(20):
        turtle.forward(board_size / 20)
        turtle.update()
        time.sleep(0.005)
    
    # Vertical line
    turtle.penup()
    turtle.goto(-280 + i * cell_size, 280)
    turtle.pendown()
    for step in range(20):
        turtle.goto(-280 + i * cell_size, 280 - (step + 1) * (board_size / 20))
        turtle.update()
        time.sleep(0.005)
    
    turtle.update()

# --- Animate row labels (1-8) ---
turtle.penup()
turtle.color(text_color)
turtle.setheading(0)

for row in range(rows):
    label = str(8 - row)
    x = -280 - border_margin//2 - 12
    y = 280 - row * cell_size + cell_size//2 - 8
    turtle.goto(x, y)
    # Animate the number appearing (scale effect)
    for size in range(5, 13, 2):
        turtle.clear()
        turtle.write(label, font=("Arial", size, "bold"))
        turtle.update()
        time.sleep(0.02)
    turtle.write(label, font=("Arial", 12, "bold"))
    turtle.update()
    time.sleep(0.1)

# --- Animate column labels (a-h) ---
for col in range(cols):
    label = chr(ord('a') + col)
    x = -280 + col * cell_size + cell_size//2 - 6
    y = 280 + border_margin//2 - 28
    turtle.goto(x, y)
    for size in range(5, 13, 2):
        turtle.clear()
        turtle.write(label, font=("Arial", size, "bold"))
        turtle.update()
        time.sleep(0.02)
    turtle.write(label, font=("Arial", 12, "bold"))
    turtle.update()
    time.sleep(0.1)

# --- Animate title ---
turtle.penup()
turtle.goto(0, 280 + border_margin//2 + 20)
turtle.color(border_color)
for size in range(8, 18, 2):
    turtle.clear()
    turtle.write("CHESSBOARD", align="center", font=("Arial", size, "bold"))
    turtle.update()
    time.sleep(0.03)
turtle.write("CHESSBOARD", align="center", font=("Arial", 16, "bold"))
turtle.update()

# --- Optional: Animate a knight moving across the board at the end ---
time.sleep(1)
turtle.penup()
turtle.color("red")
turtle.shape("turtle")
turtle.turtlesize(1.5)

# Knight move pattern: visit a few squares
positions = [(0,0), (2,1), (4,2), (6,3), (5,5), (3,6), (1,5), (0,3)]
for col, row in positions:
    x = -280 + col * cell_size + cell_size//2
    y = 280 - row * cell_size - cell_size//2
    turtle.goto(x, y)
    turtle.stamp()
    turtle.update()
    time.sleep(0.4)

# --- Finish ---
turtle.hideturtle()
turtle.update()
turtle.done()