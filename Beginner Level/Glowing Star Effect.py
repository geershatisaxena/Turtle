import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Function to draw star at different sizes
def draw_star(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Draw multiple stars for glowing effect
sizes = [250, 230, 210, 190, 170]
colors = ["darkorange", "orange", "gold", "yellow", "lightyellow"]

for size, color in zip(sizes, colors):
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    t.pencolor(color)
    draw_star(size, color)

# Add sparkles
t.penup()
t.pencolor("white")
sparkle_positions = [(100, 150), (-120, 130), (80, -140), (-90, -120), (150, -50)]
for pos in sparkle_positions:
    t.goto(pos)
    t.dot(8, "white")

t.hideturtle()
turtle.done()