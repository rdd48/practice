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
    

def part1(fname):
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
    while not finished:
        curr_dist += 1
        curr, grid, next_dir, finished = get_next_square(curr, grid, curr_dist, next_dir)
      
    # for i in grid:
    #     print(''.join([str(j[0]) if j[1] else '.' for j in i]))
    # for i in grid:
    #     print(''.join([str(f'({j[1]})') if j[1] else '.' for j in i]))

    return int(curr_dist / 2)

# print(part1('input/test.txt'))
print(part1('input/10.txt'))