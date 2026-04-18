import turtle
import time
import math
import random

# Setup
turtle.setup(1200, 900)
turtle.bgcolor("#0a0a2a")  # Deep space blue
turtle.speed(0)
turtle.tracer(0)

# Rainbow color palette for different polygons
rainbow_colors = [
    "#FF0000",  # Red
    "#FF7F00",  # Orange
    "#FFFF00",  # Yellow
    "#00FF00",  # Green
    "#0000FF",  # Blue
    "#4B0082",  # Indigo
    "#9400D3",  # Violet
    "#FF1493"   # Deep Pink
]

# Gradient colors for filling (light and dark versions)
gradient_colors = [
    ["#FF6666", "#CC0000"],  # Red gradient
    ["#FFAA66", "#CC5500"],  # Orange gradient
    ["#FFFF66", "#CCCC00"],  # Yellow gradient
    ["#66FF66", "#00CC00"],  # Green gradient
    ["#6666FF", "#0000CC"],  # Blue gradient
    ["#9B59B6", "#3B0066"],  # Indigo gradient
    ["#D580FF", "#7B00A3"],  # Violet gradient
    ["#FF69B4", "#CC0066"]   # Pink gradient
]

# Settings
base_radius = 100
center_x = 0
center_y = 0

# Layout: 2 rows x 4 columns
positions = [
    (-400, 250),   # Triangle
    (-133, 250),   # Square
    (133, 250),    # Pentagon
    (400, 250),    # Hexagon
    (-400, -50),   # Heptagon
    (-133, -50),   # Octagon
    (133, -50),    # Nonagon
    (400, -50)     # Decagon
]

