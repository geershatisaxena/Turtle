import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 pixels
    t.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
turtle.done()