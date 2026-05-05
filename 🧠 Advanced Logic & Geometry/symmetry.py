import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Radial Symmetry Design - Wheel Pattern")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palettes
color_palettes = {
    "rainbow": ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"],
    "sunset": ["#FF6B35", "#F7931E", "#FDC830", "#F37335", "#DC2430", "#8E2DE2"],
    "ocean": ["#00B4DB", "#0083B0", "#00C9FF", "#92FE9D", "#00B4DB", "#00A8C5"],
    "neon": ["#FF0066", "#00FFCC", "#FFCC00", "#9900FF", "#00FF66", "#FF3300"],
    "pastel": ["#FFB3BA", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#FF9AA2"],
    "royal": ["#800080", "#4B0082", "#9400D3", "#8B008B", "#9932CC", "#BA55D3"],
    "fire": ["#FF0000", "#FF4500", "#FF6600", "#FF8C00", "#FFA500", "#FFD700"],
    "ice": ["#00FFFF", "#00CED1", "#20B2AA", "#48D1CC", "#40E0D0", "#7FFFD4"]
}

current_palette = "rainbow"
spokes = 12
layer_count = 5
rotation_offset = 0

def draw_petal(x, y, size, angle, color, petal_type="normal"):
    """Draw a single petal/pattern element"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    
    if petal_type == "normal":
        # Simple petal shape
        pen.circle(size, 60)
        pen.left(120)
        pen.circle(size, 60)
    elif petal_type == "sharp":
        # Sharp pointed petal
        pen.forward(size)
        pen.left(30)
        pen.forward(size // 2)
        pen.backward(size // 2)
        pen.right(60)
        pen.forward(size // 2)
        pen.backward(size // 2)
        pen.left(30)
        pen.backward(size)
    elif petal_type == "rounded":
        # Rounded petal
        pen.circle(size, 90)
        pen.circle(size, 90)
    elif petal_type == "star":
        # Star-like point
        for _ in range(2):
            pen.forward(size)
            pen.left(45)
            pen.forward(size // 2)
            pen.backward(size // 2)
            pen.right(90)
            pen.forward(size // 2)
            pen.backward(size // 2)
            pen.left(45)
    
    pen.end_fill()
    pen.penup()

def draw_wheel_basic():
    """Basic wheel with spokes and rim"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Draw outer rim
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()
    pen.color(colors[0])
    pen.pensize(4)
    pen.circle(250)
    
    # Draw inner rim
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.color(colors[1])
    pen.pensize(2)
    pen.circle(200)
    
    # Draw spokes
    for i in range(spokes):
        angle = i * (360 / spokes) + rotation_offset
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.pendown()
        pen.color(colors[i % len(colors)])
        pen.pensize(3)
        pen.forward(200)
        pen.penup()
        pen.backward(200)
    
    # Draw center hub
    pen.goto(0, -30)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(colors[-1])
    pen.circle(30)
    pen.end_fill()
    
    screen.update()

def draw_mandala_wheel():
    """Mandala-style wheel with petals around the rim"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Draw radial patterns
    for ring in range(layer_count):
        radius = 50 + ring * 40
        petal_size = 15 + ring * 5
        
        for i in range(spokes * 2):
            angle = i * (360 / (spokes * 2)) + rotation_offset
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            petal_type = ring % 2 == 0 and "normal" or "rounded"
            draw_petal(x, y, petal_size, angle + 90, 
                      colors[(ring + i) % len(colors)], petal_type)
        
        screen.update()
    
    # Draw center
    pen.goto(0, -20)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(colors[-1])
    pen.circle(20)
    pen.end_fill()
    
    screen.update()

def draw_geometric_wheel():
    """Geometric wheel with interlocking shapes"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Draw radiating lines
    for i in range(spokes):
        angle = i * (360 / spokes) + rotation_offset
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.pendown()
        pen.color(colors[i % len(colors)])
        pen.pensize(2)
        pen.forward(250)
        
        # Add small shapes at ends
        x = 250 * math.cos(math.radians(angle))
        y = 250 * math.sin(math.radians(angle))
        
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[(i + 2) % len(colors)])
        for _ in range(4):
            pen.forward(15)
            pen.left(90)
        pen.end_fill()
    
    # Draw connecting arcs
    for i in range(spokes):
        angle1 = i * (360 / spokes)
        angle2 = ((i + 1) % spokes) * (360 / spokes)
        x1 = 180 * math.cos(math.radians(angle1))
        y1 = 180 * math.sin(math.radians(angle1))
        x2 = 180 * math.cos(math.radians(angle2))
        y2 = 180 * math.sin(math.radians(angle2))
        
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.color(colors[i % len(colors)])
        pen.goto(x2, y2)
    
    # Draw center design
    for i in range(12):
        angle = i * 30 + rotation_offset
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[i % len(colors)])
        pen.forward(50)
        pen.left(90)
        pen.forward(15)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
        pen.forward(15)
        pen.end_fill()
    
    screen.update()

