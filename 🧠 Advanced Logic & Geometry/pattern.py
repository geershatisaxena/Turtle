import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Alternating Long & Short Lines Pattern")
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
    "rainbow": ["red", "orange", "yellow", "green", "blue", "purple"],
    "sunset": ["#FF6B35", "#F7931E", "#FDC830", "#F37335", "#DC2430", "#8E2DE2"],
    "ocean": ["#00B4DB", "#0083B0", "#00C9FF", "#92FE9D", "#00B4DB", "#00A8C5"],
    "neon": ["#FF0066", "#00FFCC", "#FFCC00", "#9900FF", "#00FF66", "#FF3300"],
    "pastel": ["#FFB3BA", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#FF9AA2"],
    "mono": ["white", "lightgray", "gray", "dimgray", "silver", "gainsboro"]
}

current_palette = "rainbow"
long_length = 30
short_length = 10
angle = 90
current_x, current_y = 0, 0

def draw_alternating_zigzag():
    """Draw a zigzag pattern with alternating long and short segments"""
    pen.clear()
    pen.penup()
    pen.goto(-350, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    
    for i in range(100):
        color = colors[i % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length)
        else:
            pen.forward(short_length)
        
        pen.right(angle)
        
        if i % 20 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_spiral():
    """Draw a spiral where long and short lines alternate"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    current_length = long_length
    
    for i in range(150):
        color = colors[i % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length)
        else:
            pen.forward(short_length)
        
        pen.right(angle)
        current_length += 0.5
        
        if i % 30 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_star():
    """Draw a star-like pattern using alternating lines"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    
    for i in range(36):
        color = colors[i % len(colors)]
        pen.color(color)
        
        # Draw long line
        pen.forward(long_length * 2)
        pen.backward(long_length * 2)
        
        # Short turn
        pen.right(10)
        
        # Draw short line
        pen.forward(short_length)
        pen.backward(short_length)
        
        # Long turn
        pen.right(angle - 10)
        
        if i % 6 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_square_spiral():
    """Draw a square spiral with alternating segment lengths"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    length = long_length
    
    for i in range(80):
        color = colors[i % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(length)
        else:
            pen.forward(short_length)
        
        pen.right(90)
        
        if i % 2 == 0:
            length += short_length
        
        if i % 20 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_wave():
    """Draw a wave pattern with alternating long/short peaks"""
    pen.clear()
    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    amplitude = 50
    
    for i in range(200):
        color = colors[i % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length)
            pen.right(angle)
            pen.forward(amplitude)
            pen.left(angle)
        else:
            pen.forward(short_length)
            pen.left(angle)
            pen.forward(amplitude)
            pen.right(angle)
        
        if i % 30 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_mandala():
    """Draw a mandala pattern with alternating spoke lengths"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    
    colors = color_palettes[current_palette]
    
    for i in range(72):
        pen.goto(0, 0)
        pen.pendown()
        pen.setheading(i * 5)
        color = colors[i % len(colors)]
        pen.color(color)
        
        # Draw long spoke
        pen.forward(long_length * 2)
        pen.backward(long_length * 2)
        pen.right(5)
        
        # Draw short spoke
        pen.forward(short_length)
        pen.backward(short_length)
        
        pen.penup()
        
        if i % 12 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_web():
    """Draw a spider web pattern with alternating radii"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    
    colors = color_palettes[current_palette]
    radius = long_length
    
    for ring in range(8):
        radius = (ring + 1) * long_length
        pen.penup()
        pen.goto(radius, 0)
        pen.pendown()
        
        for i in range(36):
            angle_step = i * 10
            x = radius * math.cos(math.radians(angle_step))
            y = radius * math.sin(math.radians(angle_step))
            pen.goto(x, y)
            pen.penup()
            pen.goto(radius, 0)
            pen.pendown()
            
            if i % 2 == 0:
                pen.forward(short_length)
                pen.backward(short_length)
        
        pen.penup()
        screen.update()

def draw_alternating_polygon():
    """Draw a polygon with alternating side lengths"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    sides = 12
    interior_angle = 180 - (360 / sides)
    
    for i in range(60):
        color = colors[i % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length)
        else:
            pen.forward(short_length)
        
        pen.right(interior_angle)
        
        if i % 12 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_heart():
    """Draw a heart shape using alternating line lengths"""
    pen.clear()
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.left(45)
    
    colors = color_palettes[current_palette]
    
    # Left lobe
    for i in range(45):
        color = colors[i % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length * 1.2)
        else:
            pen.forward(short_length)
        
        pen.left(2)
    
    # Point
    pen.left(90)
    for i in range(30):
        color = colors[(i + 45) % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length)
        else:
            pen.forward(short_length * 1.5)
        
        pen.left(3)
    
    # Right lobe (mirror)
    pen.right(180)
    for i in range(75):
        color = colors[(i + 75) % len(colors)]
        pen.color(color)
        
        if i % 2 == 0:
            pen.forward(long_length * 1.2)
        else:
            pen.forward(short_length)
        
        pen.right(2)
    
    screen.update()

def draw_alternating_flower():
    """Draw a flower pattern with alternating petals"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    
    colors = color_palettes[current_palette]
    
    for petal in range(24):
        pen.goto(0, 0)
        pen.setheading(petal * 15)
        pen.pendown()
        
        for i in range(12):
            color = colors[(petal + i) % len(colors)]
            pen.color(color)
            
            if i % 2 == 0:
                pen.forward(long_length)
                pen.left(30)
            else:
                pen.forward(short_length)
                pen.right(60)
        
        pen.penup()
        screen.update()
    
    screen.update()

def draw_alternating_maze():
    """Draw a maze-like pattern with alternating segments"""
    pen.clear()
    pen.penup()
    pen.goto(-300, 200)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dir_index = 0
    
    for i in range(200):
        color = colors[i % len(colors)]
        pen.color(color)
        
        dx, dy = directions[dir_index % 4]
        step = long_length if i % 2 == 0 else short_length
        
        pen.goto(pen.xcor() + dx * step, pen.ycor() + dy * step)
        
        # Randomly change direction
        if random.random() < 0.1:
            dir_index += 1
        
        if i % 50 == 0:
            screen.update()
    
    screen.update()

def draw_alternating_geometric():
    """Draw geometric pattern with alternating line lengths"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    
    colors = color_palettes[current_palette]
    
    for layer in range(8):
        radius = (layer + 1) * long_length
        pen.color(colors[layer % len(colors)])
        
        for angle in range(0, 360, 30):
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            pen.goto(x, y)
            pen.pendown()
            
            for i in range(6):
                if (angle + i) % 2 == 0:
                    pen.forward(long_length)
                else:
                    pen.forward(short_length)
                pen.right(60)
            
            pen.penup()
        
        screen.update()
    
    screen.update()

# UI Controls
def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 430)
    title.write("⟷ ALTERNATING LONG & SHORT LINES PATTERNS ⟷", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -440)
    instructions.write("1=Zigzag 2=Spiral 3=Star 4=Square 5=Wave 6=Mandala 7=Web 8=Polygon 9=Heart 0=Flower M=Maze G=Geometric | S=Color | R=Redraw | ESC=Exit",
                       align="center", font=("Arial", 7, "normal"))

