import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Maze Drawing Generator")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.tracer(0)

# Maze settings
cell_size = 20  # Size of each cell in pixels
maze_width = 21  # Must be odd number for perfect maze
maze_height = 21  # Must be odd number for perfect maze

# Calculate screen boundaries
width_pixels = maze_width * cell_size
height_pixels = maze_height * cell_size
start_x = -width_pixels // 2
start_y = height_pixels // 2

# Create maze drawer
drawer = turtle.Turtle()
drawer.speed(0)
drawer.color("white")
drawer.pensize(2)
drawer.penup()
drawer.hideturtle()

# Create UI elements
ui_text = turtle.Turtle()
ui_text.speed(0)
ui_text.color("yellow")
ui_text.penup()
ui_text.hideturtle()

# Maze data structure (True = wall, False = path)
maze = [[True for _ in range(maze_width)] for _ in range(maze_height)]

def generate_maze(x, y):
    """Recursive backtracking maze generation"""
    # Mark current cell as path
    maze[y][x] = False
    
    # Create list of possible directions
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # Up, Down, Left, Right
    random.shuffle(directions)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # Check if within bounds and is a wall
        if 0 <= nx < maze_width and 0 <= ny < maze_height and maze[ny][nx]:
            # Remove the wall between current and next cell
            maze[y + dy//2][x + dx//2] = False
            # Recursively generate the next cell
            generate_maze(nx, ny)

def draw_maze():
    """Draw the maze using turtle graphics"""
    drawer.clear()
    
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x]:  # Draw wall
                draw_cell(x, y, "white")
            else:  # Draw path (optional: different color)
                draw_cell(x, y, "black", fill=True)
    
    # Draw start and end markers
    draw_start_end()
    
    screen.update()

def draw_cell(x, y, color, fill=False):
    """Draw a single cell of the maze"""
    screen_x = start_x + x * cell_size
    screen_y = start_y - y * cell_size
    
    drawer.goto(screen_x, screen_y)
    drawer.pendown()
    drawer.color(color)
    
    if fill:
        drawer.begin_fill()
        drawer.fillcolor("darkblue")
    
    for _ in range(4):
        drawer.forward(cell_size)
        drawer.right(90)
    
    if fill:
        drawer.end_fill()
    
    drawer.penup()

def draw_start_end():
    """Mark the start (green) and end (red) positions"""
    # Start at top-left (entrance)
    start_x_pos = start_x + cell_size // 2
    start_y_pos = start_y - cell_size // 2
    
    # End at bottom-right (exit)
    end_x_pos = start_x + (maze_width - 1) * cell_size + cell_size // 2
    end_y_pos = start_y - (maze_height - 1) * cell_size - cell_size // 2
    
    # Draw start marker
    drawer.goto(start_x_pos, start_y_pos)
    drawer.color("lime")
    drawer.dot(cell_size // 2)
    
    # Draw end marker
    drawer.goto(end_x_pos, end_y_pos)
    drawer.color("red")
    drawer.dot(cell_size // 2)

def generate_new_maze():
    """Generate a completely new maze"""
    global maze
    # Reset maze to all walls
    maze = [[True for _ in range(maze_width)] for _ in range(maze_height)]
    
    # Start generation from (1,1) - odd coordinates ensure proper paths
    generate_maze(1, 1)
    
    # Ensure entrance and exit are open
    maze[0][1] = False  # Entrance at top-left
    maze[maze_height-1][maze_width-2] = False  # Exit at bottom-right
    
    draw_maze()
    update_info(f"New {maze_width}x{maze_height} Maze Generated!")

def solve_maze():
    """Solve the maze using DFS and show the solution path"""
    # Find path from start (1,0) to end (maze_width-2, maze_height-1)
    start = (1, 0)
    end = (maze_width-2, maze_height-1)
    
    # DFS to find path
    stack = [(start, [start])]
    visited = set()
    visited.add(start)
    
    while stack:
        (x, y), path = stack.pop()
        
        if (x, y) == end:
            # Draw solution path
            drawer.color("yellow")
            drawer.pensize(3)
            drawer.penup()
            
            for px, py in path:
                screen_x = start_x + px * cell_size + cell_size // 2
                screen_y = start_y - py * cell_size - cell_size // 2
                drawer.goto(screen_x, screen_y)
                drawer.pendown()
            
            drawer.penup()
            update_info("Maze Solved! Path shown in yellow")
            return
        
        # Check neighbors (up, down, left, right)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < maze_width and 0 <= ny < maze_height and 
                not maze[ny][nx] and (nx, ny) not in visited):
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))
    
    update_info("No solution found!")

