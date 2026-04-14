import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("lightgray")
t.pensize(3)

# Function to draw dashed line with labels
def draw_dashed_line_with_label(start_x, start_y, length, dash, gap, color, label):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.pencolor(color)
    
    segments = length // (dash + gap)
    
    # Draw the dashed line
    for _ in range(segments):
        t.forward(dash)
        t.penup()
        t.forward(gap)
        t.pendown()
    
    # Add label
    t.penup()
    t.goto(start_x, start_y - 20)
    t.pencolor("black")
    t.write(label, font=("Arial", 12, "bold"))
    
    # Add measurement
    t.goto(start_x + length/2, start_y - 40)
    t.write(f"Dash: {dash}px  |  Gap: {gap}px", align="center", font=("Arial", 10, "normal"))

# Draw dashed lines with different specifications
draw_dashed_line_with_label(-350, 200, 600, 40, 15, "red", "Wide Dashes")
draw_dashed_line_with_label(-350, 150, 600, 20, 20, "green", "Equal Pattern")
draw_dashed_line_with_label(-350, 100, 600, 10, 30, "blue", "Tiny Dashes")
draw_dashed_line_with_label(-350, 50, 600, 30, 10, "purple", "Short Gaps")
draw_dashed_line_with_label(-350, 0, 600, 15, 15, "orange", "Standard Dashed")
draw_dashed_line_with_label(-350, -50, 600, 5, 15, "brown", "Dotted Pattern")
draw_dashed_line_with_label(-350, -100, 600, 50, 20, "darkgreen", "Extra Long Dashes")

# Title
t.penup()
t.goto(0, 280)
t.pencolor("darkblue")
t.write("DASHED LINE PATTERNS", align="center", font=("Arial", 24, "bold"))

t.goto(0, 250)
t.write("Different Dash and Gap Combinations", align="center", font=("Arial", 14, "italic"))

t.hideturtle()
turtle.done()