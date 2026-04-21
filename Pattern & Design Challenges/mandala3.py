import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Geometric Mandala")

num_points = 12
radius = 180
hue = 0.0
rotation = 0

def draw_triangle(x, y, size, color_hue):
    """Draw a triangle at given position"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.8)
    t.fillcolor(rgb)
    t.begin_fill()
    
    for _ in range(3):
        t.forward(size)
        t.left(120)
    
    t.end_fill()

def draw_diamond(x, y, width, height, color_hue):
    """Draw a diamond shape"""
    t.penup()
    t.goto(x, y - height/2)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
    t.fillcolor(rgb)
    t.begin_fill()
    
    t.goto(x + width/2, y)
    t.goto(x, y + height/2)
    t.goto(x - width/2, y)
    t.goto(x, y - height/2)
    
    t.end_fill()

while True:
    t.clear()
    
    # Draw outer ring of triangles
    for i in range(num_points):
        angle = i * (360 / num_points) + rotation
        rad = math.radians(angle)
        x = math.cos(rad) * radius
        y = math.sin(rad) * radius
        color_hue = (hue + i * 0.03) % 1.0
        draw_triangle(x, y, 25, color_hue)
    
    # Draw middle ring of diamonds
    for i in range(num_points * 2):
        angle = i * (360 / (num_points * 2)) + rotation
        rad = math.radians(angle)
        x = math.cos(rad) * (radius * 0.6)
        y = math.sin(rad) * (radius * 0.6)
        color_hue = (hue + 0.2 + i * 0.02) % 1.0
        draw_diamond(x, y, 20, 30, color_hue)
    
    # Draw inner circle
    t.penup()
    t.goto(0, -radius * 0.3)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.6) % 1.0, 1.0, 0.7)
    t.pencolor(rgb)
    t.width(3)
    t.circle(radius * 0.3)
    
    # Draw center dot
    t.penup()
    t.goto(0, -8)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.8) % 1.0, 1.0, 1.0)
    t.fillcolor(rgb)
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    
    turtle.update()
    
    rotation += 0.8
    hue += 0.003
    
    if rotation >= 360:
        rotation -= 360
    if hue > 1.0:
        hue -= 1.0

turtle.done()