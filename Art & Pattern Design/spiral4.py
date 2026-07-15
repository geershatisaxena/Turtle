import turtle
import math
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Web")
screen.tracer(0)

# Create turtle
web = turtle.Turtle()
web.speed(0)
web.hideturtle()

# Color palette
colors = [
    "#FF6B6B",  # Red
    "#FFD93D",  # Gold
    "#6BCB77",  # Green
    "#4D96FF",  # Blue
    "#9B59B6",  # Purple
    "#FF69B4",  # Pink
    "#00CED1",  # Turquoise
    "#FF8C00",  # Dark Orange
    "#DA70D6",  # Orchid
    "#7FFF00",  # Chartreuse
]

def draw_spiral_web(radius, turns, loops, color_shift=False):
    """Draw a spiral web pattern"""
    for i in range(loops):
        # Calculate angle and radius for spiral
        angle = i * 0.3
        r = radius * (i / loops)
        
        # Spiral path
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        
        # Change color based on position
        if color_shift:
            color_index = int((i / loops) * len(colors))
            web.color(colors[color_index % len(colors)])
        else:
            web.color(random.choice(colors))
        
        # Draw spiral line
        web.penup()
        web.goto(x, y)
        web.pendown()
        
        # Draw small circle/dot at each point
        web.dot(random.uniform(2, 5))
        
        # Draw connecting lines to create web effect
        if i % 3 == 0 and i > 0:
            web.penup()
            web.goto(0, 0)
            web.pendown()
            web.goto(x, y)
            web.penup()
        
        # Draw cross connections between spiral points
        if i % 5 == 0 and i > 10:
            angle2 = angle + math.pi / 3
            r2 = radius * ((i - 5) / loops)
            x2 = r2 * math.cos(angle2)
            y2 = r2 * math.sin(angle2)
            web.penup()
            web.goto(x, y)
            web.pendown()
            web.goto(x2, y2)
            web.penup()

def draw_concentric_web(radius, num_circles, num_spokes):
    """Draw a concentric web pattern with spokes"""
    # Draw concentric circles
    for i in range(num_circles):
        r = radius * (i / num_circles)
        web.penup()
        web.goto(0, -r)
        web.pendown()
        web.color(random.choice(colors))
        web.circle(r)
        
        # Add dots on circles
        for j in range(num_spokes):
            angle = (j / num_spokes) * 2 * math.pi
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            web.penup()
            web.goto(x, y)
            web.pendown()
            web.dot(random.uniform(1, 3))
            web.penup()
    
    # Draw spokes
    for i in range(num_spokes):
        angle = (i / num_spokes) * 2 * math.pi
        web.penup()
        web.goto(0, 0)
        web.pendown()
        web.color(random.choice(colors))
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        web.goto(x, y)
        web.penup()
        
        # Add dots along spokes
        for j in range(10):
            r = radius * (j / 10)
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            web.goto(x, y)
            web.pendown()
            web.dot(random.uniform(1, 2))
            web.penup()

def draw_circular_spiral(radius, revolutions, points_per_rev):
    """Draw a circular spiral with points"""
    total_points = revolutions * points_per_rev
    
    for i in range(total_points):
        # Spiral parameters
        t = i / points_per_rev  # Current revolution
        r = radius * (t / revolutions)  # Radius increases with revolution
        angle = t * 2 * math.pi  # Full rotation
        
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        
        # Color based on position
        color_index = int((t / revolutions) * len(colors))
        web.color(colors[color_index % len(colors)])
        
        # Draw point
        web.penup()
        web.goto(x, y)
        web.pendown()
        
        # Size varies with position
        size = 1 + (t / revolutions) * 3
        web.dot(size)
        
        # Draw connecting spiral line
        if i > 0:
            web.penup()
            prev_x = radius * ((i-1) / points_per_rev / revolutions) * math.cos((i-1) / points_per_rev * 2 * math.pi)
            prev_y = radius * ((i-1) / points_per_rev / revolutions) * math.sin((i-1) / points_per_rev * 2 * math.pi)
            web.goto(prev_x, prev_y)
            web.pendown()
            web.goto(x, y)
            web.penup()

def draw_web_with_pattern():
    """Main function to draw multiple web patterns"""
    
    # Clear screen
    web.clear()
    
    # Draw multiple web patterns
    # 1. Concentric web
    draw_concentric_web(200, 12, 16)
    
    # 2. Spiral web overlay
    web.penup()
    web.goto(0, 0)
    web.pendown()
    draw_spiral_web(180, 3, 80, True)
    
    # 3. Circular spiral
    web.penup()
    web.goto(0, 0)
    web.pendown()
    draw_circular_spiral(150, 4, 50)
    
    # 4. Decorative outer ring
    web.penup()
    web.goto(0, -230)
    web.pendown()
    web.color("#FFFFFF")
    web.width(2)
    web.circle(230)
    web.width(1)
    
    # Add dots on outer ring
    for i in range(36):
        angle = (i / 36) * 2 * math.pi
        x = 230 * math.cos(angle)
        y = 230 * math.sin(angle)
        web.penup()
        web.goto(x, y)
        web.pendown()
        web.color(random.choice(colors))
        web.dot(3)
        web.penup()

def draw_spider_web():
    """Draw a spider web style pattern"""
    # Clear screen
    web.clear()
    
    # Background gradient effect
    for i in range(50, 0, -1):
        r = 10 * i
        web.penup()
        web.goto(0, -r)
        web.pendown()
        web.color(f"#{int(255*(1-i/50)):02x}{int(100*(1-i/50)):02x}{int(200*(1-i/50)):02x}")
        web.circle(r)
    
    # Draw main web
    num_spokes = 24
    num_circles = 20
    
    # Spokes
    for i in range(num_spokes):
        angle = (i / num_spokes) * 2 * math.pi
        web.penup()
        web.goto(0, 0)
        web.pendown()
        web.color(random.choice(colors))
        x = 250 * math.cos(angle)
        y = 250 * math.sin(angle)
        web.goto(x, y)
        web.penup()
    
    # Concentric circles with spiral
    for i in range(num_circles):
        r = 250 * (i / num_circles)
        web.penup()
        web.goto(0, -r)
        web.pendown()
        web.color(colors[i % len(colors)])
        web.circle(r)
        
        # Add decorative dots
        for j in range(num_spokes):
            angle = (j / num_spokes) * 2 * math.pi + (i * 0.1)
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            web.penup()
            web.goto(x, y)
            web.pendown()
            size = 1 + (i / num_circles) * 3
            web.dot(size)
            web.penup()
    
    # Spiral overlay
    web.penup()
    web.goto(0, 0)
    web.pendown()
    for i in range(200):
        angle = i * 0.2
        r = 250 * (i / 200)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        web.color(colors[i % len(colors)])
        web.goto(x, y)
        web.dot(2)
        web.penup()
        web.goto(x, y)
        web.pendown()

# Choose which web to draw
# Option 1: Combined web patterns
draw_web_with_pattern()

# Option 2: Spider web style (uncomment to use)
# draw_spider_web()

# Update screen
screen.update()

# Keep window open
turtle.done()