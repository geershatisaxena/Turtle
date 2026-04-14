import turtle

t = turtle.Turtle()
t.pensize(4)
t.speed(6)

# Big dimensions
base = 350
height = 250

# Position to center on screen
t.penup()
t.goto(-175, -125)
t.pendown()

# Draw the right-angle triangle
t.fillcolor("lightblue")
t.begin_fill()

t.forward(base)   # Draw base (right)
t.left(90)        # Turn upward
t.forward(height) # Draw height (up)
t.goto(-175, -125) # Draw hypotenuse (diagonal back to start)

t.end_fill()
t.hideturtle()

# Add labels (optional)
t.penup()
t.goto(-100, -140)
t.write("Base: 350px", font=("Arial", 12, "normal"))
t.goto(-190, 0)
t.write("Height: 250px", font=("Arial", 12, "normal"))

turtle.done()