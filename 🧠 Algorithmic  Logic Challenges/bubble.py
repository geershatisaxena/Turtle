import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Bubble Sort Visualization")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
turtle.tracer(0)

# Generate random data
data = [random.randint(20, 250) for _ in range(20)]

# Draw bars
def draw_bars(data, highlight=None):
    pen.clear()

    start_x = -450
    bar_width = 40

    for i, value in enumerate(data):
        x = start_x + i * (bar_width + 5)

        pen.penup()
        pen.goto(x, -250)
        pen.pendown()

        if highlight and i in highlight:
            pen.color("red")
        else:
            pen.color("cyan")

        pen.begin_fill()

        for _ in range(2):
            pen.forward(bar_width)
            pen.left(90)
            pen.forward(value)
            pen.left(90)

        pen.end_fill()

    turtle.update()

# Bubble Sort Animation
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):

            draw_bars(arr, [j, j + 1])
            time.sleep(0.1)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                draw_bars(arr, [j, j + 1])
                time.sleep(0.1)

    draw_bars(arr)

# Initial draw
draw_bars(data)

# Start sorting
bubble_sort(data)

# Show completion message
msg = turtle.Turtle()
msg.hideturtle()
msg.color("lime")
msg.penup()
msg.goto(0, 260)
msg.write(
    "Bubble Sort Complete!",
    align="center",
    font=("Arial", 20, "bold")
)

screen.mainloop()