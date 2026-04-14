import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(4)

# Get user input (or modify these values directly)
dash_length = 30    # Change this value
gap_length = 15     # Change this value
total_length = 400
line_color = "blue"

# Draw the dashed line
t.pencolor(line_color)

segments = total_length // (dash_length + gap_length)

for _ in range(segments):
    t.forward(dash_length)
    t.penup()
    t.forward(gap_length)
    t.pendown()

# Display information
t.penup()
t.goto(-200, -50)
t.pencolor("black")
t.write(f"Dash: {dash_length}px | Gap: {gap_length}px | Total: {total_length}px", 
         align="center", font=("Arial", 14, "bold"))

t.hideturtle()
turtle.done()