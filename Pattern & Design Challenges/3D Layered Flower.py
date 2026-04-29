import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Draw multiple layers of petals
layers = [
    {"petals": 8, "size": 100, "color": "darkred"},
    {"petals": 12, "size": 80, "color": "red"},
    {"petals": 16, "size": 60, "color": "crimson"},
    {"petals": 20, "size": 40, "color": "lightcoral"}
]

for layer in layers:
    for i in range(layer["petals"]):
        t.fillcolor(layer["color"])
        t.begin_fill()
        
        t.circle(layer["size"], 60)
        t.left(120)
        t.circle(layer["size"], 60)
        t.left(120)
        
        t.end_fill()
        t.left(360 / layer["petals"])
    
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Final center
t.fillcolor("gold")
t.begin_fill()
t.circle(25)
t.end_fill()

t.hideturtle()
turtle.done()