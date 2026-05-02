import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Recursive Spiral Pattern")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the drawing turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
spiral_turtle.penup()
spiral_turtle.goto(0, 0)
spiral_turtle.pendown()
spiral_turtle.hideturtle()

# Color palettes
color_palettes = {
    "rainbow": ["red", "orange", "yellow", "green", "blue", "purple"],
    "ocean": ["darkblue", "blue", "cyan", "lightblue", "aquamarine"],
    "fire": ["darkred", "red", "orange", "gold", "yellow"],
    "forest": ["darkgreen", "green", "limegreen", "yellowgreen"],
    "pastel": ["pink", "lightpink", "lavender", "peachpuff", "lightyellow"],
    "neon": ["lime", "magenta", "cyan", "yellow", "hotpink"]
}
current_palette = "rainbow"
color_index = 0

# Spiral parameters
current_length = 5
current_angle = 90
growth_factor = 1.05
max_depth = 150
current_depth = 0
spiral_type = "square"  # square, triangle, circle, fibonacci

# UI elements
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("white")
info_display.penup()
info_display.hideturtle()

def recursive_spiral(length, angle, depth, max_depth, color_cycle=True):
    """
    Draw a recursive spiral pattern
    
    Parameters:
    - length: current segment length
    - angle: turning angle for spiral
    - depth: current recursion depth
    - max_depth: maximum recursion depth
    - color_cycle: whether to cycle through colors
    """
    global color_index
    
    if depth > max_depth:
        return
    
    # Change color based on depth
    if color_cycle:
        palette = color_palettes[current_palette]
        spiral_turtle.color(palette[color_index % len(palette)])
        color_index += 1
    
    # Draw current segment
    spiral_turtle.forward(length)
    
    # Turn by specified angle
    spiral_turtle.right(angle)
    
    # Recursive call with slightly increased length
    new_length = length * growth_factor
    recursive_spiral(new_length, angle, depth + 1, max_depth, color_cycle)

def fibonacci_spiral(step, angle, depth, max_depth):
    """
    Draw a Fibonacci spiral (golden ratio)
    """
    global color_index
    
    if depth > max_depth:
        return
    
    # Fibonacci-inspired length progression
    fib_length = step * (1.618 ** (depth / 10))
    
    palette = color_palettes[current_palette]
    spiral_turtle.color(palette[color_index % len(palette)])
    color_index += 1
    
    # Draw arc instead of straight line for Fibonacci spiral
    spiral_turtle.circle(fib_length, angle)
    
    new_step = step * 1.05
    fibonacci_spiral(new_step, angle, depth + 1, max_depth)

def triangular_spiral(length, angle, depth, max_depth):
    """
    Draw a triangular spiral pattern
    """
    global color_index
    
    if depth > max_depth:
        return
    
    palette = color_palettes[current_palette]
    spiral_turtle.color(palette[color_index % len(palette)])
    color_index += 1
    
    # Draw triangle-like segments
    for _ in range(3):
        spiral_turtle.forward(length)
        spiral_turtle.right(120)
    
    spiral_turtle.right(angle)
    new_length = length * growth_factor
    triangular_spiral(new_length, angle + 5, depth + 1, max_depth)

def circular_spiral(radius, angle, depth, max_depth):
    """
    Draw a circular recursive spiral
    """
    global color_index
    
    if depth > max_depth:
        return
    
    palette = color_palettes[current_palette]
    spiral_turtle.color(palette[color_index % len(palette)])
    color_index += 1
    
    # Draw expanding circles
    spiral_turtle.circle(radius)
    spiral_turtle.right(angle)
    
    new_radius = radius * growth_factor
    circular_spiral(new_radius, angle, depth + 1, max_depth)

