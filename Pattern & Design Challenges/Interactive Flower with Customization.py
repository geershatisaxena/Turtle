import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("lightblue")
t.pensize(2)

# User preferences (modify these)
num_petals = 12        # Number of petals (6-24)
petal_size = 80        # Size of petals (50-120)
petal_color = "pink"   # Petal color
center_color = "yellow" # Center color
outline_color = "red"   # Outline color
petal_shape = "rounded" # "rounded", "pointed", "heart"

# Function to draw rounded petal
def rounded_petal(size):
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)

# Function to draw pointed petal
def pointed_petal(size):
    t.forward(size)
    t.left(30)
    t.forward(size/1.5)
    t.left(120)
    t.forward(size/1.5)
    t.left(30)
    t.forward(size)

# Function to draw heart petal
def heart_petal(size):
    t.left(45)
    t.forward(size/1.5)
    t.circle(size/3, 180)
    t.forward(size/1.5)
    t.left(135)

# Draw petals
for i in range(num_petals):
    t.pencolor(outline_color)
    t.fillcolor(petal_color)
    t.begin_fill()
    
    if petal_shape == "rounded":
        rounded_petal(petal_size)
    elif petal_shape == "pointed":
        pointed_petal(petal_size)
    elif petal_shape == "heart":
        heart_petal(petal_size)
    
    t.end_fill()
    t.left(360 / num_petals)

# Draw center
t.penup()
t.goto(0, -20)
t.pendown()
t.fillcolor(center_color)
t.begin_fill()
t.circle(20)
t.end_fill()

# Add center dots
t.pencolor("brown")
for i in range(12):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 30)
    t.forward(12)
    t.pendown()
    t.dot(4)

# Add title
t.penup()
t.goto(0, 200)
t.pencolor("darkblue")
t.write("MY FLOWER", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()