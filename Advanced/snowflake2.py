import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(1)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Geometric Snowflake")

hue = 0.0

def draw_hexagon(size):
    """Draw a hexagon (basic ice crystal shape)"""
    t.pendown()
    for _ in range(6):
        t.forward(size)
        t.left(60)
    t.penup()

def draw_small_star(size):
    """Draw a small starburst pattern"""
    t.pendown()
    for _ in range(6):
        t.forward(size)
        t.backward(size)
        t.left(60)
    t.penup()

def draw_branch(depth, length, shrink):
    """Recursive branch drawing for fractal-like snowflake"""
    if depth == 0:
        return
    
    t.forward(length)
    
    # Draw side crystals
    for angle in [30, -30, 60, -60]:
        t.left(angle)
        draw_small_star(length * 0.3)
        draw_hexagon(length * 0.2)
        draw_branch(depth - 1, length * shrink, shrink)
        t.right(angle)
    
    t.backward(length)

def draw_snowflake():
    """Draw complete snowflake with 6-fold symmetry"""
    for i in range(6):
        rgb = colorsys.hsv_to_rgb((hue + i * 0.05) % 1.0, 1.0, 1.0)
        t.pencolor(rgb)
        
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 60)
        t.pendown()
        
        # Main branch
        t.forward(80)
        draw_hexagon(25)
        draw_small_star(15)
        draw_branch(2, 50, 0.6)
        
        t.penup()
        t.goto(0, 0)

# Animation loop
while True:
    t.clear()
    
    # Center hexagon
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(rgb)
    t.penup()
    t.goto(0, -30)
    t.setheading(0)
    draw_hexagon(30)
    
    # Draw snowflake arms
    draw_snowflake()
    
    turtle.update()
    hue += 0.008
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()