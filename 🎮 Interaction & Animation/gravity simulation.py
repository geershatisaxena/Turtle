import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Gravity Simulation - Falling and Bouncing Ball")
screen.bgcolor("lightblue")
screen.tracer(0)  # Turn off automatic animation for smoother updates

# Create the ball (a turtle circle)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 250)  # Start position (x=0, y=250)
ball.dy = 0  # Initial vertical velocity (pixels per frame)

# Create ground
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-400, -200)
ground.pendown()
ground.goto(400, -200)
ground.pensize(3)
ground.color("green")

# Physics constants
GRAVITY = -0.5    # Acceleration due to gravity (pixels per frame^2)
BOUNCE_DAMPING = 0.85  # Energy loss on each bounce (1.0 = perfect bounce)
GROUND_Y = -200   # Y-coordinate of ground level
BALL_RADIUS = 15  # Approximate radius of the ball (for collision detection)

def update_ball():
    """Update ball position and velocity each frame."""
    global GRAVITY, BOUNCE_DAMPING, GROUND_Y, BALL_RADIUS
    
    # Apply gravity to vertical velocity
    ball.dy += GRAVITY
    
    # Update position
    x, y = ball.position()
    y += ball.dy
    ball.sety(y)
    
    # Check collision with ground (ball's bottom hits ground)
    if ball.ycor() - BALL_RADIUS <= GROUND_Y:
        # Place ball exactly on ground
        ball.sety(GROUND_Y + BALL_RADIUS)
        
        # Reverse velocity and reduce by damping factor
        ball.dy = -ball.dy * BOUNCE_DAMPING
        
        # Stop very small bounces (prevents endless micro-bouncing)
        if abs(ball.dy) < 1:
            ball.dy = 0
    
    # Optional: Stop ball completely when nearly resting on ground
    if ball.ycor() - BALL_RADIUS <= GROUND_Y and abs(ball.dy) < 1:
        ball.dy = 0
        ball.sety(GROUND_Y + BALL_RADIUS)

def animate():
    """Animation loop."""
    update_ball()
    screen.update()          # Refresh screen
    screen.ontimer(animate, 16)  # ~60 FPS (16ms per frame)

# Start simulation
print("Gravity Simulation Started...")
print("Watch the ball fall and bounce!")
animate()

# Keep window open until clicked
screen.exitonclick()