import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Arc Wave Pattern")

# Wave settings
arc_radius = 20
num_arcs = 30
amplitude = 80
hue = 0.0

def draw_single_arc(direction):
    """Draw one small arc (180 degrees)"""
    if direction == "right":
        t.circle(arc_radius, 180)   # Arc curving up
    else:
        t.circle(-arc_radius, 180)  # Arc curving down

def draw_wave():
    """Draw a complete wave using alternating arcs"""
    for i in range(num_arcs):
        # Alternating colors for visual interest
        rgb = colorsys.hsv_to_rgb((hue + i * 0.02) % 1.0, 1.0, 0.8)
        t.pencolor(rgb)
        
        if i % 2 == 0:
            draw_single_arc("right")
        else:
            draw_single_arc("left")

# Animation loop - scrolling wave
x_pos = -300
while True:
    t.clear()
    t.penup()
    t.goto(x_pos, 0)
    t.setheading(0)  # Face right
    t.pendown()
    
    draw_wave()
    
    turtle.update()
    
    # Scroll the wave
    x_pos += 3
    hue += 0.005
    
    if x_pos > 300:
        x_pos = -300
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()