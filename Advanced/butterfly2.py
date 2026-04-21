import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("darkblue")
turtle.tracer(0, 0)
turtle.title("Monarch Butterfly")

hue = 0.0

def draw_wing_half(side):
    """Draw half wing based on side (+1 for right, -1 for left)"""
    direction = side
    
    t.setheading(90)
    t.circle(direction * 40, 60)
    t.circle(direction * 80, 40)
    t.circle(direction * 60, 50)
    t.setheading(180 + direction * 20)
    t.forward(70)
    t.setheading(200 + direction * 30)
    t.circle(direction * 50, 60)
    t.circle(direction * 70, 40)

def draw_wing_pattern(side):
    """Draw decorative patterns on wings"""
    direction = side
    
    # Inner wing patterns
    t.penup()
    t.goto(direction * 30, 40)
    t.pendown()
    for _ in range(3):
        t.circle(direction * 15, 360)
        t.penup()
        t.forward(direction * 20)
        t.pendown()

def draw_butterfly():
    """Draw complete symmetrical butterfly"""
    global hue
    
    # Body
    t.penup()
    t.goto(0, -60)
    t.pendown()
    t.pencolor("white")
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(90)
    t.forward(120)
    t.circle(8, 180)
    t.forward(120)
    t.end_fill()
    
    # Left wing
    t.penup()
    t.goto(0, 30)
    t.pendown()
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 0.8)
    t.pencolor(rgb)
    t.fillcolor(rgb)
    t.begin_fill()
    draw_wing_half(-1)
    t.end_fill()
    
    # Right wing
    t.penup()
    t.goto(0, 30)
    t.pendown()
    rgb2 = colorsys.hsv_to_rgb((hue + 0.15) % 1.0, 1.0, 0.8)
    t.pencolor(rgb2)
    t.fillcolor(rgb2)
    t.begin_fill()
    draw_wing_half(1)
    t.end_fill()
    
    # Wing patterns
    draw_wing_pattern(-1)
    draw_wing_pattern(1)
    
    # Antennae
    t.penup()
    t.goto(0, 65)
    t.pendown()
    t.pencolor("gold")
    t.setheading(160)
    t.forward(35)
    t.backward(35)
    t.setheading(20)
    t.forward(35)

# Animation
while True:
    t.clear()
    draw_butterfly()
    turtle.update()
    hue += 0.008
    if hue > 1.0:
        hue -= 1.0

turtle.done()