def increase_size():
    """Increase maze size"""
    global maze_width, maze_height, start_x, start_y
    if maze_width < 41 and maze_height < 41:
        maze_width += 2
        maze_height += 2
        regenerate_maze_with_new_size()

def decrease_size():
    """Decrease maze size"""
    global maze_width, maze_height, start_x, start_y
    if maze_width > 11 and maze_height > 11:
        maze_width -= 2
        maze_height -= 2
        regenerate_maze_with_new_size()

def regenerate_maze_with_new_size():
    """Regenerate maze with new dimensions"""
    global maze, start_x, start_y, width_pixels, height_pixels
    
    # Recalculate screen boundaries
    width_pixels = maze_width * cell_size
    height_pixels = maze_height * cell_size
    start_x = -width_pixels // 2
    start_y = height_pixels // 2
    
    # Clear screen and regenerate
    drawer.clear()
    maze = [[True for _ in range(maze_width)] for _ in range(maze_height)]
    generate_maze(1, 1)
    maze[0][1] = False
    maze[maze_height-1][maze_width-2] = False
    draw_maze()
    update_info(f"Maze size: {maze_width}x{maze_height}")

def update_info(message):
    """Update information display"""
    ui_text.clear()
    ui_text.goto(-400, 420)
    ui_text.write(message, font=("Arial", 12, "bold"))

def change_cell_size():
    """Toggle between small, medium, and large cell sizes"""
    global cell_size, start_x, start_y, width_pixels, height_pixels
    sizes = [15, 20, 25, 30]
    current_index = sizes.index(cell_size) if cell_size in sizes else 1
    cell_size = sizes[(current_index + 1) % len(sizes)]
    
    # Recalculate boundaries
    width_pixels = maze_width * cell_size
    height_pixels = maze_height * cell_size
    start_x = -width_pixels // 2
    start_y = height_pixels // 2
    
    draw_maze()
    update_info(f"Cell size: {cell_size}px")

def draw_boundary():
    """Draw outer boundary for the maze"""
    boundary = turtle.Turtle()
    boundary.speed(0)
    boundary.color("gray")
    boundary.pensize(3)
    boundary.penup()
    boundary.goto(start_x - 5, start_y + 5)
    boundary.pendown()
    for _ in range(2):
        boundary.forward(width_pixels + 10)
        boundary.right(90)
        boundary.forward(height_pixels + 10)
        boundary.right(90)
    boundary.hideturtle()

# Keyboard bindings
screen.listen()
screen.onkey(generate_new_maze, "n")
screen.onkey(solve_maze, "s")
screen.onkey(increase_size, "plus")
screen.onkey(increase_size, "equal")
screen.onkey(decrease_size, "minus")
screen.onkey(change_cell_size, "c")
screen.onkey(lambda: screen.bye(), "Escape")

# Draw instructions panel
def draw_instructions():
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("lightgray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(-400, -440)
    instructions.write("CONTROLS: N=New Maze  S=Solve Maze  +/-=Size  C=Cell Size  ESC=Exit",
                       font=("Arial", 10, "normal"))

# Print console instructions
print("=== MAZE DRAWING GENERATOR ===")
print()
print("Generating a perfect maze using Recursive Backtracking algorithm")
print()
print("CONTROLS:")
print("  N     - Generate a new random maze")
print("  S     - Solve the maze (shows solution path in yellow)")
print("  + / = - Increase maze size")
print("  -     - Decrease maze size")
print("  C     - Change cell size (15/20/25/30px)")
print("  ESC   - Exit program")
print()
print("White walls = barriers, Dark blue = paths")
print("Green dot = Start, Red dot = Exit")
print("Yellow line = Solution path when solved")

# Generate initial maze
generate_new_maze()
draw_boundary()
draw_instructions()
update_info("Maze generated! Press N for new maze, S to solve")

# Keep window open
screen.mainloop()