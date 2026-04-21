import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Spirograph Pattern")

# Spirograph parameters
R = 150        # Radius of large circle
r = 45         # Radius of small circle
d = 100        # Distance from center of small circle
hue = 0.0

def draw_spirograph():
    """Draw a classic spirograph pattern"""
    global hue
    
    t.penup()
    
    # Fixed number of steps (works with floats)
    total_steps = 720  # Enough for a complete pattern
    
    for theta in range(0, total_steps, 2):
        # Parametric equations for spirograph
        rad = math.radians(theta)
        x = (R - r) * math.cos(rad) + d * math.cos((R - r) * rad / r)
        y = (R - r) * math.sin(rad) - d * math.sin((R - r) * rad / r)
        
        # Color based on angle
        rgb = colorsys.hsv_to_rgb((hue + theta * 0.003) % 1.0, 1.0, 0.9)
        t.pencolor(rgb)
        
        if theta == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    
    t.penup()

# Animation - slowly change parameters
d_increment = 0
r_increment = 0
R_increment = 0

while True:
    t.clear()
    
    # Slowly vary parameters for evolving pattern
    d = 80 + math.sin(d_increment) * 40
    r = 35 + math.sin(r_increment) * 15
    R = 140 + math.sin(R_increment) * 20
    
    draw_spirograph()
    turtle.update()
    
    hue += 0.003
    
    d_increment += 0.01
    r_increment += 0.007
    R_increment += 0.005
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()