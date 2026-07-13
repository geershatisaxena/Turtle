import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Traffic Light Simulation")
screen.tracer(0)
screen.setup(600, 800)

# Constants
LIGHT_RADIUS = 40
LIGHT_SPACING = 80
POLE_WIDTH = 15
POLE_HEIGHT = 300

# Create the traffic light pole
pole = turtle.Turtle()
pole.speed(0)
pole.penup()
pole.goto(-POLE_WIDTH/2, -200)
pole.pendown()
pole.color("dark gray")
pole.begin_fill()
for _ in range(2):
    pole.forward(POLE_WIDTH)
    pole.left(90)
    pole.forward(POLE_HEIGHT)
    pole.left(90)
pole.end_fill()
pole.hideturtle()

# Create the traffic light housing
housing = turtle.Turtle()
housing.speed(0)
housing.penup()
housing.goto(-50, -50)
housing.pendown()
housing.color("black")
housing.begin_fill()
for _ in range(2):
    housing.forward(100)
    housing.left(90)
    housing.forward(250)
    housing.left(90)
housing.end_fill()
housing.hideturtle()

# Create the lights
red_light = turtle.Turtle()
red_light.speed(0)
red_light.shape("circle")
red_light.shapesize(LIGHT_RADIUS/10)
red_light.penup()
red_light.goto(0, 50)

yellow_light = turtle.Turtle()
yellow_light.speed(0)
yellow_light.shape("circle")
yellow_light.shapesize(LIGHT_RADIUS/10)
yellow_light.penup()
yellow_light.goto(0, -30)

green_light = turtle.Turtle()
green_light.speed(0)
green_light.shape("circle")
green_light.shapesize(LIGHT_RADIUS/10)
green_light.penup()
green_light.goto(0, -110)

# Create light labels
labels = turtle.Turtle()
labels.speed(0)
labels.penup()
labels.hideturtle()

# Labels for each light
labels.goto(70, 45)
labels.color("white")
labels.write("RED", font=("Arial", 10, "bold"))
labels.goto(70, -35)
labels.write("YELLOW", font=("Arial", 10, "bold"))
labels.goto(70, -115)
labels.write("GREEN", font=("Arial", 10, "bold"))

# State variables
current_state = "red"  # red, yellow, green
timer = 0
state_duration = 0
is_paused = False
is_manual = False

# Create status display
status = turtle.Turtle()
status.speed(0)
status.penup()
status.hideturtle()
status.goto(0, -320)

# Create timer display
timer_display = turtle.Turtle()
timer_display.speed(0)
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(0, -280)

# Create control panel
control_panel = turtle.Turtle()
control_panel.speed(0)
control_panel.penup()
control_panel.hideturtle()

def draw_control_panel():
    control_panel.clear()
    control_panel.goto(-250, -380)
    control_panel.color("gray")
    control_panel.pendown()
    control_panel.begin_fill()
    for _ in range(2):
        control_panel.forward(500)
        control_panel.left(90)
        control_panel.forward(60)
        control_panel.left(90)
    control_panel.end_fill()
    control_panel.penup()
    
    # Control buttons text
    control_panel.goto(0, -395)
    control_panel.color("white")
    control_panel.write("CONTROLS:", align="center", font=("Arial", 12, "bold"))
    control_panel.goto(0, -415)
    control_panel.write("Click: Next State  |  Space: Pause  |  R: Reset  |  M: Manual Mode", 
                       align="center", font=("Arial", 10, "normal"))

draw_control_panel()

# Function to update lights
def update_lights(state):
    # Clear all lights first (set to dark)
    red_light.color("dark red")
    yellow_light.color("dark goldenrod")
    green_light.color("dark green")
    
    # Turn on the appropriate light
    if state == "red":
        red_light.color("red")
        # Glow effect
        red_light.shapesize(LIGHT_RADIUS/9)
    elif state == "yellow":
        yellow_light.color("yellow")
        yellow_light.shapesize(LIGHT_RADIUS/9)
    elif state == "green":
        green_light.color("lime green")
        green_light.shapesize(LIGHT_RADIUS/9)
    
    # Reset sizes for off lights
    if state != "red":
        red_light.shapesize(LIGHT_RADIUS/10)
    if state != "yellow":
        yellow_light.shapesize(LIGHT_RADIUS/10)
    if state != "green":
        green_light.shapesize(LIGHT_RADIUS/10)

# Function to get next state
def get_next_state(current):
    if current == "red":
        return "yellow"
    elif current == "yellow":
        return "green"
    elif current == "green":
        return "yellow"  # Green to yellow before red
    
# Function to get state duration
def get_state_duration(state):
    if state == "red":
        return 5  # seconds
    elif state == "yellow":
        return 2
    elif state == "green":
        return 4

