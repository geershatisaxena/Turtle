import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Simple Mandala")

num_petals = 8
hue = 0.0

def draw_petal():
    """Draw one petal"""
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(120)

while True:
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Draw petals around the circle
    for i in range(num_petals):
        rgb = colorsys.hsv_to_rgb((hue + i * 0.05) % 1.0, 1.0, 0.9)
        t.pencolor(rgb)
        t.fillcolor(rgb)
        
        t.begin_fill()
        draw_petal()
        t.end_fill()
        t.left(360 / num_petals)
    
    # Draw center circle
    t.penup()
    t.goto(0, -30)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 1.0, 1.0)
    t.fillcolor(rgb)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    turtle.update()
    hue += 0.01
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()