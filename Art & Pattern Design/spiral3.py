import turtle
import random
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Galaxy Spiral")
screen.tracer(0)

# Create turtle
galaxy = turtle.Turtle()
galaxy.speed(0)
galaxy.hideturtle()

# Color palette for galaxy
colors = [
    "#FF6B6B",  # Red
    "#FFA07A",  # Light Salmon
    "#FFD93D",  # Gold
    "#6BCB77",  # Green
    "#4D96FF",  # Blue
    "#9B59B6",  # Purple
    "#FF69B4",  # Hot Pink
    "#00CED1",  # Dark Turquoise
    "#FF4500",  # Orange Red
    "#DA70D6",  # Orchid
]

def draw_spiral_arm(start_radius, num_stars, arm_offset, direction=1):
    """Draw a single spiral arm"""
    for i in range(num_stars):
        # Calculate position using logarithmic spiral
        radius = start_radius + i * 0.5
        angle = i * 0.15 + arm_offset
        
        x = radius * math.cos(angle * direction)
        y = radius * math.sin(angle * direction)
        
        # Random size variation
        size = random.uniform(1, 4)
        
        # Random color from palette
        color = random.choice(colors)
        galaxy.color(color)
        
        # Draw star
        galaxy.penup()
        galaxy.goto(x, y)
        galaxy.pendown()
        
        # Create star shape with varying sizes
        if i % 3 == 0:
            # Larger stars with glow effect
            galaxy.dot(size * 3)
        else:
            galaxy.dot(size)
        
        # Add some random scattered stars near the arm
        if i % 5 == 0:
            for _ in range(3):
                scatter_x = x + random.uniform(-10, 10)
                scatter_y = y + random.uniform(-10, 10)
                galaxy.penup()
                galaxy.goto(scatter_x, scatter_y)
                galaxy.pendown()
                galaxy.color(random.choice(colors))
                galaxy.dot(random.uniform(0.5, 1.5))

def draw_galaxy():
    """Draw the complete galaxy with multiple spiral arms"""
    
    # Galaxy center - bright core
    for i in range(50):
        radius = i * 1.5
        angle = random.uniform(0, 2 * math.pi)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        
        galaxy.penup()
        galaxy.goto(x, y)
        galaxy.pendown()
        
        # Core stars - bright and warm colors
        if i < 30:
            galaxy.color(random.choice(["#FFF5E6", "#FFD700", "#FFA500"]))
            galaxy.dot(random.uniform(2, 5))
        else:
            galaxy.color(random.choice(["#FFD93D", "#FFA07A"]))
            galaxy.dot(random.uniform(1, 3))
    
    # Draw multiple spiral arms
    num_arms = 4
    for arm in range(num_arms):
        arm_offset = arm * (2 * math.pi / num_arms)
        # Alternate arm directions for a more dynamic galaxy
        direction = 1 if arm % 2 == 0 else -1
        draw_spiral_arm(
            start_radius=10 + arm * 5,
            num_stars=150,
            arm_offset=arm_offset,
            direction=direction
        )
    
    # Add outer scattered stars
    for _ in range(200):
        radius = random.uniform(150, 250)
        angle = random.uniform(0, 2 * math.pi)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        
        galaxy.penup()
        galaxy.goto(x, y)
        galaxy.pendown()
        galaxy.color(random.choice(colors))
        galaxy.dot(random.uniform(0.5, 1.5))

# Draw the galaxy
draw_galaxy()

# Add some dust/nebula effect using faint dots
for _ in range(100):
    radius = random.uniform(50, 200)
    angle = random.uniform(0, 2 * math.pi)
    x = radius * math.cos(angle) + random.uniform(-20, 20)
    y = radius * math.sin(angle) + random.uniform(-20, 20)
    
    galaxy.penup()
    galaxy.goto(x, y)
    galaxy.pendown()
    galaxy.color(random.choice(["#4A0080", "#1A0033", "#2D004D"]))
    galaxy.dot(random.uniform(3, 8))

# Update screen
screen.update()

# Keep window open
turtle.done()