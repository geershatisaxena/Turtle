import turtle
import math
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Radar Scanner Simulation")
screen.tracer(0)
screen.setup(800, 800)

# Create radar screen border
border = turtle.Turtle()
border.speed(0)
border.color("green")
border.penup()
border.goto(0, -300)
border.pendown()
border.circle(300)
border.penup()

# Draw crosshairs
crosshair = turtle.Turtle()
crosshair.speed(0)
crosshair.color("dark green")
crosshair.penup()

# Horizontal line
crosshair.goto(-300, 0)
crosshair.pendown()
crosshair.goto(300, 0)
crosshair.penup()

# Vertical line
crosshair.goto(0, -300)
crosshair.pendown()
crosshair.goto(0, 300)
crosshair.penup()

# Draw concentric circles (range rings)
for radius in range(50, 301, 50):
    ring = turtle.Turtle()
    ring.speed(0)
    ring.color("dark green")
    ring.penup()
    ring.goto(0, -radius)
    ring.pendown()
    ring.circle(radius)
    ring.hideturtle()

# Range labels
labels = turtle.Turtle()
labels.speed(0)
labels.color("green")
labels.penup()
labels.hideturtle()

for i, radius in enumerate(range(50, 301, 50)):
    labels.goto(radius, -10)
    labels.write(f"{i+1}", align="center", font=("Arial", 8, "normal"))

# Compass labels
compass = turtle.Turtle()
compass.speed(0)
compass.color("green")
compass.penup()
compass.hideturtle()

compass.goto(0, 280)
compass.write("N", align="center", font=("Arial", 12, "bold"))
compass.goto(0, -290)
compass.write("S", align="center", font=("Arial", 12, "bold"))
compass.goto(290, 0)
compass.write("E", align="center", font=("Arial", 12, "bold"))
compass.goto(-290, 0)
compass.write("W", align="center", font=("Arial", 12, "bold"))

# Radar blips (targets)
blips = []
for _ in range(random.randint(5, 8)):
    blip = turtle.Turtle()
    blip.speed(0)
    blip.shape("circle")
    blip.color("lime green")
    blip.shapesize(0.5)
    blip.penup()
    
    # Random position within radar range
    angle = random.uniform(0, 360)
    distance = random.uniform(20, 270)
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    blip.goto(x, y)
    
    # Store blip data
    blip_data = {
        "turtle": blip,
        "angle": angle,
        "distance": distance,
        "x": x,
        "y": y,
        "pulse": 0,
        "pulse_direction": 1
    }
    blips.append(blip_data)

# Create rotating scanner arm
scanner = turtle.Turtle()
scanner.speed(0)
scanner.color("lime green")
scanner.penup()
scanner.goto(0, 0)

# Create scanner glow effect
glow = turtle.Turtle()
glow.speed(0)
glow.color("lime green")
glow.penup()
glow.hideturtle()

# Create sweep trail
trail = turtle.Turtle()
trail.speed(0)
trail.color("lime green")
trail.penup()
trail.pensize(2)

# Scanner angle
scanner_angle = 0
rotation_speed = 1.5

# Radar stats display
stats = turtle.Turtle()
stats.speed(0)
stats.color("green")
stats.penup()
stats.hideturtle()
stats.goto(-350, 350)

# Title
title = turtle.Turtle()
title.speed(0)
title.color("green")
title.penup()
title.hideturtle()
title.goto(0, 350)
title.write("RADAR SCANNER", align="center", font=("Arial", 18, "bold"))

# Function to create fade effect on blips
def update_blips():
    for blip in blips:
        # Pulsing effect
        blip["pulse"] += 0.05 * blip["pulse_direction"]
        if blip["pulse"] > 1:
            blip["pulse_direction"] = -1
        elif blip["pulse"] < 0:
            blip["pulse_direction"] = 1
        
        # Change size and opacity based on pulse
        size = 0.3 + blip["pulse"] * 0.3
        blip["turtle"].shapesize(size)
        
        # Make blips visible only when scanner passes over them
        blip_angle = math.degrees(math.atan2(blip["y"], blip["x"]))
        if blip_angle < 0:
            blip_angle += 360
            
        # Check if scanner is near the blip (within 15 degrees)
        angle_diff = abs(blip_angle - scanner_angle)
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
            
        if angle_diff < 15:
            blip["turtle"].color("lime green")
            # Make blip brighter when scanned
            blip["turtle"].shapesize(size * 1.5)
        else:
            # Blip fades when not scanned
            blip["turtle"].color("dark green")
            blip["turtle"].shapesize(size * 0.7)

