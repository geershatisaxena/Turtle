import turtle
import math
import time

# Screen Setup
screen = turtle.Screen()
screen.title("Pendulum Swing Simulation")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Pendulum Parameters
length = 200          # Length of pendulum
angle = 45            # Initial angle (degrees)
angular_velocity = 0
gravity = 0.4         # Gravity strength
damping = 0.995       # Energy loss

# Pivot Point
pivot_x = 0
pivot_y = 200

# Pendulum Rod
rod = turtle.Turtle()
rod.hideturtle()
rod.pensize(3)
rod.color("white")

# Pendulum Bob
bob = turtle.Turtle()
bob.shape("circle")
bob.color("cyan")
bob.shapesize(1.5)
bob.penup()

# Pivot Marker
pivot = turtle.Turtle()
pivot.hideturtle()
pivot.penup()
pivot.goto(pivot_x, pivot_y)
pivot.dot(12, "red")

# Animation Loop
while True:

    # Pendulum Physics
    angular_acceleration = -(gravity / length) * math.sin(math.radians(angle))
    angular_velocity += angular_acceleration
    angular_velocity *= damping
    angle += angular_velocity

    # Calculate Bob Position
    x = pivot_x + length * math.sin(math.radians(angle))
    y = pivot_y - length * math.cos(math.radians(angle))

    # Draw Rod
    rod.clear()
    rod.penup()
    rod.goto(pivot_x, pivot_y)
    rod.pendown()
    rod.goto(x, y)

    # Move Bob
    bob.goto(x, y)

    screen.update()
    time.sleep(0.01)