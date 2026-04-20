import turtle
import colorsys

# Setup
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Spinning Color Polygons")

# Create multiple turtles
polygons = []
colors = []
sides_list = [3, 4, 5, 6, 7, 8]
radius_step = 30
start_radius = 50

for i, sides in enumerate(sides_list):
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.penup()
    polygons.append(t)
    colors.append(0.0)  # starting hue for each

rotation_angles = [0] * len(sides_list)

def draw_polygon(turtle_obj, sides, radius, rotation):
    turtle_obj.clear()
    turtle_obj.penup()
    turtle_obj.goto(radius, 0)
    turtle_obj.setheading(rotation)
    turtle_obj.pendown()
    
    angle = 360 / sides
    for _ in range(sides):
        turtle_obj.forward(radius * 2 * math.sin(math.pi / sides))  # proper edge length
        turtle_obj.left(angle)

import math

# Animation
while True:
    for i, t_obj in enumerate(polygons):
        sides = sides_list[i]
        radius = start_radius + i * radius_step
        
        # Change color for each polygon
        rgb = colorsys.hsv_to_rgb(colors[i], 1.0, 1.0)
        t_obj.pencolor(rgb)
        
        draw_polygon(t_obj, sides, radius, rotation_angles[i])
        
        # Spin at different speeds
        rotation_angles[i] += (i + 1) * 1.2
        colors[i] += 0.005 * (i + 1)
        
        if colors[i] > 1.0:
            colors[i] -= 1.0
    
    turtle.update()