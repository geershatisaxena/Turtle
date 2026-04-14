import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(4)

# Function to draw arrowhead
def draw_arrowhead():
    t.left(45)
    t.forward(15)
    t.backward(15)
    t.right(90)
    t.forward(15)
    t.backward(15)
    t.left(45)

# Draw dashed line with arrow at the end
for _ in range(12):
    t.forward(25)
    t.penup()
    t.forward(15)
    t.pendown()

# Add arrowhead at the end
draw_arrowhead()

t.hideturtle()
turtle.done()