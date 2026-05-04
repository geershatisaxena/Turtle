import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Rotating Hexagon Spiral - Kaleidoscope Style")
screen.bgcolor("black")
screen.setup(width=1000, height=900)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color schemes
color_schemes = {
    "rainbow": ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"],
    "sunset": ["#FF6B35", "#F7931E", "#FDC830", "#F37335", "#DC2430", "#8E2DE2"],
    "ocean": ["#00B4DB", "#0083B0", "#00C9FF", "#92FE9D", "#00B4DB", "#00A8C5"],
    "fire": ["#FF0000", "#FF4500", "#FF6600", "#FF8800", "#FFAA00", "#FFCC00"],
    "ice": ["#00FFFF", "#00CED1", "#20B2AA", "#48D1CC", "#40E0D0", "#7FFFD4"],
    "purple_haze": ["#8E2DE2", "#4A00E0", "#9D50BB", "#6B3FA0", "#B83B5E", "#E94560"]
}

current_scheme = "rainbow"
hexagon_size = 8
rotation_step = 12
growth_rate = 1.02
spiral_density = 200

def draw_hexagon(x, y, size, angle, color):
    """Draw a single hexagon with outline and fill"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    
    # Draw hexagon using 6 sides
    for _ in range(6):
        pen.forward(size)
        pen.left(60)
    
    pen.end_fill()
    pen.penup()

def draw_rotating_hexagon_spiral_v2():
    """Version 2: Spiral where hexagons are placed along an Archimedean spiral"""
    colors = color_schemes[current_scheme]
    
    for i in range(spiral_density):
        # Archimedean spiral: r = a * theta
        theta = i * 0.3
        radius = i * 0.8
        
        # Calculate position on spiral
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        
        # Size increases with radius
        size = hexagon_size + i * 0.15
        
        # Rotation angle based on position
        rotation = i * 8
        
        # Color cycling
        color = colors[i % len(colors)]
        
        draw_hexagon(x, y, size, rotation, color)
        
        if i % 20 == 0:
            screen.update()

def draw_hexagon_flower():
    """Create a flower-like pattern with rotating hexagon petals"""
    colors = color_schemes[current_scheme]
    
    for i in range(spiral_density):
        angle = i * 15  # 24 flowers in a circle
        radius = i * 1.2
        
        # Position in circle
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        # Size grows with radius
        size = hexagon_size + i * 0.1
        
        # Each hexagon rotates as we go around
        rotation = angle + i * 5
        
        color = colors[i % len(colors)]
        
        draw_hexagon(x, y, size, rotation, color)
        
        if i % 20 == 0:
            screen.update()

def draw_hexagon_tunnel():
    """Create a tunnel effect with rotating hexagons"""
    colors = color_schemes[current_scheme]
    
    for i in range(spiral_density):
        # Create perspective effect
        factor = i / spiral_density
        radius = 300 * (1 - factor)
        angle_offset = i * 25
        
        num_hexagons_per_ring = max(6, int(20 * (1 - factor)))
        
        for j in range(num_hexagons_per_ring):
            angle = 360 / num_hexagons_per_ring * j + angle_offset
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            size = hexagon_size * (1 + factor * 1.5)
            rotation = angle_offset + i * 3 + j * 10
            
            color = colors[(i + j) % len(colors)]
            
            draw_hexagon(x, y, size, rotation, color)
        
        if i % 5 == 0:
            screen.update()

def draw_hexagon_moire():
    """Create moiré pattern with overlapping hexagon spirals"""
    colors = color_schemes[current_scheme]
    
    # Multiple overlapping spirals
    num_spirals = 3
    
    for s in range(num_spirals):
        offset_angle = s * 120  # 120 degrees apart
        
        for i in range(spiral_density):
            theta = i * 0.25 + offset_angle * 0.01
            radius = i * 0.9
            
            x = radius * math.cos(theta + math.radians(offset_angle))
            y = radius * math.sin(theta + math.radians(offset_angle))
            
            size = hexagon_size + i * 0.12
            rotation = theta * 30 + offset_angle
            
            # Different color for each spiral
            spiral_colors = [0, len(colors)//3, 2*len(colors)//3]
            color = colors[(i + spiral_colors[s]) % len(colors)]
            
            draw_hexagon(x, y, size, rotation, color)
            
            if i % 30 == 0:
                screen.update()

def draw_hexagon_mandala():
    """Create a mandala-style rotating hexagon pattern"""
    colors = color_schemes[current_scheme]
    
    for ring in range(15):
        num_hexagons = 6 + ring * 3
        radius = 20 + ring * 18
        size = hexagon_size + ring * 1.2
        
        for i in range(num_hexagons):
            angle = 360 / num_hexagons * i
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            # Light source effect - brighter on one side
            brightness_factor = (math.cos(math.radians(angle)) + 1) / 2
            
            rotation = angle + ring * 15
            color = colors[(ring + i) % len(colors)]
            
            draw_hexagon(x, y, size, rotation, color)
        
        screen.update()

def draw_hexagon_chaos():
    """Randomized but structured chaotic hexagon spiral"""
    colors = color_schemes[current_scheme]
    
    angle = 0
    x, y = 0, 0
    size = hexagon_size
    
    for i in range(spiral_density * 2):
        # Add some randomness to position
        angle += random.uniform(10, 20)
        radius = size * 1.2
        x += math.cos(math.radians(angle)) * radius * 0.8
        y += math.sin(math.radians(angle)) * radius * 0.8
        
        # Random size variation
        current_size = size + random.uniform(-2, 2)
        
        # Rotation based on angle plus random
        rotation = angle + random.uniform(-10, 10)
        
        color = colors[i % len(colors)]
        
        draw_hexagon(x, y, current_size, rotation, color)
        
        size *= 1.02
        
        if i % 15 == 0:
            screen.update()

def draw_hexagon_spiral_art():
    """Artistic spiral with varying opacity and overlapping"""
    colors = color_schemes[current_scheme]
    
    for i in range(spiral_density):
        # Logarithmic spiral
        theta = math.log(i + 1) * 15
        radius = i * 1.5
        
        x = radius * math.cos(math.radians(theta))
        y = radius * math.sin(math.radians(theta))
        
        # Size varies sinusoidally
        size = hexagon_size + math.sin(i * 0.1) * 5 + i * 0.05
        
        # Complex rotation pattern
        rotation = theta + math.sin(i * 0.05) * 30
        
        color = colors[abs(int(math.sin(i * 0.1) * len(colors))) % len(colors)]
        
        draw_hexagon(x, y, size, rotation, color)
        
        if i % 15 == 0:
            screen.update()

# UI and controls
def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 430)
    title.write("🌀 ROTATING HEXAGON SPIRAL - KALEIDOSCOPE 🌀", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -440)
    instructions.write("1=Spiral 2=Flower 3=Tunnel 4=Moire 5=Mandala 6=Chaos 7=Art | S=Color Scheme | R=Redraw | ESC=Exit",
                       align="center", font=("Arial", 9, "normal"))

# Pattern selection
current_pattern = 1
scheme_names = list(color_schemes.keys())

def draw_current_pattern():
    """Draw the currently selected pattern"""
    pen.clear()
    screen.update()
    
    if current_pattern == 1:
        draw_rotating_hexagon_spiral_v2()
    elif current_pattern == 2:
        draw_hexagon_flower()
    elif current_pattern == 3:
        draw_hexagon_tunnel()
    elif current_pattern == 4:
        draw_hexagon_moire()
    elif current_pattern == 5:
        draw_hexagon_mandala()
    elif current_pattern == 6:
        draw_hexagon_chaos()
    elif current_pattern == 7:
        draw_hexagon_spiral_art()
    
    screen.update()

def set_pattern_1():
    global current_pattern
    current_pattern = 1
    draw_current_pattern()

def set_pattern_2():
    global current_pattern
    current_pattern = 2
    draw_current_pattern()

def set_pattern_3():
    global current_pattern
    current_pattern = 3
    draw_current_pattern()

def set_pattern_4():
    global current_pattern
    current_pattern = 4
    draw_current_pattern()

def set_pattern_5():
    global current_pattern
    current_pattern = 5
    draw_current_pattern()

def set_pattern_6():
    global current_pattern
    current_pattern = 6
    draw_current_pattern()

def set_pattern_7():
    global current_pattern
    current_pattern = 7
    draw_current_pattern()

def change_color_scheme():
    """Cycle through color schemes"""
    global current_scheme
    idx = scheme_names.index(current_scheme)
    current_scheme = scheme_names[(idx + 1) % len(scheme_names)]
    draw_current_pattern()

def reset():
    """Redraw current pattern"""
    draw_current_pattern()

# Keyboard bindings
screen.listen()
screen.onkey(set_pattern_1, "1")
screen.onkey(set_pattern_2, "2")
screen.onkey(set_pattern_3, "3")
screen.onkey(set_pattern_4, "4")
screen.onkey(set_pattern_5, "5")
screen.onkey(set_pattern_6, "6")
screen.onkey(set_pattern_7, "7")
screen.onkey(change_color_scheme, "s")
screen.onkey(reset, "r")
screen.onkey(lambda: screen.bye(), "Escape")

# Draw UI
draw_title()

print("=" * 60)
print("     ROTATING HEXAGON SPIRAL - KALEIDOSCOPE EDITION")
print("=" * 60)
print()
print("7 different mesmerizing patterns to explore!")
print()
print("PATTERNS:")
print("  1 - Archimedean Spiral: Classic mathematical spiral")
print("  2 - Flower Pattern: Hexagon flower petals")
print("  3 - Tunnel Effect: Perspective depth illusion")
print("  4 - Moiré Pattern: Overlapping spirals")
print("  5 - Mandala: Sacred geometric ring pattern")
print("  6 - Chaos: Structured randomness")
print("  7 - Art Spiral: Logarithmic art pattern")
print()
print("FEATURES:")
print("  • Each hexagon grows and rotates progressively")
print("  • Multiple color schemes (rainbow, sunset, ocean, etc.)")
print("  • Smooth animation and rendering")
print("  • Unique mathematical formulas for each pattern")
print()
print("CONTROLS:")
print("  1-7 - Select different patterns")
print("  S   - Change color scheme")
print("  R   - Redraw current pattern")
print("  ESC - Exit program")
print()
print("Press 1 to start exploring!")

# Draw initial pattern
draw_rotating_hexagon_spiral_v2()

screen.mainloop()