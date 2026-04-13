import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw an equilateral triangle
for _ in range(3):
    t.forward(150)  # Side length
    t.left(120)     # Turn left by 120 degrees (360/3 = 120)

# Keep the window open until clicked
turtle.done()