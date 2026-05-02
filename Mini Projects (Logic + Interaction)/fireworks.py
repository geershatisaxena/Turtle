import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Fireworks Animation")
screen.bgcolor("midnightblue")
screen.setup(width=900, height=700)
screen.tracer(0)

# List to store active particles
particles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "gold", "white"]

class Particle:
    def __init__(self, x, y, vx, vy, color, size, lifetime):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.shapesize(size/10, size/10)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.vx = vx
        self.vy = vy
        self.gravity = -0.3
        self.lifetime = lifetime
        self.age = 0
        
    def update(self):
        self.vx += random.uniform(-0.2, 0.2)  # Air resistance
        self.vy += self.gravity
        x = self.turtle.xcor() + self.vx
        y = self.turtle.ycor() + self.vy
        self.turtle.goto(x, y)
        self.age += 1
        
        # Fade out effect (shrink and slow down)
        if self.age > self.lifetime * 0.7:
            current_size = self.turtle.shapesize()[0]
            new_size = max(0.1, current_size - 0.05)
            self.turtle.shapesize(new_size, new_size)
        
        return self.age < self.lifetime and abs(y) < 400
    
    def cleanup(self):
        self.turtle.hideturtle()
        self.turtle.clear()

class Rocket:
    def __init__(self, x, y, target_y):
        self.turtle = turtle.Turtle()
        self.turtle.shape("triangle")
        self.turtle.color("white")
        self.turtle.shapesize(0.8, 0.8)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(90)
        self.x = x
        self.y = y
        self.target_y = target_y
        self.speed = random.uniform(5, 8)
        
    def update(self):
        self.y += self.speed
        self.turtle.goto(self.x, self.y)
        # Add trail effect
        trail = turtle.Turtle()
        trail.shape("circle")
        trail.color("yellow")
        trail.shapesize(0.2, 0.2)
        trail.penup()
        trail.goto(self.x, self.y - 5)
        trail.pendown()
        screen.ontimer(lambda: trail.clear() or trail.hideturtle(), 50)
        return self.y >= self.target_y
    
    def cleanup(self):
        self.turtle.hideturtle()
        self.turtle.clear()

def create_explosion(x, y, color_scheme=None):
    """Create a firework explosion at (x, y)"""
    particle_count = random.randint(50, 100)
    if color_scheme is None:
        # Random colors
        explosion_colors = random.sample(colors, random.randint(3, 5))
    else:
        explosion_colors = color_scheme
    
    for _ in range(particle_count):
        # Random velocity in all directions
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 12)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed + 5  # Slight upward burst
        
        color = random.choice(explosion_colors)
        size = random.uniform(0.3, 0.8)
        lifetime = random.randint(40, 80)
        
        particle = Particle(x, y, vx, vy, color, size, lifetime)
        particles.append(particle)

def launch_random_firework():
    """Launch a firework rocket from a random ground position"""
    x = random.randint(-400, 400)
    target_y = random.randint(100, 300)
    rocket = Rocket(x, -300, target_y)
    rockets.append(rocket)

def draw_ground():
    """Draw the ground/city silhouette"""
    ground_drawer = turtle.Turtle()
    ground_drawer.speed(0)
    ground_drawer.color("black")
    ground_drawer.penup()
    ground_drawer.goto(-450, -320)
    ground_drawer.pendown()
    ground_drawer.begin_fill()
    ground_drawer.goto(450, -320)
    ground_drawer.goto(450, -350)
    ground_drawer.goto(-450, -350)
    ground_drawer.goto(-450, -320)
    ground_drawer.end_fill()
    
    # Draw buildings silhouette
    ground_drawer.penup()
    ground_drawer.goto(-450, -320)
    ground_drawer.pendown()
    ground_drawer.color("darkgray")
    
    for x in range(-430, 450, 40):
        height = random.randint(20, 80)
        ground_drawer.penup()
        ground_drawer.goto(x, -320)
        ground_drawer.pendown()
        ground_drawer.goto(x, -320 + height)
        ground_drawer.goto(x + 20, -320 + height)
        ground_drawer.goto(x + 20, -320)
    
    ground_drawer.hideturtle()

def draw_title():
    """Draw animated title"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("yellow")
    title.penup()
    title.hideturtle()
    title.goto(0, 300)
    title.write("✨ FIREWORKS SHOW ✨", align="center", font=("Arial", 24, "bold"))
    return title

def draw_instructions():
    """Draw instruction text"""
    inst = turtle.Turtle()
    inst.speed(0)
    inst.color("white")
    inst.penup()
    inst.hideturtle()
    inst.goto(0, -330)
    inst.write("Press SPACE for a firework | F for random burst | C to clear | ESC to exit", 
               align="center", font=("Arial", 12, "normal"))
    return inst

def display_fps():
    """Display FPS counter"""
    fps_display.clear()
    fps_display.goto(-430, 330)
    fps_display.write(f"Particles: {len(particles)}", font=("Arial", 10, "normal"))

def add_mouse_firework(x, y):
    """Add firework at mouse click position"""
    if y > -300:  # Don't explode underground
        create_explosion(x, y)

def space_firework():
    """Launch a firework at random position"""
    x = random.randint(-350, 350)
    y = random.randint(100, 280)
    create_explosion(x, y)

def burst_fireworks():
    """Create multiple fireworks at once"""
    for _ in range(5):
        x = random.randint(-350, 350)
        y = random.randint(50, 280)
        create_explosion(x, y)

def clear_fireworks():
    """Clear all fireworks particles"""
    global particles
    for particle in particles:
        particle.cleanup()
    particles = []

def animate():
    """Main animation loop"""
    global rockets, particles
    
    # Update rockets
    for rocket in rockets[:]:
        if rocket.update():
            create_explosion(rocket.x, rocket.y)
            rocket.cleanup()
            rockets.remove(rocket)
    
    # Update particles
    for particle in particles[:]:
        if not particle.update():
            particle.cleanup()
            particles.remove(particle)
    
    # Update UI
    display_fps()
    screen.update()
    
    # Schedule next frame
    screen.ontimer(animate, 30)

# Create UI elements
fps_display = turtle.Turtle()
fps_display.speed(0)
fps_display.color("lightgreen")
fps_display.penup()
fps_display.hideturtle()

# Draw static elements
draw_ground()
title = draw_title()
instructions = draw_instructions()

# Firework management
rockets = []
particles = []

# Keyboard bindings
screen.listen()
screen.onkey(space_firework, "space")
screen.onkey(burst_fireworks, "f")
screen.onkey(clear_fireworks, "c")
screen.onkey(lambda: launch_random_firework(), "r")
screen.onkey(lambda: screen.bye(), "Escape")

# Mouse bindings
screen.onclick(add_mouse_firework)

# Print console instructions
print("=== FIREWORKS ANIMATION ===")
print()
print("Watch colorful fireworks explode with particle effects!")
print()
print("CONTROLS:")
print("  SPACE - Launch a single firework at random position")
print("  Click - Launch firework at mouse position")
print("  F     - Burst multiple fireworks (5 at once)")
print("  R     - Launch rocket firework from ground")
print("  C     - Clear all fireworks")
print("  ESC   - Exit program")
print()
print("Rockets launch from the ground and explode in the sky!")
print("Each explosion creates 50-100 particles with gravity effect.")

# Start the animation with some initial fireworks
for _ in range(3):
    screen.ontimer(lambda: space_firework(), random.randint(500, 2000))

# Start animation
animate()

# Keep window open
screen.mainloop()