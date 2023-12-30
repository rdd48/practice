
def check_nbrs(r,c,grid,rows,cols):
    nbrs = []
    if r > 0:
        if grid[r-1][c] in '.S':
            nbrs.append((r-1,c))
    if r < rows-1:
        if grid[r+1][c] in '.S':
            nbrs.append((r+1,c))
    if c > 0:
        if grid[r][c-1] in '.S':
            nbrs.append((r,c-1))
    if c < cols-1:
        if grid[r][c+1] in '.S':
            nbrs.append((r,c+1))

    return nbrs

def main(fname, steps):
    with open(fname) as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]

    rows, cols = len(grid), len(grid[0])
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == 'S':
                start = (ridx, cidx)

    curr_paths, new_paths = {start}, set()
    for _ in range(steps):
        for path in curr_paths:
            r,c = path
            for nbr in check_nbrs(r,c,grid,rows,cols):
                new_paths.add(nbr)

        curr_paths = new_paths
        new_paths = set()
    
    # return(curr_paths)
    return len(curr_paths)

def check_nbrs2(r,c,grid,rows,cols):
    downr = (r+1)%rows if r+1 else r+1
    upr = (r-1)%rows if r-1 else r-1
    leftc = (c-1)%cols if c-1 else c-1
    rightc = (c+1)%cols if c+1 else c+1
    
    nbrs = []
    try:
        if grid[upr][c%cols] in '.S':
            nbrs.append((r-1,c))
        if grid[downr][c%cols] in '.S':
            nbrs.append((r+1,c))
        if grid[r%rows][leftc] in '.S':
            nbrs.append((r,c-1))
        if grid[r%rows][rightc] in '.S':
            nbrs.append((r,c+1))
    except:
        print(r,c)
        exit()

    return nbrs

def quad(y, n):
    # why does this work? took it from reddit
    # y = ax2 + bx + c
    # assumes x1, x2, x3 = 0, 1, 2
    # a = (y[2] - (2*y[1]) + y[0]) / 4
    a = (y[2] - (2 * y[1]) + y[0]) // 2

    # so c = y[0] makes sense, i.e. f(x) = y[0] = a(0**2) + b(0) + c
    c = y[0]

    # sub y[0] in for c, then solve for b in terms of a using x=1
    # f(x) = y[1] = a(1**2) + b(1) + y[0]
    # y[1] = a + b + y[0]
    # b = y[1] - y[0] - a
    b = y[1] - y[0] - a
    
    # then put it all together for a
    # but define above, since a is used for b
    # f(x) = y[2] = (2**2)a + 2b + c
    # y[2] = 4a + 2(y[1] - y[0] - a) + y[0]
    # y[2] = 2a + 2y[1] - y[0]
    # 2a = y[2] - 2y[1] + y[0]
    # a = (y[2] - 2y[1] + y[0]) / 2
    
    # a = (y[2] - (2 * y[1]) + y[0]) // 2
    print(y, a, b, c)

    return (a * n**2) + (b * n) + c

def main2(fname, steps):
    with open(fname) as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]

    rows, cols = len(grid), len(grid[0])
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == 'S':
                start = (ridx, cidx)

    curr_paths, new_paths = {start}, set()
    y = []
    for rd in range(1, steps+1):
        for path in curr_paths:
            r,c = path
            for nbr in check_nbrs2(r,c,grid,rows,cols):
                new_paths.add(nbr)

        curr_paths = new_paths
        new_paths = set()

        if rd in (65, 196, 327):
            y.append((len(curr_paths)))
        
        if len(y) > 2:
            return quad(y, (steps-65)//131)

    # return(curr_paths)
    return len(curr_paths)


# print(main('input/test.txt', 6))
# print(main('input/21.txt', 64))

print(main2('input/21.txt', 26501365))
# 26501365
