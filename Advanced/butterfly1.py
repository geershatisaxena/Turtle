import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Symmetrical Butterfly")

# Butterfly settings
wing_scale = 1.0
hue = 0.0

def draw_left_wing():
    """Draw the left half of the butterfly"""
    # Upper wing
    t.setheading(60)
    t.circle(50, 80)      # Wing curve
    t.circle(100, 40)     # Wing outer edge
    t.circle(80, 50)      # Wing bottom curve
    t.setheading(200)
    t.forward(60)
    
    # Lower wing
    t.setheading(240)
    t.circle(60, 70)
    t.circle(90, 45)
    t.setheading(160)
    t.forward(50)

def draw_right_wing():
    """Draw the right half of the butterfly (mirror)"""
    # Upper wing
    t.setheading(120)
    t.circle(-50, 80)
    t.circle(-100, 40)
    t.circle(-80, 50)
    t.setheading(-20)
    t.forward(60)
    
    # Lower wing
    t.setheading(-60)
    t.circle(-60, 70)
    t.circle(-90, 45)
    t.setheading(20)
    t.forward(50)

def draw_butterfly():
    """Draw complete symmetrical butterfly"""
    # Draw body
    t.penup()
    t.goto(0, -80)
    t.pendown()
    t.setheading(90)
    t.forward(160)
    
    # Draw left wing with color
    t.penup()
    t.goto(0, 20)
    t.pendown()
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 0.9)
    t.pencolor(rgb)
    t.fillcolor(rgb)
    t.begin_fill()
    draw_left_wing()
    t.end_fill()
    
    # Draw right wing with mirrored color
    t.penup()
    t.goto(0, 20)
    t.pendown()
    rgb2 = colorsys.hsv_to_rgb((hue + 0.1) % 1.0, 1.0, 0.9)
    t.pencolor(rgb2)
    t.fillcolor(rgb2)
    t.begin_fill()
    draw_right_wing()
    t.end_fill()
    
    # Draw antennae
    t.penup()
    t.goto(0, 80)
    t.pendown()
    t.pencolor("white")
    t.setheading(150)
    t.forward(40)
    t.backward(40)
    t.setheading(30)
    t.forward(40)

# Animation - color cycling and gentle flapping
flap = 0
while True:
    t.clear()
    
    # Gentle wing flapping effect
    wing_scale = 0.8 + math.sin(flap) * 0.2
    
    draw_butterfly()
    
    # Add decorative wing spots
    t.penup()
    for spot in [(30, 50), (40, 30), (50, 10), (-30, 50), (-40, 30), (-50, 10)]:
        t.goto(spot[0], spot[1])
        t.dot(8, colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 1.0, 1.0))
    
    turtle.update()
    
    flap += 0.05
    hue += 0.005
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()