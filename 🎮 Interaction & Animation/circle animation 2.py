import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.setup(400, 400)
screen.title("Spinning Loading Circle Animation")
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic updates for smooth animation

# Create the spinner
spinner = turtle.Turtle()
spinner.speed(0)
spinner.penup()
spinner.hideturtle()

# Create text turtle for percentage
text_turtle = turtle.Turtle()
text_turtle.speed(0)
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.color("white")

# Animation variables
angle = 0
radius = 80
num_dots = 12
dots = []  # Store dot turtles
dot_colors = ["red", "orange", "yellow", "green", "cyan", "blue", 
              "purple", "magenta", "pink", "white", "lime", "gold"]

def create_dots():
    """Create the loading dots arranged in a circle."""
    for i in range(num_dots):
        dot = turtle.Turtle()
        dot.speed(0)
        dot.shape("circle")
        dot.shapesize(0.8)
        dot.penup()
        
        # Calculate position
        rad_angle = (2 * math.pi / num_dots) * i
        x = math.cos(rad_angle) * radius
        y = math.sin(rad_angle) * radius
        dot.goto(x, y)
        
        # Set color based on position
        dot.color(dot_colors[i % len(dot_colors)])
        
        dots.append(dot)

def update_spinner():
    """Update the spinner animation."""
    global angle
    
    # Clear previous spinner indicators
    for dot in dots:
        dot.clear()
    
    # Rotate all dots
    for i, dot in enumerate(dots):
        # Calculate new position with rotation
        rad_angle = (2 * math.pi / num_dots) * i + math.radians(angle)
        x = math.cos(rad_angle) * radius
        y = math.sin(rad_angle) * radius
        dot.goto(x, y)
        
        # Vary size based on angle for 3D effect
        size_factor = 0.5 + 0.5 * math.sin(rad_angle * 2)
        dot.shapesize(0.6 + size_factor * 0.4)
        
        # Vary opacity effect by color brightness
        if size_factor > 0.7:
            dot.color("white")
        else:
            dot.color(dot_colors[i % len(dot_colors)])
    
    # Update angle for next frame
    angle = (angle + 8) % 360
    
    # Update loading text with simple animation
    text_turtle.clear()
    text_turtle.goto(0, -120)
    
    # Animated dots for text
    frame = int(angle / 10) % 4
    dots_text = "." * (frame + 1)
    text_turtle.write(f"LOADING{dots_text}", align="center", 
                      font=("Arial", 20, "bold"))

def create_arc_spinner():
    """Alternative: Create an arc-based spinner (like a pie chart)."""
    arc = turtle.Turtle()
    arc.speed(0)
    arc.penup()
    arc.hideturtle()
    arc.pensize(8)
    
    return arc

def animate_arc_spinner():
    """Animate an arc-style spinner (optional)."""
    arc = create_arc_spinner()
    angle_arc = 0
    
    def update_arc():
        nonlocal angle_arc
        arc.clear()
        arc.penup()
        arc.goto(0, 0)
        arc.setheading(90)
        arc.pendown()
        arc.color("cyan")
        arc.circle(radius, angle_arc % 360)
        angle_arc = (angle_arc + 10) % 360
        screen.update()
        screen.ontimer(update_arc, 30)
    
    return update_arc

def style_1():
    """Style 1: Spinning colored dots (default)."""
    create_dots()
    
    def animate():
        update_spinner()
        screen.update()
        screen.ontimer(animate, 30)
    
    return animate

def style_2():
    """Style 2: Simple rotating line spinner."""
    line = turtle.Turtle()
    line.speed(0)
    line.hideturtle()
    line.pensize(5)
    angle_line = 0
    
    def animate():
        nonlocal angle_line
        line.clear()
        line.penup()
        line.goto(0, 0)
        line.setheading(angle_line)
        line.pendown()
        line.color("cyan")
        line.forward(radius)
        line.penup()
        line.goto(0, 0)
        line.setheading(angle_line + 180)
        line.pendown()
        line.color("blue")
        line.forward(radius - 20)
        
        angle_line = (angle_line + 15) % 360
        
        # Update text
        text_turtle.clear()
        text_turtle.goto(0, -120)
        frame = int(angle_line / 15) % 4
        dots_text = "." * (frame + 1)
        text_turtle.write(f"PROCESSING{dots_text}", align="center", 
                          font=("Arial", 20, "bold"))
        
        screen.update()
        screen.ontimer(animate, 25)
    
    return animate

def style_3():
    """Style 3: Expanding and contracting circle."""
    pulse = turtle.Turtle()
    pulse.speed(0)
    pulse.hideturtle()
    pulse.pensize(3)
    pulse.color("lime")
    size = 10
    growing = True
    
    def animate():
        nonlocal size, growing
        pulse.clear()
        pulse.penup()
        pulse.goto(0, 0)
        pulse.pendown()
        
        if growing:
            size += 3
            if size >= radius:
                growing = False
        else:
            size -= 3
            if size <= 10:
                growing = True
        
        pulse.circle(size)
        
        # Update text
        text_turtle.clear()
        text_turtle.goto(0, -120)
        percentage = int((size / radius) * 100)
        text_turtle.write(f"LOADING... {percentage}%", align="center", 
                          font=("Arial", 18, "bold"))
        
        screen.update()
        screen.ontimer(animate, 30)
    
    return animate

# Choose animation style (1, 2, or 3)
print("Loading Circle Animation")
print("=======================")
print("Choose a style:")
print("1 - Spinning colored dots (default)")
print("2 - Rotating line spinner")
print("3 - Pulsing circle")

# Default to style 1
style = 1

try:
    choice = input("Enter style (1-3) or press Enter for default: ").strip()
    if choice:
        style = int(choice)
except:
    style = 1

# Start the selected animation
if style == 1:
    animate_func = style_1()
elif style == 2:
    animate_func = style_2()
else:
    animate_func = style_3()

# Start animation
animate_func()

# Keep window open
screen.mainloop()