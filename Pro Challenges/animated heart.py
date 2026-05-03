import turtle
import math
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Animated Heart Shape")
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.tracer(0)

# Create the heart turtle
heart = turtle.Turtle()
heart.speed(0)
heart.penup()
heart.hideturtle()

# Create particle turtles for effects
particles = []

# Animation state
beating = True
beat_scale = 1.0
beat_direction = 1
color_cycle = 0

# Heart colors
colors = ["red", "crimson", "firebrick", "darkred", "hotpink", "deeppink", "tomato"]

def draw_heart(x, y, scale, color):
    """Draw a heart shape at given position with scale and color"""
    heart.clear()
    heart.penup()
    heart.goto(x, y)
    heart.setheading(0)
    heart.color(color)
    heart.pendown()
    heart.begin_fill()
    
    # Heart shape using parametric equations
    heart.penup()
    heart.goto(x, y - 60 * scale)
    heart.pendown()
    
    # Left curve
    heart.left(50)
    for _ in range(150):
        heart.forward(1 * scale)
        heart.left(1)
    
    # Right curve
    heart.left(120)
    for _ in range(150):
        heart.forward(1 * scale)
        heart.left(1)
    
    heart.left(120)
    heart.end_fill()
    heart.penup()

def draw_perfect_heart(x, y, size, color):
    """Draw a mathematically perfect heart using coordinates"""
    heart.clear()
    heart.penup()
    heart.goto(x, y)
    heart.color(color)
    heart.pendown()
    heart.begin_fill()
    
    # Parametric heart: x = 16*sin(t)^3, y = 13*cos(t) - 5*cos(2t) - 2*cos(3t) - cos(4t)
    points = []
    for t in range(0, 360):
        t_rad = math.radians(t)
        x_point = 16 * math.sin(t_rad) ** 3
        y_point = 13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad)
        points.append((x_point * size + x, -y_point * size + y))
    
    # Draw the heart
    for i, (px, py) in enumerate(points):
        if i == 0:
            heart.goto(px, py)
        else:
            heart.goto(px, py)
    
    heart.end_fill()
    heart.penup()

def draw_sparkle(x, y):
    """Draw a sparkle at given position"""
    sparkle = turtle.Turtle()
    sparkle.speed(0)
    sparkle.shape("circle")
    sparkle.color(random.choice(["gold", "yellow", "orange", "pink", "white"]))
    sparkle.shapesize(0.3, 0.3)
    sparkle.penup()
    sparkle.goto(x, y)
    particles.append(sparkle)

def create_particle_burst():
    """Create a burst of particles around the heart"""
    for _ in range(30):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(random.choice(["red", "pink", "gold", "orange", "white"]))
        particle.shapesize(random.uniform(0.1, 0.4), random.uniform(0.1, 0.4))
        particle.penup()
        
        # Random position around the heart
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(80, 150)
        x = -150 * math.cos(angle) + random.randint(-50, 50)
        y = 100 * math.sin(angle) + random.randint(-50, 50)
        particle.goto(x, y)
        
        # Store velocity for animation
        particle.vx = random.uniform(-3, 3)
        particle.vy = random.uniform(-3, 3)
        particle.life = random.randint(30, 60)
        particles.append(particle)

def animate_particles():
    """Animate and remove particles"""
    for particle in particles[:]:
        if hasattr(particle, 'life'):
            particle.life -= 1
            if particle.life <= 0:
                particle.hideturtle()
                particle.clear()
                particles.remove(particle)
                continue
            
            # Move particle
            particle.goto(particle.xcor() + particle.vx, particle.ycor() + particle.vy)
            particle.vx *= 0.95
            particle.vy -= 0.2
            
            # Fade out by shrinking
            current_size = particle.shapesize()
            new_size = max(0.05, current_size[0] - 0.01)
            particle.shapesize(new_size, new_size)

def draw_glow():
    """Draw a glowing effect around the heart"""
    glow = turtle.Turtle()
    glow.speed(0)
    glow.penup()
    glow.hideturtle()
    
    for radius in range(20, 60, 5):
        glow.color(f"rgba(255, 0, 0, {1 - radius/60})")
        glow.goto(0, 0)
        glow.pendown()
        glow.circle(radius * beat_scale)
        glow.penup()
    
    glow.clear()

