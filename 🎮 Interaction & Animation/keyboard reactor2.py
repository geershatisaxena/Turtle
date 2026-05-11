import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Arrow Key Drawing")
screen.setup(width=800, height=600)

# Create turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("cyan")
pen.pensize(3)
pen.speed(0)

# Movement functions
def move_up():
    pen.setheading(90)
    pen.forward(20)

def move_down():
    pen.setheading(270)
    pen.forward(20)

def move_left():
    pen.setheading(180)
    pen.forward(20)

def move_right():
    pen.setheading(0)
    pen.forward(20)

# Optional controls
def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

def change_color():
    colors = ["cyan", "yellow", "red", "green", "white", "orange"]
    current = pen.pencolor()
    
    next_index = (colors.index(current) + 1) % len(colors)
    pen.color(colors[next_index])

# Keyboard bindings
screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.onkey(clear_screen, "c")
screen.onkey(change_color, "space")

# Instructions
print("Use Arrow Keys to Draw")
print("Press SPACE to change color")
print("Press C to clear screen")

# Keep window open
turtle.done()