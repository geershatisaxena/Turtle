import turtle
import random
from collections import deque
import time

# ----------------------
# Screen Setup
# ----------------------
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("BFS Pathfinding Visualization")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

ROWS = 30
COLS = 30
SIZE = 25

START = (1, 1)
GOAL = (28, 28)

# ----------------------
# Create Maze
# ----------------------
maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for r in range(ROWS):
    for c in range(COLS):
        if (
            r == 0 or c == 0 or
            r == ROWS - 1 or c == COLS - 1
        ):
            maze[r][c] = 1
        elif random.random() < 0.28:
            maze[r][c] = 1

maze[START[0]][START[1]] = 0
maze[GOAL[0]][GOAL[1]] = 0

# ----------------------
# Draw Cell
# ----------------------
def draw_cell(row, col, color):
    x = -375 + col * SIZE
    y = 375 - row * SIZE

    t.goto(x, y)
    t.fillcolor(color)

    t.begin_fill()
    for _ in range(4):
        t.pendown()
        t.forward(SIZE)
        t.right(90)
    t.end_fill()
    t.penup()

# ----------------------
# Draw Maze
# ----------------------
def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c]:
                draw_cell(r, c, "gray20")
            else:
                draw_cell(r, c, "white")

    draw_cell(*START, "lime")
    draw_cell(*GOAL, "red")

draw_maze()

screen.tracer(0)

# ----------------------
# BFS Search
# ----------------------
queue = deque([START])
visited = {START}
parent = {}

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

found = False

while queue:

    current = queue.popleft()

    if current == GOAL:
        found = True
        break

    r, c = current

    if current not in (START, GOAL):
        draw_cell(r, c, "deepskyblue")

    for dr, dc in dirs:

        nr = r + dr
        nc = c + dc

        nxt = (nr, nc)

        if (
            0 <= nr < ROWS and
            0 <= nc < COLS and
            maze[nr][nc] == 0 and
            nxt not in visited
        ):

            visited.add(nxt)
            parent[nxt] = current
            queue.append(nxt)

            if nxt not in (START, GOAL):
                draw_cell(nr, nc, "purple")

    screen.update()
    time.sleep(0.01)

# ----------------------
# Draw Final Path
# ----------------------
if found:

    node = GOAL

    while node != START:
        node = parent[node]

        if node != START:
            draw_cell(*node, "gold")
            screen.update()
            time.sleep(0.03)

draw_cell(*START, "lime")
draw_cell(*GOAL, "red")

screen.update()
screen.mainloop()