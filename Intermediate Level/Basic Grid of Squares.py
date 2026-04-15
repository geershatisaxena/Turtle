import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a2a")
screen.title("Nested Loops Flower Pattern")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(1.5)

# Colors for different layers
colors = ["#FF6B6B", "#FFB347", "#FFD93D", "#6BCB77", "#4D96FF", "#9B59B6", "#FF6B9E"]

# === NESTED LOOP PATTERN ===
# Outer loop: controls the layers (rings of circles)
for layer in range(1, 7):          # 6 layers
    radius = layer * 15 + 10        # Increases with each layer
    num_circles = layer * 8         # More circles in outer layers
    color = colors[layer % len(colors)]
    
    # Inner loop: draws circles around the ring
    for i in range(num_circles):
        angle = 360 / num_circles * i
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(x, y - 8)            # Position for small circle
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(8)                 # Draw small circle
        t.end_fill()
        t.penup()

# === SECOND NESTED LOOP: offset layer for density ===
for layer in range(1, 5):
    radius = layer * 20 + 5
    num_circles = layer * 6 + 4
    color = colors[(layer + 3) % len(colors)]
    
    for i in range(num_circles):
        angle = 360 / num_circles * i + 15   # Offset angle
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(x, y - 5)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(5)
        t.end_fill()

# === CENTER: dense cluster of small circles (nested loop) ===
t.penup()
for r in range(5, 50, 6):          # Radii from 5 to 47
    num_small = max(6, r // 3)      # More circles as radius grows
    for i in range(num_small):
        angle = 360 / num_small * i + (r * 2)  # Slight rotation per layer
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        
        t.goto(x, y - 3)
        t.pendown()
        t.color("#FFD93D")
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.penup()

# === FINAL CENTER DOT ===
t.goto(0, -6)
t.color("#FFFFFF")
t.begin_fill()
t.circle(6)
t.end_fill()

t.hideturtle()
screen.update()
screen.mainloop()