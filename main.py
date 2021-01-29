import random


def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat

def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2
    return mat


def compress(grid):
    new = []
    for i in range(4):
        new.append([0] * 4)
        k = 0
        for j in range(4):
            if grid[i][j] != 0:
                new[i][k] = grid[i][j]
                k += 1
    return new


def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1]:
                grid[i][j] = 2 * grid[i][j]
                grid[i][j + 1] = 0
    return grid


def reverse(grid):
    new = []
    for i in range(4):
        new.append([])
        for j in range(3, -1, -1):
            new[i].append(grid[i][j])
    return new


def transpose(grid):
    new = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            new[j][i] = grid[i][j]
    return new


def move_up(grid):
    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)
    return grid


def move_down(grid):
    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)
    return grid


def move_right(grid):
    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)
    return grid


def move_left(grid):
    grid = compress(grid)
    grid = merge(grid)
    grid = compress(grid)
    return grid
def get_curr_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return "GAME NOT OVER"
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return "GAME NOT OVER"
    for i in range(3):
        if mat[3][i] == mat[3][i + 1]:
            return "GAME NOT OVER"
    return "LOST"


