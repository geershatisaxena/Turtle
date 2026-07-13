import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Water Ripple Animation")
screen.tracer(0)
screen.setup(800, 800)

# Create water background
water = turtle.Turtle()
water.speed(0)
water.penup()
water.goto(-400, -400)
water.pendown()
water.color("medium blue")
water.begin_fill()
water.goto(400, -400)
water.goto(400, 400)
water.goto(-400, 400)
water.goto(-400, -400)
water.end_fill()
water.hideturtle()

# Lists to hold ripple data
ripples = []

# Function to create a new ripple
def create_ripple(x, y):
    # Create a new turtle for the ripple
    ripple = turtle.Turtle()
    ripple.speed(0)
    ripple.penup()
    ripple.hideturtle()
    ripple.goto(x, y)
    
    # Randomize ripple properties
    max_radius = random.randint(40, 120)
    speed = random.uniform(2, 4)
    colors = ["light blue", "cyan", "white", "light cyan", "sky blue"]
    color = random.choice(colors)
    
    # Store ripple data
    ripple_data = {
        "turtle": ripple,
        "x": x,
        "y": y,
        "radius": 5,  # Start small
        "max_radius": max_radius,
        "speed": speed,
        "color": color,
        "active": True
    }
    ripples.append(ripple_data)

# Function to draw all ripples
def draw_ripples():
    for ripple_data in ripples:
        if not ripple_data["active"]:
            continue
            
        # Clear previous drawing
        ripple_data["turtle"].clear()
        
        # Update radius
        ripple_data["radius"] += ripple_data["speed"]
        
        # Check if ripple has reached max radius
        if ripple_data["radius"] >= ripple_data["max_radius"]:
            ripple_data["active"] = False
            ripple_data["turtle"].hideturtle()
            continue
        
        # Calculate opacity (fade out as it grows)
        life_ratio = ripple_data["radius"] / ripple_data["max_radius"]
        opacity = max(0, min(1, 1.0 - life_ratio))  # Clamp between 0 and 1
        
        # Draw the ripple ring
        ripple = ripple_data["turtle"]
        ripple.penup()
        
        # Set color with brightness based on opacity
        if ripple_data["color"] == "light blue":
            r = min(1, 0.678 * opacity + 0.1)
            g = min(1, 0.847 * opacity + 0.1)
            b = min(1, 0.902 * opacity + 0.1)
        elif ripple_data["color"] == "cyan":
            r = 0.0
            g = min(1, 0.8 * opacity + 0.1)
            b = min(1, 0.8 * opacity + 0.1)
        elif ripple_data["color"] == "white":
            r = min(1, opacity + 0.1)
            g = min(1, opacity + 0.1)
            b = min(1, opacity + 0.1)
        elif ripple_data["color"] == "light cyan":
            r = min(1, 0.878 * opacity + 0.1)
            g = min(1, 1.0 * opacity + 0.1)
            b = min(1, 1.0 * opacity + 0.1)
        else:  # sky blue
            r = min(1, 0.529 * opacity + 0.1)
            g = min(1, 0.808 * opacity + 0.1)
            b = min(1, 0.922 * opacity + 0.1)
        
        ripple.color((r, g, b))
        
        # Draw the ring
        ripple.penup()
        ripple.goto(ripple_data["x"], ripple_data["y"] - ripple_data["radius"])
        ripple.pendown()
        ripple.pensize(2)
        ripple.circle(ripple_data["radius"])
        ripple.penup()
        
        # Draw inner glow for small ripples
        if ripple_data["radius"] < 20 and opacity > 0.5:
            ripple.goto(ripple_data["x"], ripple_data["y"])
            ripple.pendown()
            ripple.color((min(1, 0.3 * opacity), min(1, 0.5 * opacity), min(1, 0.8 * opacity)))
            ripple.dot(ripple_data["radius"] * 0.5)
            ripple.penup()

# Function to clean up dead ripples
def clean_ripples():
    global ripples
    ripples = [r for r in ripples if r["active"]]

# Function to create ripple on click
def create_ripple_click(x, y):
    if -350 <= x <= 350 and -350 <= y <= 350:
        # Create multiple ripples for splash effect
        for _ in range(3):
            offset_x = random.randint(-15, 15)
            offset_y = random.randint(-15, 15)
            create_ripple(x + offset_x, y + offset_y)
        
        # Update counter
        update_counter()

# Create initial ripples
def create_initial_ripples():
    for _ in range(5):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        create_ripple(x, y)
        
        # Make some ripples larger
        if random.random() > 0.5:
            ripples[-1]["max_radius"] = random.randint(80, 150)
            ripples[-1]["speed"] = random.uniform(1.5, 3)

# Function to create ripple burst
def create_ripple_burst():
    for _ in range(12):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        create_ripple(x, y)
        ripples[-1]["max_radius"] = random.randint(30, 100)
        ripples[-1]["speed"] = random.uniform(2, 5)
    update_counter()

# Counter display
counter = turtle.Turtle()
counter.speed(0)
counter.penup()
counter.hideturtle()
counter.color("white")
counter.goto(-350, 350)

def update_counter():
    counter.clear()
    active = len([r for r in ripples if r["active"]])
    counter.write(f"Active Ripples: {active}", align="left", font=("Arial", 12, "normal"))

# Title
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.goto(0, 370)
title.color("white")
title.write("🌊 Water Ripple Effect", align="center", font=("Arial", 20, "bold"))

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -370)
instructions.color("light gray")
instructions.write("Click anywhere to create ripples • SPACE for burst • C to clear", 
                  align="center", font=("Arial", 12, "normal"))

# Function to clear all ripples
def clear_ripples():
    global ripples
    for ripple in ripples:
        ripple["turtle"].clear()
        ripple["turtle"].hideturtle()
    ripples.clear()
    update_counter()

# Key bindings
screen.onkey(create_ripple_burst, "space")
screen.onkey(clear_ripples, "c")
screen.listen()

# Click handler
screen.onclick(create_ripple_click)

# Create some initial ripples
create_initial_ripples()
update_counter()

# Animation loop
def animate():
    # Draw all ripples
    draw_ripples()
    
    # Clean up dead ripples
    clean_ripples()
    
    # Randomly create new ripples
    if random.random() < 0.02:  # 2% chance each frame
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        create_ripple(x, y)
        # Make some random ripples interesting
        if random.random() > 0.7:
            ripples[-1]["max_radius"] = random.randint(80, 150)
            ripples[-1]["speed"] = random.uniform(1.5, 3)
    
    screen.update()
    screen.ontimer(animate, 30)  # ~33 FPS

# Start animation
animate()

# Keep window open
screen.mainloop()