# Function to create sweep effect
def draw_sweep():
    # Draw the scanner arm
    scanner.clear()
    scanner.goto(0, 0)
    scanner.pendown()
    scanner.goto(280 * math.cos(math.radians(scanner_angle)), 
                 280 * math.sin(math.radians(scanner_angle)))
    scanner.penup()
    
    # Draw glow behind scanner
    glow.clear()
    glow.goto(0, 0)
    glow.pendown()
    glow.begin_fill()
    
    # Create a wedge shape for the sweep
    glow.goto(280 * math.cos(math.radians(scanner_angle - 15)), 
              280 * math.sin(math.radians(scanner_angle - 15)))
    glow.goto(280 * math.cos(math.radians(scanner_angle + 15)), 
              280 * math.sin(math.radians(scanner_angle + 15)))
    glow.goto(0, 0)
    glow.end_fill()
    glow.penup()

# Function to detect and create new blips (simulate radar detection)
def simulate_detection():
    # Randomly create new blips
    if random.random() < 0.02 and len(blips) < 15:
        blip = turtle.Turtle()
        blip.speed(0)
        blip.shape("circle")
        blip.color("lime green")
        blip.shapesize(0.5)
        blip.penup()
        
        angle = random.uniform(0, 360)
        distance = random.uniform(30, 270)
        x = distance * math.cos(math.radians(angle))
        y = distance * math.sin(math.radians(angle))
        blip.goto(x, y)
        
        blip_data = {
            "turtle": blip,
            "angle": angle,
            "distance": distance,
            "x": x,
            "y": y,
            "pulse": 0,
            "pulse_direction": 1
        }
        blips.append(blip_data)

# Function to update stats
def update_stats():
    stats.clear()
    stats.goto(-350, 350)
    stats.write("RADAR STATS", align="left", font=("Arial", 12, "bold"))
    stats.goto(-350, 325)
    stats.write(f"Targets: {len(blips)}", align="left", font=("Arial", 10, "normal"))
    stats.goto(-350, 305)
    stats.write(f"Angle: {scanner_angle:.1f}°", align="left", font=("Arial", 10, "normal"))
    stats.goto(-350, 285)
    rotation_speed_display = 1.5 * 60  # Convert to RPM
    stats.write(f"Speed: {rotation_speed_display:.0f} RPM", align="left", font=("Arial", 10, "normal"))

# Function to create a noise/static effect
def create_static():
    static = turtle.Turtle()
    static.speed(0)
    static.penup()
    static.hideturtle()
    static.color("green")
    
    for _ in range(50):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        # Only place static points outside the center
        if math.sqrt(x**2 + y**2) > 10 and math.sqrt(x**2 + y**2) < 290:
            static.goto(x, y)
            static.dot(1)

# Draw some static noise
create_static()

# Main animation loop
def animate():
    global scanner_angle
    
    # Update scanner angle
    scanner_angle += rotation_speed
    if scanner_angle >= 360:
        scanner_angle -= 360
    
    # Draw sweep
    draw_sweep()
    
    # Update blips
    update_blips()
    
    # Simulate detections
    simulate_detection()
    
    # Update stats
    update_stats()
    
    screen.update()
    screen.ontimer(animate, 20)

# Radar text display
radar_text = turtle.Turtle()
radar_text.speed(0)
radar_text.color("green")
radar_text.penup()
radar_text.hideturtle()
radar_text.goto(0, -350)
radar_text.write("🔄 Scanning...", align="center", font=("Arial", 12, "normal"))

# Click to exit
screen.onclick(lambda x, y: screen.bye())

# Start animation
animate()

# Keep window open
screen.mainloop()