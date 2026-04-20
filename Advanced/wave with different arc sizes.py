import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Layered Arc Waves")

# Wave layers
layers = [
    {"radius": 15, "y_offset": -40, "speed": 2, "color_offset": 0.0},
    {"radius": 20, "y_offset": 0,   "speed": 3, "color_offset": 0.3},
    {"radius": 25, "y_offset": 40,  "speed": 4, "color_offset": 0.6}
]

num_arcs = 25
hue = 0.0
scroll_pos = 0

def draw_arc_wave(y_pos, arc_radius, color_hue):
    """Draw a wave at specific y-position with given arc radius"""
    t.penup()
    t.goto(scroll_pos, y_pos)
    t.setheading(0)
    t.pendown()
    
    for i in range(num_arcs):
        rgb = colorsys.hsv_to_rgb((color_hue + i * 0.03) % 1.0, 1.0, 0.9)
        t.pencolor(rgb)
        
        if i % 2 == 0:
            t.circle(arc_radius, 180)
        else:
            t.circle(-arc_radius, 180)

# Animation loop
while True:
    t.clear()
    
    # Draw each layer
    for layer in layers:
        layer_hue = (hue + layer["color_offset"]) % 1.0
        draw_arc_wave(layer["y_offset"], layer["radius"], layer_hue)
    
    turtle.update()
    
    # Scroll and update colors
    scroll_pos += 3
    hue += 0.008
    
    if scroll_pos > 300:
        scroll_pos = -300
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()