import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Solar System Simulation")
screen.bgcolor("black")
screen.setup(width=1200, height=900)
screen.tracer(0)

# Create the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3, 3)
sun.penup()

# Planet data: name, color, distance from sun, size, speed, orbit angle offset
planets_data = [
    {"name": "Mercury", "color": "gray", "distance": 80, "size": 0.6, "speed": 4.8, "angle": 0},
    {"name": "Venus", "color": "orange", "distance": 110, "size": 0.8, "speed": 3.5, "angle": 45},
    {"name": "Earth", "color": "blue", "distance": 150, "size": 0.9, "speed": 2.9, "angle": 90},
    {"name": "Mars", "color": "red", "distance": 190, "size": 0.7, "speed": 2.4, "angle": 135},
    {"name": "Jupiter", "color": "brown", "distance": 260, "size": 1.5, "speed": 1.3, "angle": 180},
    {"name": "Saturn", "color": "goldenrod", "distance": 320, "size": 1.3, "speed": 1.0, "angle": 225},
    {"name": "Uranus", "color": "lightblue", "distance": 380, "size": 1.1, "speed": 0.7, "angle": 270},
    {"name": "Neptune", "color": "darkblue", "distance": 430, "size": 1.1, "speed": 0.5, "angle": 315}
]

# Create planet turtles
planets = []
for data in planets_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(data["color"])
    planet.shapesize(data["size"], data["size"])
    planet.penup()
    planets.append(planet)

# Create orbit paths
orbit_turtles = []
for data in planets_data:
    orbit = turtle.Turtle()
    orbit.speed(0)
    orbit.color("gray")
    orbit.penup()
    orbit.hideturtle()
    orbit_turtles.append(orbit)

# Create moon for Earth
moon = turtle.Turtle()
moon.shape("circle")
moon.color("lightgray")
moon.shapesize(0.3, 0.3)
moon.penup()

# Create Saturn's ring
saturn_ring = turtle.Turtle()
saturn_ring.speed(0)
saturn_ring.color("gold")
saturn_ring.penup()
saturn_ring.hideturtle()

# Text display for planet info
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("white")
info_display.penup()
info_display.hideturtle()

# Star field
stars = []
for _ in range(200):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.shapesize(random.uniform(0.1, 0.3))
    star.penup()
    star.goto(random.randint(-580, 580), random.randint(-420, 420))
    stars.append(star)

def draw_orbits():
    """Draw circular orbits for all planets"""
    for i, data in enumerate(planets_data):
        orbit_turtles[i].clear()
        orbit_turtles[i].penup()
        orbit_turtles[i].goto(0, -data["distance"])
        orbit_turtles[i].pendown()
        orbit_turtles[i].circle(data["distance"])
        orbit_turtles[i].penup()

def draw_saturn_ring(x, y, angle, size):
    """Draw Saturn's ring"""
    saturn_ring.clear()
    saturn_ring.penup()
    saturn_ring.goto(x, y)
    saturn_ring.setheading(angle)
    saturn_ring.pendown()
    saturn_ring.color("gold")
    saturn_ring.pensize(3)
    saturn_ring.left(90)
    saturn_ring.circle(size * 15, 180)
    saturn_ring.right(180)
    saturn_ring.circle(size * 15, 180)
    saturn_ring.penup()

def update_info(planet_name, distance, speed):
    """Update information display"""
    info_display.clear()
    info_display.goto(-550, 400)
    info_display.write(f"🌞 SOLAR SYSTEM SIMULATION 🌍", font=("Arial", 14, "bold"))
    info_display.goto(-550, 370)
    info_display.write(f"Planet: {planet_name}", font=("Arial", 12, "normal"))
    info_display.goto(-550, 345)
    info_display.write(f"Distance from Sun: {distance} units", font=("Arial", 10, "normal"))
    info_display.goto(-550, 320)
    info_display.write(f"Orbital Speed: {speed:.1f}°/sec", font=("Arial", 10, "normal"))
    
    # Legend
    info_display.goto(-550, 280)
    info_display.write("LEGEND:", font=("Arial", 10, "bold"))
    info_display.goto(-550, 260)
    info_display.write("🟡 Sun (Center)", font=("Arial", 9, "normal"))
    info_display.goto(-550, 240)
    info_display.write("🔵 Planets (Orbiting)", font=("Arial", 9, "normal"))
    info_display.goto(-550, 220)
    info_display.write("⚪ Moon (Earth's moon)", font=("Arial", 9, "normal"))
    info_display.goto(-550, 200)
    info_display.write("🪐 Saturn's Rings", font=("Arial", 9, "normal"))

