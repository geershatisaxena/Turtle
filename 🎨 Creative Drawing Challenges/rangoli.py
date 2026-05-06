import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Colorful Rangoli Pattern")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palettes for rangoli
color_palettes = {
    "traditional": ["#FF0000", "#FF6600", "#FFD700", "#006400", "#0000FF", "#800080", "#FF1493"],
    "festive": ["#FF4500", "#FF8C00", "#FFD700", "#32CD32", "#00CED1", "#9400D3", "#FF69B4"],
    "diwali": ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#00BFFF", "#FF00FF", "#FFD700"],
    "pastel": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#D4BAFF", "#FFBAE1"],
    "jewel": ["#E63946", "#F4A261", "#E9C46A", "#2A9D8F", "#287271", "#8ECAE6", "#8338EC"],
    "peacock": ["#0047AB", "#008080", "#FFD700", "#00FF7F", "#FF69B4", "#8B00FF", "#DC143C"]
}

current_palette = "traditional"
petal_count = 8
size_multiplier = 1.0

def draw_petal(x, y, radius, angle, color, fill=True):
    """Draw a single petal/leaf shape"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.color(color)
    pen.pendown()
    
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    # Draw a petal using two arcs
    for _ in range(2):
        pen.circle(radius, 60)
        pen.left(120)
        pen.circle(radius, 60)
        pen.left(120)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_petal_simple(x, y, length, width, angle, color):
    """Draw a simple petal as an ellipse"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    
    # Draw elongated shape
    for i in range(36):
        rad = math.radians(i * 10)
        dx = length * math.cos(rad) * 0.5
        dy = width * math.sin(rad)
        pen.goto(x + dx * math.cos(math.radians(angle)) - dy * math.sin(math.radians(angle)),
                 y + dx * math.sin(math.radians(angle)) + dy * math.cos(math.radians(angle)))
    
    pen.end_fill()
    pen.penup()

