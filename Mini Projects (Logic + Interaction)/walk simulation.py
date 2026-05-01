import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Random Walk Simulation")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off animation for smoother drawing

# Create the walking turtle
walker = turtle.Turtle()
walker.shape("turtle")
walker.speed(0)
walker.pensize(2)
walker.penup()
walker.goto(0, 0)
walker.pendown()

# Color palette for the walk
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "white", "lime", "magenta"]

# Variables
step_size = 10
angle_choices = [0, 45, 90, 135, 180, 225, 270, 315]  # 8 possible directions
walking = True
color_change_freq = 5  # Change color every N steps
steps_taken = 0

# UI elements
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("white")
info_display.penup()
info_display.hideturtle()

def update_info():
    """Update the on-screen information"""
    info_display.clear()
    info_display.goto(-380, 260)
    info_display.write(f"Steps: {steps_taken} | Position: ({int(walker.xcor())}, {int(walker.ycor())}) | Step Size: {step_size}",
                       font=("Arial", 10, "normal"))

def random_walk_step():
    """Take one random step"""
    global steps_taken, walking
    
    if not walking:
        return
    
    # Choose random angle
    angle = random.choice(angle_choices)
    walker.setheading(angle)
    
    # Take a step
    walker.forward(step_size)
    steps_taken += 1
    
    # Change color periodically
    if steps_taken % color_change_freq == 0:
        walker.color(random.choice(colors))
    
    # Update display
    update_info()
    screen.update()
    
    # Check boundaries (optional: wrap around or bounce)
    x, y = walker.xcor(), walker.ycor()
    
    # Option 1: Wrap around screen edges
    if x > 390:
        walker.setx(-390)
    elif x < -390:
        walker.setx(390)
    if y > 290:
        walker.sety(-290)
    elif y < -290:
        walker.sety(290)
    
    # Schedule next step
    screen.ontimer(random_walk_step, 50)  # 50ms delay between steps

# Control functions
def increase_speed():
    """Decrease delay between steps (make walk faster)"""
    global step_size
    step_size = min(step_size + 2, 30)
    update_info()

def decrease_speed():
    """Increase delay between steps (make walk slower)"""
    global step_size
    step_size = max(step_size - 2, 2)
    update_info()

def toggle_walk():
    """Pause or resume the random walk"""
    global walking
    walking = not walking
    if walking:
        random_walk_step()  # Resume walking

def clear_trail():
    """Clear all drawings but keep turtle at current position"""
    walker.clear()
    walker.penup()
    pos = walker.pos()
    walker.goto(pos)
    walker.pendown()
    update_info()

def reset_walk():
    """Reset the entire simulation"""
    global steps_taken, walking
    walker.clear()
    walker.penup()
    walker.goto(0, 0)
    walker.pendown()
    walker.color(random.choice(colors))
    steps_taken = 0
    walking = True
    update_info()
    random_walk_step()

def change_color():
    """Manually change turtle color"""
    walker.color(random.choice(colors))
    update_info()

def draw_burst():
    """Draw a burst of random steps from current position"""
    original_pos = walker.pos()
    original_color = walker.color()[0]
    
    for _ in range(36):  # 36 steps in a circle
        walker.forward(step_size)
        walker.backward(step_size)
        walker.right(10)
    
    walker.goto(original_pos)
    walker.color(original_color)
    update_info()

# Keyboard bindings
screen.listen()
screen.onkey(toggle_walk, "space")
screen.onkey(clear_trail, "c")
screen.onkey(reset_walk, "r")
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")
screen.onkey(decrease_speed, "minus")
screen.onkey(change_color, "v")
screen.onkey(draw_burst, "b")
screen.onkey(lambda: exit(), "Escape")

# Draw instruction panel
instruction_turtle = turtle.Turtle()
instruction_turtle.speed(0)
instruction_turtle.color("lightgray")
instruction_turtle.penup()
instruction_turtle.hideturtle()
instruction_turtle.goto(-380, -260)
instruction_turtle.write("CONTROLS: SPACE=Pause/Resume  C=Clear  R=Reset  +/-=Step Size  V=Color  B=Burst  ESC=Exit",
                         font=("Arial", 10, "normal"))

# Initial display
update_info()
walker.color(random.choice(colors))

# Print instructions to console
print("=== RANDOM WALK SIMULATION ===")
print()
print("The turtle takes random steps in 8 directions (N, NE, E, SE, S, SW, W, NW)")
print()
print("CONTROLS:")
print("  SPACE - Pause / Resume the random walk")
print("  C     - Clear the trail (keep turtle position)")
print("  R     - Reset the simulation (return to center)")
print("  + / = - Increase step size (faster movement)")
print("  -     - Decrease step size (slower movement)")
print("  V     - Manually change color")
print("  B     - Draw a burst pattern")
print("  ESC   - Exit the program")
print()
print("Watch as the turtle creates a unique path each time!")

# Start the random walk
screen.update()
random_walk_step()

# Keep window open
screen.mainloop()