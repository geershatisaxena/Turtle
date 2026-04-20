import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(3)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Standing Arc Wave")

num_arcs = 20
arc_radius = 25
wave_amplitude = 60
wave_frequency = 0.3
hue = 0.0
time = 0

def draw_arc_at_position(x_pos, y_offset, color_hue):
    """Draw an arc at specific x,y position with vertical offset"""
    t.penup()
    t.goto(x_pos, y_offset)
    t.setheading(0)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
    t.pencolor(rgb)
    
    # Alternate arc direction based on position
    if int(x_pos / 20) % 2 == 0:
        t.circle(arc_radius, 180)
    else:
        t.circle(-arc_radius, 180)

# Animation loop
while True:
    t.clear()
    
    # Draw arcs across the screen
    for x in range(-300, 320, 30):
        # Create wave motion using sine
        y_offset = math.sin(x * wave_frequency + time) * wave_amplitude
        
        # Color based on position and time
        color_hue = (hue + x * 0.002) % 1.0
        draw_arc_at_position(x, y_offset, color_hue)
    
    turtle.update()
    
    # Update wave and color
    time += 0.1
    hue += 0.01
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()