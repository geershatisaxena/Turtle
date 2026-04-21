import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)

hue = 0.0

def draw_side(side):
    """Draw one side of the butterfly (side = -1 or 1)"""
    rgb = colorsys.hsv_to_rgb((hue + (0 if side == -1 else 0.2)) % 1.0, 1.0, 0.9)
    t.pencolor(rgb)
    t.fillcolor(rgb)
    t.begin_fill()
    
    # Upper wing arc
    t.setheading(side * 60)
    t.circle(side * 60, 60)
    t.circle(side * 40, 70)
    
    # Lower wing arc
    t.setheading(side * -50)
    t.circle(side * 50, 60)
    t.circle(side * 35, 65)
    
    t.end_fill()

while True:
    t.clear()
    
    # Body
    t.penup()
    t.goto(0, -60)
    t.pendown()
    t.pencolor("white")
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(90)
    t.forward(120)
    t.circle(6, 180)
    t.forward(120)
    t.end_fill()
    
    # Draw both sides using symmetry
    draw_side(-1)  # Left
    draw_side(1)   # Right
    
    turtle.update()
    hue += 0.01
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()