current_pattern = 1

def draw_current():
    """Draw the currently selected pattern"""
    pen.clear()
    
    if current_pattern == 1:
        draw_alternating_zigzag()
    elif current_pattern == 2:
        draw_alternating_spiral()
    elif current_pattern == 3:
        draw_alternating_star()
    elif current_pattern == 4:
        draw_alternating_square_spiral()
    elif current_pattern == 5:
        draw_alternating_wave()
    elif current_pattern == 6:
        draw_alternating_mandala()
    elif current_pattern == 7:
        draw_alternating_web()
    elif current_pattern == 8:
        draw_alternating_polygon()
    elif current_pattern == 9:
        draw_alternating_heart()
    elif current_pattern == 0:
        draw_alternating_flower()
    elif current_pattern == 11:
        draw_alternating_maze()
    elif current_pattern == 12:
        draw_alternating_geometric()
    
    screen.update()

def set_pattern_1(): global current_pattern; current_pattern = 1; draw_current()
def set_pattern_2(): global current_pattern; current_pattern = 2; draw_current()
def set_pattern_3(): global current_pattern; current_pattern = 3; draw_current()
def set_pattern_4(): global current_pattern; current_pattern = 4; draw_current()
def set_pattern_5(): global current_pattern; current_pattern = 5; draw_current()
def set_pattern_6(): global current_pattern; current_pattern = 6; draw_current()
def set_pattern_7(): global current_pattern; current_pattern = 7; draw_current()
def set_pattern_8(): global current_pattern; current_pattern = 8; draw_current()
def set_pattern_9(): global current_pattern; current_pattern = 9; draw_current()
def set_pattern_0(): global current_pattern; current_pattern = 0; draw_current()
def set_pattern_maze(): global current_pattern; current_pattern = 11; draw_current()
def set_pattern_geo(): global current_pattern; current_pattern = 12; draw_current()

