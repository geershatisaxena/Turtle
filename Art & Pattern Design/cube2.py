import turtle
import math

# =====================================
# Floating Cube Wave Illusion
# =====================================

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Floating Cube Wave Illusion")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)

SIZE = 25

# Draw an isometric cube
def cube(x, y, s, level):

    # Brightness based on height
    shade = max(40, min(255, int(120 + level * 8)))

    top = (shade, shade, shade)
    left = (shade - 40, shade - 40, shade - 40)
    right = (shade - 80, shade - 80, shade - 80)

    # Top face
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor(top)
    t.begin_fill()
    t.goto(x + s, y + s/2)
    t.goto(x, y + s)
    t.goto(x - s, y + s/2)
    t.goto(x, y)
    t.end_fill()

    # Left face
    t.fillcolor(left)
    t.begin_fill()
    t.goto(x - s, y + s/2)
    t.goto(x - s, y - s/2 - level)
    t.goto(x, y - s - level)
    t.goto(x, y)
    t.end_fill()

    # Right face
    t.fillcolor(right)
    t.begin_fill()
    t.goto(x + s, y + s/2)
    t.goto(x + s, y - s/2 - level)
    t.goto(x, y - s - level)
    t.goto(x, y)
    t.end_fill()

# Enable RGB colors
screen.colormode(255)

# Cube terrain
for row in range(-10, 11):
    for col in range(-10, 11):

        # Wave height
        height = (
            math.sin(row * 0.5)
            + math.cos(col * 0.5)
        ) * 15 + 25

        iso_x = (col - row) * SIZE
        iso_y = (col + row) * SIZE/2 - 150

        cube(iso_x, iso_y, SIZE, height)

# Glow border
t.pensize(3)
t.pencolor("cyan")

for r in range(260, 320, 15):
    t.penup()
    t.goto(0, -r)
    t.pendown()
    t.circle(r)

screen.update()
screen.mainloop()