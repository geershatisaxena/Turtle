import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Catch the Moving Object - Star Catcher")
screen.bgcolor("darkblue")
screen.setup(width=800, height=700)
screen.tracer(0)

# Create the catcher (paddle)
catcher = turtle.Turtle()
catcher.shape("square")
catcher.color("lime")
catcher.shapesize(1, 4)
catcher.penup()
catcher.goto(0, -300)

# Create the falling object (star)
star = turtle.Turtle()
star.shape("circle")
star.color("gold")
star.shapesize(1.5, 1.5)
star.penup()
star.goto(0, 300)

# Create score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()

# Create lives display
lives_display = turtle.Turtle()
lives_display.speed(0)
lives_display.color("red")
lives_display.penup()
lives_display.hideturtle()

# Create game over display
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()

# Create instructions display
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("gray")
instructions.penup()
instructions.hideturtle()

# Game variables
score = 0
lives = 3
star_speed = 5
star_x = 0
game_active = True

# List to store multiple falling objects (power-ups and obstacles)
power_ups = []
obstacles = []

# Power-up settings
power_up_active = False
power_up_timer = 0

def move_left():
    """Move catcher left"""
    x = catcher.xcor()
    if x > -350:
        catcher.setx(x - 30)

def move_right():
    """Move catcher right"""
    x = catcher.xcor()
    if x < 350:
        catcher.setx(x + 30)

def update_score():
    """Update score display"""
    score_display.clear()
    score_display.goto(-380, 320)
    score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))
    
    lives_display.clear()
    lives_display.goto(250, 320)
    lives_display.write(f"Lives: {'❤️' * lives}", font=("Arial", 16, "bold"))

def create_power_up():
    """Create a power-up object"""
    if random.random() < 0.02 and len(power_ups) < 2:  # 2% chance each frame
        power = turtle.Turtle()
        power.shape("square")
        power.color("purple")
        power.shapesize(1, 1)
        power.penup()
        power.goto(random.randint(-350, 350), 300)
        power_ups.append(power)

def create_obstacle():
    """Create an obstacle object"""
    if random.random() < 0.015 and len(obstacles) < 3:  # 1.5% chance
        obstacle = turtle.Turtle()
        obstacle.shape("triangle")
        obstacle.color("red")
        obstacle.shapesize(1, 1)
        obstacle.penup()
        obstacle.goto(random.randint(-350, 350), 300)
        obstacles.append(obstacle)

def activate_power_up():
    """Activate power-up effect"""
    global power_up_active, power_up_timer, star_speed
    power_up_active = True
    power_up_timer = 300  # 5 seconds (300 frames at 60fps)
    star_speed = 8  # Speed up for more challenge
    catcher.color("gold")
    catcher.shapesize(1, 6)  # Widen catcher

def deactivate_power_up():
    """Deactivate power-up effect"""
    global power_up_active, star_speed
    power_up_active = False
    star_speed = 5
    catcher.color("lime")
    catcher.shapesize(1, 4)

def game_over():
    """End the game"""
    global game_active
    game_active = False
    
    game_over_display.goto(0, 0)
    game_over_display.write("GAME OVER!", align="center", font=("Arial", 36, "bold"))
    game_over_display.goto(0, -50)
    game_over_display.write(f"Final Score: {score}", align="center", font=("Arial", 24, "bold"))
    game_over_display.goto(0, -100)
    game_over_display.write("Press R to restart or ESC to exit", align="center", font=("Arial", 14, "normal"))

def reset_game():
    """Reset the game"""
    global score, lives, game_active, star_speed, power_up_active, star_x
    global power_ups, obstacles
    
    score = 0
    lives = 3
    game_active = True
    star_speed = 5
    power_up_active = False
    star_x = 0
    
    # Clear all objects
    for power in power_ups:
        power.hideturtle()
    for obstacle in obstacles:
        obstacle.hideturtle()
    power_ups.clear()
    obstacles.clear()
    
    # Reset positions
    star.goto(random.randint(-350, 350), 300)
    catcher.goto(0, -300)
    catcher.color("lime")
    catcher.shapesize(1, 4)
    
    # Clear displays
    game_over_display.clear()
    update_score()
    
    # Show instructions again
    show_instructions()

def show_instructions():
    """Show game instructions"""
    instructions.clear()
    instructions.goto(0, -350)
    instructions.write("Use LEFT/RIGHT arrows to move | Catch gold stars | Avoid red triangles | Purple squares = Power-up!",
                       align="center", font=("Arial", 10, "normal"))