# Function to draw a star pattern inside polygon
def draw_inner_pattern(x, y, sides, radius, color):
    pattern_turtle = turtle.Turtle()
    pattern_turtle.hideturtle()
    pattern_turtle.penup()
    pattern_turtle.speed(0)
    
    # Draw inner star
    pattern_turtle.goto(x, y - radius//2)
    pattern_turtle.color(color)
    pattern_turtle.pensize(2)
    pattern_turtle.pendown()
    
    angle = 360 / sides
    for i in range(sides):
        pattern_turtle.forward(radius//3)
        pattern_turtle.right(180 - angle)
        pattern_turtle.forward(radius//3)
        pattern_turtle.left(180 - angle)
    
    pattern_turtle.penup()

# Function to draw decorative dots on vertices
def draw_vertex_dots(x, y, sides, radius, color):
    dot_turtle = turtle.Turtle()
    dot_turtle.hideturtle()
    dot_turtle.penup()
    dot_turtle.speed(0)
    
    for i in range(sides):
        angle = 360 / sides * i - 90
        vx = x + radius * math.cos(math.radians(angle))
        vy = y + radius * math.sin(math.radians(angle))
        dot_turtle.goto(vx, vy)
        dot_turtle.dot(10, color)
        turtle.update()
        time.sleep(0.02)

# Function to draw polygon outline with glow effect
def draw_glow_effect(vertices, color):
    glow_turtle = turtle.Turtle()
    glow_turtle.hideturtle()
    glow_turtle.penup()
    glow_turtle.pensize(6)
    
    # Draw multiple layers for glow effect
    for layer in range(3, 0, -1):
        glow_turtle.clear()
        glow_turtle.goto(vertices[0])
        glow_turtle.pendown()
        
        # Lighter color for glow
        glow_turtle.color(color)
        glow_turtle.pensize(layer * 2)
        
        for i in range(len(vertices) + 1):
            glow_turtle.goto(vertices[i % len(vertices)])
        glow_turtle.penup()
        turtle.update()
        time.sleep(0.03)

# Enhanced polygon drawing with animation and effects
def draw_polygon_enhanced(sides, color, gradient, position, delay=0.008):
    x, y = position
    
    # Calculate vertices
    angle = 360 / sides
    start_angle = -90
    
    vertices = []
    for i in range(sides):
        current_angle = start_angle + i * angle
        vx = x + base_radius * math.cos(math.radians(current_angle))
        vy = y + base_radius * math.sin(math.radians(current_angle))
        vertices.append((vx, vy))
    
    # Draw glow effect first
    draw_glow_effect(vertices, color)
    
    # Main polygon drawing with animation
    draw_turtle = turtle.Turtle()
    draw_turtle.hideturtle()
    draw_turtle.speed(0)
    draw_turtle.penup()
    draw_turtle.goto(vertices[0])
    draw_turtle.pendown()
    draw_turtle.color(color)
    draw_turtle.pensize(3)
    draw_turtle.fillcolor(gradient[0])
    draw_turtle.begin_fill()
    
    # Animate drawing each side
    for i in range(sides + 1):
        target = vertices[i % sides]
        current = draw_turtle.position()
        
        # Draw side in small segments
        steps = 40
        for step in range(steps + 1):
            t = step / steps
            draw_x = current[0] + t * (target[0] - current[0])
            draw_y = current[1] + t * (target[1] - current[1])
            draw_turtle.goto(draw_x, draw_y)
            turtle.update()
            time.sleep(delay / steps)
    
    draw_turtle.end_fill()
    return vertices

# Function to draw spinning rings around polygon
def draw_spinning_rings(x, y, sides, color):
    ring_turtle = turtle.Turtle()
    ring_turtle.hideturtle()
    ring_turtle.penup()
    ring_turtle.speed(0)
    
    for ring in range(2):
        radius_offset = base_radius + 15 + ring * 12
        ring_turtle.goto(x + radius_offset, y)
        ring_turtle.pendown()
        ring_turtle.color(color)
        ring_turtle.pensize(2)
        
        # Draw dashed circle
        for angle in range(0, 360, 10):
            rad = math.radians(angle)
            rx = x + radius_offset * math.cos(rad)
            ry = y + radius_offset * math.sin(rad)
            ring_turtle.goto(rx, ry)
            turtle.update()
            time.sleep(0.003)
        
        ring_turtle.penup()

# Function to draw polygon name with effects
def draw_fancy_label(sides, position, color):
    x, y = position
    names = {
        3: "TRIANGLE", 4: "SQUARE", 5: "PENTAGON",
        6: "HEXAGON", 7: "HEPTAGON", 8: "OCTAGON",
        9: "NONAGON", 10: "DECAGON"
    }
    
    label_turtle = turtle.Turtle()
    label_turtle.hideturtle()
    label_turtle.penup()
    label_turtle.speed(0)
    
    # Animated label appearance
    for size in range(5, 15, 2):
        label_turtle.clear()
        label_turtle.goto(x, y - base_radius - 40)
        label_turtle.color(color)
        label_turtle.write(f"{sides} - {names[sides]}", 
                          align="center", 
                          font=("Arial", size, "bold"))
        turtle.update()
        time.sleep(0.03)
    
    # Add side count in a circle
    label_turtle.goto(x, y - base_radius - 65)
    label_turtle.color("#FFD700")
    label_turtle.write(f"{sides} sides", 
                      align="center", 
                      font=("Arial", 10, "italic"))

# Function to draw decorative border
def draw_decorative_border():
    border = turtle.Turtle()
    border.hideturtle()
    border.penup()
    border.speed(0)
    border.goto(-550, -400)
    border.pendown()
    border.color("#FFD700")
    border.pensize(3)
    
    # Draw border with animation
    for step in range(4):
        for _ in range(50):
            border.forward(22)
            turtle.update()
            time.sleep(0.005)
        border.right(90)
    
    # Corner decorations
    corners = [(-550, -400), (550, -400), (550, 400), (-550, 400)]
    for cx, cy in corners:
        border.penup()
        border.goto(cx, cy)
        border.pendown()
        border.color("#FF69B4")
        for _ in range(4):
            border.forward(15)
            border.backward(15)
            border.right(90)

# Function to draw connecting rainbow lines
def draw_rainbow_connection(pos1, pos2, y_offset):
    connector = turtle.Turtle()
    connector.hideturtle()
    connector.penup()
    connector.pensize(4)
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    connector.goto(x1, y1 + y_offset)
    connector.pendown()
    
    # Animate rainbow connection
    for step in range(51):
        t = step / 50
        draw_x = x1 + t * (x2 - x1)
        draw_y = (y1 + y_offset) + t * ((y2 + y_offset) - (y1 + y_offset))
        connector.goto(draw_x, draw_y)
        
        # Rainbow color transition
        r = int(255 * (1 - t))
        g = int(255 * t)
        b = int(100 + 155 * (1 - abs(t - 0.5) * 2))
        connector.color(f"#{r:02x}{g:02x}{b:02x}")
        turtle.update()
        time.sleep(0.008)
    
    connector.penup()

# --- MAIN DRAWING SEQUENCE ---

# Animated title with sparkles
title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.penup()

for size in range(10, 35, 3):
    title_turtle.clear()
    title_turtle.goto(0, 420)
    title_turtle.color("#FFD700")
    title_turtle.write("🌈 POLYGON MASTERPIECE 🌈", 
                      align="center", 
                      font=("Arial", size, "bold", "italic"))
    turtle.update()
    time.sleep(0.05)

title_turtle.goto(0, 420)
title_turtle.write("🌈 POLYGON MASTERPIECE 🌈", 
                  align="center", 
                  font=("Arial", 30, "bold", "italic"))

# Subtitle
title_turtle.goto(0, 375)
title_turtle.color("#4ECDC4")
title_turtle.write("From Triangle to Decagon | 3 - 10 Sides", 
                  align="center", 
                  font=("Arial", 16, "italic"))
turtle.update()
time.sleep(0.5)

# Draw decorative border
draw_decorative_border()

# Draw all polygons
polygon_data = []

for i, sides in enumerate(range(3, 11)):
    color = rainbow_colors[i % len(rainbow_colors)]
    gradient = gradient_colors[i % len(gradient_colors)]
    position = positions[i]
    x, y = position
    
    # Draw polygon with animation
    vertices = draw_polygon_enhanced(sides, color, gradient, position, delay=0.006)
    polygon_data.append((vertices, position))
    
    # Add inner star pattern
    draw_inner_pattern(x, y, sides, base_radius, "#FFD700")
    
    # Add vertex dots
    draw_vertex_dots(x, y, sides, base_radius, "#FFFFFF")
    
    # Add spinning rings
    draw_spinning_rings(x, y, sides, color)
    
    # Add fancy label
    draw_fancy_label(sides, position, color)
    
    # Small pause between polygons
    time.sleep(0.4)

# Draw rainbow connections between polygons
for i in range(len(positions) - 1):
    draw_rainbow_connection(positions[i], positions[i + 1], -base_radius - 80)

# Add floating particles/starfield
particle_turtle = turtle.Turtle()
particle_turtle.hideturtle()
particle_turtle.speed(0)

particles = []
for _ in range(60):
    px = random.randint(-550, 550)
    py = random.randint(-400, 450)
    symbols = ["●", "○", "◆", "★", "☆", "✨"]
    particles.append((px, py, random.choice(symbols), random.choice(rainbow_colors)))

for px, py, symbol, col in particles:
    particle_turtle.goto(px, py)
    particle_turtle.color(col)
    particle_turtle.write(symbol, align="center", font=("Arial", random.randint(8, 14)))
    turtle.update()
    time.sleep(0.01)

# Fun facts panel
fact_turtle = turtle.Turtle()
fact_turtle.hideturtle()
fact_turtle.penup()

facts = [
    "📐 Triangle: Strongest geometric shape, 60° each angle",
    "⬛ Square: 4 right angles (90° each), perfect symmetry",
    "⭐ Pentagon: Found in nature (starfish, okra)",
    "🍯 Hexagon: Honeycomb efficiency, 120° angles",
    "🎯 Heptagon: 7 sides, ~128.6° interior angle",
    "🛑 Octagon: Stop sign shape, 135° interior angle",
    "🌀 Nonagon: 9 sides, 140° interior angle",
    "⚙️ Decagon: 10 sides, 144° interior angle"
]

for i, fact in enumerate(facts):
    fact_turtle.goto(-580, -350 + i * 28)
    fact_turtle.color("#96CEB4")
    fact_turtle.write(fact, font=("Arial", 11, "normal"))
    turtle.update()
    time.sleep(0.08)

# Formula display with animation
formula_turtle = turtle.Turtle()
formula_turtle.hideturtle()
formula_turtle.penup()

for size in range(8, 15, 2):
    formula_turtle.clear()
    formula_turtle.goto(200, -380)
    formula_turtle.color("#FFD700")
    formula_turtle.write("Formula: Interior Angle = (n-2) × 180° ÷ n", 
                        align="center", 
                        font=("Arial", size, "bold"))
    turtle.update()
    time.sleep(0.05)

# --- Final animation: rotating stars around polygons ---
star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.speed(0)

for rotation in range(36):
    star_turtle.clear()
    for i, (x, y) in enumerate(positions):
        angle = rotation * 10
        rad = math.radians(angle + i * 45)
        offset_x = 18 * math.cos(rad)
        offset_y = 18 * math.sin(rad)
        star_turtle.goto(x + offset_x, y + base_radius + 25)
        star_turtle.color(rainbow_colors[i % len(rainbow_colors)])
        star_turtle.write("★", align="center", font=("Arial", 18))
    turtle.update()
    time.sleep(0.04)

# Final sparkle burst
for _ in range(30):
    sparkle = turtle.Turtle()
    sparkle.hideturtle()
    sparkle.penup()
    rx = random.randint(-500, 500)
    ry = random.randint(-350, 400)
    sparkle.goto(rx, ry)
    sparkle.color(random.choice(rainbow_colors))
    sparkle.write("✨", align="center", font=("Arial", random.randint(10, 20)))
    turtle.update()
    time.sleep(0.02)

# --- Finish ---
turtle.hideturtle()
turtle.update()
time.sleep(3)
turtle.done()