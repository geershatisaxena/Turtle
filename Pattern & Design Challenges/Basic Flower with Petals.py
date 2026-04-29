import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
t.pensize(2)

# Draw flower petals using loop
num_petals = 12
for _ in range(num_petals):
    t.circle(50, 60)  # Draw arc for petal
    t.left(120)       # Turn to create petal shape
    t.circle(50, 60)
    t.left(120)
    t.left(360 / num_petals)  # Rotate for next petal

t.hideturtle()
turtle.done()




