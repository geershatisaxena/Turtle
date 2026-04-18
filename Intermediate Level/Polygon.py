import turtle
import time
import math

# Setup
turtle.setup(900, 800)
turtle.bgcolor("#1a1a2e")  # Dark elegant background
turtle.speed(0)
turtle.tracer(0)

# Color palette for different polygons
colors = [
    "#FF6B6B",  # Triangle - Red
    "#4ECDC4",  # Square - Teal
    "#45B7D1",  # Pentagon - Blue
    "#96CEB4",  # Hexagon - Green
    "#FFEAA7",  # Heptagon - Yellow
    "#DDA0DD",  # Octagon - Plum
    "#F39C12",  # Nonagon - Orange
    "#9B59B6"   # Decagon - Purple
]

# Settings
radius = 120  # Distance from center to vertices
center_x = 0
center_y = 0

# Function to draw a polygon with animation
def draw_polygon_animated(sides, color, position_offset, delay=0.02):
    """Draw a single polygon with animated sides"""
    turtle.penup()
    
    # Calculate starting position
    x = center_x + position_offset[0]
    y = center_y + position_offset[1]
    
    # Calculate angle between vertices
    angle = 360 / sides
    
    # Calculate first vertex position
    start_angle = -90  # Start at top (like a clock face)
    start_x = x + radius * math.cos(math.radians(start_angle))
    start_y = y + radius * math.sin(math.radians(start_angle))
    
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(3)
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    # Animate drawing each side
    for side in range(sides):
        current_angle = start_angle + (side + 1) * angle
        next_x = x + radius * math.cos(math.radians(current_angle))
        next_y = y + radius * math.sin(math.radians(current_angle))
        
        # Draw one side in small steps
        steps = 30
        for step in range(steps + 1):
            t = step / steps
            draw_x = start_x + t * (next_x - start_x)
            draw_y = start_y + t * (next_y - start_y)
            turtle.goto(draw_x, draw_y)
            turtle.update()
            time.sleep(delay / steps)
        
        start_x, start_y = next_x, next_y
    
    turtle.end_fill()
    turtle.penup()

# Function to draw polygon label
def draw_label(sides, position_offset, color):
    """Draw the polygon name below each shape"""
    label_turtle = turtle.Turtle()
    label_turtle.hideturtle()
    label_turtle.penup()
    label_turtle.speed(0)
    
    # Polygon names
    names = {
        3: "Triangle",
        4: "Square",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon"
    }
    
    x = center_x + position_offset[0]
    y = center_y + position_offset[1] - radius - 40
    
    label_turtle.goto(x, y)
    label_turtle.color(color)
    label_turtle.write(f"{sides} - {names[sides]}", 
                       align="center", 
                       font=("Arial", 12, "bold"))
    turtle.update()

# Layout positions (grid: 2 rows x 4 columns)
positions = [
    (-300, 150),   # Row 1, Col 1 - Triangle
    (-100, 150),   # Row 1, Col 2 - Square
    (100, 150),    # Row 1, Col 3 - Pentagon
    (300, 150),    # Row 1, Col 4 - Hexagon
    (-300, -150),  # Row 2, Col 1 - Heptagon
    (-100, -150),  # Row 2, Col 2 - Octagon
    (100, -150),   # Row 2, Col 3 - Nonagon
    (300, -150)    # Row 2, Col 4 - Decagon
]

# --- Draw title (animated) ---
title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.penup()
title_turtle.speed(0)

for size in range(10, 25, 3):
    title_turtle.clear()
    title_turtle.goto(0, 320)
    title_turtle.color("#FFEAA7")
    title_turtle.write("POLYGON GALLERY", 
                       align="center", 
                       font=("Arial", size, "bold"))
    turtle.update()
    time.sleep(0.05)

title_turtle.goto(0, 320)
title_turtle.write("POLYGON GALLERY", 
                   align="center", 
                   font=("Arial", 22, "bold"))

# Subtitle
title_turtle.goto(0, 285)
title_turtle.color("#4ECDC4")
title_turtle.write("3 to 10 sides", 
                   align="center", 
                   font=("Arial", 14, "italic"))
turtle.update()

# --- Draw all polygons in a loop ---
for i, sides in enumerate(range(3, 11)):  # 3 to 10 sides
    color = colors[i % len(colors)]
    position = positions[i]
    
    # Animate drawing the polygon
    draw_polygon_animated(sides, color, position, delay=0.03)
    
    # Add label below it
    draw_label(sides, position, color)
    
    # Small pause between polygons
    time.sleep(0.3)

# --- Draw connecting lines to show progression ---
line_turtle = turtle.Turtle()
line_turtle.hideturtle()
line_turtle.penup()
line_turtle.color("#FFEAA7")
line_turtle.pensize(2)

# Connect shapes in order
for i in range(len(positions) - 1):
    x1 = positions[i][0]
    y1 = positions[i][1] - radius - 20
    x2 = positions[i + 1][0]
    y2 = positions[i + 1][1] - radius - 20
    
    line_turtle.goto(x1, y1)
    line_turtle.pendown()
    
    # Animate the connecting line
    steps = 20
    for step in range(steps + 1):
        t = step / steps
        draw_x = x1 + t * (x2 - x1)
        draw_y = y1 + t * (y2 - y1)
        line_turtle.goto(draw_x, draw_y)
        turtle.update()
        time.sleep(0.01)
    
    line_turtle.penup()

# --- Add fun facts about polygons ---
fact_turtle = turtle.Turtle()
fact_turtle.hideturtle()
fact_turtle.penup()
fact_turtle.speed(0)

facts = [
    "Triangle: Strongest shape",
    "Square: 4 equal sides",
    "Pentagon: 5 sides",
    "Hexagon: Honeycomb shape",
    "Heptagon: 7 sides",
    "Octagon: Stop sign shape",
    "Nonagon: 9 sides",
    "Decagon: 10 sides"
]

for i, fact in enumerate(facts):
    fact_turtle.goto(-400, -320 + i * 25)
    fact_turtle.color("#96CEB4")
    fact_turtle.write(fact, font=("Arial", 10, "normal"))
    turtle.update()
    time.sleep(0.1)

# --- Finish ---
turtle.hideturtle()
turtle.update()
turtle.done()