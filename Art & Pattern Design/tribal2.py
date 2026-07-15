import turtle
import math
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a0a0a")  # Dark earthy background
screen.title("Tribal Art Pattern")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create turtle
tribal = turtle.Turtle()
tribal.speed(0)
tribal.hideturtle()

# Tribal color palette
colors = {
    'earth': '#8B4513',
    'dark_earth': '#5C2E0E',
    'red': '#8B0000',
    'dark_red': '#4A0000',
    'gold': '#DAA520',
    'dark_gold': '#B8860B',
    'white': '#F5F5DC',
    'cream': '#FFF8DC',
    'brown': '#6B3A2A',
    'black': '#1A0A00'
}

def draw_tribal_arc(radius, extent, direction=1):
    """Draw a tribal-style arc"""
    tribal.circle(radius * direction, extent)

def draw_tribal_petal(size, angle, color):
    """Draw a tribal-style petal/leaf"""
    tribal.color(color)
    tribal.begin_fill()
    
    # Draw petal shape
    for _ in range(2):
        tribal.circle(size, angle)
        tribal.left(180 - angle)
        tribal.circle(size, angle)
        tribal.left(180 - angle)
    
    tribal.end_fill()

def draw_tribal_spiral(size, turns, color):
    """Draw a tribal spiral"""
    tribal.color(color)
    tribal.penup()
    tribal.goto(0, 0)
    tribal.pendown()
    
    for i in range(int(turns * 36)):
        t = i / 36
        radius = size * (t / turns)
        angle = t * 2 * math.pi
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        tribal.goto(x, y)

def draw_tribal_triangle(size, color):
    """Draw a tribal triangle"""
    tribal.color(color)
    tribal.begin_fill()
    for _ in range(3):
        tribal.forward(size)
        tribal.left(120)
    tribal.end_fill()

def draw_tribal_pattern(radius, num_elements):
    """Draw a symmetrical tribal pattern"""
    
    # Draw outer circle
    tribal.penup()
    tribal.goto(0, -radius)
    tribal.pendown()
    tribal.color(colors['gold'])
    tribal.width(3)
    tribal.circle(radius)
    tribal.width(1)
    
    # Draw inner circles
    for i in range(3):
        r = radius * (1 - (i + 1) * 0.15)
        tribal.penup()
        tribal.goto(0, -r)
        tribal.pendown()
        tribal.color(colors['dark_gold'])
        tribal.width(2)
        tribal.circle(r)
        tribal.width(1)
    
    # Draw radial symmetry elements
    for i in range(num_elements):
        angle = (i / num_elements) * 360
        
        tribal.penup()
        tribal.goto(0, 0)
        tribal.setheading(angle)
        
        # Draw main tribal element (spoke)
        tribal.color(colors['red'])
        tribal.pendown()
        tribal.forward(radius * 0.7)
        tribal.penup()
        tribal.backward(radius * 0.7)
        
        # Draw tribal petal at end of spoke
        tribal.forward(radius * 0.7)
        tribal.pendown()
        draw_tribal_petal(radius * 0.12, 60, colors['dark_red'])
        tribal.penup()
        tribal.backward(radius * 0.7)
        
        # Draw small decorative elements
        for j in range(3):
            pos = radius * (0.3 + j * 0.2)
            tribal.forward(pos)
            tribal.pendown()
            
            # Draw small triangles
            tribal.right(30)
            draw_tribal_triangle(pos * 0.1, colors['gold'])
            tribal.left(30)
            
            tribal.penup()
            tribal.backward(pos)
    
    # Draw tribal spirals between spokes
    for i in range(num_elements):
        angle = (i / num_elements) * 360 + 180 / num_elements
        tribal.penup()
        tribal.goto(0, 0)
        tribal.setheading(angle)
        tribal.forward(radius * 0.5)
        tribal.pendown()
        
        draw_tribal_spiral(radius * 0.15, 1.5, colors['white'])
        tribal.penup()

