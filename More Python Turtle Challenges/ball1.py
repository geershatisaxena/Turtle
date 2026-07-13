import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Bouncing Ball with Increasing Height")
screen.tracer(0)
screen.setup(800, 600)

# Create ground
ground = turtle.Turtle()
ground.speed(0)
ground.penup()
ground.goto(-400, -250)
ground.pendown()
ground.color("green")
ground.begin_fill()
ground.goto(400, -250)
ground.goto(400, -300)
ground.goto(-400, -300)
ground.goto(-400, -250)
ground.end_fill()
ground.hideturtle()

# Create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(1.5)
ball.penup()

# Ball physics variables
ball_x = 0
ball_y = -230  # Starting on the ground
velocity_y = 0
velocity_x = 2  # Slight horizontal movement
gravity = -0.5
bounce_count = 0
max_bounce_height = 30
height_increment = 5  # How much height increases each bounce

# Trail effect
trail = turtle.Turtle()
trail.speed(0)
trail.penup()
trail.hideturtle()
trail.color("red")
trail_positions = []

# Shadow
shadow = turtle.Turtle()
shadow.speed(0)
shadow.shape("circle")
shadow.color("dark gray")
shadow.shapesize(0.5)
shadow.penup()

# Function to draw trail
def draw_trail():
    trail.clear()
    if len(trail_positions) > 20:
        trail_positions.pop(0)
    
    for pos in trail_positions:
        trail.penup()
        trail.goto(pos[0], pos[1])
        trail.pendown()
        trail.dot(3)

# Create bounce counter display
counter_display = turtle.Turtle()
counter_display.speed(0)
counter_display.penup()
counter_display.hideturtle()
counter_display.goto(-350, 250)

# Create height display
height_display = turtle.Turtle()
height_display.speed(0)
height_display.penup()
height_display.hideturtle()
height_display.goto(-350, 220)

# Create status display
status_display = turtle.Turtle()
status_display.speed(0)
status_display.penup()
status_display.hideturtle()
status_display.goto(0, 250)

# Create velocity display
velocity_display = turtle.Turtle()
velocity_display.speed(0)
velocity_display.penup()
velocity_display.hideturtle()
velocity_display.goto(350, 250)

# Function to update displays
def update_displays():
    counter_display.clear()
    counter_display.write(f"Bounces: {bounce_count}", align="left", font=("Arial", 14, "bold"))
    
    height_display.clear()
    current_height = (ball_y + 230) * 0.5  # Scale for display
    height_display.write(f"Height: {current_height:.1f} units", align="left", font=("Arial", 14, "bold"))
    
    velocity_display.clear()
    velocity_display.write(f"Speed: {abs(velocity_y):.1f}", align="right", font=("Arial", 14, "bold"))

# Function to create a bounce effect
def create_bounce_effect():
    # Create particles on bounce
    for _ in range(8):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(random.choice(["orange", "yellow", "red"]))
        particle.shapesize(random.uniform(0.3, 0.6))
        particle.penup()
        particle.goto(ball_x + random.randint(-10, 10), ball_y)
        
        # Store particle data
        particle_data = {
            "turtle": particle,
            "vx": random.uniform(-3, 3),
            "vy": random.uniform(1, 4),
            "life": random.randint(10, 20)
        }
        particles.append(particle_data)

# Particles list
particles = []

# Function to update particles
def update_particles():
    for particle_data in particles[:]:
        particle_data["turtle"].goto(
            particle_data["turtle"].xcor() + particle_data["vx"],
            particle_data["turtle"].ycor() + particle_data["vy"]
        )
        particle_data["vy"] -= 0.2
        particle_data["life"] -= 1
        
        # Shrink particle
        size = particle_data["life"] / 20
        particle_data["turtle"].shapesize(max(0.1, size * 0.5))
        
        if particle_data["life"] <= 0:
            particle_data["turtle"].hideturtle()
            particles.remove(particle_data)

# Create bounce meter
meter = turtle.Turtle()
meter.speed(0)
meter.penup()
meter.hideturtle()
meter.goto(-300, -300)

def draw_bounce_meter():
    meter.clear()
    # Draw meter background
    meter.goto(-300, -300)
    meter.pendown()
    meter.color("light gray")
    meter.begin_fill()
    meter.goto(-300, -230)
    meter.goto(300, -230)
    meter.goto(300, -300)
    meter.goto(-300, -300)
    meter.end_fill()
    meter.penup()
    
    # Draw current bounce height
    current_height = (ball_y + 230) * 0.5
    max_height = max_bounce_height * 0.5
    if max_height > 0:
        percentage = min(1, current_height / max_height)
        meter.goto(-300, -300)
        meter.pendown()
        meter.color("green")
        meter.begin_fill()
        meter.goto(-300, -300 + percentage * 70)
        meter.goto(-300 + percentage * 600, -300 + percentage * 70)
        meter.goto(-300 + percentage * 600, -300)
        meter.goto(-300, -300)
        meter.end_fill()
        meter.penup()
        
        # Draw label
        meter.goto(0, -310)
        meter.color("black")
        meter.write(f"Height: {current_height:.1f} / {max_height:.1f}", 
                   align="center", font=("Arial", 10, "normal"))

