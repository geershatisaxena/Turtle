import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# User preferences (modify these)
num_triangles = 80     # Number of triangles
start_size = 10         # Starting triangle size
size_increment = 2      # How much size increases each step
rotation_angle = 18     # Rotation angle between triangles (degrees)
color_mode = "rainbow"  # "rainbow", "gradient", "single"
fill_triangles = True   # Fill triangles or not

# Color setup
if color_mode == "rainbow":
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
elif color_mode == "gradient":
    colors = ["darkred", "red", "orange", "gold", "yellow", "lightyellow"]
else:
    colors = ["cyan"] * num_triangles

# Draw triangle spiral
size = start_size
for i in range(num_triangles):
    # Set color
    if color_mode == "gradient":
        color_index = int(i * len(colors) / num_triangles)
    else:
        color_index = i % len(colors)
    
    t.pencolor(colors[color_index])
    if fill_triangles:
        t.fillcolor(colors[(color_index + 2) % len(colors)])
        t.begin_fill()
    
    # Draw triangle
    for _ in range(3):
        t.forward(size)
        t.left(120)
    
    if fill_triangles:
        t.end_fill()
    
    # Rotate and increase size
    t.left(rotation_angle)
    size += size_increment

# Add information
t.penup()
t.goto(0, 250)
t.pencolor("white")
t.write("SPIRAL OF TRIANGLES", align="center", font=("Arial", 20, "bold"))
t.goto(0, 220)
t.write(f"Triangles: {num_triangles} | Start: {start_size}px | Rotation: {rotation_angle}°", 
        align="center", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()