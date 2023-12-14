def tilt_rock_north(grid, ridx, cidx):
    if ridx < 1:
        return grid
    
    new_grid = grid.copy()
    for r in range(ridx, 0, -1):
        if grid[r-1][cidx] in '#O':
            new_grid[ridx][cidx] = '.'
            new_grid[r][cidx] = 'O'
            return new_grid

        if r == 1 and grid[0][cidx] == '.':
            new_grid[ridx][cidx] = '.'
            new_grid[0][cidx] = 'O'
            return new_grid

def tilt_rock_west(grid, ridx, cidx):
    if cidx < 1:
        return grid
    
    new_grid = grid.copy()
    for c in range(cidx, 0, -1):
        if grid[ridx][c-1] in '#O':
            new_grid[ridx][cidx] = '.'
            new_grid[ridx][c] = 'O'
            return new_grid

        if c == 1 and grid[ridx][0] == '.':
            new_grid[ridx][cidx] = '.'
            new_grid[ridx][0] = 'O'
            return new_grid


def tilt_rock_south(grid, ridx, cidx):
    if ridx == len(grid)-1:
        return grid
    
    new_grid = grid.copy()
    for r in range(ridx, len(grid)):
        if grid[r+1][cidx] in '#O':
            new_grid[ridx][cidx] = '.'
            new_grid[r][cidx] = 'O'
            return new_grid

        if r == len(grid)-2 and grid[len(grid)-1][cidx] == '.':
            new_grid[ridx][cidx] = '.'
            new_grid[r+1][cidx] = 'O'
            return new_grid
        
def tilt_rock_east(grid, ridx, cidx):
    clen = len(grid[0])
    if cidx == clen-1:
        return grid
    
    new_grid = grid.copy()
    for c in range(cidx, clen):
        if grid[ridx][c+1] in '#O':
            new_grid[ridx][cidx] = '.'
            new_grid[ridx][c] = 'O'
            return new_grid

        if c == clen-2 and grid[ridx][clen-1] == '.':
            new_grid[ridx][cidx] = '.'
            new_grid[ridx][clen-1] = 'O'
            return new_grid

def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines()]
    
    grid = [] # a list of lists, each sublist is a list of chars. makes for easier assignment.
    for l in lines:
        grid.append([i for i in l])

    rows, cols = len(grid), len(grid[0])
    
    for ridx in range(1, rows): # don't need to roll the first row
        for cidx in range(cols):
            if grid[ridx][cidx] == 'O':
                grid = tilt_rock_north(grid, ridx, cidx)

    total = 0
    for ridx in range(1, rows+1):
        for cidx in range(cols):
            if grid[-ridx][cidx] == 'O':
                total += ridx
    
    return total

def flatten_grid(grid):
    fg = ''
    for r in grid:
        fg += ''.join(r)
    return fg

def unflatten_grid(fg, rows):
    grid = []
    for i in range(0, len(fg), rows):
        grid.append([j for j in fg[i:i+rows]])
    return grid

def main2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines()]
    
    grid = [] # a list of lists, each sublist is a list of chars. makes for easier assignment.
    for l in lines:
        grid.append([i for i in l])

    rows, cols = len(grid), len(grid[0])
    
    prev_grids = {}
    rounds = 1000000000

    # start from 1 since the round counting is 1-indexed
    for rd in range(1, rounds): 
        for ridx in range(1, rows):
            for cidx in range(cols):
                if grid[ridx][cidx] == 'O':
                    grid = tilt_rock_north(grid, ridx, cidx)
        for ridx in range(rows):
            for cidx in range(1,cols):
                if grid[ridx][cidx] == 'O':         
                    grid = tilt_rock_west(grid, ridx, cidx)
        for ridx in range(rows-2,-1,-1):
            for cidx in range(cols):
                if grid[ridx][cidx] == 'O':         
                    grid = tilt_rock_south(grid, ridx, cidx)
        for ridx in range(rows):
            for cidx in range(cols-2,-1,-1):
                if grid[ridx][cidx] == 'O':         
                    grid = tilt_rock_east(grid, ridx, cidx)
        
        # start adding grids to cache after stabilizing, say 100 rounds in
        if rd > 99:
            fg = flatten_grid(grid)

            if fg in prev_grids:
                prev_idx = prev_grids[fg]
                round_len = rd - prev_idx

                # there's probably a smart way of doing this. this was just trial and error.
                if rounds % round_len == rd % round_len:
                    subtotal = 0
                    for ridx in range(1, rows+1):
                        for cidx in range(cols):
                            if grid[-ridx][cidx] == 'O':
                                subtotal += ridx
                    return subtotal
            
            prev_grids[fg] = rd

print(main2('input/14.txt'))