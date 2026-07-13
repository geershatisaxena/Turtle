import turtle
import time

# Screen Setup
screen = turtle.Screen()
screen.title("Traffic Light Simulation")
screen.bgcolor("skyblue")
screen.setup(width=600, height=800)

# Traffic Light Body
body = turtle.Turtle()
body.hideturtle()
body.speed(0)
body.penup()
body.goto(-80, 200)
body.pendown()
body.color("black", "gray20")
body.begin_fill()

for _ in range(2):
    body.forward(160)
    body.right(90)
    body.forward(400)
    body.right(90)

body.end_fill()

# Pole
body.penup()
body.goto(-20, -200)
body.pendown()
body.color("gray30")
body.begin_fill()

for _ in range(2):
    body.forward(40)
    body.right(90)
    body.forward(250)
    body.right(90)

body.end_fill()

# Light Positions
positions = [
    (0, 120),   # Red
    (0, 0),     # Yellow
    (0, -120)   # Green
]

# Create Lights
lights = []

for pos in positions:
    light = turtle.Turtle()
    light.shape("circle")
    light.shapesize(4)
    light.penup()
    light.goto(pos)
    light.color("dim gray")
    lights.append(light)

# Status Text
status = turtle.Turtle()
status.hideturtle()
status.color("white")
status.penup()
status.goto(0, 250)

def update_lights(red=False, yellow=False, green=False, message=""):
    lights[0].color("red" if red else "dim gray")
    lights[1].color("yellow" if yellow else "dim gray")
    lights[2].color("lime" if green else "dim gray")

    status.clear()
    status.write(
        message,
        align="center",
        font=("Arial", 22, "bold")
    )

# Infinite Simulation
while True:

    # RED
    update_lights(red=True, message="STOP")
    time.sleep(4)

    # RED + YELLOW
    update_lights(red=True, yellow=True, message="READY")
    time.sleep(2)

    # GREEN
    update_lights(green=True, message="GO")
    time.sleep(4)

    # YELLOW
    update_lights(yellow=True, message="SLOW DOWN")
    time.sleep(2)