def catch_star():
    """Handle catching the star"""
    global score, star_speed, star_x
    
    score += 10
    update_score()
    
    # Increase difficulty every 100 points
    if score % 100 == 0 and star_speed < 12:
        star_speed += 0.5
    
    # Respawn star at random x position
    star_x = random.randint(-350, 350)
    star.goto(star_x, 300)

def hit_obstacle():
    """Handle hitting an obstacle"""
    global lives, star_speed
    
    lives -= 1
    update_score()
    
    if lives <= 0:
        game_over()
    else:
        # Shake effect
        original_pos = catcher.xcor()
        for _ in range(5):
            catcher.setx(original_pos + 10)
            screen.update()
            time.sleep(0.02)
            catcher.setx(original_pos - 10)
            screen.update()
            time.sleep(0.02)
        catcher.setx(original_pos)
        catcher.color("lime")

def update_game():
    """Main game loop"""
    global star_x, game_active, power_up_active, power_up_timer
    
    if not game_active:
        return
    
    # Move star
    y = star.ycor()
    if y > -300:
        star.sety(y - star_speed)
    else:
        # Star missed - lose a life
        lives -= 1
        update_score()
        
        if lives <= 0:
            game_over()
            return
        
        # Respawn star
        star_x = random.randint(-350, 350)
        star.goto(star_x, 300)
    
    # Check collision with catcher (star)
    if abs(star.ycor() - catcher.ycor()) < 25 and abs(star.xcor() - catcher.xcor()) < 50:
        catch_star()
    
    # Update power-ups
    for power in power_ups[:]:
        power.sety(power.ycor() - 6)
        
        # Check collision with power-up
        if abs(power.ycor() - catcher.ycor()) < 20 and abs(power.xcor() - catcher.xcor()) < 50:
            activate_power_up()
            power.hideturtle()
            power_ups.remove(power)
        elif power.ycor() < -320:
            power.hideturtle()
            power_ups.remove(power)
    
    # Update obstacles
    for obstacle in obstacles[:]:
        obstacle.sety(obstacle.ycor() - 5)
        
        # Check collision with obstacle
        if abs(obstacle.ycor() - catcher.ycor()) < 20 and abs(obstacle.xcor() - catcher.xcor()) < 50:
            hit_obstacle()
            obstacle.hideturtle()
            obstacles.remove(obstacle)
        elif obstacle.ycor() < -320:
            obstacle.hideturtle()
            obstacles.remove(obstacle)
    
    # Power-up timer
    if power_up_active:
        power_up_timer -= 1
        if power_up_timer <= 0:
            deactivate_power_up()
    
    # Create new power-ups and obstacles
    create_power_up()
    create_obstacle()
    
    # Update screen
    screen.update()
    
    # Schedule next frame
    screen.ontimer(update_game, 16)  # ~60 FPS

# Draw background decorations
def draw_background():
    """Draw decorative elements"""
    bg = turtle.Turtle()
    bg.speed(0)
    bg.color("lightblue")
    bg.penup()
    bg.hideturtle()
    
    # Draw stars in background
    for _ in range(50):
        x = random.randint(-380, 380)
        y = random.randint(-300, 350)
        bg.goto(x, y)
        bg.dot(2, "white")
    
    # Draw ground
    bg.goto(-400, -280)
    bg.pendown()
    bg.color("darkgreen")
    bg.begin_fill()
    bg.goto(400, -280)
    bg.goto(400, -350)
    bg.goto(-400, -350)
    bg.goto(-400, -280)
    bg.end_fill()
    bg.penup()

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkey(lambda: reset_game() if not game_active else None, "r")
screen.onkey(lambda: screen.bye(), "Escape")

# Draw elements
draw_background()
update_score()
show_instructions()

print("=" * 50)
print("        CATCH THE MOVING OBJECT")
print("=" * 50)
print()
print("A fast-paced catching game with power-ups and obstacles!")
print()
print("GAMEPLAY:")
print("  • Catch gold stars to earn points")
print("  • Avoid red triangles (lose a life)")
print("  • Catch purple squares for power-ups")
print("  • Each missed star costs a life")
print("  • Game ends when lives reach 0")
print()
print("POWER-UPS:")
print("  • Widens the catcher")
print("  • Changes color to gold")
print("  • Lasts 5 seconds")
print("  • Increases star speed for extra challenge!")
print()
print("CONTROLS:")
print("  LEFT/RIGHT arrows - Move the catcher")
print("  R - Restart game (after game over)")
print("  ESC - Exit program")
print()
print("Get ready! Catching stars...")

# Start the game
star.goto(random.randint(-350, 350), 300)
update_game()

screen.mainloop()