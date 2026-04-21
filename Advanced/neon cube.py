import turtle
import colorsys
import math

# Setup
t = turtle.Turtle()
t.speed(0)
t.width(3)
turtle.bgcolor("black")
turtle.tracer(0, 0)
turtle.title("Neon 3D Cube")

# Cube vertices (3D coordinates projected to 2D)
# Format: (x, y) on screen
vertices = {
    'front_bottom_left': (-120, -100),
    'front_bottom_right': (120, -100),
    'front_top_right': (120, 100),
    'front_top_left': (-120, 100),
    'back_bottom_left': (-60, -60),
    'back_bottom_right': (60, -60),
    'back_top_right': (60, 60),
    'back_top_left': (-60, 60)
}

# Edges connecting vertices
edges = [
    ('front_bottom_left', 'front_bottom_right'),
    ('front_bottom_right', 'front_top_right'),
    ('front_top_right', 'front_top_left'),
    ('front_top_left', 'front_bottom_left'),
    ('back_bottom_left', 'back_bottom_right'),
    ('back_bottom_right', 'back_top_right'),
    ('back_top_right', 'back_top_left'),
    ('back_top_left', 'back_bottom_left'),
    ('front_bottom_left', 'back_bottom_left'),
    ('front_bottom_right', 'back_bottom_right'),
    ('front_top_right', 'back_top_right'),
    ('front_top_left', 'back_top_left')
]

def draw_edge(start, end, color_hue):
    """Draw a single edge with color"""
    t.penup()
    t.goto(vertices[start])
    t.pendown()
    rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
    t.pencolor(rgb)
    t.goto(vertices[end])

def draw_cube_rotation(angle):
    """Draw cube with rotation effect"""
    # Create rotation by shifting back face
    offset_x = math.sin(angle) * 25
    offset_y = math.cos(angle * 0.8) * 15
    
    # Update back face vertices with offset
    temp_vertices = vertices.copy()
    back_vertices = ['back_bottom_left', 'back_bottom_right', 'back_top_right', 'back_top_left']
    for v in back_vertices:
        x, y = vertices[v]
        temp_vertices[v] = (x + offset_x, y + offset_y)
    
    # Draw all edges
    for i, (start, end) in enumerate(edges):
        color_hue = (hue + i * 0.02) % 1.0
        t.penup()
        t.goto(temp_vertices[start])
        t.pendown()
        rgb = colorsys.hsv_to_rgb(color_hue, 1.0, 0.9)
        t.pencolor(rgb)
        t.goto(temp_vertices[end])

# Animation
hue = 0.0
rot_angle = 0

while True:
    t.clear()
    draw_cube_rotation(rot_angle)
    turtle.update()
    
    rot_angle += 0.04
    hue += 0.01
    
    if hue > 1.0:
        hue -= 1.0

turtle.done()