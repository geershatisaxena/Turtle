import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a2a")
screen.title("Simple Lotus")
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(5)
t.hideturtle()

def draw_petal(size, color):
    """Draw one petal"""
    t.color(color)
    t.begin_fill()
    
    # Draw petal shape with arcs
    t.circle(size, 60)   # First curve
    t.left(120)
    t.circle(size, 60)   # Second curve
    t.left(120)
    t.circle(size, 60)   # Third curve
    
    t.end_fill()

def draw_simple_lotus():
    """Draw a simple lotus with 8 petals"""
    
    # Move to center
    t.penup()
    t.goto(0, -50)
    t.pendown()
    
    # Draw 8 petals in a circle
    for i in range(8):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 45)  # 45 degrees apart
        t.forward(30)
        t.pendown()
        
        draw_petal(60, '#FF69B4')
    
    # Draw center
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color('#FFD700')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    # Draw center dots
    for i in range(12):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 30)
        t.forward(12)
        t.pendown()
        t.color('#FFA500')
        t.dot(3)

# Draw the simple lotus
draw_simple_lotus()

# Keep window open
turtle.done()