def draw_text():
    """Draw romantic text"""
    text = turtle.Turtle()
    text.speed(0)
    text.color("white")
    text.penup()
    text.hideturtle()
    
    # Draw "Love" text
    text.goto(0, -200)
    text.write("❤️ LOVE YOU! ❤️", align="center", font=("Arial", 20, "bold"))
    
    text.goto(0, -250)
    text.write("Press SPACE to toggle beat | C to change color | P for particles | ESC to exit",
               align="center", font=("Arial", 10, "normal"))

def draw_floating_hearts():
    """Draw small floating hearts around"""
    floating = []
    for _ in range(8):
        fh = turtle.Turtle()
        fh.speed(0)
        fh.shape("turtle")
        fh.color(random.choice(["pink", "red", "hotpink"]))
        fh.shapesize(0.5, 0.5)
        fh.penup()
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(180, 250)
        fh.goto(-150 * math.cos(angle), 100 * math.sin(angle))
        fh.angle_offset = random.uniform(0, 2 * math.pi)
        fh.radius = radius
        floating.append(fh)
    return floating

def animate_floating_hearts(floating_hearts, time_count):
    """Animate floating hearts orbiting"""
    for i, fh in enumerate(floating_hearts):
        angle = time_count * 0.02 + i * math.pi / 4
        x = -150 * math.cos(angle) * 1.5
        y = 100 * math.sin(angle) * 1.2
        fh.goto(x, y)
        fh.setheading(math.degrees(angle))

def change_color():
    """Cycle through heart colors"""
    global current_color, color_cycle
    color_cycle = (color_cycle + 1) % len(colors)
    current_color = colors[color_cycle]

def toggle_beat():
    """Toggle beating animation on/off"""
    global beating
    beating = not beating

def add_particles():
    """Add particle burst effect"""
    create_particle_burst()

def draw_heart_shape():
    """Main function to draw and animate the heart"""
    global beat_scale, beat_direction, current_color
    
    # Create floating hearts
    floating_hearts = draw_floating_hearts()
    
    # Main animation loop
    frame = 0
    
    while True:
        # Update beat scale
        if beating:
            beat_scale += 0.02 * beat_direction
            if beat_scale >= 1.2:
                beat_direction = -1
            elif beat_scale <= 0.9:
                beat_direction = 1
        
        # Draw the heart
        draw_perfect_heart(0, 0, 1.5 * beat_scale, current_color)
        
        # Add glow effect (simple version)
        heart.penup()
        heart.goto(0, 0)
        heart.pendown()
        heart.color(current_color)
        heart.pensize(3)
        heart.circle(60 * beat_scale)
        heart.penup()
        
        # Animate particles
        animate_particles()
        
        # Animate floating hearts
        animate_floating_hearts(floating_hearts, frame)
        
        # Update frame counter
        frame += 1
        
        # Occasionally add sparkles
        if frame % 50 == 0:
            for _ in range(5):
                angle = random.uniform(0, 2 * math.pi)
                radius = random.uniform(50, 100)
                x = -150 * math.cos(angle) + random.randint(-30, 30)
                y = 100 * math.sin(angle) + random.randint(-30, 30)
                draw_sparkle(x, y)
        
        # Update screen
        screen.update()
        time.sleep(0.03)
        
        # Refresh display every few frames
        if frame % 100 == 0:
            draw_text()

# Initialize heart parameters
current_color = "red"

# Draw initial text
draw_text()

# Start the animated heart
screen.tracer(0)

# Keyboard bindings
screen.listen()
screen.onkey(change_color, "c")
screen.onkey(toggle_beat, "space")
screen.onkey(add_particles, "p")
screen.onkey(lambda: screen.bye(), "Escape")

print("=" * 50)
print("     ANIMATED HEART SHAPE")
print("=" * 50)
print()
print("A beautiful animated heart that beats and sparkles!")
print()
print("CONTROLS:")
print("  SPACE - Toggle beating animation on/off")
print("  C     - Change heart color")
print("  P     - Add particle burst effect")
print("  ESC   - Exit program")
print()
print("Watch the heart beat and the floating hearts orbit around!")

# Run the animation in a try-except to handle keyboard interrupt gracefully
try:
    draw_heart_shape()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

# Keep window open (though the loop runs continuously)
screen.mainloop()