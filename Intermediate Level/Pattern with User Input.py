import turtle

# Setup
t = turtle.Turtle()
t.speed(200)
turtle.bgcolor("black")
t.pensize(3)

# User preferences (modify these)
pattern_type = "grid"  # "grid", "checkerboard", "spiral", or "flower"
size = 40
rows = 15
cols = 12

# Color schemes
color_schemes = {
    "rainbow": ["red", "orange", "yellow", "green", "blue", "purple"],
    "cool": ["cyan", "blue", "purple", "magenta"],
    "warm": ["red", "orange", "yellow", "pink"],
    "mono": ["lightgreen", "green", "darkgreen", "lime"]
}

# Select color scheme
selected_scheme = color_schemes["rainbow"]

if pattern_type == "grid":
    for row in range(rows):
        for col in range(cols):
            t.penup()
            t.goto(col * size - 200, row * size - 150)
            t.pendown()
            t.pencolor(selected_scheme[(row + col) % len(selected_scheme)])
            for _ in range(4):
                t.forward(size)
                t.left(90)

elif pattern_type == "checkerboard":
    for row in range(rows):
        for col in range(cols):
            t.penup()
            t.goto(col * size - 200, row * size - 150)
            t.pendown()
            if (row + col) % 2 == 0:
                t.fillcolor("white")
            else:
                t.fillcolor("black")
            t.begin_fill()
            for _ in range(4):
                t.forward(size)
                t.left(90)
            t.end_fill()

elif pattern_type == "spiral":
    for i in range(50):
        t.pencolor(selected_scheme[i % len(selected_scheme)])
        for _ in range(4):
            t.forward(i * 2)
            t.left(90)
        t.left(15)

elif pattern_type == "flower":
    for i in range(12):
        t.pencolor(selected_scheme[i % len(selected_scheme)])
        t.fillcolor(selected_scheme[(i+1) % len(selected_scheme)])
        t.begin_fill()
        for _ in range(2):
            t.circle(60, 60)
            t.left(120)
            t.circle(60, 60)
            t.left(60)
        t.end_fill()
        t.left(30)

# Add title
t.penup()
t.goto(0, 250)
t.pencolor("white")
t.write(f"{pattern_type.upper()} PATTERN", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()