import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)  # Smooth animation

# Star polygon settings
points = 9           # Number of points (odd numbers give star shapes)
radius = 180
angle = 360 / points

hue = 0.0
rotation = 0

def draw_star_polygon(rot):
    t.clear()
    t.penup()
    
    # Start at first vertex
    t.goto(radius, 0)
    t.setheading(rot)
    t.pendown()
    
    # Begin fill
    t.begin_fill()
    
    # Draw star by skipping every 2nd vertex (creates star effect)
    for _ in range(points):
        t.forward(radius * 2)
        t.left(angle * 2)   # Multiply angle to make star shape
    
    t.end_fill()

# Animation loop
while True:
    # Update color (rainbow cycle)
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(rgb)
    t.fillcolor(rgb)
    
    draw_star_polygon(rotation)
    
    turtle.update()
    
    # Spin and shift color
    rotation += 1.5
    hue += 0.008
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()

