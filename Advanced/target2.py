import turtle

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("white")
turtle.tracer(0, 0)
turtle.title("Archery Target Board")

# Target colors (from outer to inner)
colors = ["black", "blue", "red", "yellow", "white"]
ring_width = 40
center_radius = 20

def draw_ring(radius, color):
    """Draw a single colored ring"""
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw from largest to smallest
for i in range(len(colors)):
    radius = (len(colors) - i) * ring_width
    draw_ring(radius, colors[i])

# Draw center dot
t.penup()
t.goto(0, -center_radius)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(center_radius)
t.end_fill()

# Draw crosshairs
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(200, 0)

turtle.done()