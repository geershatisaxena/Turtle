import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw multiple layers of kaleidoscope
layers = [60, 100, 140, 180]

for layer_size in layers:
    for i in range(36):
        t.pencolor(colors[i % len(colors)])
        t.fillcolor(colors[(i + layer_size // 20) % len(colors)])
        t.begin_fill()
        
        # Draw star shape
        for _ in range(5):
            t.forward(layer_size)
            t.left(144)
        
        t.end_fill()
        t.left(10)

t.hideturtle()
turtle.done()