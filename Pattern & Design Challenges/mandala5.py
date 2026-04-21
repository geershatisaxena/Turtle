import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)

num_arms = 12
hue = 0.0

def draw_arc_shape():
    """Draw one repeating arc shape"""
    t.circle(50, 90)
    t.left(90)
    t.circle(50, 90)

while True:
    t.clear()
    
    for i in range(num_arms):
        rgb = colorsys.hsv_to_rgb((hue + i * 0.05) % 1.0, 1.0, 0.9)
        t.pencolor(rgb)
        
        t.penup()
        t.goto(0, 0)
        t.setheading(i * (360 / num_arms))
        t.forward(80)
        t.pendown()
        
        draw_arc_shape()
    
    # Center circle
    t.penup()
    t.goto(0, -20)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 1.0, 1.0)
    t.fillcolor(rgb)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    turtle.update()
    hue += 0.008
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()