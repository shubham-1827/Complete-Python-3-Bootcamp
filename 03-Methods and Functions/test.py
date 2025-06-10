from p5 import *
import random

grid_size = 10
tile_size = 40

# Define tiles with edge compatibility (0=open, 1=wall)
tiles = [
    {"id": 0, "edges": [1, 1, 1, 1]},  # Full box
    {"id": 1, "edges": [0, 1, 0, 1]},  # Vertical wall
    {"id": 2, "edges": [1, 0, 1, 0]},  # Horizontal wall
    {"id": 3, "edges": [0, 0, 1, 1]},  # Corner
    {"id": 4, "edges": [1, 1, 0, 0]},  # Inverse corner
]

grid = [[list(range(len(tiles))) for _ in range(grid_size)] for _ in range(grid_size)]
collapsed = False


def edge_compatible(e1, e2):
    return e1 == e2


def propagate():
    changed = False
    for y in range(grid_size):
        for x in range(grid_size):
            if isinstance(grid[y][x], list) and len(grid[y][x]) == 1:
                tid = grid[y][x][0]
                t_edges = tiles[tid]["edges"]

                for dy, dx, edge_idx, neighbor_edge_idx in [
                    (-1, 0, 0, 2),
                    (0, 1, 1, 3),
                    (1, 0, 2, 0),
                    (0, -1, 3, 1),
                ]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < grid_size and 0 <= nx < grid_size:
                        if isinstance(grid[ny][nx], list):
                            old = set(grid[ny][nx])
                            grid[ny][nx] = [
                                tid2
                                for tid2 in grid[ny][nx]
                                if edge_compatible(
                                    tiles[tid2]["edges"][neighbor_edge_idx],
                                    t_edges[edge_idx],
                                )
                            ]
                            if set(grid[ny][nx]) != old:
                                changed = True
    return changed


def collapse_next():
    candidates = [
        (x, y)
        for y in range(grid_size)
        for x in range(grid_size)
        if isinstance(grid[y][x], list) and len(grid[y][x]) > 1
    ]
    if not candidates:
        return False

    x, y = random.choice(candidates)
    grid[y][x] = [random.choice(grid[y][x])]
    return True


def draw_tile(x, y, tile_id):
    px = x * tile_size
    py = y * tile_size
    fill(0)
    stroke(255)
    stroke_weight(2)

    edges = tiles[tile_id]["edges"]
    if edges[0]:
        line(px, py, px + tile_size, py)  # top
    if edges[1]:
        line(px + tile_size, py, px + tile_size, py + tile_size)  # right
    if edges[2]:
        line(px + tile_size, py + tile_size, px, py + tile_size)  # bottom
    if edges[3]:
        line(px, py + tile_size, px, py)  # left


def setup():
    size(tile_size * grid_size, tile_size * grid_size)
    title("Wave Function Collapse (p5py)")


def draw():
    global collapsed
    background(240)

    if not collapsed:
        changed = True
        while changed:
            changed = propagate()

        collapsed = not collapse_next()

    for y in range(grid_size):
        for x in range(grid_size):
            if isinstance(grid[y][x], list) and len(grid[y][x]) == 1:
                draw_tile(x, y, grid[y][x][0])
            else:
                fill(200)
                stroke(180)
                rect(x * tile_size, y * tile_size, tile_size, tile_size)


if __name__ == "__main__":
    run()
