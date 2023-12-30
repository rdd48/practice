def check_next_sq(p, grid, rows, cols):
    # return a list of any possible new squares
    next_sqs = []
    r,c = p[-1]


    # check down, up, right, left
    # up
    if r > 0:
        if (r-1, c) not in p:
            if grid[r-1][c] == '.':
                next_sqs.append([(r-1, c)])
            elif grid[r-1][c] == '>':
                next_sqs.append([(r-1, c), (r-1, c+1)])
    
    # down
    if r < rows-1:
        if (r+1, c) not in p:
            if grid[r+1][c] == '.':
                next_sqs.append([(r+1, c)])
            elif grid[r+1][c] == '>':
                next_sqs.append([(r+1, c), (r+1, c+1)])
            elif grid[r+1][c] == 'v':
                next_sqs.append([(r+1, c), (r+2, c)])
    
    # left
    if c > 0:
        if (r, c-1) not in p:
            if grid[r][c-1] == '.':
                next_sqs.append([(r, c-1)])
            elif grid[r][c-1] == 'v':
                next_sqs.append([(r, c-1), (r+1, c-1)])
    
    # right
    if c < cols-1:
        if (r, c+1) not in p:
            if grid[r][c+1] == '.':
                next_sqs.append([(r, c+1)])
            elif grid[r][c+1] == '>':
                next_sqs.append([(r, c+1), (r, c+2)])
            elif grid[r][c+1] == 'v':
                next_sqs.append([(r, c+1), (r+1, c+1)])
    
    return next_sqs

def main(fname):
    with open(fname) as f:
        grid = [l.strip() for l in f.readlines() if l.strip()]
    
    rows, cols = len(grid), len(grid[0])
    # manually close the grid at the top
    grid[0] = '#' * cols

    paths, new_paths, finished = [((0,1),(1,1))], [], []

    while True:
        for p in paths:
            if next_sqs := check_next_sq(p, grid, rows, cols):
                for ns in next_sqs:
                    if ns[0][0] == rows-1:
                        finished.append(len((*p, *ns))-1)
                    else:
                        new_paths.append((*p, *ns))
                    # if ns[0][0] == rows-2:
                    #     print(ns)
        
        if not new_paths:

            return max(finished)
        
        paths = new_paths.copy()
        new_paths = []

def check_next_sq2(p, visited, grid, rows, cols):
    # return a list of any possible new squares
    next_sqs = []
    r,c = p

    # check down, up, right, left
    # up
    if r > 0:
        if (r-1, c) not in visited and grid[r-1][c] == '.':
                next_sqs.append((r-1, c))
    
    # down
    if r < rows-1:
        if (r+1, c) not in visited and grid[r+1][c] == '.':
                next_sqs.append((r+1, c))
    
    # left
    if c > 0:
        if (r, c-1) not in visited and grid[r][c-1] == '.':
                next_sqs.append((r, c-1))
    
    # right
    if c < cols-1:
        if (r, c+1) not in visited and grid[r][c+1] == '.':
                next_sqs.append((r, c+1))
    
    return next_sqs

def main2(fname):
    with open(fname) as f:
        grid = [l.strip().replace('>','.').replace('v','.') for l in f.readlines() if l.strip()]
    
    rows, cols = len(grid), len(grid[0])
    # manually close the grid at the top
    grid[0] = '#' * cols

    paths, new_paths = [((1,1), set())], []
    finished = 0
    # longest_paths = {(r,c):0 for r in range(rows) for c in range(cols)}

    while True:
        for p, visited in paths:
            if next_sqs := check_next_sq2(p, visited, grid, rows, cols):
                for ns in next_sqs:
                    if ns[0] == rows-1:
                        print(finished, len(paths))
                        finished = max(finished, len(visited)+2)
                    else:
                        # instead of keeping whole paths, what about keeping (curr, visited)?
                        # if ns in longest_paths:
                        #     if longest_paths[ns] < len(visited)+1:
                        vc = visited.copy()
                        vc.add(p)
                        new_paths.append((ns, vc))

                        # else:
                        #     vc = visited.copy()
                        #     vc.add(p)
                        #     new_paths.append((ns, vc))
                        #     longest_paths[ns] = len(visited)+1
                            
        
        if not new_paths:
            return finished
        
        paths = new_paths.copy()
        new_paths = []
        
print(main2('input/23.txt'))