def draw_tribal_mask(radius):
    """Draw a tribal mask pattern"""
    
    # Draw mask outline
    tribal.penup()
    tribal.goto(0, radius)
    tribal.pendown()
    tribal.color(colors['earth'])
    tribal.begin_fill()
    
    # Draw face shape
    for i in range(36):
        angle = (i / 36) * 360
        r = radius * (1 + 0.2 * math.sin(angle * 3))
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        tribal.goto(x, y)
    
    tribal.end_fill()
    
    # Draw eyes (symmetrical)
    for side in [-1, 1]:
        tribal.penup()
        tribal.goto(side * radius * 0.3, radius * 0.2)
        tribal.pendown()
        tribal.color(colors['white'])
        tribal.begin_fill()
        tribal.circle(radius * 0.12)
        tribal.end_fill()
        
        # Pupil
        tribal.penup()
        tribal.goto(side * radius * 0.35, radius * 0.2)
        tribal.pendown()
        tribal.color(colors['black'])
        tribal.begin_fill()
        tribal.circle(radius * 0.05)
        tribal.end_fill()
    
    # Draw mouth
    tribal.penup()
    tribal.goto(-radius * 0.3, -radius * 0.2)
    tribal.pendown()
    tribal.color(colors['dark_red'])
    tribal.width(3)
    for i in range(12):
        angle = (i / 12) * 180
        x = -radius * 0.3 + (radius * 0.6 / 12) * i
        y = -radius * 0.2 - radius * 0.1 * math.sin(math.radians(angle))
        tribal.goto(x, y)
    tribal.width(1)
    
    # Draw tribal markings
    for i in range(8):
        angle = (i / 8) * 360 + 22.5
        tribal.penup()
        tribal.goto(0, 0)
        tribal.setheading(angle)
        tribal.forward(radius * 0.7)
        tribal.pendown()
        
        # Draw zigzag pattern
        tribal.color(colors['gold'])
        for j in range(5):
            if j % 2 == 0:
                tribal.right(30)
            else:
                tribal.left(60)
            tribal.forward(radius * 0.08)
        
        tribal.penup()

def draw_tribal_mandala(radius, layers):
    """Draw a tribal mandala pattern"""
    
    # Draw multiple layers of symmetry
    for layer in range(layers):
        r = radius * (1 - layer * 0.15)
        elements = 8 + layer * 4
        
        for i in range(elements):
            angle = (i / elements) * 360 + layer * 5
            
            tribal.penup()
            tribal.goto(0, 0)
            tribal.setheading(angle)
            tribal.forward(r * 0.3)
            tribal.pendown()
            
            # Draw layer-specific elements
            if layer % 3 == 0:
                draw_tribal_petal(r * 0.15, 40, colors['red'])
            elif layer % 3 == 1:
                draw_tribal_triangle(r * 0.15, colors['gold'])
            else:
                tribal.color(colors['dark_red'])
                tribal.begin_fill()
                tribal.circle(r * 0.1, 90)
                tribal.left(90)
                tribal.circle(r * 0.1, 90)
                tribal.left(90)
                tribal.circle(r * 0.1, 90)
                tribal.left(90)
                tribal.circle(r * 0.1, 90)
                tribal.end_fill()
            
            tribal.penup()

def draw_combined_tribal_art():
    """Combine all tribal elements into one artwork"""
    
    # Clear and setup
    tribal.clear()
    tribal.penup()
    tribal.goto(0, 0)
    
    # Draw outer decorative border
    for i in range(36):
        angle = i * 10
        tribal.penup()
        tribal.goto(0, 0)
        tribal.setheading(angle)
        tribal.forward(290)
        tribal.pendown()
        tribal.color(colors['gold'])
        tribal.dot(3)
        tribal.penup()
    
    # Draw main tribal pattern
    draw_tribal_pattern(280, 12)
    
    # Draw mandala in center
    draw_tribal_mandala(180, 4)
    
    # Draw mask overlay
    draw_tribal_mask(120)
    
    # Add decorative dots
    for i in range(24):
        angle = i * 15
        tribal.penup()
        tribal.goto(0, 0)
        tribal.setheading(angle)
        tribal.forward(300)
        tribal.pendown()
        tribal.color(colors['white'])
        tribal.dot(5)
        tribal.penup()
        
        tribal.setheading(angle + 7.5)
        tribal.forward(280)
        tribal.pendown()
        tribal.color(colors['gold'])
        tribal.dot(3)
        tribal.penup()

# Draw the tribal art
print("Drawing tribal art pattern...")
draw_combined_tribal_art()

# Update screen
screen.update()

# Keep window open
turtle.done()