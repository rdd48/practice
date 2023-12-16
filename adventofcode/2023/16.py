def get_next_beam_pos(br, bc, beam_dir):
    if beam_dir == 'L':
        return (br, bc-1)
    elif beam_dir == 'R':
        return (br, bc+1)
    elif beam_dir == 'U':
        return (br-1, bc)
    elif beam_dir == 'D':
        return (br+1, bc)

def beam_on_grid(beam, rows, cols):
    beam_pos, beam_dir = beam
    br, bc = beam_pos
    nr, nc = get_next_beam_pos(br, bc, beam_dir)
    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        return False
    return (nr, nc)

def get_new_beam_dir(beam_dir, new_sq):
    # returns strs of new dirs. if beam is split, len(new_dir) == 2
    # \\ needed to escape the \
    if beam_dir == 'L':
        new_dir = {'.': 'L', '-': 'L', '\\': 'U', '/': 'D', '|': 'UD'}
        return new_dir[new_sq]
    elif beam_dir == 'R':
        new_dir = {'.': 'R', '-': 'R', '\\': 'D', '/': 'U', '|': 'UD'}
        return new_dir[new_sq]
    elif beam_dir == 'U':
        new_dir = {'.': 'U', '-': 'LR', '\\': 'L', '/': 'R', '|': 'U'}
        return new_dir[new_sq]
    elif beam_dir == 'D':
        new_dir = {'.': 'D', '-': 'LR', '\\': 'R', '/': 'L', '|': 'D'}
        return new_dir[new_sq]

def main(fname):
    with open(fname) as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]
    
    rows, cols = len(grid), len(grid[0])
    # beams is a set of all current beams ((r,c), direction)
    # directions = L, R, D, U
    first_dir = get_new_beam_dir('R', grid[0][0])
    prev_beams = {((0,0), first_dir)}
    new_beams = set()
    all_beams = {(0,0)}

    while True:
    # for _ in range(5):
        for beam in prev_beams:
            # need to get the beams new pos and direction
            # also need to check if beam goes off grid
            if new_pos := beam_on_grid(beam, rows, cols):
                nr, nc = new_pos
                new_sq = grid[nr][nc]
                for dr in get_new_beam_dir(beam[1], new_sq):
                    new_beams.add(((nr, nc), dr))
                    all_beams.add(((nr, nc)))
        
        # print(all_beams)
        if new_beams == prev_beams:
            return len(all_beams)
        # print(len(all_beams))
        
        prev_beams = new_beams.copy()

def get_tile_energies(grid, rows, cols, startr, startc, start_dir):

    for first_dir in get_new_beam_dir(start_dir, grid[startr][startc]):
        # first_dir = get_new_beam_dir(start_dir, grid[startr][startc])
        prev_beams = {((startr, startc), first_dir)}
        new_beams = set()
        all_beams = {(startr, startc)}

    while True:
        for beam in prev_beams:
            # need to get the beams new pos and direction
            # also need to check if beam goes off grid
            if new_pos := beam_on_grid(beam, rows, cols):
                nr, nc = new_pos
                new_sq = grid[nr][nc]
                for dr in get_new_beam_dir(beam[1], new_sq):
                    new_beams.add(((nr, nc), dr))
                    all_beams.add(((nr, nc)))
        
        # print(all_beams)
        if new_beams == prev_beams:
            return len(all_beams)
        
        prev_beams = new_beams.copy()


def main2(fname):
    with open(fname) as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]
    rows, cols = len(grid), len(grid[0])
    
    best_len = 0
    for row in range(rows):
        best_len = max(best_len, get_tile_energies(grid, rows, cols, row, 0, 'R'))
        best_len = max(best_len, get_tile_energies(grid, rows, cols, row, cols-1, 'L'))
        print(row)
    print('finished RL')
    
    for col in range(cols):
        best_len = max(best_len, get_tile_energies(grid, rows, cols, 0, col, 'D'))
        best_len = max(best_len, get_tile_energies(grid, rows, cols, rows-1, col, 'U'))
        print(col)
    
    return best_len

# print(main('input/test.txt'))
print(main('input/16.txt'))

# brute force! takes forever lol
# print(main2('input/test.txt'))
print(main2('input/16.txt'))