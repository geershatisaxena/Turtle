import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Mirror Pattern - X & Y Axes Symmetry")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Current pattern settings
current_pattern = 1
current_color_palette = 0
show_axes = True

# Color palettes
color_palettes = [
    ["#FF0066", "#FF3366", "#FF6633", "#FF9933", "#FFCC00"],
    ["#00FFCC", "#00FF99", "#00FF66", "#00FF33", "#00FF00"],
    ["#9900FF", "#AA33FF", "#BB66FF", "#CC99FF", "#DDCCFF"],
    ["#FF0000", "#FF4500", "#FF8C00", "#FFD700", "#FFFF00"],
    ["#00BFFF", "#1E90FF", "#4169E1", "#0000CD", "#00008B"],
]

def draw_axes():
    """Draw X and Y axes lines"""
    if not show_axes:
        return
    
    axes = turtle.Turtle()
    axes.speed(0)
    axes.color("gray")
    axes.penup()
    axes.hideturtle()
    axes.pensize(1)
    
    # X-axis
    axes.goto(-450, 0)
    axes.pendown()
    axes.goto(450, 0)
    axes.penup()
    
    # Y-axis
    axes.goto(0, -450)
    axes.pendown()
    axes.goto(0, 450)
    axes.penup()

def plot_mirrored(x, y, color):
    """Plot points in all 4 quadrants (mirror across X and Y axes)"""
    quadrants = [(x, y), (-x, y), (x, -y), (-x, -y)]
    
    for qx, qy in quadrants:
        pen.goto(qx, qy)
        pen.dot(4, color)

def draw_mirrored_line(x1, y1, x2, y2, color):
    """Draw line mirrored across both axes"""
    quadrants = [
        (x1, y1, x2, y2),
        (-x1, y1, -x2, y2),
        (x1, -y1, x2, -y2),
        (-x1, -y1, -x2, -y2)
    ]
    
    for qx1, qy1, qx2, qy2 in quadrants:
        pen.penup()
        pen.goto(qx1, qy1)
        pen.pendown()
        pen.color(color)
        pen.goto(qx2, qy2)
        pen.penup()

def draw_star_pattern():
    """Draw a star pattern mirrored across axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    arms = 8
    
    for i in range(arms):
        angle = i * (360 / arms)
        radius = 200
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        # Draw line from center to outer point
        draw_mirrored_line(0, 0, x, y, colors[i % len(colors)])
        
        # Draw connecting lines between points
        next_angle = ((i + 1) % arms) * (360 / arms)
        x2 = radius * math.cos(math.radians(next_angle))
        y2 = radius * math.sin(math.radians(next_angle))
        draw_mirrored_line(x, y, x2, y2, colors[(i + 2) % len(colors)])
        
        screen.update()

def draw_spiral_quadrants():
    """Draw spiral pattern mirrored across axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    for i in range(200):
        t = i * 0.1
        radius = t * 3
        x = radius * math.cos(t)
        y = radius * math.sin(t)
        
        if x >= 0 and y >= 0:  # Only draw in first quadrant, mirroring handles others
            color = colors[i % len(colors)]
            plot_mirrored(x, y, color)
        
        if i % 10 == 0:
            screen.update()

