import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(3)

# User preferences (modify these)
num_squares = 48          # Number of squares in rotation
square_size = 120         # Size of each square
rotation_angle = 360 / num_squares  # Auto-calculate rotation
color_mode = "rainbow"    # "rainbow", "gradient", "single"
fill_enabled = True       # Fill squares or not

# Color setup
if color_mode == "rainbow":
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta"]
elif color_mode == "gradient":
    colors = ["darkred", "red", "orange", "gold", "yellow", "lightyellow"]
else:
    colors = ["cyan"] * num_squares

# Draw rotating squares
for i in range(num_squares):
    # Set color
    if color_mode == "gradient":
        color_index = int(i * len(colors) / num_squares)
    else:
        color_index = i % len(colors)
    
    t.pencolor(colors[color_index])
    
    if fill_enabled:
        t.fillcolor(colors[(color_index + 2) % len(colors)])
        t.begin_fill()
    
    # Draw square
    for _ in range(4):
        t.forward(square_size)
        t.left(90)
    
    if fill_enabled:
        t.end_fill()
    
    # Rotate
    t.left(rotation_angle)

# Add information
t.penup()
t.goto(0, 200)
t.pencolor("white")
t.write("ROTATING SQUARE PATTERN", align="center", font=("Arial", 20, "bold"))
t.goto(0, 170)
t.write(f"{num_squares} squares | Size: {square_size}px | Rotation: {rotation_angle}°", 
        align="center", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()