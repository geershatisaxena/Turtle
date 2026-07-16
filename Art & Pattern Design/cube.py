import turtle

# ==========================
# Cube Grid Illusion
# ==========================

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cube Grid Illusion")
screen.setup(1000, 800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)

SIZE = 40

# Draw an isometric cube
def draw_cube(x, y, s):

    # Top face
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("#EEEEEE")
    t.begin_fill()

    t.goto(x + s, y + s/2)
    t.goto(x, y + s)
    t.goto(x - s, y + s/2)
    t.goto(x, y)

    t.end_fill()

    # Left face
    t.fillcolor("#BBBBBB")
    t.begin_fill()

    t.goto(x - s, y + s/2)
    t.goto(x - s, y - s/2)
    t.goto(x, y - s)
    t.goto(x, y)

    t.end_fill()

    # Right face
    t.fillcolor("#777777")
    t.begin_fill()

    t.goto(x + s, y + s/2)
    t.goto(x + s, y - s/2)
    t.goto(x, y - s)
    t.goto(x, y)

    t.end_fill()

# Draw cube grid
rows = 8
cols = 8

for row in range(rows):
    for col in range(cols):

        x = (col - row) * SIZE
        y = (col + row) * SIZE/2 - 180

        draw_cube(x, y, SIZE)

screen.update()
screen.mainloop()