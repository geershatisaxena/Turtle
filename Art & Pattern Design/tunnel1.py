import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Neon Tunnel")
screen.setup(width=600, height=600)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Neon colors
colors = ['#FF00FF', '#00FFFF', '#FF0066', '#33FF33', '#FF6600', '#9933FF']

def draw_simple_tunnel():
    """Draw a simple neon tunnel"""
    
    # Draw concentric rings with neon effect
    for i in range(40):
        # Calculate ring size (smaller rings go deeper)
        size = 280 * (1 - i / 40 * 0.85)
        
        # Select color
        color = colors[i % len(colors)]
        t.color(color)
        
        # Draw ring with glow
        t.penup()
        t.goto(0, -size)
        t.pendown()
        t.width(2 + i * 0.05)
        
        # Draw circle with segments for neon effect
        for angle in range(0, 360, 10):
            x = size * math.cos(math.radians(angle))
            y = size * math.sin(math.radians(angle))
            t.goto(x, y)
            
            # Add glow dots
            if angle % 30 == 0:
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.color(colors[(i + 1) % len(colors)])
                t.dot(3)
                t.penup()
                t.goto(0, -size)
                t.pendown()
                t.color(color)
    
    # Draw center glow
    for i in range(10, 0, -1):
        t.penup()
        t.goto(0, -i * 5)
        t.pendown()
        brightness = int(255 * (1 - i/10))
        t.color(f"#{brightness:02x}00{brightness:02x}")
        t.circle(i * 5)

# Draw the tunnel
draw_simple_tunnel()

# Update screen
screen.update()
turtle.done()