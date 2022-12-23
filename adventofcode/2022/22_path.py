import numpy as np

def process_input(fname):
    a_len = 12 if 'test' in fname else 200
    direct_row = 13 if 'test' in fname else 201
    
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.replace('\n', '') for l in lines]

        col_size = len(max(lines[:a_len], key=len))

        a = np.zeros((a_len, col_size), dtype=int)

        # process map
        # 0 will be sides (can be passed through), 1 is open, 2 is a wall
        for ridx, row in enumerate(lines):
            for cidx, col in enumerate(row):
                if col == '.':
                    a[ridx, cidx] = 1
                elif col == '#':
                    a[ridx, cidx] = 2
        
        # process directions
        directs = []
        running_int = ''
        for ch in lines[direct_row]:
            
            if ch == 'L' or ch == 'R':
                directs.append(int(running_int))
                directs.append(ch)
                running_int = ''
            else:
                running_int += ch
        
        directs.append(int(running_int))
        
    return a, directs

def move_once(pos, ori, rows, cols):
    r,c = pos
    if ori == 'R':
        return (r, c+1) if c < cols - 1 else (r, 0)
    elif ori == 'L':
        return (r, c-1) if c > 0 else (r, cols - 1)
    elif ori == 'U':
        return (r-1, c) if r > 0 else (rows - 1, c)
    else: # ori == 'D'
        return (r+1, c) if r < rows - 1 else (0, c)

def traverse(fname):
    a, directs = process_input(fname)
    rows, cols = a.shape

    # get starting pos:
    idx = None
    for idx, i in enumerate(a[0,:]):
        if i == 1:
            break

    pos = (0, idx)
    ori = 'R'
    oris = 'RDLU'

    for d in directs:
        if d == 'L':
            ori = oris[(oris.index(ori) - 1) % 4]
        elif d == 'R':
            ori = oris[(oris.index(ori) + 1) % 4]
        elif isinstance(d, int):
            for _ in range(d):
                rnext, cnext = move_once(pos, ori, rows, cols)
                # check if 0
                if a[rnext, cnext] == 0:
                    old_pos = pos
                    while a[rnext, cnext] == 0:
                        rnext, cnext = move_once(pos, ori, rows, cols)
                        pos = (rnext, cnext)

                    # case where we wrap around to a # wall
                    if a[rnext, cnext] == 2:
                        pos = old_pos
                    
                # if '.' just move once
                elif a[rnext, cnext] == 1:
                    pos = (rnext, cnext)

                # if '#' then stop
                elif a[rnext, cnext] == 2:
                    break

    return (1000 * (pos[0]+1)) + (4 * (pos[1] + 1)) + oris.index(ori)

# print(traverse('input/test.txt'))
# print(traverse('input/22.txt'))

def move_once_cube(pos, ori, rows, cols):
    r,c = pos

    # where my cube folds
    r0, r1, r2, r3, r4 = 0, 49, 99, 149, rows-1
    c0, c1, c2, c3 = 0, 49, 99, cols-1

    if ori == 'R':
        if c == c3 and r <= r1: # a right
            return 149-r, c2, 'L'
        elif c == c2 and r1 < r <= r2: # b right
            return r1, (r%50)+100,'U'
        elif c == c2 and r2 < r <= r3: # lower a
            return 49-(r%50), c3, 'L'
        elif c == c1 and r3 < r <= r4:# lower g
            return r3, 50+(r%50), 'U'
        return (r, c+1, ori) if c < cols - 1 else (r, 0, ori)

    elif ori == 'L':
        if c == c1+1 and r <= r1: # e top
            return 149-r, 0, 'R'
        elif c == c1+1 and r1 < r <= r2:  # f
            return r2+1, r%50, 'D'
        elif c == 0 and r2 < r <= r3: # e low
            return 49-(r%50), c1+1, 'R'
        elif c == 0 and r3 < r <= r4: # d
            return 0, 50+(r%50), 'D'
        return (r, c-1, ori) if c > 0 else (r, cols - 1, ori)

    elif ori == 'U':
        if r == r2+1 and c <= c1:
            return 50+(c%50), c1+1, 'R'
        elif r == 0 and c1 < c <= c2:
            return 150+(c%50), 0, 'R'
        elif r == 0 and c2 < c <= c3:
            return r4, c%50, 'U'
        return (r-1, c, ori) if r > 0 else (rows - 1, c, ori)

    else: # ori == 'D'
        if r == r4 and c <= c1:
            return 0, 100+c, 'D'
        elif r == r1 and c2 < c <= c3:
            return 50+(c%50), c2, 'L'
        elif r == r3 and c1 < c <= c2:
            return 150+(c%50), c1, 'L'
        return (r+1, c, ori) if r < rows - 1 else (0, c, ori)

def traverse_cube(fname):
    # currently hardcoded for my input shape
    a, directs = process_input(fname)
    rows, cols = a.shape

    # get starting pos:
    idx = None
    for idx, i in enumerate(a[0,:]):
        if i == 1:
            break

    pos = (0, idx)
    ori = 'R'
    oris = 'RDLU'

    for d in directs:
        if d == 'L':
            ori = oris[(oris.index(ori) - 1) % 4]
        elif d == 'R':
            ori = oris[(oris.index(ori) + 1) % 4]
        elif isinstance(d, int):
            for _ in range(d):
                if a[pos[0], pos[1]] == 0:
                    exit('wtf?')
                prev_ori = ori
                rnext, cnext, ori = move_once_cube(pos, ori, rows, cols)
                    
                # if '.' just move once
                if a[rnext, cnext] == 1:
                    pos = (rnext, cnext)

                # if '#' then stop
                elif a[rnext, cnext] == 2:
                    ori = prev_ori
                    break

    return (1000 * (pos[0]+1)) + (4 * (pos[1] + 1)) + oris.index(ori)

# this probably won't actually work with the test, since it's hardcoded for my shape
# print(traverse('input/test.txt'))
print(traverse_cube('input/22.txt'))