def draw_flower_mirror():
    """Draw flower petals mirrored across axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    for i in range(36):
        angle = i * 10
        radius = 200
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        # Draw petal shape
        petal_radius = 40
        petal_angle = angle + 90
        
        x2 = x + petal_radius * math.cos(math.radians(petal_angle))
        y2 = y + petal_radius * math.sin(math.radians(petal_angle))
        x3 = x + petal_radius * math.cos(math.radians(petal_angle + 180))
        y3 = y + petal_radius * math.sin(math.radians(petal_angle + 180))
        
        if x >= 0 and y >= 0:
            draw_mirrored_line(x, y, x2, y2, colors[i % len(colors)])
            draw_mirrored_line(x, y, x3, y3, colors[(i + 1) % len(colors)])
        
        screen.update()

def draw_geometric_mirror():
    """Draw geometric shapes mirrored across axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    # Draw concentric squares in first quadrant, mirrored
    for size in range(40, 400, 40):
        x1, y1 = size, size
        x2, y2 = size, 0
        x3, y3 = 0, size
        
        draw_mirrored_line(0, 0, x1, y1, colors[(size//40) % len(colors)])
        draw_mirrored_line(x2, y2, x1, y1, colors[(size//40 + 1) % len(colors)])
        draw_mirrored_line(x3, y3, x1, y1, colors[(size//40 + 2) % len(colors)])
        
        screen.update()

def draw_circle_mirror():
    """Draw quarter circles mirrored across axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    for radius in range(50, 450, 50):
        points = []
        # Generate points in first quadrant
        for angle in range(0, 91):
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            points.append((int(x), int(y)))
        
        # Connect points
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            draw_mirrored_line(x1, y1, x2, y2, colors[(radius//50) % len(colors)])
        
        screen.update()

def draw_diagonal_mirror():
    """Draw symmetric diagonal pattern"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    for i in range(-400, 401, 20):
        # Draw lines at 45 degrees
        x = i
        y = i
        
        if x >= 0 and y >= 0:
            draw_mirrored_line(0, 0, x, y, colors[(abs(i)//20) % len(colors)])
        
        screen.update()

def draw_starburst_mirror():
    """Draw starburst pattern with mirrors"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    for i in range(0, 360, 15):
        angle = i
        radius = 350
        
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        if x >= 0 and y >= 0:
            draw_mirrored_line(0, 0, x, y, colors[(i//15) % len(colors)])
        
        screen.update()

def draw_mandala_mirror():
    """Draw intricate mandala pattern with mirroring"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    for ring in range(1, 6):
        radius = ring * 70
        points = 8 * ring
        
        for i in range(points):
            angle = i * (360 / points)
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            if x >= 0 and y >= 0:
                color = colors[(ring + i) % len(colors)]
                plot_mirrored(x, y, color)
                
                # Draw connecting arcs
                next_angle = ((i + 1) % points) * (360 / points)
                x2 = radius * math.cos(math.radians(next_angle))
                y2 = radius * math.sin(math.radians(next_angle))
                
                if x2 >= 0 and y2 >= 0:
                    draw_mirrored_line(x, y, x2, y2, color)
        
        screen.update()

def draw_heart_mirror():
    """Draw heart shape mirrored across both axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    # Generate heart shape points (first quadrant only)
    points = []
    for t in range(0, 91):
        t_rad = math.radians(t)
        # Parametric heart equation
        x = 16 * math.sin(t_rad) ** 3
        y = 13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad)
        points.append((x * 12, y * 12))
    
    # Connect points
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        draw_mirrored_line(x1, y1, x2, y2, colors[i % len(colors)])
        
        if i % 10 == 0:
            screen.update()
    
    # Add center dot
    plot_mirrored(0, 0, "red")

def draw_tree_mirror():
    """Draw fractal tree mirrored across axes"""
    pen.clear()
    draw_axes()
    
    colors = color_palettes[current_color_palette]
    
    def draw_branch(x, y, length, angle, depth):
        if depth == 0 or length < 5:
            return
        
        x2 = x + length * math.cos(math.radians(angle))
        y2 = y + length * math.sin(math.radians(angle))
        
        if x >= 0 and y >= 0:
            draw_mirrored_line(int(x), int(y), int(x2), int(y2), colors[depth % len(colors)])
        
        # Recursive branches
        draw_branch(x2, y2, length * 0.7, angle + 30, depth - 1)
        draw_branch(x2, y2, length * 0.7, angle - 30, depth - 1)
    
    draw_branch(0, 0, 80, 90, 8)
    screen.update()

# UI Controls
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 470)
    title.write("🪞 MIRROR PATTERN - X & Y AXES SYMMETRY 🪞", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -480)
    instructions.write("1=Star 2=Spiral 3=Flower 4=Geometric 5=Circle 6=Diagonal 7=Starburst 8=Mandala 9=Heart 0=Tree | C=Color A=Axes R=Redraw ESC=Exit",
                       align="center", font=("Arial", 8, "normal"))

def draw_current():
    """Draw the currently selected pattern"""
    pen.clear()
    
    if current_pattern == 1:
        draw_star_pattern()
    elif current_pattern == 2:
        draw_spiral_quadrants()
    elif current_pattern == 3:
        draw_flower_mirror()
    elif current_pattern == 4:
        draw_geometric_mirror()
    elif current_pattern == 5:
        draw_circle_mirror()
    elif current_pattern == 6:
        draw_diagonal_mirror()
    elif current_pattern == 7:
        draw_starburst_mirror()
    elif current_pattern == 8:
        draw_mandala_mirror()
    elif current_pattern == 9:
        draw_heart_mirror()
    elif current_pattern == 10:
        draw_tree_mirror()
    
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
def set_pattern_0(): global current_pattern; current_pattern = 10; draw_current()

def change_color():
    global current_color_palette
    current_color_palette = (current_color_palette + 1) % len(color_palettes)
    draw_current()

def toggle_axes():
    global show_axes
    show_axes = not show_axes
    draw_current()

def redraw():
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
screen.onkey(change_color, "c")
screen.onkey(toggle_axes, "a")
screen.onkey(redraw, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("     MIRROR PATTERNS - X & Y AXES SYMMETRY")
print("=" * 60)
print()
print("Every shape in the first quadrant is mirrored to all 4 quadrants!")
print()
print("PATTERNS:")
print("  1 - Star Pattern: Radiating star with 8 points")
print("  2 - Spiral Quadrants: Expanding spiral in all quadrants")
print("  3 - Flower Mirror: Petal shapes mirrored perfectly")
print("  4 - Geometric Mirror: Concentric geometric shapes")
print("  5 - Circle Mirror: Quarter circles reflected")
print("  6 - Diagonal Mirror: 45-degree line pattern")
print("  7 - Starburst Mirror: Radiating starburst")
print("  8 - Mandala Mirror: Intricate mandala design")
print("  9 - Heart Mirror: Heart shape quadrupled")
print("  0 - Tree Mirror: Fractal tree in 4 quadrants")
print()
print("CONTROLS:")
print("  0-9   - Select pattern")
print("  C     - Change color palette")
print("  A     - Toggle axes visibility")
print("  R     - Redraw")
print("  ESC   - Exit")
print()
print("Quadrant symmetry creates perfectly balanced designs!")

draw_star_pattern()
screen.mainloop()