import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(3)
turtle.bgcolor("black")
turtle.tracer(0, 0)  # Turn off automatic updates for smooth animation

# Polygon settings
sides = 6          # Change this for different polygon shapes (e.g., 5 = pentagon, 8 = octagon)
angle = 360 / sides
radius = 150

hue = 0.0          # Initial hue value

def draw_polygon(rotation):
    t.clear()
    t.penup()
    # Position turtle for first vertex of rotated polygon
    t.goto(radius, 0)
    t.setheading(rotation)
    t.pendown()

    for _ in range(sides):
        t.forward(radius * 2)   # Edge length
        t.left(angle)

# Animation loop
rotation_angle = 0
while True:
    # Change color using HSV (hue varies)
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(rgb)

    draw_polygon(rotation_angle)

    turtle.update()   # Refresh screen
    rotation_angle += 2  # Spin speed
    hue += 0.01          # Color change speed

    if hue > 1.0:
        hue -= 1.0

# Keep window open (though loop runs forever; use Ctrl+C to stop)
turtle.done()