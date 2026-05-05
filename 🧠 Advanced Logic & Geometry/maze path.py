import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Maze Path Solver Visualization")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.tracer(0)

# Maze settings
cell_size = 30
maze_width = 21   # Must be odd for perfect maze
maze_height = 21  # Must be odd for perfect maze

# Calculate screen position
width_pixels = maze_width * cell_size
height_pixels = maze_height * cell_size
start_x = -width_pixels // 2
start_y = height_pixels // 2

# Create turtles
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.penup()
maze_turtle.hideturtle()

solver_turtle = turtle.Turtle()
solver_turtle.speed(0)
solver_turtle.penup()
solver_turtle.hideturtle()

# Maze data structure
# True = wall, False = path
maze = [[True for _ in range(maze_width)] for _ in range(maze_height)]

# Solution path storage
solution_path = []
visited_cells = []

def generate_maze(x, y):
    """Recursive backtracking maze generation"""
    # Mark current cell as path
    maze[y][x] = False
    
    # Create list of possible directions (up, down, left, right)
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
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
    """Draw the maze walls"""
    maze_turtle.clear()
    
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x]:  # Draw wall
                draw_cell(x, y, "white")
    
    screen.update()

def draw_cell(x, y, color, fill=False):
    """Draw a single cell of the maze"""
    screen_x = start_x + x * cell_size
    screen_y = start_y - y * cell_size
    
    maze_turtle.goto(screen_x, screen_y)
    maze_turtle.pendown()
    maze_turtle.color(color)
    maze_turtle.pensize(2)
    
    if fill:
        maze_turtle.begin_fill()
        maze_turtle.fillcolor(color)
    
    for _ in range(4):
        maze_turtle.forward(cell_size)
        maze_turtle.right(90)
    
    if fill:
        maze_turtle.end_fill()
    
    maze_turtle.penup()

def mark_start_end():
    """Mark start (green) and end (red) positions"""
    # Start at top-left (entrance)
    start_cell = (1, 0)
    end_cell = (maze_width - 2, maze_height - 1)
    
    # Mark start
    draw_cell(start_cell[0], start_cell[1], "lime", fill=True)
    
    # Mark end
    draw_cell(end_cell[0], end_cell[1], "red", fill=True)
    
    return start_cell, end_cell

def solve_maze_dfs(x, y, end_x, end_y):
    """Solve maze using Depth-First Search (visualized)"""
    global solution_path, visited_cells
    
    # Stack for DFS: (x, y, path)
    stack = [(x, y, [(x, y)])]
    visited = set()
    visited.add((x, y))
    
    solver_turtle.clear()
    
    while stack:
        cx, cy, path = stack.pop()
        
        # Visualize current exploration
        visualization_turtle = turtle.Turtle()
        visualization_turtle.speed(0)
        visualization_turtle.penup()
        visualization_turtle.hideturtle()
        
        # Draw current position
        screen_x = start_x + cx * cell_size + cell_size // 2
        screen_y = start_y - cy * cell_size - cell_size // 2
        visualization_turtle.goto(screen_x, screen_y)
        visualization_turtle.dot(cell_size // 2, "cyan")
        
        screen.update()
        time.sleep(0.05)
        visualization_turtle.clear()
        
        # Check if reached end
        if (cx, cy) == (end_x, end_y):
            solution_path = path
            return path
        
        # Explore neighbors (up, down, left, right)
        neighbors = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < maze_width and 0 <= ny < maze_height and 
                not maze[ny][nx] and (nx, ny) not in visited):
                neighbors.append((nx, ny))
        
        # Randomize neighbor order for variety
        random.shuffle(neighbors)
        
        for nx, ny in neighbors:
            visited.add((nx, ny))
            stack.append((nx, ny, path + [(nx, ny)]))
    
    return None

def solve_maze_bfs(x, y, end_x, end_y):
    """Solve maze using Breadth-First Search (shortest path)"""
    global solution_path
    
    from collections import deque
    
    queue = deque([(x, y, [(x, y)])])
    visited = set()
    visited.add((x, y))
    
    solver_turtle.clear()
    
    while queue:
        cx, cy, path = queue.popleft()
        
        # Visualize current exploration
        visualization_turtle = turtle.Turtle()
        visualization_turtle.speed(0)
        visualization_turtle.penup()
        visualization_turtle.hideturtle()
        
        screen_x = start_x + cx * cell_size + cell_size // 2
        screen_y = start_y - cy * cell_size - cell_size // 2
        visualization_turtle.goto(screen_x, screen_y)
        visualization_turtle.dot(cell_size // 2, "cyan")
        
        screen.update()
        time.sleep(0.03)
        visualization_turtle.clear()
        
        # Check if reached end
        if (cx, cy) == (end_x, end_y):
            solution_path = path
            return path
        
        # Explore neighbors
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < maze_width and 0 <= ny < maze_height and 
                not maze[ny][nx] and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny, path + [(nx, ny)]))
    
    return None

