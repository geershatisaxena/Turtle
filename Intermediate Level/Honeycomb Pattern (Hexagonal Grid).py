import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Function to draw a hexagon
def draw_hexagon(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(size)
        t.left(60)
    t.end_fill()

# Draw honeycomb pattern
hex_size = 30
rows = 8
cols = 8
colors = ["gold", "orange", "yellow", "darkorange"]

for row in range(rows):
    for col in range(cols):
        # Calculate position
        x = col * hex_size * 1.5 - 200
        y = row * hex_size * 1.732 - 150
        
        # Offset every other row
        if row % 2 == 1:
            x += hex_size * 0.75
        
        # Color based on position
        color = colors[(row + col) % len(colors)]
        draw_hexagon(x, y, hex_size, color)

t.hideturtle()
turtle.done()