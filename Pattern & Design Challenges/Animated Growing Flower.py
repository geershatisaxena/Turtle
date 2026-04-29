import turtle
import time

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)
t.hideturtle()

# Draw growing flower
def grow_flower(num_petals):
    t.clear()
    
    # Draw petals
    for i in range(num_petals):
        t.fillcolor("pink")
        t.begin_fill()
        
        t.circle(50, 60)
        t.left(120)
        t.circle(50, 60)
        t.left(120)
        
        t.end_fill()
        t.left(360 / num_petals)
    
    # Draw center
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Animate growing petals
for petals in range(6, 25, 2):
    grow_flower(petals)
    time.sleep(0.3)

turtle.done()