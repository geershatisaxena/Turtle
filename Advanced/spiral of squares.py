import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral of Squares")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.pensize(2)

# Colors for the squares (cycling through a list)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]

# Spiral parameters
initial_size = 10      # Starting size of first square
size_increment = 5     # How much each square increases in size
angle = 90             # Turn angle for spiral (90° for squares)
number_of_squares = 50 # How many squares to draw

# Draw spiral of squares
for i in range(number_of_squares):
    # Set color (cycle through colors)
    t.color(colors[i % len(colors)])
    
    # Current square size
    size = initial_size + (i * size_increment)
    
    # Draw one square
    for _ in range(4):
        t.forward(size)
        t.left(angle)
    
 
    t.left(10)  # This creates the spiral rotation
    
    # Move forward a little to space out the squares
    t.forward(size_increment / 2)

# Hide turtle and finish
t.hideturtle()
screen.mainloop()