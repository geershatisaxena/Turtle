import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Right Angle Patterns - 90° Turns Only")
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
    "neon": ["#FF0066", "#00FFCC", "#FFCC00", "#9900FF", "#00FF66", "#FF3300"],
    "pastel": ["#FFB3BA", "#B5EAD7", "#C7CEEA", "#FFDAC1", "#E2F0CB", "#FF9AA2"],
    "mono_blue": ["#001F3F", "#003366", "#004C99", "#0066CC", "#0080FF", "#3399FF"],
    "mono_red": ["#3D0000", "#660000", "#990000", "#CC0000", "#FF0000", "#FF3333"],
    "rainbow": ["red", "orange", "yellow", "green", "blue", "purple"],
    "cyber": ["#00FF00", "#00FFFF", "#FF00FF", "#FFFF00", "#FF0000", "#0000FF"]
}

current_palette = "neon"

# Pattern parameters
step_size = 10
angle = 90  # Only 90° turns!
current_direction = 0
x, y = 0, 0

def draw_square_spiral():
    """Classic square spiral using only 90° turns"""
    pen.clear()
    x, y = 0, 0
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    size = step_size
    direction = 0  # 0=right, 1=up, 2=left, 3=down
    
    for i in range(200):
        pen.color(colors[i % len(colors)])
        pen.forward(size)
        pen.right(90)
        
        # Increase size every 2 turns to create spiral
        if i % 2 == 1:
            size += step_size
        
        if i % 50 == 0:
            screen.update()
    
    screen.update()

def draw_recursive_squares():
    """Draw nested squares (concentric)"""
    pen.clear()
    colors = color_palettes[current_palette]
    
    for i in range(30):
        size = (i + 1) * step_size * 2
        pen.penup()
        pen.goto(-size/2, -size/2)
        pen.pendown()
        pen.color(colors[i % len(colors)])
        
        # Draw square using 90° turns
        for _ in range(4):
            pen.forward(size)
            pen.left(90)
        
        pen.penup()
        screen.update()
    
    screen.update()

def draw_orthogonal_maze():
    """Draw a maze-like pattern using only right angles"""
    pen.clear()
    x, y = 0, 0
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    patterns = [(step_size, 0), (0, step_size), (-step_size*2, 0), (0, -step_size),
                (step_size*3, 0), (0, step_size*2), (-step_size, 0), (0, -step_size*3)]
    
    for i in range(50):
        pen.color(colors[i % len(colors)])
        pattern = patterns[i % len(patterns)]
        pen.goto(pen.xcor() + pattern[0], pen.ycor() + pattern[1])
        
        if i % 20 == 0:
            screen.update()
    
    screen.update()

def draw_plus_pattern():
    """Draw a pattern of plus signs using right angles"""
    pen.clear()
    pen.penup()
    
    colors = color_palettes[current_palette]
    spacing = step_size * 3
    
    for row in range(-15, 16):
        for col in range(-15, 16):
            if abs(row) % 3 == 0 or abs(col) % 3 == 0:
                x = col * spacing
                y = row * spacing
                
                pen.goto(x, y - step_size)
                pen.pendown()
                pen.color(colors[(abs(row) + abs(col)) % len(colors)])
                
                # Draw plus sign (all 90° angles)
                pen.forward(step_size * 2)
                pen.backward(step_size)
                pen.left(90)
                pen.forward(step_size)
                pen.backward(step_size * 2)
                pen.forward(step_size)
                pen.right(90)
                
                pen.penup()
        
        if row % 5 == 0:
            screen.update()
    
    screen.update()

def draw_blocks_pattern():
    """Draw a pattern of colored blocks arranged orthogonally"""
    pen.clear()
    pen.penup()
    
    colors = color_palettes[current_palette]
    block_size = step_size * 2
    
    for row in range(-12, 13):
        for col in range(-12, 13):
            x = col * block_size
            y = row * block_size
            
            # Only draw blocks in checkerboard pattern
            if (row + col) % 2 == 0:
                pen.goto(x, y)
                pen.pendown()
                pen.color(colors[(row + col) % len(colors)])
                pen.begin_fill()
                pen.fillcolor(colors[(row + col) % len(colors)])
                
                # Draw square block (90° turns)
                for _ in range(4):
                    pen.forward(block_size)
                    pen.left(90)
                
                pen.end_fill()
                pen.penup()
        
        if row % 5 == 0:
            screen.update()
    
    screen.update()

