import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Recursive Spiral Pattern")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the drawing turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.penup()
spiral.goto(0, 0)
spiral.pendown()
spiral.hideturtle()

# Color settings
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta", "pink", "white"]
current_color_index = 0
gradient_mode = True

# Spiral parameters
length = 10
angle = 30
shrink = 0.98  # Shrink factor for each recursion
min_length = 2
max_depth = 100
spiral_type = "basic"  # Default spiral type

# UI elements
info = turtle.Turtle()
info.speed(0)
info.color("white")
info.penup()
info.hideturtle()

def recursive_spiral(length, angle, shrink, min_length, depth=0):
    """
    Draw a recursive spiral pattern
    
    Each recursive call draws a segment, rotates, and calls itself
    with a reduced length until the minimum length is reached.
    """
    global current_color_index
    
    if length < min_length:
        return
    
    # Color cycling for visual effect
    if gradient_mode:
        spiral.color(colors[current_color_index % len(colors)])
        current_color_index += 1
    
    # Draw the current segment
    spiral.forward(length)
    
    # Turn by the specified angle
    spiral.right(angle)
    
    # Recursive call with reduced length
    recursive_spiral(length * shrink, angle, shrink, min_length, depth + 1)

def recursive_spiral_variable_angle(length, angle_start, angle_increment, shrink, min_length):
    """
    Recursive spiral with changing angle each iteration
    """
    global current_color_index
    
    if length < min_length:
        return
    
    if gradient_mode:
        spiral.color(colors[current_color_index % len(colors)])
        current_color_index += 1
    
    spiral.forward(length)
    spiral.right(angle_start)
    
    recursive_spiral_variable_angle(length * shrink, 
                                    angle_start + angle_increment, 
                                    angle_increment, 
                                    shrink, 
                                    min_length)

def double_recursive_spiral(length, angle, shrink, min_length, direction=1):
    """
    Double spiral that goes both left and right recursively
    Creates a branching spiral pattern
    """
    global current_color_index
    
    if length < min_length:
        return
    
    if gradient_mode:
        spiral.color(colors[current_color_index % len(colors)])
        current_color_index += 1
    
    spiral.forward(length)
    
    # Save position and heading for second branch
    pos = spiral.pos()
    heading = spiral.heading()
    
    # First branch
    spiral.right(angle * direction)
    double_recursive_spiral(length * shrink, angle, shrink, min_length, direction)
    
    # Second branch (opposite direction)
    spiral.penup()
    spiral.goto(pos)
    spiral.setheading(heading)
    spiral.pendown()
    spiral.left(angle * direction)
    double_recursive_spiral(length * shrink, angle, shrink, min_length, -direction)

def fibonacci_spiral(steps, max_steps, radius=5, angle=15):
    """
    Fibonacci-inspired recursive spiral using arcs
    """
    global current_color_index
    
    if steps > max_steps:
        return
    
    if gradient_mode:
        spiral.color(colors[steps % len(colors)])
    
    # Draw arc with increasing radius
    spiral.circle(radius, angle)
    
    # Recursive call with Fibonacci-like growth
    new_radius = radius * 1.05
    fibonacci_spiral(steps + 1, max_steps, new_radius, angle)

def square_spiral(length, depth, max_depth):
    """
    Recursive square spiral (like a growing square)
    """
    global current_color_index
    
    if depth > max_depth:
        return
    
    if gradient_mode:
        spiral.color(colors[depth % len(colors)])
    
    for _ in range(4):
        spiral.forward(length)
        spiral.right(90)
    
    spiral.right(15)
    square_spiral(length * 1.05, depth + 1, max_depth)

def nautilus_spiral(length, angle, shrink, min_length):
    """
    Nautilus shell inspired spiral with changing colors
    """
    global current_color_index
    
    if length < min_length:
        return
    
    if gradient_mode:
        spiral.color(colors[current_color_index % len(colors)])
        current_color_index += 1
    
    spiral.forward(length)
    spiral.right(angle)
    
    nautilus_spiral(length * shrink, angle + 2, shrink, min_length)

def clear_and_draw():
    """Clear screen and redraw with current parameters"""
    global current_color_index
    current_color_index = 0
    spiral.clear()
    spiral.penup()
    spiral.goto(0, 0)
    spiral.setheading(0)
    spiral.pendown()
    draw_selected_spiral()
    update_info()

def draw_selected_spiral():
    """Draw the currently selected spiral type"""
    if spiral_type == "basic":
        recursive_spiral(length, angle, shrink, min_length)
    elif spiral_type == "variable":
        recursive_spiral_variable_angle(length, 30, 2, shrink, min_length)
    elif spiral_type == "double":
        double_recursive_spiral(length, angle, shrink, min_length)
    elif spiral_type == "fibonacci":
        fibonacci_spiral(0, 200)
    elif spiral_type == "square":
        square_spiral(20, 0, 30)
    elif spiral_type == "nautilus":
        nautilus_spiral(length, 25, 0.97, 3)
    
    screen.update()

def change_color_mode():
    """Toggle gradient color mode on/off"""
    global gradient_mode
    gradient_mode = not gradient_mode
    if not gradient_mode:
        spiral.color("white")
    clear_and_draw()

