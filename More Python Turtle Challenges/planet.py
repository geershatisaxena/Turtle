import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.title("Planet Orbit Animation")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Draw Sun
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.goto(0, -40)
sun.color("yellow")
sun.begin_fill()
sun.circle(40)
sun.end_fill()

# Planet class
class Planet:
    def __init__(self, color, orbit_radius, size, speed):
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.angle = 0

        self.planet = turtle.Turtle()
        self.planet.shape("circle")
        self.planet.color(color)
        self.planet.shapesize(size)
        self.planet.penup()

        # Draw orbit path
        orbit = turtle.Turtle()
        orbit.hideturtle()
        orbit.speed(0)
        orbit.color("gray")
        orbit.penup()
        orbit.goto(0, -orbit_radius)
        orbit.pendown()
        orbit.circle(orbit_radius)

    def move(self):
        x = self.orbit_radius * math.cos(math.radians(self.angle))
        y = self.orbit_radius * math.sin(math.radians(self.angle))
        self.planet.goto(x, y)
        self.angle += self.speed


# Create planets
planets = [
    Planet("orange", 80, 0.6, 4),      # Mercury
    Planet("cyan", 130, 0.8, 3),       # Venus
    Planet("blue", 180, 1.0, 2),       # Earth
    Planet("red", 240, 0.9, 1.5),      # Mars
    Planet("brown", 320, 1.8, 0.8),    # Jupiter
]

# Main animation loop
while True:
    for planet in planets:
        planet.move()

    screen.update()
    time.sleep(0.01)