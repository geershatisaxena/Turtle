import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Radial Arc Wave")

num_arcs = 16
arc_radius = 40
radius = 150
hue = 0.0
rotation = 0

def draw_radial_arc(angle, color_hue):
    """Draw an arc radiating from center"""
    t.penup()
    rad = math.radians(angle)
    x = math.cos(rad) * radius
    y = math.sin(rad) * radius
    t.goto(x, y)
    
    # Point toward center
    t.setheading(angle + 180)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
    t.pencolor(rgb)
    
    # Draw arc curving outward
    t.circle(arc_radius, 180)

# Animation loop
while True:
    t.clear()
    
    # Draw arcs in a circle
    for i in range(num_arcs):
        angle = i * (360 / num_arcs) + rotation
        color_hue = (hue + i * 0.05) % 1.0
        draw_radial_arc(angle, color_hue)
    
    turtle.update()
    
    # Spin and change color
    rotation += 2
    hue += 0.008
    
    if rotation > 360:
        rotation -= 360
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()