def draw_flower_wheel():
    """Flower-like wheel with petals radiating from center"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Outer petals
    for i in range(spokes * 2):
        angle = i * (360 / (spokes * 2)) + rotation_offset
        radius = 220
        
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle + 90)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[i % len(colors)])
        
        # Draw leaf/petal shape
        for _ in range(2):
            pen.circle(30, 60)
            pen.left(120)
            pen.circle(30, 60)
            pen.left(120)
        
        pen.end_fill()
        
        if i % (spokes // 2) == 0:
            screen.update()
    
    # Inner petals
    for i in range(spokes):
        angle = i * (360 / spokes) + rotation_offset
        radius = 120
        
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle + 90)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[(i + 4) % len(colors)])
        
        # Draw inner petals
        pen.circle(40, 120)
        pen.left(120)
        pen.circle(40, 120)
        
        pen.end_fill()
        
        if i % 4 == 0:
            screen.update()
    
    screen.update()

def draw_spiral_wheel():
    """Spiral pattern radiating from center"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    for turn in range(3):
        for i in range(spokes):
            angle = i * (360 / spokes) + rotation_offset + turn * 15
            radius = 60 + turn * 60
            
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            # Draw spiral arms
            pen.penup()
            pen.goto(x, y)
            pen.setheading(angle + 90)
            pen.pendown()
            pen.color(colors[(turn + i) % len(colors)])
            pen.pensize(2)
            
            # Draw spiral segment
            for step in range(8):
                pen.forward(8)
                pen.right(45)
            
            pen.penup()
    
    screen.update()

def draw_radial_lines():
    """Simple but elegant radial line pattern"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Draw multiple layers of radial lines
    for ring in range(1, 6):
        radius = ring * 50
        line_count = spokes * ring
        
        for i in range(line_count):
            angle = i * (360 / line_count) + rotation_offset
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            if ring % 2 == 0:
                # Draw line from center to point
                pen.penup()
                pen.goto(0, 0)
                pen.pendown()
                pen.color(colors[i % len(colors)])
                pen.goto(x, y)
                pen.penup()
            else:
                # Draw point/dot at radius
                pen.goto(x, y)
                pen.dot(5, colors[i % len(colors)])
        
        screen.update()
    
    screen.update()

def draw_aztec_wheel():
    """Aztec calendar inspired wheel design"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Outer ring
    pen.penup()
    pen.goto(0, -260)
    pen.pendown()
    pen.color(colors[0])
    pen.pensize(5)
    pen.circle(260)
    
    # Decorative outer ring
    for i in range(spokes * 3):
        angle = i * (360 / (spokes * 3)) + rotation_offset
        x = 240 * math.cos(math.radians(angle))
        y = 240 * math.sin(math.radians(angle))
        pen.penup()
        pen.goto(x, y)
        pen.dot(4, colors[i % len(colors)])
    
    # Middle ring - square pattern
    for i in range(spokes):
        angle = i * (360 / spokes) + rotation_offset
        x1 = 180 * math.cos(math.radians(angle))
        y1 = 180 * math.sin(math.radians(angle))
        x2 = 180 * math.cos(math.radians(angle + 360/spokes))
        y2 = 180 * math.sin(math.radians(angle + 360/spokes))
        
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.color(colors[i % len(colors)])
        pen.goto(x2, y2)
    
    # Inner symbols
    for i in range(8):
        angle = i * 45 + rotation_offset
        x = 100 * math.cos(math.radians(angle))
        y = 100 * math.sin(math.radians(angle))
        
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle + 90)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[(i + 2) % len(colors)])
        
        # Draw diamond shape
        for _ in range(4):
            pen.forward(20)
            pen.left(90)
        
        pen.end_fill()
    
    screen.update()

