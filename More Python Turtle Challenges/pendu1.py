import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pendulum Swing Simulation")
screen.tracer(0)  # Turn off automatic updates for smooth animation
screen.setup(800, 600)

# Constants
GRAVITY = 0.5
DAMPING = 0.9995  # Slight energy loss to eventually stop
PENDULUM_LENGTH = 200
ANGLE = 45  # Starting angle in degrees

# Create the pendulum bob
bob = turtle.Turtle()
bob.speed(0)
bob.shape("circle")
bob.color("red")
bob.shapesize(1.5)
bob.penup()

# Create the pendulum arm
arm = turtle.Turtle()
arm.speed(0)
arm.color("black")
arm.penup()
arm.pensize(2)

# Create the pivot point
pivot = turtle.Turtle()
pivot.speed(0)
pivot.shape("circle")
pivot.color("black")
pivot.shapesize(0.8)
pivot.penup()
pivot.goto(0, 200)

# Create the support structure
support = turtle.Turtle()
support.speed(0)
support.color("gray")
support.penup()
support.pensize(3)

# Draw support structure
support.goto(-100, 200)
support.pendown()
support.goto(100, 200)
support.penup()
support.goto(-80, 200)
support.pendown()
support.goto(-80, 220)
support.penup()
support.goto(80, 200)
support.pendown()
support.goto(80, 220)
support.hideturtle()

# Draw angle arc and labels
angle_turtle = turtle.Turtle()
angle_turtle.speed(0)
angle_turtle.hideturtle()
angle_turtle.penup()

# Info display
info_turtle = turtle.Turtle()
info_turtle.speed(0)
info_turtle.hideturtle()
info_turtle.penup()
info_turtle.goto(-350, 250)

# Velocity and angle displays
display_turtle = turtle.Turtle()
display_turtle.speed(0)
display_turtle.hideturtle()
display_turtle.penup()
display_turtle.goto(0, -280)

# Variables for physics simulation
angle_rad = math.radians(ANGLE)  # Current angle in radians
angular_velocity = 0  # Current angular velocity
angular_acceleration = 0  # Current angular acceleration
time_step = 0.02
pivot_x = 0
pivot_y = 200

# Trail effect (optional - uncomment to enable)
# trail = turtle.Turtle()
# trail.speed(0)
# trail.color("red", "red")
# trail.penup()
# trail.hideturtle()
# trail_positions = []

# Function to draw the angle arc
def draw_angle_arc(current_angle, max_angle):
    angle_turtle.clear()
    if abs(current_angle) > 0.01:
        # Draw arc for current angle
        angle_turtle.penup()
        angle_turtle.goto(pivot_x, pivot_y)
        angle_turtle.pendown()
        angle_turtle.color("blue")
        angle_turtle.pensize(1)
        
        # Draw arc
        radius = 40
        start_angle = -max_angle
        end_angle = -current_angle
        angle_turtle.goto(pivot_x + radius * math.sin(math.radians(start_angle)), 
                         pivot_y - radius * math.cos(math.radians(start_angle)))
        angle_turtle.pendown()
        angle_turtle.circle(radius, end_angle - start_angle)
        angle_turtle.penup()
        
        # Draw angle labels
        angle_turtle.goto(pivot_x + 60 * math.sin(math.radians(-current_angle)), 
                         pivot_y - 60 * math.cos(math.radians(-current_angle)))
        angle_turtle.color("blue")
        angle_turtle.write(f"{abs(round(math.degrees(current_angle), 1))}°", 
                          align="center", font=("Arial", 10, "normal"))

# Function to update physics
def update_pendulum():
    global angle_rad, angular_velocity, angular_acceleration
    
    # Calculate angular acceleration using pendulum equation
    # α = -(g/L) * sin(θ)
    angular_acceleration = -(GRAVITY / PENDULUM_LENGTH) * math.sin(angle_rad)
    
    # Update angular velocity with damping
    angular_velocity += angular_acceleration * time_step
    angular_velocity *= DAMPING
    
    # Update angle
    angle_rad += angular_velocity * time_step

