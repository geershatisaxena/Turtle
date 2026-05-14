import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Fireworks - Click anywhere for a random burst!")
screen.bgcolor("midnightblue")
screen.tracer(0)  # Turn off automatic updates for smooth animation

# List to store all active particles
particles = []

class Particle:
    def __init__(self, x, y, vx, vy, color, size=3, lifetime=100):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.shapesize(size / 10)  # Convert size to turtle units
        self.turtle.speed(0)
        
        self.vx = vx
        self.vy = vy
        self.gravity = -0.2
        self.lifetime = lifetime  # Frames until particle fades
        self.age = 0
        self.size = size
        self.color_name = color  # Store the color name
        
    def update(self):
        """Update particle position and velocity."""
        # Apply gravity to vertical velocity
        self.vy += self.gravity
        
        # Update position
        x, y = self.turtle.position()
        new_x = x + self.vx
        new_y = y + self.vy
        self.turtle.goto(new_x, new_y)
        
        # Age the particle
        self.age += 1
        
        # Fade out (reduce size)
        if self.age > self.lifetime * 0.6:
            # Gradually shrink the particle
            fade_progress = (self.age - self.lifetime * 0.6) / (self.lifetime * 0.4)
            new_size = max(0.1, (self.size / 10) * (1 - fade_progress))
            self.turtle.shapesize(new_size)
        elif self.age > self.lifetime * 0.3:
            # Start shrinking slightly
            shrink_progress = (self.age - self.lifetime * 0.3) / (self.lifetime * 0.3)
            new_size = max(0.2, (self.size / 10) * (1 - shrink_progress * 0.5))
            self.turtle.shapesize(new_size)
        
        return self.age < self.lifetime  # Return False if particle should be removed
    
    def remove(self):
        """Remove particle turtle from screen."""
        self.turtle.hideturtle()
        self.turtle.clear()

def random_color():
    """Generate a random vibrant color."""
    # Use bright, saturated colors for fireworks
    colors = [
        "red", "orange", "yellow", "lime", "green", 
        "cyan", "blue", "purple", "magenta", "pink",
        "gold", "coral", "hotpink", "springgreen", "deepskyblue",
        "tomato", "violet", "indigo", "crimson", "orchid"
    ]
    return random.choice(colors)

def create_firework(x, y):
    """Create an explosion of particles at (x, y)."""
    # Number of particles in the burst
    num_particles = random.randint(40, 100)
    
    # Center color for the firework
    center_color = random_color()
    
    for _ in range(num_particles):
        # Random velocity in all directions
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 10)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        
        # Add some randomness to velocities
        vx += random.uniform(-1, 1)
        vy += random.uniform(-1, 1)
        
        # Random particle size
        size = random.uniform(2, 6)
        
        # Random lifetime (longer for slower particles)
        lifetime = random.randint(80, 150)
        
        # Slight color variation
        if random.random() < 0.3:  # 30% chance of different color
            color_variation = random_color()
        else:
            color_variation = center_color
        
        particle = Particle(x, y, vx, vy, color_variation, size, lifetime)
        particles.append(particle)
    
    # Add a few "sparkle" particles that last longer
    for _ in range(random.randint(5, 15)):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 4)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        particle = Particle(x, y, vx, vy, "yellow", 2, random.randint(120, 180))
        particles.append(particle)

def animate():
    """Animation loop - update all particles."""
    global particles
    
    # Update each particle
    active_particles = []
    for particle in particles:
        if particle.update():
            active_particles.append(particle)
        else:
            particle.remove()
    
    particles = active_particles
    
    # Update screen
    screen.update()
    
    # Continue animation
    screen.ontimer(animate, 16)  # ~60 FPS

def on_click(x, y):
    """Handle mouse click - create a firework burst."""
    print(f"💥 Firework burst at ({x}, {y})")
    create_firework(x, y)

# Instructions
print("=" * 50)
print("🎆 FIREWORKS SIMULATOR 🎆")
print("=" * 50)
print("Click anywhere on the screen for a random fireworks burst!")
print("Click multiple times for overlapping spectacular displays!")
print("Close the window to exit.")
print("=" * 50)

# Bind click event
screen.onclick(on_click)

# Start animation
animate()

# Keep window open
screen.mainloop()