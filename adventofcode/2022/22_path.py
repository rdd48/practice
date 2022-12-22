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

def move_once(pos, ori):
    r,c = pos
    if ori == 'R':
        return (r, c+1)
    elif ori == 'L':
        return (r, c-1)
    elif ori == 'U':
        return(r-1, c)
    elif ori == 'D':
        return(r+1, c)

def traverse(fname):
    a, directs = process_input(fname)

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
            for i in range(d):
                
                # check if edge
                # then wrap around

                # if '.' just move once

                # if '#' then stop
                
        else:
            print('wtf?')


print(traverse('input/test.txt'))
# print(traverse('input/22.txt'))