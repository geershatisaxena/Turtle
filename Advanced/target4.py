import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(3)
turtle.bgcolor("black")
turtle.tracer(0, 0)

# Ring settings
rings = 6
max_radius = 180
radius_step = max_radius / rings
hue = 0.0

while True:
    t.clear()
    
    # Draw rings from largest to smallest
    for i in range(rings, 0, -1):
        radius = i * radius_step
        
        # Alternate colors
        if i % 2 == 0:
            color = colorsys.hsv_to_rgb(hue, 1.0, 0.9)
        else:
            color = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 1.0, 0.6)
        
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        t.pencolor(color)
        t.fillcolor(color)
        
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    
    # Draw center bullseye
    t.penup()
    t.goto(0, -15)
    t.pendown()
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    turtle.update()
    hue += 0.01
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()