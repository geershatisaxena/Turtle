import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Colorful Snowflake")

# Snowflake settings
num_branches = 6      # Number of symmetrical branches
branch_length = 120
hue = 0.0
angle = 0             # ← FIX 1: Define angle globally

def draw_branch():
    """Draw one branch of the snowflake with smaller repeating shapes"""
    # Main branch line
    t.forward(branch_length)
    
    # Draw small side shapes (like frost crystals)
    for i in range(3):
        t.backward(branch_length * 0.3)
        t.left(45)
        draw_crystal(20)
        t.right(90)
        draw_crystal(20)
        t.left(45)
    
    t.backward(branch_length * 0.1)

def draw_crystal(size):
    """Draw a small diamond/crystal shape"""
    t.pendown()
    for _ in range(2):
        t.forward(size)
        t.left(60)
        t.forward(size)
        t.left(120)
    t.penup()

def draw_snowflake():
    """Draw one complete snowflake with colored branches"""
    global angle, hue   # ← FIX 2: Declare angle and hue as global
    
    for _ in range(num_branches):
        # Change color gradually
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(rgb)
        
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()
        
        draw_branch()
        
        angle += 360 / num_branches

# Animation loop
while True:
    t.clear()
    
    # Update color
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(rgb)
    
    draw_snowflake()
    
    turtle.update()
    
    # Spin and shift color
    angle += 1
    hue += 0.005
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()