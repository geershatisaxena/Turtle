import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("darkblue")
turtle.tracer(0, 0)
turtle.title("Lotus Mandala")

num_layers = 4
petals_per_layer = [8, 12, 16, 24]
layer_radius = [40, 80, 130, 180]
hue = 0.0
rotation = 0

def draw_lotus_petal(radius, angle, color_hue, layer):
    """Draw a lotus-style petal"""
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(radius * 0.7)
    t.left(90)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.8 + layer * 0.05)
    t.fillcolor(rgb)
    t.begin_fill()
    
    # Lotus petal shape
    t.circle(radius * 0.3, 60)
    t.circle(radius * 0.2, 80)
    t.circle(radius * 0.15, 40)
    t.circle(radius * 0.2, 80)
    t.circle(radius * 0.3, 60)
    
    t.end_fill()

while True:
    t.clear()
    
    # Draw each layer of petals
    for layer in range(num_layers):
        num_petals = petals_per_layer[layer]
        rad = layer_radius[layer]
        
        for i in range(num_petals):
            angle = i * (360 / num_petals) + rotation * (layer + 1) * 0.5
            color_hue = (hue + layer * 0.1 + i * 0.02) % 1.0
            draw_lotus_petal(rad, angle, color_hue, layer)
    
    # Decorative circles between layers
    for rad in layer_radius:
        t.penup()
        t.goto(0, -rad)
        t.pendown()
        rgb = colorsys.hsv_to_rgb((hue + 0.4) % 1.0, 1.0, 0.5)
        t.pencolor(rgb)
        t.width(1)
        t.circle(rad)
    
    # Center
    t.penup()
    t.goto(0, -15)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.7) % 1.0, 1.0, 1.0)
    t.fillcolor(rgb)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    turtle.update()
    
    rotation += 0.3
    hue += 0.002
    
    if rotation >= 360:
        rotation -= 360
    if hue > 1.0:
        hue -= 1.0

turtle.done()