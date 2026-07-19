import turtle
import random
import heapq
import time

# Screen setup
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("A* Pathfinding Visualization")

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

# Grid settings
ROWS = 25
COLS = 25
CELL = 30

START = (0, 0)
GOAL = (24, 24)

# Generate grid
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Random obstacles
for r in range(ROWS):
    for c in range(COLS):
        if random.random() < 0.25 and (r, c) != START and (r, c) != GOAL:
            grid[r][c] = 1

def draw_cell(row, col, color):
    x = -375 + col * CELL
    y = 375 - row * CELL

    drawer.goto(x, y)
    drawer.fillcolor(color)

    drawer.begin_fill()
    for _ in range(4):
        drawer.pendown()
        drawer.forward(CELL)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                draw_cell(r, c, "gray20")
            else:
                draw_cell(r, c, "white")

    draw_cell(*START, "green")
    draw_cell(*GOAL, "red")

draw_grid()

# A* Functions
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def neighbors(node):
    r, c = node

    moves = [
        (r+1, c),
        (r-1, c),
        (r, c+1),
        (r, c-1)
    ]

    result = []

    for nr, nc in moves:
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if grid[nr][nc] == 0:
                result.append((nr, nc))

    return result

def reconstruct(came_from, current):
    while current in came_from:
        current = came_from[current]

        if current not in (START, GOAL):
            draw_cell(*current, "gold")
            screen.update()
            time.sleep(0.02)

screen.tracer(0)

# A* Search
open_set = []
heapq.heappush(open_set, (0, START))

came_from = {}

g_score = {START: 0}
f_score = {START: heuristic(START, GOAL)}

visited = set()

found = False

while open_set:

    current = heapq.heappop(open_set)[1]

    if current == GOAL:
        found = True
        break

    visited.add(current)

    if current not in (START, GOAL):
        draw_cell(*current, "deepskyblue")

    for neighbor in neighbors(current):

        tentative_g = g_score[current] + 1

        if tentative_g < g_score.get(neighbor, float("inf")):

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g

            f = tentative_g + heuristic(neighbor, GOAL)
            f_score[neighbor] = f

            heapq.heappush(open_set, (f, neighbor))

            if neighbor not in (START, GOAL):
                draw_cell(*neighbor, "purple")

    screen.update()
    time.sleep(0.01)

if found:
    reconstruct(came_from, GOAL)
    print("Path Found!")
else:
    print("No Path Exists!")

draw_cell(*START, "green")
draw_cell(*GOAL, "red")

screen.update()
screen.mainloop()