def process_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        # keeping things in zero-indexed row, col like numpy so this is first row, 2nd column
        pos = (0,1)
        end = (len(lines)-1, len(lines[-1])-2)

        # blizzards will be a tuple of (row, col, dr, dc, dir)
        blizzards = set()
        for ridx, r in enumerate(lines):
            for cidx, c in enumerate(r):
                if c == '>':
                    blizzards.add((ridx, cidx, 1, 0, 'R'))
                elif c == '<':
                    blizzards.add((ridx, cidx, -1, 0, 'L'))
                elif c == '^':
                    blizzards.add((ridx, cidx, 0, -1, 'U'))
                elif c == 'v':
                    blizzards.add((ridx, cidx, 0, 1, 'D'))
    
    return blizzards, pos, end

def move_blizzards(blizzards, end):
    endr, endc = end
    new_blizzards = set()
    new_blizzards_short = set()
    for r, c, dr, dc, dir in blizzards:
        if dir == 'R':
            new_c = 1 if c == endc else c+1
            new_blizzards.add((r, new_c, dr, dc, dir))
            new_blizzards_short.add((r, new_c))
        elif dir == 'L':
            new_c = endc if c == 1 else c-1
            new_blizzards.add((r, new_c, dr, dc, dir))
            new_blizzards_short.add((r, new_c))
        elif dir == 'U':
            new_r = endr-1 if r == 1 else r-1
            new_blizzards.add((new_r, c, dr, dc, dir))
            new_blizzards_short.add((new_r, c))
        elif dir == 'D':
            new_r = 1 if r == endr-1 else r+1
            new_blizzards.add((new_r, c, dr, dc, dir))
            new_blizzards_short.add((new_r, c))

    return new_blizzards, new_blizzards_short

def get_move_options(pos, blizzards_short, end):
    endr, endc = end
    r, c = pos
    options = [(r, c), (r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    new_pos = []

    for nr,nc in options:
        # edge case where we're at the starting pos
        if (nr, nc) == (0, 1):
            new_pos.append((nr, nc))

        # edge case where we're at the end pos
        if (nr, nc) == end:
            new_pos.append((nr, nc))
        
        # check for walls
        elif nr <= 0 or nr == endr or nc == 0 or nc == endc+1:
            continue
        
        # check for blizzards
        elif (nr, nc) not in blizzards_short:
            new_pos.append((nr, nc))
    
    return new_pos

def bfs(blizzards, start, goal, map_end, win_check, rd):
    all_pos = {(start[0], start[1])}
    all_new_pos = set()

    while True:
        rd += 1
        blizzards, blizzards_short = move_blizzards(blizzards, map_end)

        for r,c in all_pos:
            # check win here
            if (r+win_check, c) == goal:
                return rd, blizzards
            
            new_pos = get_move_options((r,c), blizzards_short, map_end)
            for np in new_pos:
                all_new_pos.add(np)
        
        all_pos = all_new_pos
        all_new_pos = set()

def traverse_blizzards(fname, part2=False):
    blizzards, _, end = process_input(fname)

    rd, blizzards = bfs(blizzards, (0,1), end, end, 1, 0)
    if not part2:
        return rd

    rd, blizzards = bfs(blizzards, end, (0,1), end, -1, rd)
    rd, _ = bfs(blizzards, (0,1), end, end, 1, rd)
    return rd


# print(bfs('input/test.txt'))
print(traverse_blizzards('input/24.txt'))

# print(bfs_wrapper('input/test.txt'))
print(traverse_blizzards('input/24.txt', part2=True))