# Function to change state
def change_state(new_state=None):
    global current_state, timer, state_duration
    
    if new_state is None:
        # Auto cycle
        next_state = get_next_state(current_state)
        current_state = next_state
    else:
        current_state = new_state
    
    state_duration = get_state_duration(current_state)
    timer = state_duration
    update_lights(current_state)

# Function to update status display
def update_status():
    status.clear()
    timer_display.clear()
    
    # Show current state with color
    status.goto(0, -320)
    state_colors = {
        "red": "red",
        "yellow": "yellow",
        "green": "lime green"
    }
    status.color(state_colors[current_state])
    status.write(f"State: {current_state.upper()}", align="center", font=("Arial", 16, "bold"))
    
    # Show timer
    timer_display.goto(0, -280)
    timer_display.color("white")
    timer_display.write(f"Time remaining: {int(timer)}s", align="center", font=("Arial", 14, "normal"))
    
    # Show mode
    mode_text = "MANUAL MODE" if is_manual else "AUTO MODE"
    mode_color = "yellow" if is_manual else "white"
    status.goto(0, -350)
    status.color(mode_color)
    status.write(mode_text, align="center", font=("Arial", 12, "bold"))

# Create road
road = turtle.Turtle()
road.speed(0)
road.penup()
road.goto(-400, -200)
road.pendown()
road.color("dark gray")
road.begin_fill()
road.goto(400, -200)
road.goto(400, -250)
road.goto(-400, -250)
road.goto(-400, -200)
road.end_fill()
road.hideturtle()

# Road lines
road_lines = turtle.Turtle()
road_lines.speed(0)
road_lines.penup()
road_lines.color("white")
road_lines.pensize(2)
road_lines.hideturtle()

for x in range(-380, 380, 30):
    road_lines.goto(x, -225)
    road_lines.pendown()
    road_lines.forward(15)
    road_lines.penup()

# Function to handle manual state change
def next_state_click(x, y):
    global is_manual, current_state, timer, state_duration
    
    # Check if click is on the traffic light area
    if -50 < x < 50 and -50 < y < 200:
        if is_manual:
            # Manual mode: cycle through states
            if current_state == "red":
                change_state("yellow")
            elif current_state == "yellow":
                change_state("green")
            elif current_state == "green":
                change_state("red")
            update_status()

def toggle_pause():
    global is_paused
    is_paused = not is_paused
    pause_text = turtle.Turtle()
    pause_text.speed(0)
    pause_text.penup()
    pause_text.hideturtle()
    
    if is_paused:
        pause_text.goto(0, 200)
        pause_text.color("white")
        pause_text.write("⏸ PAUSED", align="center", font=("Arial", 20, "bold"))
    else:
        pause_text.clear()

def reset_traffic():
    global current_state, timer, state_duration
    current_state = "red"
    state_duration = get_state_duration("red")
    timer = state_duration
    update_lights("red")
    update_status()
    
    # Clear pause text if any
    for item in screen.turtles():
        if item.isvisible() and item.ycor() == 200:
            item.clear()
            item.hideturtle()

def toggle_manual():
    global is_manual, current_state, timer, state_duration
    is_manual = not is_manual
    
    if is_manual:
        # Set to red when entering manual mode
        current_state = "red"
        state_duration = get_state_duration("red")
        timer = state_duration
        update_lights("red")
    else:
        # Resume auto mode
        pass
    
    update_status()

# Initialize traffic light
change_state("red")
update_status()

# Add title
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.goto(0, 350)
title.color("white")
title.write("🚦 TRAFFIC LIGHT SIMULATION", align="center", font=("Arial", 20, "bold"))

# Add subtitle
subtitle = turtle.Turtle()
subtitle.speed(0)
subtitle.penup()
subtitle.hideturtle()
subtitle.goto(0, 320)
subtitle.color("light gray")
subtitle.write("Press SPACE to pause • Click light to advance (Manual mode)", 
              align="center", font=("Arial", 10, "normal"))

# Key bindings
screen.onkey(toggle_pause, "space")
screen.onkey(reset_traffic, "r")
screen.onkey(toggle_manual, "m")
screen.listen()

# Click handler
screen.onclick(next_state_click)

# Main animation loop
def animate():
    global timer, current_state
    
    if not is_paused:
        timer -= 0.1
        
        # Update timer display
        timer_display.clear()
        timer_display.goto(0, -280)
        timer_display.color("white")
        timer_display.write(f"Time remaining: {int(timer)}s", align="center", font=("Arial", 14, "normal"))
        
        # Check if it's time to change state
        if timer <= 0:
            if not is_manual:
                change_state()  # Auto cycle
            else:
                # In manual mode, hold at current state
                timer = 0
            update_status()
    
    screen.update()
    screen.ontimer(animate, 100)  # Update every 100ms

# Click to exit
screen.onclick(lambda x, y: screen.bye())

# Start animation
animate()

# Keep window open
screen.mainloop()