import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Turtle Drawing App - Color Selection Keys")
screen.bgcolor("white")
screen.setup(width=900, height=700)

# Create the drawing pen
pen = turtle.Turtle()
pen.shape("circle")
pen.speed(0)
pen.pensize(3)
pen.penup()

# Drawing state
drawing = False
current_color = "black"

# Color palette with corresponding keys
color_palette = {
    "r": "red",
    "g": "green", 
    "b": "blue",
    "y": "yellow",
    "o": "orange",
    "p": "purple",
    "k": "black",
    "w": "white",
    "t": "brown",
    "c": "cyan",
    "m": "magenta",
    "l": "lightgray",
    "d": "gold",
    "e": "pink"
}

def create_color_palette_ui():
    """Create a visual color palette at the bottom of the screen"""
    # Palette background
    palette = turtle.Turtle()
    palette.speed(0)
    palette.color("lightgray")
    palette.penup()
    palette.goto(-440, -320)
    palette.pendown()
    palette.begin_fill()
    for _ in range(2):
        palette.forward(880)
        palette.right(90)
        palette.forward(60)
        palette.right(90)
    palette.end_fill()
    palette.hideturtle()
    
    # Create color swatches
    start_x = -420
    y_pos = -295
    spacing = 32
    
    colors_list = list(color_palette.items())
    for i, (key, color_name) in enumerate(colors_list):
        # Color swatch
        swatch = turtle.Turtle()
        swatch.speed(0)
        swatch.shape("square")
        swatch.color(color_name)
        swatch.shapesize(1.2, 1.2)
        swatch.penup()
        swatch.goto(start_x + i * spacing, y_pos)
        
        # Key label
        label = turtle.Turtle()
        label.speed(0)
        label.color("black")
        label.penup()
        label.hideturtle()
        label.goto(start_x + i * spacing, y_pos - 18)
        label.write(key.upper(), align="center", font=("Arial", 9, "bold"))

def update_ui():
    """Update UI to show current color and status"""
    ui_text.clear()
    status_text.clear()
    
    ui_text.goto(-440, 310)
    ui_text.write(f"Current Color: {current_color.upper()}", font=("Arial", 14, "bold"))
    
    status_text.goto(-440, 280)
    status = "DRAWING" if drawing else "PEN UP"
    status_text.write(f"Status: {status} | Pen Size: {pen.pensize()}", font=("Arial", 12, "normal"))

def start_drawing(x, y):
    """Start drawing when mouse is pressed"""
    global drawing
    drawing = True
    pen.pendown()
    pen.goto(x, y)
    update_ui()
    
    # Bind the drag event to the pen
    pen.ondrag(drag_drawing)

def drag_drawing(x, y):
    """Draw while dragging mouse"""
    if drawing:
        pen.goto(x, y)

def stop_drawing(x, y):
    """Stop drawing when mouse is released"""
    global drawing
    drawing = False
    pen.penup()
    pen.ondrag(None)  # Unbind drag
    update_ui()

def change_color(color):
    """Change the drawing color"""
    global current_color
    current_color = color
    pen.color(color)
    update_ui()

def increase_pen_size():
    """Increase pen thickness"""
    new_size = min(pen.pensize() + 2, 20)
    pen.pensize(new_size)
    update_ui()

def decrease_pen_size():
    """Decrease pen thickness"""
    new_size = max(pen.pensize() - 2, 1)
    pen.pensize(new_size)
    update_ui()

def clear_canvas():
    """Clear all drawings"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    if drawing:
        pen.pendown()
    update_ui()

def toggle_pen():
    """Toggle pen up/down"""
    global drawing
    drawing = not drawing
    if drawing:
        pen.pendown()
        pen.ondrag(drag_drawing)
    else:
        pen.penup()
        pen.ondrag(None)
    update_ui()

def change_shape():
    """Change pen shape"""
    shapes = ["circle", "square", "triangle", "arrow", "turtle"]
    current = pen.shape()
    next_index = (shapes.index(current) + 1) % len(shapes)
    pen.shape(shapes[next_index])

# Keyboard bindings for colors
screen.listen()
for key, color in color_palette.items():
    screen.onkey(lambda c=color: change_color(c), key)

# Additional controls
screen.onkey(increase_pen_size, "plus")
screen.onkey(increase_pen_size, "equal")
screen.onkey(decrease_pen_size, "minus")
screen.onkey(clear_canvas, "c")
screen.onkey(toggle_pen, "space")
screen.onkey(change_shape, "s")
screen.onkey(lambda: screen.bye(), "Escape")

# Mouse bindings
screen.onclick(start_drawing, 1)   # Left click to start
screen.onclick(stop_drawing, 3)    # Right click to stop

# UI turtles
ui_text = turtle.Turtle()
ui_text.speed(0)
ui_text.color("black")
ui_text.penup()
ui_text.hideturtle()

status_text = turtle.Turtle()
status_text.speed(0)
status_text.color("gray")
status_text.penup()
status_text.hideturtle()

# Create visual interface
create_color_palette_ui()
update_ui()

# Instruction display
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("darkgray")
instructions.penup()
instructions.hideturtle()
instructions.goto(-440, -360)
instructions.write("DRAWING INSTRUCTIONS:", font=("Arial", 10, "bold"))
instructions.goto(-440, -375)
instructions.write("Left-click & drag to draw | Right-click to stop drawing", 
                   font=("Arial", 9, "normal"))
instructions.goto(-440, -390)
instructions.write("COLOR KEYS: R G B Y O P K C M D(Gold) E(Pink) | W=White T=Brown L=Light Gray",
                   font=("Arial", 9, "normal"))
instructions.goto(-440, -405)
instructions.write("OTHER KEYS: +/-=Pen Size | C=Clear | Space=Pen Up/Down | S=Shape | ESC=Exit",
                   font=("Arial", 9, "normal"))

# Print console instructions
print("=== TURTLE DRAWING APP ===")
print()
print("DRAWING CONTROLS:")
print("  Left-click & drag - Draw on canvas")
print("  Right-click       - Stop drawing (pen up)")
print("  Space             - Toggle pen up/down")
print()
print("COLOR SELECTION KEYS:")
for key, color in color_palette.items():
    print(f"  {key.upper()} - {color}")
print()
print("OTHER CONTROLS:")
print("  + / = - Increase pen size")
print("  -     - Decrease pen size")
print("  C     - Clear canvas")
print("  S     - Change pen shape")
print("  ESC   - Exit program")

# Initial pen setup
pen.goto(0, 0)
pen.color("black")

# Keep window open
screen.mainloop()