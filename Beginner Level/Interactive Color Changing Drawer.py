import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(5)
turtle.bgcolor("white")

# Color list
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown", "cyan"]
color_index = 0

# Function to change color
def change_color():
    global color_index
    color_index = (color_index + 1) % len(colors)
    t.pencolor(colors[color_index])
    print(f"Color changed to: {colors[color_index]}")

# Keyboard controls
turtle.listen()
turtle.onkeypress(change_color, "c")  # Press 'c' to change color
turtle.onkeypress(lambda: t.forward(20), "Up")  # Arrow up to move
turtle.onkeypress(lambda: t.backward(20), "Down")  # Arrow down to move
turtle.onkeypress(lambda: t.left(15), "Left")  # Arrow left to turn
turtle.onkeypress(lambda: t.right(15), "Right")  # Arrow right to turn
turtle.onkeypress(turtle.bye, "q")  # Press 'q' to quit

# Instructions
t.penup()
t.goto(-300, 250)
t.pendown()
t.write("Press 'c' to change color", font=("Arial", 14, "bold"))
t.penup()
t.goto(-300, 220)
t.write("Use Arrow Keys to Draw", font=("Arial", 14, "bold"))
t.goto(-300, 190)
t.write("Press 'q' to quit", font=("Arial", 14, "bold"))
t.penup()
t.goto(0, 0)

turtle.done()