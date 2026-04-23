import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# User preferences (modify these)
num_segments = 48       # Number of pattern segments
pattern_type = "star"   # "star", "triangle", "square", "flower"
color_mode = "rainbow"  # "rainbow", "gradient", "single"

# Color setup
if color_mode == "rainbow":
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
elif color_mode == "gradient":
    colors = ["darkred", "red", "orange", "gold", "yellow", "lightyellow"]
else:
    colors = ["cyan"] * num_segments

# Function to draw different patterns
def draw_pattern(type, size):
    if type == "star":
        for _ in range(5):
            t.forward(size)
            t.left(144)
    
    elif type == "triangle":
        for _ in range(3):
            t.forward(size)
            t.left(120)
    
    elif type == "square":
        for _ in range(4):
            t.forward(size)
            t.left(90)
    
    elif type == "flower":
        for _ in range(6):
            t.circle(size/2, 60)
            t.left(120)
            t.circle(size/2, 60)
            t.left(60)

# Draw kaleidoscope
for i in range(num_segments):
    # Set color
    if color_mode == "gradient":
        color_index = int(i * len(colors) / num_segments)
    else:
        color_index = i % len(colors)
    
    t.pencolor(colors[color_index])
    t.fillcolor(colors[(color_index + 2) % len(colors)])
    t.begin_fill()
    
    # Draw pattern
    draw_pattern(pattern_type, 100)
    
    t.end_fill()
    t.left(360 / num_segments)

# Add information
t.penup()
t.goto(0, 250)
t.pencolor("white")
t.write("KALEIDOSCOPE PATTERN", align="center", font=("Arial", 24, "bold"))
t.goto(0, 220)
t.write(f"Segments: {num_segments} | Pattern: {pattern_type} | Color: {color_mode}", 
        align="center", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()