def increase_length():
    """Increase initial segment length"""
    global length
    length = min(length + 5, 50)
    clear_and_draw()

def decrease_length():
    """Decrease initial segment length"""
    global length
    length = max(length - 5, 5)
    clear_and_draw()

def increase_angle():
    """Increase rotation angle"""
    global angle
    angle = min(angle + 5, 180)
    clear_and_draw()

def decrease_angle():
    """Decrease rotation angle"""
    global angle
    angle = max(angle - 5, 10)
    clear_and_draw()

def increase_shrink():
    """Increase shrink factor (closer to 1 = longer spiral)"""
    global shrink
    shrink = min(shrink + 0.01, 0.99)
    clear_and_draw()

def decrease_shrink():
    """Decrease shrink factor"""
    global shrink
    shrink = max(shrink - 0.01, 0.85)
    clear_and_draw()

def increase_depth():
    """Increase spiral depth"""
    global min_length
    min_length = max(min_length - 1, 1)
    clear_and_draw()

def decrease_depth():
    """Decrease spiral depth"""
    global min_length
    min_length = min(min_length + 1, 15)
    clear_and_draw()

def change_spiral_type():
    """Cycle through spiral types"""
    global spiral_type
    types = ["basic", "variable", "double", "fibonacci", "square", "nautilus"]
    current_idx = types.index(spiral_type)
    spiral_type = types[(current_idx + 1) % len(types)]
    clear_and_draw()

def randomize():
    """Randomize all spiral parameters"""
    global length, angle, shrink, min_length, spiral_type, gradient_mode
    length = random.randint(5, 30)
    angle = random.randint(15, 120)
    shrink = random.uniform(0.90, 0.99)
    min_length = random.randint(2, 10)
    gradient_mode = random.choice([True, False])
    
    types = ["basic", "variable", "double", "fibonacci", "square", "nautilus"]
    spiral_type = random.choice(types)
    
    clear_and_draw()

def update_info():
    """Update on-screen information display"""
    info.clear()
    info.goto(-450, 360)
    info.write(f"Spiral: {spiral_type.upper()} | Length: {length} | Angle: {angle}° | "
               f"Shrink: {shrink:.2f} | Min Length: {min_length}",
               font=("Arial", 10, "normal"))
    info.goto(-450, 340)
    info.write("Controls: +/-:Length | [/]:Angle | </>:Shrink | ", 
               font=("Arial", 10, "normal"))
    info.goto(-450, 320)
    info.write("D:Depth | T:Type | C:Colors | R:Random | SPACE:Redraw | ESC:Exit",
               font=("Arial", 10, "normal"))

# Draw title and border
def draw_border():
    border = turtle.Turtle()
    border.speed(0)
    border.color("gray")
    border.penup()
    border.goto(-480, -370)
    border.pendown()
    border.pensize(2)
    for _ in range(2):
        border.forward(960)
        border.right(90)
        border.forward(760)
        border.right(90)
    border.hideturtle()
    
    title = turtle.Turtle()
    title.speed(0)
    title.color("gold")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🌀 RECURSIVE SPIRAL PATTERN 🌀", align="center", font=("Arial", 16, "bold"))
    title.goto(0, 345)
    title.write("Where Math Meets Art", align="center", font=("Arial", 10, "normal"))

draw_border()
update_info()

# Keyboard bindings
screen.listen()
screen.onkey(increase_length, "plus")
screen.onkey(increase_length, "equal")
screen.onkey(decrease_length, "minus")
screen.onkey(increase_angle, "bracketright")
screen.onkey(decrease_angle, "bracketleft")
screen.onkey(increase_shrink, "period")
screen.onkey(decrease_shrink, "comma")
screen.onkey(increase_depth, "d")
screen.onkey(decrease_depth, "D")
screen.onkey(change_spiral_type, "t")
screen.onkey(change_color_mode, "c")
screen.onkey(randomize, "r")
screen.onkey(clear_and_draw, "space")
screen.onkey(lambda: screen.bye(), "Escape")

# Print console instructions
print("=" * 50)
print("     RECURSIVE SPIRAL PATTERN")
print("=" * 50)
print()
print("A recursive function draws segments, rotates, and calls itself")
print("until reaching a minimum length, creating beautiful spirals!")
print()
print("CONTROLS:")
print("  + / -     - Increase/Decrease segment length")
print("  [ / ]     - Increase/Decrease rotation angle")
print("  < / >     - Increase/Decrease shrink factor (0.85-0.99)")
print("  d / D     - Increase/Decrease spiral depth")
print("  T         - Change spiral type")
print("     • basic    - Standard recursive spiral")
print("     • variable - Changing angle each step")
print("     • double   - Branching double spiral")
print("     • fibonacci- Fibonacci spiral with arcs")
print("     • square   - Growing square spiral")
print("     • nautilus - Nautilus shell pattern")
print("  C         - Toggle gradient colors")
print("  R         - Randomize all parameters")
print("  SPACE     - Redraw current spiral")
print("  ESC       - Exit program")
print()
print("TIP: Try different angles to create unique patterns!")
print("     Golden angle (~137.5°) creates beautiful natural spirals")

# Draw initial spiral
clear_and_draw()

# Keep window open
screen.mainloop()