def draw_spiral():
    """Draw the selected spiral type"""
    global color_index, current_depth
    color_index = 0
    spiral_turtle.clear()
    spiral_turtle.penup()
    spiral_turtle.goto(0, 0)
    spiral_turtle.setheading(0)
    spiral_turtle.pendown()
    
    if spiral_type == "square":
        recursive_spiral(current_length, current_angle, 0, max_depth, True)
    elif spiral_type == "fibonacci":
        fibonacci_spiral(10, 30, 0, max_depth // 2)
    elif spiral_type == "triangle":
        triangular_spiral(current_length, 10, 0, max_depth // 2)
    elif spiral_type == "circle":
        circular_spiral(10, 15, 0, max_depth // 2)
    
    screen.update()
    update_info()

def draw_multiple_spirals():
    """Draw multiple spirals from different starting positions"""
    spiral_turtle.clear()
    positions = [(-200, 200), (200, 200), (-200, -200), (200, -200), (0, 0)]
    
    for i, (x, y) in enumerate(positions):
        spiral_turtle.penup()
        spiral_turtle.goto(x, y)
        spiral_turtle.setheading(i * 90)
        spiral_turtle.pendown()
        
        temp_type = spiral_type
        if spiral_type == "square":
            recursive_spiral(current_length, current_angle + i * 10, 0, 60, True)
        elif spiral_type == "fibonacci":
            fibonacci_spiral(8, 30 + i * 5, 0, 40)
    
    screen.update()
    update_info()

def draw_color_wheel():
    """Draw a spiral that creates a color wheel effect"""
    spiral_turtle.clear()
    spiral_turtle.penup()
    spiral_turtle.goto(0, 0)
    spiral_turtle.pendown()
    spiral_turtle.speed(0)
    
    for i in range(360):
        palette = color_palettes[current_palette]
        spiral_turtle.color(palette[i % len(palette)])
        spiral_turtle.forward(i / 10)
        spiral_turtle.right(15)
        spiral_turtle.forward(i / 20)
        spiral_turtle.right(15)
    
    screen.update()
    update_info()

def change_palette():
    """Cycle through color palettes"""
    global current_palette, color_index
    palettes = list(color_palettes.keys())
    current_index = palettes.index(current_palette)
    current_palette = palettes[(current_index + 1) % len(palettes)]
    color_index = 0
    draw_spiral()
    update_info()

def increase_complexity():
    """Increase spiral complexity (more depth)"""
    global max_depth, current_depth
    max_depth = min(max_depth + 20, 300)
    draw_spiral()
    update_info()

def decrease_complexity():
    """Decrease spiral complexity"""
    global max_depth
    max_depth = max(max_depth - 20, 30)
    draw_spiral()
    update_info()

def change_angle():
    """Change the turning angle for square spiral"""
    global current_angle, spiral_type
    if spiral_type == "square":
        current_angle = (current_angle + 5) % 180
        draw_spiral()
    update_info()

def change_growth():
    """Change the growth factor"""
    global growth_factor
    growth_factor = min(growth_factor + 0.02, 1.3)
    draw_spiral()
    update_info()

def decrease_growth():
    """Decrease the growth factor"""
    global growth_factor
    growth_factor = max(growth_factor - 0.02, 1.01)
    draw_spiral()
    update_info()

def set_spiral_type(type_name):
    """Change the spiral pattern type"""
    global spiral_type
    spiral_type = type_name
    draw_spiral()
    update_info()

def randomize():
    """Randomize all spiral parameters"""
    global current_angle, growth_factor, max_depth, current_palette, spiral_type
    
    current_angle = random.randint(45, 135)
    growth_factor = random.uniform(1.01, 1.2)
    max_depth = random.randint(50, 200)
    
    types = ["square", "fibonacci", "triangle", "circle"]
    spiral_type = random.choice(types)
    
    palettes = list(color_palettes.keys())
    current_palette = random.choice(palettes)
    
    draw_spiral()
    update_info()

def update_info():
    """Update on-screen information"""
    info_display.clear()
    info_display.goto(-450, 350)
    info_display.write(f"Spiral: {spiral_type.upper()} | Palette: {current_palette.upper()} | "
                       f"Angle: {current_angle}° | Growth: {growth_factor:.2f} | Depth: {max_depth}",
                       font=("Arial", 10, "normal"))
    info_display.goto(-450, 330)
    info_display.write("Controls: +/- Depth | [/] Angle | </> Growth | P: Palette | T: Type | "
                       "M: Multi | W: Wheel | R: Random | SPACE: Redraw",
                       font=("Arial", 10, "normal"))

# Draw decorative border
def draw_border():
    border = turtle.Turtle()
    border.speed(0)
    border.color("gray")
    border.penup()
    border.goto(-470, -370)
    border.pendown()
    border.pensize(2)
    for _ in range(2):
        border.forward(940)
        border.right(90)
        border.forward(740)
        border.right(90)
    border.hideturtle()

draw_border()
update_info()

# Keyboard bindings
screen.listen()
screen.onkey(increase_complexity, "plus")
screen.onkey(increase_complexity, "equal")
screen.onkey(decrease_complexity, "minus")
screen.onkey(change_angle, "bracketright")
screen.onkey(change_angle, "bracketleft")
screen.onkey(change_growth, "period")
screen.onkey(decrease_growth, "comma")
screen.onkey(change_palette, "p")
screen.onkey(lambda: set_spiral_type("square"), "1")
screen.onkey(lambda: set_spiral_type("fibonacci"), "2")
screen.onkey(lambda: set_spiral_type("triangle"), "3")
screen.onkey(lambda: set_spiral_type("circle"), "4")
screen.onkey(draw_multiple_spirals, "m")
screen.onkey(draw_color_wheel, "w")
screen.onkey(randomize, "r")
screen.onkey(draw_spiral, "space")
screen.onkey(lambda: screen.bye(), "Escape")

# Print console instructions
print("=== RECURSIVE SPIRAL PATTERN ===")
print()
print("A recursive spiral where each segment grows and rotates")
print()
print("CONTROLS:")
print("  + / -     - Increase/Decrease spiral complexity (depth)")
print("  [ / ]     - Change turning angle")
print("  < / >     - Change growth factor")
print("  P         - Change color palette")
print("  1,2,3,4   - Change spiral type (Square/Fibonacci/Triangle/Circle)")
print("  M         - Draw multiple spirals")
print("  W         - Draw color wheel spiral")
print("  R         - Randomize all parameters")
print("  SPACE     - Redraw current spiral")
print("  ESC       - Exit program")
print()
print("Each spiral type creates a unique recursive pattern!")
print("Fibonacci spiral uses the golden ratio for natural-looking spirals")

# Draw initial spiral
draw_spiral()

# Keep window open
screen.mainloop()