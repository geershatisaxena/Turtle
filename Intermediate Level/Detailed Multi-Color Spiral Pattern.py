import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(4)

# Color palette
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw detailed spiral
for i in range(300):
    # Change color based on position
    t.pencolor(colors[i % len(colors)])
    
    # Vary pen size for effect
    t.pensize((i % 5) + 1)
    
    # Draw spiral
    t.forward(i * 0.8)
    t.left(45)  # 45-degree angle
    
    # Add dots at intervals
    if i % 30 == 0:
        t.dot(15, "white")

t.hideturtle()
turtle.done()