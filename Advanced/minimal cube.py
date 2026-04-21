import turtle
import colorsys
import math

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)

# Cube coordinates (front and back squares)
front = [(-100, -80), (100, -80), (100, 80), (-100, 80)]
back = [(-60, -40), (60, -40), (60, 40), (-60, 40)]

hue = 0.0
rotation = 0

while True:
    t.clear()
    
    # Rotate back face
    rx = math.sin(rotation) * 30
    ry = math.cos(rotation * 0.6) * 20
    rotated_back = [(x + rx, y + ry) for (x, y) in back]
    
    # Draw back square (darker)
    rgb_back = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 1.0, 0.4)
    t.pencolor(rgb_back)
    t.penup()
    t.goto(rotated_back[0])
    t.pendown()
    for p in rotated_back[1:]:
        t.goto(p)
    t.goto(rotated_back[0])
    
    # Draw connecting lines
    for i in range(4):
        rgb_line = colorsys.hsv_to_rgb((hue + 0.3) % 1.0, 1.0, 0.7)
        t.pencolor(rgb_line)
        t.penup()
        t.goto(rotated_back[i])
        t.pendown()
        t.goto(front[i])
    
    # Draw front square (brightest)
    rgb_front = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(rgb_front)
    t.penup()
    t.goto(front[0])
    t.pendown()
    for p in front[1:]:
        t.goto(p)
    t.goto(front[0])
    
    turtle.update()
    
    rotation += 0.05
    hue += 0.008
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()