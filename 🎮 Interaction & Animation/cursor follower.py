import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mouse Following Turtle")

# Create turtle
follower = turtle.Turtle()
follower.shape("turtle")
follower.color("cyan")
follower.shapesize(2)
follower.speed(1)

# Function to move turtle towards mouse click
def follow_mouse(x, y):
    follower.setheading(follower.towards(x, y))
    follower.goto(x, y)

# Track mouse movement
screen.onscreenclick(follow_mouse)

# Keep window open
screen.mainloop()