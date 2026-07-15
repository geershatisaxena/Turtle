import turtle
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Animated Checkerboard")
screen.setup(width=600, height=600)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_animated_checkerboard(rows, cols, size, delay=0.05):
    """Draw checkerboard with animation"""
    
    colors = ['black', 'red']
    
    # Starting position (centered)
    start_x = -(cols * size) / 2
    start_y = (rows * size) / 2
    
    # Draw each square with animation
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * size
            y = start_y - row * size
            
            # Determine color
            if (row + col) % 2 == 0:
                t.color(colors[0])
            else:
                t.color(colors[1])
            
            # Draw square
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            
            for _ in range(4):
                t.forward(size)
                t.right(90)
            
            t.end_fill()
            
            # Update screen to show animation
            screen.update()
            time.sleep(delay)
    
    # Draw border
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("black")
    t.width(3)
    
    for _ in range(2):
        t.forward(cols * size)
        t.right(90)
        t.forward(rows * size)
        t.right(90)
    
    t.width(1)

# Draw animated checkerboard
draw_animated_checkerboard(8, 8, 50, delay=0.02)

# Keep window open
turtle.done()