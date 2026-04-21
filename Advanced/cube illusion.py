import turtle
import colorsys

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("3D Cube Illusion")

# Cube corner coordinates (3D to 2D projection)
# Front face
front = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
# Back face (offset and scaled for perspective)
back = [(-60, -60), (60, -60), (60, 60), (-60, 60)]

def draw_face(points, color_hue):
    """Draw a single face of the cube"""
    t.penup()
    t.goto(points[0])
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.8)
    t.pencolor(rgb)
    
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])  # Close the face

def draw_cube():
    """Draw the complete 3D cube"""
    # Draw back face (darker)
    draw_face(back, 0.55)
    
    # Draw connecting lines from back to front
    for i in range(4):
        rgb = colorsys.hsv_to_rgb(0.6, 1.0, 0.6)
        t.pencolor(rgb)
        t.penup()
        t.goto(back[i])
        t.pendown()
        t.goto(front[i])
    
    # Draw front face (brighter)
    draw_face(front, 0.05)

# Animation - rotate colors and slight movement
hue = 0.0
angle = 0

while True:
    t.clear()
    
    # Create subtle rotation illusion by shifting back face
    import math
    offset_x = math.sin(angle) * 15
    offset_y = math.cos(angle * 0.7) * 10
    
    shifted_back = [(x + offset_x, y + offset_y) for (x, y) in back]
    
    # Draw back face with shifting color
    rgb_back = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 1.0, 0.5)
    t.pencolor(rgb_back)
    draw_face(shifted_back, (hue + 0.5) % 1.0)
    
    # Draw connecting lines
    for i in range(4):
        rgb_line = colorsys.hsv_to_rgb((hue + 0.3) % 1.0, 1.0, 0.7)
        t.pencolor(rgb_line)
        t.penup()
        t.goto(shifted_back[i])
        t.pendown()
        t.goto(front[i])
    
    # Draw front face
    rgb_front = colorsys.hsv_to_rgb(hue, 1.0, 0.9)
    t.pencolor(rgb_front)
    draw_face(front, hue)
    
    turtle.update()
    
    angle += 0.05
    hue += 0.008
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()