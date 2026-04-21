import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(1)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Rainbow Target Board")

rings = 12
max_radius = 220
radius_step = max_radius / rings
hue = 0.0
rotation = 0

def draw_spinning_target():
    """Draw target with rotating ring segments"""
    for i in range(rings, 0, -1):
        radius = i * radius_step
        inner_radius = (i - 1) * radius_step
        
        # Calculate number of segments based on ring size
        num_segments = max(8, i * 2)
        angle_step = 360 / num_segments
        
        for seg in range(num_segments):
            # Calculate start and end angles
            start_angle = seg * angle_step + rotation
            end_angle = start_angle + angle_step
            
            # Color based on ring and segment
            color_hue = (hue + i * 0.05 + seg * 0.02) % 1.0
            rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
            t.fillcolor(rgb)
            t.pencolor(rgb)
            
            # Draw wedge
            t.penup()
            t.goto(0, 0)
            t.setheading(start_angle)
            t.forward(inner_radius)
            t.pendown()
            t.begin_fill()
            
            # Draw outer arc
            t.setheading(start_angle)
            t.forward(radius - inner_radius)
            t.left(90)
            t.circle(radius, angle_step)
            t.left(90)
            t.forward(radius - inner_radius)
            
            t.end_fill()

# Animation
while True:
    t.clear()
    draw_spinning_target()
    turtle.update()
    
    rotation += 1
    hue += 0.002
    
    if rotation >= 360:
        rotation -= 360
    if hue > 1.0:
        hue -= 1.0

turtle.done()