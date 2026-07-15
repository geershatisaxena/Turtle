import turtle

# Create turtle
t = turtle.Turtle()
t.speed(5)

# Draw a simple flower
for i in range(8):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 45)
    t.forward(30)
    t.pendown()
    
    # Draw petal
    t.color('#FF69B4')
    t.begin_fill()
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.end_fill()

# Draw center
t.penup()
t.goto(0, 0)
t.pendown()
t.color('#FFD700')
t.begin_fill()
t.circle(20)
t.end_fill()

# Keep window open
turtle.done()