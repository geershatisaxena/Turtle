import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# Square parameters
square_size = 110
spacing = 30
start_x = -400
start_y = -80

# Rainbow colors
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to draw square with inner circle
def draw_square_with_circle(x, y, size, color):
    # Draw outer square
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    
    # Draw white border
    t.pencolor("white")
    t.pensize(4)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    
    # Draw inner circle
    t.pencolor("gold")
    t.pensize(3)
    t.penup()
    t.goto(x + size/2, y + size/2 - size/3)
    t.pendown()
    t.circle(size/3)
    
    # Draw center dot
    t.penup()
    t.goto(x + size/2, y + size/2)
    t.dot(12, "white")

# Draw squares
for i in range(7):
    draw_square_with_circle(
        start_x + i * (square_size + spacing),
        start_y,
        square_size,
        rainbow[i]
    )
    
    # Add number label
    t.penup()
    t.goto(start_x + i * (square_size + spacing) + square_size/2, start_y - 30)
    t.pencolor("white")
    t.write(f"#{i+1}", align="center", font=("Arial", 14, "bold"))

# Title
t.penup()
t.goto(0, 200)
t.pencolor("cyan")
t.write("RAINBOW SQUARES IN A ROW", align="center", font=("Arial", 22, "bold"))

t.hideturtle()
turtle.done()