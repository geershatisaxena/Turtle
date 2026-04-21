import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(3)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Geometric Butterfly")

hue = 0.0

def draw_symmetrical_shape():
    """Draw shape using mirror symmetry"""
    for side in [-1, 1]:  # Left then right
        t.penup()
        t.goto(0, 0)
        t.pendown()
        
        # Upper wing
        t.setheading(side * 30)
        t.forward(80)
        t.left(60)
        t.forward(60)
        t.left(120)
        t.forward(60)
        t.left(60)
        t.forward(80)
        
        # Lower wing
        t.setheading(side * -30)
        t.forward(60)
        t.right(50)
        t.forward(50)
        t.right(80)
        t.forward(50)
        t.right(50)
        t.forward(60)

# Animation
while True:
    t.clear()
    
    # Draw body
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.pencolor("white")
    t.fillcolor("gray")
    t.begin_fill()
    t.setheading(90)
    t.forward(100)
    t.circle(5, 180)
    t.forward(100)
    t.end_fill()
    
    # Draw symmetrical wings
    for side in [-1, 1]:
        t.penup()
        t.goto(0, 20)
        t.pendown()
        
        rgb = colorsys.hsv_to_rgb((hue + (0 if side == -1 else 0.15)) % 1.0, 1.0, 0.9)
        t.pencolor(rgb)
        t.fillcolor(rgb)
        t.begin_fill()
        
        # Upper wing
        t.setheading(side * 45)
        t.forward(70)
        t.left(70)
        t.forward(50)
        t.left(110)
        t.forward(50)
        t.left(70)
        t.forward(70)
        
        # Lower wing
        t.setheading(side * -40)
        t.forward(50)
        t.left(60)
        t.forward(40)
        t.left(120)
        t.forward(40)
        t.left(60)
        t.forward(50)
        
        t.end_fill()
    
    # Draw antennae
    t.penup()
    t.goto(0, 55)
    t.pendown()
    t.pencolor("yellow")
    t.setheading(150)
    t.forward(30)
    t.backward(30)
    t.setheading(30)
    t.forward(30)
    
    turtle.update()
    hue += 0.01
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()