def draw_spiral_staircase():
    """Draw a spiral staircase pattern using only right angles"""
    pen.clear()
    x, y = 0, -200
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    size = step_size
    
    for i in range(100):
        pen.color(colors[i % len(colors)])
        
        # Horizontal step
        if i % 2 == 0:
            pen.forward(size)
            pen.right(90)
        # Vertical step
        else:
            pen.forward(size)
            pen.right(90)
            size += step_size / 2
        
        if i % 20 == 0:
            screen.update()
    
    screen.update()

def draw_city_skyline():
    """Draw a city skyline silhouette using rectangles"""
    pen.clear()
    pen.penup()
    
    colors = color_palettes[current_palette]
    
    for building in range(-20, 21):
        x = building * step_size * 3
        height = random.randint(3, 15) * step_size
        
        pen.goto(x, -250)
        pen.pendown()
        
        # Draw building (rectangle using 90° turns)
        for _ in range(2):
            pen.forward(step_size * 2)
            pen.left(90)
            pen.forward(height)
            pen.left(90)
        
        pen.penup()
        
        # Draw windows
        for window_y in range(1, int(height/step_size)):
            pen.goto(x + step_size/2, -250 + window_y * step_size)
            pen.dot(3, colors[(building + window_y) % len(colors)])
        
        if building % 5 == 0:
            screen.update()
    
    screen.update()

