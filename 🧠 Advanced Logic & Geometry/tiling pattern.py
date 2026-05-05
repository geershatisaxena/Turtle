import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Tiling Patterns - Floor Tile Designs")
screen.bgcolor("black")
screen.setup(width=1000, height=900)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palettes
color_palettes = {
    "classic": ["#8B4513", "#D2691E", "#CD853F", "#DEB887", "#FFDEAD"],
    "modern": ["#2C3E50", "#34495E", "#3498DB", "#2980B9", "#1ABC9C"],
    "warm": ["#E74C3C", "#EC7063", "#F1948A", "#F5B7B1", "#FDEDEC"],
    "cool": ["#1ABC9C", "#16A085", "#2ECC71", "#27AE60", "#76D7C4"],
    "mono": ["white", "lightgray", "gray", "dimgray", "silver"],
    "vibrant": ["#FF0066", "#FF6600", "#FFCC00", "#00FF66", "#0066FF"]
}

current_palette = "classic"
tile_size = 40

def draw_square_tiling():
    """Draw a simple square grid tiling (like bathroom tiles)"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    for row in range(-12, 13):
        for col in range(-12, 13):
            x = col * tile_size
            y = row * tile_size
            
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            # Draw square
            for _ in range(4):
                pen.forward(tile_size)
                pen.right(90)
            
            pen.end_fill()
            
            # Add small pattern in alternating tiles
            if (row + col) % 2 == 0:
                pen.penup()
                pen.goto(x + tile_size//2, y + tile_size//2)
                pen.dot(tile_size//4, "white")
    
    screen.update()

def draw_hexagonal_tiling():
    """Draw hexagonal tiling (honeycomb pattern)"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    hex_height = tile_size * math.sqrt(3)
    hex_width = tile_size * 2
    
    for row in range(-10, 11):
        for col in range(-10, 11):
            x = col * hex_width * 0.75
            y = row * hex_height
            
            if col % 2 != 0:
                y += hex_height / 2
            
            pen.penup()
            pen.goto(x, y)
            pen.setheading(0)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            # Draw hexagon
            for _ in range(6):
                pen.forward(tile_size)
                pen.left(60)
            
            pen.end_fill()
            
            if (row + col) % 3 == 0:
                pen.penup()
                pen.goto(x + tile_size//2, y)
                pen.dot(tile_size//4, "gold")
    
    screen.update()

def draw_triangular_tiling():
    """Draw triangular tiling (equilateral triangles)"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    tri_height = tile_size * math.sqrt(3) / 2
    
    for row in range(-15, 16):
        for col in range(-15, 16):
            x = col * tile_size
            y = row * tri_height
            
            # Alternate triangle orientation
            orientation = (row + col) % 2
            pen.penup()
            pen.goto(x, y)
            pen.setheading(0)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            if orientation == 0:
                # Pointing up
                pen.forward(tile_size)
                pen.left(120)
                pen.forward(tile_size)
                pen.left(120)
                pen.forward(tile_size)
            else:
                # Pointing down
                pen.forward(tile_size)
                pen.right(120)
                pen.forward(tile_size)
                pen.right(120)
                pen.forward(tile_size)
            
            pen.end_fill()
    
    screen.update()

def draw_brick_tiling():
    """Draw brick wall pattern (offset rectangles)"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    brick_width = tile_size * 2
    brick_height = tile_size
    
    for row in range(-12, 13):
        for col in range(-12, 13):
            x = col * brick_width
            y = row * brick_height
            
            # Offset every other row
            if row % 2 == 0:
                x += brick_width / 2
            
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[row % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[row % len(colors)])
            
            # Draw brick
            for _ in range(2):
                pen.forward(brick_width - 2)
                pen.right(90)
                pen.forward(brick_height - 2)
                pen.right(90)
            
            pen.end_fill()
    
    screen.update()

def draw_rhombus_tiling():
    """Draw rhombus/diamond tiling"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    rhombus_size = tile_size
    
    for row in range(-12, 13):
        for col in range(-12, 13):
            x = col * rhombus_size * 2
            y = row * rhombus_size
            
            if row % 2 != 0:
                x += rhombus_size
            
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            # Draw rhombus
            for i in range(4):
                if i % 2 == 0:
                    pen.forward(rhombus_size)
                    pen.left(60)
                else:
                    pen.forward(rhombus_size)
                    pen.left(120)
            
            pen.end_fill()
    
    screen.update()

def draw_octagon_square_tiling():
    """Draw octagon and square tiling (like some floor tiles)"""
    pen.clear()
    colors = color_palettes[current_palette]
    oct_size = tile_size
    square_size = oct_size * 0.7
    
    for row in range(-10, 11):
        for col in range(-10, 11):
            x = col * (oct_size * 2 + square_size)
            y = row * (oct_size * 2 + square_size)
            
            # Draw octagon
            pen.penup()
            pen.goto(x + oct_size, y)
            pen.setheading(0)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            for _ in range(8):
                pen.forward(oct_size)
                pen.left(45)
            
            pen.end_fill()
            
            # Draw square in between
            pen.penup()
            pen.goto(x + oct_size * 2 + square_size/2, y + oct_size * 2 + square_size/2)
            pen.setheading(0)
            pen.pendown()
            pen.color(colors[(row + col + 1) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col + 1) % len(colors)])
            
            for _ in range(4):
                pen.forward(square_size)
                pen.left(90)
            
            pen.end_fill()
    
    screen.update()

def draw_circle_packing_tiling():
    """Draw circle packing tiling pattern"""
    pen.clear()
    colors = color_palettes[current_palette]
    radius = tile_size / 2
    
    for row in range(-12, 13):
        for col in range(-12, 13):
            x = col * tile_size
            y = row * tile_size
            
            # Offset every other row
            if row % 2 != 0:
                x += tile_size / 2
            
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            pen.circle(radius)
            pen.end_fill()
            
            # Add highlight
            pen.penup()
            pen.goto(x - radius/2, y + radius/2)
            pen.dot(radius/3, "white")
    
    screen.update()

def draw_arabesque_tiling():
    """Draw decorative arabesque tiling pattern"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    for row in range(-10, 11):
        for col in range(-10, 11):
            x = col * tile_size * 2
            y = row * tile_size * 2
            
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            # Draw diamond
            for angle in [45, 135, 225, 315]:
                rad = math.radians(angle)
                dx = tile_size * math.cos(rad)
                dy = tile_size * math.sin(rad)
                pen.goto(x + dx, y + dy)
            
            pen.end_fill()
            
            # Draw inner square
            pen.penup()
            pen.goto(x - tile_size/2, y - tile_size/2)
            pen.pendown()
            pen.color(colors[(row + col + 1) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col + 1) % len(colors)])
            
            for _ in range(4):
                pen.forward(tile_size)
                pen.left(90)
            
            pen.end_fill()
    
    screen.update()

def draw_herringbone_tiling():
    """Draw herringbone pattern (zigzag wood floor style)"""
    pen.clear()
    colors = color_palettes[current_palette]
    plank_width = tile_size
    plank_length = tile_size * 3
    
    for row in range(-10, 11):
        for col in range(-10, 11):
            x = col * plank_length
            y = row * plank_width
            
            # Alternate direction
            direction = (row + col) % 2
            
            pen.penup()
            pen.goto(x, y)
            pen.setheading(45 if direction == 0 else -45)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            
            # Draw diamond plank
            for _ in range(2):
                pen.forward(plank_length / 2 * math.sqrt(2))
                pen.right(90)
                pen.forward(plank_width * math.sqrt(2))
                pen.right(90)
            
            pen.end_fill()
    
    screen.update()

def draw_zentangle_tiling():
    """Draw zentangle-inspired decorative tile pattern"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    for row in range(-8, 9):
        for col in range(-8, 9):
            x = col * tile_size * 2
            y = row * tile_size * 2
            
            # Draw outer square
            pen.penup()
            pen.goto(x - tile_size, y - tile_size)
            pen.pendown()
            pen.color(colors[(row + col) % len(colors)])
            pen.begin_fill()
            pen.fillcolor(colors[(row + col) % len(colors)])
            for _ in range(4):
                pen.forward(tile_size * 2)
                pen.left(90)
            pen.end_fill()
            
            # Draw inner pattern: circle
            pen.penup()
            pen.goto(x, y - tile_size)
            pen.pendown()
            pen.color("white")
            pen.circle(tile_size)
            
            # Draw inner pattern: diamond
            pen.penup()
            pen.goto(x, y - tile_size/2)
            pen.pendown()
            for angle in [45, 135, 225, 315]:
                rad = math.radians(angle)
                dx = (tile_size/2) * math.cos(rad)
                dy = (tile_size/2) * math.sin(rad)
                pen.goto(x + dx, y + dy)
    
    screen.update()

# UI Controls
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 430)
    title.write("🪄 TILING PATTERNS - FLOOR TILE DESIGNS 🪄", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -450)
    instructions.write("1=Square 2=Hexagon 3=Triangle 4=Brick 5=Rhombus 6=Octagon 7=Circle 8=Arabesque 9=Herringbone 0=Zentangle | C=Color +/-=Size R=Redraw ESC=Exit",
                       align="center", font=("Arial", 8, "normal"))

current_tile = 1

def draw_current():
    """Draw the currently selected tiling"""
    pen.clear()
    
    if current_tile == 1:
        draw_square_tiling()
    elif current_tile == 2:
        draw_hexagonal_tiling()
    elif current_tile == 3:
        draw_triangular_tiling()
    elif current_tile == 4:
        draw_brick_tiling()
    elif current_tile == 5:
        draw_rhombus_tiling()
    elif current_tile == 6:
        draw_octagon_square_tiling()
    elif current_tile == 7:
        draw_circle_packing_tiling()
    elif current_tile == 8:
        draw_arabesque_tiling()
    elif current_tile == 9:
        draw_herringbone_tiling()
    elif current_tile == 10:
        draw_zentangle_tiling()
    
    screen.update()

def set_tile_1(): global current_tile; current_tile = 1; draw_current()
def set_tile_2(): global current_tile; current_tile = 2; draw_current()
def set_tile_3(): global current_tile; current_tile = 3; draw_current()
def set_tile_4(): global current_tile; current_tile = 4; draw_current()
def set_tile_5(): global current_tile; current_tile = 5; draw_current()
def set_tile_6(): global current_tile; current_tile = 6; draw_current()
def set_tile_7(): global current_tile; current_tile = 7; draw_current()
def set_tile_8(): global current_tile; current_tile = 8; draw_current()
def set_tile_9(): global current_tile; current_tile = 9; draw_current()
def set_tile_0(): global current_tile; current_tile = 10; draw_current()

def change_color():
    global current_palette
    palettes = list(color_palettes.keys())
    idx = palettes.index(current_palette)
    current_palette = palettes[(idx + 1) % len(palettes)]
    draw_current()

def increase_size():
    global tile_size
    tile_size = min(tile_size + 5, 60)
    draw_current()

def decrease_size():
    global tile_size
    tile_size = max(tile_size - 5, 20)
    draw_current()

def redraw():
    draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_tile_1, "1")
screen.onkey(set_tile_2, "2")
screen.onkey(set_tile_3, "3")
screen.onkey(set_tile_4, "4")
screen.onkey(set_tile_5, "5")
screen.onkey(set_tile_6, "6")
screen.onkey(set_tile_7, "7")
screen.onkey(set_tile_8, "8")
screen.onkey(set_tile_9, "9")
screen.onkey(set_tile_0, "0")
screen.onkey(change_color, "c")
screen.onkey(increase_size, "plus")
screen.onkey(increase_size, "equal")
screen.onkey(decrease_size, "minus")
screen.onkey(redraw, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        TILING PATTERNS - FLOOR TILE DESIGNS")
print("=" * 60)
print()
print("10 different repeating patterns that tile the plane perfectly!")
print()
print("PATTERNS:")
print("  1 - Square Tiling: Classic grid (like bathroom tiles)")
print("  2 - Hexagonal Tiling: Honeycomb pattern")
print("  3 - Triangular Tiling: Equilateral triangles")
print("  4 - Brick Tiling: Offset rectangles (brick wall)")
print("  5 - Rhombus Tiling: Diamond pattern")
print("  6 - Octagon & Square: Archimedean tiling")
print("  7 - Circle Packing: Overlapping circles")
print("  8 - Arabesque: Decorative geometric pattern")
print("  9 - Herringbone: Zigzag wood floor style")
print("  0 - Zentangle: Decorative tile pattern")
print()
print("CONTROLS:")
print("  0-9   - Select tiling pattern")
print("  C     - Change color palette")
print("  +/-   - Adjust tile size")
print("  R     - Redraw")
print("  ESC   - Exit")
print()
print("Each pattern uses mathematical symmetry to tile the plane!")

draw_square_tiling()
screen.mainloop()