def draw_circle_ring(x, y, radius, colors):
    """Draw a ring of small circles"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(colors[0])
    pen.pensize(3)
    pen.circle(radius)
    pen.penup()
    
    # Decorative dots around the ring
    for angle in range(0, 360, 15):
        rad = math.radians(angle)
        cx = x + radius * math.cos(rad)
        cy = y + radius * math.sin(rad)
        pen.goto(cx, cy)
        pen.dot(5, colors[angle // 15 % len(colors)])
    
    pen.penup()

def draw_rangoli_basic():
    """Draw a basic 8-petal rangoli"""
    colors = color_palettes[current_palette]
    center_x, center_y = 0, 0
    radius = 100
    
    # Outer decorative circle
    pen.penup()
    pen.goto(center_x, center_y - 200)
    pen.pendown()
    pen.color(colors[0])
    pen.pensize(4)
    pen.circle(200)
    pen.penup()
    
    # 8 petals in outer ring
    for i in range(petal_count * 2):
        angle = i * (360 / (petal_count * 2))
        x = 140 * math.cos(math.radians(angle))
        y = 140 * math.sin(math.radians(angle))
        draw_petal(x, y, 60, angle + 90, colors[i % len(colors)])
    
    # Inner petals
    for i in range(petal_count):
        angle = i * (360 / petal_count)
        x = 70 * math.cos(math.radians(angle))
        y = 70 * math.sin(math.radians(angle))
        draw_petal(x, y, 50, angle + 90, colors[(i + 2) % len(colors)])
    
    # Center circle
    pen.penup()
    pen.goto(center_x, center_y - 30)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(colors[-1])
    pen.circle(30)
    pen.end_fill()
    pen.penup()
    
    # Center dot
    pen.goto(center_x, center_y)
    pen.dot(10, "white")
    
    screen.update()

def draw_rangoli_flower():
    """Draw a flower-style rangoli with layers"""
    colors = color_palettes[current_palette]
    center_x, center_y = 0, 0
    
    # Layer 1: Large outer petals
    for i in range(12):
        angle = i * 30
        x = 160 * math.cos(math.radians(angle))
        y = 160 * math.sin(math.radians(angle))
        draw_petal(x, y, 65, angle + 90, colors[i % len(colors)])
    
    # Layer 2: Medium petals
    for i in range(8):
        angle = i * 45
        x = 100 * math.cos(math.radians(angle))
        y = 100 * math.sin(math.radians(angle))
        draw_petal(x, y, 50, angle + 90, colors[(i + 3) % len(colors)])
    
    # Layer 3: Small inner petals
    for i in range(8):
        angle = i * 45 + 22.5
        x = 50 * math.cos(math.radians(angle))
        y = 50 * math.sin(math.radians(angle))
        draw_petal(x, y, 30, angle + 90, colors[(i + 5) % len(colors)])
    
    # Center design
    pen.penup()
    pen.goto(center_x, center_y - 25)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(colors[-2])
    pen.circle(25)
    pen.end_fill()
    
    for i in range(6):
        angle = i * 60
        x = 15 * math.cos(math.radians(angle))
        y = 15 * math.sin(math.radians(angle))
        pen.penup()
        pen.goto(x, y)
        pen.dot(10, colors[i % len(colors)])
    
    screen.update()

def draw_rangoli_geometric():
    """Draw a geometric rangoli with triangles and squares"""
    colors = color_palettes[current_palette]
    center_x, center_y = 0, 0
    
    # Outer square
    pen.penup()
    pen.goto(-180, -180)
    pen.pendown()
    pen.color(colors[0])
    pen.pensize(3)
    for _ in range(4):
        pen.forward(360)
        pen.left(90)
    pen.penup()
    
    # Diagonal lines
    for angle in [45, 135]:
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.pendown()
        pen.color(colors[1])
        pen.forward(250)
        pen.backward(500)
    pen.penup()
    
    # Triangles on edges
    for i in range(8):
        angle = i * 45
        x = 180 * math.cos(math.radians(angle))
        y = 180 * math.sin(math.radians(angle))
        
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle + 180)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[i % len(colors)])
        pen.forward(40)
        pen.left(120)
        pen.forward(40)
        pen.left(120)
        pen.forward(40)
        pen.end_fill()
    
    # Inner star
    for i in range(8):
        angle = i * 45 + 22.5
        x = 80 * math.cos(math.radians(angle))
        y = 80 * math.sin(math.radians(angle))
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle + 90)
        pen.pendown()
        pen.begin_fill()
        pen.fillcolor(colors[(i + 2) % len(colors)])
        pen.forward(25)
        pen.right(90)
        pen.forward(15)
        pen.right(90)
        pen.forward(25)
        pen.right(90)
        pen.forward(15)
        pen.end_fill()
    
    screen.update()

def draw_rangoli_mandala():
    """Draw an intricate mandala-style rangoli"""
    colors = color_palettes[current_palette]
    center_x, center_y = 0, 0
    
    # Concentric rings
    for ring, radius in enumerate([50, 100, 150, 200]):
        pen.penup()
        pen.goto(center_x, center_y - radius)
        pen.pendown()
        pen.color(colors[ring % len(colors)])
        pen.pensize(2 if ring % 2 == 0 else 3)
        pen.circle(radius)
    
    # Petals around each ring
    for ring_radius, num_petals in [(50, 6), (100, 8), (150, 12), (200, 16)]:
        for i in range(num_petals):
            angle = i * (360 / num_petals)
            x = ring_radius * math.cos(math.radians(angle))
            y = ring_radius * math.sin(math.radians(angle))
            petal_size = ring_radius * 0.3
            draw_petal(x, y, petal_size, angle + 90, colors[(ring_radius // 50 + i) % len(colors)])
    
    # Decorative dots
    for angle in range(0, 360, 10):
        rad = math.radians(angle)
        x = 225 * math.cos(rad)
        y = 225 * math.sin(rad)
        pen.penup()
        pen.goto(x, y)
        pen.dot(4, colors[int(angle / 10) % len(colors)])
    
    screen.update()

def draw_rangoli_kolam():
    """Draw a kolam-style rangoli (South Indian)"""
    colors = color_palettes[current_palette]
    points = []
    
    # Create a grid of dots
    dot_spacing = 40
    rows = 9
    cols = 9
    
    for row in range(rows):
        for col in range(cols):
            x = (col - cols//2) * dot_spacing
            y = (rows//2 - row) * dot_spacing
            pen.penup()
            pen.goto(x, y)
            pen.dot(5, colors[(row + col) % len(colors)])
            points.append((x, y))
    
    # Connect dots in diamond patterns
    for row in range(rows - 1):
        for col in range(cols - 1):
            x1 = (col - cols//2) * dot_spacing
            y1 = (rows//2 - row) * dot_spacing
            x2 = (col + 1 - cols//2) * dot_spacing
            y2 = (rows//2 - row) * dot_spacing
            x3 = (col - cols//2) * dot_spacing
            y3 = (rows//2 - (row + 1)) * dot_spacing
            
            # Draw diamond
            pen.penup()
            pen.goto(x1, y1)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.pensize(2)
            pen.goto((x1 + x2)/2, (y1 + y2)/2 + 10)
            pen.goto(x3, y3)
            pen.goto((x1 + x3)/2, (y1 + y3)/2 - 10)
            pen.goto(x1, y1)
    
    screen.update()

def draw_rangoli_lotus():
    """Draw a lotus-inspired rangoli"""
    colors = color_palettes[current_palette]
    center_x, center_y = 0, 0
    
    # Outer petals
    for i in range(16):
        angle = i * 22.5
        x = 170 * math.cos(math.radians(angle))
        y = 170 * math.sin(math.radians(angle))
        draw_petal(x, y, 55, angle + 90, colors[i % len(colors)])
    
    # Middle layer petals
    for i in range(12):
        angle = i * 30 + 15
        x = 110 * math.cos(math.radians(angle))
        y = 110 * math.sin(math.radians(angle))
        draw_petal(x, y, 45, angle + 90, colors[(i + 2) % len(colors)])
    
    # Inner layer
    for i in range(8):
        angle = i * 45
        x = 60 * math.cos(math.radians(angle))
        y = 60 * math.sin(math.radians(angle))
        draw_petal(x, y, 30, angle + 90, colors[(i + 4) % len(colors)])
    
    # Center
    pen.penup()
    pen.goto(center_x, center_y - 20)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(colors[-1])
    pen.circle(20)
    pen.end_fill()
    
    # Center patterns
    for i in range(6):
        angle = i * 60
        x = 12 * math.cos(math.radians(angle))
        y = 12 * math.sin(math.radians(angle))
        pen.penup()
        pen.goto(x, y)
        pen.dot(6, "#FFD700")
    
    screen.update()

def draw_rangoli_deepam():
    """Draw a deepam (lamp) inspired rangoli"""
    colors = color_palettes[current_palette]
    
    # Base platform
    pen.penup()
    pen.goto(-120, -120)
    pen.pendown()
    pen.color(colors[0])
    pen.begin_fill()
    pen.fillcolor(colors[0])
    for _ in range(4):
        pen.forward(240)
        pen.left(90)
    pen.end_fill()
    
    # Decorative lines
    for i in range(4):
        pen.penup()
        pen.goto(-100 + i * 200, -100)
        pen.pendown()
        pen.color(colors[1])
        pen.goto(-100 + i * 200, -70)
    
    # Lamp flames (petals)
    for i in range(8):
        angle = i * 45
        x = 80 * math.cos(math.radians(angle))
        y = 80 * math.sin(math.radians(angle))
        draw_petal(x, y + 20, 30, angle + 90, colors[(i + 2) % len(colors)])
    
    # Main center flame
    draw_petal(0, 30, 40, 90, colors[-2])
    draw_petal(0, 60, 25, 90, colors[-1])
    
    # Aura dots
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x = 140 * math.cos(rad)
        y = 140 * math.sin(rad) + 20
        pen.penup()
        pen.goto(x, y)
        pen.dot(6, colors[int(angle / 30) % len(colors)])
    
    screen.update()

# UI Controls
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 470)
    title.write("🎨 COLORFUL RANGOLI PATTERN 🎨", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -480)
    instructions.write("1=Basic 2=Flower 3=Geometric 4=Mandala 5=Kolam 6=Lotus 7=Deepam | C=Color | +/-=Petals | R=Redraw | ESC=Exit",
                       align="center", font=("Arial", 8, "normal"))

current_rangoli = 1

def draw_current():
    """Draw the currently selected rangoli"""
    pen.clear()
    
    if current_rangoli == 1:
        draw_rangoli_basic()
    elif current_rangoli == 2:
        draw_rangoli_flower()
    elif current_rangoli == 3:
        draw_rangoli_geometric()
    elif current_rangoli == 4:
        draw_rangoli_mandala()
    elif current_rangoli == 5:
        draw_rangoli_kolam()
    elif current_rangoli == 6:
        draw_rangoli_lotus()
    elif current_rangoli == 7:
        draw_rangoli_deepam()
    
    screen.update()

def set_rangoli_1(): global current_rangoli; current_rangoli = 1; draw_current()
def set_rangoli_2(): global current_rangoli; current_rangoli = 2; draw_current()
def set_rangoli_3(): global current_rangoli; current_rangoli = 3; draw_current()
def set_rangoli_4(): global current_rangoli; current_rangoli = 4; draw_current()
def set_rangoli_5(): global current_rangoli; current_rangoli = 5; draw_current()
def set_rangoli_6(): global current_rangoli; current_rangoli = 6; draw_current()
def set_rangoli_7(): global current_rangoli; current_rangoli = 7; draw_current()

def change_color():
    global current_palette
    palettes = list(color_palettes.keys())
    idx = palettes.index(current_palette)
    current_palette = palettes[(idx + 1) % len(palettes)]
    draw_current()

def increase_petals():
    global petal_count
    petal_count = min(petal_count + 2, 16)
    if current_rangoli in [1, 2]:
        draw_current()

def decrease_petals():
    global petal_count
    petal_count = max(petal_count - 2, 4)
    if current_rangoli in [1, 2]:
        draw_current()

def redraw():
    draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_rangoli_1, "1")
screen.onkey(set_rangoli_2, "2")
screen.onkey(set_rangoli_3, "3")
screen.onkey(set_rangoli_4, "4")
screen.onkey(set_rangoli_5, "5")
screen.onkey(set_rangoli_6, "6")
screen.onkey(set_rangoli_7, "7")
screen.onkey(change_color, "c")
screen.onkey(increase_petals, "plus")
screen.onkey(increase_petals, "equal")
screen.onkey(decrease_petals, "minus")
screen.onkey(redraw, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        COLORFUL RANGOLI PATTERN")
print("=" * 60)
print()
print("Traditional Indian geometric art patterns!")
print()
print("7 RANGOLI STYLES:")
print("  1 - Basic Rangoli: Classic 8-petal design")
print("  2 - Flower Rangoli: Layered flower pattern")
print("  3 - Geometric Rangoli: Triangles and squares")
print("  4 - Mandala Rangoli: Concentric rings with petals")
print("  5 - Kolam Rangoli: South Indian dot grid pattern")
print("  6 - Lotus Rangoli: Lotus-inspired design")
print("  7 - Deepam Rangoli: Lamp/flame pattern")
print()
print("COLOR SCHEMES:")
print("  Traditional  |  Festive  |  Diwali  |  Pastel  |  Jewel  |  Peacock")
print()
print("CONTROLS:")
print("  1-7   - Select rangoli style")
print("  C     - Change color palette")
print("  +/-   - Adjust petal count (styles 1 & 2)")
print("  R     - Redraw")
print("  ESC   - Exit")
print()
print("Rangoli brings good luck and prosperity!")

draw_rangoli_basic()
screen.mainloop()