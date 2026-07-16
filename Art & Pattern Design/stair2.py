import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Infinite 3D Staircase Illusion")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)

# Draw a single 3D block
def draw_block(x, y, size, h, color):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Top face
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + size, y)
    t.goto(x + size + h, y + h)
    t.goto(x + h, y + h)
    t.goto(x, y)
    t.end_fill()

    # Side face
    t.fillcolor("gray20")
    t.begin_fill()
    t.goto(x + size, y)
    t.goto(x + size, y - size)
    t.goto(x + size + h, y - size + h)
    t.goto(x + size + h, y + h)
    t.end_fill()

    # Front face
    t.fillcolor("gray40")
    t.begin_fill()
    t.goto(x, y)
    t.goto(x, y - size)
    t.goto(x + size, y - size)
    t.goto(x + size, y)
    t.end_fill()

# Draw Penrose-style staircase
size = 50
depth = 20
steps = 20

for i in range(steps):
    hue = i / steps
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    rgb = tuple(int(c * 255) for c in color)
    hex_color = "#%02x%02x%02x" % rgb

    x = -220 + i * 18
    y = -180 + i * 12

    draw_block(x, y, size, depth, hex_color)

# Connect the end back to the start
t.pensize(5)
t.pencolor("cyan")
t.penup()
t.goto(-220 + (steps - 1) * 18 + size, -180 + (steps - 1) * 12)
t.pendown()
t.goto(-220, -180)

screen.update()
screen.mainloop()