def draw_gears_wheel():
    """Gear/mechanical wheel design"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    # Outer gear teeth
    for i in range(spokes * 2):
        angle = i * (360 / (spokes * 2)) + rotation_offset
        x = 230 * math.cos(math.radians(angle))
        y = 230 * math.sin(math.radians(angle))
        
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle + 90)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[i % len(colors)])
        
        # Draw gear tooth
        pen.forward(20)
        pen.left(90)
        pen.forward(10)
        pen.left(90)
        pen.forward(20)
        pen.left(90)
        pen.forward(10)
        
        pen.end_fill()
    
    # Middle ring
    pen.penup()
    pen.goto(0, -180)
    pen.pendown()
    pen.color(colors[1])
    pen.pensize(8)
    pen.circle(180)
    
    # Inner spokes
    for i in range(spokes):
        angle = i * (360 / spokes) + rotation_offset
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.pendown()
        pen.color(colors[i % len(colors)])
        pen.pensize(4)
        pen.forward(180)
    
    # Center bolt
    pen.penup()
    pen.goto(0, -40)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(colors[-1])
    pen.circle(40)
    pen.end_fill()
    
    screen.update()

# UI Controls
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 470)
    title.write("⚙️ RADIAL SYMMETRY DESIGN - WHEEL PATTERNS ⚙️", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -480)
    instructions.write("1=Basic 2=Mandala 3=Geometric 4=Flower 5=Spiral 6=Radial 7=Aztec 8=Gears | S=Color | +/-=Spokes | []=Layers | R=Rotate | ESC=Exit",
                       align="center", font=("Arial", 8, "normal"))

current_design = 1

def draw_current():
    pen.clear()
    screen.update()
    
    if current_design == 1:
        draw_wheel_basic()
    elif current_design == 2:
        draw_mandala_wheel()
    elif current_design == 3:
        draw_geometric_wheel()
    elif current_design == 4:
        draw_flower_wheel()
    elif current_design == 5:
        draw_spiral_wheel()
    elif current_design == 6:
        draw_radial_lines()
    elif current_design == 7:
        draw_aztec_wheel()
    elif current_design == 8:
        draw_gears_wheel()
    
    screen.update()

def set_design_1(): global current_design; current_design = 1; draw_current()
def set_design_2(): global current_design; current_design = 2; draw_current()
def set_design_3(): global current_design; current_design = 3; draw_current()
def set_design_4(): global current_design; current_design = 4; draw_current()
def set_design_5(): global current_design; current_design = 5; draw_current()
def set_design_6(): global current_design; current_design = 6; draw_current()
def set_design_7(): global current_design; current_design = 7; draw_current()
def set_design_8(): global current_design; current_design = 8; draw_current()

def change_color():
    global current_palette
    palettes = list(color_palettes.keys())
    idx = palettes.index(current_palette)
    current_palette = palettes[(idx + 1) % len(palettes)]
    draw_current()

def increase_spokes():
    global spokes
    spokes = min(spokes + 2, 36)
    draw_current()

def decrease_spokes():
    global spokes
    spokes = max(spokes - 2, 6)
    draw_current()

def increase_layers():
    global layer_count
    layer_count = min(layer_count + 1, 8)
    draw_current()

def decrease_layers():
    global layer_count
    layer_count = max(layer_count - 1, 2)
    draw_current()

def rotate():
    global rotation_offset
    rotation_offset = (rotation_offset + 5) % 360
    draw_current()

def reset():
    global rotation_offset, spokes, layer_count
    rotation_offset = 0
    spokes = 12
    layer_count = 5
    draw_current()

screen.listen()
screen.onkey(set_design_1, "1")
screen.onkey(set_design_2, "2")
screen.onkey(set_design_3, "3")
screen.onkey(set_design_4, "4")
screen.onkey(set_design_5, "5")
screen.onkey(set_design_6, "6")
screen.onkey(set_design_7, "7")
screen.onkey(set_design_8, "8")
screen.onkey(change_color, "s")
screen.onkey(increase_spokes, "plus")
screen.onkey(increase_spokes, "equal")
screen.onkey(decrease_spokes, "minus")
screen.onkey(increase_layers, "bracketright")
screen.onkey(decrease_layers, "bracketleft")
screen.onkey(rotate, "r")
screen.onkey(reset, "R")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("     RADIAL SYMMETRY DESIGN - WHEEL PATTERNS")
print("=" * 60)
print()
print("Beautiful wheel-like patterns with perfect radial symmetry!")
print()
print("DESIGNS:")
print("  1 - Basic Wheel: Classic spokes and rims")
print("  2 - Mandala Wheel: Intricate petal patterns")
print("  3 - Geometric Wheel: Interlocking shapes")
print("  4 - Flower Wheel: Blooming flower design")
print("  5 - Spiral Wheel: Spiraling concentric arms")
print("  6 - Radial Lines: Minimalist line pattern")
print("  7 - Aztec Wheel: Calendar-inspired design")
print("  8 - Gears Wheel: Mechanical gear pattern")
print()
print("CONTROLS:")
print("  1-8   - Select wheel design")
print("  S     - Change color scheme")
print("  +/-   - Increase/Decrease number of spokes")
print("  [/]   - Increase/Decrease layers")
print("  R     - Rotate pattern")
print("  Shift-R - Reset to default")
print("  ESC   - Exit")
print()
print("Radial symmetry creates perfect balance and harmony!")

draw_wheel_basic()
screen.mainloop()