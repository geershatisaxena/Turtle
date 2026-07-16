import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("3D Ladder Illusion")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.hideturtle()

# Draw a 3D ladder rung
def draw_rung(x, y, width, depth):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Top face
    t.fillcolor("#FFD700")
    t.begin_fill()
    t.goto(x + width, y)
    t.goto(x + width + depth, y + depth)
    t.goto(x + depth, y + depth)
    t.goto(x, y)
    t.end_fill()

    # Side face
    t.fillcolor("#B8860B")
    t.begin_fill()
    t.goto(x + width, y)
    t.goto(x + width, y - 10)
    t.goto(x + width + depth, y - 10 + depth)
    t.goto(x + width + depth, y + depth)
    t.goto(x + width, y)
    t.end_fill()

# Draw ladder rails
left_x = -120
right_x = 40

t.color("#AAAAAA")

# Left rail
t.penup()
t.goto(left_x, -220)
t.pendown()
t.goto(left_x + 80, 220)

# Right rail
t.penup()
t.goto(right_x, -220)
t.pendown()
t.goto(right_x + 80, 220)

# Draw ladder rungs
for i in range(10):
    y = -180 + i * 40
    x = left_x + i * 8
    draw_rung(x, y, 160, 15)

# Glow effect
t.pencolor("cyan")
t.pensize(2)

for i in range(10):
    y = -180 + i * 40
    x = left_x + i * 8

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 160, y)
    t.goto(x + 175, y + 15)
    t.goto(x + 15, y + 15)
    t.goto(x, y)

screen.mainloop()