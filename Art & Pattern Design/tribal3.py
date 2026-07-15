import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a0a0a")
screen.title("Simple Tribal Symmetry")
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_tribal_element(size):
    """Draw one tribal element"""
    t.color('#DAA520')
    t.begin_fill()
    
    # Draw tribal shape
    for _ in range(3):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(120)
    
    t.end_fill()
    
    # Add inner detail
    t.color('#8B0000')
    t.penup()
    t.forward(size * 0.3)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.2)
    t.end_fill()
    t.penup()
    t.backward(size * 0.3)

def draw_symmetric_pattern():
    """Draw a symmetrical tribal pattern"""
    
    # Draw 8-fold symmetry
    for i in range(8):
        angle = i * 45
        
        # Main element
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(80)
        t.pendown()
        
        draw_tribal_element(40)
        t.penup()
        t.backward(80)
        
        # Inner element
        t.setheading(angle + 22.5)
        t.forward(50)
        t.pendown()
        t.color('#FF4500')
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.penup()
        t.backward(50)
    
    # Draw center
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color('#DAA520')
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    t.color('#8B0000')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# Draw the pattern
draw_symmetric_pattern()

# Keep window open
turtle.done()