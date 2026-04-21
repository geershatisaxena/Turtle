import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Target Board")

# Target settings
rings = 8                    # Number of concentric circles
max_radius = 200             # Outer circle radius
radius_step = max_radius / rings
hue = 0.0

def draw_concentric_circles():
    """Draw all concentric circles from largest to smallest"""
    for i in range(rings, 0, -1):  # Largest to smallest
        radius = i * radius_step
        
        # Calculate color - alternate or gradient
        if i % 2 == 0:
            # Even rings: brighter, saturated color
            rgb = colorsys.hsv_to_rgb((hue + i * 0.05) % 1.0, 1.0, 0.9)
        else:
            # Odd rings: darker or complementary
            rgb = colorsys.hsv_to_rgb((hue + i * 0.05 + 0.5) % 1.0, 1.0, 0.5)
        
        t.pencolor(rgb)
        t.fillcolor(rgb)
        
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        
        # Draw and fill circle
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

def draw_crosshairs():
    """Draw crosshair lines through the center"""
    t.penup()
    t.goto(0, -max_radius - 10)
    t.pendown()
    t.goto(0, max_radius + 10)
    
    t.penup()
    t.goto(-max_radius - 10, 0)
    t.pendown()
    t.goto(max_radius + 10, 0)

def draw_bullseye():
    """Draw center bullseye marker"""
    t.penup()
    t.goto(0, -10)
    t.pendown()
    rgb = colorsys.hsv_to_rgb((hue + 0.8) % 1.0, 1.0, 1.0)
    t.pencolor(rgb)
    t.fillcolor(rgb)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Animation loop
while True:
    t.clear()
    
    # Draw target board
    draw_concentric_circles()
    
    # Draw crosshairs with glowing color
    rgb_cross = colorsys.hsv_to_rgb((hue + 0.2) % 1.0, 1.0, 0.8)
    t.pencolor(rgb_cross)
    draw_crosshairs()
    
    # Draw bullseye
    draw_bullseye()
    
    turtle.update()
    
    # Cycle colors
    hue += 0.005
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()