def draw_solution_path(path):
    """Draw the solution path through the maze"""
    if not path:
        return
    
    path_turtle = turtle.Turtle()
    path_turtle.speed(0)
    path_turtle.color("yellow")
    path_turtle.penup()
    path_turtle.hideturtle()
    path_turtle.pensize(3)
    
    # Draw the path
    for i, (x, y) in enumerate(path):
        screen_x = start_x + x * cell_size + cell_size // 2
        screen_y = start_y - y * cell_size - cell_size // 2
        
        if i == 0:
            path_turtle.goto(screen_x, screen_y)
            path_turtle.pendown()
        else:
            path_turtle.goto(screen_x, screen_y)
        
        # Add dot at each step
        path_turtle.dot(4, "yellow")
        
        if i % 20 == 0:
            screen.update()
    
    path_turtle.penup()
    screen.update()

def draw_path_finder_effect(path):
    """Animate the path being discovered"""
    if not path:
        return
    
    finder = turtle.Turtle()
    finder.speed(0)
    finder.shape("turtle")
    finder.color("lime")
    finder.penup()
    finder.shapesize(1.5, 1.5)
    
    for x, y in path:
        screen_x = start_x + x * cell_size + cell_size // 2
        screen_y = start_y - y * cell_size - cell_size // 2
        finder.goto(screen_x, screen_y)
        screen.update()
        time.sleep(0.05)
    
    finder.hideturtle()

def draw_statistics(path, algorithm, time_taken):
    """Draw solution statistics"""
    stat_turtle = turtle.Turtle()
    stat_turtle.speed(0)
    stat_turtle.color("white")
    stat_turtle.penup()
    stat_turtle.hideturtle()
    stat_turtle.goto(-430, -400)
    stat_turtle.write(f"Algorithm: {algorithm}", font=("Arial", 10, "normal"))
    stat_turtle.goto(-430, -420)
    stat_turtle.write(f"Path Length: {len(path)} steps", font=("Arial", 10, "normal"))
    stat_turtle.goto(-430, -440)
    stat_turtle.write(f"Time: {time_taken:.3f} seconds", font=("Arial", 10, "normal"))

def reset_maze():
    """Generate a new maze"""
    global maze, solution_path
    maze = [[True for _ in range(maze_width)] for _ in range(maze_height)]
    generate_maze(1, 1)
    maze[0][1] = False  # Entrance
    maze[maze_height-1][maze_width-2] = False  # Exit
    solution_path = []
    draw_maze()
    return mark_start_end()

# Algorithm selection
algorithm = "DFS"  # DFS or BFS

def solve_with_algorithm(start, end):
    """Solve maze with selected algorithm"""
    global solution_path
    
    start_time = time.time()
    
    if algorithm == "DFS":
        path = solve_maze_dfs(start[0], start[1], end[0], end[1])
        algo_name = "Depth-First Search (DFS)"
    else:
        path = solve_maze_bfs(start[0], start[1], end[0], end[1])
        algo_name = "Breadth-First Search (BFS)"
    
    end_time = time.time()
    
    if path:
        solution_path = path
        draw_solution_path(path)
        draw_statistics(path, algo_name, end_time - start_time)
        return True
    else:
        return False

# UI Elements
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 420)
    title.write("🧠 MAZE PATH SOLVER VISUALIZATION 🧠", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -460)
    instructions.write("N=New Maze  S=Solve (DFS)  B=Solve (BFS)  C=Clear Path  Q=Show Path Finder  ESC=Exit",
                       align="center", font=("Arial", 10, "normal"))

def show_path_finder():
    """Animate the path finder turtle"""
    if solution_path:
        draw_path_finder_effect(solution_path)

def clear_path():
    """Clear the solution path"""
    global solution_path
    solution_path = []
    draw_maze()
    mark_start_end()

# Main execution
draw_title()
reset_maze()
start_cell, end_cell = mark_start_end()

# Keyboard bindings
screen.listen()
screen.onkey(lambda: [reset_maze(), (start_cell, end_cell)], "n")
screen.onkey(lambda: [solve_with_algorithm(start_cell, end_cell)], "s")
screen.onkey(lambda: [setattr(__import__('__main__'), 'algorithm', "BFS"), 
                       solve_with_algorithm(start_cell, end_cell)], "b")
screen.onkey(clear_path, "c")
screen.onkey(show_path_finder, "q")
screen.onkey(lambda: screen.bye(), "Escape")

print("=" * 60)
print("        MAZE PATH SOLVER VISUALIZATION")
print("=" * 60)
print()
print("Watch as algorithms find their way through the maze!")
print()
print("MAZE FEATURES:")
print("  • Perfect maze generated with recursive backtracking")
print("  • Green cell = START (top-left)")
print("  • Red cell = END (bottom-right)")
print("  • White walls, black paths")
print()
print("SOLVING ALGORITHMS:")
print("  • DFS (Depth-First Search) - Press S")
print("    - Explores deep paths first")
print("    - Finds a path quickly (not always shortest)")
print()
print("  • BFS (Breadth-First Search) - Press B")
print("    - Explores all paths equally")
print("    - Guarantees SHORTEST path")
print()
print("VISUALIZATION:")
print("  • Blue dots = Algorithm exploration")
print("  • Yellow line = Final solution path")
print("  • Press Q to see animated path finder")
print()
print("CONTROLS:")
print("  N - Generate new maze")
print("  S - Solve using DFS (watch exploration)")
print("  B - Solve using BFS (shortest path)")
print("  C - Clear solution path")
print("  Q - Show path finder animation")
print("  ESC - Exit")
print()
print("Watch the difference between DFS and BFS!")

screen.mainloop()