import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Mandala Pattern")

# Mandala settings
num_petals = 12
radius = 180
hue = 0.0
rotation = 0

def draw_petal(angle, size, color_hue):
    """Draw a single petal shape"""
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(radius * 0.3)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
    t.pencolor(rgb)
    t.fillcolor(rgb)
    t.begin_fill()
    
    # Draw petal using arcs
    t.circle(size, 60)
    t.circle(size * 0.6, 80)
    t.circle(size * 0.4, 60)
    t.circle(size, 60)
    
    t.end_fill()

def draw_circle_layer(radius_layer, width_layer, color_offset):
    """Draw a decorative circle layer"""
    t.penup()
    t.goto(0, -radius_layer)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb((hue + color_offset) % 1.0, 1.0, 0.7)
    t.pencolor(rgb)
    t.width(width_layer)
    t.circle(radius_layer)

def draw_dot_pattern(radius_dots, num_dots, color_offset):
    """Draw dots around a circle"""
    angle_step = 360 / num_dots
    
    for i in range(num_dots):
        angle = i * angle_step + rotation
        rad = math.radians(angle)
        x = math.cos(rad) * radius_dots
        y = math.sin(rad) * radius_dots
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        rgb = colorsys.hsv_to_rgb((hue + color_offset + i * 0.02) % 1.0, 1.0, 1.0)
        t.fillcolor(rgb)
        t.begin_fill()
        t.circle(6)
        t.end_fill()

def draw_mandala():
    """Draw complete mandala pattern"""
    # Outer decorative circles
    draw_circle_layer(radius, 3, 0.0)
    draw_circle_layer(radius - 15, 2, 0.1)
    draw_circle_layer(radius - 30, 1, 0.2)
    
    # Inner circle
    draw_circle_layer(radius * 0.6, 3, 0.5)
    draw_circle_layer(radius * 0.4, 2, 0.6)
    draw_circle_layer(radius * 0.2, 2, 0.7)
    
    # Draw petals
    for i in range(num_petals):
        angle = i * (360 / num_petals) + rotation
        color_hue = (hue + i * 0.03) % 1.0
        draw_petal(angle, radius * 0.5, color_hue)
    
    # Draw inner petals
    for i in range(num_petals * 2):
        angle = i * (360 / (num_petals * 2)) + rotation
        color_hue = (hue + 0.3 + i * 0.02) % 1.0
        draw_petal(angle, radius * 0.25, color_hue)
    
    # Draw dot patterns
    draw_dot_pattern(radius - 20, num_petals * 2, 0.8)
    draw_dot_pattern(radius * 0.7, num_petals, 0.4)
    draw_dot_pattern(radius * 0.5, num_petals * 3, 0.6)
    draw_dot_pattern(radius * 0.3, num_petals, 0.9)
    
    # Center dot
    t.penup()
    t.goto(0, -12)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.9) % 1.0, 1.0, 1.0)
    t.fillcolor(rgb)
    t.begin_fill()
    t.circle(12)
    t.end_fill()

# Animation loop
while True:
    t.clear()
    draw_mandala()
    turtle.update()
    
    rotation += 0.5
    hue += 0.002
    
    if rotation >= 360:
        rotation -= 360
    if hue > 1.0:
        hue -= 1.0

turtle.done()