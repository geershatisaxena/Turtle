import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Bubble Sort Visualizer")
screen.bgcolor("black")
screen.setup(1200, 700)

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

turtle.tracer(0)

# Random data
data = [random.randint(30, 400) for _ in range(18)]

def draw_array(arr, active=None, sorted_part=0):
    drawer.clear()

    start_y = 280

    for i, value in enumerate(arr):

        y = start_y - i * 35

        drawer.penup()
        drawer.goto(-500, y)
        drawer.pendown()

        # Color selection
        if i >= len(arr) - sorted_part:
            drawer.color("lime")
        elif active and i in active:
            drawer.color("red")
        else:
            drawer.color("cyan")

        drawer.pensize(18)
        drawer.forward(value)

        # Value label
        drawer.penup()
        drawer.goto(-520, y - 8)
        drawer.color("white")
        drawer.write(
            str(arr[i]),
            font=("Arial", 10, "bold")
        )

    turtle.update()


def bubble_sort_visual(arr):
    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(n - i - 1):

            draw_array(arr, [j, j + 1], i)
            time.sleep(0.12)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                draw_array(arr, [j, j + 1], i)
                time.sleep(0.12)

        if not swapped:
            break

    draw_array(arr, sorted_part=n)


# Start animation
bubble_sort_visual(data)

# Completion text
writer = turtle.Turtle()
writer.hideturtle()
writer.color("gold")
writer.penup()
writer.goto(0, 320)
writer.write(
    "Bubble Sort Finished ✓",
    align="center",
    font=("Arial", 24, "bold")
)

screen.mainloop()