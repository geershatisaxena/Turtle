import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

square_size = 50

for row in range(8):
    for col in range(8):
        t.penup()
        t.goto(col * square_size - 200, 200 - row * square_size)
        t.pendown()

        if (row + col) % 2 == 0:
            t.fillcolor("white")
        else:
            t.fillcolor("black")

        t.begin_fill()
        for _ in range(4):
            t.forward(square_size)
            t.right(90)
        t.end_fill()

t.hideturtle()
turtle.done()