import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Changing Smiley Face")

# Turtle setup
face = turtle.Turtle()
face.hideturtle()
face.speed(0)
face.pensize(3)

# Function to draw eyes
def draw_eyes():
    for x in (-40, 40):
        face.penup()
        face.goto(x, 50)
        face.pendown()
        face.begin_fill()
        face.circle(10)
        face.end_fill()

# Function to draw face
def draw_base():
    face.penup()
    face.goto(0, -150)
    face.setheading(0)
    face.color("black", "yellow")
    face.pendown()

    face.begin_fill()
    face.circle(150)
    face.end_fill()

# Happy mouth
def happy():
    face.penup()
    face.goto(-60, -20)
    face.setheading(-60)
    face.pendown()
    face.circle(70, 120)

# Sad mouth
def sad():
    face.penup()
    face.goto(-60, -90)
    face.setheading(60)
    face.pendown()
    face.circle(-70, 120)

# Surprised mouth
def surprised():
    face.penup()
    face.goto(0, -70)
    face.pendown()
    face.circle(30)

# Angry mouth + eyebrows
def angry():
    # Eyebrows
    face.penup()
    face.goto(-70, 90)
    face.pendown()
    face.goto(-20, 60)

    face.penup()
    face.goto(70, 90)
    face.pendown()
    face.goto(20, 60)

    # Mouth
    face.penup()
    face.goto(-60, -80)
    face.setheading(60)
    face.pendown()
    face.circle(-70, 120)

# Main animation loop
expressions = [happy, sad, surprised, angry]

while True:
    for expression in expressions:
        face.clear()

        draw_base()
        draw_eyes()

        face.color("black")
        expression()

        screen.update()
        turtle.time.sleep(1.5)

turtle.done()