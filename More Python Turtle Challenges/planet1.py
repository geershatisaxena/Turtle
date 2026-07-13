import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Animation")
screen.tracer(0)  # Turn off automatic updates for smooth animation

# Create the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2.5)  # Make sun larger
sun.penup()

# Create a list to hold planet data
planets = []

# Planet colors
colors = ["light blue", "orange", "red", "green", "cyan", "magenta", "white", "gold"]

# Create planets with different orbits, sizes, speeds, and colors
for i in range(8):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(colors[i % len(colors)])
    
    # Randomize planet properties
    orbit_radius = 80 + i * 40  # Distance from sun
    size = 0.5 + (i * 0.2)       # Planet size
    speed = 0.5 + (8 - i) * 0.3  # Speed (inner planets move faster)
    angle = random.uniform(0, 360)  # Random starting position
    
    planet.shapesize(size)
    planet.penup()
    
    # Store planet data in a dictionary
    planet_data = {
        "turtle": planet,
        "radius": orbit_radius,
        "speed": speed,
        "angle": angle,
        "color": colors[i % len(colors)]
    }
    planets.append(planet_data)

# Draw orbit paths (optional - comment out to hide orbits)
orbit_turtles = []
for i, planet_data in enumerate(planets):
    orbit = turtle.Turtle()
    orbit.speed(0)
    orbit.color("gray")
    orbit.penup()
    orbit.goto(0, -planet_data["radius"])
    orbit.pendown()
    orbit.circle(planet_data["radius"])
    orbit.penup()
    orbit.hideturtle()
    orbit_turtles.append(orbit)

# Function to update planet positions
def update_planets():
    for planet_data in planets:
        # Update angle based on speed
        planet_data["angle"] += planet_data["speed"] * 0.02
        
        # Calculate new position using trigonometry
        x = planet_data["radius"] * math.cos(math.radians(planet_data["angle"]))
        y = planet_data["radius"] * math.sin(math.radians(planet_data["angle"]))
        
        # Move planet to new position
        planet_data["turtle"].goto(x, y)

# Animation loop
def animate():
    update_planets()
    screen.update()  # Update screen after all movements
    screen.ontimer(animate, 20)  # Schedule next frame (50 FPS)

# Add some text labels
turtle_text = turtle.Turtle()
turtle_text.hideturtle()
turtle_text.penup()
turtle_text.color("white")
turtle_text.goto(0, 250)
turtle_text.write("Solar System Animation", align="center", font=("Arial", 20, "bold"))

# Click to exit
screen.onclick(lambda x, y: screen.bye())

# Start animation
animate()

# Keep window open
screen.mainloop()