import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Concentric Rotating Stars")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Color settings
turtle.colormode(255)

def draw_star(size, points, offset=0):
    """Draw a star with given size and number of points"""
    angle = 180 - (180 / points)
    
    for _ in range(points):
        t.forward(size)
        t.right(angle + offset)
        t.forward(size)
        t.left(180 - (360 / points))

# Parameters
num_stars = 12           # Number of concentric stars
initial_size = 20        # Starting star size
size_increment = 15      # Size increase between stars
rotation_step = 5        # Rotation between layers

# Draw concentric rotating stars
for i in range(num_stars):
    # Dynamic color (rainbow effect)
    r = (i * 20) % 256
    g = (i * 30) % 256
    b = (i * 40) % 256
    t.pencolor(r, g, b)
    
    # Calculate size for this star
    current_size = initial_size + (i * size_increment)
    
    # Draw star with rotation
    draw_star(current_size, 5, i * rotation_step)
    
    # Lift pen to move to center for next star
    t.penup()
    t.home()
    t.pendown()

t.hideturtle()
screen.update()
screen.mainloop()