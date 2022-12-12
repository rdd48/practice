import numpy as np

def process_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        rows = len(lines)
        cols = len(lines[0])
        a = np.zeros((rows, cols), dtype='int')

        letters = 'SabcdefghijklmnopqrstuvwxyzE'

        for row, line in enumerate(lines):
            for col, val in enumerate(line):
                a[row, col] = letters.index(val)
                if val == 'S':
                    start = (row, col)

    return a, start

def check_edge(pos, rows, cols):
    l = True if pos[1] > 0 else False
    r = True if pos[1] < cols-1 else False
    u = True if pos[0] > 0 else False
    d = True if pos[0] < rows-1 else False
    return l,r,u,d

def climb(fname):
    a, start = process_input(fname)
    rows, cols = a.shape
    paths = [[start]]
    next_paths = []
    visited = set(start)
    left_pos, right_pos, down_pos, up_pos = False, False, False, False
    
    while True:
        for path in paths:
            left, right, up, down = check_edge(path[-1], rows, cols)
            x,y = path[-1]

            if left:
                left_pos = (x, y-1)
                if a[x,y] >= a[left_pos]-1 and left_pos not in visited:
                    visited.add(left_pos)
                    if a[left_pos] == 27:
                        return len(path)
                    next_paths.append(path + [left_pos])
            
            if right:
                right_pos = (x, y+1)
                if a[x,y] >= a[right_pos]-1 and right_pos not in visited:
                    visited.add(right_pos)
                    if a[right_pos] == 27:
                        return len(path)
                    next_paths.append(path + [right_pos])
            
            if up:
                up_pos = (x-1, y)
                if a[x,y] >= a[up_pos]-1 and up_pos not in visited:
                    visited.add(up_pos)
                    if a[up_pos] == 27:
                        return len(path)
                    next_paths.append(path + [up_pos])
            
            if down:
                down_pos = (x+1, y)
                if a[x,y] >= a[down_pos]-1 and down_pos not in visited:
                    visited.add(down_pos)
                    if a[down_pos] == 27:
                        return len(path)
                    next_paths.append(path + [down_pos])
        
        paths = next_paths
        next_paths = []

# print(climb('input/test.txt'))
# print(climb('input/12.txt'))


def climb2(fname):
    a, _ = process_input(fname)
    rows, cols = a.shape
    paths = []
    for r in range(rows):
        for c in range(cols):
            if a[r, c] == 1:

                # visited will need to be unique for each item now, right? idk it's 12:15am
                paths.append([[(r,c)], set((r,c))])

    next_paths = []

    
    
    while True:
        for p in paths:
            path, visited = p
            left, right, up, down = check_edge(path[-1], rows, cols)
            x,y = path[-1]

            if left:
                left_pos = (x, y-1)
                if a[x,y] >= a[left_pos]-1 and left_pos not in visited:
                    visited.add(left_pos)
                    if a[left_pos] == 27:
                        return len(path)
                    next_paths.append([path + [left_pos], visited])
            
            if right:
                right_pos = (x, y+1)
                if a[x,y] >= a[right_pos]-1 and right_pos not in visited:
                    visited.add(right_pos)
                    if a[right_pos] == 27:
                        return len(path)
                    next_paths.append([path + [right_pos], visited])
            
            if up:
                up_pos = (x-1, y)
                if a[x,y] >= a[up_pos]-1 and up_pos not in visited:
                    visited.add(up_pos)
                    if a[up_pos] == 27:
                        return len(path)
                    next_paths.append([path + [up_pos], visited])
            
            if down:
                down_pos = (x+1, y)
                if a[x,y] >= a[down_pos]-1 and down_pos not in visited:
                    visited.add(down_pos)
                    if a[down_pos] == 27:
                        return len(path)
                    next_paths.append([path + [down_pos], visited])
        
        paths = next_paths
        next_paths = []

# print(climb2('input/test.txt'))
print(climb2('input/12.txt'))