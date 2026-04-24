import turtle
import math  # Import math for cos, sin, pi

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# User preferences (modify these)
ring_radius = 180      # Radius of the ring
num_shapes = 16        # Number of shapes in the ring
shape_type = "star"    # "circle", "square", "triangle", "star", "flower"
shape_size = 35        # Size of each shape
color_scheme = "rainbow"  # "rainbow", "gradient", "mono"
connect_shapes = False   # Connect shapes with lines
fill_shapes = True        # Fill shapes with color

# Color setup
if color_scheme == "rainbow":
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
elif color_scheme == "gradient":
    colors = ["darkred", "red", "orange", "gold", "yellow", "lightyellow"]
else:
    colors = ["cyan"] * num_shapes

# Function to draw different shapes
def draw_shape(x, y, heading, shape, size, color, fill):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    
    t.pencolor(color)
    if fill:
        t.fillcolor(color)
        t.begin_fill()
    
    if shape == "circle":
        t.circle(size)
    
    elif shape == "square":
        for _ in range(4):
            t.forward(size)
            t.left(90)
    
    elif shape == "triangle":
        for _ in range(3):
            t.forward(size)
            t.left(120)
    
    elif shape == "star":
        for _ in range(5):
            t.forward(size)
            t.left(144)
    
    elif shape == "flower":
        for _ in range(6):
            t.circle(size/2, 60)
            t.left(120)
            t.circle(size/2, 60)
            t.left(60)
    
    if fill:
        t.end_fill()

# Store positions for connections
positions = []

# Draw the ring
for i in range(num_shapes):
    angle = i * (360 / num_shapes)
    # Use math.cos and math.sin instead of turtle.cos/turtle.sin
    x = ring_radius * math.cos(math.radians(angle))
    y = ring_radius * math.sin(math.radians(angle))
    positions.append((x, y))
    
    # Set color
    if color_scheme == "gradient":
        color_index = int(i * len(colors) / num_shapes)
    else:
        color_index = i % len(colors)
    
    # Additional rotation for some shapes
    shape_heading = angle
    if shape_type == "square":
        shape_heading += 45  # Rotate squares for diamond look
    
    draw_shape(x, y, shape_heading, shape_type, shape_size, colors[color_index], fill_shapes)

# Connect shapes if enabled
if connect_shapes:
    t.pencolor("white")
    t.pensize(2)
    for i in range(num_shapes):
        t.penup()
        t.goto(positions[i])
        t.pendown()
        t.goto(positions[(i + 1) % num_shapes])

# Add center design
t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("gold")
t.fillcolor("orange")
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(0, 0)
t.dot(12, "white")
t.dot(6, "yellow")

# Add information
t.penup()
t.goto(0, 280)
t.pencolor("white")
t.write("CIRCULAR RING OF SHAPES", align="center", font=("Arial", 20, "bold"))
t.goto(0, 250)
t.write(f"Radius: {ring_radius}px | Shapes: {num_shapes} | Type: {shape_type}", 
        align="center", font=("Arial", 12, "normal"))
t.goto(0, 225)
t.write(f"Color: {color_scheme} | Fill: {fill_shapes} | Connected: {connect_shapes}", 
        align="center", font=("Arial", 11, "normal"))

t.hideturtle()
turtle.done()