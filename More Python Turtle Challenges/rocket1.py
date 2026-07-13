import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Rocket Launch Animation")
screen.tracer(0)  # Turn off automatic updates for smooth animation

# Create the rocket
rocket = turtle.Turtle()
rocket.speed(0)
rocket.penup()

# Draw the rocket body
def draw_rocket():
    rocket.clear()
    rocket.penup()
    
    # Rocket body (white)
    rocket.goto(0, 0)
    rocket.pendown()
    rocket.color("white")
    rocket.begin_fill()
    rocket.goto(10, 0)
    rocket.goto(10, 40)
    rocket.goto(8, 45)
    rocket.goto(-8, 45)
    rocket.goto(-10, 40)
    rocket.goto(-10, 0)
    rocket.goto(0, 0)
    rocket.end_fill()
    
    # Nose cone (red)
    rocket.penup()
    rocket.goto(-8, 45)
    rocket.pendown()
    rocket.color("red")
    rocket.begin_fill()
    rocket.goto(0, 60)
    rocket.goto(8, 45)
    rocket.end_fill()
    
    # Windows (blue)
    rocket.penup()
    rocket.goto(0, 30)
    rocket.pendown()
    rocket.color("light blue")
    rocket.begin_fill()
    rocket.circle(3)
    rocket.end_fill()
    
    # Fins (red)
    rocket.penup()
    rocket.goto(-10, 5)
    rocket.pendown()
    rocket.color("red")
    rocket.begin_fill()
    rocket.goto(-20, -5)
    rocket.goto(-10, 0)
    rocket.end_fill()
    
    rocket.penup()
    rocket.goto(10, 5)
    rocket.pendown()
    rocket.begin_fill()
    rocket.goto(20, -5)
    rocket.goto(10, 0)
    rocket.end_fill()

draw_rocket()

# Smoke particles list
smoke_particles = []

# Create smoke turtle
smoke_turtle = turtle.Turtle()
smoke_turtle.speed(0)
smoke_turtle.penup()
smoke_turtle.hideturtle()

# Rocket position and velocity
rocket_x = 0
rocket_y = -250
rocket_vy = 0
launching = True
launch_complete = False

# Create star background
def create_stars():
    stars = turtle.Turtle()
    stars.speed(0)
    stars.penup()
    stars.hideturtle()
    stars.color("white")
    for _ in range(100):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        stars.goto(x, y)
        stars.dot(random.randint(1, 3))
create_stars()

# Function to create smoke puff
def create_smoke():
    smoke = turtle.Turtle()
    smoke.speed(0)
    smoke.penup()
    smoke.hideturtle()
    
    # Random position near rocket base
    x_offset = random.uniform(-15, 15)
    y_offset = random.uniform(-20, 0)
    smoke.goto(rocket_x + x_offset, rocket_y + y_offset - 10)
    
    # Random smoke properties
    size = random.uniform(5, 25)
    smoke.color("light gray")
    smoke.dot(size)
    smoke.color("gray")
    smoke.dot(size * 0.7)
    smoke.color("dark gray")
    smoke.dot(size * 0.4)
    
    # Store smoke data
    smoke_data = {
        "turtle": smoke,
        "x": rocket_x + x_offset,
        "y": rocket_y + y_offset - 10,
        "vx": random.uniform(-1, 1),
        "vy": random.uniform(0.5, 2),
        "size": size,
        "life": random.randint(30, 60),
        "max_life": 60
    }
    smoke_particles.append(smoke_data)

# Function to update smoke
def update_smoke():
    global smoke_particles
    for smoke in smoke_particles[:]:  # Iterate over a copy
        # Update position
        smoke["x"] += smoke["vx"] * 0.5
        smoke["y"] += smoke["vy"] * 0.5
        smoke["vy"] += 0.05  # Slight upward drift
        smoke["life"] -= 1
        
        # Update smoke turtle position and fade
        smoke["turtle"].goto(smoke["x"], smoke["y"])
        
        # Fade out and shrink
        life_ratio = smoke["life"] / smoke["max_life"]
        new_size = smoke["size"] * life_ratio
        
        # Change color based on life
        if life_ratio > 0.6:
            smoke["turtle"].color("light gray")
        elif life_ratio > 0.3:
            smoke["turtle"].color("gray")
        else:
            smoke["turtle"].color("dark gray")
        
        smoke["turtle"].dot(new_size)
        
        # Remove dead smoke
        if smoke["life"] <= 0:
            smoke["turtle"].clear()
            smoke["turtle"].hideturtle()
            smoke_particles.remove(smoke)

# Ground
ground = turtle.Turtle()
ground.speed(0)
ground.penup()
ground.goto(-400, -260)
ground.pendown()
ground.color("dark green")
ground.begin_fill()
ground.goto(400, -260)
ground.goto(400, -300)
ground.goto(-400, -300)
ground.goto(-400, -260)
ground.end_fill()
ground.hideturtle()

# Launch pad
pad = turtle.Turtle()
pad.speed(0)
pad.penup()
pad.goto(-20, -260)
pad.pendown()
pad.color("gray")
pad.begin_fill()
for _ in range(2):
    pad.forward(40)
    pad.left(90)
    pad.forward(10)
    pad.left(90)
pad.end_fill()
pad.hideturtle()

# Text display
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("white")
text_turtle.goto(0, 250)
text_turtle.write("🚀 Rocket Launch!", align="center", font=("Arial", 24, "bold"))

# Altitude display
alt_turtle = turtle.Turtle()
alt_turtle.hideturtle()
alt_turtle.penup()
alt_turtle.color("yellow")
alt_turtle.goto(-300, 250)

# Animation loop
frame_count = 0

def animate():
    global rocket_x, rocket_y, rocket_vy, launching, launch_complete, frame_count
    
    # Physics update
    if launching:
        # Rocket thrust acceleration
        thrust = 0.5
        gravity = -0.1
        
        rocket_vy += thrust + gravity
        rocket_y += rocket_vy
        
        # Create smoke during launch
        if frame_count % 2 == 0 and rocket_y < 200:
            for _ in range(random.randint(2, 4)):
                create_smoke()
        
        # Stop launching when rocket goes high enough
        if rocket_y > 300:
            launching = False
            launch_complete = True
            
    # Update rocket position
    rocket.goto(rocket_x, rocket_y)
    
    # Update smoke
    update_smoke()
    
    # Update altitude display
    altitude = int(rocket_y + 260)
    if altitude < 0:
        altitude = 0
    alt_turtle.clear()
    alt_turtle.write(f"Altitude: {altitude} m", align="center", font=("Arial", 14, "normal"))
    
    # Check if rocket is off screen
    if rocket_y > 400:
        text_turtle.clear()
        text_turtle.goto(0, 0)
        text_turtle.write("🎉 Liftoff Successful! 🎉", align="center", font=("Arial", 30, "bold"))
        text_turtle.goto(0, -40)
        text_turtle.write("Click to exit", align="center", font=("Arial", 16, "normal"))
        screen.onclick(lambda x, y: screen.bye())
        screen.update()
        return
    
    frame_count += 1
    screen.update()
    screen.ontimer(animate, 20)

# Click to exit
screen.onclick(lambda x, y: screen.bye())

# Start animation
animate()

# Keep window open
screen.mainloop()