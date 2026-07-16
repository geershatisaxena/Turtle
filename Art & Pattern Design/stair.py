import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("3D Staircase Illusion")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Colors for 3D effect
top_color = "#DDEEFF"
side_color = "#88AADD"
front_color = "#4466AA"

# Draw one 3D step
def draw_step(x, y, w, h, depth):
    # Top face
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(top_color)
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w + depth, y + depth)
    t.goto(x + depth, y + depth)
    t.goto(x, y)
    t.end_fill()

    # Front face
    t.fillcolor(front_color)
    t.begin_fill()
    t.goto(x, y - h)
    t.goto(x + w, y - h)
    t.goto(x + w, y)
    t.goto(x, y)
    t.end_fill()

    # Side face
    t.fillcolor(side_color)
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y - h)
    t.goto(x + w + depth, y - h + depth)
    t.goto(x + w + depth, y + depth)
    t.goto(x + w, y)
    t.end_fill()

# Draw staircase
x, y = -250, -150
step_width = 80
step_height = 25
depth = 20

for i in range(8):
    draw_step(
        x + i * 30,
        y + i * step_height,
        step_width,
        step_height,
        depth
    )

# Add glowing outline effect
t.color("cyan")
t.pensize(3)
for i in range(8):
    px = x + i * 30
    py = y + i * step_height

    t.penup()
    t.goto(px, py)
    t.pendown()

    t.goto(px + step_width, py)
    t.goto(px + step_width + depth, py + depth)
    t.goto(px + depth, py + depth)
    t.goto(px, py)

t.hideturtle()
screen.mainloop()