import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a0a2e")  # Deep purple night sky
screen.title("Lotus Flower")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create turtle
lotus = turtle.Turtle()
lotus.speed(0)
lotus.hideturtle()

# Color palette
colors = {
    'petal_light': '#FFB7D5',
    'petal_mid': '#FF69B4',
    'petal_dark': '#FF1493',
    'petal_tip': '#FF0066',
    'center': '#FFD700',
    'stamen': '#FFA500',
    'water': '#1a3a5c',
    'leaf': '#228B22',
    'leaf_light': '#32CD32'
}

def draw_petal(radius, angle, color, reverse=False):
    """Draw a single petal using arcs"""
    lotus.penup()
    lotus.setheading(0)
    
    if reverse:
        lotus.right(angle/2)
    else:
        lotus.left(angle/2)
    
    lotus.forward(radius)
    lotus.pendown()
    lotus.color(color)
    lotus.begin_fill()
    
    # Draw petal using arcs
    # First arc (left side)
    lotus.left(90)
    lotus.circle(radius * 0.6, 120)
    
    # Second arc (right side)  
    lotus.right(60)
    lotus.circle(radius * 0.6, 120)
    
    # Complete the petal
    lotus.right(150)
    lotus.forward(radius * 0.3)
    
    lotus.end_fill()

def draw_layered_petal(radius, angle, colors_list, layers=3):
    """Draw a petal with multiple layers for depth"""
    for i in range(layers):
        scale = 1 - (i * 0.15)
        r = radius * scale
        color = colors_list[i % len(colors_list)]
        draw_petal(r, angle, color)

def draw_lotus_flower(petals=12, petal_size=150):
    """Draw the complete lotus flower"""
    
    # Draw water reflection
    lotus.penup()
    lotus.goto(0, -300)
    lotus.pendown()
    lotus.color("#0a1a3a")
    lotus.begin_fill()
    lotus.circle(350)
    lotus.end_fill()
    
    # Draw water ripples
    for i in range(3, 0, -1):
        lotus.penup()
        lotus.goto(0, -i * 80 - 50)
        lotus.pendown()
        lotus.color(f"#{int(30+50*i):02x}{int(50+30*i):02x}{int(80+40*i):02x}")
        lotus.width(1)
        lotus.circle(i * 80 + 50)
    
    # Draw floating leaves
    for i in range(6):
        angle = i * 60 + 30
        lotus.penup()
        x = 180 * math.cos(math.radians(angle))
        y = 180 * math.sin(math.radians(angle)) - 100
        lotus.goto(x, y)
        lotus.pendown()
        
        # Draw leaf
        lotus.color(colors['leaf_light'] if i % 2 == 0 else colors['leaf'])
        lotus.begin_fill()
        lotus.circle(40, 60)
        lotus.left(120)
        lotus.circle(40, 60)
        lotus.left(120)
        lotus.circle(40, 60)
        lotus.end_fill()
        
        # Leaf vein
        lotus.penup()
        lotus.goto(x, y + 20)
        lotus.pendown()
        lotus.color('#006400')
        lotus.width(1)
        lotus.goto(x, y - 20)
        lotus.penup()
    
    # Draw outer petals (larger, lighter)
    for i in range(petals):
        angle = (i / petals) * 360
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        lotus.forward(20)
        
        # Alternate colors for outer petals
        if i % 3 == 0:
            color = colors['petal_light']
        elif i % 3 == 1:
            color = colors['petal_mid']
        else:
            color = '#FF8CBF'
        
        draw_petal(petal_size * 0.8, 45, color)
    
    # Draw middle petals (slightly smaller, deeper color)
    for i in range(petals - 2):
        angle = (i / (petals - 2)) * 360 + 15
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        lotus.forward(10)
        
        if i % 2 == 0:
            color = colors['petal_mid']
        else:
            color = colors['petal_dark']
        
        draw_petal(petal_size * 0.6, 40, color)
    
    # Draw inner petals (smallest, darkest)
    for i in range(petals - 4):
        angle = (i / (petals - 4)) * 360 + 7.5
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        
        if i % 2 == 0:
            color = colors['petal_dark']
        else:
            color = colors['petal_tip']
        
        draw_petal(petal_size * 0.4, 35, color)
    
    # Draw center of lotus
    lotus.penup()
    lotus.goto(0, 0)
    lotus.pendown()
    lotus.color(colors['center'])
    lotus.begin_fill()
    lotus.circle(20)
    lotus.end_fill()
    
    # Draw stamens
    for i in range(24):
        angle = (i / 24) * 360
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        lotus.forward(15)
        lotus.pendown()
        lotus.color(colors['stamen'])
        lotus.width(2)
        lotus.forward(10)
        lotus.penup()
        lotus.dot(3, colors['center'])
    
    # Draw inner stamens
    for i in range(12):
        angle = (i / 12) * 360 + 15
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        lotus.forward(10)
        lotus.pendown()
        lotus.color('#FF8C00')
        lotus.width(1)
        lotus.forward(6)
        lotus.penup()
        lotus.dot(2, '#FFD700')

def draw_lotus_buddha_style():
    """Draw a lotus with Buddha-style symmetrical petals"""
    
    # Background
    lotus.penup()
    lotus.goto(0, -350)
    lotus.pendown()
    lotus.color("#0d0d2b")
    lotus.begin_fill()
    lotus.circle(350)
    lotus.end_fill()
    
    # Draw 8-petal lotus (sacred geometry)
    for i in range(8):
        angle = i * 45
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        
        # Multi-layered petal
        for layer in range(3):
            scale = 1 - (layer * 0.15)
            r = 150 * scale
            lotus.penup()
            lotus.forward(10 * (layer + 1))
            lotus.pendown()
            
            if layer == 0:
                color = '#FF6B9D'
            elif layer == 1:
                color = '#FF1493'
            else:
                color = '#C71585'
            
            lotus.color(color)
            lotus.begin_fill()
            
            # Draw symmetrical petal
            for j in range(2):
                lotus.circle(r * 0.4, 60)
                lotus.left(120)
                lotus.circle(r * 0.4, 60)
                lotus.left(60)
            
            lotus.end_fill()
            lotus.penup()
            lotus.goto(0, 0)
    
    # Inner lotus
    for i in range(8):
        angle = i * 45 + 22.5
        lotus.penup()
        lotus.goto(0, 0)
        lotus.setheading(angle)
        lotus.forward(30)
        lotus.pendown()
        lotus.color('#FF69B4')
        lotus.begin_fill()
        lotus.circle(40, 90)
        lotus.left(90)
        lotus.circle(40, 90)
        lotus.left(90)
        lotus.circle(40, 90)
        lotus.left(90)
        lotus.circle(40, 90)
        lotus.end_fill()
        lotus.penup()
    
    # Center
    lotus.penup()
    lotus.goto(0, 0)
    lotus.pendown()
    lotus.color('#FFD700')
    lotus.begin_fill()
    lotus.circle(25)
    lotus.end_fill()
    
    # Sacred geometry circles
    for r in [50, 100, 150, 200, 250]:
        lotus.penup()
        lotus.goto(0, -r)
        lotus.pendown()
        lotus.color(f"#{int(200-50*(r/250)):02x}{int(100-30*(r/250)):02x}{int(255-80*(r/250)):02x}")
        lotus.width(1)
        lotus.circle(r)
        lotus.width(1)

# Draw the lotus
draw_lotus_flower(petals=12, petal_size=150)

# Alternative: Draw Buddha-style lotus (uncomment to use)
# draw_lotus_buddha_style()

# Update screen
screen.update()

# Keep window open
turtle.done()