def draw_title():
    """Draw title on screen"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("yellow")
    title.penup()
    title.hideturtle()
    title.goto(0, 420)
    title.write("SOLAR SYSTEM SIMULATION", align="center", font=("Arial", 20, "bold"))
    title.goto(0, 390)
    title.color("white")
    title.write("Press SPACE to pause | R to reset | ESC to exit", align="center", font=("Arial", 10, "normal"))

# Animation variables
angle_increments = [data["speed"] for data in planets_data]
angles = [data["angle"] for data in planets_data]
running = True
moon_angle = 0
saturn_index = 5  # Saturn's index in planets list

def reset_simulation():
    """Reset all planet angles"""
    global angles, moon_angle
    for i in range(len(angles)):
        angles[i] = planets_data[i]["angle"]
    moon_angle = 0
    update_info("Click on a planet!", 0, 0)

def toggle_pause():
    """Pause or resume the simulation"""
    global running
    running = not running
    pause_text = turtle.Turtle()
    pause_text.speed(0)
    pause_text.color("red")
    pause_text.penup()
    pause_text.hideturtle()
    if not running:
        pause_text.goto(0, 0)
        pause_text.write("PAUSED", align="center", font=("Arial", 30, "bold"))
        screen.update()
        turtle.time.sleep(0.5)
        pause_text.clear()
    else:
        pause_text.clear()

def on_planet_click(x, y):
    """Show planet info when clicked"""
    # Find which planet was clicked (simple distance check)
    for i, planet in enumerate(planets):
        dist = math.sqrt((planet.xcor() - x)**2 + (planet.ycor() - y)**2)
        if dist < 20:
            update_info(planets_data[i]["name"], 
                       planets_data[i]["distance"], 
                       planets_data[i]["speed"])
            break

# Draw star field animation (twinkling)
def twinkle_stars():
    """Make stars twinkle randomly"""
    for star in stars:
        if random.random() < 0.02:
            new_size = random.uniform(0.1, 0.5)
            star.shapesize(new_size, new_size)

def animate():
    """Main animation loop"""
    global angles, moon_angle, running
    
    # Draw orbits first
    draw_orbits()
    
    frame = 0
    
    while True:
        if running:
            # Update angles for each planet
            for i in range(len(planets)):
                angles[i] += angle_increments[i]
                if angles[i] >= 360:
                    angles[i] -= 360
                
                # Calculate planet position
                radian = math.radians(angles[i])
                x = planets_data[i]["distance"] * math.cos(radian)
                y = planets_data[i]["distance"] * math.sin(radian)
                planets[i].goto(x, y)
                
                # Draw Saturn's ring
                if i == saturn_index:
                    draw_saturn_ring(x, y, angles[i] - 90, planets_data[i]["size"])
            
            # Update moon position (orbits Earth)
            moon_angle += 12  # Moon orbits faster
            if moon_angle >= 360:
                moon_angle -= 360
            
            # Earth is at index 2
            earth_x = planets[2].xcor()
            earth_y = planets[2].ycor()
            moon_radian = math.radians(moon_angle)
            moon_x = earth_x + 35 * math.cos(moon_radian)
            moon_y = earth_y + 35 * math.sin(moon_radian)
            moon.goto(moon_x, moon_y)
            
            # Twinkle stars
            twinkle_stars()
            
            # Update frame counter for info cycling
            frame += 1
            if frame % 300 == 0:
                # Cycle through planet info automatically
                planet_idx = (frame // 300) % len(planets_data)
                update_info(planets_data[planet_idx]["name"],
                           planets_data[planet_idx]["distance"],
                           planets_data[planet_idx]["speed"])
        
        screen.update()
        turtle.time.sleep(0.02)

# Keyboard bindings
screen.listen()
screen.onkey(toggle_pause, "space")
screen.onkey(reset_simulation, "r")
screen.onkey(lambda: screen.bye(), "Escape")
screen.onclick(on_planet_click)

# Draw initial elements
draw_title()
draw_orbits()
update_info("Click on any planet!", 0, 0)

print("=" * 60)
print("           SOLAR SYSTEM SIMULATION")
print("=" * 60)
print()
print("An accurate simulation of planets orbiting the Sun!")
print()
print("FEATURES:")
print("  • 8 planets with relative speeds and distances")
print("  • Earth's moon orbiting around it")
print("  • Saturn's rings visual effect")
print("  • Twinkling star field")
print("  • Planet info on click")
print()
print("CONTROLS:")
print("  SPACE - Pause/Resume simulation")
print("  Click on a planet - Show planet information")
print("  R - Reset planet positions")
print("  ESC - Exit program")
print()
print("Planet order (from Sun):")
print("  Mercury → Venus → Earth → Mars → Jupiter → Saturn → Uranus → Neptune")
print()

# Run the animation
try:
    animate()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()