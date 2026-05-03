import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Collision Detection Demo")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)

# Create two moving objects
object1 = turtle.Turtle()
object1.shape("circle")
object1.color("red")
object1.shapesize(2, 2)
object1.penup()

object2 = turtle.Turtle()
object2.shape("square")
object2.color("blue")
object2.shapesize(2, 2)
object2.penup()

# UI elements
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("white")
info_display.penup()
info_display.hideturtle()

collision_counter = turtle.Turtle()
collision_counter.speed(0)
collision_counter.color("yellow")
collision_counter.penup()
collision_counter.hideturtle()

# Object properties using lists to avoid global variable issues
obj1 = {
    'x': -200,
    'y': 0,
    'dx': 3,
    'dy': 4,
    'radius': 20
}

obj2 = {
    'x': 200,
    'y': 0,
    'dx': -4,
    'dy': -3,
    'radius': 20
}

# Boundaries
boundary_left = -420
boundary_right = 420
boundary_top = 320
boundary_bottom = -320

# Collision tracking
collision_count = 0
running = True

def check_wall_collision(obj):
    """Check and handle wall collisions for an object"""
    x = obj['x'] + obj['dx']
    y = obj['y'] + obj['dy']
    dx = obj['dx']
    dy = obj['dy']
    radius = obj['radius']
    
    # Bounce off walls
    if x - radius <= boundary_left:
        dx = abs(dx)
        x = boundary_left + radius
    elif x + radius >= boundary_right:
        dx = -abs(dx)
        x = boundary_right - radius
    
    if y - radius <= boundary_bottom:
        dy = abs(dy)
        y = boundary_bottom + radius
    elif y + radius >= boundary_top:
        dy = -abs(dy)
        y = boundary_top - radius
    
    return x, y, dx, dy

def check_collision():
    """Check and handle collision between objects"""
    global collision_count
    
    # Calculate distance between centers
    dx = obj1['x'] - obj2['x']
    dy = obj1['y'] - obj2['y']
    distance = math.sqrt(dx**2 + dy**2)
    
    # Check if collision occurred
    if distance < obj1['radius'] + obj2['radius']:
        collision_count += 1
        
        # Simple elastic collision response
        # Swap velocities for a simple but effective collision
        obj1['dx'], obj2['dx'] = obj2['dx'], obj1['dx']
        obj1['dy'], obj2['dy'] = obj2['dy'], obj1['dy']
        
        # Push objects apart to prevent sticking
        overlap = (obj1['radius'] + obj2['radius']) - distance
        if overlap > 0:
            angle = math.atan2(dy, dx)
            move_x = math.cos(angle) * overlap / 2
            move_y = math.sin(angle) * overlap / 2
            obj1['x'] += move_x
            obj1['y'] += move_y
            obj2['x'] -= move_x
            obj2['y'] -= move_y
        
        return True
    return False

def update_positions():
    """Update object positions"""
    # Update object1
    x1, y1, dx1, dy1 = check_wall_collision(obj1)
    obj1['x'] = x1
    obj1['y'] = y1
    obj1['dx'] = dx1
    obj1['dy'] = dy1
    
    # Update object2
    x2, y2, dx2, dy2 = check_wall_collision(obj2)
    obj2['x'] = x2
    obj2['y'] = y2
    obj2['dx'] = dx2
    obj2['dy'] = dy2
    
    # Check collision between objects
    check_collision()
    
    # Update turtle positions
    object1.goto(obj1['x'], obj1['y'])
    object2.goto(obj2['x'], obj2['y'])

def update_info():
    """Update on-screen information"""
    info_display.clear()
    info_display.goto(-430, 330)
    info_display.write("COLLISION DETECTION DEMO", font=("Arial", 14, "bold"))
    info_display.goto(-430, 305)
    info_display.write(f"Red Circle: ({int(obj1['x'])}, {int(obj1['y'])}) | Speed: {abs(obj1['dx']):.1f}", 
                       font=("Arial", 10, "normal"))
    info_display.goto(-430, 285)
    info_display.write(f"Blue Square: ({int(obj2['x'])}, {int(obj2['y'])}) | Speed: {abs(obj2['dx']):.1f}", 
                       font=("Arial", 10, "normal"))
    
    collision_counter.clear()
    collision_counter.goto(-430, 260)
    collision_counter.write(f"Collisions: {collision_count}", font=("Arial", 12, "bold"))