def change_color_scheme():
    """Cycle through color schemes"""
    global current_palette
    palettes = list(color_palettes.keys())
    idx = palettes.index(current_palette)
    current_palette = palettes[(idx + 1) % len(palettes)]
    draw_current()

def increase_length():
    global long_length, short_length
    long_length = min(long_length + 5, 50)
    short_length = min(short_length + 3, 20)
    draw_current()

def decrease_length():
    global long_length, short_length
    long_length = max(long_length - 5, 15)
    short_length = max(short_length - 3, 5)
    draw_current()

def reset():
    draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_pattern_1, "1")
screen.onkey(set_pattern_2, "2")
screen.onkey(set_pattern_3, "3")
screen.onkey(set_pattern_4, "4")
screen.onkey(set_pattern_5, "5")
screen.onkey(set_pattern_6, "6")
screen.onkey(set_pattern_7, "7")
screen.onkey(set_pattern_8, "8")
screen.onkey(set_pattern_9, "9")
screen.onkey(set_pattern_0, "0")
screen.onkey(set_pattern_maze, "m")
screen.onkey(set_pattern_geo, "g")
screen.onkey(change_color_scheme, "s")
screen.onkey(increase_length, "plus")
screen.onkey(increase_length, "equal")
screen.onkey(decrease_length, "minus")
screen.onkey(reset, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("     ALTERNATING LONG & SHORT LINES PATTERNS")
print("=" * 60)
print()
print("Creating patterns where long and short lines alternate!")
print()
print("PATTERNS:")
print("  1 - Zigzag: Alternating zigzag pattern")
print("  2 - Spiral: Growing spiral with alternating segments")
print("  3 - Star: Star pattern with alternating rays")
print("  4 - Square Spiral: Square spiral alternating lengths")
print("  5 - Wave: Undulating wave pattern")
print("  6 - Mandala: Circular mandala with alternating spokes")
print("  7 - Web: Spider web with alternating radii")
print("  8 - Polygon: Rotating polygon with alternating sides")
print("  9 - Heart: Heart shape using alternating lines")
print("  0 - Flower: Flower pattern with alternating petals")
print("  M - Maze: Maze-like alternating path")
print("  G - Geometric: Complex geometric design")
print()
print("CONTROLS:")
print("  0-9, M, G - Select patterns")
print("  S         - Change color scheme")
print("  +/-       - Adjust line lengths")
print("  R         - Redraw")
print("  ESC       - Exit")
print()
print("Watch how rhythm is created by alternating line lengths!")

draw_alternating_zigzag()
screen.mainloop()