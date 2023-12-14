def get_starting_square(start, grid):
    # note this just gets one path for the start

    rows = len(grid)
    cols = len(grid[0])
    r, c = start

    # check left, right, up, down
    # left
    if c-1 >= 0:
        if grid[r][c-1][0] in '-FL':
            next_ds = {'-': 'L', 'F': 'D', 'L': 'U'}
            grid[r][c-1] = (grid[r][c-1][0], 1)
            return (r, c-1), grid, next_ds[grid[r][c-1][0]]

    # right
    if c+1 < cols:
        if grid[r][c+1][0] in '-7J':
            next_ds = {'-': 'R', '7': 'D', 'J': 'U'}
            grid[r][c+1] = (grid[r][c+1][0], 1)
            return (r, c+1), grid, next_ds[grid[r][c+1][0]]

    # up
    if r-1 >= 0:
        if grid[r-1][c][0] in '|F7':
            next_ds = {'|': 'U', 'F': 'R', '7': 'L'}
            grid[r-1][c] = (grid[r-1][c][0], 1)
            return (r-1, c), grid, next_ds[grid[r-1][c][0]]

    # down
    if r+1 < rows:
        if grid[r+1][c][0] in '|JL':
            next_ds = {'|': 'D', 'J': 'L', 'L': 'R'}
            grid[r+1][c] = (grid[r+1][c][0], 1)
            return (r+1, c), grid, next_ds[grid[r+1][c][0]]

def get_next_square(start, grid, curr_dist, next_dir):
    r, c = start

    # check left, right, up, down
    # left
    if next_dir == 'L':
        if grid[r][c-1][0] in '-FL':
            next_ds = {'-': 'L', 'F': 'D', 'L': 'U'}
            grid[r][c-1] = (grid[r][c-1][0], curr_dist)
            return (r, c-1), grid, next_ds[grid[r][c-1][0]], False

    # right
    if next_dir == 'R':
        if grid[r][c+1][0] in '-7J':
            next_ds = {'-': 'R', '7': 'D', 'J': 'U'}
            grid[r][c+1] = (grid[r][c+1][0], curr_dist)
            return (r, c+1), grid, next_ds[grid[r][c+1][0]], False

    # up
    if next_dir == 'U':
        if grid[r-1][c][0] in '|F7':
            next_ds = {'|': 'U', 'F': 'R', '7': 'L'}
            grid[r-1][c] = (grid[r-1][c][0], curr_dist)
            return (r-1, c), grid, next_ds[grid[r-1][c][0]], False

    # down
    if next_dir == 'D':
        if grid[r+1][c][0] in '|JL':
            next_ds = {'|': 'D', 'J': 'L', 'L': 'R'}
            grid[r+1][c] = (grid[r+1][c][0], curr_dist)
            return (r+1, c), grid, next_ds[grid[r+1][c][0]], False
    
    grid[r][c] = ('X',curr_dist)
    return start, grid, '', True

def shoelace(loop_tiles):
    fwd = 0
    rev = 0
    for idx, val in enumerate(loop_tiles):
        curr_x, curr_y = val
        next_x, next_y = loop_tiles[(idx+1) % len(loop_tiles)]
        fwd += (curr_x * next_y)
        rev += (curr_y * next_x)
    return 0.5 * abs(fwd - rev)

def main(fname):
    with open(fname) as f:
        # grid will be a list of lists. each list is a row. within each list is a tuple of (character, distance from S)
        grid = [] 
        start = 'wtf'
        lines = [l.strip() for l in f.readlines() if l.strip()]
        for idx, l in enumerate(lines):
            grid.append([(i, None) for i in l])
            if 'S' in l:
                grid[idx][l.index('S')] = ('S', 0)
                start = (idx, l.index('S'))

    curr_dist = 1
    finished = False

    curr, grid, next_dir = get_starting_square(start, grid)
    loop_tiles = [start]
    while not finished:
        loop_tiles.append(curr)
        curr_dist += 1
        curr, grid, next_dir, finished = get_next_square(curr, grid, curr_dist, next_dir)

    print(f'part 1: {int(curr_dist / 2)}')

    # pick's theorem?
    # area = interior + (1/2 * boundary) - 1
    # interior = area - (1/2 * boundary) + 1

    # shoelace formula?
    # area = 1/2 * abs(((x1 * y2) + (y2 * x3)...) - (y1 * x2))

    shoe_area = shoelace(loop_tiles)
    return f'part 2: {int(shoe_area - (0.5 * len(loop_tiles)) + 1)}'

    

# print(part1('input/test.txt'))
print(main('input/10.txt'))