def draw_boundary():
    """Draw the boundary walls"""
    boundary = turtle.Turtle()
    boundary.speed(0)
    boundary.color("white")
    boundary.penup()
    boundary.goto(boundary_left, boundary_bottom)
    boundary.pendown()
    boundary.pensize(3)
    for _ in range(2):
        boundary.forward(boundary_right - boundary_left)
        boundary.right(90)
        boundary.forward(boundary_top - boundary_bottom)
        boundary.right(90)
    boundary.hideturtle()

def draw_instructions():
    """Draw instruction text"""
    inst = turtle.Turtle()
    inst.speed(0)
    inst.color("gray")
    inst.penup()
    inst.hideturtle()
    inst.goto(0, 340)
    inst.write("SPACE=Pause | R=Reset | +/-=Speed | ESC=Exit", 
               align="center", font=("Arial", 12, "bold"))

def reset_simulation():
    """Reset objects to starting positions"""
    global collision_count, running
    
    obj1['x'] = -200
    obj1['y'] = 0
    obj1['dx'] = 3
    obj1['dy'] = 4
    
    obj2['x'] = 200
    obj2['y'] = 0
    obj2['dx'] = -4
    obj2['dy'] = -3
    
    collision_count = 0
    running = True
    
    update_info()

def increase_speed():
    """Increase object speeds"""
    obj1['dx'] *= 1.2
    obj1['dy'] *= 1.2
    obj2['dx'] *= 1.2
    obj2['dy'] *= 1.2
    # Cap maximum speed
    max_speed = 100
    for obj in [obj1, obj2]:
        obj['dx'] = max(min(obj['dx'], max_speed), -max_speed)
        obj['dy'] = max(min(obj['dy'], max_speed), -max_speed)

def decrease_speed():
    """Decrease object speeds"""
    obj1['dx'] *= 0.8
    obj1['dy'] *= 0.8
    obj2['dx'] *= 0.8
    obj2['dy'] *= 0.8
    # Minimum speed threshold
    min_speed = 1
    if abs(obj1['dx']) < min_speed and abs(obj1['dy']) < min_speed:
        obj1['dx'] = 3 if obj1['dx'] >= 0 else -3
        obj1['dy'] = 3 if obj1['dy'] >= 0 else -3
    if abs(obj2['dx']) < min_speed and abs(obj2['dy']) < min_speed:
        obj2['dx'] = 3 if obj2['dx'] >= 0 else -3
        obj2['dy'] = 3 if obj2['dy'] >= 0 else -3

def toggle_pause():
    global running
    running = not running
    
    # Show pause message
    pause_turtle = turtle.Turtle()
    pause_turtle.speed(0)
    pause_turtle.color("red")
    pause_turtle.penup()
    pause_turtle.hideturtle()
    if not running:
        pause_turtle.goto(0, 0)
        pause_turtle.write("PAUSED", align="center", font=("Arial", 30, "bold"))
        screen.update()
        turtle.time.sleep(0.5)
        pause_turtle.clear()
    else:
        pause_turtle.clear()

def animate():
    """Main animation loop"""
    global running
    
    while True:
        if running:
            update_positions()
            update_info()
        
        screen.update()
        turtle.time.sleep(0.016)  # ~60 FPS

# Draw initial elements
draw_boundary()
draw_instructions()
update_info()

# Keyboard bindings
screen.listen()
screen.onkey(toggle_pause, "space")
screen.onkey(reset_simulation, "r")
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")
screen.onkey(decrease_speed, "minus")
screen.onkey(lambda: screen.bye(), "Escape")

# Initial positions
object1.goto(obj1['x'], obj1['y'])
object2.goto(obj2['x'], obj2['y'])

print("=" * 50)
print("     COLLISION DETECTION DEMO")
print("=" * 50)
print()
print("Two objects moving and bouncing with realistic physics!")
print()
print("FEATURES:")
print("  • Elastic collisions between objects")
print("  • Wall collisions with bounce")
print("  • Real-time collision counter")
print("  • Speed adjustment")
print()
print("CONTROLS:")
print("  SPACE - Pause/Resume simulation")
print("  R     - Reset simulation")
print("  +/-   - Increase/Decrease object speed")
print("  ESC   - Exit program")
print()
print("Watch the red circle and blue square bounce off each other!")

# Start animation
try:
    animate()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()