def draw_cross_hatch_pattern():
    """Draw a cross-hatch pattern using orthogonal lines"""
    pen.clear()
    pen.penup()
    
    colors = color_palettes[current_palette]
    
    # Horizontal lines
    for y in range(-250, 251, step_size * 2):
        pen.goto(-300, y)
        pen.pendown()
        pen.color(colors[(y // step_size) % len(colors)])
        pen.forward(600)
        pen.penup()
    
    # Vertical lines
    for x in range(-300, 301, step_size * 2):
        pen.goto(x, -250)
        pen.pendown()
        pen.color(colors[(x // step_size) % len(colors)])
        pen.goto(x, 250)
        pen.penup()
    
    screen.update()

def draw_zigzag_pattern():
    """Draw a zigzag pattern using only right angles"""
    pen.clear()
    pen.penup()
    pen.goto(-350, 0)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    amplitude = 50
    
    for i in range(70):
        pen.color(colors[i % len(colors)])
        
        # Zigzag using right angles
        pen.forward(step_size * 2)
        pen.right(90)
        pen.forward(amplitude)
        pen.right(90)
        pen.forward(step_size * 2)
        pen.left(90)
        pen.forward(amplitude)
        pen.left(90)
        
        if i % 10 == 0:
            screen.update()
    
    screen.update()

def draw_optical_illusion():
    """Create an optical illusion using right angles"""
    pen.clear()
    pen.penup()
    
    colors = color_palettes[current_palette]
    size = step_size * 3
    
    for i in range(8):
        angle_offset = i * 45
        radius = 150
        
        for j in range(8):
            x = radius * math.cos(math.radians(angle_offset + j * 45))
            y = radius * math.sin(math.radians(angle_offset + j * 45))
            
            pen.goto(x - size/2, y - size/2)
            pen.pendown()
            pen.color(colors[(i + j) % len(colors)])
            
            # Draw square
            for _ in range(4):
                pen.forward(size)
                pen.left(90)
            
            pen.penup()
        
        screen.update()

def draw_tree_pattern():
    """Draw a right-angle tree fractal"""
    pen.clear()
    pen.penup()
    pen.goto(0, -300)
    pen.setheading(90)
    pen.pendown()
    
    colors = color_palettes[current_palette]
    
    def draw_branch(length, depth):
        if depth == 0 or length < 5:
            return
        
        pen.color(colors[depth % len(colors)])
        pen.forward(length)
        
        # Right branch
        pen.right(90)
        draw_branch(length * 0.7, depth - 1)
        
        # Left branch  
        pen.left(180)
        draw_branch(length * 0.7, depth - 1)
        
        # Return to start
        pen.right(90)
        pen.backward(length)
    
    draw_branch(80, 12)
    screen.update()

# UI elements
def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 430)
    title.write("🔲 RIGHT ANGLE PATTERNS (90° Turns Only) 🔲", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -440)
    instructions.write("1=Spiral 2=Squares 3=Maze 4=Plus 5=Blocks 6=Stairs 7=City 8=Cross 9=Zigzag 0=Optical T=Tree | S=Color | R=Redraw | ESC=Exit",
                       align="center", font=("Arial", 8, "normal"))

# Pattern selection
current_pattern = 1

def draw_current_pattern():
    """Draw the currently selected pattern"""
    pen.clear()
    
    if current_pattern == 1:
        draw_square_spiral()
    elif current_pattern == 2:
        draw_recursive_squares()
    elif current_pattern == 3:
        draw_orthogonal_maze()
    elif current_pattern == 4:
        draw_plus_pattern()
    elif current_pattern == 5:
        draw_blocks_pattern()
    elif current_pattern == 6:
        draw_spiral_staircase()
    elif current_pattern == 7:
        draw_city_skyline()
    elif current_pattern == 8:
        draw_cross_hatch_pattern()
    elif current_pattern == 9:
        draw_zigzag_pattern()
    elif current_pattern == 0:
        draw_optical_illusion()
    elif current_pattern == 10:
        draw_tree_pattern()
    
    screen.update()

def set_pattern_1(): global current_pattern; current_pattern = 1; draw_current_pattern()
def set_pattern_2(): global current_pattern; current_pattern = 2; draw_current_pattern()
def set_pattern_3(): global current_pattern; current_pattern = 3; draw_current_pattern()
def set_pattern_4(): global current_pattern; current_pattern = 4; draw_current_pattern()
def set_pattern_5(): global current_pattern; current_pattern = 5; draw_current_pattern()
def set_pattern_6(): global current_pattern; current_pattern = 6; draw_current_pattern()
def set_pattern_7(): global current_pattern; current_pattern = 7; draw_current_pattern()
def set_pattern_8(): global current_pattern; current_pattern = 8; draw_current_pattern()
def set_pattern_9(): global current_pattern; current_pattern = 9; draw_current_pattern()
def set_pattern_0(): global current_pattern; current_pattern = 0; draw_current_pattern()
def set_pattern_tree(): global current_pattern; current_pattern = 10; draw_current_pattern()

def change_color_scheme():
    """Cycle through color schemes"""
    global current_palette
    palettes = list(color_palettes.keys())
    idx = palettes.index(current_palette)
    current_palette = palettes[(idx + 1) % len(palettes)]
    draw_current_pattern()

def reset():
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
screen.onkey(set_pattern_8, "8")
screen.onkey(set_pattern_9, "9")
screen.onkey(set_pattern_0, "0")
screen.onkey(set_pattern_tree, "t")
screen.onkey(change_color_scheme, "s")
screen.onkey(reset, "r")
screen.onkey(lambda: screen.bye(), "Escape")

# Draw UI
draw_title()

print("=" * 60)
print("     RIGHT ANGLE PATTERNS (90° Turns Only)")
print("=" * 60)
print()
print("All patterns are created using ONLY 90-degree turns!")
print()
print("PATTERNS:")
print("  1 - Square Spiral: Classic expanding spiral")
print("  2 - Nested Squares: Concentric squares")
print("  3 - Maze Pattern: Orthogonal maze-like path")
print("  4 - Plus Pattern: Grid of plus signs")
print("  5 - Colored Blocks: Checkerboard block pattern")
print("  6 - Spiral Stairs: Staircase spiral")
print("  7 - City Skyline: Cityscape with windows")
print("  8 - Cross Hatch: Grid of orthogonal lines")
print("  9 - Zigzag: Bouncing zigzag pattern")
print("  0 - Optical Illusion: 45° rotated squares")
print("  T - Tree Fractal: Right-angle binary tree")
print()
print("CONTROLS:")
print("  0-9, T - Select different patterns")
print("  S - Change color scheme")
print("  R - Redraw current pattern")
print("  ESC - Exit program")
print()
print("Every line, every turn is exactly 90 degrees!")

# Draw initial pattern
draw_square_spiral()

screen.mainloop()