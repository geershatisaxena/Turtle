import turtle

# Setup
t = turtle.Turtle()
t.speed(200)
turtle.bgcolor("black")
t.pensize(2)

# Color palettes
palette1 = ["red", "crimson", "darkred"]
palette2 = ["blue", "deepskyblue", "cyan"]
palette3 = ["green", "lime", "lightgreen"]
palette4 = ["purple", "magenta", "violet"]

# Draw complex pattern using 4 levels of nested loops
patterns = 8  # Number of pattern repetitions

for pattern in range(patterns):
    # Choose color palette based on pattern
    if pattern < 2:
        colors = palette1
    elif pattern < 4:
        colors = palette2
    elif pattern < 6:
        colors = palette3
    else:
        colors = palette4
    
    for size_mult in range(1, 4):
        t.pencolor(colors[size_mult - 1])
        t.fillcolor(colors[size_mult - 1])
        t.begin_fill()
        
        # Draw a star-like shape
        for _ in range(25):
            t.forward(50 * size_mult)
            t.left(144)
        
        t.end_fill()
    
    t.left(360 / patterns)

# Add decorative circles
t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("white")
t.circle(100)
t.circle(120)

t.hideturtle()
turtle.done()