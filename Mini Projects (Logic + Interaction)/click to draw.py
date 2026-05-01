import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Click-to-Draw Program")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic updates for smooth drawing

# Create drawing turtle
drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()
drawer.hideturtle()

# Create UI text turtle
ui_text = turtle.Turtle()
ui_text.speed(0)
ui_text.color("black")
ui_text.penup()
ui_text.hideturtle()

# Global variables
current_shape = "circle"  # Default shape
current_color = "blue"    # Default color
shapes = ["circle", "square", "triangle", "star"]
colors = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan"]

# Draw UI panel
def draw_ui():
    ui_text.clear()
    
    # Draw UI background
    ui_text.goto(-380, 260)
    ui_text.pendown()
    ui_text.color("lightgray")
    ui_text.begin_fill()
    for _ in range(2):
        ui_text.forward(760)
        ui_text.right(90)
        ui_text.forward(50)
        ui_text.right(90)
    ui_text.end_fill()
    ui_text.penup()
    
    # Display current settings
    ui_text.color("black")
    ui_text.goto(-350, 280)
    ui_text.write(f"Shape: {current_shape.upper()} | Color: {current_color.upper()}", 
                  font=("Arial", 14, "bold"))
    
    # Display instructions
    ui_text.goto(-350, 265)
    ui_text.write("Click: Draw shape | 1:Circle 2:Square 3:Triangle 4:Star | C:Change Color | D:Clear All | R:Random", 
                  font=("Arial", 9, "normal"))

# Function to draw a shape at (x, y)
def draw_shape(x, y):
    drawer.goto(x, y)
    drawer.color(current_color)
    drawer.pendown()
    drawer.begin_fill()
    
    size = 30  # Base size for shapes
    
    if current_shape == "circle":
        drawer.circle(size)
    
    elif current_shape == "square":
        for _ in range(4):
            drawer.forward(size * 2)
            drawer.right(90)
    
    elif current_shape == "triangle":
        for _ in range(3):
            drawer.forward(size * 2)
            drawer.left(120)
    
    elif current_shape == "star":
        for _ in range(5):
            drawer.forward(size * 2)
            drawer.right(144)
    
    drawer.end_fill()
    drawer.penup()

# Shape selection functions
def set_circle():
    global current_shape
    current_shape = "circle"
    draw_ui()

def set_square():
    global current_shape
    current_shape = "square"
    draw_ui()

def set_triangle():
    global current_shape
    current_shape = "triangle"
    draw_ui()

def set_star():
    global current_shape
    current_shape = "star"
    draw_ui()

# Change color
def change_color():
    global current_color, colors, current_color_index
    # Cycle through colors
    current_color_index = (colors.index(current_color) + 1) % len(colors)
    current_color = colors[current_color_index]
    draw_ui()

# Random color
def random_color():
    import random
    global current_color
    current_color = random.choice(colors)
    draw_ui()

# Clear all drawings
def clear_all():
    drawer.clear()
    draw_ui()

# Keyboard bindings
screen.listen()
screen.onkey(set_circle, "1")
screen.onkey(set_square, "2")
screen.onkey(set_triangle, "3")
screen.onkey(set_star, "4")
screen.onkey(change_color, "c")
screen.onkey(random_color, "r")
screen.onkey(clear_all, "d")

# Bind click event
screen.onclick(draw_shape)

# Initial UI
draw_ui()

# Give instructions in console
print("=== CLICK-TO-DRAW PROGRAM ===")
print("Click anywhere to draw the selected shape")
print("Press 1: Circle")
print("Press 2: Square")
print("Press 3: Triangle")
print("Press 4: Star")
print("Press C: Change color")
print("Press R: Random color")
print("Press D: Clear all drawings")

# Keep window open
screen.mainloop()