import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("navy")
turtle.tracer(0, 0)

hue = 0.0

def draw_arm():
    """Draw one arm of the snowflake with repeating diamond shapes"""
    for i in range(4):
        t.forward(30)
        
        # Draw diamond
        t.left(45)
        t.forward(15)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(15)
        t.left(45)

def snowflake():
    for _ in range(6):
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(rgb)
        
        t.penup()
        t.goto(0, 0)
        t.setheading(_ * 60)
        t.pendown()
        
        draw_arm()

# Animate
while True:
    t.clear()
    snowflake()
    turtle.update()
    hue += 0.01
    if hue > 1.0:
        hue = 0

turtle.done()