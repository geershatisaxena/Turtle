import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rotating Star Pattern")
screen.tracer(0)  # Turn off animation for faster drawing

# Create turtle
t = turtle.Turtle()
t.speed(12)
t.pensize(2)

# Colors for stars
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta", "pink", "gold"]

# Star parameters
star_points = 5      # Number of points on each star
star_size = 100      # Size of the star
rotation_angle = 5   # How much to rotate each star
number_of_stars = 72 # Total stars (360° / rotation_angle)

# Function to draw a star
def draw_star(size, points):
    angle = 180 - (180 / points)  # Interior angle for star points
    
    for _ in range(points):
        t.forward(size)
        t.right(angle)
        t.forward(size)
        t.left(180 - (360 / points))

# Draw rotating stars
for i in range(number_of_stars):
    # Set color
    t.color(colors[i % len(colors)])
    
    # Draw star
    draw_star(star_size, star_points)
    
    # Rotate for next star
    t.right(rotation_angle)

t.hideturtle()
screen.update()  # Update the screen once
screen.mainloop()