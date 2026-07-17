import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(2)

colors = ["red", "yellow", "blue", "green", "orange"]

for i in range(50):
    t.color(colors[i % 5])
    t.forward(i * 2)
    t.left(145)

turtle.done()