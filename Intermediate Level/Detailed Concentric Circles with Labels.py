import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("lightgray")
t.pensize(3)

# Draw concentric circles with measurements
radii = [50, 100, 150, 200, 250]
colors = ["red", "orange", "green", "blue", "purple"]

for i, radius in enumerate(radii):
    # Draw circle
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.pencolor(colors[i])
    t.pensize(4)
    t.circle(radius)
    
    # Add radius label
    t.penup()
    t.goto(radius + 10, 0)
    t.pencolor("black")
    t.write(f"r = {radius}px", font=("Arial", 12, "bold"))
    
    # Add diameter label
    t.penup()
    t.goto(radius + 10, -20)
    t.write(f"d = {radius * 2}px", font=("Arial", 10, "normal"))

# Add center dot
t.penup()
t.goto(0, 0)
t.pendown()
t.dot(15, "black")
t.write("Center", align="center", font=("Arial", 10, "bold"))

# Add title
t.penup()
t.goto(0, 280)
t.pencolor("darkblue")
t.write("CONCENTRIC CIRCLES", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()