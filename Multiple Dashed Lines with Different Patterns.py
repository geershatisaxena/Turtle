import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
turtle.bgcolor("black")

# Function to draw dashed line
def draw_dashed_line(y_pos, dash_len, gap_len, color, thickness):
    t.penup()
    t.goto(-300, y_pos)
    t.pendown()
    t.pencolor(color)
    t.pensize(thickness)
    
    for _ in range(15):
        t.forward(dash_len)
        t.penup()
        t.forward(gap_len)
        t.pendown()

# Draw multiple dashed lines with different patterns
draw_dashed_line(200, 30, 10, "red", 4)      # Long dash, short gap
draw_dashed_line(150, 20, 20, "green", 4)    # Equal dash and gap
draw_dashed_line(100, 10, 30, "blue", 4)     # Short dash, long gap
draw_dashed_line(50, 15, 15, "yellow", 4)    # Dotted style
draw_dashed_line(0, 40, 20, "orange", 5)     # Thick dashes
draw_dashed_line(-50, 8, 12, "purple", 3)    # Small dashes
draw_dashed_line(-100, 25, 25, "cyan", 4)    # Equal pattern
draw_dashed_line(-150, 50, 10, "pink", 6)    # Very long dashes

# Add labels
t.penup()
t.goto(-350, 195)
t.pencolor("white")
t.write("Long Dash, Short Gap", font=("Arial", 10, "bold"))

t.goto(-350, 145)
t.write("Equal Dash & Gap", font=("Arial", 10, "bold"))

t.goto(-350, 95)
t.write("Short Dash, Long Gap", font=("Arial", 10, "bold"))

t.goto(-350, 45)
t.write("Dotted Style", font=("Arial", 10, "bold"))

t.hideturtle()
turtle.done()