# Create bounce effect on ground
def bounce_ground():
    # Flash effect
    flash = turtle.Turtle()
    flash.speed(0)
    flash.penup()
    flash.goto(ball_x, -250)
    flash.color("yellow")
    flash.shape("circle")
    flash.shapesize(2)
    flash.showturtle()
    
    def flash_animate(step=0):
        if step < 5:
            flash.shapesize(2 - step * 0.3)
            screen.ontimer(lambda: flash_animate(step + 1), 50)
        else:
            flash.hideturtle()
    
    flash_animate()

# Main animation loop
def animate():
    global ball_x, ball_y, velocity_y, velocity_x, bounce_count, max_bounce_height
    
    # Apply gravity
    velocity_y += gravity
    
    # Update position
    ball_x += velocity_x
    ball_y += velocity_y
    
    # Bounce off walls (horizontal)
    if ball_x > 380 or ball_x < -380:
        velocity_x *= -1
    
    # Bounce off ground
    if ball_y <= -230:
        ball_y = -230  # Position on ground
        
        # Increase bounce height
        max_bounce_height += height_increment
        
        # Calculate new velocity based on increased height
        # Using physics: v = sqrt(2 * g * h)
        velocity_y = math.sqrt(2 * abs(gravity) * max_bounce_height)
        bounce_count += 1
        
        # Create effects
        create_bounce_effect()
        bounce_ground()
        
        # Update displays
        update_displays()
        draw_bounce_meter()
        
        # Add some randomness to horizontal movement
        velocity_x += random.uniform(-0.5, 0.5)
        velocity_x = max(-5, min(5, velocity_x))  # Limit horizontal speed
    
    # Update ball position
    ball.goto(ball_x, ball_y)
    
    # Update shadow
    shadow.goto(ball_x, -250)
    shadow.shapesize(0.5 + (ball_y + 230) / 500)  # Shadow grows with height
    
    # Update trail
    trail_positions.append((ball_x, ball_y))
    draw_trail()
    
    # Update particles
    update_particles()
    
    # Randomly create a ripple effect on ground
    if bounce_count > 0 and bounce_count % 3 == 0 and ball_y > -230:
        # Create ground ripple
        ripple = turtle.Turtle()
        ripple.speed(0)
        ripple.penup()
        ripple.hideturtle()
        ripple.color("light green")
        ripple.goto(ball_x, -250)
        ripple.pendown()
        ripple.circle(5)
        ripple.penup()
        ripple.goto(ball_x, -255)
        ripple.pendown()
        ripple.circle(10)
        ripple.penup()
        ripple.goto(ball_x, -260)
        ripple.pendown()
        ripple.circle(15)
    
    screen.update()
    screen.ontimer(animate, 20)  # 50 FPS

# Create score/status text
status_display.goto(0, 250)
status_display.color("dark blue")
status_display.write("🏀 Jumping Ball", align="center", font=("Arial", 18, "bold"))

# Subtitle
subtitle = turtle.Turtle()
subtitle.speed(0)
subtitle.penup()
subtitle.hideturtle()
subtitle.goto(0, 220)
subtitle.color("gray")
subtitle.write("Each bounce goes higher!", align="center", font=("Arial", 12, "normal"))

# Controls
controls = turtle.Turtle()
controls.speed(0)
controls.penup()
controls.hideturtle()
controls.goto(0, -340)
controls.color("dark gray")
controls.write("Click to reset • Press SPACE to pause • R to reset", align="center", font=("Arial", 11, "normal"))

# Pause variable
paused = False
pause_text = None

def toggle_pause():
    global paused, pause_text
    paused = not paused
    if paused:
        pause_text = turtle.Turtle()
        pause_text.speed(0)
        pause_text.penup()
        pause_text.hideturtle()
        pause_text.goto(0, 100)
        pause_text.color("red")
        pause_text.write("⏸ PAUSED", align="center", font=("Arial", 30, "bold"))
    else:
        # Clear pause text
        if pause_text:
            pause_text.clear()
            pause_text.hideturtle()
            pause_text = None

def reset_animation():
    global ball_x, ball_y, velocity_y, velocity_x, bounce_count, max_bounce_height, trail_positions, particles, paused, pause_text
    
    # Reset ball
    ball_x = 0
    ball_y = -230
    velocity_y = 0
    velocity_x = 2
    bounce_count = 0
    max_bounce_height = 30
    
    # Clear trail
    trail_positions.clear()
    trail.clear()
    
    # Clear particles
    for particle in particles:
        particle["turtle"].hideturtle()
    particles.clear()
    
    # Clear pause
    paused = False
    if pause_text:
        pause_text.clear()
        pause_text.hideturtle()
        pause_text = None
    
    # Update displays
    update_displays()
    draw_bounce_meter()

# Key bindings
screen.onkey(toggle_pause, "space")
screen.onkey(reset_animation, "r")
screen.listen()

# Click to reset
screen.onclick(lambda x, y: reset_animation())

# Initial display setup
update_displays()
draw_bounce_meter()

# Start animation
animate()

# Keep window open
screen.mainloop()