# Function to draw pendulum
def draw_pendulum():
    # Calculate bob position
    bob_x = pivot_x + PENDULUM_LENGTH * math.sin(angle_rad)
    bob_y = pivot_y - PENDULUM_LENGTH * math.cos(angle_rad)
    
    # Draw arm
    arm.clear()
    arm.goto(pivot_x, pivot_y)
    arm.pendown()
    arm.goto(bob_x, bob_y)
    arm.penup()
    
    # Move bob
    bob.goto(bob_x, bob_y)
    
    # Draw angle arc
    current_angle_deg = math.degrees(angle_rad)
    draw_angle_arc(current_angle_deg, 60)  # Max angle for arc display
    
    return bob_x, bob_y

# Function to update info display
def update_info():
    info_turtle.clear()
    current_angle = math.degrees(angle_rad)
    velocity = abs(angular_velocity * PENDULUM_LENGTH / 10)  # Approximate linear velocity
    
    # Show pendulum stats
    info_turtle.goto(-350, 250)
    info_turtle.write("Pendulum Physics", align="left", font=("Arial", 14, "bold"))
    info_turtle.goto(-350, 225)
    info_turtle.write(f"Angle: {current_angle:.1f}°", align="left", font=("Arial", 12, "normal"))
    info_turtle.goto(-350, 205)
    info_turtle.write(f"Velocity: {velocity:.1f} m/s", align="left", font=("Arial", 12, "normal"))
    info_turtle.goto(-350, 185)
    info_turtle.write(f"Energy: {abs(current_angle):.1f}%", align="left", font=("Arial", 12, "normal"))

# Function to create a string trace (optional)
def create_string_trace():
    string_turtle = turtle.Turtle()
    string_turtle.speed(0)
    string_turtle.color("light gray")
    string_turtle.penup()
    string_turtle.hideturtle()
    
    # Draw vertical dotted line for reference
    string_turtle.goto(0, 200)
    string_turtle.pendown()
    string_turtle.pensize(1)
    string_turtle.goto(0, 0)
    string_turtle.penup()
    
    # Draw horizontal reference line
    string_turtle.goto(-PENDULUM_LENGTH, 0)
    string_turtle.pendown()
    string_turtle.goto(PENDULUM_LENGTH, 0)
    string_turtle.hideturtle()

# Function to reset pendulum on click
def reset_pendulum(x, y):
    global angle_rad, angular_velocity
    angle_rad = math.radians(45)  # Reset to 45 degrees
    angular_velocity = 0
    # Clear trail if using
    # trail.clear()
    # trail_positions.clear()

# Function to toggle pause on space key
paused = False

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_text = turtle.Turtle()
        pause_text.hideturtle()
        pause_text.penup()
        pause_text.goto(0, 100)
        pause_text.color("red")
        pause_text.write("⏸ PAUSED", align="center", font=("Arial", 24, "bold"))
        pause_text.goto(0, 70)
        pause_text.write("Press SPACE to resume", align="center", font=("Arial", 14, "normal"))
    else:
        # Clear pause text
        for item in screen.turtles():
            if item.isvisible() and item.xcor() == 0 and item.ycor() == 100:
                item.clear()
                item.hideturtle()

# Main animation loop
def animate():
    global paused, angular_velocity, angle_rad  # Add angular_velocity and angle_rad to global declaration
    
    if not paused:
        update_pendulum()
        
        # Draw pendulum
        bob_x, bob_y = draw_pendulum()
        
        # Update information
        update_info()
        
        # If pendulum has almost stopped, add a small nudge to keep it moving
        if abs(angular_velocity) < 0.0005 and abs(math.degrees(angle_rad)) > 1:
            angular_velocity += 0.0001 * math.copysign(1, -angle_rad)
    
    screen.update()
    screen.ontimer(animate, 20)  # 50 FPS

# Create reference lines
create_string_trace()

# Add instruction text
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, -300)
instructions.color("gray")
instructions.write("Click on screen to reset • Press SPACE to pause", 
                  align="center", font=("Arial", 12, "normal"))

# Display controls
controls = turtle.Turtle()
controls.hideturtle()
controls.penup()
controls.goto(350, 250)
controls.color("gray")
controls.write("Controls:", align="center", font=("Arial", 12, "bold"))
controls.goto(350, 230)
controls.write("Click: Reset", align="center", font=("Arial", 11, "normal"))
controls.goto(350, 210)
controls.write("SPACE: Pause", align="center", font=("Arial", 11, "normal"))

# Bind events
screen.onclick(reset_pendulum)
screen.onkey(toggle_pause, "space")
screen.listen()

# Start animation
animate()

# Keep window open
screen.mainloop()