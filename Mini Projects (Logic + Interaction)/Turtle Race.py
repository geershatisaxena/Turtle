import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("forestgreen")
screen.setup(width=800, height=600)

# Customize the race track
track_marker = turtle.Turtle()
track_marker.speed(0)
track_marker.color("white")
track_marker.penup()
track_marker.hideturtle()

# Draw finish line
finish_line = 350
track_marker.goto(finish_line, 250)
track_marker.pendown()
track_marker.goto(finish_line, -250)
track_marker.penup()

# Draw lane dividers
y_positions = [150, 50, -50, -150]
for y in y_positions:
    track_marker.goto(-350, y)
    track_marker.pendown()
    track_marker.forward(700)
    track_marker.penup()

# Create race turtles
colors = ["red", "blue", "orange", "purple"]
turtles = []
start_x = -350
start_y = 180
y_step = 100

for i in range(4):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(start_x, start_y - i * y_step)
    racer.pendown()
    turtles.append(racer)

# Add a title banner
title = turtle.Turtle()
title.hideturtle()
title.penup()
title.color("white")
title.goto(0, 260)
title.write("🐢 TURTLE RACE 🐢", align="center", font=("Arial", 24, "bold"))

# Instructions on screen
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.color("yellow")
info.goto(0, -280)
info.write("Click anywhere on the screen to start the race!", align="center", font=("Arial", 14, "normal"))

# Race state
race_active = False

def start_race(x, y):
    global race_active
    if not race_active:
        race_active = True
        info.clear()
        info.write("RACE ON! 🏁", align="center", font=("Arial", 14, "bold"))
        run_race()

def run_race():
    global race_active
    winner = None
    while race_active and winner is None:
        for racer in turtles:
            # Each turtle moves a random distance (2 to 20 pixels)
            move_distance = random.randint(2, 20)
            racer.forward(move_distance)
            
            # Check if this turtle crossed the finish line
            if racer.xcor() >= finish_line:
                winner = racer
                break
        time.sleep(0.03)  # Small delay to make race visible
    
    if winner:
        winner_color = winner.pencolor() if hasattr(winner, 'pencolor') else winner.color()[0]
        declare_winner(winner_color)

def declare_winner(color):
    winner_turtle = turtle.Turtle()
    winner_turtle.hideturtle()
    winner_turtle.penup()
    winner_turtle.color("gold")
    winner_turtle.goto(0, 0)
    winner_turtle.write(f"🏆 WINNER: {color.upper()} TURTLE! 🏆", 
                        align="center", font=("Arial", 20, "bold"))
    
    # Option to restart game
    restart = turtle.Turtle()
    restart.hideturtle()
    restart.penup()
    restart.color("white")
    restart.goto(0, -50)
    restart.write("Press 'r' to restart", align="center", font=("Arial", 14, "normal"))
    screen.onkey(restart_game, "r")

def restart_game():
    # Clear all turtles and text
    for racer in turtles:
        racer.clear()
        racer.hideturtle()
    # Reset screen
    screen.clearscreen()
    # Re-initialize game
    initialize_game()

def initialize_game():
    global race_active, turtles
    race_active = False
    screen.bgcolor("forestgreen")
    screen.setup(width=800, height=600)
    screen.title("Turtle Race Game")
    
    # Recreate track and turtles
    track_marker = turtle.Turtle()
    track_marker.speed(0)
    track_marker.color("white")
    track_marker.penup()
    track_marker.hideturtle()
    track_marker.goto(finish_line, 250)
    track_marker.pendown()
    track_marker.goto(finish_line, -250)
    track_marker.penup()
    
    y_positions = [150, 50, -50, -150]
    for y in y_positions:
        track_marker.goto(-350, y)
        track_marker.pendown()
        track_marker.forward(700)
        track_marker.penup()
    
    colors = ["red", "blue", "orange", "purple"]
    turtles = []
    start_x = -350
    start_y = 180
    for i in range(4):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(colors[i])
        racer.penup()
        racer.goto(start_x, start_y - i * 100)
        racer.pendown()
        turtles.append(racer)
    
    title = turtle.Turtle()
    title.hideturtle()
    title.penup()
    title.color("white")
    title.goto(0, 260)
    title.write("🐢 TURTLE RACE 🐢", align="center", font=("Arial", 24, "bold"))
    
    info = turtle.Turtle()
    info.hideturtle()
    info.penup()
    info.color("yellow")
    info.goto(0, -280)
    info.write("Click anywhere on the screen to start the race!", align="center", font=("Arial", 14, "normal"))
    
    screen.onclick(start_race)
    screen.listen()

# Initial game setup
initialize_game()

# Keep the window open
screen.mainloop()