import numpy as np


def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        rows = len(lines)
        cols = len(lines[0].strip())
        grid = np.zeros((rows, cols), dtype=int)
        for row_idx, l in enumerate(lines):
            for col_idx, ch in enumerate(l.strip()):
                if ch == '>':
                    grid[row_idx, col_idx] = 1
                elif ch == 'v':
                    grid[row_idx, col_idx] = 2

        return rows, cols, grid


def is_right(c, cols):
    return True if c == cols - 1 else False


def is_bottom(r, rows):
    return True if r == rows - 1 else False


def print_grid(grid):
    rows, cols = np.shape(grid)
    for r in range(rows):
        print(grid[r, :])


def main(filename):
    rows, cols, grid = process_input(filename)
    moved = True
    steps = 0
    while moved:
        steps += 1

        moved = False
        grid_ones = np.zeros((rows, cols), dtype=int)
        grid_twos = np.zeros((rows, cols), dtype=int)

        # print_grid(grid)
        # print('')

        # check for >s first
        for r in range(rows):
            for c in range(cols):
                if grid[r, c] == 1:
                    # check if on the right
                    if is_right(c, cols):
                        next_c = 0
                    else:
                        next_c = c + 1

                    if grid[r, next_c] == 0:
                        grid_ones[r, next_c] = 1
                        moved = True
                    else:
                        grid_ones[r, c] = 1
                if grid[r, c] == 2:
                    grid_ones[r, c] = 2

        # check for vs last
        for r in range(rows):
            for c in range(cols):
                if grid[r, c] == 2:
                    # check if on the bottom
                    if is_bottom(r, rows):
                        next_r = 0
                    else:
                        next_r = r + 1

                    if grid_ones[next_r, c] == 0:
                        grid_twos[next_r, c] = 2
                        moved = True
                    else:
                        grid_twos[r, c] = 2

        grid = np.zeros((rows, cols), dtype=int)
        for r in range(rows):
            for c in range(cols):
                if grid_ones[r, c] == 1:
                    grid[r, c] = 1
                elif grid_twos[r, c] == 2:
                    grid[r, c] = 2

        print(steps)
        # print_grid(grid)
        # print('')

    return steps


# print(main('input/test.txt'))
print(main('input/25_cukes.txt'))
